#!/usr/bin/env python3
"""Kelime hata oranı (WER): senaryo metni vs Whisper çıktısı.

Kullanım: python3 tools/ses/hata-orani.py <ref.txt> <whisper.json>
Normalizasyon (iki tarafa aynı): küçük harf, kısaltmalar açılır (you'll → you will ...), rakamlar İngilizce
kelimeye çevrilir (150 → one hundred fifty, 1,000 → one thousand, 1923 → nineteen twenty three, 2008 → two thousand
eight, 5% → five percent, $5 → five dollars), "and" sayı içinde atılır, noktalama silinir.
2026-10-26: TTS metni "one hundred and fifty" iken Whisper "150" yazıyordu → sahte hata (WER kapısını şişirir).
Yalnız standart kütüphane.
"""
import difflib, json, re, sys

BIR = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
ON = "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()
BUYUK = [(10 ** 12, "trillion"), (10 ** 9, "billion"), (10 ** 6, "million"), (1000, "thousand"), (100, "hundred")]
SAYI_KELIME = set(BIR) | set(ON[2:]) | {"hundred", "thousand", "million", "billion", "trillion"}


def soz(n):
    if n < 20:
        return BIR[n]
    if n < 100:
        return ON[n // 10] + ("" if n % 10 == 0 else " " + BIR[n % 10])
    for v, ad in BUYUK:
        if n >= v:
            return soz(n // v) + " " + ad + ("" if n % v == 0 else " " + soz(n % v))


def yil_mi(n):
    return 1100 <= n <= 2099 and len(str(n)) == 4


def yil(n):
    if 2000 <= n <= 2009:
        return soz(n)
    bas, son = divmod(n, 100)
    return soz(bas) + (" hundred" if son == 0 else (" oh " + BIR[son] if son < 10 else " " + soz(son)))


def sayi(m):
    t = m.group(0)
    dolar = t.startswith("$"); yuzde = t.endswith("%")
    t = t.strip("$%").replace(",", "")
    if "." in t:
        a, b = t.split(".", 1)
        s = soz(int(a or 0)) + " point " + " ".join(BIR[int(c)] for c in b)
    else:
        n = int(t)
        s = yil(n) if (yil_mi(n) and not dolar and not yuzde and "," not in m.group(0)) else soz(n)
    return " " + s + (" percent" if yuzde else "") + (" dollars" if dolar else "") + " "


def norm(s):
    s = s.lower()
    for a, b in (("you'll", "you will"), ("we'll", "we will"), ("that's", "thats"), ("it's", "its")):
        s = s.replace(a, b)
    s = re.sub(r"\$(\d[\d,.]*)\s+(thousand|million|billion|trillion)\b", r"\1 \2 dollars", s)
    s = re.sub(r"\$?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?%?", sayi, s)
    s = re.sub(r"(?<=\w)-(?=\w)", " ", s)
    w = re.sub(r"[^a-z0-9 ]", " ", s).split()
    # sayı içindeki "and" (one hundred and fifty) atılır
    return [x for i, x in enumerate(w) if not (x == "and" and 0 < i < len(w) - 1 and w[i - 1] in SAYI_KELIME and w[i + 1] in SAYI_KELIME)]


def main():
    ref = open(sys.argv[1], encoding="utf-8").read(); hyp = json.load(open(sys.argv[2], encoding="utf-8"))["text"]
    r, h = norm(ref), norm(hyp)
    d = list(range(len(h) + 1))
    for i in range(1, len(r) + 1):
        onceki, d[0] = d[0], i
        for j in range(1, len(h) + 1):
            onceki, d[j] = d[j], min(d[j] + 1, d[j - 1] + 1, onceki + (r[i - 1] != h[j - 1]))
    print(f"kelime={len(r)} hata={d[-1]} WER=%{d[-1] / max(len(r), 1) * 100:.1f}")
    sm = difflib.SequenceMatcher(a=r, b=h, autojunk=False)
    for op, a1, a2, b1, b2 in sm.get_opcodes():
        if op != "equal":
            print(op, " ".join(r[a1:a2]), "->", " ".join(h[b1:b2]))


if __name__ == "__main__":
    main()
