#!/usr/bin/env python3
"""Thumbnail kafa değişimi (yeni Canva üretimi yok). Gövde = miras 05-gorsel/leo/<M>.png, kafa = 1929 05-gorsel/leo/<ifade>.png.
Hiza: kafa bölgesinde (y 40–340, x 820–1100) gri ton mutlak farkı en küçük kayma (±70 px). Maske hedef koordinatında, y_kes'te yumuşak geçiş.
Kullanım: python3 -I kafa-degis.py <govde M06> <kafa c-isaret> <cikis adı> [dx] [y_kes]  → leo/<cikis>.png + hiza raporu (stdout)"""
import os, sys, numpy as np
from PIL import Image, ImageDraw, ImageFilter
KOK = os.path.dirname(os.path.abspath(__file__)); VID = os.path.abspath(os.path.join(KOK, "..", ".."))
L29 = os.path.join(VID, "..", "2026-10-26-1929-1000-dolar/05-gorsel/leo")
def gri(im): x = np.array(im).astype(float); return x[..., :3].mean(-1) * (x[..., 3] > 0)
def hiza(govde, kafa):
    A, B = gri(govde), gri(kafa); en = None
    for dy in range(-30, 31, 2):
        for dx in range(-70, 71, 2):
            e = np.abs(A[40:340, 820:1100] - np.roll(np.roll(B, dy, 0), dx, 1)[40:340, 820:1100]).mean()
            if en is None or e < en[0]: en = (e, dx, dy)
    return en
def degis(govde, kafa, dx, dy, y_kes=392, yumus=16):
    k = Image.new("RGBA", govde.size, (0, 0, 0, 0)); k.paste(kafa, (dx, dy), kafa)
    m = Image.new("L", govde.size, 0); d = ImageDraw.Draw(m)
    d.ellipse((770, -60, 1120, y_kes + 30), fill=255); d.rectangle((770, -60, 1120, 200), fill=255)
    a = np.array(m.filter(ImageFilter.GaussianBlur(yumus))).astype(np.float32) / 255; a[y_kes + 30:, :] = 0
    ka = np.array(k.getchannel("A")).astype(np.float32) / 255; w = a * ka
    G = np.array(govde).astype(np.float32); K = np.array(k).astype(np.float32)
    # maske içinde kafa katmanı gövdenin YERİNE geçer (eski kafanın kulak/saç/çene izi kalmasın): premultiplied karışım
    Ga = G[..., 3:] / 255 * (1 - a[..., None]); Kw = w[..., None]
    alfa = Ga + Kw; out = G.copy()
    out[..., :3] = np.where(alfa > 0, (G[..., :3] * Ga + K[..., :3] * Kw) / np.maximum(alfa, 1e-6), G[..., :3]); out[..., 3] = (alfa[..., 0] * 255)
    return Image.fromarray(out.round().astype(np.uint8), "RGBA")
if __name__ == "__main__":
    gv, kf, ad = sys.argv[1:4]
    govde = Image.open(os.path.join(VID, "05-gorsel/leo", gv + ".png")).convert("RGBA"); kafa = Image.open(os.path.join(L29, kf + ".png")).convert("RGBA")
    e, dx, dy = hiza(govde, kafa)
    if len(sys.argv) > 4: dx = int(sys.argv[4])          # elle dx (eğik kafada boyun sürekliliği için hiza ile yaka arasında uzlaşma)
    yk = int(sys.argv[5]) if len(sys.argv) > 5 else 392
    out = degis(govde, kafa, dx, dy, y_kes=yk)
    # yaka geçişi: y_kes ±40 satırında gövde ile fark (sıçrama ölçüsü, gorsel-varlik-sanatcisi 'satır sıçraması' ile aynı mantık)
    s = np.abs(gri(out)[352:432, 800:1100] - gri(govde)[352:432, 800:1100]).mean()
    out.save(os.path.join(KOK, "leo", ad + ".png")); print(f"{ad}: hiza farkı {e:.2f} dx {dx} dy {dy} | yaka bandı fark {s:.2f}")
