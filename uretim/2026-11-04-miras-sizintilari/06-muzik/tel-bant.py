#!/usr/bin/env python3
"""Telefon bandı (300 Hz–4 kHz) enerji payı. Ölçüt ≥0.08 (hafıza 2026-10-27). Kullanım: tel-bant.py dosya..."""
import subprocess, sys, numpy as np
for y in sys.argv[1:]:
    x = np.frombuffer(subprocess.run(["ffmpeg","-v","error","-i",y,"-t","120","-ac","1","-ar","16000","-f","f32le","-"],capture_output=True).stdout, np.float32)
    n = 4096; F = np.abs(np.fft.rfft(x[:len(x)//n*n].reshape(-1, n) * np.hanning(n), axis=1))**2
    f = np.fft.rfftfreq(n, 1/16000); e = F.sum(0)
    print(f"{y.split('/')[-1]}\t{e[(f>=300)&(f<=4000)].sum()/e.sum():.3f}")
