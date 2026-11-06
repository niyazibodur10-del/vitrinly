#!/usr/bin/env python3
"""Rig ağız/göz yaması çıkarımı + piksel hizası testi (gorsel-varlik-sanatcisi, 2026-10-27).
Taban: paket-v1 a (1920x1080) ve onun M4 kesiği leo/a-konusma-kapali.png. Her Cxx (aynı kadraj düzenlemesi) için:
  fark = max kanal |Cxx - a| > 30 ; 3x3 açma (kontur alt-piksel kaymasını atar)
  beklenen bölge: göz (x 830-1060, y 175-275) ya da ağız/çene (x 830-1050, y 280-440)
  dis_oran = beklenen bölge DIŞINDA kalan ham fark pikseli / tüm kare (kabul <= %1)
  yama kutusu = beklenen bölgedeki açılmış farkın bbox'ı + 14 px
  alfa = farkın 11 px genişletilmişi, 9 px Gauss yumuşatma, kutu kenarında 0'a zorlanır
  dikis = kutu kenarındaki 3 px halkada fark>30 oranı (düşük iyi; yama sınırı değişmeyen bölgede mi)
  geri_kurma = a + yama ile Cxx arasındaki kutu içi ortalama |fark| (düşük iyi) ve kutu dışı fark=0
Çıktı: <rig>/<ad>.png (RGBA, kutu boyutunda) + rig-yamalar.json (konum, ölçüm).
Kullanım: python -I rig-yama.py <a.png> <rig_klasoru> <Cxx.png:ad:bolge> ..."""
import sys, os, json, cv2, numpy as np
Z = {"goz": (830, 175, 1060, 275), "agiz": (830, 280, 1050, 440)}
def main():
    a = cv2.imread(sys.argv[1]); out = sys.argv[2]; os.makedirs(out, exist_ok=True); H, W = a.shape[:2]; res = {}
    for spec in sys.argv[3:]:
        p, ad, bol = spec.split(":"); b = cv2.imread(p)
        d = np.abs(a.astype(int) - b.astype(int)).max(2); raw = (d > 30).astype(np.uint8)
        op = cv2.morphologyEx(raw, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
        zx0, zy0, zx1, zy1 = Z[bol]; zone = np.zeros_like(raw); zone[zy0:zy1, zx0:zx1] = 1
        dis = float((raw & (1 - zone)).sum() / raw.size); dis_acik = float((op & (1 - zone)).sum() / raw.size)
        ys, xs = np.where(op & zone)
        x0, y0, x1, y1 = max(xs.min() - 14, 0), max(ys.min() - 14, 0), min(xs.max() + 15, W), min(ys.max() + 15, H)
        m = cv2.dilate((op & zone).astype(np.uint8), np.ones((11, 11), np.uint8)).astype(np.float32)
        m = cv2.GaussianBlur(m, (0, 0), 4.5); m = m[y0:y1, x0:x1]
        ramp = np.ones_like(m); r = 6
        for i in range(r): v = i / r; ramp[i, :] = np.minimum(ramp[i, :], v); ramp[-1 - i, :] = np.minimum(ramp[-1 - i, :], v); ramp[:, i] = np.minimum(ramp[:, i], v); ramp[:, -1 - i] = np.minimum(ramp[:, -1 - i], v)
        al = np.clip(m * 1.6, 0, 1) * ramp
        ring = np.ones((y1 - y0, x1 - x0), bool); ring[3:-3, 3:-3] = False
        dikis = float(raw[y0:y1, x0:x1][ring].mean())
        rec = a.astype(np.float32).copy(); rec[y0:y1, x0:x1] = b[y0:y1, x0:x1] * al[..., None] + a[y0:y1, x0:x1] * (1 - al[..., None])
        e_in = float(np.abs(rec[y0:y1, x0:x1] - b[y0:y1, x0:x1]).mean())
        e_in_deg = float(np.abs(rec[y0:y1, x0:x1] - b[y0:y1, x0:x1]).max(2)[op[y0:y1, x0:x1] > 0].mean()) if op[y0:y1, x0:x1].any() else 0.0
        rgba = cv2.cvtColor(b[y0:y1, x0:x1], cv2.COLOR_BGR2BGRA); rgba[..., 3] = (al * 255).astype(np.uint8)
        cv2.imwrite(os.path.join(out, ad + ".png"), rgba)
        res[ad] = {"kaynak": p, "bolge": bol, "konum_xy": [int(x0), int(y0)], "boyut_wh": [int(x1 - x0), int(y1 - y0)],
                   "ham_fark_tum_%": round(raw.mean() * 100, 3), "bolge_disi_ham_%": round(dis * 100, 3), "bolge_disi_acilmis_%": round(dis_acik * 100, 3),
                   "dikis_halka_fark_%": round(dikis * 100, 2), "geri_kurma_kutu_ort_abs": round(e_in, 2), "geri_kurma_degisen_px_ort_abs": round(e_in_deg, 2),
                   "kabul_hiza": bool(dis <= 0.01)}
        print(ad, json.dumps(res[ad], ensure_ascii=False))
    json.dump({"taban": sys.argv[1], "kanvas": [W, H], "not": "yamalar 1920x1080 tuval koordinatında; leo/a-konusma-kapali.png (M4 kesik) ya da paket-v1 a üstüne konum_xy'ye bindirilir", "yamalar": res},
              open(os.path.join(out, "rig-yamalar.json"), "w"), ensure_ascii=False, indent=1)
if __name__ == "__main__": main()
