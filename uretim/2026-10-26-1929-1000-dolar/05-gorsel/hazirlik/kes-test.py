#!/usr/bin/env python3
"""Düz zeminli Canva pozlarında 3 kesme yöntemi + ölçüm (gorsel-varlik-sanatcisi, 2026-10-27).
Kullanım: python -I kes-test.py <girdi.png> <cikis_klasoru>
M1 renk anahtarı: köşe zemin rengine Lab uzaklığı, yumuşak rampa (d 14..30), en büyük bileşen + delik doldurma.
M2 GrabCut: M1'den tohum (aşınmış M1 = kesin ön, genişletilmiş tümleyen = kesin arka), 5 tur.
M4 M1 + aynı arındırma.
M3 M2 + kenar arındırma: kenar bandında (alfa<1) zemin rengini çıkarıp (un-premultiply) mavi taşmayı giderir.
Ölçüm: kenar artığı = maske sınırının 3 px iç halkasında zemine ΔE<25 olan piksel oranı (düşük iyi);
  saçak = alfa>0.5 olup zemine ΔE<12 olan piksel sayısı (zemin parçası ön planda kalmış); ön plan alanı.
Yeşil önizleme (60,200,60) üstünde kompozit + kafa/el yakın kırpımları.
"""
import sys, os, json
import cv2, numpy as np

def lab(img): return cv2.cvtColor(img, cv2.COLOR_BGR2LAB).astype(np.float32) * np.array([100/255, 1, 1], np.float32) - np.array([0, 128, 128], np.float32)

def bg_color(img):
    c = np.concatenate([img[:24, :24].reshape(-1, 3), img[:24, -24:].reshape(-1, 3), img[-24:, :24].reshape(-1, 3)])
    return np.median(c, 0)

def largest_filled(m):
    n, lb, st, _ = cv2.connectedComponentsWithStats((m > 0).astype(np.uint8))
    if n <= 1: return m
    k = 1 + np.argmax(st[1:, cv2.CC_STAT_AREA]); keep = (lb == k).astype(np.uint8)
    # delik doldurma: dışarıdan erişilemeyen zemin = delik
    # dış zemin = görüntü kenarına değen zemin bileşenleri (kol-gövde arası alt kenara değer, delik sayılmaz)
    n2, lb2 = cv2.connectedComponents((keep == 0).astype(np.uint8))
    edge = set(np.unique(np.concatenate([lb2[0], lb2[-1], lb2[:, 0], lb2[:, -1]]))) - {0}
    outside = np.isin(lb2, list(edge))
    holes = ((keep == 0) & ~outside).astype(np.uint8)
    # yalnız küçük delikler doldurulur (göz akı vb.); büyük kapalı zemin cebi (kol halkası) zemin kalır
    nh, lh, sh, _ = cv2.connectedComponentsWithStats(holes)
    small = np.zeros_like(holes)
    for i in range(1, nh):
        if sh[i, cv2.CC_STAT_AREA] < 400: small[lh == i] = 1
    holes = small
    return np.clip(keep + holes, 0, 1)

def m1(img, bgc):
    d = np.linalg.norm(lab(img) - lab(bgc.reshape(1, 1, 3).astype(np.uint8))[0, 0], axis=2)
    a = np.clip((d - 14) / 16, 0, 1)
    core = largest_filled((a > 0.5).astype(np.uint8))
    a = np.where(cv2.dilate(core, np.ones((5, 5), np.uint8)) > 0, a, 0)
    a = np.maximum(a, core.astype(np.float32) * (cv2.erode(core, np.ones((5, 5), np.uint8)) > 0))
    return a, d

def m2(img, a1):
    core = (a1 > 0.5).astype(np.uint8)
    mask = np.full(core.shape, cv2.GC_PR_BGD, np.uint8)
    mask[core > 0] = cv2.GC_PR_FGD
    mask[cv2.erode(core, np.ones((15, 15), np.uint8)) > 0] = cv2.GC_FGD
    mask[cv2.dilate(core, np.ones((15, 15), np.uint8)) == 0] = cv2.GC_BGD
    b, f = np.zeros((1, 65)), np.zeros((1, 65))
    cv2.grabCut(img, mask, None, b, f, 5, cv2.GC_INIT_WITH_MASK)
    m = np.where((mask == cv2.GC_FGD) | (mask == cv2.GC_PR_FGD), 1, 0).astype(np.uint8)
    m = largest_filled(m)
    return cv2.GaussianBlur(m.astype(np.float32), (3, 3), 0)

def decontam(img, a, bgc):
    f = img.astype(np.float32); al = np.clip(a, 0.05, 1)[..., None]
    band = (a > 0) & (a < 0.999)
    out = f.copy()
    un = (f - (1 - al) * bgc.astype(np.float32)) / al
    out[band] = np.clip(un[band], 0, 255)
    return out.astype(np.uint8)

def measure(img, a, d):
    core = (a > 0.5).astype(np.uint8)
    ring = core - cv2.erode(core, np.ones((7, 7), np.uint8))
    rr = ring > 0
    resid = float((d[rr] < 25).mean()) if rr.any() else 0.0
    fringe = int(((a > 0.5) & (d < 12)).sum())
    return {"kenar_artigi_orani": round(resid, 4), "sacak_px": fringe, "on_plan_px": int(core.sum())}

def preview(img, a, path):
    g = np.zeros_like(img); g[:] = (60, 200, 60); al = a[..., None]
    comp = (img * al + g * (1 - al)).astype(np.uint8); cv2.imwrite(path, comp); return comp

def main():
    src, out = sys.argv[1], sys.argv[2]; os.makedirs(out, exist_ok=True)
    img = cv2.imread(src); bgc = bg_color(img)
    a1, d = m1(img, bgc)
    a2 = m2(img, a1)
    img3 = decontam(img, a2, bgc)
    # M3 ölçümü: arındırılmış görüntünün zemine uzaklığı
    d3 = np.linalg.norm(lab(img3) - lab(bgc.reshape(1, 1, 3).astype(np.uint8))[0, 0], axis=2)
    img4 = decontam(img, a1, bgc)
    d4 = np.linalg.norm(lab(img4) - lab(bgc.reshape(1, 1, 3).astype(np.uint8))[0, 0], axis=2)
    res = {"girdi": src, "zemin_bgr": [int(v) for v in bgc], "boyut": list(img.shape[1::-1])}
    comps = []
    for ad, im, a, dd in (("M1-renk-anahtari", img, a1, d), ("M2-grabcut", img, a2, d), ("M3-grabcut-arindirma", img3, a2, d3), ("M4-renk-arindirma", img4, a1, d4)):
        res[ad] = measure(im, a, dd)
        rgba = cv2.cvtColor(im, cv2.COLOR_BGR2BGRA); rgba[..., 3] = (a * 255).astype(np.uint8)
        cv2.imwrite(os.path.join(out, f"{ad}.png"), rgba)
        comps.append((ad, preview(im, a, os.path.join(out, f"{ad}-yesil.jpg"))))
    # kontak: her yöntem için tam + saç kenarı yakın + saat/el yakın
    ys, xs = np.where(a2 > 0.5); top = ys.min(); cx = int(xs[ys < top + 60].mean())
    hair = (max(cx - 200, 0), max(top - 20, 0), cx + 200, top + 260)
    rows = []
    for ad, c in comps:
        full = cv2.resize(c, (640, 360))
        hc = cv2.resize(c[hair[1]:hair[3], hair[0]:hair[2]], (400, 280), interpolation=cv2.INTER_NEAREST)
        hc = cv2.resize(hc, (512, 360))
        row = np.hstack([full, hc]); cv2.putText(row, ad, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 3); cv2.putText(row, ad, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (255, 255, 255), 1)
        rows.append(row)
    cv2.imwrite(os.path.join(out, "kesme-kontak.jpg"), np.vstack(rows))
    print(json.dumps(res, ensure_ascii=False, indent=1))
    json.dump(res, open(os.path.join(out, "kesme-olcum.json"), "w"), ensure_ascii=False, indent=1)

if __name__ == "__main__": main()
