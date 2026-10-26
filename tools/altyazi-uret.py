#!/usr/bin/env python3
"""Whisper kelime zamanları + senaryo metni -> YouTube SRT + Remotion kelime kelime altyazı verisi (JSON).

Kullanım:
  python3 tools/altyazi-uret.py <kelimeler.json> <metin.txt> --srt cikis.en.srt [--json altyazi.json]
         [--ofset 1.0] [--vurgu "savings,coffee"] [--parca-kelime 4] [--srt-karakter 42] [--srt-sn 6]

- Görünen metin senaryodan gelir (Whisper noktalama/yazım değiştirebilir); zaman Whisper'dan.
  Hizalama difflib ile yapılır → WER > 0 olsa da çalışır; eşleşmeyen senaryo kelimeleri komşu
  kelimelerin arasına doğrusal yerleştirilir (rapor: kaç kelime tahmini zamanlı).
- --ofset: miksteki anlatım başlangıcı (miks.py --giris), saniye.
- SRT bloğu: en çok --srt-karakter karakter/satır, 2 satır, --srt-sn sn; cümle sonunda ve >=0.6 sn boşlukta biter.
- JSON (Remotion `captionChunks` ile aynı şekil: [[{t,s,e,hl}]]): 1..--parca-kelime kelimelik parçalar,
  noktalamada ve >=0.35 sn boşlukta bölünür. hl = --vurgu listesindeki kelime veya rakam içeren kelime.
Elenen: elle gruplama (pilot v2 veri-uret.py; 12 dk/≈1800 kelimede ölçeklenmez), Whisper metnini doğrudan
göstermek (noktalama/"1923" gibi yazımlar bozulabiliyor).
Bağımlılık: yalnız standart kütüphane.
"""
import argparse, difflib, json, re, sys


def norm(w):
    return re.sub(r"[^a-z0-9]", "", w.lower())


def hizala(gorunen, whisper):
    a = [norm(w) for w in gorunen]; b = [norm(w["w"]) for w in whisper]
    zaman = [None] * len(gorunen)
    for op, a1, a2, b1, b2 in difflib.SequenceMatcher(a=a, b=b, autojunk=False).get_opcodes():
        if op == "equal" or (op == "replace" and a2 - a1 == b2 - b1):
            for k in range(a2 - a1):
                zaman[a1 + k] = (whisper[b1 + k]["s"], whisper[b1 + k]["e"])
        elif op == "replace":  # farklı sayıda kelime: whisper aralığını senaryo kelimelerine böl
            s, e = whisper[b1]["s"], whisper[b2 - 1]["e"]; n = a2 - a1
            for k in range(n):
                zaman[a1 + k] = (s + (e - s) * k / n, s + (e - s) * (k + 1) / n)
    tahmini = sum(z is None for z in zaman)
    for i, z in enumerate(zaman):  # eşleşmeyen (silinmiş) kelimeler: komşular arasına
        if z is None:
            onceki = next((zaman[j][1] for j in range(i - 1, -1, -1) if zaman[j]), 0.0)
            sonraki = next((zaman[j][0] for j in range(i + 1, len(zaman)) if zaman[j]), onceki + 0.3)
            zaman[i] = (onceki, max(onceki + 0.05, min(sonraki, onceki + 0.3)))
    return zaman, tahmini


def ts(x):
    ms = int(round(x * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); s, ms = divmod(ms, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"


def srt_bloklari(W, kar, sn):
    bloklar, cur = [], []
    for i, w in enumerate(W):
        cur.append(w)
        metin = " ".join(x["t"] for x in cur)
        sonraki = W[i + 1] if i + 1 < len(W) else None
        bitir = (sonraki is None or w["t"][-1] in ".!?" or (sonraki["s"] - w["e"]) >= 0.6
                 or len(metin + " " + sonraki["t"]) > 2 * kar or sonraki["e"] - cur[0]["s"] > sn)
        if bitir:
            bloklar.append(cur); cur = []
    return bloklar


def iki_satir(kelimeler, kar):
    metin = " ".join(kelimeler)
    if len(metin) <= kar:
        return metin
    best = min(range(1, len(kelimeler)), key=lambda k: abs(len(" ".join(kelimeler[:k])) - len(" ".join(kelimeler[k:]))))
    return " ".join(kelimeler[:best]) + "\n" + " ".join(kelimeler[best:])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("kelimeler"); ap.add_argument("metin")
    ap.add_argument("--srt", required=True); ap.add_argument("--json")
    ap.add_argument("--ofset", type=float, default=0.0); ap.add_argument("--vurgu", default="")
    ap.add_argument("--parca-kelime", type=int, default=4)
    ap.add_argument("--srt-karakter", type=int, default=42); ap.add_argument("--srt-sn", type=float, default=6.0)
    a = ap.parse_args()
    whisper = json.load(open(a.kelimeler, encoding="utf-8"))["words"]
    gorunen = open(a.metin, encoding="utf-8").read().split()
    if not whisper or not gorunen:
        sys.exit("HATA: boş kelime listesi veya metin")
    zaman, tahmini = hizala(gorunen, whisper)
    vurgu = {norm(v) for v in a.vurgu.split(",") if v.strip()}
    W = [{"t": g, "s": round(s + a.ofset, 3), "e": round(e + a.ofset, 3),
          "hl": norm(g) in vurgu or bool(re.search(r"\d", g))} for g, (s, e) in zip(gorunen, zaman)]
    out = []
    for n, b in enumerate(srt_bloklari(W, a.srt_karakter, a.srt_sn), 1):
        out.append(f"{n}\n{ts(b[0]['s'])} --> {ts(b[-1]['e'])}\n{iki_satir([x['t'] for x in b], a.srt_karakter)}\n")
    open(a.srt, "w", encoding="utf-8").write("\n".join(out))
    if a.json:
        parcalar, cur = [], []
        for i, w in enumerate(W):
            cur.append(w)
            sonraki = W[i + 1] if i + 1 < len(W) else None
            if (sonraki is None or len(cur) >= a.parca_kelime or w["t"][-1] in ".,!?;:" or sonraki["s"] - w["e"] >= 0.35):
                parcalar.append(cur); cur = []
        json.dump(parcalar, open(a.json, "w", encoding="utf-8"), ensure_ascii=False)
    print(f"kelime={len(W)} whisper={len(whisper)} tahmini_zamanli={tahmini} srt_blok={len(out)} "
          f"son={W[-1]['e']:.2f} sn" + (f" parca={len(parcalar)}" if a.json else ""))


if __name__ == "__main__":
    main()
