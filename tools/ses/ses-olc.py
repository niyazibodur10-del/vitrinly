#!/usr/bin/env python3
"""Anlatıcı sesi ölçümü (tını + tempo göstergeleri).

Kullanım: ses-olc.py <ses> [whisper.json] [ref.txt]
Çıktı (tek satır JSON):
  sure_sn, f0_ort_hz (perde ortalaması), f0_std_st (perde değişkenliği, yarım ton; düşük = monoton),
  f0_aralik_st (5.-95. yüzdelik aralığı, yarım ton), sesli_oran,
  merkez_hz (spektral ağırlık merkezi; yüksek = parlak/ince, düşük = koyu/boğuk),
  kpm (kelime/dk: ref kelime sayısı / ilk-son kelime arası süre), duraklama_sayisi (>=250 ms boşluk),
  ort_guven (Whisper kelime olasılığı ortalaması), dusuk_guven (p<0.6 kelime sayısı)
Bağımlılık: numpy + ffmpeg. Perde: YIN (de Cheveigné & Kawahara 2002), 60–300 Hz erkek ses aralığı.
"""
import json, re, subprocess, sys
import numpy as np

SR = 16000


def yukle(yol):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", yol, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32).astype(np.float64)


def yin(x, fmin=60, fmax=300, cer=1024, adim=160, esik=0.2):
    tmin, tmax = SR // fmax, SR // fmin
    f0 = []
    for i in range(0, len(x) - cer - tmax, adim):
        fr = x[i:i + cer + tmax]
        if np.sqrt(np.mean(fr[:cer] ** 2)) < 0.01:  # sessiz kare
            f0.append(0.0); continue
        d = np.array([np.sum((fr[:cer] - fr[t:t + cer]) ** 2) for t in range(tmax + 1)])
        cmnd = np.ones_like(d)
        cs = np.cumsum(d[1:])
        cmnd[1:] = d[1:] * np.arange(1, tmax + 1) / np.maximum(cs, 1e-12)
        t = None
        for k in range(tmin, tmax):
            if cmnd[k] < esik:
                while k + 1 < tmax and cmnd[k + 1] < cmnd[k]:
                    k += 1
                t = k; break
        if t is None:
            f0.append(0.0); continue
        # parabolik ara değer
        a, b, c = cmnd[t - 1], cmnd[t], cmnd[t + 1]
        den = a - 2 * b + c
        tt = t + (0.5 * (a - c) / den if den != 0 else 0)
        f0.append(SR / tt)
    return np.array(f0)


def main():
    x = yukle(sys.argv[1])
    x = x / (np.max(np.abs(x)) + 1e-9) * 0.9  # seviye bağımsız ölçüm
    out = {"sure_sn": round(len(x) / SR, 2)}
    f0 = yin(x)
    v = f0[f0 > 0]
    st = 12 * np.log2(v / np.median(v))
    out.update(f0_ort_hz=round(float(np.mean(v)), 1), f0_std_st=round(float(np.std(st)), 2),
               f0_aralik_st=round(float(np.percentile(st, 95) - np.percentile(st, 5)), 1),
               sesli_oran=round(len(v) / len(f0), 2))
    # spektral merkez (konuşma olan kareler)
    n = 1024
    fr = np.lib.stride_tricks.sliding_window_view(x, n)[::512] * np.hanning(n)
    mag = np.abs(np.fft.rfft(fr, axis=1))
    en = mag.sum(1)
    m = en > np.percentile(en, 40)
    freqs = np.fft.rfftfreq(n, 1 / SR)
    out["merkez_hz"] = int(np.mean((mag[m] * freqs).sum(1) / mag[m].sum(1)))
    if len(sys.argv) > 2:
        w = json.load(open(sys.argv[2]))["words"]
        nref = len(re.findall(r"[A-Za-z0-9']+", open(sys.argv[3]).read())) if len(sys.argv) > 3 else len(w)
        konusma = w[-1]["e"] - w[0]["s"]
        out["kpm"] = round(nref / konusma * 60, 1)
        out["duraklama_sayisi"] = sum(1 for a, b in zip(w, w[1:]) if b["s"] - a["e"] >= 0.25)
        out["ort_guven"] = round(float(np.mean([k["p"] for k in w])), 3)
        out["dusuk_guven"] = sum(1 for k in w if k["p"] < 0.6)
    print(json.dumps(out, ensure_ascii=False))


if __name__ == "__main__":
    main()
