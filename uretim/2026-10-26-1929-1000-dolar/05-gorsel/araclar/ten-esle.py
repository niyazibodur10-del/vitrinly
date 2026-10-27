#!/usr/bin/env python3
"""Kesik Leo'da ten rengini referans pozun yüz tenine eşler (Lab medyan kaydırma, yumuşak maske).
Canva düzenlemesinde ten kayması (ör. C05 kutu yansıması, ΔE 6,5) yeni üretim harcamadan giderilir.
Ten maskesi: HSV H 5-25 (OpenCV), S>60, V>110, alfa>0; --haric x0,y0,x1,y1 dikdörtgeni (ör. karton kutu, ten tonuna yakın) yüz satırları (y<--yuz_alt) dışında hariç.
Kullanım: python -I ten-esle.py <kesik.png> <ref_ham.png> <ref_kafa x0,y0,x1,y1> <kaynak_kafa x0,y0,x1,y1> <cikis.png> [--haric x0,y0,x1,y1 --yuz_alt y]"""
import sys, cv2, numpy as np, json
def skin(img):
    h = cv2.cvtColor(img, cv2.COLOR_BGR2HSV); return (h[..., 0] >= 5) & (h[..., 0] <= 25) & (h[..., 1] > 60) & (h[..., 2] > 110)
def labf(i): return cv2.cvtColor(i, cv2.COLOR_BGR2LAB).astype(np.float32)
a = sys.argv; cut = cv2.imread(a[1], cv2.IMREAD_UNCHANGED); ref = cv2.imread(a[2])
rb = list(map(int, a[3].split(','))); sb = list(map(int, a[4].split(','))); out = a[5]
har = list(map(int, a[a.index('--haric') + 1].split(','))) if '--haric' in a else None
yuz = int(a[a.index('--yuz_alt') + 1]) if '--yuz_alt' in a else 0
img = cut[..., :3]; al = cut[..., 3]
rs = skin(ref); rm = np.zeros_like(rs); rm[rb[1]:rb[3], rb[0]:rb[2]] = True
ss = skin(img) & (al > 200); sm = np.zeros_like(ss); sm[sb[1]:sb[3], sb[0]:sb[2]] = True
dl = np.median(labf(ref)[rs & rm], 0) - np.median(labf(img)[ss & sm], 0)
mask = skin(img) & (al > 0)
if har:
    r = np.zeros_like(mask); r[har[1]:har[3], har[0]:har[2]] = True; r[:yuz] = False; mask &= ~r
mf = cv2.GaussianBlur(mask.astype(np.float32), (0, 0), 1.5)[..., None]
L = labf(img) + dl * mf
res = cut.copy(); res[..., :3] = cv2.cvtColor(np.clip(L, 0, 255).astype(np.uint8), cv2.COLOR_LAB2BGR)
cv2.imwrite(out, res); print(json.dumps({"lab_kaydirma_opencv": [round(float(v), 2) for v in dl], "maske_px": int(mask.sum())}))
