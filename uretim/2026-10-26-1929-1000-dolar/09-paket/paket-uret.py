#!/usr/bin/env python3
"""paket.md veri bloklarından 3 yayın paketi üretir (tek kaynak; elle kopyalama yok).
Çıktı: yayin-paketi.json, yayin-paketi-shorts-1.json, yayin-paketi-shorts-2.json (şema tools/yayin/yayin_paket.py SEMA).
Yollar paket klasörüne göreli ve ../ ile: 09-paket/ ve teslim/ kardeş klasör → iki yerden de geçerli.
"""
import json, re, pathlib

BURA = pathlib.Path(__file__).resolve().parent
s = (BURA / "paket.md").read_text(encoding="utf-8")
V = {k: v.rstrip("\n") for k, v in re.findall(r"<!-- veri:([\w-]+) -->\s*```[^\n]*\n(.*?)```", s, re.S)}

ONERILEN = V["basliklar"].splitlines()[0]
ETIKETLER = [t.strip() for t in V["etiketler"].split(",") if t.strip()]
BOLUMLER = [{"zaman": z, "baslik": b} for z, b in re.findall(r"^(\d{2}:\d{2}) (.+)$", V["bolumler"], re.M)]
SENTETIK = True  # monetizasyon-uyum-uzmani kesin kararı: politika-raporu.md §4
DURUM = {"gizlilik": "private", "cocuklara_ozel": False, "sentetik_medya": SENTETIK, "lisans": "youtube", "gomulebilir": True}
ONAY = {"niyazi_onayi": False, "tarih": None}
META = {"kategori_id": "27", "varsayilan_dil": "en", "ses_dili": "en"}

SHORTS_ETIKET = {
    1: ["1929 stock market crash", "great depression", "1929 crash", "bank runs", "financial history", "shorts", "toonomy"],
    2: ["inflation explained", "deflation explained", "purchasing power", "great depression", "financial history", "shorts", "toonomy"],
}
paketler = {
    "yayin-paketi.json": {
        "sema": "yayin-paketi/1",
        "_not": "1929-1000-dolar uzun video. paket.md'den paket-uret.py ile üretildi; elle düzenleme yok. Slot: Çar 2026-10-28 12:00 ET (EDT, UTC-4; Niyazi onayı 2026-10-28, saat koordinatör).",
        "tur": "uzun",
        "dosyalar": {"video": "../08-kurgu/final-16x9.mp4", "thumbnail": "../09-paket/thumbnail/A2-kapilar.jpg",
                     "altyazilar": [{"dosya": "../08-kurgu/final.en.srt", "dil": "en", "ad": "English"}]},
        "metadata": {"baslik": ONERILEN, "aciklama": V["aciklama"], "etiketler": ETIKETLER, "bolumler": BOLUMLER, **META},
        "durum": {**DURUM, "yayin_zamani": "2026-10-28T12:00:00-04:00"},
        "oynatma_listesi_id": None, "onay": dict(ONAY)},
}
for n, gun in ((1, "2026-11-02T09:00:00-05:00"), (2, "2026-11-03T09:00:00-05:00")):
    paketler[f"yayin-paketi-shorts-{n}.json"] = {
        "sema": "yayin-paketi/1",
        "_not": f"1929-1000-dolar Shorts {n}. Related video = uzun video (Studio adımı, YAYIN.md). paket-uret.py ile üretildi.",
        "tur": "shorts",
        "dosyalar": {"video": f"../08-kurgu/shorts-{n}.mp4", "altyazilar": []},
        "metadata": {"baslik": V[f"shorts{n}-baslik"], "aciklama": V[f"shorts{n}-aciklama"],
                     "etiketler": SHORTS_ETIKET[n], "bolumler": [], **META},
        "durum": {**DURUM, "yayin_zamani": gun},
        "oynatma_listesi_id": None, "onay": dict(ONAY)}

for ad, p in paketler.items():
    (BURA / ad).write_text(json.dumps(p, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print("yazıldı", ad)
