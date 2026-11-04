#!/usr/bin/env python3
"""paket.md veri bloklarından 3 yayın paketi üretir (tek kaynak; elle JSON yok) — S03 miras sızıntıları.
Kaynak S08 paket-uret.py (2026-10-28 klasörü); eklenenler: {YASAL_NOT} (F3 rakam-tablosu varsa oradan birebir, yoksa
paket.md veri:yasal-not), {KAYNAK_F3} (rakam-tablosu "Kaynaklar (açıklama)" bloğu; yoksa görünür yer tutucu),
Shorts `ilgili_video` alanı (Data API'de karşılığı yok → Studio; uretim-muhendisi talebi), Shorts 2 yedek blok seçimi
(SHORTS2 = "asil" | "yedek"; D4 kararı). Yollar ../ ile (09-paket/ ve teslim/ kardeş). Şema: tools/yayin/yayin_paket.py SEMA.
"""
import json, re, pathlib

BURA = pathlib.Path(__file__).resolve().parent
KLAS = BURA.parent
YER = "[YER TUTUCU: müzik atfı F6 — 06-muzik/atif-satirlari.md]"
YER_KAYNAK = "[YER TUTUCU: F3 birincil kaynaklar — 03-metin/rakam-tablosu.md]"
SHORTS2 = "asil"  # D4 (%47/%55) teyit edilmezse "yedek" (finans-dogrulayici F3)
SENTETIK = True   # monetizasyon-uyum-uzmani: politika-raporu.md kararı gelene kadar geçici true (1929, S08 emsali)

def bloklar(s):
    return {k: v.rstrip("\n") for k, v in re.findall(r"<!-- veri:([\w-]+) -->\s*```[^\n]*\n(.*?)```", s, re.S)}

def muzik():
    f = KLAS / "06-muzik/atif-satirlari.md"
    if not f.is_file(): return {"MUZIK_UZUN": YER, "MUZIK_SHORTS1": YER, "MUZIK_SHORTS2": YER}
    a = f.read_text(encoding="utf-8")
    m = {"MUZIK_UZUN": re.search(r"```\n(.*?)```", a, re.S).group(1).strip()}
    for n in (1, 2):
        x = re.search(r"Shorts %d açıklaması: `(.+?)`" % n, a)
        m[f"MUZIK_SHORTS{n}"] = x.group(1) if x else YER
    return m

def f3(V):
    """Yasal not ve ek kaynaklar: F3 rakam-tablosu.md varsa oradan (birebir), yoksa taslak + yer tutucu."""
    rt = KLAS / "03-metin/rakam-tablosu.md"
    yasal, kaynak, kip = V["yasal-not"], YER_KAYNAK, "taslak"
    if rt.is_file():
        t = rt.read_text(encoding="utf-8")
        y = re.search(r"\*\*Yasal not \(açıklama\):\*\* \"(.+?)\"", t)
        k = re.search(r"Kaynaklar \(açıklama\).*?```[^\n]*\n(.*?)```", t, re.S)
        if y: yasal, kip = y.group(1), "rakam-tablosu"
        if k: kaynak = k.group(1).strip()
    return {"YASAL_NOT": yasal, "KAYNAK_F3": kaynak}, kip

def doldur(t, M):
    for k, v in M.items(): t = t.replace("{%s}" % k, v)
    return t

V = bloklar((BURA / "paket.md").read_text(encoding="utf-8"))
F3, F3_KIP = f3(V)
M = {**muzik(), **F3}
ZAMAN = dict(l.split("|", 1) for l in V["yayin-zamani"].splitlines() if l.strip())
THUMB = V.get("thumbnail-ana", "").strip() or None
ONERILEN = V["basliklar"].splitlines()[0]
ETIKETLER = [t.strip() for t in V["etiketler"].split(",") if t.strip()]
BOLUMLER = [{"zaman": z, "baslik": b} for z, b in re.findall(r"^(\d{2}:\d{2}) (.+)$", V["bolumler"], re.M)]
S2 = "shorts2" if SHORTS2 == "asil" else "shorts2-yedek"
DURUM = {"gizlilik": "private", "cocuklara_ozel": False, "sentetik_medya": SENTETIK, "lisans": "youtube", "gomulebilir": True}
ONAY = {"niyazi_onayi": False, "tarih": None}
META = {"kategori_id": "27", "varsayilan_dil": "en", "ses_dili": "en"}
SHORTS_ETIKET = {
    1: ["great wealth transfer", "baby boomer inheritance", "inheritance explained", "wealth transfer", "heirs", "shorts", "toonomy"],
    2: (["inheritance", "charitable giving", "family philanthropy", "great wealth transfer", "heirs", "shorts", "toonomy"] if SHORTS2 == "asil"
        else ["inheritance", "spouse inheritance", "great wealth transfer", "baby boomer inheritance", "heirs", "shorts", "toonomy"]),
}
ILGILI = {"baslik": ONERILEN, "video_id": None,
          "uygulama": "Studio > Shorts > Ayrıntılar > Related video (Data API v3 videos kaynağında alan yok, 2026-11-04)"}
dosyalar = {"video": "../08-kurgu/final-16x9.mp4", "altyazilar": [{"dosya": "../08-kurgu/final.en.srt", "dil": "en", "ad": "English"}]}
if THUMB: dosyalar["thumbnail"] = THUMB
paketler = {"yayin-paketi.json": {
    "sema": "yayin-paketi/1",
    "_not": f"S03 miras sızıntıları uzun video (C). paket.md'den paket-uret.py ile üretildi; elle düzenleme yok. Slot {ZAMAN['uzun']} (EST). Yasal not: {F3_KIP}.",
    "tur": "uzun", "dosyalar": dosyalar,
    "metadata": {"baslik": ONERILEN, "aciklama": doldur(V["aciklama"], M), "etiketler": ETIKETLER, "bolumler": BOLUMLER, **META},
    "durum": {**DURUM, "yayin_zamani": ZAMAN["uzun"]},
    "oynatma_listesi_id": None, "onay": dict(ONAY)}}
for n, blok in ((1, "shorts1"), (2, S2)):
    paketler[f"yayin-paketi-shorts-{n}.json"] = {
        "sema": "yayin-paketi/1",
        "_not": f"S03 Shorts {n} ({blok}). ilgili_video = uzun video (Studio adımı, YAYIN.md). paket-uret.py ile üretildi.",
        "tur": "shorts",
        "dosyalar": {"video": f"../08-kurgu/shorts-{n}.mp4", "altyazilar": []},
        "metadata": {"baslik": V[f"{blok}-baslik"], "aciklama": doldur(V[f"{blok}-aciklama"], M),
                     "etiketler": SHORTS_ETIKET[n], "bolumler": [], **META},
        "durum": {**DURUM, "yayin_zamani": ZAMAN[f"shorts-{n}"]},
        "ilgili_video": dict(ILGILI),
        "oynatma_listesi_id": None, "onay": dict(ONAY)}
for ad, p in paketler.items():
    (BURA / ad).write_text(json.dumps(p, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    j = json.dumps(p, ensure_ascii=False)
    print("yazıldı", ad, "· müzik:", "YER TUTUCU" if YER in j else "atif-satirlari.md", "· kaynak:", "YER TUTUCU" if YER_KAYNAK in j else ("F3" if "KAYNAK_F3" in V["aciklama"] and ad == "yayin-paketi.json" else "—"),
          "· yasal:", F3_KIP, "· thumbnail:", p["dosyalar"].get("thumbnail"))
