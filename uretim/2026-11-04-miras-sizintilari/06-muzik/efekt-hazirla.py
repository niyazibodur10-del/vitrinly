#!/usr/bin/env python3
"""CC0 SFX -> 48 kHz FLAC, tepe -3 dBFS (numpy f32; OGA ogg >0 dBFS olabilir, hafıza 2026-11-02).
Kullanım: efekt-hazirla.py <girdi> <cikti.flac> [bas_sn] [sure_sn]"""
import subprocess, sys, numpy as np
g, c = sys.argv[1], sys.argv[2]
kom = ["ffmpeg", "-v", "error"]
if len(sys.argv) > 3: kom += ["-ss", sys.argv[3]]
kom += ["-i", g]
if len(sys.argv) > 4: kom += ["-t", sys.argv[4]]
x = np.frombuffer(subprocess.run(kom + ["-ac", "2", "-ar", "48000", "-f", "f32le", "-"], capture_output=True, check=True).stdout, np.float32).copy()
x *= 10 ** (-3 / 20) / max(np.abs(x).max(), 1e-9)
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", "48000", "-ac", "2", "-i", "-", "-c:a", "flac", "-sample_fmt", "s16", c], input=x.tobytes(), check=True)
print(c, f"{len(x)/2/48000:.2f} sn")
