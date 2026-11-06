#!/usr/bin/env python3
"""Ses yama/birleştirme: parçaları 12 ms fade ile uç uca ekler (48 kHz mono float WAV).

Kullanım: birlestir.py <plan.json | '[[...]]'> <cikis.wav> --ana ana.wav [--duzeltme duz.wav] [--kaynak ad=dosya ...]
  plan: [[kaynak, başlangıç_sn, bitiş_sn], ...]; kaynak "o" = --ana, "d" = --duzeltme, diğerleri --kaynak ad=dosya.
Kural: sessiz noktadan (−50 dB altı) kes; birleştirmeden sonra TEK loudnorm geçişi (tools/ses/temizle.sh / tts-son.sh).
2026-10-26: ana/düzeltme yolları betiğe gömülüydü (pilot dosyası) → parametre yapıldı.
"""
import argparse, json, os, subprocess, sys
import numpy as np, soundfile as sf

SR = 48000


def load(f):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", f, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, dtype=np.float32).copy()


def seg(a, t0, t1, fade=0.012):
    s = a[int(t0 * SR):int(t1 * SR)].copy(); n = min(int(fade * SR), len(s) // 2)
    if n:
        s[:n] *= np.linspace(0, 1, n); s[-n:] *= np.linspace(1, 0, n)
    return s


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("plan"); ap.add_argument("cikis")
    ap.add_argument("--ana", required=True); ap.add_argument("--duzeltme")
    ap.add_argument("--kaynak", action="append", default=[], help="ad=dosya")
    a = ap.parse_args()
    yollar = {"o": a.ana, **({"d": a.duzeltme} if a.duzeltme else {}), **dict(k.split("=", 1) for k in a.kaynak)}
    plan = json.load(open(a.plan)) if os.path.exists(a.plan) else json.loads(a.plan)
    eksik = {src for src, _, _ in plan} - set(yollar)
    if eksik:
        sys.exit(f"HATA: planda tanımsız kaynak: {sorted(eksik)}")
    sesler = {k: load(v) for k, v in yollar.items() if any(src == k for src, _, _ in plan)}
    out = []
    for src, t0, t1 in plan:
        if t1 * SR > len(sesler[src]) + 1 or t0 >= t1:
            sys.exit(f"HATA: geçersiz aralık {src} {t0}-{t1} (kaynak {len(sesler[src]) / SR:.2f} sn)")
        out.append(seg(sesler[src], t0, t1))
    y = np.concatenate(out); sf.write(a.cikis, y, SR, subtype="FLOAT")
    print(a.cikis, round(len(y) / SR, 2))


if __name__ == "__main__":
    main()
