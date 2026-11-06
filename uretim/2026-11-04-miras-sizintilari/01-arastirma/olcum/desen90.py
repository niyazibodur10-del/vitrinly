#!/usr/bin/env python3
"""90 gün niş desen istatistiği. Kullanım: python3 desen90.py delta90.json [haric_kanal_listesi.txt]"""
import json,re,statistics,sys
d=json.load(open(sys.argv[1]))
H=set(open(sys.argv[2]).read().split("\n"))-{""} if len(sys.argv)>2 else set()
r=[x for x in d['videolar_90g'] if not any(x['kanal'].startswith(h) for h in H) and x['yas_gun']>=7 and x['kanal_medyan']>=1000 and not re.search(r"[ऀ-෿؀-ۿ]",x['baslik'])]
print("niş n=",len(r),"kanal",len({x['kanal'] for x in r}))
def rap(ad,f):
    s=[x['skor_med'] for x in r if f(x)]
    if len(s)>=3: print(f"{ad:34} n={len(s):>3} medyan={statistics.median(s):5.2f} >=2x={sum(v>=2 for v in s)/len(s):4.0%} >=5x={sum(v>=5 for v in s):>3}")
P={"What Happens If / If":r"what happens|^if |\bif (you|america|the)","Why ...":r"\bwhy\b","How ...":r"^how\b","Here's / This is":r"here'?s|this is","Nobody/No one":r"nobody|no one","Collapse/Crisis/Crash/Bubble":r"collapse|crisis|crash|bubble|panic","Rakam/$":r"\$|\d","Yıl (19xx/20xx)":r"\b(1[6-9]\d\d|20\d\d)\b","Soru ?":r"\?","Sen/You":r"\byou(r)?\b","Ülke öznesi":r"america|u\.?s\.?\b|china|france|japan|russia|europe|uk\b|britain|germany|canada|india|saudi","Trump":r"trump","AI":r"\bai\b|nvidia|openai","Tarih/Empire/Rise-fall":r"history|empire|rise and fall|ancient|origin|richest","Zengin/Billionaire":r"rich|billionaire|wealth","Fiyat/pahalı/ev":r"expensive|price|cost|afford|housing|rent|grocer"}
for k,p in P.items():
    rap(k,lambda x,p=p:re.search(p,x['baslik'],re.I)); rap("   değil",lambda x,p=p:not re.search(p,x['baslik'],re.I))
rap("TÜMÜ BÜYÜK kelime",lambda x:re.search(r"\b[A-Z]{4,}\b",x['baslik']))
for lo,hi in [(4,10),(10,15),(15,20),(20,30),(30,60),(60,999)]: rap(f"süre {lo}-{hi} dk",lambda x,lo=lo,hi=hi:lo<=x['sure_dk']<hi)
for lo,hi in [(0,1e4),(1e4,1e5),(1e5,1e6),(1e6,1e9)]: rap(f"abone {int(lo):>9}-",lambda x,lo=lo,hi=hi:lo<=x['abone']<hi)
print("\nTOP skor_med (>=3x, >=30k):")
for x in sorted(r,key=lambda x:-x['skor_med']):
    if x['skor_med']>=3 and x['izlenme']>=30000: print(f" {x['skor_med']:6.1f}x ab={x['skor_abone']:5.2f} {x['izlenme']:>9} {x['sure_dk']:5}dk {x['yas_gun']:4.0f}g {x['id']} {x['kanal'][:22]:22}({x['abone']}) | {x['baslik'][:80]}")
print("\nTOP izlenme/abone (>=2, >=100k):")
for x in sorted(r,key=lambda x:-x['skor_abone']):
    if x['skor_abone']>=2 and x['izlenme']>=100000: print(f" ab={x['skor_abone']:6.1f} med={x['skor_med']:5.1f}x {x['izlenme']:>9} {x['sure_dk']:5}dk {x['id']} {x['kanal'][:22]:22}({x['abone']}) | {x['baslik'][:80]}")
