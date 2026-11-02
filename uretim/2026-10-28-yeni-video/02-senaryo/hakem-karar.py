#!/usr/bin/env python3
"""Hakem F2 bileşik puanı + ağırlık duyarlılığı + hook/aritmetik kontrolü (deterministik).

Kullanım: python3 -I hakem-karar.py   (1929 videosundaki betiğin kopyası; PUAN/HOOK/kontroller değişti)
- viralite: viralite-analisti nihai puanı (viralite.md, tools/viralite.py) [T]
- diğerleri: hakem yargısı 1-10 [T]; gerekçe senaryo-karari.md §2
İki durum: 'once' = taramaların bugünkü rengi, 'sonra' = zorunlu F3 düzeltmeleri uygulanınca.
"""
from decimal import Decimal as D
from itertools import permutations

AGIRLIK = {"viralite": D("0.35"), "dogrulama": D("0.15"), "politika": D("0.15"),
           "uretim": D("0.10"), "kimlik": D("0.15"), "ozgunluk": D("0.10")}
assert sum(AGIRLIK.values()) == D("1.00")

PUAN = {
    "once": {
        "S06": {"viralite": D("7.50"), "dogrulama": 8, "politika": 9, "uretim": 7, "kimlik": 7, "ozgunluk": 7},
        "S01": {"viralite": D("7.25"), "dogrulama": 7, "politika": 8, "uretim": 6, "kimlik": 7, "ozgunluk": 6},
        "S08": {"viralite": D("7.25"), "dogrulama": 8, "politika": 8, "uretim": 9, "kimlik": 8, "ozgunluk": 6},
    },
    "sonra": {
        "S06": {"viralite": D("7.50"), "dogrulama": 9, "politika": 9, "uretim": 7, "kimlik": 7, "ozgunluk": 7},
        "S01": {"viralite": D("7.25"), "dogrulama": 8, "politika": 9, "uretim": 6, "kimlik": 7, "ozgunluk": 6},
        "S08": {"viralite": D("7.25"), "dogrulama": 9, "politika": 8, "uretim": 9, "kimlik": 8, "ozgunluk": 6},
    },
}
HOOK = {"S06": 8, "S01": 8, "S08": 9}  # viralite.md §2 hook ölçütü = ilk 15 sn (eşitlik bozucu)
ESIK = D("0.30")


def skor(p, w):
    return sum(w[k] * D(p[k]) for k in w).quantize(D("0.01"))


def sirala(durum, w):
    s = {i: skor(p, w) for i, p in PUAN[durum].items()}
    return sorted(s.items(), key=lambda x: (-x[1], -HOOK[x[0]], x[0]))


def kazanan(sira):
    (a, sa), (b, sb) = sira[0], sira[1]
    if sa - sb < ESIK:
        if HOOK[b] > HOOK[a]:
            return b, "eşit (<0.30), hook belirledi"
        return a, ("eşit (<0.30), hook belirledi" if HOOK[a] > HOOK[b] else "eşit, hook da eşit → puan")
    return a, "açık fark"


for durum in ("once", "sonra"):
    sira = sirala(durum, AGIRLIK)
    k, neden = kazanan(sira)
    print(f"[{durum}] " + " | ".join(f"{i} {s}" for i, s in sira) + f"  → kazanan {k} ({neden})")

for durum in ("once", "sonra"):
    say, degisen, maxfark = {}, [], D("0")
    for a, b in permutations(AGIRLIK, 2):
        w = dict(AGIRLIK); w[a] -= D("0.05"); w[b] += D("0.05")
        sira = sirala(durum, w)
        k, neden = kazanan(sira)
        say[k] = say.get(k, 0) + 1
        maxfark = max(maxfark, abs(dict(sira)["S06"] - dict(sira)["S08"]))
        if k != "S08":
            degisen.append(f"{a}->{b}")
    print(f"[{durum}] ±0.05 ağırlık, 30 durum → " + ", ".join(f"{k}={v}" for k, v in sorted(say.items()))
          + f"; S06-S08 en büyük |fark| {maxfark}; S08 dışı kazanan: {degisen or 'yok'}")

# Eşitlik bozucuyu devre dışı bırakınca (yalnız puan) kim kazanır — şeffaflık
for durum in ("once", "sonra"):
    print(f"[{durum}] hook'suz sıra: " + " > ".join(i for i, _ in sirala(durum, AGIRLIK)))

# Hook kelime sayısı (≤40) ve hook rakamlarının birincil veriyle aritmetiği (on-dogrulama.md §4, MTS FY2026)
HOOKLAR = {
    "S08": "Shrink the US government down to one household. It brings home five thousand four hundred dollars a month. It spends about seven thousand four hundred. Let's sit at its kitchen table and see where the gap goes.",
    "S06": "Everyone watches the Fed. But your mortgage rate mostly follows a different number. This fall it went above five percent for the first time in almost twenty years. Let's follow that number all the way to your front door.",
}
for i, h in HOOKLAR.items():
    n = len(h.split())
    print(f"hook {i}: {n} kelime ≤40 {'OK' if n <= 40 else 'KALDI'}")
gelir, gider, faiz, borc = D("5403.3"), D("7395.8"), D("1051.8"), D("40170")  # milyar $ (MTS T1/T9, Debt to the Penny)
print(f"S08 ölçek ($/ay = milyar $/yıl): gelir {gelir:.0f} → 'five thousand four hundred' "
      f"{'OK' if abs(gelir-5400)/5400 < D('0.01') else 'KALDI'}; gider {gider:.0f} → 'about seven thousand four hundred' "
      f"{'OK' if abs(gider-7400)/7400 < D('0.01') else 'KALDI'}; açık/ay {gider-gelir:.1f} → thumbnail '-$2,000/MO' "
      f"{'OK' if abs(gider-gelir-2000)/2000 < D('0.01') else 'KALDI'}")
print(f"S08 faiz/gelir {(faiz/gelir*100).quantize(D('0.1'))}% → 'one in every five dollars' "
      f"{'OK' if abs(faiz/gelir-D('0.2')) < D('0.01') else 'KALDI'}; gider/gelir {(gider/gelir).quantize(D('0.001'))} → "
      f"'$7 for every $5' (1.4) {'OK' if abs(gider/gelir-D('1.4')) < D('0.05') else 'KALDI'}; hane borcu "
      f"{(borc/gelir*5400*12/1000).quantize(D('0.1'))}K $ (toplam borç)")
