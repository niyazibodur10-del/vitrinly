#!/usr/bin/env python3
"""Düz yeşil zeminli nesne kesimi (B2-G1 bisiklet; gorsel-varlik-sanatcisi 2026-11-12).
M4/kes-gc kapalı delikleri dolduruyor → tel arası küçük yeşil boşluklar kalırdı. Burada delik doldurma YOK:
alfa = yumuşak Lab anahtarı clip((d-10)/14); yeşil sızıntı giderme G ≤ max(R,B) (nesnede yeşil renk yok);
alfa>0,5 bileşenlerinden 300 px'ten küçük olanlar silinir (gürültü). Ölçüm: kalan yeşil px, ada sayısı, kapalı yeşil boşluk sayısı.
Kullanım: python -I kes-yesil.py <girdi.png> <cikis_rgba.png> [<onizleme.jpg>]"""
import sys, json, cv2, numpy as np
def lab(i): return cv2.cvtColor(i, cv2.COLOR_BGR2LAB).astype(np.float32) * np.array([100/255, 1, 1], np.float32) - np.array([0, 128, 128], np.float32)
im = cv2.imread(sys.argv[1]); H, W = im.shape[:2]
kenar = np.concatenate([im[:20].reshape(-1, 3), im[-20:].reshape(-1, 3), im[:, :20].reshape(-1, 3), im[:, -20:].reshape(-1, 3)])
bg = np.median(kenar, 0); d = np.linalg.norm(lab(im) - lab(bg.reshape(1, 1, 3).astype(np.uint8))[0, 0], axis=2)
a = np.clip((d - 10) / 14, 0, 1)
n, lb, st, _ = cv2.connectedComponentsWithStats((a > 0.5).astype(np.uint8))
kucuk = np.isin(lb, [i for i in range(1, n) if st[i, 4] < 300]); a[kucuk] = 0
b, g, r = [im[..., i].astype(np.float32) for i in range(3)]
g2 = np.minimum(g, np.maximum(r, b)); out = np.dstack([b, g2, r]).clip(0, 255).astype(np.uint8)
rgba = np.dstack([out, (a * 255).astype(np.uint8)]); cv2.imwrite(sys.argv[2], rgba)
yesil_kalan = int(((a > 0.5) & (g > np.maximum(r, b) + 25)).sum())
n2 = cv2.connectedComponents((a > 0.5).astype(np.uint8))[0] - 1
ys, xs = np.nonzero(a > 0.5)
print(json.dumps({"girdi": sys.argv[1], "zemin_bgr": bg.tolist(), "on_plan_px": int((a > 0.5).sum()), "ada": n2, "silinen_kucuk_ada": int(kucuk.sum()),
                  "yesil_kalan_px": yesil_kalan, "bbox": [int(xs.min()), int(ys.min()), int(xs.max()), int(ys.max())]}))
if len(sys.argv) > 3:
    al = a[..., None]; gri = np.full_like(out, 128, np.float32)
    cv2.imwrite(sys.argv[3], (out * al + gri * (1 - al)).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 92])
