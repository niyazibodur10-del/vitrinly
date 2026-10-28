#!/usr/bin/env python3
"""F3 doğrulama kapısı (finans-dogrulayici).
metin.md'deki ANLATIM (yazıyla sayılar), GÖRSEL (rakamlar) ve Shorts satırlarından
bütün sayıları çıkarır; her birini dogrulama.md'deki iddia tablosunun ID'sine eşler.
Eşlenmeyen sayı = KAPI KALDI.  Kullanım: python3 -I dogrulama-kontrol.py metin.md
"""
import re, sys, collections

UNITS = {w: i for i, w in enumerate(
    "zero one two three four five six seven eight nine ten eleven twelve thirteen "
    "fourteen fifteen sixteen seventeen eighteen nineteen".split())}
TENS = {w: 10 * i for i, w in enumerate(
    "_ _ twenty thirty forty fifty sixty seventy eighty ninety".split()) if w != "_"}
ORD = {"first": 1, "second": 2, "third": 3, "fourth": 4, "fifth": 5, "sixth": 6, "seventh": 7,
       "eighth": 8, "ninth": 9, "tenth": 10, "eleventh": 11, "twelfth": 12}
PLUR = {"twenties": 20, "thirties": 30, "forties": 40, "fifties": 50}
NUMW = set(UNITS) | set(TENS) | {"hundred", "hundreds", "thousand", "thousands", "point", "half"} | set(ORD) | set(PLUR)


def small(toks):
    """'twenty','eight' / 'twenty-eight' / 'eleven' -> int (0-99)."""
    v = 0
    for t in toks:
        if t in TENS: v += TENS[t]
        elif t in UNITS: v += UNITS[t]
        elif t in ORD: v += ORD[t]
        elif t in PLUR: v += PLUR[t]
    return v


def parse(span):
    toks = [t for t in re.split(r"[\s\-]+", span.lower()) if t]
    # yıl: "nineteen twenty-nine", "twenty twenty-six"
    if len(toks) >= 2 and toks[0] in ("nineteen", "twenty") and "hundred" not in toks and "thousand" not in toks \
            and "point" not in toks and (toks[1] in TENS or toks[1] in PLUR):
        return 100 * UNITS.get(toks[0], 20 if toks[0] == "twenty" else 0) + small(toks[1:]) if toks[0] == "nineteen" \
            else 2000 + small(toks[1:])
    if "point" in toks:
        i = toks.index("point")
        whole = parse(" ".join(toks[:i]))
        dec = "".join(str(UNITS[t]) for t in toks[i + 1:] if t in UNITS)
        return float(f"{whole}.{dec}")
    total, cur = 0, 0
    half = "half" in toks
    for t in toks:
        if t in UNITS: cur += UNITS[t]
        elif t in TENS: cur += TENS[t]
        elif t in ORD: cur += ORD[t]
        elif t in ("hundred", "hundreds"): cur = (cur or 1) * 100
        elif t in ("thousand", "thousands"): total += (cur or 1) * 1000; cur = 0
    v = total + cur
    return v + 0.5 if half else v


SPAN = re.compile(r"\b(?:(?:%s)(?![a-z])(?:[\s\-]+(?:and[\s\-]+(?:a[\s\-]+)?)?)?)+" % "|".join(sorted(NUMW, key=len, reverse=True)), re.I)


def words_numbers(text):
    out = []
    for m in SPAN.finditer(text):
        s = m.group(0).strip(" -")
        s = re.sub(r"\s+and(\s+a)?$", "", s)
        if not s or s.lower() in ("point", "half", "second"):
            continue
        out.append((s, parse(s)))
    return out


DIG = re.compile(r"(?<![A-Za-z0-9_])[−\-+~≈]?\$?\d[\d,]*(?:\.\d+)?%?")

CLEAN = re.compile(r"↺ ?\d+:\d\d|\d+:\d\d|\[[^\]]*\]|\b(?:BEA|BLS|FRH|FDIC|HUL|FRED)-?[A-Z0-9-]*|Table 6\.6A|Tablo 5|\b[A-ZÖ]{1,2}\d+[a-z]?\b|×\d|\d+ (?:sn|kelime|madeni|kişi)\b|\(K\d\)|ikiye|\b\d+'(?:d[ae]|t[ae]|[iıuü]n?)\b")

# Eşleme: değer -> iddia ID (dogrulama.md §2). Yapısal sayılar (oyun kuralı, sahne no) "Y".
ANLATIM_MAP = {
    1929: "T01", 1933: "T01", 1921: "C03", 1930: "C10", 1932: "C19", 1934: "C26", 1936: "C21", 1954: "C20",
    2022: "C32", 2025: "C30", 2026: "C30",
    1000: "C01", 1430: "C02", 8: "C02/C04/C19", 63: "C03", 381: "C04", 381.17: "C05", 6: "C04",
    10: "C06/C08", 28: "C07", 13: "C07", 12: "C07/C30", 500: "C08", 3: "C05/Y",
    16000: "C11", 8000: "C11", 11: "C12", 4: "C12/C24", 9000: "C13", 20: "C15", 200: "C16", 800: "C16",
    30: "C18", 21: "C17", 1270: "C17", 41.22: "C19", 89: "C19", 108: "C19", 138: "C19",
    7: "C21", 4000: "C25", 2500: "C26", 9: "C27", 3.7: "C30", 964: "C31", 27: "C32", 13.5: "C32",
    250000: "C33", 1: "Y/C26", 2: "Y/C26", 100: "C10",
}
# GÖRSEL: ekrandaki rakam -> iddia ID (Y = yapısal: sahne/poz/kural no, kendi kurgumuz)
GORSEL_MAP = {
    "1929": "T01", "$1,000": "C01", "1,000": "C01", "1.000": "C01", "2026": "C30", "$1,430": "C02", "12": "C02",
    "8": "C02", "1": "Y", "2": "Y", "3": "C05", "3,": "C05", "1921": "C03", "63": "C03", "381.17": "C05",
    "381": "C04", "10%": "C06", "90%": "C06", "28": "C07", "29": "C07", "−13%": "C07", "−12%": "C07",
    "~500": "C08", "~$500": "C08", "−50%": "C08", "~10": "C08", "≈24.000": "C14", "1930": "C10",
    "8,000": "C11", "~16,000": "C11", "11,": "C12", "9": "C27", "10": "Y", "1933": "T01", "506": "C13",
    "366": "C13", "646": "C13", "775": "C13", "617": "C13", "975": "C13", "669": "C13", "498": "C13",
    "659": "C13", "1,350": "C13", "2,293": "C13", "1,453": "C13", "4,000": "C13/C25", "≈9,100": "C13",
    "~9,000": "C13", "~20": "C15", "$1": "C15", "1,34": "C15", "6,83": "C15", "~$800": "C16",
    "17.3": "C17", "1932": "C19", "13.6": "C17", "12.6": "C32", "1,272": "C17", "$1,272": "C17",
    "1,373": "C32", "−21%": "C17", "~30%": "C18", "0%": "Y", "41.22": "C19", "1954": "C20", "108": "C19",
    "$108": "C19", "~$138": "C19", "1936": "C21", "2009": "C21", "8,": "C19", "−89%": "C19",
    "4": "C24", "6": "C26", "~4,000": "C25", "16,": "C26", "1,": "C26", "1934": "C26", "$2,500": "C26",
    "+3.7%": "C30", "$964": "C31", "100": "C32", "72.8": "C32", "−27.2%": "C32", "2022": "C32",
    "113.5": "C32", "+13.5%": "C32", "881": "C32", "$250,000": "C33", "33": "C13", "5": "Y", "7": "Y",
    "26": "C32",
    # RED-1 sonrası (2026-10-27): doğrulayıcının kendi verdiği değerler
    "≈299,": "C06b", "≈299": "C06b",   # S06 görsel notu: 28 Eki öncesi kapanış 298,97 (D-2)
    "61": "C27",                         # S19 G2: 1934 toplam askıya alma 9 + 52 (D-5)
    "42": "C32", "48": "C32",            # S21 G5 eksen: Eyl 1929→Mar 1933 = 42 ay, Eyl 2022→Eyl 2026 = 48 ay (Ö-1)
}
VALID_SMALL_STRUCT = {"one", "two", "three"}  # "three doors", "one door", "two answers": yapı


def main(path):
    md = open(path, encoding="utf-8").read()
    body = md.split("## 3. Retention haritası")[0]
    rows = []
    scene = None
    for line in body.splitlines():
        h = re.match(r"### (S\d\d)", line)
        if h: scene = h.group(1); continue
        if scene and line.startswith("| ") and not line.startswith("| ANLATIM") and not line.startswith("|---"):
            cells = [c.strip() for c in line.strip().strip("|").split(" | ")]
            if len(cells) >= 2:
                rows.append((scene, cells[0], " | ".join(cells[1:])))
    shorts = re.findall(r"\*\*(?:Kendi hook'u|Kapanış satırı)[^:]*:\*\* \"([^\"]+)\"", md)
    # RED-1 sonrası: Shorts'un okunacak tam metni de taranır (kesit sınırları değişti)
    shorts += re.findall(r"\*\*Okunacak tam metin[^:]*:\*\* <<([^>]+)>>", md)

    unmapped, cnt = [], collections.Counter()
    print("## ANLATIM (yazıyla sayılar)")
    for sc, an, _ in rows:
        for raw, val in words_numbers(an):
            key = int(val) if float(val).is_integer() else val
            tag = ANLATIM_MAP.get(key)
            if raw.lower() == "thousands":  # S10 "Thousands never did." (D-3) -> FDIC "About 4,000 banks never reopened"
                tag = "C22/C25"
            if tag is None and raw.lower() in VALID_SMALL_STRUCT:
                tag = "Y"
            cnt["anlatim"] += 1
            print(f"{sc}\t{raw!r}\t{val}\t{tag or 'EŞLENMEDİ'}")
            if tag is None: unmapped.append((sc, raw, val))
    print("\n## SHORTS satırları")
    for s in shorts:
        for raw, val in words_numbers(s):
            key = int(val) if float(val).is_integer() else val
            tag = ANLATIM_MAP.get(key) or ("Y" if raw.lower() in VALID_SMALL_STRUCT else None)
            cnt["shorts"] += 1
            print(f"Shorts\t{raw!r}\t{val}\t{tag or 'EŞLENMEDİ'}")
            if tag is None: unmapped.append(("Shorts", raw, val))
    print("\n## GÖRSEL (rakamlar, benzersiz)")
    gv = collections.OrderedDict()
    for sc, _, gs in rows:
        gs = CLEAN.sub(" ", gs)
        for m in DIG.finditer(gs):
            tok = m.group(0)
            gv.setdefault(tok, []).append(sc)
    for tok, scs in gv.items():
        cnt["gorsel"] += 1
        tag = GORSEL_MAP.get(tok)
        print(f"{tok}\t{','.join(sorted(set(scs)))}\t{tag or 'EŞLENMEDİ'}")
        if tag is None: unmapped.append(("GÖRSEL/" + ",".join(sorted(set(scs))), tok, None))
    print(f"\nSayım: ANLATIM {cnt['anlatim']} · Shorts {cnt['shorts']} · GÖRSEL benzersiz {cnt['gorsel']}")
    print(f"Eşlenmeyen (ANLATIM+Shorts+GÖRSEL): {len(unmapped)}")
    for u in unmapped: print("  EŞLENMEDİ", u)
    return gv, unmapped


if __name__ == "__main__":
    gv, un = main(sys.argv[1] if len(sys.argv) > 1 else "metin.md")
    sys.exit(1 if un else 0)
