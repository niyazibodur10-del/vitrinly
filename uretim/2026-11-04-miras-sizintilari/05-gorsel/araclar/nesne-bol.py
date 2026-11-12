#!/usr/bin/env python3
"""Nesne sayfasını sütun boşluklarına göre nesnelere böler (kes-m4 tek görselde yalnız en büyük bileşeni tuttuğu için).
Kullanım: python -I nesne-bol.py <sayfa.png> <cikis_oneki> <ad1,ad2,...>  → <onek>-<ad>-ham.png (30 px pay)."""
import sys, cv2, numpy as np
img = cv2.imread(sys.argv[1]); h, w = img.shape[:2]; adlar = sys.argv[3].split(",")
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB).astype(np.float32)
bg = np.median(np.concatenate([lab[:24, :24].reshape(-1, 3), lab[:24, -24:].reshape(-1, 3)]), 0)
m = (np.linalg.norm(lab - bg, axis=2) > 25).astype(np.uint8)
m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
col = m.sum(0) > 3; seg = []; x = 0
while x < w:
    if col[x]:
        s = x
        while x < w and col[x]: x += 1
        if x - s > 40: seg.append((s, x))
    x += 1
# yakın parçaları birleştir (aynı nesnenin ince boşlukları)
bir = [list(seg[0])]
for s, e in seg[1:]:
    if s - bir[-1][1] < 12: bir[-1][1] = e
    else: bir.append([s, e])
assert len(bir) == len(adlar), f"{len(bir)} parça bulundu, {len(adlar)} ad verildi: {bir}"
for (s, e), ad in zip(bir, adlar):
    ys = np.where(m[:, s:e].any(1))[0]; y0, y1 = max(ys[0] - 30, 0), min(ys[-1] + 30, h)
    x0, x1 = max(s - 30, 0), min(e + 30, w)
    cv2.imwrite(f"{sys.argv[2]}-{ad}-ham.png", img[y0:y1, x0:x1]); print(ad, (x0, y0, x1, y1))
