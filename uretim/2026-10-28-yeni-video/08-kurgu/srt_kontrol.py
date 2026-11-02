#!/usr/bin/env python3
"""SRT kapısı (kurgu-editoru, F7): biçim + okunabilirlik + son videonun sesine hiza.

Kullanım: python3 srt_kontrol.py <altyazi.srt> <render-whisper.json> [--sure <video sn>] [--ref <referans-metni.txt>]
Kontroller:
  1. Biçim: sıra numarası ardışık, zaman biçimi, bitiş > başlangıç, çakışma yok, son blok video süresini aşmıyor.
  2. Okunabilirlik: satır ≤42 karakter, blok ≤2 satır, süre 0.7–7 sn, okuma hızı ≤21 karakter/sn (YouTube/Netflix ölçütü).
  3. Hiza: her bloğun ilk ve son kelimesi render sesinin Whisper kelime zamanlarıyla eşlenir (difflib, normalize kelime);
     başlangıç farkı (blok başı − kelime başı) ve bitiş farkı; kapı: eşleşen blokların p95 |başlangıç farkı| ≤150 ms
     ve eşleşme oranı ≥%90. Rastgele 20 blok örneği (tohum 7) ayrıca listelenir.
  4. Metin: SRT kelimeleri referans metinle (normalize) karşılaştırılır → yazım farkı sayısı (0 olmalı).
Yalnız standart kütüphane.
"""
import argparse, difflib, json, random, re, sys


def zs(s):
    h, m, r = s.split(":"); sn, ms = r.split(",")
    return int(h) * 3600 + int(m) * 60 + int(sn) + int(ms) / 1000


def oku(yol):
    bloklar = []
    for parca in re.split(r"\n\s*\n", open(yol, encoding="utf-8").read().strip()):
        sat = parca.strip().split("\n")
        m = re.match(r"(\d\d:\d\d:\d\d,\d\d\d) --> (\d\d:\d\d:\d\d,\d\d\d)$", sat[1].strip())
        bloklar.append({"no": int(sat[0]), "bas": zs(m.group(1)), "son": zs(m.group(2)), "satirlar": sat[2:]})
    return bloklar


n = lambda s: re.sub(r"[^a-z0-9]", "", s.lower())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("srt"); ap.add_argument("whisper"); ap.add_argument("--sure", type=float); ap.add_argument("--ref")
    a = ap.parse_args()
    B = oku(a.srt)
    hata = []
    for i, b in enumerate(B):
        if b["no"] != i + 1: hata.append(f"sıra {b['no']}≠{i+1}")
        if b["son"] <= b["bas"]: hata.append(f"#{b['no']} bitiş≤başlangıç")
        if i and b["bas"] < B[i - 1]["son"]: hata.append(f"#{b['no']} çakışma")
    if a.sure and B[-1]["son"] > a.sure + 0.01: hata.append(f"son blok {B[-1]['son']} > video {a.sure}")
    uzun = [b["no"] for b in B if any(len(s) > 42 for s in b["satirlar"]) or len(b["satirlar"]) > 2]
    sure = [b["no"] for b in B if not (0.7 <= b["son"] - b["bas"] <= 7.0)]
    cps = [(b["no"], round(len(" ".join(b["satirlar"])) / (b["son"] - b["bas"]), 1)) for b in B]
    hizli = [c for c in cps if c[1] > 21]
    # hiza
    W = json.load(open(a.whisper))["words"]
    wk = [n(w.get("w", w.get("word", ""))) for w in W]
    sk, sidx = [], []
    for bi, b in enumerate(B):
        for k in " ".join(b["satirlar"]).split():
            sk.append(n(k)); sidx.append(bi)
    sm = difflib.SequenceMatcher(a=sk, b=wk, autojunk=False)
    es = {}
    for blok in sm.get_matching_blocks():
        for j in range(blok.size):
            es[blok.a + j] = blok.b + j
    ilk = {}; son = {}
    for i, bi in enumerate(sidx):
        ilk.setdefault(bi, i); son[bi] = i
    fark = []; farkson = []
    for bi, b in enumerate(B):
        i = ilk[bi]
        if i in es:
            w = W[es[i]]; fark.append((b["no"], round((b["bas"] - w.get("s", w.get("start"))) * 1000)))
        j = son[bi]
        if j in es:
            w = W[es[j]]; farkson.append((b["no"], round((b["son"] - w.get("e", w.get("end"))) * 1000)))
    mut = sorted(abs(f) for _, f in fark)
    p95 = mut[int(0.95 * (len(mut) - 1))] if mut else None
    oran = len(fark) / len(B)
    random.seed(7)
    ornek = sorted(random.sample(fark, min(20, len(fark))))
    yazim = None
    if a.ref:
        rk = [n(x) for x in open(a.ref, encoding="utf-8").read().split()]
        rk = [x for x in rk if x]; skk = [x for x in sk if x]
        op = difflib.SequenceMatcher(a=rk, b=skk, autojunk=False).get_opcodes()
        yazim = [(t, rk[i1:i2], skk[j1:j2]) for t, i1, i2, j1, j2 in op if t != "equal"]
    sonuc = {"blok": len(B), "bicim_hata": hata, "uzun_satir": uzun, "sure_disi": sure, "hizli_cps>21": hizli,
             "cps_maks": max(c[1] for c in cps), "hiza_eslesen": len(fark), "hiza_oran": round(oran, 3),
             "bas_fark_p95_ms": p95, "bas_fark_ort_ms": round(sum(f for _, f in fark) / len(fark)),
             "bas_fark_maks": max(fark, key=lambda x: abs(x[1])), "son_fark_p95_ms": sorted(abs(f) for _, f in farkson)[int(0.95 * (len(farkson) - 1))],
             "ornek_20": ornek, "yazim_farki": yazim}
    gecti = not hata and not uzun and p95 is not None and p95 <= 150 and oran >= 0.9 and (yazim is None or not yazim)
    sonuc["KAPI"] = "GEÇTİ" if gecti else "KALDI"
    print(json.dumps(sonuc, ensure_ascii=False, indent=1))
    sys.exit(0 if gecti else 1)


if __name__ == "__main__":
    main()
