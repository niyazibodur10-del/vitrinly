#!/usr/bin/env python3
"""Okafor örnek ailesi kutu aritmetiği (senaryo-yazari, S03 F3). Örnek/illüstrasyon; dolar tutarı yok.
Kullanım: python3 -I veri/kutu-hesap.py ../metin.md  → assert + metin taraması (D2 çift sayım kalıpları)."""
import re, sys
yuklenen = {"HOUSE": 4, "RETIREMENT": 4, "BANK": 2}
duraklar = [("LIVING", -2), ("CARE", -1), ("SPOUSE (detour, +years)", 0), ("GIVING", -1), ("HOUSE (slice)", 0), ("TAX & TIME", 0)]
toplam = sum(yuklenen.values()); assert toplam == 10
kalan = toplam
for ad, d in duraklar:
    kalan += d; print(f"{ad:28s} {d:+d} → {kalan}")
assert kalan == 6, kalan                       # "Delivered: six boxes, minus a slice"
assert kalan / 2 == 3                          # "about three boxes each, a little less" (dilim yüzünden)
assert dict(duraklar)["SPOUSE (detour, +years)"] == 0   # D2: eş durağı kayıp değil
print(f"Teslim: {kalan} kutu − dilim, 2 çocuk → ≈{kalan/2:.0f} − (dilim/2) her biri")
if len(sys.argv) > 1:
    t = open(sys.argv[1], encoding="utf-8").read().lower()
    yasak = [r"fifty-two trillion", r"\b52 ?t", r"124 ?[−-] ?54", r"minus fifty-four", r"inside the (total|124|hundred)", r"more than half of it", r"seventy percent", r"one in a thousand", r"thirty million"]
    bul = [(y, len(re.findall(y, t))) for y in yasak if re.findall(y, t)]
    print("D2/R27 yasak kalıp taraması:", "0 → GEÇTİ" if not bul else f"KALDI {bul}")
    sys.exit(1 if bul else 0)
