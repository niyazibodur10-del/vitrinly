#!/usr/bin/env python3
"""Bölüm 1 L1-A yerleşimi: tezgâh ön katmanı + ikili/tekli bindirme testi + yerlesim.json (gorsel-varlik-sanatcisi 2026-11-10).
Kesik tabanlar kadraj kenarında kesik (kol), bu yüzden: tekli çekimde ölçek 1 (kesik kenar = kadraj kenarı); ikilide Mike (aynalı) solda
dış kenarı kadraj solunda, Jake sağda önde (ölçek büyük) ve sol omzu Mike'ın iç kol kesiğini örter. Arama: Jake ölçeği/x için kesik
kenarın açıkta kalan piksel sayısı = 0 olan en küçük örtüşme.
Kullanım: python -I yerlesim.py <L1-A.png> <jake_rgba> <mike_rgba_aynali> <cikis_klasoru> <onizleme_klasoru>"""
import sys, os, json, cv2, numpy as np
P, J, M, OUT, ON = sys.argv[1:6]; os.makedirs(OUT, exist_ok=True); os.makedirs(ON, exist_ok=True)
pl = cv2.imread(P); H, W = pl.shape[:2]; YC = 1186  # tezgâh arka kenarı (sütun taraması 1179–1191 + göz)
# tezgâh ön katmanı: y>=YC tam; sol uçtaki kâse + kupa GrabCut ile
al = np.zeros((H, W), np.float32); al[YC:] = 1
# kâse + kupa (sol uç): elle çizilmiş olası bölge + çekirdek tohumlu GrabCut (dikdörtgen başlatma blok verdi → elendi)
gm = np.full((H, W), cv2.GC_BGD, np.uint8); ob = np.zeros((H, W), np.uint8)
kase = np.array([[0, 1046], [45, 1062], [85, 1082], [100, 1110], [96, 1160], [80, 1220], [50, 1262], [0, 1270]], np.int32)
cv2.fillPoly(ob, [kase], 1); cv2.rectangle(ob, (103, 1106), (214, 1276), 1, -1); cv2.ellipse(ob, (228, 1186), (28, 48), 0, 0, 360, 1, -1)
gm[cv2.dilate(ob, np.ones((17, 17), np.uint8)) > 0] = cv2.GC_PR_BGD; gm[ob > 0] = cv2.GC_PR_FGD
cv2.rectangle(gm, (120, 1135), (198, 1265), int(cv2.GC_FGD), -1); cv2.fillPoly(gm, [np.array([[0, 1075], [60, 1090], [70, 1200], [0, 1240]], np.int32)], int(cv2.GC_FGD))
b = np.zeros((1, 65)); f = np.zeros((1, 65)); cv2.grabCut(pl, gm, None, b, f, 6, cv2.GC_INIT_WITH_MASK)
obj = ((gm == 1) | (gm == 3)).astype(np.uint8); obj = cv2.morphologyEx(obj, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8)); al = np.maximum(al, obj.astype(np.float32))
al = cv2.GaussianBlur(al, (0, 0), 1.0); al[YC + 3:] = 1
cv2.imwrite(f"{OUT}/L1-A-tezgah-on.png", np.dstack([pl, (al * 255).astype(np.uint8)]))
def yuk(p): i = cv2.imread(p, cv2.IMREAD_UNCHANGED); return i[..., :3].astype(np.float32), i[..., 3].astype(np.float32) / 255
jc, ja = yuk(J); mc, ma = yuk(M)
def yerles(c, a, s, x, y):
    cc = cv2.resize(c, None, fx=s, fy=s, interpolation=cv2.INTER_AREA); aa = cv2.resize(a, None, fx=s, fy=s, interpolation=cv2.INTER_AREA)
    C = np.zeros((H, W, 3), np.float32); A = np.zeros((H, W), np.float32); h, w = aa.shape
    x0, y0 = max(x, 0), max(y, 0); x1, y1 = min(x + w, W), min(y + h, H)
    C[y0:y1, x0:x1] = cc[y0 - y:y1 - y, x0 - x:x1 - x]; A[y0:y1, x0:x1] = aa[y0 - y:y1 - y, x0 - x:x1 - x]; return C, A
def bas(katlar, zemin):
    o = zemin.astype(np.float32)
    for C, A in katlar: o = C * A[..., None] + o * (1 - A[..., None])
    return o
fg = (pl.astype(np.float32), al)
# ikili: Mike s=0.5 x=0, bel (yerel y 1900) tezgâhta
sM = float(os.environ.get("SM", 0.55)); yM = int(YC - sM * 1900); CM, AM = yerles(mc, ma, sM, 0, yM)
kesM_x = int(sM * 1080) - 1  # Mike iç kesik kenarı (aynalı: sağ kenar)
kesik = np.zeros((H, W), bool); kesik[:YC, kesM_x - 2:kesM_x + 1] = AM[:YC, kesM_x - 2:kesM_x + 1] > 0.5
best = None
for sJ in np.arange(0.50, 0.70, 0.01):
    wJ = int(round(sJ * 1080)); xJ = W - wJ; yJ = int(YC - sJ * 1800)
    CJ, AJ = yerles(jc, ja, sJ, xJ, yJ); acik = int((kesik & (AJ < 0.95)).sum())
    if acik == 0: best = (round(float(sJ), 2), xJ, yJ); break
assert best, "örtüşme bulunamadı"
sJ, xJ, yJ = best; CJ, AJ = yerles(jc, ja, sJ, xJ, yJ)
iki = bas([(CM, AM), (CJ, AJ), fg], pl)
# Jake kesik dış kenar kadraj sağında mı (sağ kenar = W-1)
cv2.imwrite(f"{ON}/ikili.jpg", iki.astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 88])
# tekliler: plaka 1.25 yakınlaştırma (tezgâh çizgisi sabit), karakter s=1 x=0 y=0
def yakin(img, a, cx, z=1.25):
    Mx = np.float32([[z, 0, cx * (1 - z)], [0, z, YC * (1 - z)]])
    return cv2.warpAffine(img, Mx, (W, H), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT), cv2.warpAffine(a, Mx, (W, H), flags=cv2.INTER_LINEAR)
tek = {}
for ad, c, a, cx in [("jake", jc, ja, 760), ("mike", mc, ma, 320)]:
    zp, za = yakin(pl, al, cx); C, A = yerles(c, a, 1.0, 0, 0)
    o = bas([(C, A), (zp.astype(np.float32), za)], zp); cv2.imwrite(f"{ON}/tek-{ad}.jpg", o.astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 88])
    tek[ad] = {"plaka_olcek": 1.25, "plaka_capa_xy": [cx, YC], "karakter_olcek": 1.0, "karakter_xy": [0, 0]}
J_ = {"tezgah_y": YC, "on_katman": "plaka/L1-A-tezgah-on.png (karakterlerin ÜSTÜNE, plakayla aynı dönüşüm)",
      "ikili": {"mike": {"olcek": sM, "xy": [0, yM], "z": 1}, "jake": {"olcek": sJ, "xy": [xJ, yJ], "z": 2},
                "kural": "Jake Mike'ın önünde; Jake'in sol omzu Mike'ın iç kol kesiğini örter (açık kesik piksel = 0)"},
      "tekli": tek, "kural": "kesik tabanların kol kenarı düz kesik: ölçek <1 iken dış kenar kadraj kenarına yaslanmalı; aksi halde kesik görünür"}
json.dump(J_, open(f"{OUT}/yerlesim-l1a.json", "w"), ensure_ascii=False, indent=1); print(json.dumps(J_, ensure_ascii=False))
