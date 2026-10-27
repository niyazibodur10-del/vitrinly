#!/usr/bin/env python3
"""F8 thumbnail üretimi + testler — S03 "You Have $1,000 in 1929. Can You Keep It?"

Kullanım:  python3 thumb-uret.py            (tüm adaylar + testler)
Çıktı:     bu klasör (adaylar/, test/, olcum.json); finalistler kökte A/B/C.
Metin her zaman kodla yazılır (Anton, video/public/fonts). Görseller yalnız mevcut
Canva varlıkları (05-gorsel/canva-ham, leo/). Yeni Canva üretimi yok.
"""
import io, json, math, os, sys, hashlib
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageEnhance

KOK = os.path.dirname(os.path.abspath(__file__))
VID = os.path.abspath(os.path.join(KOK, "..", ".."))
REPO = os.path.abspath(os.path.join(VID, "..", ".."))
G = os.path.join(VID, "05-gorsel")
W, H = 1280, 720
LAC = (11, 16, 38)          # kontur / bant lacivert
BEYAZ = (255, 255, 255)
SARI = (255, 210, 63)       # #FFD23F vurgu (konsept §1)
SURE_KUTU = (1088, 634, 1280, 720)   # sağ alt süre damgası, boş kalmalı

# ---------- yazı tipi ----------
_FCACHE = {}
def font(px, ad="Anton-400"):
    k = (ad, px)
    if k not in _FCACHE:
        ttf = os.path.join(os.environ.get("THUMB_TMP", "/tmp"), ad + ".ttf")
        if not os.path.exists(ttf):
            from fontTools.ttLib import TTFont
            f = TTFont(os.path.join(REPO, "video/public/fonts", ad + ".woff2")); f.flavor = None; f.save(ttf)
        _FCACHE[k] = ImageFont.truetype(ttf, px)
    return _FCACHE[k]

def cap_yuk(px, ad="Anton-400"):
    b = font(px, ad).getbbox("H"); return b[3] - b[1]

# ---------- yardımcılar ----------
def yukle(yol, mod="RGBA"):
    return Image.open(os.path.join(G, yol)).convert(mod)

def kafa_degis(govde, kafa, dx=0, dy=0, y_kes=392, yumus=14):
    """Aynı kadrajlı bel üstü pozlarda (kafa kayması ≤%0,6, 05-gorsel/rapor.md) kafayı değiştirir.
    Maske: kafa+boyun, y_kes çizgisinde yumuşak geçiş (yaka aynı)."""
    k = Image.new("RGBA", govde.size, (0, 0, 0, 0)); k.paste(kafa, (dx, dy))
    m = Image.new("L", govde.size, 0); d = ImageDraw.Draw(m)
    d.ellipse((790 + dx, -60 + dy, 1100 + dx, y_kes + 30 + dy), fill=255)
    d.rectangle((790 + dx, -60 + dy, 1100 + dx, 200 + dy), fill=255)
    m = m.filter(ImageFilter.GaussianBlur(yumus))
    a = np.array(m).astype(np.float32) / 255
    a[(y_kes + dy + 30):, :] = 0
    m = Image.fromarray((a * 255).astype(np.uint8))
    out = govde.copy(); out.paste(k, (0, 0), Image.fromarray(np.minimum(np.array(m), np.array(k.split()[3]))))
    # gövde alfası kafa alfasıyla birleşsin (saç taşması)
    al = np.maximum(np.array(govde.split()[3]), (np.array(k.split()[3]) * (np.array(m) / 255)).astype(np.uint8))
    out.putalpha(Image.fromarray(al))
    return out

def yerlestir(tuval, kesik, olcek, x, y, isik=None, golge=True):
    """kesik (1920x1080 RGBA) → olcek, sol-üst (x,y). isik: sıcak kenar ışığı rengi."""
    k = kesik.resize((int(kesik.width * olcek), int(kesik.height * olcek)), Image.LANCZOS)
    if golge:
        a = k.split()[3].filter(ImageFilter.GaussianBlur(18))
        sh = Image.new("RGBA", k.size, (0, 0, 0, 0)); sh.putalpha(a.point(lambda v: int(v * 0.55)))
        tuval.alpha_composite(sh, (x + 10, y + 14)) if x + 10 >= 0 and y + 14 >= 0 else _yap(tuval, sh, x + 10, y + 14)
    if isik:
        a = np.array(k.split()[3]).astype(np.float32)
        ic = np.array(k.split()[3].filter(ImageFilter.GaussianBlur(6))).astype(np.float32)
        kenar = np.clip((a - ic) * 2.2, 0, 255).astype(np.uint8)
        rim = Image.new("RGBA", k.size, isik + (0,)); rim.putalpha(Image.fromarray(kenar).filter(ImageFilter.GaussianBlur(3)))
        _yap(tuval, k, x, y); _yap(tuval, rim, x, y)
    else:
        _yap(tuval, k, x, y)
    return tuval

def _yap(tuval, img, x, y):
    t = Image.new("RGBA", tuval.size, (0, 0, 0, 0)); t.paste(img, (x, y), img); tuval.alpha_composite(t)

def radyal(w, h, cx, cy, r, renk, guc):
    yy, xx = np.mgrid[0:h, 0:w]; d = np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2) / r
    a = np.clip(1 - d, 0, 1) ** 2 * guc * 255
    im = Image.new("RGBA", (w, h), renk + (0,)); im.putalpha(Image.fromarray(a.astype(np.uint8))); return im

def karart(img, k):
    return ImageEnhance.Brightness(img).enhance(k)

def plaka(yol, olcek, ox, oy, blur=0, parlak=1.0):
    p = Image.open(os.path.join(G, yol)).convert("RGB")
    p = p.resize((int(p.width * olcek), int(p.height * olcek)), Image.LANCZOS).crop((ox, oy, ox + W, oy + H))
    if blur: p = p.filter(ImageFilter.GaussianBlur(blur))
    if parlak != 1.0: p = karart(p, parlak)
    return p.convert("RGBA")

# ---------- metin ----------
def metin(lay, kutular, x, y, parcalar, px, kontur=None, golge=True, hiza="sol"):
    """parcalar: [(yazı, renk), ...] tek satır. Döner: satır bbox. kutular'a her parça eklenir."""
    f = font(px); kon = kontur if kontur is not None else max(6, px // 11)
    gen = sum(f.getlength(t) for t, _ in parcalar) + f.getlength(" ") * 0
    if hiza == "orta": x = int(x - gen / 2)
    if hiza == "sag": x = int(x - gen)
    d = ImageDraw.Draw(lay)
    cx = x
    for t, renk in parcalar:
        if golge:
            sh = Image.new("RGBA", lay.size, (0, 0, 0, 0))
            ImageDraw.Draw(sh).text((cx + 6, y + 8), t, font=f, fill=(0, 0, 0, 170), stroke_width=kon, stroke_fill=(0, 0, 0, 170))
            lay.alpha_composite(sh.filter(ImageFilter.GaussianBlur(6)))
        d = ImageDraw.Draw(lay)
        d.text((cx, y), t, font=f, fill=renk + (255,), stroke_width=kon, stroke_fill=LAC + (255,))
        b = d.textbbox((cx, y), t, font=f)
        kutular.append({"metin": t, "renk": renk, "bbox": [b[0], b[1], b[2], b[3]], "px": px, "kontur": kon})
        cx += f.getlength(t)
    return (x, y, cx, y + px)

def sigdir(satir, gen, maks):
    px = maks
    while px > 20 and font(px).getlength(satir) > gen: px -= 2
    return px

# ---------- grafik (C): Dow çapaları 03-metin/veri/dow-capalari-FRH.csv ----------
DOW = [(1921 + 7.5 / 12, 63.0), (1929 + 8.1 / 12, 381.17), (1929 + 10.5 / 12, 190.6), (1932 + 6.25 / 12, 41.22)]

def dow_cizgi(lay, x0, x1, y0, y1, kalin=16):
    t0, t1 = DOW[0][0], DOW[-1][0]
    pts = [(x0 + (t - t0) / (t1 - t0) * (x1 - x0), y1 - v / 400 * (y1 - y0)) for t, v in DOW]
    gl = Image.new("RGBA", lay.size, (0, 0, 0, 0)); dg = ImageDraw.Draw(gl)
    dg.line(pts, fill=(80, 170, 255, 200), width=kalin * 3, joint="curve")
    lay.alpha_composite(gl.filter(ImageFilter.GaussianBlur(14)))
    d = ImageDraw.Draw(lay)
    d.line(pts, fill=LAC + (255,), width=kalin + 8, joint="curve")
    d.line(pts, fill=(63, 169, 255, 255), width=kalin, joint="curve")
    for i in (1, 3):
        x, y = pts[i]; r = kalin * 0.9
        d.ellipse((x - r, y - r, x + r, y + r), fill=BEYAZ + (255,), outline=LAC + (255,), width=5)
    return pts

def kilit(lay, cx, cy, s):
    d = ImageDraw.Draw(lay)
    d.arc((cx - 0.55 * s, cy - 1.25 * s, cx + 0.55 * s, cy - 0.05 * s), 180, 360, fill=LAC + (255,), width=int(0.34 * s))
    d.arc((cx - 0.55 * s, cy - 1.25 * s, cx + 0.55 * s, cy - 0.05 * s), 180, 360, fill=(200, 205, 215, 255), width=int(0.2 * s))
    d.line((cx - 0.55 * s, cy - 0.65 * s, cx - 0.55 * s, cy - 0.1 * s), fill=(200, 205, 215, 255), width=int(0.2 * s))
    d.line((cx + 0.55 * s, cy - 0.65 * s, cx + 0.55 * s, cy - 0.1 * s), fill=(200, 205, 215, 255), width=int(0.2 * s))
    d.rounded_rectangle((cx - 0.85 * s, cy - 0.2 * s, cx + 0.85 * s, cy + 1.0 * s), radius=int(0.15 * s), fill=SARI + (255,), outline=LAC + (255,), width=int(0.08 * s))
    d.ellipse((cx - 0.13 * s, cy + 0.2 * s, cx + 0.13 * s, cy + 0.46 * s), fill=LAC + (255,))
    d.rectangle((cx - 0.05 * s, cy + 0.4 * s, cx + 0.05 * s, cy + 0.72 * s), fill=LAC + (255,))

# ---------- varyantlar ----------
def leo_saskin_kutulu():
    return kafa_degis(yukle("leo/C14-kutu-gogus.png"), yukle("leo/d-saskin.png"))

def varyant_A(metin_id):
    bg = plaka("canva-ham/C01.png", 0.80, 330, 95, parlak=0.95)
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); kut = []
    # kapı üstü dev "?" (konsept A: ikon yerine büyük soru işareti); kapılar C01 json → 0.80 ölçek, -330/-95
    kj = json.load(open(os.path.join(G, "kapilar/C01-kapi-koordinatlari.json")))["kapilar"]
    for ad in ("mavi", "yesil", "kahve"):
        x, y, w, h = kj[ad]["panel_bbox_xywh"]
        cx = (x + w / 2) * 0.80 - 330; cy = (y + h / 2) * 0.80 - 95
        if ad == "kahve":   # kahve kapıdan sızan sıcak ışık (sürpriz ipucu)
            bg.alpha_composite(radyal(W, H, int(cx), int(cy), 260, (255, 190, 90), 0.55))
        f = font(190); b = f.getbbox("?"); gw = b[2] - b[0]
        ImageDraw.Draw(lay).text((cx - gw / 2 - b[0], cy - 120), "?", font=f, fill=BEYAZ + (255,), stroke_width=12, stroke_fill=LAC + (255,))
    leo = yukle("leo/c-isaret.png")
    yerlestir(bg, leo, 0.86, 1035 - int(990 * 0.86), 150, isik=(255, 200, 120))
    bg.alpha_composite(lay); lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    if metin_id == "A1":
        px = sigdir("PICK A DOOR", 900, 150); metin(lay, kut, 40, 18, [("PICK A ", BEYAZ), ("DOOR", SARI)], px)
    else:
        px = sigdir("ONE IS A DISASTER", 1000, 150); metin(lay, kut, 40, 18, [("ONE IS A ", BEYAZ), ("DISASTER", SARI)], px)
    return bg, lay, kut

def varyant_B(metin_id):
    bg = plaka("canva-ham/C01.png", 1.25, 1150, 160, blur=7, parlak=0.55)
    bg.alpha_composite(radyal(W, H, 400, 560, 520, (255, 190, 80), 0.75))
    leo = leo_saskin_kutulu()
    s = 0.80; ox, oy = 400 - int(945 * s), -12
    # kutu arkasında altın parıltı (S12 "banknotlar parlar"; kutu içi gösterilmez, rakam yok)
    kx0, ky0, kx1, ky1 = 700 * s + ox, 660 * s + oy, 1180 * s + ox, 880 * s + oy
    bg.alpha_composite(radyal(W, H, int((kx0 + kx1) / 2), int(ky0), 330, (255, 215, 110), 0.95))
    yerlestir(bg, leo, s, ox, oy, isik=(255, 210, 130))
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); kut = []
    # kutu üstü "1929" damgası (kod)
    dam = Image.new("RGBA", (300, 120), (0, 0, 0, 0)); dd = ImageDraw.Draw(dam)
    dd.rounded_rectangle((6, 6, 294, 114), radius=10, outline=(110, 40, 25, 235), width=8)
    f = font(84); b = dd.textbbox((0, 0), "1929", font=f)
    dd.text(((300 - (b[2] - b[0])) / 2 - b[0], (120 - (b[3] - b[1])) / 2 - b[1]), "1929", font=f, fill=(110, 40, 25, 235))
    dam = dam.rotate(7, resample=Image.BICUBIC, expand=True)
    dx, dy = int((kx0 + kx1) / 2 - dam.width / 2), int(ky0 + 40)
    lay.alpha_composite(dam, (dx, dy))
    kut.append({"metin": "1929", "renk": (110, 40, 25), "bbox": [dx, dy, dx + dam.width, dy + dam.height], "px": 84, "kontur": 0, "damga": True})
    satirlar = [("THE", BEYAZ), ("SURPRISE", SARI), ("DOOR", BEYAZ)] if metin_id == "B1" else [("EVERYONE", BEYAZ), ("LAUGHED", SARI)]
    gen = 500; px = min(sigdir(t, gen, 190) for t, _ in satirlar)
    y = 40 if len(satirlar) == 3 else 110
    for t, r in satirlar:
        metin(lay, kut, 1235, y, [(t, r)], px, hiza="sag"); y += int(px * 1.02)
    return bg, lay, kut

def varyant_C(metin_id):
    bg = plaka("canva-ham/C01.png", 0.9, 290, 120, blur=9, parlak=0.38)
    lay0 = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    d = ImageDraw.Draw(lay0)
    for gx in range(540, 1240, 70): d.line((gx, 215, gx, 600), fill=(90, 120, 200, 45), width=2)
    for gy in range(215, 601, 64): d.line((540, gy, 1220, gy), fill=(90, 120, 200, 45), width=2)
    dow_cizgi(lay0, 560, 1060, 215, 600, kalin=18)
    bg.alpha_composite(lay0)
    leo = yukle("leo/d-saskin.png")
    yerlestir(bg, leo, 0.86, 260 - int(947 * 0.86), 120, isik=(255, 200, 120))
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); kut = []
    if metin_id == "C1":
        px = sigdir("STOCKS −89%", 720, 170); metin(lay, kut, 1240, 16, [("STOCKS ", BEYAZ), ("−89%", SARI)], px, hiza="sag")
    else:
        px = sigdir("THE −89% DOOR", 720, 170); metin(lay, kut, 1240, 16, [("THE ", BEYAZ), ("−89%", SARI), (" DOOR", BEYAZ)], px, hiza="sag")
    return bg, lay, kut

def varyant_D(metin_id):
    # yeşil kapıya punch-in + kod asma kilit (S17 "MARCH 1933")
    bg = plaka("canva-ham/C01.png", 1.35, 980, 280, parlak=0.85)
    kj = json.load(open(os.path.join(G, "kapilar/C01-kapi-koordinatlari.json")))["kapilar"]["yesil"]
    x, y, w, h = kj["panel_bbox_xywh"]; cx = (x + w / 2) * 1.35 - 980; cy = (y + h / 2) * 1.35 - 280
    lay0 = Image.new("RGBA", (W, H), (0, 0, 0, 0)); kilit(lay0, int(cx), int(cy) + 10, 95); bg.alpha_composite(lay0)
    leo = yukle("leo/d-saskin.png")
    yerlestir(bg, leo, 0.86, 1020 - int(947 * 0.86), 120, isik=(255, 200, 120))
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); kut = []
    satirlar = [("EVERY BANK", BEYAZ), ("CLOSED", SARI)] if metin_id == "D1" else [("MARCH", BEYAZ), ("1933", SARI)]
    px = min(sigdir(t, 560, 170) for t, _ in satirlar); yy = 30
    for t, r in satirlar:
        metin(lay, kut, 40, yy, [(t, r)], px); yy += int(px * 1.02)
    return bg, lay, kut

VARYANT = {"A1": varyant_A, "A2": varyant_A, "B1": varyant_B, "B2": varyant_B,
           "C1": varyant_C, "C2": varyant_C, "D1": varyant_D, "D2": varyant_D}
METIN = {"A1": "PICK A DOOR", "A2": "ONE IS A DISASTER", "B1": "THE SURPRISE DOOR + 1929",
         "B2": "EVERYONE LAUGHED + 1929", "C1": "STOCKS −89%", "C2": "THE −89% DOOR",
         "D1": "EVERY BANK CLOSED", "D2": "MARCH 1933"}

# ---------- ölçüm ----------
def lum(c):
    def ch(v):
        v = v / 255; return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    return 0.2126 * ch(c[0]) + 0.7152 * ch(c[1]) + 0.0722 * ch(c[2])

def wcag(a, b):
    la, lb = sorted([lum(a), lum(b)], reverse=True); return (la + 0.05) / (lb + 0.05)

def kontrast(zemin, kut):
    """Metin rengi ↔ kontursuz zemin: glif çevresi 24 px halkada piksel bazlı WCAG, en kötü %5 (p5) ve medyan.
    Konturlu okunuş: dolgu ↔ kontur rengi (lacivert)."""
    z = np.array(zemin.convert("RGB")).astype(np.float64) / 255
    zl = np.where(z <= 0.03928, z / 12.92, ((z + 0.055) / 1.055) ** 2.4)
    L = 0.2126 * zl[..., 0] + 0.7152 * zl[..., 1] + 0.0722 * zl[..., 2]
    out = []
    for k in kut:
        x0, y0, x1, y1 = [int(v) for v in k["bbox"]]; x0 = max(0, x0 - 24); y0 = max(0, y0 - 24); x1 = min(W, x1 + 24); y1 = min(H, y1 + 24)
        bl = L[y0:y1, x0:x1].ravel(); lt = lum(k["renk"])
        r = (np.maximum(bl, lt) + 0.05) / (np.minimum(bl, lt) + 0.05)
        out.append({"metin": k["metin"], "zemin_p5": round(float(np.percentile(r, 5)), 2), "zemin_medyan": round(float(np.median(r)), 2),
                    "dolgu_kontur": round(wcag(k["renk"], LAC), 2) if k.get("kontur") else None,
                    "mobil_buyuk_harf_px": round(cap_yuk(k["px"]) * 168 / W, 1) if not k.get("damga") else round(cap_yuk(k["px"]) * 168 / W, 1)})
    return out

def kesisim(a, b):
    return max(0, min(a[2], b[2]) - max(a[0], b[0])) * max(0, min(a[3], b[3]) - max(a[1], b[1]))

def kelime_say(m):
    return len([w for w in m.replace("+", " ").split() if w])

def uret(vid, klasor):
    bg, lay, kut = VARYANT[vid](vid)
    zemin = bg.copy()
    son = Image.alpha_composite(bg, lay).convert("RGB")
    yol = os.path.join(klasor, f"{vid}.jpg")
    q = 92
    while True:
        b = io.BytesIO(); son.save(b, "JPEG", quality=q, optimize=True, progressive=True)
        if b.tell() <= 2 * 1024 * 1024 or q < 60: break
        q -= 4
    open(yol, "wb").write(b.getvalue())
    sure_ihlal = sum(kesisim(k["bbox"], SURE_KUTU) for k in kut)
    return son, {"id": vid, "metin": METIN[vid], "kelime": kelime_say(METIN[vid]), "dosya": os.path.relpath(yol, KOK),
                 "boyut": list(son.size), "bayt": len(b.getvalue()), "jpeg_q": q,
                 "kontrast": kontrast(zemin, kut), "sure_damgasi_ihlal_px": sure_ihlal,
                 "sha256": hashlib.sha256(b.getvalue()).hexdigest()[:16]}

def main():
    os.makedirs(os.path.join(KOK, "adaylar"), exist_ok=True); os.makedirs(os.path.join(KOK, "test"), exist_ok=True)
    sec = sys.argv[1:] or list(VARYANT)
    sonuc = {}; imgs = {}
    for v in sec:
        im, r = uret(v, os.path.join(KOK, "adaylar")); sonuc[v] = r; imgs[v] = im
        mob = min(c["mobil_buyuk_harf_px"] for c in r["kontrast"] if not c["metin"] == "1929")
        print(f"{v}: {r['metin']:<26} kelime {r['kelime']}  {r['bayt']/1024:.0f} KB  mobil büyük harf min {mob} px  "
              f"zemin p5 min {min(c['zemin_p5'] for c in r['kontrast'])}  dolgu/kontur {[c['dolgu_kontur'] for c in r['kontrast']]}  süre ihlal {r['sure_damgasi_ihlal_px']}")
    json.dump(sonuc, open(os.path.join(KOK, "test", "olcum-adaylar.json"), "w"), ensure_ascii=False, indent=1, default=list)
    # 168x94 kontrol sayfası (gerçek boyut + 2x)
    n = len(imgs); cols = 4; rows = math.ceil(n / cols)
    sh = Image.new("RGB", (cols * 200, rows * 130), (255, 255, 255)); d = ImageDraw.Draw(sh)
    for i, (v, im) in enumerate(imgs.items()):
        t = im.resize((168, 94), Image.LANCZOS); x, y = (i % cols) * 200 + 16, (i // cols) * 130 + 8
        sh.paste(t, (x, y)); d.text((x, y + 98), v, fill=(0, 0, 0))
    sh.save(os.path.join(KOK, "test", "mobil-168x94-adaylar.png"))

if __name__ == "__main__":
    main()
