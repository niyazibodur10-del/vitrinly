#!/usr/bin/env python3
"""F5 varlık hazırlığı — S08 Kitchen Table Budget (animasyon-yonetmeni, 2026-11-02).
Üretir (git dışı, yeniden üretilebilir): video/public/kbutce/
  plakalar G01 G06 G10 (16:9) + G09 (9:16) JPEG q92 · nesneler (G03 zarflar, G07 ev nesneleri) PNG
  Leo bel üstü pozları (1929 kesikleri + G05 zarftan-zarf) 1929 ile AYNI ortak kırpım kutusunda → rig yamaları dikişsiz
  rig yamaları (alfa × taban a silüeti) + tek göz kırpma · ses (varsa): anlatim.wav, shorts-1-ek.wav, shorts-2-ek.wav
Üretir (git içinde): video/src/videolar/yeni-video/rig.ts
Kullanım: ~/.finansal-arac/venv/bin/python -I uretim/2026-10-28-yeni-video/07-animasyon/varlik-hazirla.py
Kaynak desen: uretim/2026-10-26-1929-1000-dolar/07-animasyon/hazirla-tam.py (görsel kısmı)."""
import json, shutil
from pathlib import Path
import numpy as np
from PIL import Image
KOK = Path(__file__).resolve().parents[3]
U = KOK / "uretim/2026-10-28-yeni-video"; G = U / "05-gorsel"; S = U / "04-ses"
G29 = KOK / "uretim/2026-10-26-1929-1000-dolar/05-gorsel"
P = KOK / "video/public/kbutce"; P.mkdir(parents=True, exist_ok=True)
RIG_POZ = {"a": "a-konusma-kapali", "b": "b-konusma-acik", "C12": "C12-sunum", "C13": "C13-kollar-kavusmus",
           "C14": "C14-kutu-gogus", "C21": "C21-el-sallar", "balt": "b-alt-gulumseyerek-konusma"}
IFADE_POZ = {"c": "c-isaret", "d": "d-saskin", "e": "e-dusunen", "f": "f-sevincli", "C20": "C20-saate-bakar"}
def main():
    for c in ["G01", "G06", "G10", "G09"]:
        Image.open(G / f"canva-ham/{c}.png").convert("RGB").save(P / f"{c}.jpg", quality=92)
    nesne = {}
    for f in sorted((G / "nesne").glob("G0*.png")):  # alfa kutusuna kırp (yerleşim kodda en-boy oranıyla)
        im = Image.open(f).convert("RGBA"); im = im.crop(im.getbbox()); im.save(P / f.name, optimize=True)
        nesne[f.stem] = [im.width, im.height]
    kaynak = {ad: G29 / f"leo/{f}.png" for ad, f in {**RIG_POZ, **IFADE_POZ}.items()}
    bx = []
    for f in kaynak.values():
        al = np.array(Image.open(f))[:, :, 3]; ys, xs = np.where(al > 8); bx.append((xs.min(), ys.min(), xs.max(), ys.max()))
    bx = np.array(bx)
    kutu = (max(0, int(bx[:, 0].min()) - 6), max(0, int(bx[:, 1].min()) - 6), min(1920, int(bx[:, 2].max()) + 7), 1080)
    kaynak["G05"] = G / "leo/G05-zarftan-zarf.png"  # kafa a ile hizalı (gorsel rapor: kor. 0,97, kayma <0,5 px)
    for ad, f in kaynak.items():
        Image.open(f).convert("RGBA").crop(kutu).save(P / f"leo-{ad}.png", optimize=True)
    rig = json.load(open(G29 / "rig/rig-yamalar.json"))["yamalar"]
    a_al = np.array(Image.open(kaynak["a"]))[:, :, 3].astype(np.float32) / 255
    yama = {}
    for ad, r in rig.items():
        x, y = r["konum_xy"]; w, h = r["boyut_wh"]
        ya = np.array(Image.open(G29 / f"rig/{ad}.png").convert("RGBA")).astype(np.float32)
        ya[:, :, 3] *= a_al[y:y + h, x:x + w]
        Image.fromarray(ya.astype(np.uint8)).save(P / f"{ad}.png")
        yama[ad] = {"x": x - kutu[0], "y": y - kutu[1], "w": w, "h": h}
    g = np.array(Image.open(P / "goz-kapali-C06.png").convert("RGBA")).astype(np.float32)
    cols = np.where(g[:, :, 3].max(0) > 40)[0]; orta = int(cols.min() + (cols.max() - cols.min()) * 0.5)
    g[:, :, 3] *= np.clip((orta + 6 - np.arange(g.shape[1])) / 12.0, 0, 1)[None, :]
    Image.fromarray(g.astype(np.uint8)).save(P / "goz-tek-C06.png"); yama["goz-tek-C06"] = dict(yama["goz-kapali-C06"])
    ses = []
    for f in ["anlatim.wav", "shorts-1-ek.wav", "shorts-2-ek.wav"]:
        if (S / f).exists():
            shutil.copy(S / f, P / f); ses.append(f)
    (KOK / "video/src/videolar/yeni-video/rig.ts").write_text(
        "// Otomatik üretildi: uretim/2026-10-28-yeni-video/07-animasyon/varlik-hazirla.py — elle düzenleme.\n"
        "export type Kutu = {x: number; y: number; w: number; h: number};\n"
        "export const KLASOR = \"kbutce\";\n"
        f"export const NESNE: Record<string, [number, number]> = {json.dumps(nesne)};\n"
        f"export const SUNUCU_T: Kutu = {json.dumps({'x': kutu[0], 'y': kutu[1], 'w': kutu[2] - kutu[0], 'h': kutu[3] - kutu[1]})};\n"
        f"export const YAMA_T: Record<string, Kutu> = {json.dumps(yama)};\n"
        "export const AGIZ_YAMA: Record<string, string> = {\"B\": \"agiz-B-C07\", \"C\": \"agiz-C-C08\", \"H\": \"agiz-C-C08\", \"E\": \"agiz-E-C09\", \"F\": \"agiz-F-C10\", \"G\": \"agiz-B-C07\"};\n")
    print(json.dumps({"kutu": kutu, "yama": len(yama), "ses": ses}))
if __name__ == "__main__":
    main()
