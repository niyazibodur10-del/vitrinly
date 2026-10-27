#!/usr/bin/env python3
"""Metindeki türetilmiş rakamlar [H]. Kullanım: python3 -I hesap.py (bu klasörde)."""
import csv, os
B = os.path.dirname(os.path.abspath(__file__))
d = {}
for f in ("cpi-1928-1934-CPIAUCNS.csv", "cpi-2019-2026-CPIAUCNS.csv"):
    for x in csv.DictReader(open(os.path.join(B, f))):
        if x["CPIAUCNS"]:
            d[x["observation_date"]] = float(x["CPIAUCNS"])
g = lambda y, m: d[f"{y}-{m:02d}-01"]
p = lambda a, b: round((g(*b) / g(*a) - 1) * 100, 1)
alim = lambda a, b: round(1000 * g(*a) / g(*b))
print("Borsa kapisi 1000 x 41.22/381.17 =", round(1000 * 41.22 / 381.17), "| dusus %", round((41.22 / 381.17 - 1) * 100, 1))
print("Borsa kapisi Kasim 1929 'almost half' -> ~", 500)
print("Borsa 108$ 1929 alim gucuyle (Eyl29->Tem32 TUFE):", round(1000 * 41.22 / 381.17 * g(1929, 9) / g(1932, 7)))
print("TUFE Eyl1929->Tem1932 %", p((1929, 9), (1932, 7)), "| 1000$ alim gucu", alim((1929, 9), (1932, 7)))
print("TUFE Eyl1929->Mar1933 %", p((1929, 9), (1933, 3)), "| 1000$ alim gucu", alim((1929, 9), (1933, 3)))
print("TUFE Eyl2022->Eyl2026 %", p((2022, 9), (2026, 9)), "| 1000$ alim gucu", alim((2022, 9), (2026, 9)))
print("TUFE Eyl2025->Eyl2026 %", p((2025, 9), (2026, 9)), "| 1000$ alim gucu", alim((2025, 9), (2026, 9)))
for y in range(1930, 1934):
    print(f"  yillik Eyl{y-1}->Eyl{y} %", p((y - 1, 9), (y, 9)))
for y in range(2021, 2027):
    print(f"  yillik Eyl{y-1}->Eyl{y} %", p((y - 1, 9), (y, 9)))
t = [r for r in csv.DictReader(open(os.path.join(B, "fdic-tablo5-askiya-alma-1921-1933.csv"))) if int(r["yil"]) >= 1930]
n = sum(int(r["askiya_alinan_banka"]) for r in t)
dep = sum(int(r["mevduat_bin_usd"]) for r in t); los = sum(int(r["mudi_kaybi_bin_usd"]) for r in t)
print("FDIC 1930-33 askiya alma:", n, "| mevduat bin$", dep, "| kayip bin$", los, "| kayip/mevduat %", round(100 * los / dep, 1), "| 1000$ basina", round(1000 * los / dep))
print("Banka kapisi askiya alinan bankada kalan ortalama:", 1000 - round(1000 * los / dep))
print("Tum ticari bank mevduatina gore kayip toplami (4 yil, sutun 4 toplami) %", round(0.57 + 1.01 + 0.57 + 2.15, 2))
print("Banka sayisi (FRH-BP: >8000 uye + ~16000 uye degil) ~24000 -> askiya alma payi %", round(100 * n / 24000))
print("1929 ucret (BEA T6.6A satir 1) 1430$ -> 1000$ =", round(1000 / 1430 * 12, 1), "aylik ucret")
