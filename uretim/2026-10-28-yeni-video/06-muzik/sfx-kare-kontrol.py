#!/usr/bin/env python3
"""Kapı: her sesli olayın ilk vuruşu animasyon-efekt-cue.json'daki görsel olaya ±2 kare mi?
 (1) cue.json zamanı vs olay zamanı (kare farkı)  (2) sfx-stem.wav'da gerçek yer: vuruşun kendi dosyasının ilk 0.3 sn'si stem'le çapraz ilintilenir (±0.08 sn ≈ ±2.4 kare; dışarıdaki gerçek kayma pencere kenarında >2 kare okunur. Tekrarlı vuruş ve iç tekrarlı dosyada yanlış tepe seçilmesin diye dar),
 bulunan yer + dosya içi vuruş noktası (whoosh tepesi / ses başlangıcı) vs olay zamanı. Çıkış 0 = GEÇTİ."""
import json, subprocess, sys, numpy as np
B = __import__("os").path.dirname(__import__("os").path.abspath(__file__))
c = json.load(open(f"{B}/cue.json")); fps = c["fps"]; SR = 48000
REPO = __import__("os").path.abspath(f"{B}/../../..")
YOL = {"$E/": f"{B}/kaynak/efekt/", "$O/": f"{B}/kaynak/ozgun/", "$AE/": f"{REPO}/assets/efekt/"}
x = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", f"{B}/stems/sfx-stem.wav", "-ac", "1", "-f", "f32le", "-"],
                                 capture_output=True).stdout, np.float32)
ilk = {}
for s in c["sfx"]:
    ilk.setdefault(s["t_olay"], s)
k1, k2, kotu = [], [], []
for to, s in sorted(ilk.items()):
    d1 = abs(s["t"] - s.get("kirp", 0) + s["vurus_ofset"] - to) * fps          # cue: vuruş noktası = olay
    # stem'de gerçek yer: vuruşun kendi dosyasıyla çapraz ilinti (üst üste binen SFX'lerden etkilenmez), ±0.08 sn
    yol = next(s["dosya"].replace(p, q) for p, q in YOL.items() if s["dosya"].startswith(p))
    of = s["vurus_ofset"] - s.get("kirp", 0)                 # vuruş noktasının stem'deki dosya başına göre yeri
    f = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", yol, "-ac", "1", "-ar", "48000", "-f", "f32le", "-"],
                                     capture_output=True).stdout, np.float32)[int(round(s["vurus_ofset"] * SR)):][:int(0.3 * SR)]
    beklenen = int(round((s["t"] + of) * SR)); a = max(beklenen - int(0.08 * SR), 0)   # şablon = vuruş noktasından sonraki 0.3 sn
    seg = x[a:beklenen + int(0.08 * SR) + len(f)]
    n = len(seg) + len(f); r = np.fft.irfft(np.fft.rfft(seg, n) * np.conj(np.fft.rfft(f, n)), n)[:len(seg) - len(f) + 1]
    on = int(np.argmax(np.abs(r)))
    d2 = abs((max(a, 0) + on) / SR - to) * fps
    k1.append(d1); k2.append(d2)
    if d1 > 2 or d2 > 2:
        kotu.append((round(to, 3), s["dosya"].split("/")[-1], round(d1, 2), round(d2, 2)))
print(f"olay {len(ilk)} · cue farkı max {max(k1):.2f} kare · stem başlangıç farkı medyan {np.median(k2):.2f}, max {max(k2):.2f} kare · ±2 kare dışı: {len(kotu)} {kotu[:10]}")
sys.exit(1 if kotu else 0)
