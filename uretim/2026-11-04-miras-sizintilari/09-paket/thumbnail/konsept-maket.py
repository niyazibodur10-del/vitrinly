#!/usr/bin/env python3
"""F4 erken thumbnail maketi (S03 miras): her konseptin metin yerleşimini düz zemin + gri yer tutucu (Leo/nesne) ile çizer,
168x94'e küçültüp satır satır OCR (psm 7, normal + ters) ve metin↔zemin p5 kontrastı ölçer. Görsel gelince F8a'da thumb-uret v2'ye taşınır.
Kullanım: THUMB_TMP=<geçici> python3 -I konsept-maket.py  → maket/*.png + maket/olcum.json"""
import os, re, json, subprocess, tempfile, numpy as np
from PIL import Image, ImageDraw, ImageOps
KOK = os.path.dirname(os.path.abspath(__file__)); REPO = os.path.abspath(os.path.join(KOK, "../../../.."))
W, H = 1280, 720; LAC = (11, 16, 38); BEYAZ = (255, 255, 255); SARI = (255, 210, 63); KIRMIZI = (214, 40, 40)
SURE = (1088, 634, 1280, 720)
def font(px):
    from PIL import ImageFont
    ttf = os.path.join(os.environ.get("THUMB_TMP", "/tmp"), "Anton-400.ttf")
    if not os.path.exists(ttf):
        from fontTools.ttLib import TTFont
        f = TTFont(os.path.join(REPO, "video/public/fonts/Anton-400.woff2")); f.flavor = None; f.save(ttf)
    return ImageFont.truetype(ttf, px)
def lum(c):
    v = np.asarray(c, dtype=float) / 255; v = np.where(v <= 0.03928, v / 12.92, ((v + 0.055) / 1.055) ** 2.4)
    return 0.2126 * v[..., 0] + 0.7152 * v[..., 1] + 0.0722 * v[..., 2]
def satir(img, x, y, kelimeler, px, plaka=None):
    """kelimeler: [(yazı, dolgu, kontur)]; kelime kelime, boşluk 0,32 em (1929 dersi). Döner bbox listesi."""
    d = ImageDraw.Draw(img); f = font(px); kut = []; cx = x
    for t, dol, kon in kelimeler:
        b = d.textbbox((cx, y), t, font=f)
        if plaka: d.rectangle((b[0] - 22, b[1] - 14, b[2] + 22, b[3] + 14), fill=plaka)
        d.text((cx, y), t, font=f, fill=dol, stroke_width=(max(6, px // 11) if kon else 0), stroke_fill=kon)
        kut.append({"metin": t, "dolgu": dol, "bbox": list(b), "plaka": plaka}); cx = b[2] + 0.32 * px + (44 if plaka else 0)
    return kut
def yer_tutucu(img, kutular):
    d = ImageDraw.Draw(img)
    for k in kutular: d.rounded_rectangle(k, 40, fill=(120, 120, 120))
# konsept: zemin, yer tutucu (Leo/nesne alanı), satırlar [(y, px, [(kelime, dolgu, kontur)], plaka)]
K = {
 "K1a": ((10, 78, 88), [(640, 90, 1240, 720)], [(70, 200, [("WHO", SARI, LAC), ("GETS", SARI, LAC)], None), (300, 200, [("IT?", SARI, LAC)], None), (540, 120, [("$124T", BEYAZ, None)], KIRMIZI)]),
 "K1b": ((10, 78, 88), [(640, 90, 1240, 720)], [(90, 210, [("WHAT'S", SARI, LAC)], None), (330, 210, [("LEFT?", SARI, LAC)], None)]),
 "K2a": ((150, 215, 200), [(560, 260, 1280, 720), (0, 560, 560, 720)], [(50, 220, [("IT", LAC, BEYAZ), ("LEAKS", LAC, BEYAZ)], None)]),
 "K2b": ((150, 215, 200), [(560, 260, 1280, 720), (0, 560, 560, 720)], [(40, 150, [("LEAKING", LAC, BEYAZ)], None), (230, 150, [("ALL", LAC, BEYAZ), ("THE", LAC, BEYAZ), ("WAY", LAC, BEYAZ)], None)]),
 "K3a": ((250, 225, 140), [(40, 300, 560, 720), (560, 180, 900, 720), (960, 520, 1180, 700)], [(40, 180, [("SMALLER.", LAC, BEYAZ)], None), (40, 180, [], None)]),
 "K3b": ((250, 225, 140), [(40, 330, 560, 720), (560, 230, 900, 720), (960, 540, 1180, 700)], [(40, 170, [("SENT", LAC, BEYAZ), ("BIG,", LAC, BEYAZ), ("GOT", KIRMIZI, BEYAZ), ("SMALL", KIRMIZI, BEYAZ)], None)]),
 "K4a": ((196, 64, 44), [(560, 60, 1280, 720)], [(70, 170, [("IT", BEYAZ, LAC), ("KEEPS", BEYAZ, LAC)], None), (300, 170, [("LEAKING", BEYAZ, None)], LAC)]),
 "K4b": ((196, 64, 44), [(560, 60, 1280, 720)], [(110, 230, [("MORE", BEYAZ, LAC)], None), (370, 230, [("TAPE?", BEYAZ, LAC)], None)]),
}
# K3a ikinci satır: "LATER." kırmızı levha (karşıtlık rengi)
K["K3a"] = (K["K3a"][0], K["K3a"][1], [(40, 170, [("SMALLER.", LAC, BEYAZ)], None), (270, 150, [("LATER.", BEYAZ, None)], KIRMIZI)])
def ocr_satir(img168, bbox):
    sx = 168 / W; x0, y0, x1, y1 = bbox
    kr = img168.crop((max(0, int(x0 * sx) - 3), max(0, int(y0 * sx) - 3), min(168, int(x1 * sx) + 4), min(94, int(y1 * sx) + 4)))
    kr = kr.resize((kr.width * 4, kr.height * 4), Image.BICUBIC); out = ""
    for v in (kr.convert("L"), ImageOps.invert(kr.convert("L"))):
        with tempfile.NamedTemporaryFile(suffix=".png") as t:
            v.save(t.name); out += " " + subprocess.run(["tesseract", t.name, "-", "--psm", "7"], capture_output=True, text=True).stdout
    return re.sub(r"S(?=\d)", "$", out.upper())
def main():
    os.makedirs(os.path.join(KOK, "maket"), exist_ok=True); sonuc = {}
    for ad, (zemin, yt, satirlar) in K.items():
        img = Image.new("RGB", (W, H), zemin); zem = np.array(img).astype(float); yer_tutucu(img, yt)   # p5 = metin ↔ planlanan zemin; yer tutucu çakışması F8a gerçek görselde ölçülür
        kut = []; satir_kut = []
        for y, px, kel, pl in satirlar:
            if not kel: continue
            k = satir(img, 60, y, kel, px, pl); kut += k
            satir_kut.append(([w["metin"] for w in k], [min(b["bbox"][0] for b in k), min(b["bbox"][1] for b in k), max(b["bbox"][2] for b in k), max(b["bbox"][3] for b in k)], px))
        img.save(os.path.join(KOK, "maket", ad + ".png")); k168 = img.resize((168, 94), Image.LANCZOS)
        k168.resize((672, 376), Image.NEAREST).save(os.path.join(KOK, "maket", ad + "-168.png"))
        r = {"kelime": len(kut), "satirlar": []}
        for kel, bb, px in satir_kut:
            o = ocr_satir(k168, bb); bul = [w for w in kel if re.sub(r"[^A-Z0-9$]", "", w) and re.sub(r"[^A-Z0-9$]", "", w) in re.sub(r"[^A-Z0-9$ ]", " ", o).split()]
            capH = font(px).getbbox("H"); r["satirlar"].append({"kelimeler": kel, "ocr168_bulunan": bul, "buyuk_harf_168_px": round((capH[3] - capH[1]) * 168 / W, 1)})
        p5 = []
        for k in kut:
            x0, y0, x1, y1 = [int(v) for v in k["bbox"]]
            if k["plaka"]: bl = np.array([lum(k["plaka"])])
            else: bl = lum(zem[max(0, y0 - 24):y1 + 24, max(0, x0 - 24):x1 + 24]).ravel()
            lt = lum(k["dolgu"]); rr = (np.maximum(bl, lt) + .05) / (np.minimum(bl, lt) + .05); p5.append(float(np.percentile(rr, 5)))
        r["kontrast_p5_min"] = round(min(p5), 2)
        r["sure_damgasi_ihlal"] = any(k["bbox"][2] > SURE[0] and k["bbox"][3] > SURE[1] for k in kut)
        sonuc[ad] = r
    json.dump(sonuc, open(os.path.join(KOK, "maket", "olcum.json"), "w"), ensure_ascii=False, indent=1)
    for a, r in sonuc.items():
        print(a, "kelime", r["kelime"], "| OCR168", sum(len(s["ocr168_bulunan"]) for s in r["satirlar"]), "/", r["kelime"], "| harf168 min", min(s["buyuk_harf_168_px"] for s in r["satirlar"]), "px | p5", r["kontrast_p5_min"], "| damga", r["sure_damgasi_ihlal"])
if __name__ == "__main__": main()
