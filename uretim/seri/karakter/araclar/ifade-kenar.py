#!/usr/bin/env python3
"""İfade portresi kenar temizliği (hakem Z3b, gorsel-varlik-sanatcisi 2026-11-11).
Sorun: GrabCut ikili maske + 4,3x büyütme → saç/kulak kenarında tırtık, kopuk uç, kızıl/koyu renk bulaşığı.
Yöntem: (1) kenar bandında (≤20 px) yabancı piksel (doygunluk <0,22: gri zemin halesi) → zemin; (2) alfa>0,5 ikili maske
kapama + açma (elips r=4), en büyük bileşen, delik doldurma; (3) kontur pürüzsüzleştirme Gauss σ3 → eşik; (4) yumuşak kenar σ2;
(5) renk: kenardan ≤8 px içerideki ve dışarıdaki pikseller en yakın "temiz iç" (kenardan >14 px içeri) pikselin rengini alır,
8–14 px arasında yumuşak geçiş → saçağa bulaşan zemin/kızıl/koyu ton saç-ten tonuna çekilir.
Boyut, konum ve gövde (alt kesik) değişmez. Kullanım: python -I ifade-kenar.py <girdi.png> <cikis.png> [<yesil.jpg>]"""
import sys, json, cv2, numpy as np
src, dst = sys.argv[1], sys.argv[2]
im = cv2.imread(src, cv2.IMREAD_UNCHANGED); bgr = im[..., :3].astype(np.float32); a0 = im[..., 3].astype(np.float32) / 255
H, W = a0.shape
hsv = cv2.cvtColor(im[..., :3], cv2.COLOR_BGR2HSV); sat = hsv[..., 1] / 255.0
dolu = a0 > 0.5
def edt(b): return cv2.distanceTransform(b.astype(np.uint8), cv2.DIST_L2, 5)
ic = edt(dolu)
val = hsv[..., 2] / 255.0
ust = np.zeros((H, W), bool); ust[: int(H * 0.55)] = True
yabanci = dolu & (ic <= 20) & (sat < 0.22)
# kafada zemine karışmış tel ucu: soluk (s<0,33) ve ten kadar parlak değil (v<0,80); saç s≥0,45, ten v≥0,8
yabanci |= dolu & ust & (ic <= 24) & (sat < 0.33) & (val < 0.80)
m = dolu & ~yabanci
k = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (9, 9))
m = cv2.morphologyEx(m.astype(np.uint8), cv2.MORPH_CLOSE, k); m = cv2.morphologyEx(m, cv2.MORPH_OPEN, k)
n, lb, st, _ = cv2.connectedComponentsWithStats(m)
if n > 2: m = (lb == 1 + int(np.argmax(st[1:, 4]))).astype(np.uint8)
inv = (1 - m).astype(np.uint8); ff = inv.copy(); msk = np.zeros((H + 2, W + 2), np.uint8)
for (x, y) in [(0, 0), (W - 1, 0)]:
    if ff[y, x]: cv2.floodFill(ff, msk, (x, y), 2)
m = np.where(ff == 1, 1, m).astype(np.uint8)  # kenara bağlı olmayan zemin = delik → doldur
# alt kenar (kart kesiği) ve yanlar: pürüzsüzleştirme sırasında kadraj kenarında aşınma olmasın diye yansıtmalı sınır
ms = cv2.GaussianBlur(m.astype(np.float32), (0, 0), 3, borderType=cv2.BORDER_REPLICATE) > 0.5
a = cv2.GaussianBlur(ms.astype(np.float32), (0, 0), 2, borderType=cv2.BORDER_REPLICATE)
# renk: temiz iç = kenardan >8 px içeride; dışı ve ince bant en yakın temiz iç rengini alır
d_in = edt(ms)
IC, GECIS = 14, 8  # temiz iç: kenardan >14 px; ≤8 px tamamen iç rengi; 8–14 geçiş (4–8 bandı tel uçlarında gri bıraktı)
temiz = d_in > IC
kafa = ust  # kafa bölgesinde temiz iç = doygun (gri karışık tel kaynak olmasın); gövdede şart yok (beyaz tişört)
temiz &= ~kafa | (sat > 0.30)
_, lab = cv2.distanceTransformWithLabels((~temiz).astype(np.uint8), cv2.DIST_L2, 5, labelType=cv2.DIST_LABEL_PIXEL)
ys, xs = np.nonzero(temiz)  # etiketler sıfır piksellerine tarama sırasıyla verilir (assert ile doğrulanır)
assert (lab[ys, xs] == np.arange(1, len(ys) + 1)).all(), "etiket sırası varsayımı tutmadı"
yakin = bgr[ys[lab - 1], xs[lab - 1]]
w = np.clip((d_in - GECIS) / (IC - GECIS), 0, 1)[..., None]  # 0 (≤8 px) → yakın iç rengi, 1 (≥14 px) → özgün
out = bgr * w + yakin * (1 - w)
res = np.dstack([np.clip(out, 0, 255).astype(np.uint8), (np.clip(a, 0, 1) * 255).astype(np.uint8)])
cv2.imwrite(dst, res)
# ölçüm: tırtık = kontur eğrilik yoğunluğu vekili (çevre / pürüzsüz çevre), ada sayısı, yarı saydam saçak alanı
def cevre(b): c, _ = cv2.findContours(b.astype(np.uint8), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE); return sum(cv2.arcLength(x, True) for x in c)
n2 = cv2.connectedComponents((res[..., 3] > 25).astype(np.uint8))[0] - 1
print(json.dumps({"girdi": src, "silinen_yabanci_px": int(yabanci.sum()), "cevre_once": round(cevre(dolu)), "cevre_sonra": round(cevre(ms)),
                  "ada_sayisi": int(n2), "boyut": [W, H]}))
if len(sys.argv) > 3:
    g = np.full((H, W, 3), (60, 200, 60), np.float32); aa = res[..., 3:].astype(np.float32) / 255
    cv2.imwrite(sys.argv[3], (res[..., :3] * aa + g * (1 - aa)).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 92])
