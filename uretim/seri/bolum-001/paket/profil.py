#!/usr/bin/env python3
"""Kanal profil resmi önerisi: videodaki takip kartının geçici logosu (video/src/seri/Kartlar.tsx GeciciLogo) birebir, 800x800 PNG.
Profil resmi ile videodaki "FOLLOW" kartındaki avatar aynı olsun diye. Kullanım: python3 profil.py <cikis.png>"""
import sys
from PIL import Image, ImageDraw
S = 3200; k = S / 100
ALTIN, JAKE, MIKE = (255, 201, 60), (77, 168, 255), (255, 90, 78)
im = Image.new("RGBA", (S, S), (12, 14, 22, 255)); d = ImageDraw.Draw(im)  # koyu zemin: platform daire kırpımında kenar temiz
d.ellipse((2 * k, 2 * k, 98 * k, 98 * k), fill=ALTIN)
ic = Image.new("RGBA", (S, S), (0, 0, 0, 0)); di = ImageDraw.Draw(ic)
di.polygon([(0, 0), (S, 0), (0, S)], fill=JAKE); di.polygon([(S, 0), (S, S), (0, S)], fill=MIKE)
maske = Image.new("L", (S, S), 0); ImageDraw.Draw(maske).ellipse((6 * k, 6 * k, 94 * k, 94 * k), fill=255)
im.paste(ic, (0, 0), maske)
w = int(11 * k); pts = [(27 * k, 52 * k), (43 * k, 68 * k), (74 * k, 34 * k)]
d.line(pts, fill="white", width=w, joint="curve")
for x, y in (pts[0], pts[2]): d.ellipse((x - w / 2, y - w / 2, x + w / 2, y + w / 2), fill="white")
im.resize((800, 800), Image.LANCZOS).save(sys.argv[1])
print("ok", sys.argv[1])
