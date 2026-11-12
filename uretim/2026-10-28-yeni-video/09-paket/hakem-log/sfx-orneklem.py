#!/usr/bin/env python3
"""Hakem SFX hizası örneklemi: 5 rastgele vuruş (tohum 20261102).
Ses: vuruş dosyası (vuruş noktasından sonraki 0,3 sn) sfx-stem ile ±0,5 sn çapraz ilinti → stem'deki vuruş anı (ajanın ±0,08 penceresinden geniş).
Görsel: final videoda olay ±0,4 sn, 30 fps kare farkı; olay başı = farkın ilk kez tepe değerin %40'ını aştığı kare. Kapı |vuruş − görsel| ≤ 2 kare.
Ayrıca kontakt: olay −3…+3 kare (hakem-log/sfx-kontakt-<t>.jpg)."""
import json, random, subprocess, os, numpy as np
SR = 48000; V = "08-kurgu/final-16x9.mp4"; S = "06-muzik/stems/sfx-stem.wav"
R = os.path.abspath("../.."); YOL = {"$E/": "06-muzik/kaynak/efekt/", "$O/": "06-muzik/kaynak/ozgun/", "$AE/": f"{R}/assets/efekt/"}
def oku(p, ss=None, t=None):
    return np.frombuffer(subprocess.run(["ffmpeg","-nostdin","-v","error"]+(["-ss",f"{ss}"] if ss is not None else [])+["-i",p]+(["-t",f"{t}"] if t else [])+["-ac","1","-ar",str(SR),"-f","f32le","-"],capture_output=True).stdout, np.float32)
cue = json.load(open("06-muzik/cue.json"))["sfx"]
aday = [c for c in cue if 1 < c["t_olay"] < 670]
random.seed(20261102); sec = sorted(random.sample(aday, 5), key=lambda c: c["t_olay"])
kal = 0
for c in sec:
    to = c["t_olay"]
    yol = next(c["dosya"].replace(p, q) for p, q in YOL.items() if c["dosya"].startswith(p))
    f = oku(yol)[int(round(c["vurus_ofset"] * SR)):][:int(0.3 * SR)]
    b = to - 0.5; seg = oku(S, b, 1.0 + 0.3)
    n = len(seg) + len(f); r = np.fft.irfft(np.fft.rfft(seg, n) * np.conj(np.fft.rfft(f, n)), n)[:len(seg) - len(f) + 1]
    ta = b + int(np.argmax(np.abs(r))) / SR
    vb = to - 0.4
    raw = subprocess.run(["ffmpeg","-nostdin","-v","error","-ss",f"{vb}","-i",V,"-t","0.8","-vf","fps=30,scale=480:270","-f","rawvideo","-pix_fmt","gray","-"],capture_output=True).stdout
    k = np.frombuffer(raw, np.uint8).reshape(-1, 270, 480).astype(int)
    d = np.abs(np.diff(k, axis=0)).mean((1, 2)); i = int(np.argmax(d > 0.4 * d.max()))
    tv = vb + (i + 1) / 30
    fk = (ta - tv) * 30; ok = abs(fk) <= 2; kal += not ok
    subprocess.run(["ffmpeg","-nostdin","-v","error","-ss",f"{to-0.1}","-i",V,"-vf","fps=30,scale=320:-1,tile=7x1","-frames:v","1","-y",f"09-paket/hakem-log/sfx-kontakt-{to:.3f}.jpg"])
    print(f"t_olay {to:7.3f} | {c['olay'][:50]:50s} | {c['dosya'].split('/')[-1][:20]:20s} | stem vuruşu {ta:7.3f} ({(ta-to)*30:+.1f}) · görsel başı {tv:7.3f} ({(tv-to)*30:+.1f}) · fark {fk:+.1f} kare {'OK' if ok else 'KALDI'}")
print(f"SONUÇ: {5-kal}/5 ±2 kare")
