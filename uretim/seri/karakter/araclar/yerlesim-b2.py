#!/usr/bin/env python3
"""Bölüm 2 yerleşimi: L3-A (garaj yolu) + G1 bisiklet + tabanlar; L1-A S1 bisiklet girişi. gorsel-varlik-sanatcisi 2026-11-12.
Ölçek: garaj yolu genişliği y≈1260'ta ~1060 px ≈ 3,2 m → ~330 px/m; bisiklet ~1,7 m → ölçek 0,33 (resim genişliği 1600).
Kullanım: python -I yerlesim-b2.py <video/public/seri> <onizleme_klasoru>"""
import sys, os, json, cv2, numpy as np
P, ON = sys.argv[1], sys.argv[2]; os.makedirs(ON, exist_ok=True)
B2, B1 = P + "/bolum-002", P + "/bolum-001"; W, H = 1080, 1920
bj = json.load(open(B2 + "/nesne/bisiklet.json"))
def yuk(p): i = cv2.imread(p, cv2.IMREAD_UNCHANGED); return i[..., :3].astype(np.float32), i[..., 3].astype(np.float32) / 255
def koy(zemin, c, a, s, x, y):
    cc = cv2.resize(c, None, fx=s, fy=s, interpolation=cv2.INTER_AREA); aa = cv2.resize(a, None, fx=s, fy=s, interpolation=cv2.INTER_AREA)
    h, w = aa.shape; x0, y0, x1, y1 = max(x, 0), max(y, 0), min(x + w, W), min(y + h, H)
    if x1 <= x0 or y1 <= y0: return zemin
    al = aa[y0 - y:y1 - y, x0 - x:x1 - x, None]; zemin[y0:y1, x0:x1] = cc[y0 - y:y1 - y, x0 - x:x1 - x] * al + zemin[y0:y1, x0:x1] * (1 - al); return zemin
def zoom(img, cx, cy, z, sigma=0):
    M = np.float32([[z, 0, cx * (1 - z)], [0, z, cy * (1 - z)]]); o = cv2.warpAffine(img, M, (W, H), flags=cv2.INTER_CUBIC, borderMode=cv2.BORDER_REFLECT)
    return cv2.GaussianBlur(o, (0, 0), sigma) if sigma else o
l3 = cv2.imread(B2 + "/plaka/L3-A.png").astype(np.float32)
bb, ba = yuk(B2 + "/nesne/bisiklet-basik.png"); sb, sa = yuk(B2 + "/nesne/bisiklet-sisik.png")
S_B, ZEMIN = 0.33, 1250; bw = int(round(S_B * bj["boyut"][0]))
def bis_xy(zy, s, cx=540, surum="basik"): return [int(cx - s * bj["boyut"][0] / 2), int(round(zy - s * bj[f"zemin_y_{surum}"]))]
Y = {"plaka": "plaka/L3-A.png", "olcum": {"derz_y": 1408, "ufuk_garaj_tabani_y": 600, "garaj_yolu_genislik_px": {"y790": 520, "y1260": 1060}, "px_per_m_y1260": 330},
     "genis_l3": {"bisiklet": {"dosya": "nesne/bisiklet-basik.png | bisiklet-sisik.png", "olcek": S_B, "zemin_y": ZEMIN,
                  "xy_basik": bis_xy(ZEMIN, S_B), "xy_sisik": bis_xy(ZEMIN, S_B, surum="sisik"), "not": "iki sürüm aynı tuval; takasta yalnız y farkı (zemin_y_sisik)"}},
     "yakin_l3": {"plaka": "L3-A x1.3, çapa (540,600), Gauss σ4 (alan derinliği)", "taban": {"olcek": 1.0, "xy": [0, 0], "dosya": "../bolum-001/karakter/<kim>-taban.png"},
                  "agiz": "../bolum-001/agiz/<kim>-agiz-*.png aynı konum (bölüm 1 VARLIKLAR.md)", "kural": "kesik kollar kadraj kenarında, alt kadraj altı: ek ön katman gerekmez"},
     "portre_l3": {"plaka": "L3-A x1.6, çapa (540,700), σ6", "konum": "../bolum-001/yerlesim.json → ifade_tekli.konum (aynı)"},
     "s1_mutfak_giris": {"plaka": "bölüm 1 tekli Mike (L1-A x1.25, çapa (320,1186)) + tezgah-on", "bisiklet": {"olcek": 0.7, "zemin_y": 1945,
                  "x_bas": 1080, "x_son": 430, "katman": "tezgah-on ÜSTÜNDE (kameraya en yakın)", "ziplama": "y ±8 px, tekerlek dönüşü yok (statik görsel)"}}}
json.dump(Y, open(B2 + "/yerlesim.json", "w"), ensure_ascii=False, indent=1)
# önizlemeler
o1 = koy(l3.copy(), bb, ba, S_B, *Y["genis_l3"]["bisiklet"]["xy_basik"]); o2 = koy(l3.copy(), sb, sa, S_B, *Y["genis_l3"]["bisiklet"]["xy_sisik"])
jc, ja = yuk(B1 + "/karakter/jake-taban.png"); o3 = koy(zoom(l3, 540, 600, 1.3, 4), jc, ja, 1.0, 0, 0)
l1 = cv2.imread(B1 + "/plaka/L1-A.png").astype(np.float32); fg = cv2.imread(B1 + "/plaka/L1-A-tezgah-on.png", cv2.IMREAD_UNCHANGED)
mc, ma = yuk(B1 + "/karakter/mike-taban.png"); z = zoom(l1, 320, 1186, 1.25); zf = zoom(fg.astype(np.float32), 320, 1186, 1.25)
o4 = koy(z, mc, ma, 1.0, 0, 0); al = zf[..., 3:] / 255; o4 = zf[..., :3] * al + o4 * (1 - al)
s4 = 0.7; o4 = koy(o4, bb, ba, s4, 560, int(1945 - s4 * bj["zemin_y_basik"]))
for ad, o in [("genis-basik", o1), ("genis-sisik", o2), ("yakin-jake-l3", o3), ("s1-mutfak-giris", o4)]: cv2.imwrite(f"{ON}/{ad}.jpg", o.astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 88])
print(json.dumps(Y["genis_l3"], ensure_ascii=False))
