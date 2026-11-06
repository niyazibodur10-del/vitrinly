#!/usr/bin/env python3
"""Hakem F2 bileşik puanı + ağırlık duyarlılığı + uç durum + hook/aritmetik kontrolü (deterministik).

Kullanım: python3 -I hakem-karar.py   (2026-10-28 betiğinin kopyası v3; PUAN/HOOK/kontroller değişti)
- viralite: viralite-analisti nihai puanı (viralite.md, model v0.2) [T]; S05 = Alt-2 başlıkla 7.70
- diğerleri: hakem yargısı 1-10 [T]; gerekçe senaryo-karari.md §2
İki durum: 'once' = taramaların bugünkü rengi, 'sonra' = zorunlu F3 düzeltmeleri uygulanınca.
"""
from decimal import Decimal as D
from itertools import permutations

AGIRLIK = {"viralite": D("0.35"), "dogrulama": D("0.15"), "politika": D("0.15"),
           "uretim": D("0.10"), "kimlik": D("0.15"), "ozgunluk": D("0.10")}
assert sum(AGIRLIK.values()) == D("1.00")

VIR = {"S03": (D("7.60"), D("8.10"), D("8.40")), "S01": (D("7.40"), D("8.00"), D("8.35")),
       "S05": (D("7.10"), D("7.70"), D("8.05"))}  # köt./tem./iyi. (S05 Alt-2: temel 7.70, aralık = cezasız aralık −0.25 [H])
PUAN = {
    "once": {
        "S03": {"dogrulama": 6, "politika": 9, "uretim": 7, "kimlik": 8, "ozgunluk": 6},
        "S01": {"dogrulama": 5, "politika": 7, "uretim": 6, "kimlik": 7, "ozgunluk": 6},
        "S05": {"dogrulama": 6, "politika": 8, "uretim": 7, "kimlik": 6, "ozgunluk": 5},
    },
    "sonra": {
        "S03": {"dogrulama": 8, "politika": 9, "uretim": 7, "kimlik": 8, "ozgunluk": 7},
        "S01": {"dogrulama": 7, "politika": 8, "uretim": 6, "kimlik": 7, "ozgunluk": 6},
        "S05": {"dogrulama": 8, "politika": 8, "uretim": 7, "kimlik": 6, "ozgunluk": 6},
    },
}
HOOK = {"S03": 7, "S01": 9, "S05": 9}  # viralite.md §3 hook ölçütü = ilk 15 sn (eşitlik bozucu)
ESIK = D("0.30")


def skor(p, v, w):
    q = dict(p); q["viralite"] = v
    return sum(w[k] * D(q[k]) for k in w).quantize(D("0.01"))


def sirala(durum, w, vir=None):
    vir = vir or {i: VIR[i][1] for i in VIR}
    s = {i: skor(p, vir[i], w) for i, p in PUAN[durum].items()}
    return sorted(s.items(), key=lambda x: (-x[1], -HOOK[x[0]], x[0]))


def kazanan(sira):
    (a, sa), (b, sb) = sira[0], sira[1]
    if sa - sb < ESIK:
        return (b if HOOK[b] > HOOK[a] else a), "eşit (<0.30), hook belirledi"
    return a, f"açık fark {sa - sb}"


for durum in ("once", "sonra"):
    sira = sirala(durum, AGIRLIK)
    k, neden = kazanan(sira)
    print(f"[{durum}] " + " | ".join(f"{i} {s}" for i, s in sira) + f"  → kazanan {k} ({neden})")

for durum in ("once", "sonra"):
    say, degisen, minfark = {}, [], D("99")
    for a, b in permutations(AGIRLIK, 2):
        w = dict(AGIRLIK); w[a] -= D("0.05"); w[b] += D("0.05")
        sira = sirala(durum, w)
        k, _ = kazanan(sira)
        say[k] = say.get(k, 0) + 1
        minfark = min(minfark, dict(sira)["S03"] - dict(sira)["S01"])
        if k != "S03":
            degisen.append(f"{a}->{b}")
    print(f"[{durum}] ±0.05 ağırlık, 30 durum → " + ", ".join(f"{k}={v}" for k, v in sorted(say.items()))
          + f"; S03-S01 en küçük fark {minfark}; S03 dışı kazanan: {degisen or 'yok'}")

# Uç durum: kazanan kötümser, rakipler iyimser viralite
for durum in ("once", "sonra"):
    vir = {"S03": VIR["S03"][0], "S01": VIR["S01"][2], "S05": VIR["S05"][2]}
    sira = sirala(durum, AGIRLIK, vir)
    k, neden = kazanan(sira)
    print(f"[{durum}] uç (S03 köt., S01/S05 iyi.): " + " | ".join(f"{i} {s}" for i, s in sira) + f" → {k} ({neden})")

# Viralite ağırlığı kaç olursa S01 S03'ü geçer? (kalan ağırlıklar oransal küçülür)
for durum in ("once", "sonra"):
    bulunan = None
    for yuz in range(35, 101):
        wv = D(yuz) / 100
        olcek = (1 - wv) / (1 - AGIRLIK["viralite"])
        w = {k: (wv if k == "viralite" else AGIRLIK[k] * olcek) for k in AGIRLIK}
        k, _ = kazanan(sirala(durum, w))
        if k != "S03":
            bulunan = wv; break
    print(f"[{durum}] S01'in kazanması için viralite ağırlığı ≥ {bulunan or 'yok (1.00 bile yetmez)'}")

# Hook adayları (F3 girdisi): kelime sayısı ≤40
HOOKLAR = {
    "S03-eski": "About one hundred twenty-four trillion dollars is changing hands as the boomers age, Bank of America says. It's the biggest handover of money ever. Let's follow one family's share and count what leaks out on the way.",
    "S03-H1b": "About one hundred twenty-four trillion dollars is set to pass down in America by twenty forty-eight, Cerulli estimates. But eighteen trillion goes to charity, and fifty-four trillion stops at a spouse first. So what really reaches the kids?",
    "S03-H1c": "One hundred twenty-four trillion dollars. That's the number everyone quotes for the boomers' money. But it's a forecast out to twenty forty-eight, and it leaks. Let's follow one family's share and count what's left.",
}
for i, h in HOOKLAR.items():
    n = len(h.split())
    print(f"hook {i}: {n} kelime ≤40 {'OK' if n <= 40 else 'KALDI'}")

# S03 aritmetik (Cerulli Ara 2024 kırılımı, on-dogrulama.md S03 [A]): mirasçı + bağış ≈ toplam → eş payı İÇİNDE
toplam, mirasci, bagis, es = D("124"), D("105"), D("18"), D("54")
fark = abs(mirasci + bagis - toplam) / toplam
print(f"S03 105+18={mirasci+bagis} vs 124 → sapma %{(fark*100).quantize(D('0.1'))} "
      f"{'OK (eş payı toplamın içinde: çıkarılırsa çift sayım)' if fark < D('0.01') else 'KALDI'}; "
      f"yanlış okuma 124-54-18={toplam-es-bagis} T$ (metne girmez)")

# S01 tez kontrolü: kronolojik rekor tutarları (milyon $) monoton artıyor mu? (on-dogrulama.md S01)
seri = [("Bağdat 2003", 1000), ("Mt. Gox 2014", 473), ("Bangladeş 2016", 101), ("Binance 2026", 6300)]
artan = all(b[1] > a[1] for a, b in zip(seri, seri[1:]))
print(f"S01 'bigger heists' monoton artış: {'EVET' if artan else 'HAYIR → başlık/tez değişmeli'}; "
      f"Binance/Bybit {D('6.3')/D('1.5')} (alt sınır {(D('5.7')/D('1.5')).quantize(D('0.1'))})")
