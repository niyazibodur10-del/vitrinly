#!/usr/bin/env python3
"""F5 kritik yol testi — varlık + ses + Rhubarb hazırlığı (animasyon-yonetmeni, 2026-10-27).

05-gorsel/ ve 04-ses/ kaynaklarından video/public/k1929/ (git dışı, yeniden üretilebilir) ve
video/src/k1929/veri.ts (otomatik) üretir.
  - plakalar: C01, C03, C15 → JPEG q92
  - Leo: a (taban, A/X), b (D), C02 duruş, C04 yürüme, C05 kutulu yürüme (kes-m4 ile kesilir) → bbox kırpımlı PNG
  - rig yamaları (B=C07, C/H=C08, E=C09, F=C10, G=C07 geçici) + göz kırpma C06 + tek göz (wink) türevi
  - ses: anlatim.wav'dan test parçaları → tek kritik-ses.wav; her parça için Rhubarb (PocketSphinx, --dialogFile)
Kullanım: ~/.finansal-arac/venv/bin/python -I hazirla.py
"""
import json, subprocess, sys
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent))
from sessizlik_kapisi import sessizlik, uygula  # noqa: E402
from PIL import Image

KOK = Path(__file__).resolve().parents[3]
U = KOK / "uretim/2026-10-26-1929-1000-dolar"
G = U / "05-gorsel"
S = U / "04-ses"
A = U / "07-animasyon"
P = KOK / "video/public/k1929"
PY = Path.home() / ".finansal-arac/venv/bin/python"
RHUBARB = Path.home() / ".finansal-arac/rhubarb/build/rhubarb/rhubarb"
P.mkdir(parents=True, exist_ok=True)
(A / "rhubarb").mkdir(exist_ok=True)

# Test parçaları (anlatim.wav zamanları, sn). S01 hook başı + S04 klon yürüyüşü ve "Remember that laugh".
PARCALAR = [
    {"id": "s01", "bas": 0.00, "son": 8.00},
    {"id": "s04", "bas": 62.00, "son": 73.70},
]

# Rhubarb şekli → yama (rig-yamalar.json adları); A/X = taban a, D = paket-v1 b (tam görsel değişimi)
AGIZ = {"B": "agiz-B-C07", "C": "agiz-C-C08", "H": "agiz-C-C08", "E": "agiz-E-C09", "F": "agiz-F-C10", "G": "agiz-B-C07"}

# Altyazı anahtar kelime renkleri (kapı renkleri + sayı sarısı)
RENK = {"blue": "#4da3ff", "stock": "#4da3ff", "green": "#5fd35f", "bank": "#5fd35f",
        "brown": "#e0884a", "shoebox": "#e0884a", "shoebox.": "#e0884a", "box": "#e0884a"}
SARI = "#ffd43b"
SARI_KELIME = {"laugh", "doors", "disaster", "gamble", "surprise", "player", "september"}


def kirp(src, dst, pad=6):
    im = Image.open(src).convert("RGBA")
    a = np.array(im)[:, :, 3]
    ys, xs = np.where(a > 8)
    x0, y0 = max(0, xs.min() - pad), max(0, ys.min() - pad)
    x1, y1 = min(im.width, xs.max() + pad + 1), min(im.height, ys.max() + pad + 1)
    im.crop((x0, y0, x1, y1)).save(dst, optimize=True)
    return {"x": int(x0), "y": int(y0), "w": int(x1 - x0), "h": int(y1 - y0)}


def main():
    v = {"leo": {}, "yama": {}}
    for c in ["C01", "C03"]:
        Image.open(G / f"canva-ham/{c}.png").convert("RGB").save(P / f"{c}.jpg", quality=92)
    Image.open(G / "plaka/C15-sepya.png").convert("RGB").save(P / "C15.jpg", quality=92)  # dalga 3: sepya eşlenmiş

    # Sunucu rig: bel üstü pozlar (a, b, c, C12) aynı kadrajda → ortak kırpım kutusu (birleşik bbox), yamalar aynı konumda
    SUNUCU_POZ = [("a", "a-konusma-kapali"), ("b", "b-konusma-acik"), ("C12", "C12-sunum")]
    bx = []
    for _, f in SUNUCU_POZ:
        al = np.array(Image.open(G / f"leo/{f}.png"))[:, :, 3]; ys, xs = np.where(al > 8)
        bx.append((xs.min(), ys.min(), xs.max(), ys.max()))
    bx = np.array(bx)
    kutu = (max(0, int(bx[:, 0].min()) - 6), max(0, int(bx[:, 1].min()) - 6), min(1920, int(bx[:, 2].max()) + 7), min(1080, int(bx[:, 3].max()) + 7))
    for ad, f in SUNUCU_POZ:
        Image.open(G / f"leo/{f}.png").crop(kutu).save(P / f"leo-{ad}.png", optimize=True)
    v["sunucu"] = {"x": kutu[0], "y": kutu[1], "w": kutu[2] - kutu[0], "h": kutu[3] - kutu[1]}

    rig = json.load(open(G / "rig/rig-yamalar.json"))["yamalar"]
    # Yamaların alfası taban a'nın siluetiyle çarpılır: yama kutusu çene/kulak kenarında Canva zemininin (slate-blue)
    # piksellerini taşıyordu → AgizTest'te yüz kenarında mavi hale (2026-10-27 ölçüm/kare). Silüet dışı = 0.
    a_al = np.array(im_a_tam := Image.open(G / "leo/a-konusma-kapali.png"))[:, :, 3].astype(np.float32) / 255
    for ad, r in rig.items():
        x, y = r["konum_xy"]; w, h = r["boyut_wh"]
        ya = np.array(Image.open(G / f"rig/{ad}.png").convert("RGBA")).astype(np.float32)
        ya[:, :, 3] *= a_al[y:y + h, x:x + w]
        Image.fromarray(ya.astype(np.uint8)).save(P / f"{ad}.png")
        v["yama"][ad] = {"x": r["konum_xy"][0] - kutu[0], "y": r["konum_xy"][1] - kutu[1],
                         "w": r["boyut_wh"][0], "h": r["boyut_wh"][1]}
    # Tek göz kırpma (wink): C06 yamasının izleyiciye göre sol yarısı; kesim yüz ortasında yumuşak rampa
    g = Image.open(P / "goz-kapali-C06.png").convert("RGBA"); ga = np.array(g).astype(np.float32)
    al6 = ga[:, :, 3]; cols = np.where(al6.max(0) > 40)[0]
    orta = int(cols.min() + (cols.max() - cols.min()) * 0.5)
    ramp = np.clip((orta + 6 - np.arange(g.width)) / 12.0, 0, 1)
    ga[:, :, 3] *= ramp[None, :]
    Image.fromarray(ga.astype(np.uint8)).save(P / "goz-tek-C06.png")
    v["yama"]["goz-tek-C06"] = dict(v["yama"]["goz-kapali-C06"])
    v["wink_orta_x"] = orta

    # Klon pozları: gorsel-varlik-sanatcisi kesikleri (C05 ten eşlemeli). Kadrajın SOLUNA yürür; aynalama yasak.
    for c, f in [("C02", "C02-tam-boy"), ("C04", "C04-yurume"), ("C05", "C05-kutuyla-yurume")]:
        v["leo"][c] = kirp(G / f"leo/{f}.png", P / f"leo-{c}.png")

    # Ses + Rhubarb
    kel = json.load(open(S / "kelimeler.json"))["words"]
    parcalar = []; liste = []
    for p in PARCALAR:
        w = P / f"ses-{p['id']}.wav"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(S / "anlatim.wav"), "-ss", str(p["bas"]), "-to", str(p["son"]),
                        "-ac", "1", "-ar", "48000", str(w)], check=True)
        liste.append(f"file '{w}'")
        kk = [x for x in kel if p["bas"] <= x["s"] < p["son"]]
        metin = " ".join(x["w"] for x in kk).replace(" ,", ",").replace("$1 ,000", "one thousand dollars").replace("$1,000", "one thousand dollars")
        metin = metin.replace("1929", "nineteen twenty-nine").replace("Door 1", "Door one")
        dlg = A / f"rhubarb/{p['id']}-diyalog.txt"; dlg.write_text(metin + "\n")
        rj = A / f"rhubarb/{p['id']}.json"
        subprocess.run([str(RHUBARB), "-r", "pocketSphinx", "-f", "json", "--dialogFile", str(dlg), "-o", str(rj), str(w)],
                       check=True, capture_output=True)
        ham = json.load(open(rj))["mouthCues"]
        # Sessizlik kapısı: ≥100 ms sessiz aralıklarda ağız X (Rhubarb cümle sonlarında şekli 5–8 kare tutuyordu)
        cues = uygula(ham, sessizlik(str(w)))
        json.dump({"mouthCues": cues}, open(A / f"rhubarb/{p['id']}-kapili.json", "w"))
        kelimeler = []
        for x in kk:
            t = x["w"]; k = t.lower().strip(".,?!")
            renk = RENK.get(k) or (SARI if (k in SARI_KELIME or any(ch.isdigit() for ch in k)) else None)
            kelimeler.append({"t": t, "s": round(x["s"] - p["bas"], 3), "e": round(x["e"] - p["bas"], 3), "renk": renk})
        parcalar.append({"id": p["id"], "kaynakBas": p["bas"], "sure": round(p["son"] - p["bas"], 3), "agiz": cues, "kelimeler": kelimeler})
    # "$1" + ",000" Whisper bölünmesi → tek kelime
    for p in parcalar:
        ks = p["kelimeler"]
        for i in range(len(ks) - 1):
            if ks[i] and ks[i + 1] and ks[i]["t"] == "$1" and ks[i + 1]["t"].startswith(",000"):
                ks[i] = {"t": "$1" + ks[i + 1]["t"], "s": ks[i]["s"], "e": ks[i + 1]["e"], "renk": SARI}; ks[i + 1] = None
        p["kelimeler"] = [k for k in ks if k]
    lf = P / "liste.txt"; lf.write_text("\n".join(liste) + "\n")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lf), "-c", "copy", str(P / "kritik-ses.wav")], check=True)
    lf.unlink()
    # Senkron testi için birleşik Rhubarb çizelgesi (kritik-ses.wav zamanında)
    birlesik = []; ofs = 0.0
    for p in parcalar:
        for c in p["agiz"]:
            birlesik.append({"start": round(c["start"] + ofs, 3), "end": round(c["end"] + ofs, 3), "value": c["value"]})
        ofs += p["sure"]
    json.dump({"mouthCues": birlesik}, open(A / "rhubarb/kritik-birlesik.json", "w"))

    ts = KOK / "video/src/k1929/veri.ts"; ts.parent.mkdir(exist_ok=True)
    ts.write_text(
        "// Otomatik üretildi: uretim/2026-10-26-1929-1000-dolar/07-animasyon/hazirla.py — elle düzenleme.\n"
        "export type Cue = {start: number; end: number; value: string};\n"
        "export type Kelime = {t: string; s: number; e: number; renk: string | null};\n"
        "export type Kutu = {x: number; y: number; w: number; h: number};\n"
        "export type Parca = {id: string; kaynakBas: number; sure: number; agiz: Cue[]; kelimeler: Kelime[]};\n"
        f"export const AGIZ_YAMA: Record<string, string> = {json.dumps(AGIZ)};\n"
        f"export const SUNUCU: Kutu = {json.dumps(v['sunucu'])};\n"
        f"export const YAMA: Record<string, Kutu> = {json.dumps(v['yama'])};\n"
        f"export const POZ: Record<string, Kutu> = {json.dumps(v['leo'])};\n"
        f"export const PARCALAR: Parca[] = {json.dumps(parcalar, ensure_ascii=False)};\n")
    print(json.dumps({"sunucu": v["sunucu"], "poz": v["leo"], "parca": [(p["id"], p["sure"], len(p["agiz"]), len(p["kelimeler"])) for p in parcalar]}))


if __name__ == "__main__":
    main()
