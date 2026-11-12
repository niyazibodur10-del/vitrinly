#!/usr/bin/env python3
"""F3 politika denetimi v2 (S08, hakem P1–P4) — monetizasyon-uyum-uzmani.
Kullanım: python3 -I politika-denetim.py metin.md --onceki <önceki metin.md> ...
Ayrıştırır: ANLATIM, GÖRSEL, Shorts "Okunacak tam metin" <<…>>. Deterministik.
P1 parti/isim/seçim · P2 korku dili bağlamı · P3 tavsiye/varlık · ilk 30 sn şok · savaş görseli ·
zaman sözcüğü · Shorts niteleyici · önceki metinle 5-gram (Ö7 ≤ %10)."""
import re, sys

P1 = [r"\btrump", r"\bbiden", r"\bharris", r"\bvance\b", r"\bobama", r"\bpelosi", r"\bjohnson\b",
      r"\bschumer", r"\bmcconnell", r"\bpowell\b", r"\bdemocrat", r"\brepublican", r"\bgop\b",
      r"\bmaga\b", r"\bpresident", r"\bsenator", r"\belection", r"\bmidterm", r"\bballot",
      r"\bparty\b", r"\bparties\b", r"\bcongress", r"\bwhite house", r"\bvoters?\b", r"\bvote\b",
      r"parti", r"başkan", r"seçim", r"demokrat", r"cumhuriyetçi", r"kongre", r"yüz(ü|ler)? görün"]
RENK = r"(kırmızı|mavi)[^|.]{0,40}(parti|eyalet|harita|taraf)|\b(red|blue) (state|team|party)"
P2 = [r"\bspiral", r"\bdefault", r"\bbankrupt", r"\bcollapse", r"\bcrash", r"\bdoom", r"\bdisaster"]
P2_NIT = [r"possibilit", r"\bcould\b", r"\bmay\b", r"\bmight\b", r"\bbrakes?\b", r"some economists"]
P3 = [r"\byour money\b", r"\byou should\b", r"\bprotect yourself", r"\byou need to\b", r"\byou must\b",
      r"\bi recommend", r"\bbuy\b", r"\bsell\b", r"\binvest", r"\bgold\b", r"\bbitcoin", r"\bcrypto",
      r"\bstocks?\b", r"\bhedge\b", r"\bsavings? account", r"\bfinancial advi", r"\bexpert\b",
      r"\badvis[oe]r", r"\bsafe(st)? (asset|place|bet)", r"\bguarantee"]
SOK = [r"\bshit", r"\bfuck", r"\bdamn\b", r"\bhell\b", r"\bterrif", r"\bpanic", r"\bdoom",
       r"\bcollapse", r"\bcrash", r"\bdestroy", r"\bshocking"]
SAVAS_G = r"savaş|asker|bomba|silah|patlama|tank|kan\b|ceset|yıkıntı|cephe"
ZAMAN = [r"\bthis week\b", r"\btoday\b", r"\byesterday\b", r"\bjust (announced|released)", r"\btonight\b"]
NIT = [r"history", r"not a forecast", r"possibilit", r"scenario", r"\bin our kitchen", r"if the u\.s\. were"]


def bul(desen, t):
    out = []
    for d in desen:
        for m in re.finditer(d, t, flags=re.I):
            a = max(0, m.start() - 45); out.append(f"…{t[a:m.end()+35]}…".replace("\n", " "))
    return out


def ngr(t, n=5):
    k = re.findall(r"[a-z0-9']+", t.lower()); return {tuple(k[i:i+n]) for i in range(len(k)-n+1)}


def sahneler(t):
    return re.findall(r"### (S\d\d) · ([0-9:]+)–[^\n]*\n\| ANLATIM \| GÖRSEL \|\n\|---\|---\|\n\| ([^|]+)\|([^\n]*)", t)


def main():
    a = sys.argv[1:]; md = open(a[0], encoding="utf-8").read()
    onceki = a[a.index("--onceki")+1:] if "--onceki" in a else []
    sh = sahneler(md)
    anl = " ".join(s[2] for s in sh); gor = " ".join(s[3] for s in sh)
    ilk30 = " ".join(s[2] for s in sh if s[1] < "0:30")
    shorts = re.findall(r"Okunacak tam metin[^<]*<<(.+?)>>", md)
    meta = re.findall(r"^# F3[^\"]*\"([^\"]+)\"", md, flags=re.M)
    print(f"Sahne {len(sh)} · anlatım {len(anl.split())} kelime · Shorts {len(shorts)} · başlık {meta}")
    def rapor(ad, liste):
        print(f"\n[{ad}] {len(liste)}"); [print("  ", x) for x in liste]
    rapor("P1 anlatım", bul(P1, anl)); rapor("P1 GÖRSEL", bul(P1, gor)); rapor("P1 renk", bul([RENK], gor))
    rapor("P1 Shorts", bul(P1, " ".join(shorts))); rapor("P1 başlık", bul(P1, " ".join(meta)))
    p2 = []
    for c in re.split(r"(?<=[.?!])\s+", anl + " " + " ".join(shorts)):
        if any(re.search(d, c, re.I) for d in P2):
            p2.append(("NİTELİ " if any(re.search(d, c, re.I) for d in P2_NIT) else "NİTELİKSİZ ") + c)
    rapor("P2 korku dili (cümle)", p2)
    rapor("P3 anlatım", bul(P3, anl)); rapor("P3 Shorts", bul(P3, " ".join(shorts)))
    rapor("P3 GÖRSEL/ekran", bul(P3, gor))
    rapor("İlk 30 sn şok/küfür", bul(SOK, ilk30)); rapor("Şok/küfür tüm", bul(SOK, anl))
    rapor("Savaş görseli (GÖRSEL)", bul([SAVAS_G], gor)); rapor("Zaman sözcüğü", bul(ZAMAN, anl + " ".join(shorts)))
    for i, s in enumerate(shorts, 1):
        print(f"\n[Shorts {i}] {len(s.split())} kelime ≈{len(s.split())/160*60:.0f} sn · niteleyici: "
              f"{[d for d in NIT if re.search(d, s, re.I)] or 'YOK'} · anlatımda olmayan cümle: "
              f"{[c for c in re.split(r'(?<=[.?!])\s+', s) if c.strip() and c.strip() not in anl] }")
    g = ngr(anl)
    for y in onceki:
        o = " ".join(x[2] for x in sahneler(open(y, encoding="utf-8").read()))
        r = len(g & ngr(o)) / len(g) * 100
        print(f"\n[Ö7] {y}: {r:.1f} % ({'GEÇTİ' if r <= 10 else 'KALDI'}) · ortak: {sorted(' '.join(x) for x in g & ngr(o))[:8]}")


if __name__ == "__main__":
    main()
