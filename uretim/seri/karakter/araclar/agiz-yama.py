#!/usr/bin/env python3
"""Ağız durumları: kapalı (taban) + açık (EDIT) → yama PNG'leri: kapali, yari (optik akış t=0,5 ara kare), acik.
(gorsel-varlik-sanatcisi 2026-11-10; Leo rig-yama.py'den: fark maskesi +11 px, Gauss 4,5, 6 px kutu rampası; bölge parametreli.)
Hiza testi: bölge dışı ham fark (>30) oranı ≤ %1 (düzenleme yüzün geri kalanını oynatmadı mı); dikiş halkası farkı; geri kurma hatası.
--ayna: çıktılar yatay aynalanır (Mike tabanı aynalı kullanılıyor), konum x' = W - x - w.
Kullanım: python -I agiz-yama.py <kapali.png> <acik.png> <x0,y0,x1,y1> <cikis_klasoru> <onek> [--ayna]"""
import sys, os, json, cv2, numpy as np
k = cv2.imread(sys.argv[1]); o = cv2.imread(sys.argv[2]); x0, y0, x1, y1 = map(int, sys.argv[3].split(",")); out, on = sys.argv[4], sys.argv[5]
ayna = "--ayna" in sys.argv; os.makedirs(out, exist_ok=True); H, W = k.shape[:2]
assert o.shape == k.shape, f"boyut farklı {o.shape} {k.shape}"
d = np.abs(k.astype(int) - o.astype(int)).max(2); raw = (d > 30).astype(np.uint8)
op = cv2.morphologyEx(raw, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
zone = np.zeros_like(raw); zone[y0:y1, x0:x1] = 1
dis = float((raw & (1 - zone)).sum() / raw.size)
ys, xs = np.where(op & zone); assert len(xs), "bölgede fark yok"
bx0, by0, bx1, by1 = max(xs.min() - 14, 0), max(ys.min() - 14, 0), min(xs.max() + 15, W), min(ys.max() + 15, H)
m = cv2.dilate((op & zone).astype(np.uint8), np.ones((11, 11), np.uint8)).astype(np.float32)
m = cv2.GaussianBlur(m, (0, 0), 4.5)[by0:by1, bx0:bx1]
ramp = np.ones_like(m); r = 6
for i in range(r):
    v = i / r; ramp[i, :] = np.minimum(ramp[i, :], v); ramp[-1 - i, :] = np.minimum(ramp[-1 - i, :], v); ramp[:, i] = np.minimum(ramp[:, i], v); ramp[:, -1 - i] = np.minimum(ramp[:, -1 - i], v)
al = np.clip(m * 1.6, 0, 1) * ramp
ring = np.ones((by1 - by0, bx1 - bx0), bool); ring[3:-3, 3:-3] = False; dikis = float(raw[by0:by1, bx0:bx1][ring].mean())
# yarı: DIS optik akış ile kapalı↔açık ara kare (t=0,5), kutu + 24 px bağlamla
p = 24; cx0, cy0, cx1, cy1 = max(bx0 - p, 0), max(by0 - p, 0), min(bx1 + p, W), min(by1 + p, H)
kk, oo = k[cy0:cy1, cx0:cx1], o[cy0:cy1, cx0:cx1]
dis_ = cv2.DISOpticalFlow_create(cv2.DISOPTICAL_FLOW_PRESET_MEDIUM)
f_ko = dis_.calc(cv2.cvtColor(kk, cv2.COLOR_BGR2GRAY), cv2.cvtColor(oo, cv2.COLOR_BGR2GRAY), None)
f_ok = dis_.calc(cv2.cvtColor(oo, cv2.COLOR_BGR2GRAY), cv2.cvtColor(kk, cv2.COLOR_BGR2GRAY), None)
gy, gx = np.mgrid[0:kk.shape[0], 0:kk.shape[1]].astype(np.float32)
wk = cv2.remap(kk, gx - 0.5 * f_ko[..., 0], gy - 0.5 * f_ko[..., 1], cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
wo = cv2.remap(oo, gx - 0.5 * f_ok[..., 0], gy - 0.5 * f_ok[..., 1], cv2.INTER_LINEAR, borderMode=cv2.BORDER_REPLICATE)
yari_tam = k.copy(); yari_tam[cy0:cy1, cx0:cx1] = (0.5 * wk.astype(np.float32) + 0.5 * wo.astype(np.float32)).astype(np.uint8)
res = {}
for ad, src in [("kapali", k), ("yari", yari_tam), ("acik", o)]:
    rgba = cv2.cvtColor(src[by0:by1, bx0:bx1], cv2.COLOR_BGR2BGRA); rgba[..., 3] = (al * 255).astype(np.uint8)
    if ayna: rgba = cv2.flip(rgba, 1)
    cv2.imwrite(os.path.join(out, f"{on}-agiz-{ad}.png"), rgba)
rec = k.astype(np.float32).copy(); rec[by0:by1, bx0:bx1] = o[by0:by1, bx0:bx1] * al[..., None] + k[by0:by1, bx0:bx1] * (1 - al[..., None])
e = float(np.abs(rec[by0:by1, bx0:bx1] - o[by0:by1, bx0:bx1]).max(2)[op[by0:by1, bx0:bx1] > 0].mean())
X = W - bx1 if ayna else bx0
J = {"kapali": sys.argv[1], "acik": sys.argv[2], "konum_xy": [int(X), int(by0)], "boyut_wh": [int(bx1 - bx0), int(by1 - by0)], "aynali": ayna,
     "bolge_disi_ham_%": round(dis * 100, 3), "dikis_halka_%": round(dikis * 100, 2), "geri_kurma_degisen_px_ort_abs": round(e, 2),
     "kabul_hiza": dis <= 0.01}
json.dump(J, open(os.path.join(out, f"{on}-agiz.json"), "w"), ensure_ascii=False, indent=1); print(json.dumps(J, ensure_ascii=False))
