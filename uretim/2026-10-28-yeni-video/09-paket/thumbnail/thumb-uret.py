#!/usr/bin/env python3
"""F8 thumbnail üretimi + testler — S08 "If America Earned $5,400 a Month, Here's Its Budget"

Kullanım:  python3 thumb-uret.py            (tüm adaylar + testler)
Çıktı:     bu klasör (adaylar/, test/, olcum.json); finalistler kökte (A/B/C), seçim raporda.
Metin her zaman kodla yazılır (Anton, video/public/fonts). Görseller yalnız mevcut
Canva varlıkları (bu videonun 05-gorsel/canva-ham, nesne/, leo/ + 1929 leo/ jest kesikleri). Yeni Canva üretimi yok.
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
def metin(lay, kutular, x, y, parcalar, px, kontur=None, golge=True, hiza="sol", kr=LAC):
    """parcalar: [(yazı, renk), ...] tek satır. Döner: satır bbox. kutular'a her parça eklenir."""
    f = font(px); kon = kontur if kontur is not None else max(6, px // 11)
    BOS = 0.32 * px
    def L(t): return f.getlength(t.replace(" ", "")) + t.count(" ") * BOS
    gen = sum(L(t) for t, _ in parcalar)
    if hiza == "orta": x = int(x - gen / 2)
    if hiza == "sag": x = int(x - gen)
    d = ImageDraw.Draw(lay)
    cx = x
    for t, renk in parcalar:
        if golge:
            sh = Image.new("RGBA", lay.size, (0, 0, 0, 0))
            wx = cx
            for w in t.split(" "):
                if w: ImageDraw.Draw(sh).text((wx + 6, y + 8), w, font=f, fill=(0, 0, 0, 170), stroke_width=kon, stroke_fill=(0, 0, 0, 170)); wx += f.getlength(w)
                wx += BOS
            lay.alpha_composite(sh.filter(ImageFilter.GaussianBlur(6)))
        d = ImageDraw.Draw(lay)
        wx = cx
        for i, w in enumerate(t.split(" ")):
            if w:
                d.text((wx, y), w, font=f, fill=renk + (255,), stroke_width=kon, stroke_fill=kr + (255,))
                b = d.textbbox((wx, y), w, font=f)
                kutular.append({"metin": w, "renk": renk, "bbox": [b[0], b[1], b[2], b[3]], "px": px, "kontur": kon, "kontur_renk": kr})
                wx += f.getlength(w)
            if i < len(t.split(" ")) - 1: wx += BOS
        cx += L(t)
    return (x, y, cx, y + px)

def sigdir(satir, gen, maks):
    px = maks
    while px > 20 and font(px).getlength(satir.replace(" ", "")) + satir.count(" ") * 0.32 * px > gen: px -= 2
    return px

# ---------- bu videoya özgü (S08 bütçe) ----------
L29 = os.path.join(REPO, "uretim/2026-10-26-1929-1000-dolar/05-gorsel/leo")   # muaf karakter kesikleri (05-gorsel/rapor.md)
KIRMIZI = (214, 40, 40)      # #D62828 vurgu levhası (beyaz yazı 5,3:1)
KOYU = (24, 28, 36)

def leo29(ad): return Image.open(os.path.join(L29, ad + ".png")).convert("RGBA")

def levha(bg, lay, kut, x, y, yazi, px, zemin, renk=BEYAZ, pad=(26, 10), hiza="sol", aci=0):
    """Renkli levha (zemine, ölçüm bunu görür) + üstünde kontursuz metin (katmana)."""
    f = font(px); BOS = 0.32 * px
    gen = f.getlength(yazi.replace(" ", "")) + yazi.count(" ") * BOS
    ch = cap_yuk(px); ust = f.getbbox("H")[1]
    if hiza == "orta": x = int(x - gen / 2 - pad[0])
    if hiza == "sag": x = int(x - gen - 2 * pad[0])
    x0, y0, x1, y1 = x, y, int(x + gen + 2 * pad[0]), int(y + ch + 2 * pad[1] + 0.36 * ch)
    sh = Image.new("RGBA", bg.size, (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle((x0 + 8, y0 + 10, x1 + 8, y1 + 10), radius=18, fill=(0, 0, 0, 120))
    bg.alpha_composite(sh.filter(ImageFilter.GaussianBlur(8)))
    ImageDraw.Draw(bg).rounded_rectangle((x0, y0, x1, y1), radius=18, fill=zemin + (255,), outline=LAC + (255,), width=7)
    ty = y0 + (y1 - y0 - ch) / 2 - ust
    d = ImageDraw.Draw(lay); wx = x0 + pad[0]
    for i, w in enumerate(yazi.split(" ")):
        d.text((wx, ty), w, font=f, fill=renk + (255,))
        bb = d.textbbox((wx, ty), w, font=f)
        kut.append({"metin": w, "renk": renk, "bbox": list(bb), "px": px, "kontur": 0, "levha": zemin})
        wx += f.getlength(w) + BOS
    return (x0, y0, x1, y1)

def varyant_A(mid):
    """Duygu: d-saskin yakın yüz, sıcak masa (G06) — açık/sıcak zemin (koyu lacivert tekrarı yok)."""
    bg = plaka("canva-ham/G06.png", 1.4, 704, 480, blur=5, parlak=1.08)   # masanın boş, lamba ışıklı ortası (kupa/kâğıt/lamba kadraj dışı)
    bg.alpha_composite(radyal(W, H, 380, 330, 620, (255, 200, 90), 0.55))
    bg.alpha_composite(radyal(W, H, 1080, 400, 640, (255, 230, 170), 0.95))   # metin alanı aydınlık: koyu yazı ↔ zemin p5 ≥4,5
    leo = leo29("d-saskin")
    s = 1.02; yerlestir(bg, leo, s, 300 - int(945 * s), 18 - int(31 * s), isik=(255, 230, 170))
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); kut = []
    X = 1245
    if mid == "A1":
        levha(bg, lay, kut, X, 40, "−$2,000", 170, KIRMIZI, hiza="sag")
        for i, t in enumerate(("EVERY", "MONTH")):
            px = 150; metin(lay, kut, X, 290 + i * 158, [(t, KOYU)], px, hiza="sag", kr=BEYAZ, golge=False)
    else:
        metin(lay, kut, X, 40, [("ALWAYS", KOYU)], 140, hiza="sag", kr=BEYAZ, golge=False)
        levha(bg, lay, kut, X, 205, "$2,000", 175, KIRMIZI, hiza="sag")
        metin(lay, kut, X, 455, [("SHORT", KOYU)], 150, hiza="sag", kr=BEYAZ, golge=False)
    return bg, lay, kut

def hesap_makinesi(bg, lay, kut, x, y, s, yazi):
    hm = yukle("nesne/G07-hesap-makinesi.png"); yerlestir(bg, hm, s, x, y)
    lx0, ly0, lx1, ly1 = x + 74 * s, y + 107 * s, x + 270 * s, y + 172 * s       # LCD (cetvel ölçümü, 350x460 kesik)
    ImageDraw.Draw(bg).rounded_rectangle((lx0, ly0, lx1, ly1), radius=int(6 * s), fill=(196, 222, 186, 255))
    px = 40
    while font(px + 2).getlength(yazi) < (lx1 - lx0) * 0.90 and cap_yuk(px + 2) < (ly1 - ly0) * 0.80: px += 2
    f = font(px); g = f.getlength(yazi); ch = cap_yuk(px)
    tx, ty = lx1 - g - (lx1 - lx0) * 0.05, ly0 + (ly1 - ly0 - ch) / 2 - f.getbbox("H")[1]
    ImageDraw.Draw(lay).text((tx, ty), yazi, font=f, fill=(20, 32, 24, 255))
    kut.append({"metin": yazi, "renk": (20, 32, 24), "bbox": list(ImageDraw.Draw(lay).textbbox((tx, ty), yazi, font=f)), "px": px, "kontur": 0, "levha": (196, 222, 186)})

def varyant_B(mid):
    """Obje: hesap makinesi ekranında −2,000, düşünen Leo; kırmızı-mercan zemin."""
    bg = Image.new("RGBA", (W, H), (200, 52, 44, 255))
    bg.alpha_composite(radyal(W, H, 470, 430, 700, (255, 120, 80), 0.75))
    leo = leo29("e-dusunen")
    s = 0.86; yerlestir(bg, leo, s, 1010 - int(915 * s), 40, isik=(255, 200, 150))
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); kut = []
    hesap_makinesi(bg, lay, kut, 40, 178, 1.92, "−2,000")
    t = {"B1": "EVERY MONTH", "B2": "SHORT AGAIN"}[mid]
    px = sigdir(t, 610, 140); levha(bg, lay, kut, 40, 22, t, px, KOYU, renk=SARI)
    return bg, lay, kut

def zarf(bg, lay, kut, cx, alt, s, etiket, ezemin):
    z = yukle("nesne/G03-zarf-kapali.png")
    x = int(cx - 219 * s); y = int(alt - 509 * s); yerlestir(bg, z, s, x, y)
    if etiket:
        px = 40
        while font(px + 2).getlength(etiket) < 330 * s * 0.86: px += 2
        levha(bg, lay, kut, cx, int(y + 300 * s), etiket, px, ezemin, hiza="orta", pad=(int(14 * s), int(6 * s)))

def varyant_C(mid):
    """Karşıtlık: faiz zarfı > ordu zarfı (R08 doğrulandı, S-metin "more than its whole military"); camgöbeği zemin."""
    bg = Image.new("RGBA", (W, H), (22, 160, 150, 255))
    bg.alpha_composite(radyal(W, H, 860, 360, 720, (120, 230, 210), 0.6))
    leo = kafa_degis(leo29("C13-kollar-kavusmus"), leo29("d-saskin"))
    s = 0.84; yerlestir(bg, leo, s, 250 - int(940 * s), 60, isik=(255, 220, 170))
    lay = Image.new("RGBA", (W, H), (0, 0, 0, 0)); kut = []
    zarf(bg, lay, kut, 930, 760, 1.12, None, None)       # tek zarf = videodaki "envelope five" (boyut kıyası yok → abartı yok)
    if mid == "C1":
        levha(bg, lay, kut, 1245, 22, "INTEREST", 150, KIRMIZI, hiza="sag")
        levha(bg, lay, kut, 1245, 236, "> MILITARY", 120, KOYU, hiza="sag")
    else:
        levha(bg, lay, kut, 1240, 24, "INTEREST > MILITARY", 104, KIRMIZI, hiza="sag")
    return bg, lay, kut

VARYANT = {k: v for k, v in (("A1", varyant_A), ("A2", varyant_A), ("B1", varyant_B), ("B2", varyant_B), ("C1", varyant_C), ("C2", varyant_C))}
METIN = {"A1": "−$2,000 EVERY MONTH", "A2": "ALWAYS $2,000 SHORT", "B1": "EVERY MONTH + −2,000",
         "B2": "SHORT AGAIN + −2,000", "C1": "INTEREST + > MILITARY", "C2": "INTEREST > MILITARY"}

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
        pd = 0 if k.get("levha") else 24          # levha metni: yalnız levha içi (glif kutusu); serbest metin: 24 px halka
        x0, y0, x1, y1 = [int(v) for v in k["bbox"]]; x0 = max(0, x0 - pd); y0 = max(0, y0 - pd); x1 = min(W, x1 + pd); y1 = min(H, y1 + pd)
        bl = L[y0:y1, x0:x1].ravel(); lt = lum(k["renk"])
        r = (np.maximum(bl, lt) + 0.05) / (np.minimum(bl, lt) + 0.05)
        if k.get("damga"):
            r = (np.maximum(bl, lt) + 0.05) / (np.minimum(bl, lt) + 0.05)
        out.append({"metin": k["metin"], "bbox": [int(v) for v in k["bbox"]], "zemin_p5": round(float(np.percentile(r, 5)), 2), "zemin_medyan": round(float(np.median(r)), 2),
                    "dolgu_kontur": round(wcag(k["renk"], k.get("kontur_renk", LAC)), 2) if k.get("kontur") else None,
                    "mobil_buyuk_harf_px": round(cap_yuk(k["px"]) * 168 / W, 1) if not k.get("damga") else round(cap_yuk(k["px"]) * 168 / W, 1)})
    return out

def kesisim(a, b):
    return max(0, min(a[2], b[2]) - max(a[0], b[0])) * max(0, min(a[3], b[3]) - max(a[1], b[1]))

def kelime_say(m):
    return len([w for w in m.replace("+", " ").split() if w and w not in (">",)])

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
        mob = min(c["mobil_buyuk_harf_px"] for c in r["kontrast"] )
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
