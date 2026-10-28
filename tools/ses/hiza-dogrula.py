#!/usr/bin/env python3
"""Akustik hiza doğrulaması: anlatım wav'ında her cümlenin gerçek ses başlangıcı/bitişi (cümle penceresi ±0,2 sn içinde
10 ms RMS'in ilk/son kez eşiği (-45 dBFS) geçtiği an; TTS cümle arası dijital sessizlik) vs hizalı kelimeler (+ ham Whisper
karşılaştırması). Kapı (docs/kalite-kapilari.md altyazı ±150 ms): hizalı ilk kelime başı ve son kelime sonu |fark| p95 <= 150 ms.

Kullanım: ~/.finansal-arac/venv/bin/python tools/ses/hiza-dogrula.py --dizin uretim/<video>/04-ses [--esik-db -45] [--kapi-ms 150]
  Girdi adları (dizine göre): --ses anlatim.wav --zaman anlatim-ham.zaman.json --hizali kelimeler-hizali.json
  --kelimeler kelimeler.json (ham Whisper; yoksa karşılaştırma satırı atlanır)
Çıkış kodu: 0 GEÇTİ, 1 KALDI (eski 04-ses/hiza-dogrula.py her zaman 0 dönüyordu).
Genelleştirildi 2026-10-27 (uretim-muhendisi): kaynak uretim/2026-10-26-1929-1000-dolar/04-ses/hiza-dogrula.py.
"""
import argparse, json, os, sys
import numpy as np, soundfile as sf


def main():
    ap = argparse.ArgumentParser(description="Akustik altyazı hiza kapısı")
    ap.add_argument("--dizin", default=".")
    ap.add_argument("--ses", default="anlatim.wav"); ap.add_argument("--zaman", default="anlatim-ham.zaman.json")
    ap.add_argument("--hizali", default="kelimeler-hizali.json"); ap.add_argument("--kelimeler", default="kelimeler.json")
    ap.add_argument("--esik-db", type=float, default=-45.0); ap.add_argument("--kapi-ms", type=float, default=150.0)
    a = ap.parse_args()
    yol = lambda p: p if os.path.isabs(p) else os.path.join(a.dizin, p)
    y, sr = sf.read(yol(a.ses))
    if y.ndim > 1:
        y = y.mean(axis=1)
    h = int(0.01 * sr)
    rms = 20 * np.log10(np.sqrt(np.convolve(y ** 2, np.ones(h) / h, "same")) + 1e-12)
    C = json.load(open(yol(a.zaman)))["cumleler"]; O = json.load(open(yol(a.hizali)))["words"]
    W = json.load(open(yol(a.kelimeler)))["words"] if os.path.exists(yol(a.kelimeler)) else None

    def akustik(c):
        i0, i1 = int(max(0, c["bas"] - 0.2) * sr), int((c["son"] + 0.2) * sr); idx = np.where(rms[i0:i1] > a.esik_db)[0]
        if not len(idx):
            return None
        return (i0 + idx[0]) / sr, (i0 + idx[-1]) / sr

    fb, fs, wb, sessiz, eksik = [], [], [], [], []
    for ci, c in enumerate(C):
        ak = akustik(c); ws = [o for o in O if o["cumle"] == ci]
        if ak is None:
            sessiz.append(ci); continue
        if not ws:
            eksik.append(ci); continue
        s0, e0 = ak
        fb.append(abs(ws[0]["s"] - s0)); fs.append(abs(ws[-1]["e"] - e0))
        if W:
            ilk = min(W, key=lambda w: abs(w["s"] - s0)); wb.append(abs(ilk["s"] - s0))
    if not fb:
        sys.exit("HATA: ölçülebilir cümle yok (ses/zaman dosyası uyuşmuyor mu?)")
    p = lambda v, q: round(sorted(v)[min(len(v) - 1, int(q * len(v)))] * 1000)
    print(f"cümle={len(C)} | hizalı baş fark p50={p(fb,.5)} p95={p(fb,.95)} maks={p(fb,1)} ms | hizalı son fark p50={p(fs,.5)} p95={p(fs,.95)} maks={p(fs,1)} ms")
    if wb:
        print(f"karşılaştırma ham Whisper en yakın kelime başı: p50={p(wb,.5)} p95={p(wb,.95)} maks={p(wb,1)} ms")
    if sessiz:
        print(f"UYARI: penceresinde eşik üstü ses olmayan cümleler: {sessiz}")
    if eksik:
        print(f"UYARI: hizalı kelimesi olmayan cümleler (kapıyı düşürür): {eksik}")
    gecti = p(fb, .95) <= a.kapi_ms and p(fs, .95) <= a.kapi_ms and not eksik
    print("KAPI", "GEÇTİ" if gecti else "KALDI")
    return 0 if gecti else 1


if __name__ == "__main__":
    sys.exit(main())
