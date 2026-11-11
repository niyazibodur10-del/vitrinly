#!/usr/bin/env python3
"""Sayfa ifade portreleri → animasyon varlığı (gorsel-varlik-sanatcisi 2026-11-10).
Adım: kırpım (sayfa kartı) → Lanczos 1080 genişlik + hafif keskinleştirme (ESRGAN CPU çakışması nedeniyle ertelendi) → kes-gc.py →
ten Lab eşleme (yalnız ten maskesi, yumuşak; hedef = konuşma tabanı ten medyanı) → <cikis>/<ad>.png + ifade.json (kenar kesiği başlangıç y).
Z3b sürümü: IFADE_SAC_PX=0 (kes-gc saç ab boyaması kapalı: tellerde kızıl/bordo leke yapıyordu) + sonda ifade-kenar.py.
Kullanım: [IFADE_SAC_PX=0] python -I ifade-hazirla.py <kirpim_klasoru> <cikis> <TJ_kesik.png> <TM_kesik.png> <kes-gc.py>"""
import sys, os, json, glob, subprocess, cv2, numpy as np
K, OUT, TJ, TM, KES = sys.argv[1:6]; os.makedirs(OUT, exist_ok=True); tmp = os.path.join(OUT, "_ara"); os.makedirs(tmp, exist_ok=True)
def ten_mask(bgr):
    h = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV); return (h[..., 0] >= 3) & (h[..., 0] <= 22) & (h[..., 1] > 50) & (h[..., 2] > 120)
def ten_med(path):
    i = cv2.imread(path, cv2.IMREAD_UNCHANGED); a = i[..., 3] > 250; m = ten_mask(i[..., :3]) & a
    m[int(i.shape[0] * 0.40):] = False  # yalnız yüz (gövde/ kol dışı)
    return np.median(cv2.cvtColor(i[..., :3], cv2.COLOR_BGR2LAB)[m].astype(np.float32), 0)
hedef = {"jake": ten_med(TJ), "mike": ten_med(TM)}
J = {}
for p in sorted(glob.glob(os.path.join(K, "*.png"))):
    ad = os.path.basename(p)[:-4]; kim = ad.split("-")[0]
    im = cv2.imread(p); s = 1080 / im.shape[1]
    up = cv2.resize(im, None, fx=s, fy=s, interpolation=cv2.INTER_LANCZOS4)
    bl = cv2.GaussianBlur(up, (0, 0), 2.0); up = cv2.addWeighted(up, 1.35, bl, -0.35, 0)
    ham = os.path.join(tmp, ad + ".png"); cv2.imwrite(ham, up)
    r = subprocess.run([sys.executable, "-I", KES, ham, os.path.join(tmp, ad + "-k.png"), os.path.join(tmp, ad + "-y.jpg"), str(int(up.shape[0] * 0.62))], capture_output=True, text=True, check=True, env={**os.environ, "SAC_PX": os.environ.get("IFADE_SAC_PX", str(int(up.shape[0] * 0.36)))})
    kes = json.loads(r.stdout.strip().splitlines()[-1])
    i = cv2.imread(os.path.join(tmp, ad + "-k.png"), cv2.IMREAD_UNCHANGED)
    lab = cv2.cvtColor(i[..., :3], cv2.COLOR_BGR2LAB).astype(np.float32)
    m = ten_mask(i[..., :3]) & (i[..., 3] > 250); m[int(i.shape[0] * 0.62):] = False
    once = np.median(lab[m], 0); fark = hedef[kim] - once
    mt = ten_mask(i[..., :3]) & (i[..., 3] > 250)  # kaydırma tüm ten (yüz + boyun): satır kesiği boyunda ton basamağı yaptı
    w = cv2.GaussianBlur(mt.astype(np.float32), (0, 0), 6)[..., None]
    lab2 = np.clip(lab + w * fark, 0, 255); i[..., :3] = cv2.cvtColor(lab2.astype(np.uint8), cv2.COLOR_LAB2BGR)
    sonra = np.median(cv2.cvtColor(i[..., :3], cv2.COLOR_BGR2LAB)[m].astype(np.float32), 0)
    de = lambda a, b: float(np.linalg.norm((a - b) * np.array([100 / 255, 1, 1])))
    # gri zemin halesi (Lanczos+keskinleştirme halkası): alfa 2 px içeri, 1 px yumuşat
    al = cv2.erode(i[..., 3], np.ones((5, 5), np.uint8)); i[..., 3] = cv2.GaussianBlur(al, (0, 0), 1.0)
    if kim == "mike": i = cv2.flip(i, 1)  # Mike tabanı aynalı kullanılıyor → ifadeler de aynalı (saç yönü tutarlı)
    cv2.imwrite(os.path.join(OUT, ad + ".png"), i)
    # Z3b (2026-11-11): kenar temizliği (tırtık, kopuk uç, renk bulaşığı) → ifade-kenar.py, yerinde
    kz = subprocess.run([sys.executable, "-I", os.path.join(os.path.dirname(os.path.abspath(__file__)), "ifade-kenar.py"), os.path.join(OUT, ad + ".png"), os.path.join(OUT, ad + ".png"), os.path.join(tmp, ad + "-kenar-yesil.jpg")], capture_output=True, text=True, check=True)
    J[ad] = {"boyut": [i.shape[1], i.shape[0]], "kenar_kesik_baslangic_y": min([v for v in kes["kenara_degme"].values() if v >= 0] or [i.shape[0]]),
             "alt_kesik_y": i.shape[0], "ten_dE_once": round(de(once, hedef[kim]), 1), "ten_dE_sonra": round(de(sonra, hedef[kim]), 1), "sacak_px": kes["sacak_px"]}
json.dump(J, open(os.path.join(OUT, "ifade.json"), "w"), ensure_ascii=False, indent=1)
for k, v in J.items(): print(k, v)
