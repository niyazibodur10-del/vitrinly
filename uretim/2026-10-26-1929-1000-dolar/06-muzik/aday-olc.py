#!/usr/bin/env python3
"""Müzik/SFX aday ölçümü (F4). Yalnız numpy + ffmpeg; CPU hafif (nice ile çalıştır).

Kullanım:
  aday-olc.py muzik <konusma-ornegi> <dosya>...   → müzik tablosu (JSON satırları)
  aday-olc.py sfx <dosya>...                      → SFX tablosu (JSON satırları)

Müzik ölçütleri:
  lufs / lra / tp  : ffmpeg ebur128 (entegre ses yüksekliği, ses yüksekliği aralığı, true peak)
  konusma_bandi    : 1–4 kHz enerji payı (yüksekse anlatımı maskeler; pilot eşiği ≤0.15)
  merkez_hz        : spektral ağırlık merkezi (parlaklık)
  bpm              : başlangıç-zarfı otokorelasyonu ile tempo tahmini (60–180) [tahmin]
  st_std_db        : 3 sn kısa süreli ses yüksekliği std (yatak olarak dalgalanma; düşük = sabit)
  maske_snr_db     : müzik konuşmanın 21 LU altına çekilip konuşma örneğiyle karıştırıldığında,
                     konuşmalı karelerde 1–4 kHz bandında konuşma/müzik oranının medyanı
                     (yüksek = anlaşılırlık için daha güvenli). Whisper WER F6'da gerçek anlatımla ölçülür.
SFX ölçütleri: sure, aktif_sn (tepeye göre −30 dB üstü), tepe_dbfs, taban_db (en sessiz %10 kare RMS'i, tepeye göre),
  merkez_hz.
"""
import json, re, subprocess, sys
import numpy as np

SR = 16000


def yukle(yol, sr=SR, sure=None):
    kom = ["ffmpeg", "-v", "error", "-i", yol]
    if sure:
        kom += ["-t", str(sure)]
    kom += ["-ac", "1", "-ar", str(sr), "-f", "f32le", "-"]
    return np.frombuffer(subprocess.run(kom, capture_output=True, check=True).stdout, dtype=np.float32).astype(np.float64)


def ebur(yol):
    e = subprocess.run(["ffmpeg", "-nostats", "-i", yol, "-af", "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True).stderr
    oz = e[e.rfind("Summary:"):]
    g = lambda k: float(re.search(k + r":\s+(-?[\d.]+|-inf)", oz).group(1).replace("-inf", "-99"))
    kisa = [float(x) for x in re.findall(r"S:\s*(-?[\d.]+)", e)]
    kisa = [k for k in kisa if k > -60]
    return g("I"), g("LRA"), g("Peak"), (float(np.std(kisa)) if kisa else 0.0)


def spektrum(x, cer=2048, adim=1024):
    w = np.hanning(cer)
    idx = np.arange(0, len(x) - cer, adim)
    F = np.abs(np.fft.rfft(np.stack([x[i:i + cer] * w for i in idx]), axis=1)) ** 2
    return F, np.fft.rfftfreq(cer, 1 / SR)


def bpm_tahmin(x):
    F, f = spektrum(x, 1024, 160)  # 10 ms adım
    fl = np.maximum(np.diff(np.log1p(F), axis=0), 0).sum(1)
    fl -= fl.mean()
    ac = np.correlate(fl, fl, "full")[len(fl) - 1:]
    kare = 160 / SR
    lag = np.arange(len(ac)) * kare
    m = (lag >= 60 / 180) & (lag <= 60 / 60)
    en = np.argmax(ac * m)
    return round(60 / lag[en], 1)


def muzik(konusma_yol, yol):
    lufs, lra, tp, st = ebur(yol)
    x = yukle(yol)
    F, f = spektrum(x)
    top = F.sum()
    bant = F[:, (f >= 1000) & (f <= 4000)].sum() / top
    merkez = float((F.sum(0) * f).sum() / F.sum(0).sum())
    bpm = bpm_tahmin(x[: SR * 60])
    # maskeleme: 30 sn konuşma örneği; müzik −21 LU (RMS yaklaşımı)
    k = yukle(konusma_yol, sure=30)
    n = len(k)
    mz = np.resize(x, n)  # kısa parçayı döngüle
    rms = lambda v: np.sqrt(np.mean(v ** 2) + 1e-12)
    aktif_k = k[np.abs(k) > 0.02]
    mz = mz / rms(mz) * rms(aktif_k) * 10 ** (-21 / 20)
    Fk, ff = spektrum(k)
    Fm, _ = spektrum(mz)
    b = (ff >= 1000) & (ff <= 4000)
    ek, em = Fk[:, b].sum(1), Fm[:, b].sum(1)
    konusmali = Fk.sum(1) > np.percentile(Fk.sum(1), 40)
    snr = float(np.median(10 * np.log10(ek[konusmali] / (em[konusmali] + 1e-12))))
    return dict(dosya=yol.split("/")[-1], sure=round(len(x) / SR, 1), lufs=lufs, lra=lra, tp=tp,
                konusma_bandi=round(float(bant), 3), merkez_hz=round(merkez), bpm=bpm,
                st_std_db=round(st, 1), maske_snr_db=round(snr, 1))


def sfx(yol):
    x = yukle(yol, 48000)
    sr = 48000
    tepe = np.abs(x).max() + 1e-12
    cer = int(0.01 * sr)
    r = np.sqrt(np.array([np.mean(x[i:i + cer] ** 2) for i in range(0, len(x) - cer, cer)]) + 1e-12)
    aktif = (20 * np.log10(r / r.max()) > -30).sum() * 0.01
    taban = 20 * np.log10(np.percentile(r, 10) / r.max())
    k = yukle(yol)
    F, f = spektrum(np.pad(k, (0, max(0, 4096 - len(k)))))  # çok kısa efekt: sıfır doldur
    merkez = float((F.sum(0) * f).sum() / max(F.sum(0).sum(), 1e-12)) if len(F) else 0.0
    return dict(dosya=yol.split("/")[-1], sure=round(len(x) / sr, 2), aktif_sn=round(aktif, 2),
                tepe_dbfs=round(20 * np.log10(tepe), 1), taban_db=round(float(taban), 1), merkez_hz=round(merkez))


if __name__ == "__main__":
    kip = sys.argv[1]
    if kip == "muzik":
        for y in sys.argv[3:]:
            print(json.dumps(muzik(sys.argv[2], y), ensure_ascii=False), flush=True)
    else:
        for y in sys.argv[2:]:
            print(json.dumps(sfx(y), ensure_ascii=False), flush=True)
