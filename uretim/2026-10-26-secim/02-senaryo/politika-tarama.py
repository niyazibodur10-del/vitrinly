#!/usr/bin/env python3
"""F2 politika ön taraması — ölçüm betiği (monetizasyon-uyum-uzmani).

Kullanım: python3 politika-tarama.py <senaryolar.md> <pilot-metin.md>

Her senaryo bloğundan seslendirilecek/yayınlanacak İngilizce metni (tırnak içi
metinler + başlıklar + thumbnail metni) çıkarır ve şunları sayar:
  1. Tavsiye/uzman dili (AI personası riski, answer/1311392)
  2. Hassas/reklam kelimeleri (answer/6162278: savaş, intihar, şiddet, nefret sembolü)
  3. Gerçek kişi/kurum adları (sentetik beyan ve karalama riski, answer/14328491)
  4. Pilot metinle 5-gram örtüşmesi (Ö7, iç kural ≤ %10)
  5. Senaryolar arası en yüksek 5-gram örtüşmesi (seri şablon riski)
Çıkış deterministiktir (iki koşu aynı olmalı).
"""
import re
import sys
from itertools import combinations

ADVICE = [
    r"\byou should\b", r"\bi recommend\b", r"\bbuy now\b", r"\bsell now\b",
    r"\bguaranteed?\b", r"\binvest in\b", r"\bfinancial advi[cs]", r"\badvisor\b",
    r"\bexpert\b", r"\bdon'?t invest\b", r"\bbest investment\b", r"\btip\b",
    r"\bterrible bet\b", r"\bbad investment\b", r"\bdo not touch\b",
    r"\bkeep cash\b", r"\bpicked wrong\b", r"\bi believe now\b",
]
SENSITIVE = [
    r"\bwar\b", r"\bsuicid", r"\bkill", r"\bdeath\b", r"\bdied\b", r"\bblood",
    r"\bnazi", r"\bhitler", r"\bswastika", r"\bterror", r"\bbomb", r"\bweapon",
    r"\bdisaster\b", r"\bheist\b", r"\bvillain\b", r"\biran\b", r"\bisrael",
]
REAL = [
    r"\bcisco\b", r"\blehman\b", r"\bhunt\b", r"\bltcm\b", r"\bkrupp\b",
    r"\bthyssen\b", r"\bstinnes\b", r"\bbuffett\b", r"\bcoreweave\b",
    r"\bbarclays\b", r"\bfed\b", r"\bvolcker\b", r"\bbaker\b",
    r"\bbank of united states\b", r"\bnobel\b",
]


def bloklar(md):
    parcalar = re.split(r"^### (S\d\d) — ", md, flags=re.M)
    out = {}
    for i in range(1, len(parcalar), 2):
        sid, govde = parcalar[i], parcalar[i + 1]
        govde = re.split(r"^---$|^## ", govde, flags=re.M)[0]
        out[sid] = govde
    return out


def yayin_metni(govde):
    satirlar = []
    for s in govde.splitlines():
        if re.search(r"Çalışma başlığı|Alternatif \d|Hook \(kelimesi|köprü|Özgün tez|Shorts kancası|Thumbnail fikri", s):
            satirlar += re.findall(r'"([^"]+)"', s)
            m = re.search(r"\*\*(?:Çalışma başlığı|Alternatif \d):\*\*\s*(.+)$", s)
            if m:
                satirlar.append(m.group(1))
    return " \n".join(satirlar)


def say(desen, metin):
    bulgu = []
    for d in desen:
        for m in re.finditer(d, metin, flags=re.I):
            bulgu.append(m.group(0).lower())
    return sorted(set(bulgu))


def ngram(metin, n=5):
    k = re.findall(r"[a-z0-9']+", metin.lower())
    return {tuple(k[i:i + n]) for i in range(len(k) - n + 1)}


def oran(a, b):
    return 0.0 if not a else len(a & b) / len(a)


def main():
    md = open(sys.argv[1], encoding="utf-8").read()
    pilot = open(sys.argv[2], encoding="utf-8").read()
    pilot_txt = " ".join(re.findall(r"\|\s*P\d\d\s*\|[^|]*\|\s*([^|]+)\|", pilot))
    pilot_txt = re.sub(r"[*/]", " ", pilot_txt)
    pg = ngram(pilot_txt)
    b = bloklar(md)
    metinler = {sid: yayin_metni(g) for sid, g in b.items()}
    grams = {sid: ngram(t) for sid, t in metinler.items()}
    print("| ID | Kelime | Tavsiye/uzman dili | Hassas kelime | Gerçek kişi/kurum | Pilot 5-gram | En yakın senaryo 5-gram |")
    print("|---|---|---|---|---|---|---|")
    for sid in sorted(metinler):
        t = metinler[sid]
        en = max(((oran(grams[sid], grams[o]), o) for o in grams if o != sid))
        print(f"| {sid} | {len(t.split())} | {', '.join(say(ADVICE, t)) or '—'} | "
              f"{', '.join(say(SENSITIVE, t)) or '—'} | {', '.join(say(REAL, t)) or '—'} | "
              f"{oran(grams[sid], pg)*100:.1f} % | {en[0]*100:.1f} % ({en[1]}) |")
    cift = max((max(oran(grams[a], grams[c]), oran(grams[c], grams[a])), a, c) for a, c in combinations(sorted(grams), 2))
    print(f"\nSenaryo sayısı: {len(metinler)} · pilot 5-gram sayısı: {len(pg)}")
    print(f"En yüksek senaryo çifti örtüşmesi: {cift[0]*100:.1f} % ({cift[1]}–{cift[2]})")
    print("İç kural Ö7: pilot örtüşmesi ≤ 10 %")
    kalan = [s for s in grams if oran(grams[s], pg) > 0.10]
    print("Ö7 sonucu:", "GEÇTİ" if not kalan else "KALDI " + ",".join(kalan))


if __name__ == "__main__":
    main()
