#!/usr/bin/env python3
"""F2 senaryo kapısı (v2, 2026-10-28; v1 = 2026-10-26-1929-1000-dolar/02-senaryo/senaryo-kontrol.py).
Kapılar: ≥10 senaryo · ≥7 farklı açı türü · slot sütunu (--sutun B) ≥6 · her senaryoda 3 başlık ≤60 kr,
seçilen hook ≤40 kelime (160 kpm ≈ 15 sn) + ≥2 elenen varyant, Shorts kancası, risk notu, sonuçtan bağımsızlık satırı,
Leo rolü (hepsi farklı) · hook/Shorts'ta telaffuz listesi yok · başlıkta aşınmış kalıp yok
("Nobody/No one", "real reason/true origin/get wrong", yalın "AI bubble") · hook'ta önceki video açılış kalıbı yok.
Kullanım: python3 senaryo-kontrol.py senaryolar.md [--sutun B]"""
import re, sys
YASAK = re.compile(r"\b(charts?|complicated|scenarios?|truth|crash(es|ed|ing)?|bold)\b", re.I)
KALIP_BASLIK = re.compile(r"\b(nobody|no one|real reason|true origin|get wrong)\b|\bAI bubble\b", re.I)
ESKI_ACILIS = re.compile(r"(it's september|you have one thousand|let's play|imagine waking|three doors)", re.I)
args = sys.argv[1:]
sutun_hedef = args[args.index("--sutun") + 1] if "--sutun" in args else "B"
metin = open(args[0], encoding="utf-8").read()
govde = metin.split("## Test")[0]
bloklar = re.split(r"^### (S\d\d) — ", govde, flags=re.M)[1:]
hata = 0; acilar = {}; sutun = {}; roller = {}
def kelime(s): return len(re.findall(r"[A-Za-z0-9$][\w$.,'’\-]*", s))
print("| ID | Alan | Metin | Karakter | Kelime | Bulgu | Sonuç |")
print("|---|---|---|---|---|---|---|")
for i in range(0, len(bloklar), 2):
    sid, blok = bloklar[i], bloklar[i+1]
    basliklar = re.findall(r"^- \*\*(Çalışma başlığı|Alternatif 1|Alternatif 2):\*\* (.+)$", blok, re.M)
    if len(basliklar) != 3:
        print(f"| {sid} | Başlık sayısı | {len(basliklar)} | — | — | 3 gerekli | KALDI |"); hata += 1
    for alan, deger in basliklar:
        d = deger.strip(); n = len(d); k = KALIP_BASLIK.search(d)
        ok = n <= 60 and not k; hata += not ok
        print(f"| {sid} | {alan} | {d} | {n} | — | {k.group(0) if k else 'yok'} | {'GEÇTİ' if ok else 'KALDI'} |")
    h = re.search(r"^- \*\*Hook \(kelimesi kelimesine, 0–15 sn\):\*\* \"(.+)\"$", blok, re.M)
    if not h:
        print(f"| {sid} | Hook | YOK | — | — | — | KALDI |"); hata += 1
    else:
        k = kelime(h.group(1))
        y = sorted({m.group(0).lower() for m in YASAK.finditer(h.group(1))})
        e = ESKI_ACILIS.search(h.group(1))
        ok = k <= 40 and not y and not e; hata += not ok
        bulgu = ", ".join(y + ([e.group(0)] if e else [])) or "yok"
        print(f"| {sid} | Hook | (seçilen) | — | {k} | {bulgu} | {'GEÇTİ' if ok else 'KALDI'} |")
    elenen = len(re.findall(r"^  - H\d .*\(elendi", blok, re.M))
    ok = elenen >= 2; hata += not ok
    print(f"| {sid} | Elenen hook varyantı | {elenen} | — | — | ≥2 | {'GEÇTİ' if ok else 'KALDI'} |")
    sh = re.search(r"^- \*\*Shorts kancası:\*\* \"(.+?)\"", blok, re.M)
    if not sh:
        print(f"| {sid} | Shorts kancası | YOK | — | — | — | KALDI |"); hata += 1
    else:
        y = sorted({m.group(0).lower() for m in YASAK.finditer(sh.group(1))})
        ok = not y and kelime(sh.group(1)) <= 30; hata += not ok
        print(f"| {sid} | Shorts kancası | — | — | {kelime(sh.group(1))} | {', '.join(y) or 'yok'} | {'GEÇTİ' if ok else 'KALDI'} |")
    for alan in ("Risk notu", "Sonuçtan bağımsızlık"):
        ok = bool(re.search(rf"^- \*\*{alan}:\*\* \S", blok, re.M)); hata += not ok
        print(f"| {sid} | {alan} | {'var' if ok else 'YOK'} | — | — | — | {'GEÇTİ' if ok else 'KALDI'} |")
    a = re.search(r"^- \*\*Açı türü:\*\* ([^(\n]+)", blok, re.M)
    s = re.search(r"^- \*\*Sütun:\*\* (\w)", blok, re.M)
    r = re.search(r"^- \*\*Leo'nun rolü[^:]*:\*\* \*\*([^*]+)\*\*", blok, re.M)
    acilar[sid] = a.group(1).strip() if a else "?"
    sutun[sid] = s.group(1) if s else "?"
    roller[sid] = r.group(1).strip().lower() if r else "?"
n = len(acilar); farkli = len(set(acilar.values())); s_say = sum(1 for v in sutun.values() if v == sutun_hedef)
rol_farkli = len(set(roller.values())) == n and "?" not in roller.values()
print(f"\nSenaryo sayısı: {n} (kapı ≥10) · farklı açı türü: {farkli} (kapı ≥7) · {sutun_hedef} sütunu: {s_say} (kapı ≥6) · Leo rolleri hepsi farklı: {rol_farkli}")
for sid in acilar: print(f"  {sid}: {sutun[sid]} · {acilar[sid]} · Leo: {roller[sid]}")
if n < 10 or farkli < 7 or s_say < 6 or not rol_farkli: hata += 1
print("KAPI:", "GEÇTİ" if hata == 0 else f"KALDI ({hata} hata)")
sys.exit(1 if hata else 0)
