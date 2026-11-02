#!/usr/bin/env python3
"""F2 politika ön taraması v2 — monetizasyon-uyum-uzmani (2026-10-26 betiğinden türetildi).

Kullanım: python3 politika-tarama.py <senaryolar.md> <onceki-metin.md> [<onceki-metin.md> ...]

Her senaryo için:
  A. Yayın metni (tırnak içi İngilizce + başlıklar): tavsiye/uzman dili (1311392 AI persona),
     hassas kelime (6162278), gerçek kişi/kurum, meta veri vaat kalıpları (6162278 başlık/thumbnail).
  B. Tüm blok (Türkçe yapı + karakter anı dahil): siyaset, şiddet/saldırı, AI/Anthropic çıkar
     çatışması, önceki video format işaretleri (oyun/kapı/klon/sunucu) — 1311392 "same situation".
  C. Önceki metin(ler)le 5-gram örtüşme (iç kural Ö7 ≤ %10) ve senaryolar arası en yüksek.
Deterministik: iki koşu birebir aynı olmalı.
"""
import re
import sys
from itertools import combinations

ADVICE = [r"\byou should\b", r"\bi recommend\b", r"\bbuy now\b", r"\bsell now\b",
          r"\bguaranteed?\b", r"\binvest in\b", r"\bfinancial advi[cs]", r"\badvisor\b",
          r"\bexpert\b", r"\bdon'?t invest\b", r"\bbest investment\b", r"\btip\b",
          r"\block in\b", r"\brefinance now\b", r"\bwhich number should you\b",
          r"\byour money\b", r"\bact now\b", r"\bbefore it'?s too late\b"]
SENSITIVE = [r"\bwar\b", r"\bsuicid", r"\bkill", r"\bdeaths?\b", r"\bdied\b", r"\bblood",
             r"\bterror", r"\bbomb", r"\bweapon", r"\battacks?\b", r"\bdisaster\b",
             r"\bvillain\b", r"\bheist\b", r"\billegal\b", r"\bcrash", r"\bcollapse"]
REAL = [r"\banthropic\b", r"\bclaude\b", r"\bcoreweave\b", r"\bnvidia\b", r"\bvolcker\b",
        r"\btrump\b", r"\bbiden\b", r"\bdemocrat", r"\brepublican", r"\bkavanaugh\b",
        r"\bsupreme court\b", r"\bunitree\b", r"\bsaudi\b", r"\bfed\b", r"\bmicrosoft\b",
        r"\balphabet\b", r"\bamazon\b", r"\bgoldman\b", r"\bdan ives\b"]
CLICKBAIT = [r"\bis america next\b", r"\bwait,? what\b", r"\bnot what it seems\b",
             r"\bwhat happens to your money\b", r"\bnot yours\b", r"\bhero or villain\b",
             r"\btrick\b", r"\bnobody\b", r"\breal reason\b"]
# Tüm blok (TR+EN) taraması
SIYASET = [r"seçim", r"\bmidterm", r"\bvote\b", r"parti", r"kongre", r"\bcongress\b",
           r"demokrat", r"cumhuriyet", r"trump", r"başkan", r"hükümet", r"pekin", r"siyasi"]
SIDDET = [r"saldırı", r"ölüm", r"ölü\b", r"savaş", r"\battack", r"şiddet", r"patlama", r"jeopoliti"]
AI_CC = [r"anthropic", r"claude", r"\bs-1\b", r"halka arz", r"\bipo\b"]
FORMAT1929 = [r"\boyun\b", r"\bkapı", r"\bklon", r"sunucu", r"\bgame\b", r"\bdoor", r"\bclone",
              r"\bhost\b", r"üç kapı", r"leo kaybe"]


def bloklar(md):
    p = re.split(r"^### (S\d\d) — ", md, flags=re.M)
    return {p[i]: re.split(r"^---$|^## ", p[i + 1], flags=re.M)[0] for i in range(1, len(p), 2)}


def yayin_metni(g):
    out = []
    for s in g.splitlines():
        if re.search(r"Çalışma başlığı|Alternatif \d|Hook \(kelimesi|köprü|Özgün tez|Shorts kancası|Thumbnail fikri|Akılda kalan", s):
            out += re.findall(r'"([^"]+)"', s)
            m = re.search(r"\*\*(?:Çalışma başlığı|Alternatif \d):\*\*\s*(.+)$", s)
            if m:
                out.append(m.group(1))
    return " \n".join(out)


def basliklar(g):
    return " \n".join(re.findall(r"\*\*(?:Çalışma başlığı|Alternatif \d):\*\*\s*(.+)$", g, flags=re.M)
                      + re.findall(r'Metin: "([^"]+)"', g))


def say(desen, metin):
    return sorted({m.group(0).lower() for d in desen for m in re.finditer(d, metin, flags=re.I)})


def sayi(desen, metin):
    return sum(len(re.findall(d, metin, flags=re.I)) for d in desen)


def ngram(t, n=5):
    k = re.findall(r"[a-z0-9']+", t.lower())
    return {tuple(k[i:i + n]) for i in range(len(k) - n + 1)}


def oran(a, b):
    return 0.0 if not a else len(a & b) / len(a)


def onceki(yol):
    t = open(yol, encoding="utf-8").read()
    satir = re.findall(r"\| ANLATIM \| GÖRSEL \|\n\|---\|---\|\n\| ([^|]+)\|", t)
    return " ".join(satir)


def kisa(x):
    return ", ".join(x) or "—"


def main():
    md = open(sys.argv[1], encoding="utf-8").read()
    once = " ".join(onceki(y) for y in sys.argv[2:])
    pg = ngram(once)
    b = bloklar(md)
    mt = {s: yayin_metni(g) for s, g in b.items()}
    gr = {s: ngram(t) for s, t in mt.items()}
    print("## A. Yayın metni (EN)")
    print("| ID | Kelime | Tavsiye dili | Hassas | Gerçek kişi/kurum | Başlık/thumb vaat kalıbı | Önceki 5-gram | En yakın senaryo |")
    print("|---|---|---|---|---|---|---|---|")
    for s in sorted(mt):
        t = mt[s]
        en = max((oran(gr[s], gr[o]), o) for o in gr if o != s)
        print(f"| {s} | {len(t.split())} | {kisa(say(ADVICE, t))} | {kisa(say(SENSITIVE, t))} | "
              f"{kisa(say(REAL, t))} | {kisa(say(CLICKBAIT, basliklar(b[s])))} | "
              f"{oran(gr[s], pg)*100:.1f} % | {en[0]*100:.1f} % ({en[1]}) |")
    print("\n## B. Tüm blok (TR+EN) işaret sayıları")
    print("| ID | Siyaset | Şiddet/saldırı | AI/Anthropic | 1929 format işareti |")
    print("|---|---|---|---|---|")
    for s in sorted(b):
        g = b[s]
        print(f"| {s} | {sayi(SIYASET, g)} | {sayi(SIDDET, g)} | {sayi(AI_CC, g)} | {kisa(say(FORMAT1929, g))} |")
    cift = max((max(oran(gr[a], gr[c]), oran(gr[c], gr[a])), a, c) for a, c in combinations(sorted(gr), 2))
    print(f"\nSenaryo: {len(mt)} · önceki metin 5-gram: {len(pg)} · en yüksek senaryo çifti: {cift[0]*100:.1f} % ({cift[1]}–{cift[2]})")
    kalan = [s for s in sorted(gr) if oran(gr[s], pg) > 0.10]
    print("Ö7 (önceki ≤ 10 %):", "GEÇTİ" if not kalan else "KALDI " + ",".join(kalan))


if __name__ == "__main__":
    main()
