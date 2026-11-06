#!/usr/bin/env python3
"""M4 kesme v2 (Lab renk anahtarı + arındırma) — kapalı delik kuralı düzeltildi (gorsel-varlik-sanatcisi, 2026-10-27).
v1 (hazirlik/kes-test.py) yalnız <400 px kapalı delikleri dolduruyordu; C02'de koyu gri pantolonun bir parçası
zemine ΔE<14 düşüp 1.6k px'lik delik açtı. v2: kapalı (kenara değmeyen) delik, içindeki medyan zemin uzaklığı
d_med > 6 ise (gerçek zemin değil, zemine yakın renkli giysi) VEYA alanı < 400 ise doldurulur. Gerçek zemin cebi
(kol-gövde arası) d_med≈0-3 → zemin kalır.
Ölçüm: kenar artığı, saçak (alfa>.5 & d<12), doldurulan/bırakılan kapalı delikler (alan, d_med).
Kullanım: python -I kes-m4.py <girdi.png> <cikis.png> [<yesil_onizleme.jpg>]"""
import sys, json, cv2, numpy as np

def lab(img): return cv2.cvtColor(img, cv2.COLOR_BGR2LAB).astype(np.float32) * np.array([100/255, 1, 1], np.float32) - np.array([0, 128, 128], np.float32)

def main():
    src, dst = sys.argv[1], sys.argv[2]; img = cv2.imread(src)
    c = np.concatenate([img[:24, :24].reshape(-1, 3), img[:24, -24:].reshape(-1, 3), img[-24:, :24].reshape(-1, 3)])
    bgc = np.median(c, 0); bgl = lab(bgc.reshape(1, 1, 3).astype(np.uint8))[0, 0]
    d = np.linalg.norm(lab(img) - bgl, axis=2)
    a = np.clip((d - 14) / 16, 0, 1)
    core = (a > 0.5).astype(np.uint8)
    n, lb, st, _ = cv2.connectedComponentsWithStats(core); k = 1 + np.argmax(st[1:, 4]); keep = (lb == k).astype(np.uint8)
    n2, lb2 = cv2.connectedComponents((keep == 0).astype(np.uint8))
    edge = set(np.unique(np.concatenate([lb2[0], lb2[-1], lb2[:, 0], lb2[:, -1]]))) - {0}
    holes_info = []; fill = np.zeros_like(keep)
    for i in range(1, n2):
        if i in edge: continue
        sel = lb2 == i; area = int(sel.sum()); dm = float(np.median(d[sel]))
        f = area < 400 or dm > 6
        if f: fill[sel] = 1
        if area >= 100: holes_info.append({"alan": area, "d_med": round(dm, 1), "dolduruldu": bool(f)})
    core = np.clip(keep + fill, 0, 1)
    a = np.where(cv2.dilate(core, np.ones((5, 5), np.uint8)) > 0, a, 0)
    a = np.maximum(a, core.astype(np.float32) * (cv2.erode(core, np.ones((5, 5), np.uint8)) > 0))
    a[fill > 0] = 1.0
    # arındırma
    f32 = img.astype(np.float32); al = np.clip(a, 0.05, 1)[..., None]; band = (a > 0) & (a < 0.999)
    out = f32.copy(); un = (f32 - (1 - al) * bgc.astype(np.float32)) / al; out[band] = np.clip(un[band], 0, 255); out = out.astype(np.uint8)
    d2 = np.linalg.norm(lab(out) - bgl, axis=2)
    cc = (a > 0.5).astype(np.uint8); ring = (cc - cv2.erode(cc, np.ones((7, 7), np.uint8))) > 0
    res = {"girdi": src, "zemin_bgr": [int(v) for v in bgc], "kenar_artigi_orani": round(float((d2[ring] < 25).mean()), 4),
           "sacak_px": int(((a > 0.5) & (d2 < 12) & (fill == 0)).sum()), "on_plan_px": int(cc.sum()),
           "kapali_delikler_>=100px": holes_info,
           "on_plan_bbox_xyxy": [int(v) for v in (np.where(cc.any(0))[0][[0, -1]].tolist()[:1] + np.where(cc.any(1))[0][[0, -1]].tolist()[:1] + np.where(cc.any(0))[0][[0, -1]].tolist()[1:] + np.where(cc.any(1))[0][[0, -1]].tolist()[1:])]}
    rgba = cv2.cvtColor(out, cv2.COLOR_BGR2BGRA); rgba[..., 3] = (a * 255).astype(np.uint8); cv2.imwrite(dst, rgba)
    if len(sys.argv) > 3:
        g = np.zeros_like(out); g[:] = (60, 200, 60); cv2.imwrite(sys.argv[3], (out * a[..., None] + g * (1 - a[..., None])).astype(np.uint8), [cv2.IMWRITE_JPEG_QUALITY, 88])
    print(json.dumps(res, ensure_ascii=False))

if __name__ == "__main__": main()
