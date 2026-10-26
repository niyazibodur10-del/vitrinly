#!/usr/bin/env python3
"""Kendi üretimimiz geçiş efektleri (lisans/Content ID riski yok).

Kullanım: efekt-uret.py <cikis-dizini>
Üretir (48 kHz stereo FLAC, tepe -3 dBFS):
  whoosh-kisa.flac  (0.45 sn, hızlı kesme)   whoosh-uzun.flac (0.9 sn, sahne geçişi)
  riser.flac        (1.6 sn, gerilim yükselişi; "büyük sayı" öncesi)
Yöntem: pembe gürültü -> zamanla kayan rezonanslı bant geçiren (durum değişkenli filtre) ->
asimetrik zarf -> soldan sağa pan. Tekrarlanabilir (sabit tohum).
"""
import subprocess, sys
import numpy as np

SR = 48000


def pembe(n, rng):
    # Voss-McCartney yerine FFT ile 1/f şekillendirme
    w = rng.standard_normal(n)
    W = np.fft.rfft(w); f = np.fft.rfftfreq(n, 1 / SR); f[0] = f[1]
    return np.fft.irfft(W / np.sqrt(f), n)


def svf_bant(x, fc, q):
    """Zamanla değişen merkez frekanslı durum değişkenli bant geçiren filtre."""
    y = np.zeros_like(x); lp = bp = 0.0
    for i in range(len(x)):
        g = 2 * np.sin(np.pi * fc[i] / SR)
        hp = x[i] - lp - bp / q
        bp += g * hp; lp += g * bp
        y[i] = bp
    return y


def whoosh(sure, f_bas, f_tepe, f_son, tepe_oran, q, tohum):
    rng = np.random.default_rng(tohum)
    n = int(sure * SR); t = np.linspace(0, 1, n)
    x = pembe(n, rng)
    # frekans: tepeye logaritmik çık, sonra in
    fc = np.where(t < tepe_oran,
                  f_bas * (f_tepe / f_bas) ** (t / tepe_oran),
                  f_tepe * (f_son / f_tepe) ** ((t - tepe_oran) / (1 - tepe_oran)))
    y = svf_bant(x, fc, q) + 0.15 * svf_bant(x, fc * 2.2, q)
    zarf = np.where(t < tepe_oran, (t / tepe_oran) ** 2, np.exp(-5 * (t - tepe_oran) / (1 - tepe_oran)))
    y *= zarf
    pan = np.clip(t * 1.2 - 0.1, 0, 1)  # soldan sağa
    st = np.stack([y * np.cos(pan * np.pi / 2), y * np.sin(pan * np.pi / 2)], 1)
    return st / np.abs(st).max() * 10 ** (-3 / 20)


def riser(sure, tohum):
    rng = np.random.default_rng(tohum)
    n = int(sure * SR); t = np.linspace(0, 1, n)
    fc = 200 * (6000 / 200) ** (t ** 1.5)
    y = svf_bant(pembe(n, rng), fc, 4.0)
    # alttan yükselen ton (perde 55 -> 110 Hz), gerilim için
    faz = 2 * np.pi * np.cumsum(55 * 2 ** t) / SR
    y = y / np.abs(y).max() + 0.25 * np.sin(faz) * t
    y *= t ** 2.2 * (1 - np.exp(-(1 - t) * 60))  # sonda keskin kesilme
    st = np.stack([y, y], 1)
    return st / np.abs(st).max() * 10 ** (-3 / 20)


def yaz(yol, st):
    p = subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-",
                        "-c:a", "flac", "-sample_fmt", "s16", yol], input=st.astype(np.float32).tobytes())
    assert p.returncode == 0


if __name__ == "__main__":
    d = sys.argv[1]
    yaz(f"{d}/whoosh-kisa.flac", whoosh(0.45, 400, 2500, 700, 0.45, 2.5, 1))
    yaz(f"{d}/whoosh-uzun.flac", whoosh(0.9, 250, 1800, 400, 0.5, 2.0, 2))
    yaz(f"{d}/riser.flac", riser(1.6, 3))
    print("tamam")
