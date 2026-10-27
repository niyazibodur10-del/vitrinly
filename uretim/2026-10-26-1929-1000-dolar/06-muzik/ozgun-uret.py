#!/usr/bin/env python3
"""1929-1000-dolar: kendi üretimimiz SFX ve gerilim yatakları (lisans ve Content ID riski yok).

Kullanım: python3 ozgun-uret.py <cikis-dizini>
Çıktı: 48 kHz stereo FLAC, tepe -3 dBFS. Sabit tohum, aynı komut aynı dosyayı üretir.
Yöntem: yalnız numpy sentezi (toplamsal sinüs, FFT ile şekillendirilmiş gürültü, zarflar).
Yataklar tam ölçü sayısında ve dairesel (FFT) filtreli olduğu için kesintisiz döner.

SFX:  ding-oyunsovu, ding-ding-dogru, buzzer-yanlis, saat-tik, saat-tok, sayac-tikirti,
      kasa-kilit, gerilim-vurus, ruzgar-dusus, radyo-cizirti, ka-ching, kapi-isik-acilis
Yatak: yatak-nabiz-90bpm (gerilim), yatak-dip-drone (1932 dip), yatak-kilit-saat-100bpm (1933 kilit)
"""
import subprocess, sys
import numpy as np

SR = 48000
RNG = np.random.default_rng(1929)


def t_(sure):
    return np.arange(int(sure * SR)) / SR


def norm(x, db=-3.0):
    return x / (np.abs(x).max() + 1e-12) * 10 ** (db / 20)


def stereo(x, pan=0.0):
    a = (pan + 1) * np.pi / 4
    return np.stack([x * np.cos(a), x * np.sin(a)], 1) * np.sqrt(2)


def bant_gurultu(n, f1, f2, egim=0.0, rng=RNG):
    """FFT ile bant sınırlı gürültü (dairesel → döngüde dikiş yok)."""
    W = np.fft.rfft(rng.standard_normal(n))
    f = np.fft.rfftfreq(n, 1 / SR)
    m = ((f >= f1) & (f <= f2)).astype(float)
    m[1:] *= (f[1:] / max(f1, 1)) ** egim
    return np.fft.irfft(W * m, n)


def fft_alcak(x, fc):
    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(len(x), 1 / SR)
    X *= 1 / np.sqrt(1 + (f / fc) ** 4)
    return np.fft.irfft(X, len(x))


def can(f, sure, oranlar=(1, 2.0, 2.76, 5.4, 8.93), sonum=(1.0, 1.6, 2.4, 3.6, 5.0), tau=0.9):
    """Çan/zil: uyumsuz kısmi tonlar, yüksek kısmiler daha hızlı söner."""
    t = t_(sure)
    y = sum((0.6 ** i) * np.sin(2 * np.pi * f * r * t) * np.exp(-t * s / tau)
            for i, (r, s) in enumerate(zip(oranlar, sonum)))
    atak = np.minimum(t / 0.002, 1)
    return y * atak


def testere(f, t, ust=4000):
    """Bant sınırlı testere dalga (toplamsal)."""
    y = np.zeros_like(t)
    for k in range(1, int(ust / f) + 1):
        y += np.sin(2 * np.pi * f * k * t) / k
    return y


def klik(sure, f1, f2, tau):
    n = int(sure * SR)
    g = bant_gurultu(n, f1, f2)
    return g * np.exp(-t_(sure) / tau)


def yerlestir(hedef, x, bas):
    i = int(bas * SR)
    j = min(len(hedef), i + len(x))
    hedef[i:j] += x[:j - i]


def yaz(yol, st):
    st = np.asarray(st, dtype=np.float32)
    if st.ndim == 1:
        st = stereo(st)
    p = subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-",
                        "-c:a", "flac", "-sample_fmt", "s16", yol], input=st.astype(np.float32).tobytes())
    assert p.returncode == 0, yol


# ---------------- SFX ----------------
def ding_oyunsovu():
    return norm(can(1318.5, 1.6) + 0.5 * can(1975.5, 1.6, tau=0.6))  # E6 + B6 (beşli), parlak sunucu zili


def ding_ding_dogru():
    y = np.zeros(int(1.5 * SR))
    yerlestir(y, can(1046.5, 1.0, tau=0.5), 0.0)   # C6
    yerlestir(y, can(1318.5, 1.3, tau=0.7), 0.16)  # E6
    return norm(y)


def buzzer_yanlis():
    t = t_(0.75)
    y = testere(92, t, 3500) + testere(97.5, t, 3500)   # sapmalı iki testere: "yanlış cevap" vızıltısı
    y *= 1 + 0.25 * np.sin(2 * np.pi * 11 * t)
    zarf = np.minimum(t / 0.01, 1) * np.minimum((0.75 - t) / 0.06, 1)
    return norm(fft_alcak(y * zarf, 2500))


def saat_tik(f=3200, sure=0.09):
    t = t_(sure)
    y = klik(sure, 1500, 9000, 0.004) + 0.6 * np.sin(2 * np.pi * f * t) * np.exp(-t / 0.012)
    return norm(y)


def sayac_tikirti():
    """Sayı sayacı dönerken hızlı tıkırtı (1.5 sn, 18/sn, sonda yavaşlar)."""
    y = np.zeros(int(1.6 * SR))
    zaman, ara = 0.0, 1 / 18
    while zaman < 1.45:
        yerlestir(y, 0.7 * saat_tik(2600 + RNG.uniform(-150, 150), 0.05), zaman)
        zaman += ara
        if zaman > 1.0:
            ara *= 1.12
    return norm(y)


def kasa_kilit():
    """Kasa çarkı tıkırtısı (hızlanan 7 tık) + ağır metal sürgü 'kunk'."""
    y = np.zeros(int(1.8 * SR))
    zaman = 0.0
    for i in range(7):
        yerlestir(y, 0.35 * saat_tik(2100 + 80 * i, 0.06), zaman)
        zaman += 0.11 * (0.86 ** i)
    t = t_(1.2)
    gum = np.sin(2 * np.pi * (70 + 40 * np.exp(-t / 0.03)) * t) * np.exp(-t / 0.18)
    metal = sum(a * np.sin(2 * np.pi * f * t) * np.exp(-t / d)
                for a, f, d in ((0.5, 410, 0.35), (0.35, 1130, 0.22), (0.2, 2210, 0.12), (0.12, 3370, 0.07)))
    yerlestir(y, 1.0 * gum + 0.6 * metal + 0.5 * klik(1.2, 200, 4000, 0.01), zaman + 0.08)
    return norm(y)


def gerilim_vurus():
    """Tek notalık gerilim vuruşu: düşen alt bas + uyumsuz küme (La2 + Si♭2) 2.5 sn kuyruk."""
    t = t_(2.6)
    bas = np.sin(2 * np.pi * np.cumsum(45 + 45 * np.exp(-t / 0.08)) / SR) * np.exp(-t / 0.9)
    kume = (testere(110, t, 2500) + testere(116.54, t, 2500) + 0.5 * testere(220.5, t, 2500))
    kume = fft_alcak(kume, 900) * np.minimum(t / 0.03, 1) * np.exp(-t / 1.1)
    darbe = klik(2.6, 60, 3000, 0.02)
    return norm(1.0 * bas + 0.35 * kume + 0.5 * darbe)


def ruzgar_dusus():
    """Rüzgâr (yavaş dalgalanan bant gürültü) + çizgi film düşüş tonu 880 → 110 Hz."""
    sure = 2.8
    t = t_(sure)
    n = len(t)
    g = bant_gurultu(n, 150, 1400, egim=-0.5)
    g *= 0.6 + 0.4 * np.sin(2 * np.pi * 0.7 * t + 1)
    f = 880 * (110 / 880) ** (np.clip(t - 0.3, 0, 2.2) / 2.2)
    ton = np.sin(2 * np.pi * np.cumsum(f) / SR) * np.clip((t - 0.3) / 0.1, 0, 1) * np.clip((2.6 - t) / 0.3, 0, 1)
    zarf = np.minimum(t / 0.4, 1) * np.minimum((sure - t) / 0.4, 1)
    y = norm(g) * 0.8 + 0.45 * ton
    return norm(stereo(y * zarf, 0.0) + 0.15 * stereo(norm(bant_gurultu(n, 150, 1400)) * zarf, 0.6))


def radyo_cizirti():
    """1933 radyosu: bant sınırlı hışırtı + çıtırtılar (Roosevelt radyo silueti altına), 3 sn döngü."""
    n = int(3.0 * SR)
    h = bant_gurultu(n, 300, 3200) * 0.35
    cit = np.zeros(n)
    for i in RNG.integers(0, n - 500, 90):
        cit[i:i + 200] += RNG.uniform(0.3, 1.0) * np.exp(-np.arange(200) / 25) * RNG.choice([-1, 1])
    cit = np.fft.irfft(np.fft.rfft(cit) * (np.fft.rfftfreq(n, 1 / SR) > 800), n)
    uğultu = 0.08 * np.sin(2 * np.pi * 60 * t_(3.0))
    return norm(h + 0.8 * cit / (np.abs(cit).max() + 1e-9) + uğultu)


def ka_ching():
    """Yazar kasa: çekmece metali + çift zil."""
    y = np.zeros(int(1.4 * SR))
    yerlestir(y, 0.6 * klik(0.25, 600, 6000, 0.05), 0.0)
    yerlestir(y, can(2093, 1.2, tau=0.5) + 0.7 * can(2637, 1.2, tau=0.45), 0.09)  # C7 + E7
    return norm(y)


def kapi_isik_acilis():
    """Oyun şovu kapısı ışıkla açılır: yükselen gürültü süpürmesi + 4 notalık parıltı arpeji."""
    sure = 1.6
    y = np.zeros(int(sure * SR))
    n = len(y)
    t = t_(sure)
    sup = bant_gurultu(n, 300, 8000) * (t / sure) ** 2 * np.exp(-np.maximum(t - 1.2, 0) / 0.1)
    y += 0.35 * norm(sup)
    for i, f in enumerate((1046.5, 1318.5, 1568.0, 2093.0)):  # C6 E6 G6 C7
        yerlestir(y, 0.5 * can(f, 0.9, tau=0.35), 0.75 + 0.09 * i)
    return norm(y)


# ---------------- Yataklar ----------------
def kick(f0=55, sure=0.4):
    t = t_(sure)
    return np.sin(2 * np.pi * np.cumsum(f0 + 90 * np.exp(-t / 0.02)) / SR) * np.exp(-t / 0.12)


def yatak_nabiz():
    """90 BPM, 24 ölçü (64 sn): kalp atışı (çift tok), sekizlik saat tıkı, La1 drone + yavaş filtre."""
    bpm, olcu = 90, 24
    vurus = 60 / bpm
    sure = olcu * 4 * vurus
    n = int(sure * SR)
    t = np.arange(n) / SR
    y = np.zeros(n)
    for b in range(olcu * 4):
        tb = b * vurus
        yerlestir(y, 0.9 * kick(52), tb)
        yerlestir(y, 0.55 * kick(48), tb + 0.18)
        for k in (0, 0.5):
            yerlestir(y, 0.25 * saat_tik(3000 if k == 0 else 2300, 0.05), tb + k * vurus)
    lfo = 0.5 + 0.5 * np.sin(2 * np.pi * t / sure * 3)       # 3 tam dalga → döngüde dikiş yok
    drone = (np.sin(2 * np.pi * 55 * t) + 0.5 * np.sin(2 * np.pi * 82.5 * t) + 0.3 * np.sin(2 * np.pi * 110.4 * t))
    drone *= 0.25 + 0.1 * lfo
    # telefon hoparlöründe duyulsun diye orta bant: 220/330 Hz testere, yavaş tremolo, alçak geçiren 900 Hz
    orta = fft_alcak(testere(220.0, t, 2000) + 0.7 * testere(330.0, t, 2000), 900)
    orta *= (0.5 + 0.5 * np.sin(2 * np.pi * t * 6 * olcu * 4 / sure * 0.25)) * (0.4 + 0.6 * lfo)
    orta = norm(orta) * 0.45
    return norm(stereo(y + drone, 0) + stereo(0.15 * drone, 0.4) + stereo(orta, -0.3))


def yatak_dip():
    """Re minör karanlık pad (Re2 Fa2 La2 Mi3), uzun nefes dalgalanması, 60 sn döngü."""
    sure = 60.0
    n = int(sure * SR)
    t = np.arange(n) / SR
    notalar = (73.42, 87.31, 110.0, 164.81)
    y = np.zeros((n, 2))
    for i, f in enumerate(notalar):
        for d, pan in ((-0.6, -0.5), (0.6, 0.5)):           # iki sesli hafif sapma → koro genişliği
            fd = f * 2 ** (d / 1200 * 8)
            fd = round(fd * sure) / sure                     # tam döngü frekansı
            nefes = 0.6 + 0.4 * np.sin(2 * np.pi * (i + 1) * t / sure + i)
            ton = (np.sin(2 * np.pi * fd * t) + 0.5 * np.sin(2 * np.pi * 2 * fd * t)
                   + 0.3 * np.sin(2 * np.pi * 3 * fd * t) + 0.2 * np.sin(2 * np.pi * 4 * fd * t)) * nefes / (i + 1) ** 0.5
            y += stereo(ton, pan) * 0.5
    ruzgar = fft_alcak(bant_gurultu(n, 80, 3000, egim=-0.7), 700)
    y += stereo(norm(ruzgar) * 0.08, 0)
    return norm(y)


def yatak_kilit_saat():
    """100 BPM, 20 ölçü (48 sn): saat tik-tak dörtlük, bas ostinato La1-La1-Do2-Si1, ölçü başı metal vuruş."""
    bpm, olcu = 100, 20
    vurus = 60 / bpm
    sure = olcu * 4 * vurus
    n = int(sure * SR)
    y = np.zeros(n)
    bas_notalar = (55.0, 55.0, 65.41, 61.74)
    for m in range(olcu):
        for b in range(4):
            tb = (m * 4 + b) * vurus
            yerlestir(y, 0.25 * saat_tik(3200 if b % 2 == 0 else 2000, 0.06), tb)
            tt = t_(vurus * 0.9)
            f = bas_notalar[b]
            ton = sum(a * np.sin(2 * np.pi * k * f * tt) for k, a in ((1, 1), (2, 0.6), (3, 0.45), (4, 0.3), (5, 0.2))) * np.exp(-tt / 0.35)
            yerlestir(y, 0.5 * ton * np.minimum(tt / 0.005, 1), tb)
        tt = t_(1.2)
        metal = sum(a * np.sin(2 * np.pi * f * tt) * np.exp(-tt / d)
                    for a, f, d in ((0.5, 410, 0.4), (0.3, 1130, 0.25), (0.15, 2210, 0.12)))
        yerlestir(y, 0.08 * metal, m * 4 * vurus)
    return norm(stereo(y, 0))


if __name__ == "__main__":
    d = sys.argv[1]
    isler = {
        "ding-oyunsovu": ding_oyunsovu, "ding-ding-dogru": ding_ding_dogru, "buzzer-yanlis": buzzer_yanlis,
        "saat-tik": lambda: saat_tik(3200), "saat-tok": lambda: saat_tik(1900), "sayac-tikirti": sayac_tikirti,
        "kasa-kilit": kasa_kilit, "gerilim-vurus": gerilim_vurus, "ruzgar-dusus": ruzgar_dusus,
        "radyo-cizirti": radyo_cizirti, "ka-ching": ka_ching, "kapi-isik-acilis": kapi_isik_acilis,
        "yatak-nabiz-90bpm": yatak_nabiz, "yatak-dip-drone": yatak_dip, "yatak-kilit-saat-100bpm": yatak_kilit_saat,
    }
    sec = sys.argv[2:] or list(isler)
    for ad in sec:
        yaz(f"{d}/ozgun-{ad}.flac", isler[ad]())
        print("yazıldı", ad)
