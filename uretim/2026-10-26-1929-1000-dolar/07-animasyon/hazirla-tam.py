#!/usr/bin/env python3
"""F5 tam video + 9:16 — varlık ve veri hazırlığı (animasyon-yonetmeni, 2026-10-27).

Üretir (yeniden üretilebilir, git dışı): video/public/k1929t/
  - plakalar C01 C03 C15(sepya) C16 C17 C18 C19 (JPEG q92), C22 dikey stüdyo
  - C01 kapı bölgesi Real-ESRGAN x4 → x2 (punch-in ve 9:16 kapı kırpımları; 07-animasyon/buyutme/)
  - bel üstü Leo pozları (rig uyumlu: a b C12 C13 C14 C21 b-alt; ifade: c d e f C20) ortak kırpım kutusunda
  - tam boy pozlar C02 C04 C05; rig yamaları (alfa × taban a silüeti) + tek göz kırpma
  - ses: anlatim.wav (tam) + shorts-1-ek.wav, shorts-2-ek.wav
Üretir (git içinde): video/src/k1929/veri-tam.ts — sahne sınırları, sahne başına kelimeler ve ağız çizelgesi (yerel zaman),
  altyazı parçaları (global), Shorts ek kayıtları.
Önkoşul: rhubarb-tum.py (07-animasyon/rhubarb/sahne/*-kapili.json).
Kullanım: ~/.finansal-arac/venv/bin/python -I hazirla-tam.py
"""
import json, re, shutil, subprocess
from pathlib import Path
import numpy as np
from PIL import Image

KOK = Path(__file__).resolve().parents[3]
U = KOK / "uretim/2026-10-26-1929-1000-dolar"
G, S, A = U / "05-gorsel", U / "04-ses", U / "07-animasyon"
P = KOK / "video/public/k1929t"; P.mkdir(parents=True, exist_ok=True)

RIG_POZ = {"a": "a-konusma-kapali", "b": "b-konusma-acik", "C12": "C12-sunum", "C13": "C13-kollar-kavusmus",
           "C14": "C14-kutu-gogus", "C21": "C21-el-sallar", "balt": "b-alt-gulumseyerek-konusma"}
IFADE_POZ = {"c": "c-isaret", "d": "d-saskin", "e": "e-dusunen", "f": "f-sevincli", "C20": "C20-saate-bakar"}
TAM_BOY = {"C02": "C02-tam-boy", "C04": "C04-yurume", "C05": "C05-kutuyla-yurume"}
KAPI_KUTU = (460, 215, 1440, 765)  # buyut.py kırpımı (C01 koordinatı)

# Altyazı anahtar kelime renkleri: kapı renkleri + sarı vurgu (altyazi-parcalar.json 'hl')
MAVI, YESIL, KAHVE, SARI = "#4da3ff", "#5fd35f", "#e0884a", "#ffd43b"
RENK = {"blue": MAVI, "stock": MAVI, "stocks": MAVI, "green": YESIL, "bank": YESIL, "banks": YESIL,
        "brown": KAHVE, "shoebox": KAHVE, "box": KAHVE, "boxes": KAHVE, "shoeboxes": KAHVE}


def main():
    for c in ["C01", "C03", "C16", "C17", "C18", "C19", "C22"]:
        Image.open(G / f"canva-ham/{c}.png").convert("RGB").save(P / f"{c}.jpg", quality=92)
    Image.open(G / "plaka/C15-sepya.png").convert("RGB").save(P / "C15.jpg", quality=92)
    x4 = A / "buyutme/C01-kapilar-x4.png"
    if x4.exists():
        im = Image.open(x4); im.resize((im.width // 2, im.height // 2), Image.LANCZOS).save(P / "C01-kapilar-x2.jpg", quality=93)

    tum = {**RIG_POZ, **IFADE_POZ}
    bx = []
    for f in tum.values():
        al = np.array(Image.open(G / f"leo/{f}.png"))[:, :, 3]; ys, xs = np.where(al > 8)
        bx.append((xs.min(), ys.min(), xs.max(), ys.max()))
    bx = np.array(bx)
    kutu = (max(0, int(bx[:, 0].min()) - 6), max(0, int(bx[:, 1].min()) - 6), min(1920, int(bx[:, 2].max()) + 7), 1080)
    for ad, f in tum.items():
        Image.open(G / f"leo/{f}.png").crop(kutu).save(P / f"leo-{ad}.png", optimize=True)
    poz_tam = {}
    for ad, f in TAM_BOY.items():
        im = Image.open(G / f"leo/{f}.png").convert("RGBA"); al = np.array(im)[:, :, 3]; ys, xs = np.where(al > 8)
        k = (max(0, xs.min() - 6), max(0, ys.min() - 6), min(1920, xs.max() + 7), min(1080, ys.max() + 7))
        im.crop(k).save(P / f"leo-{ad}.png", optimize=True)
        poz_tam[ad] = {"x": int(k[0]), "y": int(k[1]), "w": int(k[2] - k[0]), "h": int(k[3] - k[1])}

    rig = json.load(open(G / "rig/rig-yamalar.json"))["yamalar"]
    a_al = np.array(Image.open(G / "leo/a-konusma-kapali.png"))[:, :, 3].astype(np.float32) / 255
    yama = {}
    for ad, r in rig.items():
        x, y = r["konum_xy"]; w, h = r["boyut_wh"]
        ya = np.array(Image.open(G / f"rig/{ad}.png").convert("RGBA")).astype(np.float32)
        ya[:, :, 3] *= a_al[y:y + h, x:x + w]
        Image.fromarray(ya.astype(np.uint8)).save(P / f"{ad}.png")
        yama[ad] = {"x": x - kutu[0], "y": y - kutu[1], "w": w, "h": h}
    g = np.array(Image.open(P / "goz-kapali-C06.png").convert("RGBA")).astype(np.float32)
    cols = np.where(g[:, :, 3].max(0) > 40)[0]; orta = int(cols.min() + (cols.max() - cols.min()) * 0.5)
    g[:, :, 3] *= np.clip((orta + 6 - np.arange(g.shape[1])) / 12.0, 0, 1)[None, :]
    Image.fromarray(g.astype(np.uint8)).save(P / "goz-tek-C06.png"); yama["goz-tek-C06"] = dict(yama["goz-kapali-C06"])

    for f in ["anlatim.wav", "shorts-1-ek.wav", "shorts-2-ek.wav"]:
        shutil.copy(S / f, P / f)

    sah = json.load(open(S / "sahne-zamanlari.json"))["sahneler"]
    kel = json.load(open(S / "kelimeler-hizali.json"))["words"]
    sahneler = []
    for s in sah:
        ad = s["sahne"]; b = s["bas"]
        cues = json.load(open(A / f"rhubarb/sahne/{ad}-kapili.json"))["mouthCues"]
        ks = [{"w": w["w"], "s": round(w["s"] - b, 3), "e": round(w["e"] - b, 3)} for w in kel if w["sahne"] == ad]
        sahneler.append({"id": ad, "bas": b, "bitis": s["bitis"], "sure": round(s["bitis"] - b, 3), "kelimeler": ks,
                         "agiz": [{"start": c["start"], "end": c["end"], "value": c["value"]} for c in cues]})
    parcalar = []
    for p in json.load(open(S / "altyazi-parcalar.json")):
        out = []
        for w in p:
            k = re.sub(r"[^a-z']", "", w["t"].lower())
            renk = RENK.get(k) or (SARI if w.get("hl") else None)
            out.append({"t": w["t"], "s": w["s"], "e": w["e"], "renk": renk})
        parcalar.append(out)
    shorts = {}
    for n in (1, 2):
        z = json.load(open(S / f"shorts-{n}-ek-ham.zaman.json"))["cumleler"]
        cues = json.load(open(A / f"rhubarb/sahne/shorts-{n}-ek-kapili.json"))["mouthCues"]
        sure = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(S / f"shorts-{n}-ek.wav")],
                                    capture_output=True, text=True).stdout)
        shorts[f"sh{n}"] = {"sure": round(sure, 3), "cumleler": z, "agiz": cues}

    ts = KOK / "video/src/k1929/veri-tam.ts"
    ts.write_text(
        "// Otomatik üretildi: uretim/2026-10-26-1929-1000-dolar/07-animasyon/hazirla-tam.py — elle düzenleme.\n"
        "import type { Cue, Kelime, Kutu } from \"./veri\";\n"
        "export type SahneVeri = {id: string; bas: number; bitis: number; sure: number; kelimeler: {w: string; s: number; e: number}[]; agiz: Cue[]};\n"
        f"export const KLASOR = \"k1929t\";\n"
        f"export const SUNUCU_T: Kutu = {json.dumps({'x': kutu[0], 'y': kutu[1], 'w': kutu[2] - kutu[0], 'h': kutu[3] - kutu[1]})};\n"
        f"export const YAMA_T: Record<string, Kutu> = {json.dumps(yama)};\n"
        f"export const POZ_T: Record<string, Kutu> = {json.dumps(poz_tam)};\n"
        f"export const KAPI_KUTU = {json.dumps(list(KAPI_KUTU))};\n"
        f"export const SAHNELER: SahneVeri[] = {json.dumps(sahneler, ensure_ascii=False)};\n"
        f"export const ALTYAZI: Kelime[][] = {json.dumps(parcalar, ensure_ascii=False)};\n"
        f"export const SHORTS_EK: Record<string, {{sure: number; cumleler: {{metin: string; bas: number; son: number}}[]; agiz: Cue[]}}> = {json.dumps(shorts, ensure_ascii=False)};\n")
    print(json.dumps({"kutu": kutu, "sahne": len(sahneler), "altyazi": len(parcalar), "kapi_x2": (P / "C01-kapilar-x2.jpg").exists()}))


if __name__ == "__main__":
    main()
