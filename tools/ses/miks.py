#!/usr/bin/env python3
"""Anlatım + alt müzik (ducking) + efektler -> stereo miks, son dosyada -14 LUFS / TP -1.

Kullanım:
  miks.py <anlatim.wav> <muzik> <cikis.m4a> [--muzik-db -12] [--duck-db 9] [--giris 2.0] [--cikis-sn 3.0]
          [--efekt dosya.flac@saniye@dB ...]   (saniye anlatımın başına göre; dB efekt kazancı)
Mantık:
  - Müzik önce kendi başına -14 LUFS'a ölçeklenir, sonra --muzik-db (konuşma yokken yatak seviyesi) uygulanır.
  - Konuşma varken sidechain kompresör müziği yaklaşık --duck-db kadar daha bastırır
    (hedef: konuşma altında müzik, anlatımdan 18–24 dB düşük).
  - Müzik gerekirse döngülenir; girişte 1 sn fade-in, sonda --cikis-sn kadar uzar ve söner.
  - Son stereo dosya 2 geçişli loudnorm ile -14 LUFS / TP -1'e getirilir (ortak ders: normalizasyon son stereo dosyada).
  - Ölçüm: konuşma bölümlerinde anlatım ve bastırılmış müzik ayrı ayrı (kısa süreli LUFS) ölçülür, fark raporlanır.
"""
import argparse, json, re, subprocess, sys, tempfile, os
import numpy as np


def sh(*a):
    return subprocess.run(list(a), capture_output=True, text=True)


def lufs(yol, af=""):
    r = sh("ffmpeg", "-hide_banner", "-nostats", "-i", yol, "-af", (af + "," if af else "") + "ebur128=peak=true",
           "-f", "null", "-")
    s = r.stderr[r.stderr.rfind("Summary"):]
    g = lambda k: float(re.search(k + r":\s+(-?[\d.]+|-inf)", s).group(1).replace("-inf", "-120"))
    return {"I": g("I"), "LRA": g("LRA"), "TP": g("Peak")}


def sure(yol):
    return float(sh("ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", yol).stdout)


def kisa_lufs_dizisi(yol, sr=48000):
    """400 ms pencere / 100 ms adım RMS seviyesi (dB, 100 Hz üstü) — iki stem arasındaki farkı ölçmek için."""
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", yol, "-ac", "1", "-ar", str(sr), "-af", "highpass=f=100",
                          "-f", "f32le", "-"], capture_output=True).stdout
    x = np.frombuffer(raw, np.float32).astype(float)
    w, h = int(0.4 * sr), int(0.1 * sr)
    return np.array([10 * np.log10(np.mean(x[i:i + w] ** 2) + 1e-12) for i in range(0, len(x) - w, h)])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("anlatim"); ap.add_argument("muzik"); ap.add_argument("cikis")
    ap.add_argument("--muzik-db", type=float, default=-12)
    ap.add_argument("--duck-db", type=float, default=9)
    ap.add_argument("--giris", type=float, default=2.0)
    ap.add_argument("--cikis-sn", type=float, default=3.0)
    ap.add_argument("--efekt", action="append", default=[])
    a = ap.parse_args()

    tmp = tempfile.mkdtemp()
    ds = sure(a.anlatim); top = a.giris + ds + a.cikis_sn
    mk = -14 - lufs(a.muzik)["I"] + a.muzik_db  # müzik kazancı
    # sidechain: oran, --duck-db kadar bastırma verecek şekilde (eşik üstü ~12 dB konuşma enerjisi varsayımı)
    oran = max(1.5, 12 / max(12 - a.duck_db, 0.5))
    girdiler = ["-i", a.anlatim, "-stream_loop", "-1", "-i", a.muzik]
    fc = [f"[0:a]aresample=48000,pan=stereo|c0=c0|c1=c0,adelay={int(a.giris*1000)}:all=1,apad=whole_dur={top}[v]",
          "[v]asplit=3[v1][vsc][vstem]",
          f"[1:a]aresample=48000,aformat=channel_layouts=stereo,atrim=0:{top},volume={mk:.2f}dB,"
          f"afade=t=in:d=1,afade=t=out:st={top - a.cikis_sn + 0.5}:d={a.cikis_sn - 0.5}[m]",
          f"[m][vsc]sidechaincompress=threshold=0.015:ratio={oran:.1f}:attack=30:release=450:knee=4:makeup=1[md]",
          "[md]asplit=2[m1][mstem]"]
    karisim = ["[v1]", "[m1]"]
    for i, e in enumerate(a.efekt):
        yol, t, db = e.split("@")
        girdiler += ["-i", yol]
        fc.append(f"[{i+2}:a]aresample=48000,aformat=channel_layouts=stereo,volume={db}dB,"
                  f"adelay={int((a.giris+float(t))*1000)}:all=1[e{i}]")
        karisim.append(f"[e{i}]")
    fc.append("".join(karisim) + f"amix=inputs={len(karisim)}:normalize=0:duration=first[mix]")
    ham = f"{tmp}/ham.wav"
    r = sh("ffmpeg", "-v", "error", "-y", *girdiler, "-filter_complex", ";".join(fc),
           "-map", "[mix]", "-c:a", "pcm_f32le", ham,
           "-map", "[vstem]", "-c:a", "pcm_f32le", f"{tmp}/v.wav",
           "-map", "[mstem]", "-c:a", "pcm_f32le", f"{tmp}/m.wav")
    if r.returncode: sys.exit(r.stderr)
    # son stereo dosyada 2 geçişli loudnorm
    j = sh("ffmpeg", "-hide_banner", "-nostats", "-i", ham, "-af", "loudnorm=I=-14:TP=-1:LRA=11:print_format=json",
           "-f", "null", "-").stderr
    m = json.loads(j[j.rfind("{"):j.rfind("}") + 1])
    ln = (f"loudnorm=I=-14:TP=-1:LRA=11:measured_I={m['input_i']}:measured_TP={m['input_tp']}:"
          f"measured_LRA={m['input_lra']}:measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true")
    r = sh("ffmpeg", "-v", "error", "-y", "-i", ham, "-af", ln + ",aresample=48000", "-c:a", "aac", "-b:a", "192k",
           a.cikis)
    if r.returncode: sys.exit(r.stderr)
    # ölçüm: konuşma anlarında anlatım - müzik farkı
    v, mu = kisa_lufs_dizisi(f"{tmp}/v.wav"), kisa_lufs_dizisi(f"{tmp}/m.wav")
    n = min(len(v), len(mu)); v, mu = v[:n], mu[:n]
    konusma = v > (np.max(v) - 20)
    fark = v[konusma] - mu[konusma]
    yatak = mu[: int(a.giris * 10) - 4]  # giriş (yalnız müzik) bölümü
    son = lufs(a.cikis)
    out = {"cikis": a.cikis, "sure_sn": round(sure(a.cikis), 2), "son_I_LUFS": son["I"], "son_TP_dBTP": son["TP"],
           "son_LRA": son["LRA"], "konusma_alti_fark_dB_medyan": round(float(np.median(fark)), 1),
           "konusma_alti_fark_dB_p10_p90": [round(float(np.percentile(fark, 10)), 1),
                                            round(float(np.percentile(fark, 90)), 1)],
           "giris_yatak_vs_konusma_dB": round(float(np.median(v[konusma]) - np.median(yatak)), 1) if len(yatak) else None,
           "sidechain_oran": round(oran, 1), "muzik_kazanc_dB": round(mk, 1)}
    print(json.dumps(out, ensure_ascii=False))


if __name__ == "__main__":
    main()
