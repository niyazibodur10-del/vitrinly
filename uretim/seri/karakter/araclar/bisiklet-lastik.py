#!/usr/bin/env python3
"""B2-G1 bisiklet: basık (özgün) + şişik (kod) sürüm, aynı tuval (takasta hizalı). gorsel-varlik-sanatcisi 2026-11-12.
Gölge: lastik altı yarı saydam temas gölgesi (yeşil sızıntı sonrası zeytin) → nötr koyu.
Şişik: merkez Hough'tan (cx, cy), dış yarıçap yan dış kenardan; alt yarıda [R-50, R+4] halkası temiz yan sektörün
radyal medyan profiliyle boyanır (aynalama üstteki fren kaliperini alta taşıdı → elendi), alt yarıda R+3 dışı (basık şişkinlik + gölge) saydam yapılır.
Kullanım: python -I bisiklet-lastik.py <kesik_rgba.png> <cikis_klasoru> <arka_cx> <arka_cy> <on_cx> <on_cy>"""
import sys, os, json, cv2, numpy as np
im = cv2.imread(sys.argv[1], cv2.IMREAD_UNCHANGED); out = sys.argv[2]; os.makedirs(out, exist_ok=True); H, W = im.shape[:2]
a = im[..., 3].astype(np.float32) / 255
# gölge: alfa<0,75 ve alt bantta (tekerlerin alt %12'si) → nötr koyu, alfa ×0,8
ys = np.nonzero(a > 0.5)[0]; ymax = ys.max()
golge = (a > 0.01) & (a < 0.75) & (np.arange(H)[:, None] > ymax - 60)
basik = im.copy(); basik[golge, :3] = 28; basik[golge, 3] = (a[golge] * 0.8 * 255).astype(np.uint8)
res = {}
sisik = basik.copy()
yy, xx = np.mgrid[0:H, 0:W]
for ad, cx, cy, taraf in [("arka", int(sys.argv[3]), int(sys.argv[4]), "sol"), ("on", int(sys.argv[5]), int(sys.argv[6]), "sag")]:
    # elips uydurma (eksen hizalı): dış lastik konturu; açı −165..−15° (tepe ±20° fren/çatal hariç) + yanlar 5..35° / 145..175°
    # (basıklık yalnız altta). Çizimdeki teker tam daire değil: daire modeli arka alt kenarı 68 px kaçırdı → elendi.
    pts = []
    for t in np.radians(np.r_[-165:-110:2, -70:-15:2, 5:35:2, 145:175:2]):
        for rr in range(380, 230, -1):
            x, y = int(round(cx + rr * np.cos(t))), int(round(cy + rr * np.sin(t)))
            if 0 <= x < W and 0 <= y < H and a[y, x] > 0.5: pts.append((x, y)); break
    P_ = np.array(pts, np.float64)
    for _ in range(10):
        X, Yp = P_[:, 0], P_[:, 1]; Am = np.c_[X * X, Yp * Yp, X, Yp]; k = np.linalg.lstsq(Am, np.ones(len(P_)), rcond=None)[0]
        Ae, Ce, De, Ee = k; x0, y0 = -De / (2 * Ae), -Ee / (2 * Ce); F = 1 + De * De / (4 * Ae) + Ee * Ee / (4 * Ce)
        ax, by = np.sqrt(F / Ae), np.sqrt(F / Ce)
        rho = np.hypot((X - x0) / ax, (Yp - y0) / by); art = np.abs(rho - 1) * (ax + by) / 2
        if art.max() <= 3: break
        P_ = P_[art <= max(3.0, np.percentile(art, 70))]
    yontem = "elips"
    if len(P_) < 30 or not (0.9 <= ax / by <= 1.1):  # az nokta / aşırı basık elips → daire yedeği (Hough merkezi + yan dış kenar)
        yontem = "daire"; x0, y0 = float(cx), float(cy); row = np.nonzero(a[cy, :] > 0.5)[0]
        Rd = cx - int(row[row < cx].min()) if taraf == "sol" else int(row[row > cx].max()) - cx; ax = by = float(Rd); art = np.array([0.0])
    cx, cy = int(round(x0)), int(round(y0)); R = int(round((ax + by) / 2)); sapma = float(art.max()); pts = P_
    r = np.hypot((xx - x0) / ax, (yy - y0) / by) * R  # normalize elips yarıçapı (px, ortalama yarıçap ölçeğinde)
    aci = np.degrees(np.arctan2((yy - y0) / by, (xx - x0) / ax))
    sektor = (np.abs(np.abs(aci) - 180) < 20) if taraf == "sol" else (np.abs(aci) < 20)
    ri = np.round(r).astype(int); prof = {}
    for kk in range(R - 50, R + 5):
        sel = sektor & (ri == kk)
        if sel.any(): prof[kk] = np.median(basik[sel].astype(np.float32), 0)
    halka = (yy > cy + 0.6 * R) & (r >= R - 50) & (r <= R + 4)  # yalnız alt bölge: yanlarda aynakol lastiğin önünde (ilk sürüm dişleri kesti)
    # geçiş bandı 0,4R–0,6R: yalnız boş (saydam) pikseller doldurulur → sınırda boşluk kalmaz, önden geçen zincir/aynakol korunur
    halka |= (yy > cy + 0.4 * R) & (yy <= cy + 0.6 * R) & (r >= R - 50) & (r <= R + 4) & (basik[..., 3] < 128)
    hy, hx = np.nonzero(halka)
    sisik[hy, hx] = np.array([prof.get(int(ri[y, x]), [0, 0, 0, 0]) for y, x in zip(hy, hx)], np.float32).round().astype(np.uint8)
    sil = (yy > cy + 0.75 * R) & (r > R + 4) & (np.abs(xx - cx) <= R + 60)  # yalnız taban şişkinliği: daha yukarısı aynakol/zincir (ilk sürüm sildi)
    # basık lastiğin halka içine ezilmiş kalıntısı (R-85..R-50, alt yarı): lastik renkli (doygun) pikseller silinir; teller gümüş (soluk) kalır
    hsv = cv2.cvtColor(basik[..., :3], cv2.COLOR_BGR2HSV)
    kalinti = (yy > cy + 0.5 * R) & (r >= R - 85) & (r < R - 50) & ((hsv[..., 1] > 70) | (hsv[..., 2] < 60))
    sil |= kalinti
    # özgün (aşağıda çizilmiş) jantın iç yayı R-75..R-48: yapı tensöründe gradyanı radyal olan (yay) pikseller silinir, teller (teğet gradyan) kalır
    gri = cv2.cvtColor(basik[..., :3], cv2.COLOR_BGR2GRAY).astype(np.float32)
    gx = cv2.Sobel(gri, cv2.CV_32F, 1, 0, ksize=3); gy = cv2.Sobel(gri, cv2.CV_32F, 0, 1, ksize=3)
    jxx = cv2.GaussianBlur(gx * gx, (0, 0), 2); jyy = cv2.GaussianBlur(gy * gy, (0, 0), 2); jxy = cv2.GaussianBlur(gx * gy, (0, 0), 2)
    teta = 0.5 * np.arctan2(2 * jxy, jxx - jyy)  # baskın gradyan yönü
    ux, uy = (xx - cx) / np.maximum(r, 1), (yy - cy) / np.maximum(r, 1)
    radyal = np.abs(np.cos(teta) * ux + np.sin(teta) * uy) > 0.85
    yay = (yy > cy + 0.5 * R) & (r >= R - 75) & (r < R - 48) & radyal & (basik[..., 3] > 60)
    yay = cv2.dilate(yay.astype(np.uint8), np.ones((3, 3), np.uint8)).astype(bool) & (yy > cy + 0.5 * R) & (r >= R - 75) & (r < R - 46)
    sil |= yay
    sisik[sil, 3] = 0
    res[ad] = {"merkez": [cx, int(cy)], "dis_yaricap": int(R), "uydurma_nokta": len(pts), "uydurma_max_sapma_px": round(sapma, 1), "basik_alt_y": int(np.nonzero(a[:, cx] > 0.5)[0].max()), "sisik_alt_y": int(round(y0 + by)), "elips_ax_by": [round(float(ax), 1), round(float(by), 1)], "yontem": yontem}
# şişik sürüme temas gölgesi (basıktaki gölge silindi): her teker altına elips, σ6, en çok %45 koyuluk, yalnız saydam alana
gl = np.zeros((H, W), np.float32)
for k in ("arka", "on"):
    cx, cy = res[k]["merkez"]; R = res[k]["dis_yaricap"]; cv2.ellipse(gl, (int(cx), int(res[k]["sisik_alt_y"])), (int(R * 0.85), 10), 0, 0, 360, 1.0, -1)
gl = cv2.GaussianBlur(gl, (0, 0), 6) * 0.45
sa = sisik[..., 3].astype(np.float32) / 255; yeni_a = sa + gl * (1 - sa)
renk = (sisik[..., :3].astype(np.float32) * sa[..., None] + 28 * (gl * (1 - sa))[..., None]) / np.maximum(yeni_a, 1e-4)[..., None]
sisik[..., :3] = np.clip(renk, 0, 255).astype(np.uint8); sisik[..., 3] = np.clip(yeni_a * 255, 0, 255).astype(np.uint8)
# ortak kırpım (iki sürüm aynı kutu)
al = np.maximum(basik[..., 3], sisik[..., 3]) > 10; ys2, xs2 = np.nonzero(al); m = 16
x0, y0, x1, y1 = max(xs2.min() - m, 0), max(ys2.min() - m, 0), min(xs2.max() + m, W), min(ys2.max() + m, H)
for ad, img in [("bisiklet-basik", basik), ("bisiklet-sisik", sisik)]: cv2.imwrite(os.path.join(out, ad + ".png"), img[y0:y1, x0:x1])
res["kirpim_xyxy"] = [int(x0), int(y0), int(x1), int(y1)]; res["boyut"] = [int(x1 - x0), int(y1 - y0)]
for k in ("arka", "on"):
    res[k]["merkez"] = [int(res[k]["merkez"][0] - x0), int(res[k]["merkez"][1] - y0)]
    res[k]["basik_alt_y"] = int(res[k]["basik_alt_y"] - y0); res[k]["sisik_alt_y"] = int(res[k]["sisik_alt_y"] - y0)
res["zemin_y_basik"] = max(res["arka"]["basik_alt_y"], res["on"]["basik_alt_y"]); res["zemin_y_sisik"] = max(res["arka"]["sisik_alt_y"], res["on"]["sisik_alt_y"])
json.dump(res, open(os.path.join(out, "bisiklet.json"), "w"), ensure_ascii=False, indent=1); print(json.dumps(res))
