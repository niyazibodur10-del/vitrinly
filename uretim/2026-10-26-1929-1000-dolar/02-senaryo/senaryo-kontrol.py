#!/usr/bin/env python3
"""F2 senaryo kapısı: başlık ≤60 karakter, seçilen hook ≤40 kelime (~15 sn @150 kpm),
hook'ta telaffuz listesi kelimesi yok, ≥10 senaryo, ≥5 farklı açı türü, ≥7 A sütunu.
Kullanım: python3 senaryo-kontrol.py senaryolar.md"""
import re, sys
YASAK = re.compile(r"\b(charts?|complicated|scenarios?|truth|crash(es|ed|ing)?|bold)\b", re.I)
metin = open(sys.argv[1], encoding="utf-8").read()
# Yalnız senaryo bölümleri (### S01 ... ) taranır; test bölümü hariç
govde = metin.split("## Test")[0]
bloklar = re.split(r"^### (S\d\d) — ", govde, flags=re.M)[1:]
hata = 0; acilar = {}; sutun = {}
print("| ID | Alan | Metin | Karakter | Kelime | Yasak kelime | Sonuç |")
print("|---|---|---|---|---|---|---|")
for i in range(0, len(bloklar), 2):
    sid, blok = bloklar[i], bloklar[i+1]
    for alan, deger in re.findall(r"^- \*\*(Çalışma başlığı|Alternatif 1|Alternatif 2):\*\* (.+)$", blok, re.M):
        n = len(deger.strip()); ok = n <= 60; hata += not ok
        print(f"| {sid} | {alan} | {deger.strip()} | {n} | — | — | {'GEÇTİ' if ok else 'KALDI'} |")
    h = re.search(r"^- \*\*Hook \(kelimesi kelimesine, 0–15 sn\):\*\* \"(.+)\"$", blok, re.M)
    if not h:
        print(f"| {sid} | Hook | YOK | — | — | — | KALDI |"); hata += 1
    else:
        k = len(re.findall(r"[A-Za-z0-9$][\w$.,'’\-]*", h.group(1)))
        y = sorted({m.group(0).lower() for m in YASAK.finditer(h.group(1))})
        ok = k <= 40 and not y; hata += not ok
        print(f"| {sid} | Hook | (seçilen) | — | {k} | {', '.join(y) or 'yok'} | {'GEÇTİ' if ok else 'KALDI'} |")
    a = re.search(r"^- \*\*Açı türü:\*\* ([^(\n]+)", blok, re.M)
    s = re.search(r"^- \*\*Sütun:\*\* (\w)", blok, re.M)
    acilar[sid] = a.group(1).strip() if a else "?"
    sutun[sid] = s.group(1) if s else "?"
n = len(acilar); farkli = len(set(acilar.values())); a_say = sum(1 for v in sutun.values() if v == "A")
print(f"\nSenaryo sayısı: {n} (kapı ≥10) · farklı açı türü: {farkli} (kapı ≥5) · A sütunu: {a_say} (kapı ≥7)")
for sid in acilar: print(f"  {sid}: {sutun[sid]} · {acilar[sid]}")
if n < 10 or farkli < 5 or a_say < 7: hata += 1
print("KAPI:", "GEÇTİ" if hata == 0 else f"KALDI ({hata} hata)")
sys.exit(1 if hata else 0)
