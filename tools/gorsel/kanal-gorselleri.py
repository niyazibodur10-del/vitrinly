#!/usr/bin/env python3
"""Financial Rise — kanal banner'ı (2560x1440) ve profil fotoğrafı (800x800) üretici + testler.

Çalıştırma (repo kökünden):
  ~/.finansal-arac/venv/bin/python tools/gorsel/kanal-gorselleri.py            # tüm adaylar + testler
  ... --banner-karakter <png> --banner-isaret <png> --profil-karakter <png>     # Canva kaynak görseli gelince
  ... --arkaplan <16:9 sahne png>                                               # Canva arka planı (opsiyonel)
  ... --kazanan-banner A --kazanan-profil P1                                    # nihai dosyaları yazar

Girdi karakter görseli: düz renk arka planlı (Canva paket-v1 gibi) veya şeffaf PNG. Düz arka plan kenar
piksellerinden otomatik bulunur ve renk anahtarıyla çıkarılır (yarı saydam kenarlarda arka plan rengi ayrıştırılır).
Metin her zaman kodla yazılır (yapay zekâ yazıyı bozar). Yazı tipleri: video/public/fonts (Anton, Fredoka).

Sınırlar (YouTube Yardım, answer/10456525, 2026-10-26 okundu): banner en az 2048x1152, 16:9, önerilen 2560x1440,
≤6 MB; güvenli alan 2048 tuvalde 1235x338 → 2560 tuvalde 1546x423 (x1,25). Profil 98x98 görüntülenir, ≤15 MB.
"""
import argparse, json, os, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

KOK = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
FONT = os.path.join(KOK, "video", "public", "fonts")
W, H = 2560, 1440
SW, SH = 1546, 423                       # güvenli alan (tüm cihazlar)
SX, SY = (W - SW) // 2, (H - SH) // 2    # 507, 508
# Kırpma görünümleri (2560 tuvalde). Güvenli alan YouTube kaynaklı; diğerleri yaygın tasarım rehberleri [AÖ].
KIRPMA = {
    "tv": (0, 0, W, H),
    "masaustu": (0, SY, W, SY + SH),
    "tablet": ((W - 1855) // 2, SY, (W + 1855) // 2, SY + SH),
    "mobil": (SX, SY, SX + SW, SY + SH),
}
# Marka paleti (pilot videodaki lacivert/altın ile uyumlu)
LACI_UST, LACI_ALT = (8, 17, 38), (18, 38, 76)
ALTIN, YESIL, BEYAZ, LACI_KOYU = (255, 200, 61), (46, 212, 125), (255, 255, 255), (10, 19, 40)


# ---------------------------------------------------------------- yardımcılar
ETIKET = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def etiket(px):
    return ImageFont.truetype(ETIKET, px) if os.path.exists(ETIKET) else font("Anton-400.woff2", px)


def font(ad, px):
    f = ImageFont.truetype(os.path.join(FONT, ad), px)
    if "Fredoka" in ad:                 # değişken yazı tipi: Pillow varsayılanı Light (300)
        f.set_variation_by_axes([700])
    return f


def lum(c):
    c = np.asarray(c, dtype=np.float64)[..., :3] / 255.0
    c = np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    return c[..., 0] * 0.2126 + c[..., 1] * 0.7152 + c[..., 2] * 0.0722


def wcag(l1, l2):
    a, b = np.maximum(l1, l2), np.minimum(l1, l2)
    return (a + 0.05) / (b + 0.05)


def kes(yol):
    """Karakteri arka plandan ayır → kırpılmış RGBA."""
    im = Image.open(yol)
    if im.mode == "RGBA" and np.asarray(im)[..., 3].min() < 250:
        a = np.asarray(im)
    else:
        rgb = np.asarray(im.convert("RGB")).astype(np.float64)
        kenar = np.concatenate([rgb[:8].reshape(-1, 3), rgb[:, :8].reshape(-1, 3), rgb[:, -8:].reshape(-1, 3)])
        bg = np.median(kenar, 0)
        d = np.sqrt(((rgb - bg) ** 2).sum(-1))
        t0, t1 = 14.0, 48.0
        al = np.clip((d - t0) / (t1 - t0), 0, 1)
        al = al * al * (3 - 2 * al)
        # küçük adacıkları at (arka plan dokusu)
        import cv2
        m = (al > 0.5).astype(np.uint8)
        n, lab, st, _ = cv2.connectedComponentsWithStats(m, 8)
        if n > 1:
            buyuk = st[1:, cv2.CC_STAT_AREA].max()
            tut = np.zeros(n, bool); tut[1:] = st[1:, cv2.CC_STAT_AREA] > buyuk * 0.01
            yakın = cv2.dilate(tut[lab].astype(np.uint8), np.ones((7, 7), np.uint8)) > 0
            al = np.where(yakın, al, 0)
        # arka plan rengini kenarlardan ayrıştır: C = (I - (1-a)B) / a
        a3 = np.maximum(al, 1e-3)[..., None]
        fg = np.clip((rgb - (1 - a3) * bg) / a3, 0, 255)
        fg = np.where(al[..., None] > 0.98, rgb, fg)
        a = np.dstack([fg, al * 255]).round().astype(np.uint8)
    img = Image.fromarray(a, "RGBA")
    return img.crop(img.getbbox())


def dikey_gradyan(w, h, ust, alt):
    t = np.linspace(0, 1, h)[:, None, None]
    g = np.array(ust)[None, None] * (1 - t) + np.array(alt)[None, None] * t
    return Image.fromarray(np.repeat(g, w, 1).astype(np.uint8), "RGB")


def radyal(w, h, cx, cy, r, renk, guc):
    yy, xx = np.mgrid[0:h, 0:w]
    d = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2) / r
    a = np.clip(1 - d, 0, 1) ** 2 * guc
    lay = np.zeros((h, w, 4), np.uint8); lay[..., :3] = renk; lay[..., 3] = (a * 255).astype(np.uint8)
    return Image.fromarray(lay, "RGBA")


def grafik_noktalari(seed, x0, x1, y0, y1, n=26):
    """Yukarı eğilimli rastgele yürüyüş (sabit tohum → her çalıştırmada aynı)."""
    r = np.random.default_rng(seed)
    xs = np.linspace(x0, x1, n)
    trend = np.linspace(y0, y1, n)
    gurultu = np.cumsum(r.normal(0, 1, n)); gurultu -= np.linspace(gurultu[0], gurultu[-1], n)
    sal = r.normal(0, 1, n) * 18
    ys = trend + gurultu * 22 + sal
    ys[0], ys[-1] = y0, y1
    return list(zip(xs, ys))


def arkaplan(seed=7, sahne=None, grafik=True, grafik_y=(1180, 600)):
    if sahne:  # Canva sahnesi: 16:9 → 2560x1440 kapla, hafif karart (metin kontrastı için)
        s = Image.open(sahne).convert("RGB")
        s = s.resize((W, int(s.height * W / s.width)), Image.LANCZOS) if s.width / s.height <= W / H else \
            s.resize((int(s.width * H / s.height), H), Image.LANCZOS)
        s = s.crop(((s.width - W) // 2, (s.height - H) // 2, (s.width - W) // 2 + W, (s.height - H) // 2 + H))
        kar = Image.new("RGB", (W, H), LACI_UST)
        return Image.blend(s, kar, 0.35).convert("RGBA")
    bg = dikey_gradyan(W, H, LACI_UST, LACI_ALT).convert("RGBA")
    izg = Image.new("RGBA", (W, H)); d = ImageDraw.Draw(izg)   # silik ızgara (ayrı katman: RGBA'ya doğrudan çizim karışmaz)
    for x in range(0, W, 128):
        d.line([(x, 0), (x, H)], fill=(120, 160, 255, 22), width=2)
    for y in range(SY % 106, H, 106):
        d.line([(0, y), (W, y)], fill=(120, 160, 255, 22), width=2)
    bg = Image.alpha_composite(bg, izg)
    r = np.random.default_rng(seed)
    # silüet şehir (2 katman), tepeler güvenli bant içine uzanır → masaüstü bantta görünür
    for katman, (renk, hmin, hmax, pen) in enumerate([((20, 40, 78), 260, 620, (255, 214, 120, 60)),
                                                      ((11, 23, 48), 160, 470, (255, 200, 61, 110))]):
        lay = Image.new("RGBA", (W, H)); ld = ImageDraw.Draw(lay)
        x = -40
        while x < W:
            bw = int(r.integers(70, 190)); bh = int(r.integers(hmin, hmax))
            ld.rectangle([x, H - bh, x + bw, H], fill=renk + (255,))
            if r.random() < 0.3:      # çatı anteni / basamak
                ld.rectangle([x + bw // 3, H - bh - 40, x + bw // 3 + 10, H - bh], fill=renk + (255,))
            for wy in range(H - bh + 24, H - 10, 34):
                for wx in range(x + 14, x + bw - 18, 26):
                    if r.random() < 0.16:
                        ld.rectangle([wx, wy, wx + 10, wy + 14], fill=pen)
            x += bw + int(r.integers(4, 22))
        bg = Image.alpha_composite(bg, lay)
    if grafik:
        bg = Image.alpha_composite(bg, cizgi_grafik(seed, y0=grafik_y[0], y1=grafik_y[1]))
    return bg


def cizgi_grafik(seed, x0=-20, x1=W - 120, y0=1180, y1=600, kalin=16):
    lay = Image.new("RGBA", (W, H))
    p = grafik_noktalari(seed, x0, x1, y0, y1)
    # alan dolgusu (yeşil, saydam)
    alan = Image.new("L", (W, H), 0)
    ImageDraw.Draw(alan).polygon(p + [(x1, H), (x0, H)], fill=60)
    alan = Image.fromarray((np.asarray(alan) * np.linspace(1, 0.15, H)[:, None]).astype(np.uint8))
    yesil = Image.new("RGBA", (W, H), YESIL + (0,)); yesil.putalpha(alan)
    lay = Image.alpha_composite(lay, yesil)
    # parlama + çizgi
    parla = Image.new("RGBA", (W, H)); ImageDraw.Draw(parla).line(p, fill=YESIL + (150,), width=kalin * 3, joint="curve")
    lay = Image.alpha_composite(lay, parla.filter(ImageFilter.GaussianBlur(18)))
    ld = ImageDraw.Draw(lay)
    ld.line(p, fill=YESIL + (255,), width=kalin, joint="curve")
    # ok başı
    (ax, ay), (bx, by) = p[-2], p[-1]
    v = np.array([bx - ax, by - ay]); v /= np.linalg.norm(v); nrm = np.array([-v[1], v[0]])
    uc = np.array([bx, by]) + v * 60
    ld.polygon([tuple(uc), tuple(np.array([bx, by]) + nrm * 38 - v * 6), tuple(np.array([bx, by]) - nrm * 38 - v * 6)],
               fill=YESIL + (255,))
    return lay


def karakter_yerlestir(bg, kar, cx, ust_y, yukseklik=None, kenar=10, isik=(255, 190, 90)):
    """Karakteri alt kenara oturt (bel kesiti tuval dışında kalır), sıcak arka ışık + açık kontur (lacivertte siyah gömlek ayrışsın).
    yukseklik > H - ust_y ise karakter tuvalin altından taşar (kafa büyür, el/kol bant dışına iner)."""
    yuk = max(yukseklik or 0, H - ust_y)
    olcek = yuk / kar.height
    k = kar.resize((round(kar.width * olcek), yuk), Image.LANCZOS)
    x = int(cx - k.width / 2)
    bg = Image.alpha_composite(bg, radyal(W, H, cx, ust_y + k.height * 0.35, k.height * 0.75, isik, 0.55))
    a = k.split()[3]
    kont = a.filter(ImageFilter.MaxFilter(kenar * 2 + 1)).filter(ImageFilter.GaussianBlur(1.2))
    kl = Image.new("RGBA", k.size, (255, 236, 200, 0)); kl.putalpha(kont)
    bg.alpha_composite(kl, (x, ust_y)); bg.alpha_composite(k, (x, ust_y))
    al = np.asarray(k)[..., 3] > 128; sol = int(np.argmax(al.any(0)))
    uc_y = ust_y + int(np.where(al[:, sol])[0].mean())          # en soldaki nokta (işaret eden el ucu)
    return bg, (x, ust_y, x + k.width, H), kafa_kutusu(k, x, ust_y), (x + sol, uc_y)


def metin_katmani(parcalar):
    """parcalar: [(metin, font, renk, (x,y), golge_px, kontur_px, kontur_renk)] → (RGBA katman, kutular, maskeler)"""
    lay = Image.new("RGBA", (W, H)); kutular = []
    for metin, f, renk, (x, y), golge, kontur, kr in parcalar:
        if golge:
            g = Image.new("RGBA", (W, H)); ImageDraw.Draw(g).text((x + golge * 0.4, y + golge), metin, font=f,
                                                                fill=(0, 0, 0, 170), stroke_width=kontur, stroke_fill=(0, 0, 0, 170))
            lay = Image.alpha_composite(lay, g.filter(ImageFilter.GaussianBlur(golge * 0.6)))
        d = ImageDraw.Draw(lay)
        d.text((x, y), metin, font=f, fill=renk + (255,), stroke_width=kontur, stroke_fill=(kr or LACI_KOYU) + (255,))
        m = Image.new("L", (W, H)); ImageDraw.Draw(m).text((x, y), metin, font=f, fill=255)
        kutular.append({"metin": metin, "renk": renk, "kutu": d.textbbox((x, y), metin, font=f, stroke_width=kontur),
                        "maske": m, "kontur": kontur, "kontur_renk": kr or LACI_KOYU})
    return lay, kutular


def hap(lay, kutu, renk, r=None):
    x0, y0, x1, y1 = kutu
    ImageDraw.Draw(lay).rounded_rectangle(kutu, radius=r or (y1 - y0) // 2, fill=renk + (255,))


def sigdir(metin, ad, genislik, maks=400):
    px = maks
    while px > 10 and font(ad, px).getbbox(metin)[2] > genislik:
        px -= 2
    return px


# ---------------------------------------------------------------- banner adayları
def metin_blogu(x0, x1, ust, slogan, ritim, hiza="sol", alt=None, ad_maks=210, ritim_px=54):
    """Kanal adı + slogan + yayın ritmi; dikeyde [ust, alt] içine sığar (alt varsayılan: bant altı - 34)."""
    alt = alt or (SY + SH - 34)
    gen = x1 - x0
    ad1, ad2 = "FINANCIAL ", "RISE"
    px = min(sigdir(ad1 + ad2, "Anton-400.woff2", gen), ad_maks)
    sl_px = min(sigdir(slogan, "Fredoka-700.woff2", gen), 64)
    fr = font("Anton-400.woff2", ritim_px); br = fr.getbbox(ritim)
    hap_h = (br[3] - br[1]) + 36
    while True:
        fa = font("Anton-400.woff2", px); b = fa.getbbox(ad1 + ad2)
        fs = font("Fredoka-700.woff2", sl_px); bs = fs.getbbox(slogan)
        top = (b[3] - b[1]) + 30 + (bs[3] - bs[1]) + 30 + hap_h
        if ust + top <= alt or px < 60:
            break
        px -= 4; sl_px = max(40, sl_px - 1)
    w1 = fa.getlength(ad1); tw = b[2]
    xs = x0 if hiza == "sol" else x0 + (gen - tw) // 2
    y_ad = ust - b[1]
    y_sl = ust + (b[3] - b[1]) + 30 - bs[1]
    xs_sl = xs if hiza == "sol" else x0 + (gen - bs[2]) // 2
    hy0 = y_sl + bs[3] + 30
    hx0 = xs if hiza == "sol" else x0 + (gen - (br[2] + 60)) // 2
    hk = (hx0, hy0, hx0 + br[2] + 60, hy0 + hap_h)
    parcalar = [(ad1, fa, BEYAZ, (xs, y_ad), 10, 0, None), (ad2, fa, ALTIN, (xs + w1, y_ad), 10, 0, None),
                (slogan, fs, BEYAZ, (xs_sl, y_sl), 6, 0, None),
                (ritim, fr, LACI_KOYU, (hx0 + 30, hy0 + 18 - br[1]), 0, 0, None)]
    return parcalar, hk


def banner(aday, a):
    if aday == "A":       # karakter solda (sevinçli) + şehir + yükselen grafik, metin sağda
        bg = arkaplan(sahne=a.arkaplan, grafik_y=(1330, 700))   # grafik metnin altından geçer
        kar = kes(a.banner_karakter)
        bg, kk, kafa, _ = karakter_yerlestir(bg, kar, SX + 300, SY + 22, yukseklik=a.a_yukseklik)
        uc = None
        parcalar, hk = metin_blogu(SX + 640, SX + SW - 30, SY + 48, a.slogan, a.ritim)
    elif aday == "B":     # karakter sağda ekranın soluna, metne işaret ediyor
        bg = arkaplan(sahne=a.arkaplan)
        kar = kes(a.banner_isaret)
        # işaret eden el kutunun solunda; yüz kutunun sağ ~%60'ında → yüzü güvenli alanın sağ kısmına koy
        bg, kk, kafa, uc = karakter_yerlestir(bg, kar, SX + SW - 300, SY + 40)
        parcalar, hk = metin_blogu(SX + 30, SX + 830, SY + 48, a.slogan, a.ritim)
    elif aday == "C":     # minimal logo-tipi: karakter yok, ortalı yazı + ok
        bg = arkaplan(sahne=a.arkaplan)
        kk = kafa = uc = None
        parcalar, hk = metin_blogu(SX + 120, SX + SW - 120, SY + 40, a.slogan, a.ritim, hiza="orta")
    else:
        raise SystemExit("aday A/B/C")
    lay = Image.new("RGBA", (W, H)); hap(lay, hk, ALTIN)
    mlay, kutular = metin_katmani(parcalar)
    zemin = Image.alpha_composite(bg, lay)       # hap dahil, metin hariç → kontrast ölçümü zemini
    son = Image.alpha_composite(zemin, mlay).convert("RGB")
    return son, zemin.convert("RGB"), kutular, kk, hk, kafa, uc


def kontrast(zemin, kutular):
    z = np.asarray(zemin); sonuc = []
    for k in kutular:
        m = np.asarray(k["maske"]) > 0
        x0, y0, x1, y1 = (int(round(v)) for v in k["kutu"])
        pad = 12
        bolge = np.zeros_like(m); bolge[max(0, y0 - pad):y1 + pad, max(0, x0 - pad):x1 + pad] = True
        arka = z[bolge & ~m]
        r = wcag(lum(k["renk"]), lum(arka))
        sonuc.append({"metin": k["metin"].strip(), "dolgu": "#%02x%02x%02x" % k["renk"],
                      "wcag_en_kotu_%5": round(float(np.percentile(r, 5)), 2), "wcag_medyan": round(float(np.median(r)), 2),
                      "kutu": [int(v) for v in k["kutu"]]})
    return sonuc


def guvenli_alan_testi(kutular, kk, hk, yuz_kutu=None):
    sorun = []
    def icinde(b, ad):
        if not (b[0] >= SX and b[1] >= SY and b[2] <= SX + SW and b[3] <= SY + SH):
            sorun.append({"oge": ad, "kutu": [int(v) for v in b]})
    for k in kutular:
        icinde(k["kutu"], k["metin"].strip())
    icinde(hk, "ritim hapı")
    if yuz_kutu:
        icinde(yuz_kutu, "karakter kafası")
    return sorun


def kafa_kutusu(k, x, y):
    """Kafa kutusu: alfa maskesinin en üst noktasını içeren bileşen, karakter boyunun üst %22'si."""
    import cv2
    a = (np.asarray(k)[..., 3] > 128).astype(np.uint8)
    ust = int(np.argmax(a.any(1))); h = int(k.height * 0.22)
    dilim = a[ust:ust + h].copy()
    n, lab = cv2.connectedComponents(dilim, 8)
    tx = int(np.argmax(dilim[0])); c = lab[0, tx]
    ys, xs = np.where(lab == c)
    return (x + int(xs.min()), y + ust + int(ys.min()), x + int(xs.max()), y + ust + int(ys.max()))


def onizleme(son, ad, hedef):
    os.makedirs(hedef, exist_ok=True)
    # 1) bölge çizgili tam görünüm
    g = son.copy().convert("RGBA"); d = ImageDraw.Draw(g)
    renk = {"tv": (255, 255, 255), "masaustu": (80, 200, 255), "tablet": (255, 160, 60), "mobil": (255, 60, 60)}
    for k, (x0, y0, x1, y1) in KIRPMA.items():
        d.rectangle([x0 + 3, y0 + 3, x1 - 4, y1 - 4], outline=renk[k] + (255,), width=6)
        d.text((x0 + 16, y0 + 10), k.upper(), font=font("Anton-400.woff2", 40), fill=renk[k] + (255,))
    g.convert("RGB").resize((1280, 720), Image.LANCZOS).save(os.path.join(hedef, f"{ad}-bolgeler.jpg"), quality=88)
    # 2) cihaz kırpmaları (gerçek ekran genişliğine yakın ölçek: masaüstü ~1284, telefon ~390 CSS px)
    satirlar = []
    tv = son.resize((960, 540), Image.LANCZOS); satirlar.append(("TV (tam tuval, 960 px'e ölçekli)", tv))
    ms = son.crop(KIRPMA["masaustu"]).resize((1284, round(1284 * SH / W)), Image.LANCZOS)
    satirlar.append(("Masaüstü (2560x423 bant, 1284 px genişlikte)", ms))
    tb = son.crop(KIRPMA["tablet"]).resize((960, round(960 * SH / 1855)), Image.LANCZOS)
    satirlar.append(("Tablet (1855x423, 960 px)", tb))
    mb = son.crop(KIRPMA["mobil"]); mb1 = mb.resize((390, round(390 * SH / SW)), Image.LANCZOS)
    satirlar.append(("Mobil (1546x423, 390 CSS px = gerçek telefon boyu)", mb1))
    satirlar.append(("Mobil x3 cihaz pikseli (1170 px)", mb.resize((1170, round(1170 * SH / SW)), Image.LANCZOS)))
    gw = 1320; gh = sum(im.height + 60 for _, im in satirlar) + 20
    sheet = Image.new("RGB", (gw, gh), (235, 235, 235)); sd = ImageDraw.Draw(sheet); y = 10
    for t, im in satirlar:
        sd.text((18, y + 8), t, font=etiket(24), fill=(20, 20, 20)); y += 48
        sheet.paste(im, (18, y)); y += im.height + 12
    sheet.save(os.path.join(hedef, f"{ad}-kirpmalar.jpg"), quality=88)
    return mb1


# ---------------------------------------------------------------- profil adayları
def buyut_esrgan(img):
    """Real-ESRGAN x4 (yerel ağırlık). Yoksa LANCZOS."""
    w = os.path.expanduser("~/.finansal-arac/RealESRGAN_x4.pth")
    try:
        import torch, spandrel
        m = spandrel.ModelLoader().load_from_file(w).eval()
        torch.set_num_threads(os.cpu_count() or 4)
        x = torch.from_numpy(np.asarray(img.convert("RGB")).astype(np.float32) / 255).permute(2, 0, 1)[None]
        with torch.no_grad():
            y = m(x).clamp(0, 1)[0].permute(1, 2, 0).numpy()
        return Image.fromarray((y * 255).round().astype(np.uint8))
    except Exception as e:
        print("  ESRGAN kullanılamadı, LANCZOS:", e)
        return img.resize((img.width * 4, img.height * 4), Image.LANCZOS)


def portre_kes(yol, esrgan=True, onbellek=None, oran=0.47):
    """Kafa+omuz kare kesimi (RGBA, 1600x1600). Kafa tepesi alfa maskesinden bulunur."""
    if onbellek and os.path.exists(onbellek):
        return Image.open(onbellek).convert("RGBA")
    kar = kes(yol)
    a = np.asarray(kar)[..., 3] > 128
    ust = np.argmax(a.any(1))
    satir = a[ust:ust + int(kar.height * 0.25)]
    xs = np.where(satir.any(0))[0]; cx = int((xs.min() + xs.max()) / 2)
    kenar = int(kar.height * oran)           # kare boyu: kafa dairenin ~%75'i (36 px'te yüz seçilsin)
    x0 = cx - kenar // 2; y0 = max(0, ust - int(kenar * 0.07))
    kare = Image.new("RGBA", (kenar, kenar)); kare.alpha_composite(kar.crop((x0, y0, x0 + kenar, y0 + kenar)))
    if esrgan:
        rgb = Image.new("RGB", kare.size, (128, 128, 128)); rgb.paste(kare, mask=kare.split()[3])
        b = buyut_esrgan(rgb).resize((1600, 1600), Image.LANCZOS)
        al = kare.split()[3].resize((1600, 1600), Image.LANCZOS)
        # kenar rengini düzelt: alfa sınırında gri karışımı yerine orijinalin büyütmesini kullan
        org = kare.resize((1600, 1600), Image.LANCZOS)
        mix = np.where((np.asarray(al) > 250)[..., None], np.asarray(b), np.asarray(org)[..., :3])
        p = Image.fromarray(mix.astype(np.uint8)).convert("RGBA"); p.putalpha(al)
    else:
        p = kare.resize((1600, 1600), Image.LANCZOS)
    if onbellek:
        p.save(onbellek)
    return p


def profil(aday, a, portre):
    """P1 lacivert zemin + altın halka (marka) · P4 yeşil zemin · P2 FR monogramı · P3 P1 + ok rozeti."""
    S = 1600
    if aday in ("P1", "P3", "P4"):
        if aday == "P4":
            bg = Image.new("RGBA", (S, S), YESIL + (255,))
        else:
            bg = dikey_gradyan(S, S, LACI_ALT, LACI_UST).convert("RGBA")
            bg = Image.alpha_composite(bg, radyal(S, S, S / 2, S * 0.42, S * 0.62, (255, 190, 90), 0.55))
        # yükselen grafik (zeminde, yüzün arkasında)
        gl = Image.new("RGBA", (S, S)); d = ImageDraw.Draw(gl)
        p = grafik_noktalari(3, 0, S, S * 0.86, S * 0.22, n=10)
        d.line(p, fill=(BEYAZ if aday == "P4" else YESIL) + (255,), width=46, joint="curve")
        bg = Image.alpha_composite(bg, gl)
        kont = portre.split()[3].filter(ImageFilter.MaxFilter(29)).filter(ImageFilter.GaussianBlur(1.5))
        kl = Image.new("RGBA", portre.size, (255, 240, 210, 0)); kl.putalpha(kont)
        bg.alpha_composite(kl, (0, 40)); bg.alpha_composite(portre, (0, 40))
        if aday != "P4":   # daire kenarında altın halka (koyu temada daireyi belirginleştirir)
            ImageDraw.Draw(bg).ellipse([22, 22, S - 22, S - 22], outline=ALTIN + (255,), width=44)
        if aday == "P3":   # sağ altta yükselen ok rozeti
            r = 230; cx, cy = S - 360, S - 360
            dd = ImageDraw.Draw(bg)
            dd.ellipse([cx - r, cy - r, cx + r, cy + r], fill=YESIL + (255,), outline=BEYAZ + (255,), width=26)
            ok = [(cx - 120, cy + 90), (cx - 20, cy - 10), (cx + 30, cy + 40), (cx + 110, cy - 50)]
            dd.line(ok, fill=BEYAZ + (255,), width=46, joint="curve")
            dd.polygon([(cx + 150, cy - 95), (cx + 40, cy - 85), (cx + 140, cy + 15)], fill=BEYAZ + (255,))
    elif aday == "P2":     # FR monogramı + ok
        bg = dikey_gradyan(S, S, LACI_ALT, LACI_UST).convert("RGBA")
        f = font("Anton-400.woff2", 900)
        d = ImageDraw.Draw(bg); bb = d.textbbox((0, 0), "FR", font=f)
        x = (S - (bb[2] - bb[0])) // 2 - bb[0]; y = (S - (bb[3] - bb[1])) // 2 - bb[1] + 40
        d.text((x, y), "F", font=f, fill=BEYAZ + (255,)); d.text((x + f.getlength("F"), y), "R", font=f, fill=ALTIN + (255,))
        p = grafik_noktalari(5, 260, S - 300, S * 0.80, S * 0.24, n=7)
        d.line(p, fill=YESIL + (255,), width=60, joint="curve")
        (ax, ay), (bx, by) = p[-2], p[-1]
        v = np.array([bx - ax, by - ay]); v /= np.linalg.norm(v); n = np.array([-v[1], v[0]])
        d.polygon([tuple(np.array([bx, by]) + v * 110), tuple(np.array([bx, by]) + n * 80), tuple(np.array([bx, by]) - n * 80)], fill=YESIL + (255,))
    else:
        raise SystemExit("profil P1/P2/P3/P4")
    return bg.convert("RGB").resize((800, 800), Image.LANCZOS)


def daire_onizleme(p, boyutlar=(98, 36)):
    out = []
    for s in boyutlar:
        k = p.resize((s, s), Image.LANCZOS).convert("RGBA")
        m = Image.new("L", (s * 4, s * 4)); ImageDraw.Draw(m).ellipse([0, 0, s * 4 - 1, s * 4 - 1], fill=255)
        k.putalpha(m.resize((s, s), Image.LANCZOS)); out.append(k)
    return out


def lab(c):
    import cv2
    a = np.asarray(c, dtype=np.uint8).reshape(-1, 1, 3)
    L = cv2.cvtColor(a, cv2.COLOR_RGB2LAB).reshape(-1, 3).astype(np.float64)
    return np.column_stack([L[:, 0] * 100 / 255, L[:, 1] - 128, L[:, 2] - 128])


def profil_olc(p):
    """Daire içi ölçüm: zemin = halkanın hemen içi (r 0.80–0.88) medyanı; ten ve saç/gömlek (koyu) medyanları.
    WCAG oranı yalnız parlaklık; ΔE76 renk tonu farkını da yakalar (ten-yeşil gibi)."""
    a = np.asarray(p.convert("RGB")); s = a.shape[0]
    yy, xx = np.mgrid[0:s, 0:s]; r = np.sqrt((xx - s / 2) ** 2 + (yy - s / 2) ** 2) / (s / 2)
    zem = a[(r > 0.80) & (r < 0.88) & (yy < s * 0.45)]          # üst halka: karakterin dışı
    z = np.median(zem, 0); Lz = float(lum(z))
    ic = a[r < 0.75].astype(int); R, G, B = ic[:, 0], ic[:, 1], ic[:, 2]
    ten = ic[(R > G) & (G > B) & (R - B > 60) & (R > 150)]
    koyu = ic[ic.max(1) < 60]
    out = {"zemin_rgb": [int(v) for v in z], "ten_orani_daire_ici": round(len(ten) / len(ic), 3)}
    if len(ten):
        t = np.median(ten, 0)
        out["ten_zemin_wcag"] = round(float(wcag(lum(t), Lz)), 2)
        out["ten_zemin_dE76"] = round(float(np.linalg.norm(lab([t])[0] - lab([z])[0])), 1)
    if len(koyu):
        k = np.median(koyu, 0)
        out["sac_gomlek_zemin_wcag"] = round(float(wcag(lum(k), Lz)), 2)
    return out


# ---------------------------------------------------------------- ana akış
def main():
    ap = argparse.ArgumentParser()
    pk = os.path.join(KOK, "assets", "karakter", "paket-v1")
    ap.add_argument("--banner-karakter", default=os.path.join(pk, "f-sevincli.png"))
    ap.add_argument("--banner-isaret", default=os.path.join(pk, "c-isaret.png"))
    ap.add_argument("--profil-karakter", default=os.path.join(pk, "a-konusma-kapali.png"))
    ap.add_argument("--arkaplan", default=None, help="Canva 16:9 sahne (opsiyonel); yoksa kodla çizilir")
    ap.add_argument("--slogan", default="Money stories, animated.")
    ap.add_argument("--slogan-alt", default="Past crashes. Today's news. What's next.")
    ap.add_argument("--ritim", default="NEW VIDEOS  TUE · FRI · SUN")
    ap.add_argument("--cikis", default=os.path.join(KOK, "uretim", "kanal-kimligi"))
    ap.add_argument("--adaylar", default="A,B,C")
    ap.add_argument("--profil-adaylar", default="P1,P2,P3,P4")
    ap.add_argument("--kazanan-banner", default=None)
    ap.add_argument("--kazanan-profil", default=None)
    ap.add_argument("--a-yukseklik", type=int, default=1140, help="A adayında karakter boyu (px); >918 ise tuval altından taşar")
    ap.add_argument("--esrgan", type=int, default=1)
    a = ap.parse_args()
    on = os.path.join(a.cikis, "onizleme"); os.makedirs(on, exist_ok=True)
    olc = {"guvenli_alan": [SX, SY, SX + SW, SY + SH], "banner": {}, "profil": {}}

    for aday in [x for x in a.adaylar.split(",") if x]:
        for si, sl in enumerate([a.slogan, a.slogan_alt]):
            a2 = argparse.Namespace(**{**vars(a), "slogan": sl})
            son, zemin, kutular, kk, hk, kafa, uc = banner(aday, a2)
            ad = f"banner-{aday}-s{si + 1}"
            yol = os.path.join(on, ad + ".jpg"); son.save(yol, quality=92, optimize=True, subsampling=0)
            mb = onizleme(son, ad, on)
            # mobil gerçek boyda metin yüksekliği (CSS px): kutu yüksekliği x 390/1546
            yuk = {k["metin"].strip(): round((k["kutu"][3] - k["kutu"][1]) * 390 / SW, 1) for k in kutular}
            olc["banner"][ad] = {"slogan": sl, "kontrast": kontrast(zemin, kutular),
                                 "guvenli_alan_tasmasi": guvenli_alan_testi(kutular, kk, hk, kafa),
                                 "karakter_kutusu": [int(v) for v in kk] if kk else None,
                                 "kafa_kutusu": [int(v) for v in kafa] if kafa else None,
                                 "isaret_eli_ucu": list(uc) if uc else None,
                                 "isaret_eli_mobil_bantta": (SX <= uc[0] <= SX + SW and SY <= uc[1] <= SY + SH) if uc else None,
                                 "mobil_390px_metin_yuksekligi_css_px": yuk,
                                 "dosya_bayt": os.path.getsize(yol)}
            print(ad, json.dumps(olc["banner"][ad]["guvenli_alan_tasmasi"]), yuk)

    portre = None
    for aday in [x for x in a.profil_adaylar.split(",") if x]:
        if aday != "P2" and portre is None:
            portre = portre_kes(a.profil_karakter, bool(a.esrgan), os.path.join(on, "_portre-" + os.path.splitext(os.path.basename(a.profil_karakter))[0] + "-047.png"))
        p = profil(aday, a, portre)
        yol = os.path.join(on, f"profil-{aday}.png"); p.save(yol, optimize=True)
        olc["profil"][aday] = {**profil_olc(p), "dosya_bayt": os.path.getsize(yol)}
    # profil karşılaştırma tablosu: 800 / 98 / 36 (gerçek boy) + 36'nın x4 büyütmesi (göz için)
    if olc["profil"]:
        ads = list(olc["profil"]); sheet = Image.new("RGB", (len(ads) * 420 + 20, 620), (249, 249, 249))
        sd = ImageDraw.Draw(sheet)
        for i, ad in enumerate(ads):
            p = Image.open(os.path.join(on, f"profil-{ad}.png")); x = 20 + i * 420
            k98, k36 = daire_onizleme(p)
            sd.text((x, 10), ad, font=font("Anton-400.woff2", 36), fill=(0, 0, 0))
            sheet.paste(p.resize((300, 300), Image.LANCZOS), (x, 60))
            sheet.paste(k98, (x, 380), k98); sheet.paste(k36, (x + 120, 380), k36)
            b36 = k36.resize((144, 144), Image.NEAREST); sheet.paste(b36, (x + 180, 380), b36)
            sd.text((x, 540), "98 px · 36 px · 36 px x4", font=etiket(20), fill=(60, 60, 60))
        sheet.save(os.path.join(on, "profil-karsilastirma.png"))
        # koyu temada da (YouTube karanlık mod #0f0f0f)
        sheet2 = Image.new("RGB", sheet.size, (15, 15, 15)); sheet2.paste(sheet.crop((0, 370, sheet.width, 540)), (0, 0))
        sheet2.crop((0, 0, sheet.width, 170)).save(os.path.join(on, "profil-karsilastirma-koyu.png"))

    if a.kazanan_banner:
        aday, _, s = a.kazanan_banner.partition("-")
        a2 = argparse.Namespace(**{**vars(a), "slogan": a.slogan_alt if s == "s2" else a.slogan})
        son, *_ = banner(aday, a2)
        hedef = os.path.join(a.cikis, "banner-2560x1440.jpg")
        for q in (92, 88, 84, 80):
            son.save(hedef, quality=q, optimize=True, subsampling=0)
            if os.path.getsize(hedef) <= 6 * 1024 * 1024:
                break
        olc["kazanan_banner"] = {"aday": a.kazanan_banner, "boyut": list(son.size), "jpeg_kalite": q,
                                 "dosya_bayt": os.path.getsize(hedef)}
    if a.kazanan_profil:
        if a.kazanan_profil != "P2" and portre is None:
            portre = portre_kes(a.profil_karakter, bool(a.esrgan), os.path.join(on, "_portre-" + os.path.splitext(os.path.basename(a.profil_karakter))[0] + "-047.png"))
        p = profil(a.kazanan_profil, a, portre)
        hedef = os.path.join(a.cikis, "profil-800.png"); p.save(hedef, optimize=True)
        olc["kazanan_profil"] = {"aday": a.kazanan_profil, "boyut": list(p.size), "dosya_bayt": os.path.getsize(hedef)}
    with open(os.path.join(on, "olcumler.json"), "w") as f:
        json.dump(olc, f, ensure_ascii=False, indent=1)
    print(json.dumps({k: v for k, v in olc.items() if k != "banner"}, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
