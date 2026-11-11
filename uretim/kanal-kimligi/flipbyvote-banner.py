#!/usr/bin/env python3
"""Flip By Vote kanal banner'ı (2560x1440) — 2 varyant + kırpım testleri. Yeni AI üretimi yok.
Girdiler: L1-A mutfak plakası (bulanık zemin), ifade portreleri (Mike heyecanlı, Jake düşünceli; bölüm 1 kapağıyla aynı ikili).
Stil: bölüm 1 kapağı (koyu #0C0E16 panel, altın $100, beyaz Anton, Fredoka alt satır, çizilmiş ok).
Kullanım: python3 flipbyvote-banner.py [--kazanan A|B]
Çıktı: onizleme/fbv-banner-<V>.jpg, -bolgeler.jpg, -kirpmalar.jpg, fbv-olcum.json; --kazanan ile flipbyvote-banner.png + kontak."""
import argparse, hashlib, json, os, subprocess, tempfile
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance, ImageFont

KOK = "/home/user/vitrinly"
BU = os.path.join(KOK, "uretim", "kanal-kimligi")
ONZ = os.path.join(BU, "onizleme")
FONT = os.path.join(KOK, "video", "public", "fonts")
IFADE = os.path.join(KOK, "video", "public", "seri", "bolum-001", "ifade")
PLAKA = os.path.join(KOK, "uretim", "seri", "karakter", "canva-ham", "L1-A.png")
W, H = 2560, 1440
SW, SH = 1546, 423
SX, SY = (W - SW) // 2, (H - SH) // 2  # 507, 508
KIRPMA = {"tv": (0, 0, W, H), "masaustu": (0, SY, W, SY + SH),
          "tablet": ((W - 1855) // 2, SY, (W + 1855) // 2, SY + SH), "mobil": (SX, SY, SX + SW, SY + SH)}
KOYU, ALTIN, BEYAZ, MAVI, KIRMIZI = (12, 14, 22), (255, 201, 60), (255, 255, 255), (77, 168, 255), (255, 90, 78)
YUZ_Y0, YUZ_Y1 = 85, 900   # portre kaynağında saç tepesi → çene (alfa satır genişliği ölçümü, boyun ~y 950)
ETIKET = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def anton(px): return ImageFont.truetype(os.path.join(FONT, "Anton-400.woff2"), px)


def fred(px):
    f = ImageFont.truetype(os.path.join(FONT, "Fredoka-700.woff2"), px); f.set_variation_by_axes([700]); return f


def lum(c):
    c = np.asarray(c, dtype=np.float64)[..., :3] / 255.0
    c = np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    return c[..., 0] * 0.2126 + c[..., 1] * 0.7152 + c[..., 2] * 0.0722


def wcag(a, b): return (np.maximum(a, b) + 0.05) / (np.minimum(a, b) + 0.05)


def sha(p): return hashlib.sha256(open(p, "rb").read()).hexdigest()[:12]


def zemin():
    """L1-A'nın üst-orta kısmı (pencere/dolaplar) → 2560x1440, bulanık + karartılmış + kenar vinyeti, alt koyu panel."""
    p = Image.open(PLAKA).convert("RGB")
    k = p.crop((0, 260, 1080, 260 + 608)).resize((W, H), Image.LANCZOS).filter(ImageFilter.GaussianBlur(14))
    k = ImageEnhance.Brightness(k).enhance(0.42)
    k = ImageEnhance.Color(k).enhance(0.8)
    a = np.asarray(k).astype(np.float64)
    yy, xx = np.mgrid[0:H, 0:W]
    r = np.sqrt(((xx - W / 2) / (W / 2)) ** 2 + ((yy - H / 2) / (H / 2)) ** 2)
    v = np.clip(1 - 0.45 * np.clip(r - 0.35, 0, 1), 0.4, 1)[..., None]
    a = a * v + np.array(KOYU) * (1 - v)
    # alt koyu panel (kapak gibi): y 960'tan 1180'e erir
    t = np.clip((yy - 960) / 220.0, 0, 1)[..., None] ** 1.3
    a = a * (1 - t) + np.array(KOYU) * t
    return Image.fromarray(a.astype(np.uint8)).convert("RGBA")


def portre(ad, olcek, ayna=False):
    im = Image.open(os.path.join(IFADE, ad + ".png")).convert("RGBA")
    if ayna: im = im.transpose(Image.FLIP_LEFT_RIGHT)
    w, h = round(im.width * olcek), round(im.height * olcek)
    im = im.resize((w, h), Image.LANCZOS)
    # alt kesik kenarı koyu panele erit (kaynak y 1000 → 1350 arası alfa 1 → 0)
    al = np.asarray(im.split()[3]).astype(np.float64)
    ys = np.arange(h)[:, None] / olcek
    al *= np.clip(1 - (ys - 1000) / 350.0, 0, 1)
    # omuzların düz kesik yan kenarlarını erit (kaynak y>900'de |x-540| 300→520)
    xs = np.abs(np.arange(w)[None, :] / olcek - 540)
    yan = np.clip(1 - (xs - 300) / 220.0, 0, 1)
    agirlik = np.clip((ys - 900) / 200.0, 0, 1)
    al *= 1 - agirlik * (1 - yan)
    im.putalpha(Image.fromarray(al.astype(np.uint8)))
    return im


def yuz_kutusu(ad, olcek, x, y):
    a = np.asarray(Image.open(os.path.join(IFADE, ad + ".png")))[..., 3] > 128
    xs = np.where(a[YUZ_Y0:YUZ_Y1].any(0))[0]
    return (x + xs.min() * olcek, y + YUZ_Y0 * olcek, x + xs.max() * olcek, y + YUZ_Y1 * olcek)


def isik(tuval, cx, cy, r, renk, guc):
    """karakter arkasına renkli halo (Mike kırmızı, Jake mavi: profil logosundaki iki renk)."""
    yy, xx = np.mgrid[0:H, 0:W]
    d = np.clip(1 - np.sqrt((xx - cx) ** 2 + (yy - cy) ** 2) / r, 0, 1) ** 2 * guc
    a = np.asarray(tuval).astype(np.float64)
    a[..., :3] = a[..., :3] * (1 - d[..., None]) + np.array(renk) * d[..., None]
    return Image.fromarray(a.astype(np.uint8), "RGBA")


class Metin:
    """Metni hem tuvale hem ölçüm maskesine çizer."""
    def __init__(self, tuval):
        self.t = tuval; self.d = ImageDraw.Draw(tuval); self.kutular = []

    def yaz(self, xy, s, f, renk, kontur=8, anchor="la", ad=None):
        """xy[1] = mürekkebin ÜST kenarı (Anton'un büyük iç boşluğu yüzünden yazı tipi çapası değil)."""
        ub = self.d.textbbox((0, 0), s, font=f, anchor=anchor)
        xy = (xy[0], xy[1] - ub[1])
        m = Image.new("L", (W, H), 0)
        ImageDraw.Draw(m).text(xy, s, font=f, fill=255, anchor=anchor)
        self.d.text(xy, s, font=f, fill=renk, anchor=anchor, stroke_width=kontur, stroke_fill=(8, 9, 14))
        bb = m.getbbox(); self.kutular.append({"metin": ad or s, "kutu": bb, "maske": m, "renk": renk})
        return bb

    def ok(self, x, ymid, boy, uzun):
        p = [(x, ymid - boy * 0.09), (x + uzun * 0.55, ymid - boy * 0.09), (x + uzun * 0.55, ymid - boy * 0.22), (x + uzun, ymid),
             (x + uzun * 0.55, ymid + boy * 0.22), (x + uzun * 0.55, ymid + boy * 0.09), (x, ymid + boy * 0.09)]
        self.d.polygon(p, fill=BEYAZ, outline=(8, 9, 14), width=5)
        return (x, ymid - boy * 0.22, x + uzun, ymid + boy * 0.22)

    def para_satiri(self, cx, y, boy, hiza="orta", x0=None):
        f = anton(boy); w1 = self.d.textlength("$100", font=f); w2 = self.d.textlength("$1,000,000", font=f); ok = boy * 0.75
        top = w1 + w2 + ok + 60
        x = cx - top / 2 if hiza == "orta" else x0
        b1 = self.yaz((x, y), "$100", f, ALTIN)
        ob = self.ok(x + w1 + 30, (b1[1] + b1[3]) / 2, boy, ok)
        b2 = self.yaz((x + w1 + ok + 60, y), "$1,000,000", f, BEYAZ)
        return (min(b1[0], ob[0]), min(b1[1], b2[1]), b2[2], max(b1[3], b2[3])), top


def varyant(v):
    t = zemin()
    yuzler = {}
    if v == "A":
        # A "karşı karşıya": Mike solda heyecanlı, Jake sağda düşünceli, metin ortada (oylama gerilimi)
        o = 0.44
        mx, jx = SX + 10, SX + SW - 10 - round(1080 * o)
        y = SY + 22 - round(YUZ_Y0 * o)
        t = isik(t, mx + 540 * o, SY + 230, 520, KIRMIZI, 0.22); t = isik(t, jx + 540 * o, SY + 230, 520, MAVI, 0.22)
        for ad, x in (("mike-heyecanli-temiz", mx), ("jake-dusunceli", jx)):
            p = portre(ad, o); t.alpha_composite(p, (x, y)); yuzler[ad] = yuz_kutusu(ad, o, x, y)
        M = Metin(t); cx = W / 2
        b0 = M.yaz((cx, SY + 30), "FLIP BY VOTE", anton(178), BEYAZ, kontur=9, anchor="ma")
        bp, _ = M.para_satiri(cx, b0[3] + 34, 104)
        M.yaz((cx, bp[3] + 26), "You decide every move.", fred(60), (235, 240, 250), kontur=5, anchor="ma")
    else:
        # B "ikili + başlık": metin solda büyük, ikili sağda kapaktaki gibi omuz omuza
        o = 0.44
        jx = SX + SW - 16 - round(894 * o)           # Jake yüzünün sağ kenarı güvenli alanın 16 px içinde
        mx = jx - 300                                # Mike önde-solda, omuz bindirmesi
        y = SY + 18 - round(YUZ_Y0 * o)
        t = isik(t, mx + 540 * o, SY + 230, 520, KIRMIZI, 0.22); t = isik(t, jx + 540 * o, SY + 230, 520, MAVI, 0.22)
        for ad, x in (("jake-dusunceli", jx), ("mike-heyecanli-temiz", mx)):
            p = portre(ad, o); t.alpha_composite(p, (x, y)); yuzler[ad] = yuz_kutusu(ad, o, x, y)
        M = Metin(t); x0 = SX + 30
        b0 = M.yaz((x0, SY + 22), "FLIP BY VOTE", anton(172), BEYAZ, kontur=9)
        bp, _ = M.para_satiri(None, b0[3] + 30, 98, hiza="sol", x0=x0)
        M.yaz((x0 + 4, bp[3] + 30), "You decide every move.", fred(56), (235, 240, 250), kontur=5)
    return t.convert("RGB"), M.kutular, yuzler


def olc(son, kutular, yuzler):
    z = np.asarray(son); out = {"metin": [], "guvenli_alan_disi": [], "yuz": {}}
    for k in kutular:
        m = np.asarray(k["maske"]) > 0; x0, y0, x1, y1 = k["kutu"]; pad = 14
        b = np.zeros_like(m); b[y0 - pad:y1 + pad, x0 - pad:x1 + pad] = True
        r = wcag(lum(k["renk"]), lum(z[b & ~m]))
        out["metin"].append({"metin": k["metin"], "kutu": list(k["kutu"]), "wcag_p5": round(float(np.percentile(r, 5)), 2),
                             "wcag_medyan": round(float(np.median(r)), 2)})
        if not (x0 >= SX and y0 >= SY and x1 <= SX + SW and y1 <= SY + SH): out["guvenli_alan_disi"].append(k["metin"])
    for ad, (x0, y0, x1, y1) in yuzler.items():
        ic = x0 >= SX and y0 >= SY and x1 <= SX + SW and y1 <= SY + SH
        out["yuz"][ad] = {"kutu": [round(v) for v in (x0, y0, x1, y1)], "guvenli_alanda": bool(ic)}
        if not ic: out["guvenli_alan_disi"].append(ad)
    return out


def ocr(im):
    """Mobil gerçek boy (390 CSS px) → x4 büyüt → tesseract psm 11 (+ satır satır psm 6)."""
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "o.png")
        im.resize((im.width * 4, im.height * 4), Image.LANCZOS).convert("L").save(p)
        r = subprocess.run(["tesseract", p, "-", "--psm", "11"], capture_output=True, text=True).stdout
    return " ".join(r.split())


def onizleme(son, ad):
    g = son.copy(); d = ImageDraw.Draw(g)
    renk = {"tv": (255, 255, 255), "masaustu": (80, 200, 255), "tablet": (255, 160, 60), "mobil": (255, 60, 60)}
    for k, (x0, y0, x1, y1) in KIRPMA.items():
        d.rectangle([x0 + 3, y0 + 3, x1 - 4, y1 - 4], outline=renk[k], width=6)
        d.text((x0 + 16, y0 + 10), k.upper(), font=anton(40), fill=renk[k])
    g.resize((1280, 720), Image.LANCZOS).save(os.path.join(ONZ, f"fbv-banner-{ad}-bolgeler.jpg"), quality=88)
    et = ImageFont.truetype(ETIKET, 24)
    mb = son.crop(KIRPMA["mobil"]); mb1 = mb.resize((390, round(390 * SH / SW)), Image.LANCZOS)
    sat = [("TV (tam tuval, 960 px)", son.resize((960, 540), Image.LANCZOS)),
           ("Masaüstü (2560x423 bant, 1284 px)", son.crop(KIRPMA["masaustu"]).resize((1284, round(1284 * SH / W)), Image.LANCZOS)),
           ("Tablet (1855x423, 960 px)", son.crop(KIRPMA["tablet"]).resize((960, round(960 * SH / 1855)), Image.LANCZOS)),
           ("Mobil (1546x423, 390 CSS px = gerçek telefon boyu)", mb1),
           ("Mobil x3 cihaz pikseli (1170 px)", mb.resize((1170, round(1170 * SH / SW)), Image.LANCZOS))]
    gh = sum(i.height + 60 for _, i in sat) + 20
    sh = Image.new("RGB", (1320, gh), (235, 235, 235)); sd = ImageDraw.Draw(sh); y = 10
    for tt, i in sat:
        sd.text((18, y + 8), tt, font=et, fill=(20, 20, 20)); y += 48; sh.paste(i, (18, y)); y += i.height + 12
    yol = os.path.join(ONZ, f"fbv-banner-{ad}-kirpmalar.jpg"); sh.save(yol, quality=88)
    return mb1, yol


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--kazanan", default=None); a = ap.parse_args()
    os.makedirs(ONZ, exist_ok=True)
    sonuc = {"girdi_sha256_12": {os.path.relpath(p, KOK): sha(p) for p in
             [PLAKA, os.path.join(IFADE, "mike-heyecanli-temiz.png"), os.path.join(IFADE, "jake-dusunceli.png")]}}
    for v in ("A", "B"):
        son, kut, yuz = varyant(v)
        son.save(os.path.join(ONZ, f"fbv-banner-{v}.jpg"), quality=90)
        mb1, _ = onizleme(son, v)
        o = olc(son, kut, yuz); o["ocr_mobil_390"] = ocr(mb1)
        o["ocr_mobil_x3_1170"] = ocr(son.crop(KIRPMA["mobil"]).resize((1170, round(1170 * SH / SW)), Image.LANCZOS))
        o["ocr_mobil_390_tam"] = all(w in o["ocr_mobil_390"].upper().replace(",", "").replace("$", "S")
                                     for w in ("FLIP", "VOTE", "S100", "S1000000", "DECIDE", "MOVE"))
        sonuc[v] = o
        if a.kazanan == v:
            hedef = os.path.join(BU, "flipbyvote-banner.png"); son.save(hedef, optimize=True)
            o["dosya"] = {"yol": os.path.relpath(hedef, KOK), "bayt": os.path.getsize(hedef), "boyut": list(son.size)}
            import shutil
            shutil.copy(os.path.join(ONZ, f"fbv-banner-{v}-kirpmalar.jpg"), os.path.join(BU, "flipbyvote-banner-kirpimlar.jpg"))
    json.dump(sonuc, open(os.path.join(ONZ, "fbv-olcum.json"), "w"), ensure_ascii=False, indent=1)
    print(json.dumps(sonuc, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()
