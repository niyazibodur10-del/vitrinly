#!/usr/bin/env python3
"""Bölüm kapağı: videodan kare + metin paneli → 1080x1920 kapak ve 1080x1350 (4:5) güvenli kırpım.
Kullanım: python3 kapak.py <video> <saniye> <kaynak_y_bas> <kaynak_y_bit> <cikis_onek> [--ep 1] [--ust "$100"] [--alt "$1,000,000"] [--satir "You decide every move."]
Tasarım: kaynak bölge 1:1, y=285'ten başlar → 4:5 güvenli alan (y 285..1635) hem yüz hem metni taşır; 3:4 profil ızgarası
(1080x1440, y 240..1680) bu alanı kapsar. Üst/alt dolgu: aynı karenin bulanık-karartılmış hali."""
import argparse, subprocess, io
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageEnhance

FONT = "/home/user/vitrinly/video/public/fonts/"
ALTIN, JAKE, MIKE = (255, 201, 60), (77, 168, 255), (255, 90, 78)
W, H, GUV_Y, GUV_H = 1080, 1920, 285, 1350

def kare(video, t):
    b = subprocess.run(["ffmpeg", "-v", "error", "-ss", str(t), "-i", video, "-frames:v", "1", "-f", "image2pipe", "-vcodec", "png", "-"],
                       capture_output=True, check=True).stdout
    return Image.open(io.BytesIO(b)).convert("RGB")

def golgeli(d, xy, metin, font, renk, kalinlik=8):
    d.text(xy, metin, font=font, fill=renk, stroke_width=kalinlik, stroke_fill=(10, 10, 14))

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("video"); ap.add_argument("t", type=float); ap.add_argument("y0", type=int); ap.add_argument("y1", type=int)
    ap.add_argument("cikis"); ap.add_argument("--ep", default="1")
    ap.add_argument("--ust", default="$100"); ap.add_argument("--alt", default="$1,000,000")
    ap.add_argument("--satir", default="You decide every move.")
    ap.add_argument("--olcek", type=float, default=1.0, help="kaynak bölge büyütme (yatay merkezden kırpılır)")
    ap.add_argument("--marka", default="FLIP BY VOTE", help="üst bantta (yalnız 9:16'da görünür) marka")
    a = ap.parse_args()
    k = kare(a.video, a.t)
    assert k.size == (W, H), k.size
    zemin = ImageEnhance.Brightness(k.resize((W // 8, H // 8)).filter(ImageFilter.GaussianBlur(3)).resize((W, H))).enhance(0.45)
    tuval = zemin.copy()
    bolge = k.crop((0, a.y0, W, a.y1))
    if a.olcek != 1.0:
        bw, bh = int(W * a.olcek), int(bolge.height * a.olcek)
        bolge = bolge.resize((bw, bh), Image.LANCZOS).crop(((bw - W) // 2, 0, (bw - W) // 2 + W, bh))
    tuval.paste(bolge, (0, GUV_Y))
    alt_y = GUV_Y + bolge.height
    # bölge alt kenarını koyu gradyanla eritip metin paneline bağla
    grad = Image.new("L", (1, 260)); grad.putdata([int(255 * (i / 259) ** 1.4) for i in range(260)])
    koyu = Image.new("RGB", (W, 260), (12, 14, 22))
    tuval.paste(koyu, (0, alt_y - 260), grad.resize((W, 260)))
    ImageDraw.Draw(tuval).rectangle((0, alt_y, W, H), fill=(12, 14, 22))
    d = ImageDraw.Draw(tuval)
    ImageDraw.Draw(tuval).rectangle((0, 0, W, GUV_Y), fill=(12, 14, 22))
    anton = lambda s: ImageFont.truetype(FONT + "Anton-400.woff2", s)
    fred = ImageFont.truetype(FONT + "Fredoka-700.woff2", 66); fred.set_variation_by_axes([700])
    if a.marka:
        d.text((W // 2, GUV_Y // 2 + 20), a.marka, font=anton(96), fill=(255, 255, 255), anchor="mm")
    # EP rozeti
    rozet = f"EP. {a.ep}"; fr = anton(64)
    bx = d.textbbox((0, 0), rozet, font=fr); rw, rh = bx[2] - bx[0] + 56, 92
    ry = alt_y - 40
    d.rounded_rectangle(((W - rw) // 2, ry, (W + rw) // 2, ry + rh), 22, fill=ALTIN)
    d.text((W // 2, ry + rh // 2), rozet, font=fr, fill=(20, 17, 10), anchor="mm")
    # $100 [ok] $1,000,000 — boyut sığdırılarak
    for boy in range(170, 90, -4):
        fa = anton(boy); w1 = d.textlength(a.ust, font=fa); w2 = d.textlength(a.alt, font=fa); ok = boy * 0.75
        if w1 + w2 + ok + 60 <= W - 80: break
    top = w1 + w2 + ok + 60; x = (W - top) / 2; y = ry + rh + 30
    golgeli(d, (x, y), a.ust, fa, ALTIN)
    ox = x + w1 + 30; oy = y + boy * 0.62
    d.polygon([(ox, oy - boy * 0.09), (ox + ok * 0.55, oy - boy * 0.09), (ox + ok * 0.55, oy - boy * 0.22), (ox + ok, oy),
               (ox + ok * 0.55, oy + boy * 0.22), (ox + ok * 0.55, oy + boy * 0.09), (ox, oy + boy * 0.09)], fill=(255, 255, 255),
              outline=(10, 10, 14), width=5)
    golgeli(d, (ox + ok + 30, y), a.alt, fa, (255, 255, 255))
    sy = y + boy * 1.45
    d.text((W // 2, sy), a.satir, font=fred, fill=(235, 240, 250), anchor="ma", stroke_width=4, stroke_fill=(10, 10, 14))
    son = sy + 90
    assert son <= GUV_Y + GUV_H - 20, f"metin güvenli alanın dışına taşıyor: {son}"
    tuval.save(a.cikis + "-1080x1920.jpg", quality=92)
    tuval.crop((0, GUV_Y, W, GUV_Y + GUV_H)).save(a.cikis + "-1080x1350.jpg", quality=92)
    print(f"bölge {a.y0}-{a.y1} → tuval {GUV_Y}-{alt_y}; ok satırı boyu {boy}px; metin alt sınırı {son:.0f} ≤ {GUV_Y+GUV_H-20}")

if __name__ == "__main__":
    main()
