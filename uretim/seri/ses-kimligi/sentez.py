"""Flip By Vote ses kimliği — sentez kütüphanesi (yalnız numpy/scipy, sabit tohum = deterministik).
Kendi üretimimiz: dış örnek yok. uret.py bunu kullanır."""
import numpy as np
from scipy.signal import butter, sosfilt

SR = 48000


def nota(n):
    """'C4', 'F#3', 'Bb2' → Hz"""
    ad = {"C": 0, "D": 2, "E": 4, "F": 5, "G": 7, "A": 9, "B": 11}
    p = ad[n[0]]; i = 1
    while i < len(n) and n[i] in "#b":
        p += 1 if n[i] == "#" else -1; i += 1
    o = int(n[i:])
    return 440.0 * 2 ** ((p + 12 * (o + 1) - 69) / 12)


def filtre(x, tip, f, derece=2):
    if tip == "bp":
        sos = butter(derece, [f[0] / (SR / 2), f[1] / (SR / 2)], btype="band", output="sos")
    else:
        sos = butter(derece, f / (SR / 2), btype=tip, output="sos")
    return sosfilt(sos, x)


def zarf(n, atak, cozul, egri=6.0):
    t = np.arange(n) / SR
    a = np.clip(t / max(atak, 1e-4), 0, 1)
    return a * np.exp(-egri * t / max(cozul, 1e-4))


def ks(f, sure, rng, parlaklik=0.5, sonum=0.996):
    """Karplus-Strong tel (pizz / bas / ukulele)."""
    n = int(sure * SR); p = max(2, int(SR / f))
    buf = rng.uniform(-1, 1, p)
    buf = filtre(np.concatenate([buf, buf]), "low", 1500 + 7000 * parlaklik)[-p:]
    y = np.zeros(n); i = 0
    while i < n:
        k = min(p, n - i)
        y[i:i + k] = buf[:k]
        yeni = sonum * 0.5 * (buf + np.roll(buf, -1))
        buf = yeni
        i += k
    return y / (np.max(np.abs(y)) + 1e-9)


def marimba(f, sure=0.9, parlak=1.0):
    n = int(sure * SR); t = np.arange(n) / SR
    y = (np.sin(2 * np.pi * f * t) * np.exp(-t * 5)
         + 0.35 * parlak * np.sin(2 * np.pi * f * 3.93 * t) * np.exp(-t * 18)
         + 0.12 * parlak * np.sin(2 * np.pi * f * 9.2 * t) * np.exp(-t * 40))
    y *= np.clip(t / 0.002, 0, 1)
    return y


def glock(f, sure=1.2):
    n = int(sure * SR); t = np.arange(n) / SR
    y = (np.sin(2 * np.pi * f * t) * np.exp(-t * 3) + 0.4 * np.sin(2 * np.pi * f * 2.76 * t) * np.exp(-t * 7)
         + 0.2 * np.sin(2 * np.pi * f * 5.4 * t) * np.exp(-t * 14))
    return y * np.clip(t / 0.001, 0, 1)


def kick(sure=0.35, f0=110, f1=45):
    n = int(sure * SR); t = np.arange(n) / SR
    f = f1 + (f0 - f1) * np.exp(-t * 30)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * np.exp(-t * 9)


def gurultu(sure, rng, tip, f, atak=0.001, cozul=0.05, egri=6.0):
    n = int(sure * SR)
    return filtre(rng.standard_normal(n), tip, f) * zarf(n, atak, cozul, egri)


def snap(rng):
    # parmak şıklatma: kısa bant gürültüsü + 2.2 kHz rezonans
    n = int(0.08 * SR); t = np.arange(n) / SR
    g = filtre(rng.standard_normal(n), "bp", (1500, 4500)) * np.exp(-t * 90)
    r = np.sin(2 * np.pi * 2200 * t) * np.exp(-t * 120) * 0.4
    return (g + r) * np.clip(t / 0.0005, 0, 1)


def clap(rng):
    n = int(0.18 * SR); t = np.arange(n) / SR
    e = np.zeros(n)
    for d in (0, 0.009, 0.018):
        e += np.where(t >= d, np.exp(-(t - d) * 160), 0)
    e += 0.5 * np.exp(-t * 25)
    return filtre(rng.standard_normal(n), "bp", (900, 3500)) * e


def shaker(rng, sure=0.07):
    return gurultu(sure, rng, "high", 6500, atak=0.006, cozul=0.03)


def pad(frekanslar, sure, rng, kesim=1100, atak=0.8, birak=1.0, trem=0.0):
    n = int(sure * SR); t = np.arange(n) / SR
    y = np.zeros(n)
    for f in frekanslar:
        for d in (-0.07, 0.0, 0.07):  # hafif detune testere
            ff = f * 2 ** (d / 12)
            faz = rng.uniform(0, 1)
            y += 2 * ((ff * t + faz) % 1.0) - 1
    y = filtre(y, "low", kesim, 2)
    a = np.clip(t / atak, 0, 1) * np.clip((sure - t) / birak, 0, 1)
    if trem:
        a *= 1 - 0.35 * (0.5 + 0.5 * np.sin(2 * np.pi * trem * t))
    return y * a / max(1, len(frekanslar) * 3)


def yerlestir(hedef, x, t, kazanc=1.0, pan=0.0):
    """stereo hedefe (2, N) mono x'i t sn'den ekle; pan −1 sol … +1 sağ (eşit güç)."""
    i = int(round(t * SR))
    if i >= hedef.shape[1]:
        return
    k = min(len(x), hedef.shape[1] - i)
    a = (pan + 1) * np.pi / 4
    hedef[0, i:i + k] += x[:k] * kazanc * np.cos(a)
    hedef[1, i:i + k] += x[:k] * kazanc * np.sin(a)


def dongu_kapat(y, n):
    """n örneklik döngü: n'den taşan kuyruk başa eklenir (dikişsiz döngü)."""
    out = y[:, :n].copy()
    kuyruk = y[:, n:]
    out[:, :kuyruk.shape[1]] += kuyruk[:, :n]
    return out


def tepe_norm(y, db=-1.0):
    return y * (10 ** (db / 20) / (np.max(np.abs(y)) + 1e-12))


def oda(y, rng, karisim=0.12, sure=0.6):
    """kısa oda yankısı (gürültü IR, stereo dekorele)."""
    n = int(sure * SR); t = np.arange(n) / SR
    out = y.copy()
    for k in range(2):
        ir = rng.standard_normal(n) * np.exp(-t * 7.0)
        ir = filtre(ir, "low", 5000)
        ir /= np.sqrt(np.sum(ir ** 2))
        m = y.mean(0)
        L = len(m) + n
        w = np.fft.irfft(np.fft.rfft(m, L) * np.fft.rfft(ir, L), L)[:y.shape[1]]
        out[k] += karisim * w
    return out


def yatak_eq(y, oyuk_db=-12.0, ust_db=-6.0):
    """konuşma oyuğu (sıfır faz, FFT): <700 Hz düz, 1,2–3,8 kHz oyuk_db, >6 kHz ust_db; arası log-yumuşak geçiş."""
    n = y.shape[1]; f = np.fft.rfftfreq(n, 1 / SR); lf = np.log10(np.maximum(f, 1))
    db = np.interp(lf, np.log10([700, 1200, 3800, 6000, 24000]), [0, oyuk_db, oyuk_db, ust_db, ust_db])
    g = 10 ** (db / 20)
    return np.fft.irfft(np.fft.rfft(y, axis=1) * g, n, axis=1)
