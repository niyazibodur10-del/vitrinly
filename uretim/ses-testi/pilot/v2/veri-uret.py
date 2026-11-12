#!/usr/bin/env python3
"""Pilot v2 zamanlama verisi: Rhubarb ağız zamanları + Whisper kelime zamanları -> video/src/pilot/data.ts + SRT.
Kullanım: veri-uret.py <rhubarb.json> <whisper-kelimeler.json> <ofset_sn>
Whisper anlatım stem'i (ofsetsiz) üzerinde çalıştırılır; ofset = miksteki müzik girişi (miks.py --giris).
Rhubarb zaten ofsetli (baş boşluklu) anlatım üzerinde çalıştırılır."""
import json, re, sys
rh, kel, ofset = json.load(open(sys.argv[1])), json.load(open(sys.argv[2]))["words"], float(sys.argv[3])
# Görünen metin (senaryo yazımı; Whisper noktalamayı değiştirebilir) — kelime sayısı Whisper ile 1:1 (WER %0)
gorunen = "Imagine waking up one morning, and your savings are worth less than a cup of coffee. Sounds impossible? In 1923, in Germany, that's exactly what happened.".split()
assert len(gorunen) == len(kel), (len(gorunen), len(kel))
vurgu = {"savings", "coffee.", "impossible?", "1923,", "Germany,", "happened."}
W = [{"t": g, "s": round(w["s"] + ofset, 2), "e": round(w["e"] + ofset, 2), "hl": g in vurgu} for g, w in zip(gorunen, kel)]
# altyazı parçaları (v1 ile aynı gruplama)
boy = [1, 2, 2, 3, 3, 5, 1, 1, 2, 2, 2, 2]
chunks, i = [], 0
for b in boy: chunks.append(W[i:i + b]); i += b
assert i == len(W)
cues = [{"start": c["start"], "end": c["end"], "value": c["value"]} for c in rh["mouthCues"]]
open("video/src/pilot/data.ts", "w").write(
    "// Otomatik üretildi: uretim/ses-testi/pilot/v2/veri-uret.py (Rhubarb ağız zamanları + Whisper kelime zamanları). Elle düzenleme.\n"
    "// Ses: Kokoro am_fenrir 0.9 anlatım + CC0 müzik/efekt miksi (pilot v2). Zamanlar video/public/pilot-ses.wav'a göre.\n"
    "export type Cue = {start: number; end: number; value: string};\n"
    "export type Word = {t: string; s: number; e: number; hl: boolean};\n"
    f"export const mouthCues: Cue[] = {json.dumps(cues)};\n"
    f"export const captionChunks: Word[][] = {json.dumps(chunks)};\n")
# SRT (YouTube altyazısı): satır grupları
satir = [5, 6, 5, 2, 4, 4]
def ts(x): h, r = divmod(x, 3600); m, s = divmod(r, 60); return f"{int(h):02}:{int(m):02}:{int(s):02},{int(round((s % 1) * 1000)):03}"
out, i = [], 0
for n, b in enumerate(satir, 1):
    g = W[i:i + b]; i += b
    out.append(f"{n}\n{ts(g[0]['s'])} --> {ts(g[-1]['e'])}\n{' '.join(w['t'] for w in g)}\n")
assert i == len(W)
open("uretim/ses-testi/pilot/pilot-v2.en.srt", "w").write("\n".join(out))
print("\n".join(out)); print({w["t"]: w["s"] for w in W if w["t"] in ("cup", "Germany,", "1923,", "Sounds")})
