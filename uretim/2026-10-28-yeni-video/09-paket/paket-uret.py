#!/usr/bin/env python3
"""paket.md veri bloklarından 3 yayın paketi üretir (tek kaynak; elle kopyalama yok).
Yayın zamanı, thumbnail ve müzik atfı da tek kaynaktan: paket.md `veri:yayin-zamani`, `veri:thumbnail-ana`,
06-muzik/atif-satirlari.md ({MUZIK_*} belirteçleri; dosya yoksa görünür yer tutucu → paket-kontrol --final hata verir).
Yollar ../ ile: 09-paket/ ve teslim/ kardeş klasör → iki yerden de geçerli. Şema: tools/yayin/yayin_paket.py SEMA.
"""
import json, re, pathlib

BURA = pathlib.Path(__file__).resolve().parent
YER = "[YER TUTUCU: müzik atfı F6 — 06-muzik/atif-satirlari.md]"

def bloklar(s):
    return {k: v.rstrip("\n") for k, v in re.findall(r"<!-- veri:([\w-]+) -->\s*```[^\n]*\n(.*?)```", s, re.S)}

def muzik():
    f = BURA.parent / "06-muzik/atif-satirlari.md"
    if not f.is_file(): return {"MUZIK_UZUN": YER, "MUZIK_SHORTS1": YER, "MUZIK_SHORTS2": YER}
    a = f.read_text(encoding="utf-8")
    m = {"MUZIK_UZUN": re.search(r"```\n(.*?)```", a, re.S).group(1).strip()}
    for n in (1, 2):
        x = re.search(r"Shorts %d açıklaması: `(.+?)`" % n, a)
        m[f"MUZIK_SHORTS{n}"] = x.group(1) if x else YER
    return m

def doldur(t, M):
    for k, v in M.items(): t = t.replace("{%s}" % k, v)
    return t

V = bloklar((BURA / "paket.md").read_text(encoding="utf-8"))
M = muzik()
ZAMAN = dict(l.split("|", 1) for l in V["yayin-zamani"].splitlines() if l.strip())
THUMB = V.get("thumbnail-ana", "").strip() or None
ONERILEN = V["basliklar"].splitlines()[0]
ETIKETLER = [t.strip() for t in V["etiketler"].split(",") if t.strip()]
BOLUMLER = [{"zaman": z, "baslik": b} for z, b in re.findall(r"^(\d{2}:\d{2}) (.+)$", V["bolumler"], re.M)]
SENTETIK = True  # monetizasyon-uyum-uzmani: F3 önerisi true (politika-denetimi P4); F8 politika-raporu.md kesin kararı gelince güncellenir
DURUM = {"gizlilik": "private", "cocuklara_ozel": False, "sentetik_medya": SENTETIK, "lisans": "youtube", "gomulebilir": True}
ONAY = {"niyazi_onayi": False, "tarih": None}
META = {"kategori_id": "27", "varsayilan_dil": "en", "ses_dili": "en"}
SHORTS_ETIKET = {
    1: ["us budget explained", "national debt", "interest on the national debt", "defense spending", "federal budget", "shorts", "toonomy"],
    2: ["national debt", "debt to gdp", "us debt history", "economic history", "post war economy", "shorts", "toonomy"],
}
dosyalar = {"video": "../08-kurgu/final-16x9.mp4", "altyazilar": [{"dosya": "../08-kurgu/final.en.srt", "dil": "en", "ad": "English"}]}
if THUMB: dosyalar["thumbnail"] = THUMB
paketler = {"yayin-paketi.json": {
    "sema": "yayin-paketi/1",
    "_not": f"S08 kitchen-table uzun video (B). paket.md'den paket-uret.py ile üretildi; elle düzenleme yok. Slot {ZAMAN['uzun']} (EST).",
    "tur": "uzun", "dosyalar": dosyalar,
    "metadata": {"baslik": ONERILEN, "aciklama": doldur(V["aciklama"], M), "etiketler": ETIKETLER, "bolumler": BOLUMLER, **META},
    "durum": {**DURUM, "yayin_zamani": ZAMAN["uzun"]},
    "oynatma_listesi_id": None, "onay": dict(ONAY)}}
for n in (1, 2):
    paketler[f"yayin-paketi-shorts-{n}.json"] = {
        "sema": "yayin-paketi/1",
        "_not": f"S08 Shorts {n}. Related video = uzun video (Studio adımı, YAYIN.md). paket-uret.py ile üretildi.",
        "tur": "shorts",
        "dosyalar": {"video": f"../08-kurgu/shorts-{n}.mp4", "altyazilar": []},
        "metadata": {"baslik": V[f"shorts{n}-baslik"], "aciklama": doldur(V[f"shorts{n}-aciklama"], M),
                     "etiketler": SHORTS_ETIKET[n], "bolumler": [], **META},
        "durum": {**DURUM, "yayin_zamani": ZAMAN[f"shorts-{n}"]},
        "oynatma_listesi_id": None, "onay": dict(ONAY)}
for ad, p in paketler.items():
    (BURA / ad).write_text(json.dumps(p, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("yazıldı", ad, "· müzik:", "YER TUTUCU" if YER in json.dumps(p, ensure_ascii=False) else "atif-satirlari.md", "· thumbnail:", p["dosyalar"].get("thumbnail"))
