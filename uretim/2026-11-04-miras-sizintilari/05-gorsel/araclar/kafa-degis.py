#!/usr/bin/env python3
"""Thumbnail Leo kafa değişimi (S03): görsel kolun kafa-sabit pozlarına 1929/paket-v1 ifade kafaları.
Maske ve geçiş thumb-uret.py v2 kafa_degis ile aynı (y_kes 392, yumuşatma 14); fark: alt sınır sert kesim yerine 40 px rampa. dx/dy = kafa-hiza.py kaymasının tersi.
Kullanım: python -I kafa-degis.py → thumb-leo/K*.png + kontakt/thumb-kafa.jpg"""
import numpy as np, pathlib
from PIL import Image, ImageDraw, ImageFilter
B = pathlib.Path(__file__).resolve().parents[1]; L29 = B.parents[1] / "2026-10-26-1929-1000-dolar/05-gorsel/leo"
def kafa_degis(govde, kafa, dx=0, dy=0, y_kes=392, yumus=14):
    k = Image.new("RGBA", govde.size, (0, 0, 0, 0)); k.paste(kafa, (dx, dy))
    m = Image.new("L", govde.size, 0); d = ImageDraw.Draw(m)
    d.ellipse((790 + dx, -60 + dy, 1100 + dx, y_kes + 30 + dy), fill=255); d.rectangle((790 + dx, -60 + dy, 1100 + dx, 200 + dy), fill=255)
    a = np.array(m.filter(ImageFilter.GaussianBlur(yumus))).astype(np.float32) / 255; r0 = y_kes + dy - 10; a[r0:r0 + 40, :] *= np.linspace(1, 0, 40, dtype=np.float32)[:, None]; a[r0 + 40:, :] = 0  # sert kesim yerine 40 px rampa (K1 çene altı basamağı)
    m = Image.fromarray((a * 255).astype(np.uint8)); out = govde.copy()
    out.paste(k, (0, 0), Image.fromarray(np.minimum(np.array(m), np.array(k.split()[3]))))
    al = np.maximum(np.array(govde.split()[3]), (np.array(k.split()[3]) * (np.array(m) / 255)).astype(np.uint8)); out.putalpha(Image.fromarray(al))
    return out
P = lambda p: Image.open(p).convert("RGBA")
IS = [("K1-M06-saskin", "leo/M06.png", L29 / "d-saskin.png", 0, 0),
      ("K1b-M06-notr", "leo/M06.png", L29 / "a-konusma-kapali.png", 0, 0),
      ("K3-M04-dusunen", "leo/M04.png", L29 / "e-dusunen.png", 0, 1),
      ("K3b-M04-notr", "leo/M04.png", L29 / "a-konusma-kapali.png", 0, 1),
      ("K4-M05-saskin", "leo/M05.png", L29 / "d-saskin.png", 0, 1),
      ("K4b-M05-gulumser", "leo/M05.png", L29 / "b-alt-gulumseyerek-konusma.png", 0, 1)]
ks = []
for ad, g, k, dx, dy in IS:
    o = kafa_degis(P(B / g), P(k), dx, dy); o.save(B / "thumb-leo" / f"{ad}.png"); ks.append(o)
kt = Image.new("RGB", (640 * 3, 360 * 2), (12, 78, 88))
for i, o in enumerate(ks):
    t = o.resize((640, 360), Image.LANCZOS); kt.paste(t, (640 * (i % 3), 360 * (i // 3)), t)
kt.save(B / "kontakt" / "thumb-kafa.jpg", quality=88); print(len(ks), "kafa değişimi yazıldı")
