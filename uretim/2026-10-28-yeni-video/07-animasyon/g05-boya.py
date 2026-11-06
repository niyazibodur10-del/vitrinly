#!/usr/bin/env python3
"""G05 (Leo zarftan zarf çıkarır) zarflarını boyar: dış = faiz kırmızı, iç = BORROWED mor (kraft pikselleri; ten hariç).
Girdi/çıktı leo kırpım koordinatında (varlik-hazirla.py kutusu). Çıktı: video/public/kbutce/leo-G05k.png (+ G05m: iç kırmızı, dış mor
= matruşkanın bir sonraki katmanı). Kullanım: ~/.finansal-arac/venv/bin/python -I .../g05-boya.py"""
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw
KOK = Path(__file__).resolve().parents[3]; P = KOK / "video/public/kbutce"
im = Image.open(P / "leo-G05.png").convert("RGBA"); a = np.array(im).astype(np.float32) / 255
hsv = np.array(im.convert("RGB").convert("HSV")).astype(np.float32) / 255
H, S, V = hsv[..., 0] * 360, hsv[..., 1], hsv[..., 2]
kraft = (H >= 24) & (H <= 46) & (S >= 0.22) & (S <= 0.8) & (V >= 0.25)
kutu = np.zeros(kraft.shape, bool); kutu[505:960, 540:960] = True
kraft &= kutu
ic = Image.new("L", im.size, 0); ImageDraw.Draw(ic).polygon([(600, 515), (848, 492), (874, 700), (790, 744), (735, 750), (606, 714)], fill=255)
ic = np.array(ic) > 0
def boya(maske, rgb):
    hh, ss, vv = Image.new("RGB", (1, 1), rgb).convert("HSV").getpixel((0, 0))
    out = hsv.copy(); out[..., 0][maske] = hh / 255; out[..., 1][maske] = np.clip(S[maske] / 0.45 * ss / 255, 0, 1)
    out[..., 2][maske] = np.clip(V[maske] * (vv / 255) / 0.78, 0, 1)
    return out
KIRMIZI, MOR = (224, 90, 79), (155, 107, 223)
for ad, (dis, icr) in {"G05k": (KIRMIZI, MOR), "G05m": (MOR, KIRMIZI)}.items():
    o = boya(kraft & ~ic, dis); o2 = boya(kraft & ic, icr); o[kraft & ic] = o2[kraft & ic]
    rgb = Image.fromarray((o * 255).astype(np.uint8), "HSV").convert("RGB")
    out = rgb.convert("RGBA"); out.putalpha(im.getchannel("A")); out.save(P / f"leo-{ad}.png", optimize=True)
print("kraft piksel", int(kraft.sum()), "iç", int((kraft & ic).sum()))
