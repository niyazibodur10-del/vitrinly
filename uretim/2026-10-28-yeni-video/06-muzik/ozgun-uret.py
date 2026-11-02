#!/usr/bin/env python3
"""S08 mutfak masası kendi efektlerimiz (numpy sentez, sabit tohum 5400). Çıkış kaynak/ozgun/*.flac, 48 kHz, tepe −3 dBFS.
  ozgun-hesap-tus      : hesap makinesi plastik tuş (kısa tık + gövde rezonansı 1.1 kHz)
  ozgun-hesap-tus-dizi : 5 tuşluk dizi (rakam girişi, 0.11 sn arayla, hafif rastgele)
  ozgun-yapiskan-not   : yapışkan notun buzdolabına yapışması (bant geçiren gürültü + 180 Hz gövde)
  ozgun-zarf-kule      : zarf kulesinin büyümesi için kısa yükselen "tık-tık-tık" (3 kâğıt tıkı, artan perde)"""
import subprocess, os, numpy as np
SR = 48000; rng = np.random.default_rng(5400); d = os.path.dirname(os.path.abspath(__file__))
def t(s): return np.arange(int(SR * s)) / SR
def bp(x, lo, hi):
    X = np.fft.rfft(x); f = np.fft.rfftfreq(len(x), 1 / SR); X[(f < lo) | (f > hi)] = 0; return np.fft.irfft(X, len(x))
def tus(perde=1100):
    a = t(0.09); klik = bp(rng.standard_normal(len(a)), 2000, 7000) * np.exp(-a * 400)
    govde = np.sin(2 * np.pi * perde * a) * np.exp(-a * 70) * 0.5 + np.sin(2 * np.pi * perde * 2.7 * a) * np.exp(-a * 120) * 0.2
    return klik * 0.6 + govde
def yaz(ad, x):
    x = np.concatenate([np.zeros(int(SR * 0.005)), x, np.zeros(int(SR * 0.05))]); x = x / np.abs(x).max() * 10 ** (-3 / 20)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-", "-c:a", "flac", f"{d}/kaynak/ozgun/{ad}.flac"], input=x.astype(np.float32).tobytes(), check=True)
yaz("ozgun-hesap-tus", tus())
dizi = np.zeros(int(SR * 0.7))
for i in range(5):
    k = tus(1100 * (1 + rng.uniform(-0.04, 0.04))); s = int(SR * (i * 0.11 + rng.uniform(0, 0.015))); dizi[s:s + len(k)] += k * rng.uniform(0.8, 1)
yaz("ozgun-hesap-tus-dizi", dizi)
a = t(0.25); yaz("ozgun-yapiskan-not", bp(rng.standard_normal(len(a)), 700, 3500) * np.exp(-a * 60) + np.sin(2 * np.pi * 180 * a) * np.exp(-a * 45) * 0.7)
kule = np.zeros(int(SR * 0.6))
for i, p in enumerate([1.0, 1.19, 1.41]):
    b = t(0.12); k = bp(rng.standard_normal(len(b)), 1200 * p, 4000 * p) * np.exp(-b * 80) + np.sin(2 * np.pi * 420 * p * b) * np.exp(-b * 50) * 0.5
    s = int(SR * i * 0.16); kule[s:s + len(k)] += k
yaz("ozgun-zarf-kule", kule)
