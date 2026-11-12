#!/usr/bin/env python3
"""Hakem F2 bileşik puanı + ağırlık duyarlılığı (deterministik).

Kullanım: python3 hakem-karar.py
Girdi bu dosyanın içinde (puanlar senaryo-karari.md §2'de gerekçeli).
- viralite: viralite-analisti nihai puanı (tools/viralite.py çıktısı) [T]
- diğerleri: hakem yargısı 1-10 [T], kaynak raporlara dayanır
İki durum: 'once' = taramaların bugünkü rengi, 'sonra' = zorunlu F3 düzeltmeleri uygulanınca kalan risk.
"""
from decimal import Decimal as D
from itertools import permutations

AGIRLIK = {
    "viralite": D("0.35"),
    "dogrulama": D("0.15"),
    "politika": D("0.15"),
    "uretim": D("0.10"),
    "kimlik": D("0.15"),
    "ozgunluk": D("0.10"),
}
assert sum(AGIRLIK.values()) == D("1.00")

PUAN = {
    "once": {
        "S03": {"viralite": D("8.40"), "dogrulama": 6, "politika": 7, "uretim": 6, "kimlik": 8, "ozgunluk": 9},
        "S01": {"viralite": D("7.75"), "dogrulama": 9, "politika": 9, "uretim": 8, "kimlik": 6, "ozgunluk": 7},
        "S06": {"viralite": D("7.20"), "dogrulama": 8, "politika": 7, "uretim": 7, "kimlik": 6, "ozgunluk": 7},
    },
    "sonra": {
        "S03": {"viralite": D("8.40"), "dogrulama": 8, "politika": 8, "uretim": 6, "kimlik": 8, "ozgunluk": 9},
        "S01": {"viralite": D("7.75"), "dogrulama": 9, "politika": 9, "uretim": 8, "kimlik": 6, "ozgunluk": 7},
        "S06": {"viralite": D("7.20"), "dogrulama": 8, "politika": 8, "uretim": 7, "kimlik": 6, "ozgunluk": 7},
    },
}
HOOK = {"S03": 9, "S01": 8, "S06": 8}  # viralite.md §2 hook ölçütü (eşitlik bozucu: ilk 15 sn)
ESIK = D("0.30")  # bundan küçük fark = eşit say (viralite modeliyle aynı eşik)


def skor(p, w):
    return sum(w[k] * D(p[k]) for k in w).quantize(D("0.01"))


def sirala(durum, w):
    s = {i: skor(p, w) for i, p in PUAN[durum].items()}
    return sorted(s.items(), key=lambda x: (-x[1], -HOOK[x[0]], x[0]))


def kazanan(sira):
    """Fark < ESIK ise ilk 15 sn (hook) belirler."""
    (a, sa), (b, sb) = sira[0], sira[1]
    if sa - sb < ESIK and HOOK[b] > HOOK[a]:
        return b, "eşit (<0.30), hook belirledi"
    if sa - sb < ESIK:
        return a, "eşit (<0.30), hook belirledi" if HOOK[a] > HOOK[b] else "eşit, hook da eşit"
    return a, "açık fark"


for durum in ("once", "sonra"):
    sira = sirala(durum, AGIRLIK)
    k, neden = kazanan(sira)
    print(f"[{durum}] " + " | ".join(f"{i} {s}" for i, s in sira) + f"  → kazanan {k} ({neden})")

# Duyarlılık: bir ağırlıktan 0.05 al, başka birine ver (6x5 = 30 durum) — her iki durumda
for durum in ("once", "sonra"):
    say = {}
    for a, b in permutations(AGIRLIK, 2):
        w = dict(AGIRLIK)
        w[a] -= D("0.05"); w[b] += D("0.05")
        k, _ = kazanan(sirala(durum, w))
        say[k] = say.get(k, 0) + 1
    print(f"[{durum}] ±0.05 ağırlık, 30 durum → kazanan sayısı: " +
          ", ".join(f"{k}={v}" for k, v in sorted(say.items())))
