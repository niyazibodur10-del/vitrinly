#!/usr/bin/env python3
"""Mike ifade portrelerinde saç kenarındaki açık/gri hale lekelerini koddan temizler (hakem Z3, 2026-11-11).
Yeni görsel üretmez: aynı PNG'nin kenar bandında (saydamlığa ≤28 px, y < 760) saç/ten renginde OLMAYAN
(doygunluk < 0,28 ya da ton 5–55° dışı) pikselleri saydam yapar, alfa kenarını 0,8 px yumuşatır. Çıktı *-temiz.png.
Kullanım: ~/.finansal-arac/earshot-venv/bin/python sac-hale-temizle.py <girdi.png>... (çıktı aynı klasöre)
"""
import sys
import numpy as np
from PIL import Image
from scipy import ndimage

for yol in sys.argv[1:]:
    im = np.asarray(Image.open(yol).convert("RGBA")).astype(float)
    rgb, a = im[..., :3] / 255, im[..., 3] / 255
    mx, mn = rgb.max(-1), rgb.min(-1)
    sat = (mx - mn) / np.maximum(mx, 1e-6)
    d = mx - mn + 1e-6
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    ton = np.where(mx == r, ((g - b) / d) % 6, np.where(mx == g, (b - r) / d + 2, (r - g) / d + 4)) * 60
    dolu = a > 0.05
    uzak = ndimage.distance_transform_edt(dolu)
    yy = np.arange(a.shape[0])[:, None] * np.ones_like(a)
    bant = dolu & (uzak <= 28) & (yy < 760)
    yabanci = (sat < 0.28) | (ton < 5) | (ton > 55)
    yabanci |= (yy < 520) & ((sat < 0.4) | (ton > 45))  # saç tepesi: daha sıkı (halkalar)
    sil = bant & yabanci
    sil = ndimage.binary_dilation(sil, iterations=1) & bant
    a2 = np.where(sil, 0, a)
    # küçük ada/delik temizliği ve yumuşak kenar
    m = ndimage.binary_opening(a2 > 0.5, iterations=1)
    etk, n = ndimage.label(m)
    if n > 1:  # yalnız en büyük gövde (kopuk lekeler gider)
        m = etk == (1 + int(np.argmax(ndimage.sum(m, etk, range(1, n + 1)))))
    m = np.where(bant, ndimage.binary_erosion(m, iterations=1), m)  # bantta 1 px içeri: açık saçak gider
    a3 = np.minimum(a2, ndimage.gaussian_filter(m.astype(float), 0.8))
    a3 = np.where(yy >= 760, a, a3)
    out = np.dstack([im[..., :3], a3 * 255]).round().clip(0, 255).astype(np.uint8)
    cik = yol.replace(".png", "-temiz.png")
    Image.fromarray(out, "RGBA").save(cik, optimize=True)
    print(cik, "silinen px:", int(sil.sum()))
