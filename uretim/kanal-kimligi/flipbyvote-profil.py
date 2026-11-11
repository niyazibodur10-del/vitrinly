#!/usr/bin/env python3
"""Flip By Vote profil resmi v2: Jake + Mike yüzleri (tik/rozet yok). 2 varyant + 98/48 px daire testi (açık/koyu tema).
Girdi: ifade portreleri (mike-gulen-temiz, jake-gulen). Kullanım: python3 flipbyvote-profil.py [--kazanan P1|P2]"""
import argparse, json, os, shutil, hashlib
import numpy as np
from PIL import Image, ImageDraw, ImageFont

KOK = "/home/user/vitrinly"; BU = os.path.join(KOK, "uretim/kanal-kimligi"); ONZ = os.path.join(BU, "onizleme")
IFADE = os.path.join(KOK, "video/public/seri/bolum-001/ifade")
S = 800
ZEMIN = {"P1": ((255, 214, 92), (255, 186, 40)), "P2": ((120, 196, 255), (60, 150, 245))}  # altın / gök mavisi (radyal iç→dış)
ETIKET = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"


def lum(c):
    c = np.asarray(c, float)[..., :3] / 255; c = np.where(c <= 0.04045, c / 12.92, ((c + 0.055) / 1.055) ** 2.4)
    return c @ [0.2126, 0.7152, 0.0722]


def portre(ad, o, sag_erit=0):
    im = Image.open(os.path.join(IFADE, ad + ".png")).convert("RGBA")
    im = im.resize((round(im.width * o), round(im.height * o)), Image.LANCZOS)
    if sag_erit:  # öndeki portrenin (Mike) düz sağ kesik kenarını (omuz altı) arkadakine erit
        a = np.asarray(im.split()[3]).astype(float); h, w = a.shape
        ys = np.arange(h)[:, None] / o; xs = np.arange(w)[None, :]
        a *= 1 - np.clip((ys - 1000) / 150, 0, 1) * (1 - np.clip((w - 1 - xs) / sag_erit, 0, 1))
        im.putalpha(Image.fromarray(a.astype(np.uint8)))
    return im


def yuz(ad, o, x, y):
    a = np.asarray(Image.open(os.path.join(IFADE, ad + ".png")))[..., 3] > 128
    xs = np.where(a[85:900].any(0))[0]
    return [round(x + xs.min() * o), round(y + 85 * o), round(x + xs.max() * o), round(y + 900 * o)]


def varyant(v):
    ic, dis = ZEMIN[v]
    yy, xx = np.mgrid[0:S, 0:S]; r = np.clip(np.hypot(xx - S / 2, yy - S * 0.4) / (S * 0.6), 0, 1)[..., None]
    t = Image.fromarray((np.array(ic) * (1 - r) + np.array(dis) * r).astype(np.uint8)).convert("RGBA")
    o = 0.47
    y = 150 - round(85 * o)                 # saç tepesi y≈150 (daire içinde, üstte nefes payı)
    mx, jx = 160 - round(540 * o) + 70, 640 - round(540 * o) - 70   # yüz merkezleri x≈230 / 570
    t.alpha_composite(portre("jake-gulen", o), (jx, y))                # Jake arkada (sağ)
    t.alpha_composite(portre("mike-gulen-temiz", o, sag_erit=110), (mx, y))          # Mike önde (sol), ekran yönü: Mike SOLDA
    return t, {"mike": yuz("mike-gulen-temiz", o, mx, y), "jake": yuz("jake-gulen", o, jx, y)}


def daire(p, s):
    k = p.resize((s, s), Image.LANCZOS).convert("RGBA"); m = Image.new("L", (s * 4, s * 4))
    ImageDraw.Draw(m).ellipse([0, 0, s * 4 - 1, s * 4 - 1], fill=255); k.putalpha(m.resize((s, s), Image.LANCZOS)); return k


def olc(p, yuzler):
    a = np.asarray(p.convert("RGB")); out = {}
    for k, (x0, y0, x1, y1) in yuzler.items():
        cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
        ic = all(np.hypot(px - S / 2, py - S / 2) <= S / 2 for px, py in ((x0, cy), (x1, cy), (cx, y0)))
        out[k] = {"kutu": [x0, y0, x1, y1], "genislik_cap_orani": round((x1 - x0) / S, 3),
                  "48px_yuz_genisligi": round((x1 - x0) / S * 48, 1), "98px_yuz_genisligi": round((x1 - x0) / S * 98, 1),
                  "daire_icinde": bool(ic)}
    yy, xx = np.mgrid[0:S, 0:S]; rr = np.hypot(xx - S / 2, yy - S / 2)
    kenar = a[(rr > S * 0.46) & (rr < S * 0.5)]
    Lk = float(np.median(lum(kenar)))
    out["daire_kenari_wcag_acik_tema"] = round((1.05) / (Lk + 0.05), 2)
    out["daire_kenari_wcag_koyu_tema"] = round((Lk + 0.05) / (float(lum((15, 15, 15))) + 0.05), 2)
    sac = a[150:200, 150:700].reshape(-1, 3); sac = sac[sac.max(1) < 110]   # saç pikselleri (koyu kahve)
    zem = np.median(a[60:110, 300:500].reshape(-1, 3), 0)
    if len(sac): out["sac_zemin_wcag"] = round(float((lum(zem) + 0.05) / (np.median(lum(sac)) + 0.05)), 2)
    return out


def kontak(adaylar, yol):
    et = ImageFont.truetype(ETIKET, 18)
    W = 40 + len(adaylar) * 520; sh = Image.new("RGB", (W, 330), (200, 200, 200)); d = ImageDraw.Draw(sh)
    for i, (ad, p) in enumerate(adaylar):
        x0 = 20 + i * 520
        for j, (bg, fg) in enumerate((((255, 255, 255), (20, 20, 20)), ((15, 15, 15), (235, 235, 235)))):
            bx = x0 + j * 250; d.rectangle([bx, 10, bx + 240, 320], fill=bg)
            d.text((bx + 10, 16), f"{ad} {'açık' if j == 0 else 'koyu'}", font=et, fill=fg)
            c98 = daire(p, 98); sh.paste(c98, (bx + 10, 50), c98); c48 = daire(p, 48); sh.paste(c48, (bx + 125, 75), c48)
            d.text((bx + 10, 155), "x2 (retina):", font=et, fill=fg)
            c = daire(p, 98).resize((196, 196), Image.NEAREST) if False else None
            k = daire(p, 48 * 2); sh.paste(k, (bx + 10, 185), k)
            k2 = daire(p, 36); sh.paste(k2, (bx + 125, 205), k2); d.text((bx + 120, 250), "36px", font=et, fill=fg)
    sh.save(yol)


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--kazanan"); a = ap.parse_args()
    sonuc = {"girdi_sha256_12": {n: hashlib.sha256(open(os.path.join(IFADE, n + ".png"), "rb").read()).hexdigest()[:12]
                                 for n in ("mike-gulen-temiz", "jake-gulen")}}
    adaylar = []
    for v in ("P1", "P2"):
        p, yz = varyant(v); p.convert("RGB").save(os.path.join(ONZ, f"fbv-profil-{v}.png")); adaylar.append((v, p))
        sonuc[v] = olc(p, yz)
    kontak(adaylar, os.path.join(ONZ, "fbv-profil-v2-karsilastirma.png"))
    if a.kazanan:
        hedef = os.path.join(BU, "flipbyvote-profil-800.png"); v1 = os.path.join(BU, "flipbyvote-profil-800-v1.png")
        if not os.path.exists(v1): shutil.copy(hedef, v1)
        p = dict(adaylar)[a.kazanan]; p.convert("RGB").save(hedef, optimize=True)
        kontak([(a.kazanan, p)], os.path.join(BU, "flipbyvote-profil-onizleme.png"))
        sonuc["dosya"] = {"yol": hedef, "bayt": os.path.getsize(hedef), "kazanan": a.kazanan}
    json.dump(sonuc, open(os.path.join(ONZ, "fbv-profil-olcum.json"), "w"), indent=1, ensure_ascii=False)
    print(json.dumps(sonuc, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()
