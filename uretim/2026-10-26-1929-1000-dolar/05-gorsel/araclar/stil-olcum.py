#!/usr/bin/env python3
"""Plaka stil ölçümü (Leo kesiğiyle çizim dili uyumu için vekil metrikler; gorsel-varlik-sanatcisi 2026-10-27).
  kontur  = siyah-şapka (blackhat 7x7) > 28 olan koyu ince çizgi piksel oranı (%)
  duzluk  = 3x3 bulanıklık sonrası Sobel büyüklüğü < 6 olan piksel oranı (%) — cel-shading düz alanları
  doku    = 7x7 yerel gri std medyanı — boyamsı/fotoğrafsı doku göstergesi (düşük = düz boyama)
  doygunluk = HSV S medyanı
Leo kesiği için yalnız alfa>0.9 iç pikselleri ölçülür. Kullanım: python -I stil-olcum.py <png>..."""
import sys, json, cv2, numpy as np
def meas(p):
    im = cv2.imread(p, cv2.IMREAD_UNCHANGED); m = None
    if im.shape[2] == 4: m = im[..., 3] > 230; im = im[..., :3]
    m = np.ones(im.shape[:2], bool) if m is None else cv2.erode(m.astype(np.uint8), np.ones((9, 9), np.uint8)) > 0
    g = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    bh = cv2.morphologyEx(g, cv2.MORPH_BLACKHAT, np.ones((7, 7), np.uint8))
    gb = cv2.GaussianBlur(g, (3, 3), 0).astype(np.float32)
    mag = cv2.magnitude(cv2.Sobel(gb, cv2.CV_32F, 1, 0), cv2.Sobel(gb, cv2.CV_32F, 0, 1))
    mu = cv2.blur(gb, (7, 7)); sd = np.sqrt(np.maximum(cv2.blur(gb * gb, (7, 7)) - mu * mu, 0))
    s = cv2.cvtColor(im, cv2.COLOR_BGR2HSV)[..., 1]
    return {"kontur_%": round(float((bh[m] > 28).mean() * 100), 2), "duzluk_%": round(float((mag[m] < 6).mean() * 100), 1),
            "doku_std_med": round(float(np.median(sd[m])), 2), "doygunluk_med": int(np.median(s[m]))}
if __name__ == "__main__":
    r = {p.split('/')[-1]: meas(p) for p in sys.argv[1:]}
    for k, v in r.items(): print(f"{k:26} {v}")
