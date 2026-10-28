#!/usr/bin/env python3
"""F8 thumbnail testleri: 168x94 OCR okunurluğu, mobil kontrol sayfası, rakip yan yana ızgara, başlıkla okunuş.
Kullanım: python3 thumb-test.py <rakip_klasoru> [aday ...]
Rakip thumbnail'ları i.ytimg.com'dan repo DIŞINA indirilir (ilk argüman); repoya yalnız ızgara görüntüsü girer.
"""
import json, os, re, subprocess, sys, tempfile
from PIL import Image, ImageDraw, ImageFont, ImageFilter

KOK = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(KOK, "..", "..", "..", ".."))
BASLIK = "You Have $1,000 in 1929. Can You Keep It?"
BEKLENEN = {"A1": "PICK A DOOR", "A2": "ONE IS A DISASTER", "B1": "THE SURPRISE DOOR", "B2": "EVERYONE LAUGHED",
            "C1": "STOCKS 89", "C2": "THE 89 DOOR", "D1": "EVERY DOOR LOCKED", "D2": "MARCH 1933", "D3": "EVERY BANK CLOSED"}
DJV = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
DJVB = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"

def f(px, b=False):
    p = DJVB if b else DJV
    return ImageFont.truetype(p, px) if os.path.exists(p) else ImageFont.load_default()

def ocr(img, boy=(168, 94)):
    """168x94'e küçült → x4 büyüt (göz yerine OCR; bilgi 168x94'te kaybolduysa geri gelmez) → tesseract."""
    from PIL import ImageOps
    k = img.resize(boy, Image.LANCZOS).resize((boy[0] * 4, boy[1] * 4), Image.BICUBIC) if boy != img.size else img
    out = ""
    for v in (k, ImageOps.invert(k.convert("L"))):      # beyaz-konturlu metin için ters çevrilmiş de denenir
        with tempfile.NamedTemporaryFile(suffix=".png") as t:
            v.save(t.name)
            out += " " + subprocess.run(["tesseract", t.name, "-", "--psm", "11"], capture_output=True, text=True).stdout
    return re.sub(r"[^A-Z0-9 ]", " ", out.upper())

def ocr_skor(vid, img):
    kel = BEKLENEN[vid].split(); r = {"beklenen": kel}
    for ad, boy in (("tam_1280", img.size), ("mobil_168", (168, 94))):
        metin = ocr(img, boy); bul = [w for w in kel if re.search(r"\b" + w + r"\b", metin)]
        r[ad] = {"bulunan": bul, "oran": round(len(bul) / len(kel), 2), "ham": " ".join(metin.split())[:80]}
    # OCR araç sınırı: tam boyutta da bulunamayan kelime 168'de ölçülemez → oran tam boyutta bulunanlara göre
    taban = r["tam_1280"]["bulunan"]
    r["mobil_korunan"] = round(len([w for w in taban if w in r["mobil_168"]["bulunan"]]) / max(1, len(taban)), 2)
    return r

def mobil_sayfa(imgs, yol):
    n = len(imgs)
    sh = Image.new("RGB", (40 + n * 200, 420), (255, 255, 255)); d = ImageDraw.Draw(sh)
    for i, (v, im) in enumerate(imgs.items()):
        x = 20 + i * 200
        t = im.resize((168, 94), Image.LANCZOS); sh.paste(t, (x, 30))
        sh.paste(t.convert("L").convert("RGB"), (x, 140))                        # gri ton (değer kontrastı)
        sh.paste(t.filter(ImageFilter.GaussianBlur(1.2)), (x, 250))               # "kısık göz" bulanıklık
        d.text((x, 8), v, font=f(16, True), fill=(0, 0, 0))
    for y, e in ((30, "168x94"), (140, "gri"), (250, "bulanik 1.2px")):
        d.text((20, y + 98), e, font=f(12), fill=(90, 90, 90))
    sh.save(yol)

def kart(img, baslik, kanal, w=320):
    h = int(w * 9 / 16); c = Image.new("RGB", (w, h + 70), (15, 15, 15)); d = ImageDraw.Draw(c)
    c.paste(img.resize((w, h), Image.LANCZOS), (0, 0))
    d.rounded_rectangle((w - 50, h - 24, w - 6, h - 6), radius=4, fill=(0, 0, 0)); d.text((w - 46, h - 23), "11:54", font=f(13, True), fill=(255, 255, 255))
    # başlığı 2 satıra böl
    sat, cur = [], ""
    for wd in baslik.split():
        if f(15, True).getlength(cur + " " + wd) > w - 10: sat.append(cur); cur = wd
        else: cur = (cur + " " + wd).strip()
    sat.append(cur)
    for i, s in enumerate(sat[:2]): d.text((4, h + 6 + i * 19), s, font=f(15, True), fill=(241, 241, 241))
    d.text((4, h + 48), kanal, font=f(12), fill=(170, 170, 170))
    return c

def rakip_izgara(imgs, rakip_dir, yol):
    meta = json.load(open(os.path.join(rakip_dir, "meta.json")))
    hucre = [(Image.open(os.path.join(rakip_dir, m["id"] + ".jpg")).convert("RGB"), m["baslik"], m["kanal"]) for m in meta]
    bizim = [(im, BASLIK, f"Toonomy · {v}") for v, im in imgs.items()]
    # bizimkiler 2., 5., 8. sıraya (akışta rakiplerin arasında)
    sira = list(hucre);
    for j, b in enumerate(bizim): sira.insert(1 + j * 4, b)
    cols = 4; rows = (len(sira) + cols - 1) // cols
    g = Image.new("RGB", (cols * 330 + 10, rows * 255 + 10), (15, 15, 15))
    for i, (im, b, k) in enumerate(sira):
        g.paste(kart(im, b, k), (10 + (i % cols) * 330, 10 + (i // cols) * 255))
    g.save(yol, quality=88)
    # mobil liste (168x94 + başlık sağda), aynı sıra
    m = Image.new("RGB", (420, len(sira) * 104 + 10), (255, 255, 255)); d = ImageDraw.Draw(m)
    for i, (im, b, k) in enumerate(sira):
        y = 10 + i * 104; m.paste(im.resize((168, 94), Image.LANCZOS), (8, y))
        sat, cur = [], ""
        for wd in b.split():
            if f(13, True).getlength(cur + " " + wd) > 230: sat.append(cur); cur = wd
            else: cur = (cur + " " + wd).strip()
        sat.append(cur)
        for j, s in enumerate(sat[:3]): d.text((184, y + 2 + j * 17), s, font=f(13, True), fill=(15, 15, 15))
        d.text((184, y + 60), k, font=f(11), fill=(96, 96, 96))
    m.save(yol.replace(".jpg", "-mobil-liste.jpg"), quality=90)

def benzerlik(imgs, rakip_dir):
    """Karışma ölçüsü: 16x9 küçük kopyada ortalama renk farkı (RGB öklid, 0–441) + 9x8 dHash Hamming (0–64).
    Bizim her finalist için en yakın rakip; finalistler arası fark (Test & Compare için ayrışma)."""
    import numpy as np
    meta = json.load(open(os.path.join(rakip_dir, "meta.json")))
    def v(im): return np.array(im.convert("RGB").resize((16, 9), Image.LANCZOS)).astype(float)
    def dh(im):
        g = np.array(im.convert("L").resize((9, 8), Image.LANCZOS)).astype(int); return (g[:, 1:] > g[:, :-1]).ravel()
    def fark(a, b): return round(float(np.sqrt(((v(a) - v(b)) ** 2).sum(-1)).mean()), 1), int((dh(a) != dh(b)).sum())
    rak = {m["kanal"] + ":" + m["id"]: Image.open(os.path.join(rakip_dir, m["id"] + ".jpg")) for m in meta}
    out = {"rakip": {}, "finalist_arasi": {}}
    for k, im in imgs.items():
        fs = sorted(((fark(im, r), n) for n, r in rak.items()), key=lambda x: x[0][0])
        out["rakip"][k] = {"en_yakin": fs[0][1], "renk_farki": fs[0][0][0], "dhash": fs[0][0][1],
                           "rakip_ortalama_renk_farki": round(sum(f[0][0] for f in fs) / len(fs), 1)}
    ks = list(imgs)
    for i in range(len(ks)):
        for j in range(i + 1, len(ks)):
            out["finalist_arasi"][ks[i] + "-" + ks[j]] = dict(zip(("renk_farki", "dhash"), fark(imgs[ks[i]], imgs[ks[j]])))
    return out

def main():
    rakip = sys.argv[1]; sec = sys.argv[2:] or sorted(BEKLENEN)
    imgs = {}
    for v in sec:
        import glob
        fin = glob.glob(os.path.join(KOK, v + "-*.jpg"))
        p = fin[0] if fin else os.path.join(KOK, "adaylar", v + ".jpg")
        imgs[v] = Image.open(p).convert("RGB")
    os.makedirs(os.path.join(KOK, "test"), exist_ok=True)
    son = {v: ocr_skor(v, im) for v, im in imgs.items()}
    for v, r in son.items(): print(f"{v}: OCR tam {r['tam_1280']['oran']:.2f} {r['tam_1280']['bulunan']} | 168x94 {r['mobil_168']['oran']:.2f} {r['mobil_168']['bulunan']} | korunan {r['mobil_korunan']:.2f}")
    import glob
    etiket = "finalist" if all(glob.glob(os.path.join(KOK, v + "-*.jpg")) for v in sec) else "adaylar"
    json.dump(son, open(os.path.join(KOK, "test", f"ocr-168x94-{etiket}.json"), "w"), ensure_ascii=False, indent=1)
    mobil_sayfa(imgs, os.path.join(KOK, "test", f"mobil-168x94-{etiket}.png"))
    if etiket == "finalist":
        rakip_izgara(imgs, rakip, os.path.join(rakip, "rakip-yan-yana.jpg"))   # rakip görseli içerir → repo dışı
        b = benzerlik(imgs, rakip); print(json.dumps(b, ensure_ascii=False))
        json.dump(b, open(os.path.join(KOK, "test", "rakip-benzerlik.json"), "w"), ensure_ascii=False, indent=1)

if __name__ == "__main__":
    main()
