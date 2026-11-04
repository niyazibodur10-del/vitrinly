#!/usr/bin/env python3
"""konu-havuzu.md alan kapısı: her konuda Outlier, İlgi, Hassas, 'Neden izlenir' satırı var mı. Kullanım: alan_kontrol.py konu-havuzu.md"""
import re,sys
t=open(sys.argv[1],encoding="utf-8").read().split("## Kontrol listesi")[0]
bl=re.split(r"^### (?=[ABC]\d+\b)",t,flags=re.M)[1:]
alan={"outlier":r"\*\*Outlier","ilgi":r"\*\*İlgi","hassas":r"Hassas:\*\*","neden_izlenir":r"\*\*Neden izlenir:\*\*"}
ok=True;print("| ID | "+" | ".join(alan)+" | Sonuç |\n|---|"+"---|"*(len(alan)+1))
for b in bl:
    i=b.split()[0];r={k:bool(re.search(v,b)) for k,v in alan.items()};g=all(r.values());ok&=g
    print(f"| {i} | "+" | ".join("var" if x else "YOK" for x in r.values())+f" | {'GEÇTİ' if g else 'KALDI'} |")
print(f"\nAlan kapısı: {'GEÇTİ' if ok else 'KALDI'} ({len(bl)} konu)");sys.exit(0 if ok else 1)
