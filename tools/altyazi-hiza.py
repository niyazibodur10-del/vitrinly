#!/usr/bin/env python3
"""Gömülü altyazı hizası testi: altyazı kelime zamanları vs SON videonun sesinden Whisper kelime zamanları.

Kullanım:
  ~/.finansal-arac/venv/bin/python tools/ses/yaziya-dok.py final.mp4 render-kelimeler.json medium.en
  python3 tools/altyazi-hiza.py render-kelimeler.json <altyazi.json | data.ts> [--fps 30] [--esik-kare 2]
altyazi.json: tools/altyazi-uret.py --json çıktısı ([[{t,s,e,hl}]]); data.ts: `captionChunks: Word[][] = [...]` satırı.
Kapı: eşleşen kelimelerde başlangıç farkının p95'i <= --esik-kare kare ve eşleşme oranı >= %90 → GEÇTİ.
Pilot v2 ölçümü (2026-10-26): 26/26 eşleşme, ort 9 ms, maks 40 ms.
Yalnız standart kütüphane.
"""
import argparse, difflib, json, re, sys


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("whisper"); ap.add_argument("altyazi")
    ap.add_argument("--fps", type=float, default=30); ap.add_argument("--esik-kare", type=float, default=2)
    a = ap.parse_args()
    t = open(a.altyazi, encoding="utf-8").read()
    if a.altyazi.endswith(".ts"):
        m = re.search(r"captionChunks[^=]*=\s*(\[.*?\]);\s*$", t, re.M | re.S)
        if not m:
            sys.exit("HATA: data.ts içinde captionChunks bulunamadı")
        t = m.group(1)
    W = [w for c in json.loads(t) for w in c]
    R = json.load(open(a.whisper, encoding="utf-8"))["words"]
    n = lambda s: re.sub(r"[^a-z0-9]", "", s.lower())
    sm = difflib.SequenceMatcher(a=[n(w["t"]) for w in W], b=[n(r["w"]) for r in R], autojunk=False)
    fark = []
    for blk in sm.get_matching_blocks():
        for k in range(blk.size):
            w, r = W[blk.a + k], R[blk.b + k]
            fark.append((w["t"], w["s"] - r["s"]))
    if not fark:
        sys.exit("HATA: eşleşen kelime yok")
    ab = sorted(abs(x) for _, x in fark)
    p95 = ab[min(len(ab) - 1, int(0.95 * len(ab)))]
    oran = len(fark) / max(len(W), 1)
    print(f"altyazi_kelime={len(W)} whisper_kelime={len(R)} eslesen={len(fark)} (%{oran*100:.0f}) "
          f"ort={sum(ab)/len(ab)*1000:.0f} ms p95={p95*1000:.0f} ms maks={ab[-1]*1000:.0f} ms")
    kotu = [(k, round(x * 1000)) for k, x in fark if abs(x) > a.esik_kare / a.fps]
    if kotu:
        print("eşik üstü:", kotu[:20])
    ok = p95 <= a.esik_kare / a.fps and oran >= 0.9
    print("GEÇTİ" if ok else "KALDI")
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
