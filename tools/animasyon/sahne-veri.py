#!/usr/bin/env python3
"""Sahne verisi → Remotion TS modülü (sahne sınırları, sahne başına kelimeler + ağız çizelgesi, renkli altyazı, ek kayıtlar).

Kullanım:
  python3 -I tools/animasyon/sahne-veri.py --ses-dizin uretim/<video>/04-ses --rhubarb uretim/<video>/07-animasyon/rhubarb \
      --cikis video/src/<kisa>/veri-sahne.ts [--renk renkler.json] [--ek sh1:shorts-1-ek] [--ek sh2:shorts-2-ek]
  Girdi (ses-dizin içinde): sahne-zamanlari.json, kelimeler-hizali.json (words[].sahne), altyazi-parcalar.json
    (öbekler; kelimede "hl" = vurgu); ek kayıt için <ad>-ham.zaman.json + <ad>.wav. Rhubarb: <rhubarb>/sahne/<id>-kapili.json
    (tools/animasyon/rhubarb-toplu.py çıktısı).
  --renk: {"vurgu": "#ffd43b", "kelime": {"stock": "#4da3ff", ...}} — altyazıda anahtar kelime renkleri.
  Çıktı: export SAHNELER, ALTYAZI, SHORTS_EK (+ tipler). Görsel varlık hazırlığı (poz kırpımı, plakalar) videoya özeldir,
  bu araçta yok (uretim/<video>/07-animasyon/varlik-hazirla.py).
Genelleştirildi 2026-10-28 (uretim-muhendisi): kaynak uretim/2026-10-26-1929-1000-dolar/07-animasyon/hazirla-tam.py
(veri kısmı). Test: 1929 girdisiyle SAHNELER/ALTYAZI/SHORTS_EK JSON'u video/src/k1929/veri-tam.ts ile birebir aynı.
"""
import argparse, json, re, subprocess
from pathlib import Path


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--ses-dizin", required=True); ap.add_argument("--rhubarb", required=True); ap.add_argument("--cikis", required=True)
    ap.add_argument("--renk"); ap.add_argument("--ek", action="append", default=[], help="anahtar:dosya_kökü (ör. sh1:shorts-1-ek)")
    a = ap.parse_args()
    S, R = Path(a.ses_dizin), Path(a.rhubarb) / "sahne"
    renk = json.load(open(a.renk)) if a.renk else {"vurgu": "#ffd43b", "kelime": {}}
    sah = json.load(open(S / "sahne-zamanlari.json"))["sahneler"]
    kel = json.load(open(S / "kelimeler-hizali.json"))["words"]
    sahneler = []
    for s in sah:
        ad, b = s["sahne"], s["bas"]
        cues = json.load(open(R / f"{ad}-kapili.json"))["mouthCues"]
        ks = [{"w": w["w"], "s": round(w["s"] - b, 3), "e": round(w["e"] - b, 3)} for w in kel if w["sahne"] == ad]
        sahneler.append({"id": ad, "bas": b, "bitis": s["bitis"], "sure": round(s["bitis"] - b, 3), "kelimeler": ks,
                         "agiz": [{"start": c["start"], "end": c["end"], "value": c["value"]} for c in cues]})
    parcalar = []
    for p in json.load(open(S / "altyazi-parcalar.json")):
        parcalar.append([{"t": w["t"], "s": w["s"], "e": w["e"],
                          "renk": renk["kelime"].get(re.sub(r"[^a-z']", "", w["t"].lower())) or (renk["vurgu"] if w.get("hl") else None)}
                         for w in p])
    ekler = {}
    for e in a.ek:
        anahtar, kok = e.split(":")
        z = json.load(open(S / f"{kok}-ham.zaman.json"))["cumleler"]
        cues = json.load(open(R / f"{kok}-kapili.json"))["mouthCues"]
        sure = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(S / f"{kok}.wav")],
                                    capture_output=True, text=True, check=True).stdout)
        ekler[anahtar] = {"sure": round(sure, 3), "cumleler": z, "agiz": cues}
    Path(a.cikis).write_text(
        "// Otomatik üretildi: tools/animasyon/sahne-veri.py — elle düzenleme.\n"
        "export type Cue = {start: number; end: number; value: string};\n"
        "export type Kelime = {t: string; s: number; e: number; renk: string | null};\n"
        "export type SahneVeri = {id: string; bas: number; bitis: number; sure: number; kelimeler: {w: string; s: number; e: number}[]; agiz: Cue[]};\n"
        f"export const SAHNELER: SahneVeri[] = {json.dumps(sahneler, ensure_ascii=False)};\n"
        f"export const ALTYAZI: Kelime[][] = {json.dumps(parcalar, ensure_ascii=False)};\n"
        f"export const SHORTS_EK: Record<string, {{sure: number; cumleler: {{metin: string; bas: number; son: number}}[]; agiz: Cue[]}}> = {json.dumps(ekler, ensure_ascii=False)};\n")
    print(json.dumps({"sahne": len(sahneler), "altyazi": len(parcalar), "ek": list(ekler)}))


if __name__ == "__main__":
    main()
