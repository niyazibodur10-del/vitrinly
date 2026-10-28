#!/usr/bin/env python3
"""Akustik hiza doğrulaması (ses-muhendisi): anlatim.wav'da her cümlenin gerçek ses başlangıcı/bitişi (sessizlikten sonra
10 ms RMS'in ilk/son kez -45 dBFS'i geçtiği an; TTS cümle arası dijital sessizlik) vs kelimeler-hizali.json ve ham kelimeler.json.
Kapı (docs/kalite-kapilari.md altyazı ±150 ms): hizalı ilk kelime başı ve son kelime sonu |fark| p95 <= 150 ms.
Kullanım: ~/.finansal-arac/venv/bin/python hiza-dogrula.py"""
import json, numpy as np, soundfile as sf
y, sr = sf.read("anlatim.wav"); h = int(0.01 * sr)
rms = 20 * np.log10(np.sqrt(np.convolve(y ** 2, np.ones(h) / h, "same")) + 1e-12)
C = json.load(open("anlatim-ham.zaman.json"))["cumleler"]; O = json.load(open("kelimeler-hizali.json"))["words"]
W = json.load(open("kelimeler.json"))["words"]
def akustik(c):
    a, b = int(max(0, c["bas"] - 0.2) * sr), int((c["son"] + 0.2) * sr); idx = np.where(rms[a:b] > -45)[0]
    return (a + idx[0]) / sr, (a + idx[-1]) / sr
fb, fs, wb = [], [], []
for ci, c in enumerate(C):
    s0, e0 = akustik(c); ws = [o for o in O if o["cumle"] == ci]
    fb.append(abs(ws[0]["s"] - s0)); fs.append(abs(ws[-1]["e"] - e0))
    ilk = min(W, key=lambda w: abs(w["s"] - s0)); wb.append(abs(ilk["s"] - s0))
p = lambda v, q: round(sorted(v)[min(len(v) - 1, int(q * len(v)))] * 1000)
print(f"cümle={len(C)} | hizalı baş fark p50={p(fb,.5)} p95={p(fb,.95)} maks={p(fb,1)} ms | hizalı son fark p50={p(fs,.5)} p95={p(fs,.95)} maks={p(fs,1)} ms")
print(f"karşılaştırma ham Whisper en yakın kelime başı: p50={p(wb,.5)} p95={p(wb,.95)} maks={p(wb,1)} ms")
print("KAPI", "GEÇTİ" if p(fb, .95) <= 150 and p(fs, .95) <= 150 else "KALDI")
