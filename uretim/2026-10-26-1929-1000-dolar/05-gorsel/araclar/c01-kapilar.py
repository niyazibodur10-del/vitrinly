#!/usr/bin/env python3
"""C01 stüdyo plakası ölçümü: kapı bbox'ları (HSV renk segmentasyonu), kapı başına medyan H (derece),
levha alanları (kapı üstü altın çerçeve iç bölgesi), levha içi kenar yoğunluğu (yazı vekili: Canny piksel oranı),
merkez %80 kontrolü. Kullanım: python -I c01-kapilar.py <C01.png> <cikti.json> [<kirpim_kontak.jpg>]"""
import sys, json, cv2, numpy as np
img = cv2.imread(sys.argv[1]); H, W = img.shape[:2]
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV); h = hsv[..., 0].astype(int) * 2; s = hsv[..., 1]; v = hsv[..., 2]
rng = {"mavi": (190, 240), "yesil": (90, 160), "kahve": (15, 40)}
out = {"boyut": [W, H], "kapilar": {}, "levhalar": {}}
band = np.zeros((H, W), bool); band[int(.25 * H):int(.72 * H), int(.2 * W):int(.8 * W)] = True  # kapı kuşağı (yansıma hariç)
for ad, (lo, hi) in rng.items():
    m = ((h >= lo) & (h <= hi) & (s > 90) & (v > 50) & band).astype(np.uint8)
    m = cv2.morphologyEx(m, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
    n, lb, st, _ = cv2.connectedComponentsWithStats(m)
    k = 1 + np.argmax(st[1:, 4]); x, y, w, hh, a = st[k]
    sel = lb == k
    # dış kasa: aynı ton, gevşek eşik, panel kutusunun ±45 px çevresi (alt sınır panel altı: zemin yansıması hariç)
    loose = ((h >= lo) & (h <= hi) & (s > 60) & (v > 35)).astype(np.uint8)
    ly0, ly1, lx0, lx1 = max(y - 45, 0), min(y + hh + 4, H), max(x - 45, 0), min(x + w + 45, W)
    lm = cv2.morphologyEx(loose[ly0:ly1, lx0:lx1], cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    yy, xx = np.where(lm > 0); dis = [int(lx0 + xx.min()), int(ly0 + yy.min()), int(lx0 + xx.max()), int(ly0 + yy.max())]
    out["kapilar"][ad] = {"dis_kasa_xyxy": dis, "panel_bbox_xywh": [int(x), int(y), int(w), int(hh)], "alan_px": int(a),
                          "medyan_H_derece": float(np.median(h[sel])), "medyan_S": float(np.median(s[sel])),
                          "aralik": [lo, hi], "aralikta": bool(lo <= np.median(h[sel]) <= hi),
                          "merkez80_icinde": bool(x >= .1 * W and x + w <= .9 * W and y >= .1 * H and y + hh <= .9 * H)}
# levhalar: kapı üstündeki altın çerçeve (H 25-50, S>100, V>120) -> iç dikdörtgen
gold = ((h >= 20) & (h <= 55) & (s > 90) & (v > 110)).astype(np.uint8)
crops = []
for ad, d in out["kapilar"].items():
    x, y, w, hh = d["panel_bbox_xywh"]
    roi = gold[max(y - 140, 0):y - 40, x - 20:x + w + 20]  # kapı kasası (~y-30) hariç
    ys, xs = np.where(roi > 0)
    gx0, gy0 = x - 20 + xs.min(), max(y - 140, 0) + ys.min(); gx1, gy1 = x - 20 + xs.max(), max(y - 140, 0) + ys.max()
    ix0, iy0, ix1, iy1 = gx0 + 10, gy0 + 10, gx1 - 10, gy1 - 10  # çerçeve kalınlığı ~8 px
    inner = img[iy0:iy1, ix0:ix1]; g = cv2.cvtColor(inner, cv2.COLOR_BGR2GRAY)
    ed = cv2.Canny(g, 40, 120); dens = float((ed > 0).mean())
    out["levhalar"][ad] = {"cerceve_xyxy": [int(gx0), int(gy0), int(gx1), int(gy1)], "ic_alan_xyxy": [int(ix0), int(iy0), int(ix1), int(iy1)],
                           "ic_kenar_yogunlugu": round(dens, 4), "ic_gri_std": round(float(g.std()), 2), "bos": dens < 0.01}
    crops.append(cv2.resize(img[gy0 - 10:gy1 + 10, gx0 - 10:gx1 + 10], None, fx=2, fy=2, interpolation=cv2.INTER_NEAREST))
out["merkez80"] = [int(.1 * W), int(.1 * H), int(.9 * W), int(.9 * H)]
json.dump(out, open(sys.argv[2], "w"), ensure_ascii=False, indent=1); print(json.dumps(out, ensure_ascii=False, indent=1))
if len(sys.argv) > 3:
    hmax = max(c.shape[0] for c in crops)
    cv2.imwrite(sys.argv[3], np.hstack([cv2.copyMakeBorder(c, 0, hmax - c.shape[0], 0, 6, cv2.BORDER_CONSTANT) for c in crops]))
