#!/usr/bin/env python3
"""viralite-analisti: model v0.1 kurallarinin 90 gunluk nis verisiyle (delta90, n=959) testi.
Kullanim: python3 kalibrasyon90.py ../../01-arastirma/olcum/delta90-2026-11-04.json ../../01-arastirma/olcum/haric.txt
Nis filtresi desen90.py ile birebir ayni. Cikti deterministik (siralama sabit)."""
import json, re, statistics, sys
d = json.load(open(sys.argv[1]))
H = set(open(sys.argv[2]).read().split("\n")) - {""}
r = [x for x in d["videolar_90g"] if not any(x["kanal"].startswith(h) for h in H) and x["yas_gun"] >= 7
     and x["kanal_medyan"] >= 1000 and not re.search(r"[ऀ-෿؀-ۿ]", x["baslik"])]
r.sort(key=lambda x: x["id"])
print(f"nis n={len(r)} kanal={len({x['kanal'] for x in r})} | tum medyan={statistics.median(x['skor_med'] for x in r):.2f}")
def rap(ad, f):
    a = [x["skor_med"] for x in r if f(x)]; b = [x["skor_med"] for x in r if not f(x)]
    if len(a) < 3: print(f"{ad:38} n={len(a)} (az)"); return
    print(f"{ad:38} n={len(a):>3} med={statistics.median(a):4.2f} >=3x={sum(v>=3 for v in a)/len(a):4.0%} >=10x={sum(v>=10 for v in a):>2} | degil n={len(b):>3} med={statistics.median(b):4.2f} >=3x={sum(v>=3 for v in b)/len(b):4.0%}")
T = lambda p: (lambda x: re.search(p, x["baslik"], re.I))
# 1) somut ozne tavani (v0.1 kural 1): kisi/ulke/sehir/kurum/sirket/nesne
ULKE = r"america|\bu\.?s\.?a?\b|china|chinese|france|japan|russia|europe|\buk\b|britain|germany|canada|india|saudi|mexico|argentina|venezuela|greece|italy|spain|switzerland|dubai|singapore|korea|brazil|iran|israel|turkey|africa|norway|sweden|australia|chile|egypt|rome|roman|soviet|ottoman"
KISI = r"trump|musk|buffett|bezos|hitler|napoleon|rockefeller|morgan|madoff|burry|powell|biden|putin|xi\b|zuckerberg|altman|jobs\b|newton|mansa|vanderbilt|carnegie|ford\b|keynes|marx|elon"
KURUM = r"fed\b|federal reserve|nvidia|apple|google|amazon|tesla|openai|microsoft|walmart|costco|mcdonald|disney|netflix|boeing|intel|meta\b|bank of|wall street|imf|nasdaq|s&p|dow\b|blackrock|harvard|nfl|subway|starbucks|ikea|lego|nike|coca|pepsi"
NESNE = r"gold|silver|oil|bitcoin|crypto|dollar|euro|yen|house|housing|home|egg|coffee|beef|car\b|cars\b|diamond|tulip|chocolate|rice|buffet|noodle|island|empire|city|town|mall|airport|railroad|ship"
SOMUT = "|".join([ULKE, KISI, KURUM, NESNE])
rap("somut ozne (ulke|kisi|kurum|nesne)", T(SOMUT))
rap("  yalniz ulke", T(ULKE)); rap("  yalniz kisi", T(KISI)); rap("  yalniz kurum", T(KURUM)); rap("  yalniz nesne", T(NESNE))
# 2) merak kaliplari
rap("paradoks (so why|why hasn't|...but|yet)", T(r"so why|why hasn'?t|why isn'?t|\.\.\..*\?|\byet\b"))
rap("what happens if/when", T(r"what happens|what if|^if "))
rap("tarih->gelecek", T(r"before a|last time|always happens|prediction|about to|next\b|is coming|will (change|be|burst|collapse)"))
rap("gizli is modeli", T(r"actually make money|economics of|business model|make money\?"))
# 3) zamanlama vekili: gundem kelimesi
rap("gundem (ai|trump|tariff|midterm|2026|2027|fed|crash now)", T(r"\bai\b|trump|tariff|midterm|2026|2027|\bfed\b|right now|just\b"))
rap("tarihsel (history|19xx|ancient|empire|ww)", T(r"history|\b1[5-9]\d\d\b|ancient|empire|world war|medieval|roman|century"))
# 4) seri
rap("seri isareti (part|ep|episode|#n)", T(r"\bpart\b|\bep\.?\s*\d|episode|#\d"))
# 5) milyon taban orani (kanal buyuklugune gore, nis, 90 g)
print("\nMilyon taban orani (nis, 90 g, >=7 gunluk):")
for lo, hi in [(0, 1e4), (1e4, 5e4), (5e4, 2e5), (2e5, 1e6), (1e6, 1e10)]:
    g = [x for x in r if lo <= x["abone"] < hi]
    if g: print(f"  abone {int(lo):>8}-{int(hi):<10} n={len(g):>3} >=1M={sum(x['izlenme']>=1e6 for x in g):>2} ({sum(x['izlenme']>=1e6 for x in g)/len(g):.1%}) >=100K={sum(x['izlenme']>=1e5 for x in g):>3} ({sum(x['izlenme']>=1e5 for x in g)/len(g):.1%}) maks={max(x['izlenme'] for x in g):>9}")
allv = [x for x in d["videolar_90g"] if x["yas_gun"] >= 7]
g = [x for x in allv if x["abone"] < 1e4]
print(f"  TUM ornek (nis disi dahil) abone<10K n={len(g)} >=1M={sum(x['izlenme']>=1e6 for x in g)} >=100K={sum(x['izlenme']>=1e5 for x in g)} maks={max(x['izlenme'] for x in g)}")
