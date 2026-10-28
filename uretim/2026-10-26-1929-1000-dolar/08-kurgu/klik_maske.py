#!/usr/bin/env python3
"""Kapı: abone klik sesi anlatımı maskeliyor mu? Her klik için 400 ms pencerede (klik −100 ms … +300 ms)
K-ağırlıksız kaba ölçüm: miks (kliksiz) ile miks (klikli) RMS farkı (dB) + klik / anlatım tepe oranı.
Eşik: RMS artışı ≤ 1,0 dB ve (klik tepesi anlatım tepesinin ≥ 6 dB altında VEYA pencerede konuşma yok: anlatım tepesi < −20 dBFS) → GEÇTİ.
Konuşmasız pencerede (cümle arası) klik maskeleyecek söz yoktur; Shorts gibi anlatım ayrı stem olmayan dosyada 3. argüman eski miks olur.
Kullanım: python3 klik_maske.py <eski_miks.wav> <yeni_miks.wav> <anlatim.wav> t1 t2 ..."""
import subprocess, sys
import numpy as np
SR = 48000
def c(p): return np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", p, "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True, check=True).stdout, np.float32).reshape(-1, 2)
a, b, n = c(sys.argv[1]), c(sys.argv[2]), c(sys.argv[3])
kalan = 0
for t in map(float, sys.argv[4:]):
    i, j = int((t - 0.1) * SR), int((t + 0.3) * SR)
    rms = lambda x: 20 * np.log10(np.sqrt((x ** 2).mean()) + 1e-12)
    d = rms(b[i:j]) - rms(a[i:j])
    klik = 20 * np.log10(np.abs(b[i:j] - a[i:j]).max() + 1e-12); anl = 20 * np.log10(np.abs(n[i:j]).max() + 1e-12)
    sessiz = anl < -20
    ok = d <= 1.0 and (klik <= anl - 6 or sessiz)
    kalan += not ok
    print(f"t={t:7.2f}  RMS artışı {d:+.2f} dB · klik tepe {klik:.1f} dBFS · anlatım tepe {anl:.1f} dBFS{' (konuşma yok)' if sessiz else ''} · {'GEÇTİ' if ok else 'KALDI'}")
sys.exit(1 if kalan else 0)
