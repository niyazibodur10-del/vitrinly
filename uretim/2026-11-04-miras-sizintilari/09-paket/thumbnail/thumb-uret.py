#!/usr/bin/env python3
"""F8a thumbnail üretimi — S03 miras sızıntıları. Leo = gorsel-varlik-sanatcisi kafa değişimli kesikleri (05-gorsel/thumb-leo/),
kutu/bant = 05-gorsel/nesne/. Zemin, banknot, bant şeridi, etiket ve metin KOD. K3 kutu oranı 03-metin/veri/kutu-hesap.py'den.
Kullanım: THUMB_TMP=<geçici> python3 -I thumb-uret.py [K1 K3 K4 K4b] → adaylar/<id>.jpg + test/olcum-adaylar.json
(çıktı biçimi uretim/2026-10-28-yeni-video/09-paket/thumbnail/thumb-uret.py v2 ile aynı; thumb-test.py bunu okur)"""
import hashlib, io, json, math, os, random, re, subprocess, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

KOK = os.path.dirname(os.path.abspath(__file__)); VID = os.path.abspath(os.path.join(KOK, "..", ".."))
REPO = os.path.abspath(os.path.join(VID, "..", "..")); G = os.path.join(VID, "05-gorsel")
W, H = 1280, 720
LAC = (11, 16, 38); BEYAZ = (255, 255, 255); SARI = (255, 210, 63); KIRMIZI = (214, 40, 40); KRAFT = (238, 222, 186)
SURE_KUTU = (1088, 634, 1280, 720)

def font(px, ad="Anton-400"):
    ttf = os.path.join(os.environ.get("THUMB_TMP", "/tmp"), ad + ".ttf")
    if not os.path.exists(ttf):
        from fontTools.ttLib import TTFont
        f = TTFont(os.path.join(REPO, "video/public/fonts", ad + ".woff2")); f.flavor = None; f.save(ttf)
    return ImageFont.truetype(ttf, px)

def cap_yuk(px):
    b = font(px).getbbox("H"); return b[3] - b[1]

def kutu_orani():
    """kutu-hesap.py: yüklenen 10 kutu → teslim 6. Alan oranı 0,6 → kenar oranı √0,6 (2D'de boy kıyası alanla okunur)."""
    out = subprocess.run([sys.executable, "-I", os.path.join(VID, "03-metin/veri/kutu-hesap.py")], capture_output=True, text=True, check=True).stdout
    son = [int(m) for m in re.findall(r"→ (\d+)", out)]
    return 10, son[-1], math.sqrt(son[-1] / 10)

# ---------- çizim yardımcıları ----------
def radyal(cx, cy, r, renk, guc):
    y, x = np.mgrid[0:H, 0:W]; d = np.clip(1 - np.hypot(x - cx, y - cy) / r, 0, 1) ** 1.6 * guc
    a = np.dstack([np.full((H, W), c, np.uint8) for c in renk] + [(d * 255).astype(np.uint8)])
    return Image.fromarray(a, "RGBA")

def zemin(renk, isik):
    bg = Image.new("RGBA", (W, H), renk + (255,))
    for cx, cy, r, c, g in isik: bg.alpha_composite(radyal(cx, cy, r, c, g))
    return bg

def leo(bg, ad, s, ox, oy):
    """Kesik 1920x1080 (a kadrajı); s ölçek, (ox, oy) sol üst. Altta yumuşak gölge yok: bel kesiti karenin altından taşar."""
    im = Image.open(os.path.join(G, "thumb-leo", ad + ".png")).convert("RGBA")
    im = im.resize((round(im.width * s), round(im.height * s)), Image.LANCZOS)
    sh = Image.new("RGBA", bg.size, (0, 0, 0, 0)); a = im.getchannel("A").point(lambda v: v * 0.45)
    sh.paste(Image.new("RGBA", im.size, (0, 0, 0, 255)), (ox + 14, oy + 10), a)
    bg.alpha_composite(sh.filter(ImageFilter.GaussianBlur(12)))
    bg.alpha_composite(im, (ox, oy)) if ox >= 0 and oy >= 0 else bg.paste(im, (ox, oy), im)
    return bg

def nesne(bg, ad, h, x, alt, golge=True):
    im = Image.open(os.path.join(G, "nesne", ad + ".png")).convert("RGBA"); im = im.crop(im.getchannel("A").getbbox())
    w = round(im.width * h / im.height); im = im.resize((w, h), Image.LANCZOS)
    if golge:
        d = ImageDraw.Draw(sh := Image.new("RGBA", bg.size, (0, 0, 0, 0)))
        d.ellipse((x - 10, alt - 18, x + w + 30, alt + 14), fill=(60, 40, 0, 110)); bg.alpha_composite(sh.filter(ImageFilter.GaussianBlur(8)))
    bg.alpha_composite(im, (x, alt - h)); return (x, alt - h, x + w, alt)

def banknot(bg, cx, cy, w, aci, ton=0):
    """Genel yeşil banknot: kalın kontur, iç çerçeve, daire. Yazı, portre, gerçek para deseni yok."""
    h = int(w * 0.48); s = 3; im = Image.new("RGBA", (w * s, h * s), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    k = 6 * s; g = (96 + ton, 178 + ton // 2, 92 + ton)
    d.rounded_rectangle((k // 2, k // 2, w * s - k // 2, h * s - k // 2), 6 * s, fill=g, outline=(18, 52, 28), width=k)
    i = int(h * s * 0.2); d.rounded_rectangle((i, i, w * s - i, h * s - i), 4 * s, outline=(40, 110, 50), width=3 * s)
    r = int(h * s * 0.2); d.ellipse((w * s // 2 - r, h * s // 2 - r, w * s // 2 + r, h * s // 2 + r), fill=(160, 214, 150), outline=(40, 110, 50), width=3 * s)
    im = im.resize((w, h), Image.LANCZOS).rotate(aci, expand=True, resample=Image.BICUBIC)
    sh = Image.new("RGBA", bg.size, (0, 0, 0, 0)); sh.paste(Image.new("RGBA", im.size, (0, 0, 0, 120)), (cx - im.width // 2 + 6, cy - im.height // 2 + 8), im.getchannel("A"))
    bg.alpha_composite(sh.filter(ImageFilter.GaussianBlur(5))); bg.alpha_composite(im, (cx - im.width // 2, cy - im.height // 2))
    return (cx - im.width // 2, cy - im.height // 2, cx + im.width // 2, cy + im.height // 2)

def bant(bg, x0, y0, x1, y1, gen=34):
    """Kahverengi koli bandı şeridi (yarı saydam, koyu kenar)."""
    lay = Image.new("RGBA", bg.size, (0, 0, 0, 0)); d = ImageDraw.Draw(lay)
    d.line((x0, y0, x1, y1), fill=(150, 104, 52, 235), width=gen); d.line((x0, y0, x1, y1), fill=(196, 150, 92, 140), width=gen // 3)
    bg.alpha_composite(lay)

def yarik(bg, pts):
    ImageDraw.Draw(bg).polygon(pts, fill=(52, 18, 12, 255), outline=(20, 10, 8, 255))

def metin(lay, kut, x, y, kelimeler, px, kontur=True, plaka=None, kr=LAC):
    """kelimeler: [(yazı, renk)]; kelime kelime çizim, boşluk 0,32 em (1929 dersi). plaka varsa satırın arkasına levha."""
    f = font(px); kon = max(6, px // 11) if kontur else 0; BOS = 0.32 * px
    d = ImageDraw.Draw(lay); cx = x; boxes = []
    for t, renk in kelimeler:
        b = d.textbbox((cx, y), t, font=f); boxes.append((t, renk, b)); cx = b[2] + BOS
    if plaka:
        x0 = min(b[2][0] for b in boxes); x1 = max(b[2][2] for b in boxes); y0 = min(b[2][1] for b in boxes); y1 = max(b[2][3] for b in boxes)
        lb = (x0 - 24, y0 - 18, x1 + 24, y1 + 18)
        sh = Image.new("RGBA", lay.size, (0, 0, 0, 0)); ImageDraw.Draw(sh).rounded_rectangle((lb[0] + 6, lb[1] + 8, lb[2] + 6, lb[3] + 8), 12, fill=(0, 0, 0, 150))
        lay.alpha_composite(sh.filter(ImageFilter.GaussianBlur(6))); ImageDraw.Draw(lay).rounded_rectangle(lb, 12, fill=plaka + (255,))
    else:
        sh = Image.new("RGBA", lay.size, (0, 0, 0, 0))
        for t, renk, b in boxes: ImageDraw.Draw(sh).text((b[0] + 6, y + 8), t, font=f, fill=(0, 0, 0, 170), stroke_width=kon, stroke_fill=(0, 0, 0, 170))
        lay.alpha_composite(sh.filter(ImageFilter.GaussianBlur(6)))
    d = ImageDraw.Draw(lay)
    for t, renk, b in boxes:
        bx = b[0]
        d.text((bx, y), t, font=f, fill=renk + (255,), stroke_width=kon, stroke_fill=kr + (255,))
        kut.append({"metin": t, "renk": renk, "bbox": list(b), "px": px, "kontur": kon, "kontur_renk": kr, "levha": plaka})
    return max(b[2][2] for b in boxes), max(b[2][3] for b in boxes)

# ---------- varyantlar ----------
def varyant_K1(vid, yuz=os.path.join(KOK, "leo", "K1c-M06-kuskulu")):   # 2026-11-09: şaşkın → bilmiş/kuşkulu (c-isaret kafası; kanal-analisti teşhisi: ifade tekrarı)
    """Duygu: Leo şaşkın, kucağındaki kutunun alt köşesi yarık, banknotlar sola dökülüyor; kutu etiketi $124T. Metin WHO / GETS / IT?"""
    bg = zemin((10, 70, 80), [(960, 260, 620, (64, 168, 172), 0.85), (930, 210, 300, (255, 196, 120), 0.35)])
    s, ox, oy = 0.80, 190, 0
    leo(bg, yuz, s, ox, oy)
    T = lambda x, y: (round(x * s + ox), round(y * s + oy))        # kesik koordinatı → tuval
    bx0, by0 = T(673, 569); bx1, _ = T(1218, 1004)
    yarik(bg, [T(673, 905), T(735, 1004), T(673, 1004)])            # alt sol köşe yarığı (görünür alanın altında kalırsa da iz verir)
    yarik(bg, [(bx0, 640), (bx0 + 46, 720), (bx0, 720)])
    kut = []; lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    # banknotlar: yarıktan sola-aşağı, en fazla 5, metin yasak bölgesinin (x ≤ 600) dışında
    for cx, cy, w, a, t in ((bx0 - 10, 676, 120, 18, 0), (bx0 - 70, 610, 110, -24, 12), (bx0 - 40, 540, 100, 38, -8), (bx0 + 40, 700, 104, -8, 6)):
        banknot(bg, cx, cy, w, a, t)
    # kutu etiketi: kraft levha + $124T (Cerulli tahmini, 2048'e kadar; atıf yok, H8)
    ex = (bx0 + bx1) // 2 + 10; ey = by0 + 24
    f = font(150); tb = ImageDraw.Draw(lay).textbbox((0, 0), "$124T", font=f); tw, th = tb[2] - tb[0], tb[3] - tb[1]
    lb = (ex - tw // 2 - 26, ey - 16, ex + tw // 2 + 26, ey + th + 30)
    ImageDraw.Draw(bg).rounded_rectangle(lb, 10, fill=KRAFT + (255,), outline=(70, 50, 30, 255), width=5)
    ImageDraw.Draw(lay).text((ex - tw // 2 - tb[0], ey - tb[1] + 6), "$124T", font=f, fill=LAC + (255,))
    kut.append({"metin": "$124T", "renk": LAC, "bbox": [ex - tw // 2, ey + 6, ex + tw // 2, ey + th + 6], "px": 150, "kontur": 0, "levha": KRAFT})
    # başlık metni: 3 satır, sol 40–580
    # 3 satır yüksekliğe sığdır (16–700 px): satır kutusu yüksekliği ölçülerek px küçültülür
    px = 200
    while px > 100:
        hs = [ImageDraw.Draw(lay).textbbox((0, 0), t, font=font(px)) for t in ("WHO", "GETS", "IT?")]
        if sum(h[3] - h[1] for h in hs) + 2 * 30 + 2 * max(6, px // 11) <= 684: break
        px -= 4
    y = 16
    for t in ("WHO", "GETS", "IT?"):
        b = ImageDraw.Draw(lay).textbbox((0, 0), t, font=font(px)); _, yb = metin(lay, kut, 48, y - b[1] + 8, [(t, SARI)], px); y = yb + 30
    return bg, lay, kut

def varyant_K3(vid):
    """Karşıtlık: büyük kutu (yüklenen) ↔ küçük, bantlı kutu (varan); alan oranı kutu-hesap.py 6/10. Leo pano ile sağda. Metin SMALLER. / LATER."""
    bg = zemin((250, 225, 140), [(980, 300, 560, (255, 244, 200), 0.8)])
    ImageDraw.Draw(bg).rectangle((0, 618, W, H), fill=(232, 198, 112, 255))   # zemin bandı
    leo(bg, "K3b-M04-notr", 0.74, 400, 8)
    # pano: envanter listesi, 6 durak çizgisi; kayıplı 3 durak (LIVING, CARE, GIVING — kutu-hesap.py) kırmızı çizik. Yazı yok.
    d = ImageDraw.Draw(bg); px0, py0 = round(787 * 0.74 + 400), round(581 * 0.74 + 8)
    for i, cizik in enumerate((1, 1, 0, 1, 0, 0)):
        y = py0 + 62 + i * 34; d.line((px0 + 34, y, px0 + 190, y), fill=(120, 120, 130, 255), width=7)
        if cizik: d.line((px0 + 26, y - 2, px0 + 198, y + 2), fill=KIRMIZI + (255,), width=6)
    yuk, tes, k = kutu_orani()
    hb = 290; hk = round(hb * k)
    nesne(bg, "M02-kiremit", hb, 40, 690)
    kx0, ky0, kx1, ky1 = nesne(bg, "M02-kiremit-yarik", hk, 410, 690)
    # küçük kutu: köşelerde çapraz bant + dikişten çıkan tek banknot
    bant(bg, kx0 + 8, ky0 + 40, kx0 + 70, ky0 + 4); bant(bg, kx0 + 4, ky0 + 10, kx0 + 66, ky0 + 52)
    bant(bg, kx1 - 92, ky1 - 18, kx1 - 22, ky1 - 80)
    banknot(bg, kx0 + (kx1 - kx0) // 2 - 10, ky0 + 2, 92, 14, 0)
    kut = []; lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    _, yb = metin(lay, kut, 48, 6, [("SMALLER.", LAC)], 160, kr=BEYAZ)
    metin(lay, kut, 72, yb + 34, [("LATER.", BEYAZ)], 120, kontur=False, plaka=KIRMIZI)
    return bg, lay, kut, {"kutu_yuklenen": yuk, "kutu_teslim": tes, "kenar_orani": round(k, 4), "buyuk_h": hb, "kucuk_h": hk}

def varyant_K4(vid, yuz="K4-M05-saskin"):
    """Mizah: Leo bir köşeyi bantlıyor, para öbür köşeden akıyor. Metin IT KEEPS / LEAKING (lacivert levha)."""
    bg = zemin((196, 64, 44), [(930, 250, 560, (236, 120, 84), 0.75)])
    s, ox, oy = 0.68, 300, -12
    leo(bg, yuz, s, ox, oy)
    T = lambda x, y: (round(x * s + ox), round(y * s + oy))
    bx0, by0 = T(534, 807); bx1, _ = T(1370, 1079)
    # sağ üst köşede çapraz eski bantlar
    bant(bg, bx1 - 120, by0 + 6, bx1 - 4, by0 + 92, 30); bant(bg, bx1 - 110, by0 + 92, bx1 - 6, by0 + 14, 30)
    # sol köşe: yarık + dökülen banknotlar (metin bölgesinin altında, x ≤ bx0)
    yarik(bg, [(bx0, by0 + 40), (bx0 + 40, H), (bx0, H)])
    for cx, cy, w, a, t in ((bx0 - 20, 690, 116, 22, 0), (bx0 - 96, 652, 108, -30, 10), (bx0 - 170, 694, 104, 12, -6), (bx0 + 6, 600, 100, -40, 4)):
        banknot(bg, cx, cy, w, a, t)
    kut = []; lay = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    _, yb = metin(lay, kut, 48, 30, [("IT", BEYAZ), ("KEEPS", BEYAZ)], 172)
    metin(lay, kut, 72, yb + 52, [("LEAKING", BEYAZ)], 150, kontur=False, plaka=LAC)
    return bg, lay, kut

VARYANT = {"K1": varyant_K1, "K3": varyant_K3, "K4": varyant_K4, "K4b": lambda v: varyant_K4(v, "K4b-M05-gulumser"), "K1s": lambda v: varyant_K1(v, "K1-M06-saskin")}
METIN = {"K1": "WHO GETS IT? + $124T", "K3": "SMALLER. LATER.", "K4": "IT KEEPS LEAKING", "K4b": "IT KEEPS LEAKING", "K1s": "WHO GETS IT? + $124T"}

# ---------- ölçüm ----------
def lum(c):
    def ch(v):
        v = v / 255; return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    return 0.2126 * ch(c[0]) + 0.7152 * ch(c[1]) + 0.0722 * ch(c[2])

def wcag(a, b):
    la, lb = sorted([lum(a), lum(b)], reverse=True); return (la + 0.05) / (lb + 0.05)

def kontrast(zem, kut):
    """Metin ↔ kontursuz zemin (metin katmanı hariç her şey): serbest metinde glif çevresi 24 px halka, levhada levha rengi; p5 + medyan."""
    z = np.array(zem.convert("RGB")).astype(np.float64) / 255
    zl = np.where(z <= 0.03928, z / 12.92, ((z + 0.055) / 1.055) ** 2.4); L = 0.2126 * zl[..., 0] + 0.7152 * zl[..., 1] + 0.0722 * zl[..., 2]
    out = []
    for k in kut:
        lt = lum(k["renk"])
        if k.get("levha"): bl = np.array([lum(k["levha"])])
        else:
            x0, y0, x1, y1 = [int(v) for v in k["bbox"]]; bl = L[max(0, y0 - 24):min(H, y1 + 24), max(0, x0 - 24):min(W, x1 + 24)].ravel()
        r = (np.maximum(bl, lt) + 0.05) / (np.minimum(bl, lt) + 0.05)
        out.append({"metin": k["metin"], "bbox": [int(v) for v in k["bbox"]], "zemin_p5": round(float(np.percentile(r, 5)), 2), "zemin_medyan": round(float(np.median(r)), 2),
                    "dolgu_kontur": round(wcag(k["renk"], k["kontur_renk"]), 2) if k.get("kontur") else None,
                    "mobil_buyuk_harf_px": round(cap_yuk(k["px"]) * 168 / W, 1)})
    return out

def kesisim(a, b):
    return max(0, min(a[2], b[2]) - max(a[0], b[0])) * max(0, min(a[3], b[3]) - max(a[1], b[1]))

def kelime_say(m):
    return len([w for w in m.replace("+", " ").split() if w])

def uret(vid, klasor):
    r = VARYANT[vid](vid); bg, lay, kut = r[:3]; ek = r[3] if len(r) > 3 else {}
    son = Image.alpha_composite(bg, lay).convert("RGB")
    q = 92
    while True:
        b = io.BytesIO(); son.save(b, "JPEG", quality=q, optimize=True)
        if b.tell() <= 2 * 1024 * 1024 or q < 60: break
        q -= 4
    yol = os.path.join(klasor, f"{vid}.jpg"); open(yol, "wb").write(b.getvalue())
    return son, dict({"id": vid, "metin": METIN[vid], "kelime": kelime_say(METIN[vid]), "dosya": os.path.relpath(yol, KOK), "boyut": list(son.size),
                      "bayt": len(b.getvalue()), "jpeg_q": q, "kontrast": kontrast(bg, kut),
                      "sure_damgasi_ihlal_px": sum(kesisim(k["bbox"], SURE_KUTU) for k in kut), "sha256": hashlib.sha256(b.getvalue()).hexdigest()[:16]}, **ek)

def main():
    os.makedirs(os.path.join(KOK, "adaylar"), exist_ok=True); os.makedirs(os.path.join(KOK, "test"), exist_ok=True)
    sec = sys.argv[1:] or list(VARYANT); sonuc = {}
    for v in sec:
        im, r = uret(v, os.path.join(KOK, "adaylar")); sonuc[v] = r
        print(f"{v}: {r['metin']:<22} kelime {r['kelime']}  {r['bayt']/1024:.0f} KB  büyük harf168 min {min(c['mobil_buyuk_harf_px'] for c in r['kontrast'])} px  "
              f"p5 min {min(c['zemin_p5'] for c in r['kontrast'])}  dolgu/kontur {[c['dolgu_kontur'] for c in r['kontrast']]}  süre ihlal {r['sure_damgasi_ihlal_px']}  sha {r['sha256']}"
              + (f"  kutu {r['kutu_yuklenen']}→{r['kutu_teslim']} kenar {r['kenar_orani']} ({r['buyuk_h']}→{r['kucuk_h']} px)" if 'kutu_teslim' in r else ""))
    json.dump(sonuc, open(os.path.join(KOK, "test", "olcum-adaylar.json"), "w"), ensure_ascii=False, indent=1, default=list)

if __name__ == "__main__":
    main()
