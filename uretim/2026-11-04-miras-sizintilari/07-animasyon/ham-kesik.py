#!/usr/bin/env python3
"""GEÇİCİ kesik (animasyon-yonetmeni, F5 kritik test): Canva ham PNG'lerinin düz mavi zemini renk uzaklığıyla saydamlaştırılır.
gorsel-varlik-sanatcisi'nin gerçek kesikleri (05-gorsel/leo/, nesne/) gelince bunların yerine geçer; dosya adları "ham-" önekli.
Ayrıca M08 (yol) ve M09 (kasa içi) plakaları jpg olarak public/kmiras'a kopyalanır.
Kullanım (repo kökü): python3 -I uretim/2026-11-04-miras-sizintilari/07-animasyon/ham-kesik.py"""
from pathlib import Path
import numpy as np
from PIL import Image

KOK = Path(__file__).resolve().parents[3]
HAM = KOK / "uretim/2026-11-04-miras-sizintilari/05-gorsel/canva-ham"
OUT = KOK / "video/public/kmiras"
OUT.mkdir(parents=True, exist_ok=True)
# (kaynak, kırpım kutusu x0,y0,x1,y1 | None, çıktı adı)
KESIK = [
    ("M01", (790, 250, 1430, 860), "ham-kamyon-arka"),
    ("M01", (0, 250, 800, 860), "ham-kamyon-yan"),
    ("M04", None, "ham-leo-pano"),
    ("M05", None, "ham-leo-bant"),
    ("M07", None, "ham-leo-rulo"),
]


def kes(src, kutu, ad):
    im = np.asarray(Image.open(HAM / f"{src}.png").convert("RGB")).astype(np.float32)
    kenar = np.concatenate([im[:8].reshape(-1, 3), im[-8:].reshape(-1, 3), im[:, :8].reshape(-1, 3), im[:, -8:].reshape(-1, 3)])
    zemin = np.median(kenar, axis=0)
    d = np.sqrt(((im - zemin) ** 2).sum(-1))
    a = np.clip((d - 18) / 22, 0, 1)  # 18 altı tam saydam, 40 üstü tam opak
    rgba = np.dstack([im, a * 255]).astype(np.uint8)
    if kutu:
        x0, y0, x1, y1 = kutu
        rgba = rgba[y0:y1, x0:x1]
    ys, xs = np.where(rgba[..., 3] > 40)
    rgba = rgba[max(0, ys.min() - 4): ys.max() + 5, max(0, xs.min() - 4): xs.max() + 5]
    Image.fromarray(rgba).save(OUT / f"{ad}.png")
    return ad, rgba.shape[1], rgba.shape[0], [int(v) for v in zemin]


# gorsel-varlik-sanatcisi'nin gerçek kesikleri (05-gorsel/nesne, leo) varsa onlar kullanılır (bbox'a kırpılır), yoksa geçici renk anahtarı
GERCEK = {"ham-kamyon-arka": "nesne/M01-arka-acik.png", "ham-kamyon-yan": "nesne/M01-yan.png", "ham-leo-pano": "leo/M04.png", "ham-leo-bant": "leo/M05.png", "ham-leo-rulo": "leo/M07.png"}
GV = KOK / "uretim/2026-11-04-miras-sizintilari/05-gorsel"
for s in KESIK:
    g = GV / GERCEK[s[2]]
    if g.exists():
        im = Image.open(g).convert("RGBA"); bb = im.getchannel("A").point(lambda v: 255 if v > 40 else 0).getbbox()
        im.crop(bb).save(OUT / f"{s[2]}.png"); print(s[2], "gerçek kesik", g.name, im.crop(bb).size)
    else:
        print(*kes(*s))
for src, ad in (("M08", "M08"), ("M09", "M09")):
    Image.open(HAM / f"{src}.png").convert("RGB").save(OUT / f"{ad}.jpg", quality=90)
    print(ad, "jpg")
