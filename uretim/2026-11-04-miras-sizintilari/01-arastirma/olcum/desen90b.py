#!/usr/bin/env python3
"""Ek kalıp testi (desen90 filtresiyle). Kullanım: desen90b.py delta90.json haric.txt"""
import json,re,statistics,sys
d=json.load(open(sys.argv[1])); H=set(open(sys.argv[2]).read().split("\n"))-{""}
r=[x for x in d['videolar_90g'] if not any(x['kanal'].startswith(h) for h in H) and x['yas_gun']>=7 and x['kanal_medyan']>=1000 and not re.search(r"[ऀ-෿؀-ۿ]",x['baslik'])]
P={"Paradoks (So why / Why hasn't / ...but)":r"so why|why hasn'?t|why isn'?t|\.\.\. (and|but|so|it'?s)|yet\b","Gizli iş modeli (actually make money / economics of / business model)":r"actually make|make money|economics of|business model|who really profits","Tarih→gelecek (before a / last time / always happens / will change / prediction)":r"before a|last time|always\"? happens|will change|prediction|is coming|about to","Rakam/$ + yıl":r"(\$|\d).*\b(19|20)\d\d\b|\b(19|20)\d\d\b.*\$"}
for k,p in P.items():
    s=[x for x in r if re.search(p,x['baslik'],re.I)]; v=[x['skor_med'] for x in s]
    if v: print(f"{k[:60]:60} n={len(v):>3} kanal={len({x['kanal'] for x in s}):>2} medyan={statistics.median(v):.2f} >=2x={sum(a>=2 for a in v)/len(v):.0%}")
v=[x['skor_med'] for x in r]; print(f"{'tüm niş':60} n={len(v)} medyan={statistics.median(v):.2f} >=2x={sum(a>=2 for a in v)/len(v):.0%}")
