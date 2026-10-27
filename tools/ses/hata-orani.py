#!/usr/bin/env python3
"""Kelime hata oranı (WER): senaryo metni vs Whisper çıktısı.

Kullanım: python3 tools/ses/hata-orani.py <ref.txt> <whisper.json>
Normalizasyon (iki tarafa aynı): küçük harf, kısaltmalar açılır (you'll → you will ...), rakamlar İngilizce
kelimeye çevrilir (150 → one hundred fifty, 1,000 → one thousand, 1923 → nineteen twenty three, 2008 → two thousand
eight, 5% → five percent, $5 → five dollars), "and" sayı içinde atılır, noktalama silinir.
2026-10-26: TTS metni "one hundred and fifty" iken Whisper "150" yazıyordu → sahte hata (WER kapısını şişirir).
2026-10-27 (1929-1000-dolar F4: 45 hatanın 41'i normalizasyon artığıydı) eklendi:
  - sıra sayıları: 3rd/28th/1st ↔ third/twenty eighth/first; ay + gün rakamı (January 1 / March 4) → ordinal (first/fourth)
  - on yıllar: 1930s / '30s ↔ nineteen thirties / thirties
  - para biçimi (kanonik, yalnız norm(); hizalayıcılar norm_alt() kullanır): sayıdan sonra "dollar(s)" atılır,
    baştaki "one"/"a" + hundred/thousand/... atılır, "twelve hundred" = "one thousand two hundred",
    "point five" = "and a half" → "$1,000" = "one thousand dollars" = "1000 dollars" = "a thousand" = "thousand dollars";
    "$1,270" = "twelve hundred seventy"; "1500 dollars" yıl sanılmaz.
  - kesme işareti birleştirilir (Leo's = Leos, doesn't = doesnt): sesçe aynı, TTS hatası değil.
  Seçenekler: A) sayı kelime dizisini tamsayıya çözmek (her biçim tek değer; ama "nineteen twenty nine" yıl/sayı
  belirsiz, yanlış çözüm sessizce hata gizler) — elendi; B) belirli eşdeğerlik kuralları (seçilen: her kural test
  edilebilir, tools/ses/test_hata_orani.py). Bedel: anlatıcı "dollars" kelimesini atlarsa sayılmaz (TTS'te kabul).
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


SIRA_OZEL = {"one": "first", "two": "second", "three": "third", "five": "fifth", "eight": "eighth", "nine": "ninth", "twelve": "twelfth"}
AYLAR = "january february march april may june july august september october november december"


def sira(n):
    w = soz(n).split()
    w[-1] = SIRA_OZEL.get(w[-1]) or (w[-1][:-1] + "ieth" if w[-1].endswith("y") else w[-1] + "th")
    return " ".join(w)


def cogul(metin):
    w = metin.split()
    w[-1] = w[-1][:-1] + "ies" if w[-1].endswith("y") else w[-1] + "s"
    return " ".join(w)


def sayi(m, eski=False):
    t = m.group(0)
    dolar = t.startswith("$"); yuzde = t.endswith("%")
    t = t.strip("$%").replace(",", "")
    if "." in t:
        a, b = t.split(".", 1)
        s = soz(int(a or 0)) + " point " + " ".join(BIR[int(c)] for c in b)
    else:
        n = int(t)
        para_sonra = not eski and re.match(r"\s*(dollars?|bucks|usd)\b", m.string[m.end():])
        s = yil(n) if (yil_mi(n) and not dolar and not yuzde and not para_sonra and "," not in m.group(0)) else soz(n)
    return " " + s + (" percent" if yuzde else "") + (" dollars" if dolar else "") + " "


def norm_alt(s, eski=False):
    """Alt-kelime normalizasyonu (hizalayıcılar için; kelime kelime çağrılır, bağlam kuralı yok).
    eski=True: 2026-10-26 davranışı birebir (kilitli videoların hizalama çıktısı bayt bayt yeniden üretilsin diye)."""
    s = s.lower()
    for a, b in (("you'll", "you will"), ("we'll", "we will"), ("that's", "thats"), ("it's", "its")):
        s = s.replace(a, b)
    if eski:
        s = re.sub(r"\$(\d[\d,.]*)\s+(thousand|million|billion|trillion)\b", r"\1 \2 dollars", s)
        s = re.sub(r"\$?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?%?", lambda m: sayi(m, True), s)
        s = re.sub(r"(?<=\w)-(?=\w)", " ", s)
        w = re.sub(r"[^a-z0-9 ]", " ", s).split()
        return [x for i, x in enumerate(w) if not (x == "and" and 0 < i < len(w) - 1 and w[i - 1] in SAYI_KELIME and w[i + 1] in SAYI_KELIME)]
    s = s.replace("\u2019", "'")
    s = re.sub(r"\b(\d+)(?:st|nd|rd|th)\b", lambda m: " " + sira(int(m.group(1))) + " ", s)
    s = re.sub(r"\b(\d{3}0)'?s\b", lambda m: " " + cogul(yil(int(m.group(1)))) + " ", s)
    s = re.sub(r"(?<![\w])'(\d0)s\b", lambda m: " " + cogul(soz(int(m.group(1)))) + " ", s)
    s = re.sub(r"\b(" + AYLAR.replace(" ", "|") + r")\s+(\d{1,2})\b(?![.,]?\d)",
               lambda m: m.group(1) + " " + (sira(int(m.group(2))) if 1 <= int(m.group(2)) <= 31 else m.group(2)), s)
    s = re.sub(r"\$(\d[\d,.]*)\s+(thousand|million|billion|trillion)\b", r"\1 \2 dollars", s)
    s = re.sub(r"\$?(?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?%?", sayi, s)
    s = re.sub(r"(?<=\w)-(?=\w)", " ", s)
    s = re.sub(r"(?<=[a-z])'(?=[a-z])", "", s)
    w = re.sub(r"[^a-z0-9 ]", " ", s).split()
    # sayı içindeki "and" (one hundred and fifty) atılır
    return [x for i, x in enumerate(w) if not (x == "and" and 0 < i < len(w) - 1 and w[i - 1] in SAYI_KELIME and w[i + 1] in SAYI_KELIME)]


BASAMAK = {"hundred", "thousand", "million", "billion", "trillion"}


def kanonik(w):
    """Bağlamlı eşdeğerlikler (tam metinde): twelve hundred → one thousand two hundred, point five → and a half,
    baştaki one/a + basamak atılır, sayıdan sonra dollar(s) atılır."""
    o, i = [], 0
    while i < len(w):
        x = w[i]; onceki = o[-1] if o else ""; sonraki = w[i + 1] if i + 1 < len(w) else ""
        if x in BIR[11:20] and sonraki == "hundred" and onceki not in SAYI_KELIME:
            o += ["one", "thousand", BIR[BIR.index(x) - 10]]
        elif x == "point" and sonraki == "five" and onceki in SAYI_KELIME and (i + 2 >= len(w) or w[i + 2] not in BIR):
            o += ["and", "a", "half"]; i += 1
        else:
            o.append(x)
        i += 1
    s = []
    for i, x in enumerate(o):
        sonraki = o[i + 1] if i + 1 < len(o) else ""
        onceki = s[-1] if s else ""
        if x in ("one", "a") and sonraki in BASAMAK and onceki not in SAYI_KELIME:
            continue
        if x in ("dollar", "dollars") and (onceki in SAYI_KELIME or onceki == "half"):
            continue
        s.append(x)
    return s


def norm_eski(s):
    return norm_alt(s, eski=True)


def norm(s):
    """WER normalizasyonu: norm_alt + bağlamlı kanonik kurallar (iki tarafa aynı uygulanır)."""
    return kanonik(norm_alt(s))


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
