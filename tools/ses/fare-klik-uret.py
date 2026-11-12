#!/usr/bin/env python3
"""Kendi üretimimiz fare tıklaması (abone ol animasyonu klik sesi) → assets/efekt/ozgun-fare-klik.flac
Sentez: basma (filtreli gürültü patlaması + 1,9 kHz gövde rezonansı) + 72 ms sonra bırakma (−7 dB, 2,4 kHz). Tohum sabit → deterministik.
Lisans: Toonomy kendi üretimi (assets/LISANSLAR.md). Kullanım: python3 tools/ses/fare-klik-uret.py"""
import os, subprocess
import numpy as np
SR = 48000
rng = np.random.default_rng(1929)
def patlama(f0, kazanc, sure=0.03):
    n = int(sure * SR); t = np.arange(n) / SR
    g = rng.standard_normal(n)
    g = np.convolve(g, [1, -0.97], "same")                     # yüksek geçiren (tık parlaklığı)
    zarf = np.exp(-t / 0.0022)
    govde = np.sin(2 * np.pi * f0 * t) * np.exp(-t / 0.006)
    x = (0.7 * g * zarf + 0.6 * govde) * kazanc
    x[:24] *= np.linspace(0, 1, 24)                             # 0,5 ms atak (çıtırtı olmasın)
    return x
x = np.zeros(int(0.16 * SR))
a = patlama(1900, 1.0); x[:len(a)] += a
b = patlama(2400, 10 ** (-7 / 20)); i = int(0.072 * SR); x[i:i + len(b)] += b
x = x / np.abs(x).max() * 10 ** (-3 / 20)
st = np.stack([x, x * 0.96], 1).astype(np.float32)
cik = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "assets", "efekt", "ozgun-fare-klik.flac")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-", "-c:a", "flac", "-sample_fmt", "s32", os.path.abspath(cik)],
               input=st.tobytes(), check=True)
print("yazıldı:", os.path.abspath(cik))
