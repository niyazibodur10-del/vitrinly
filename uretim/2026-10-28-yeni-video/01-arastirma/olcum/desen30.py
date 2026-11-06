#!/usr/bin/env python3
"""Son 30 gün niş alt kümesinde başlık/süre/sütun desen istatistiği (kanal içi skor).
Kullanım: python3 desen30.py delta-veri.json"""
import json,re,statistics,sys
d=json.load(open(sys.argv[1]))
N={"Patrick Boyle","ColdFusion","How Money Works","Economics Explained","Moon","Grant Rudow","Internet Education","The Infographics Show","Damon Cassidy","Mark Tilbury Economics","Money & Macro","Fin Tek","Wall Street Millennial","Finance Bureau","Markets of the Past","Bald Guy Money","Econoclasts","Marcus Explains","Meerkat Explains","Chill Financial Historian","Finance Economist","America Prime"," Fred - Money Historian","Jack McAllister","Joe Blogs","Eurodollar University","Geopolitical Economy Report","Cyrus Janssen"}
r=[x for x in d['videolar_30g'] if x['kanal'] in N and x['yas_gun']>=3]
A=re.compile(r"\b(1[0-9]{3})\b|history|historian|hitler|ancient|empire|origin|rise and fall|went bankrupt|died",re.I)
C=re.compile(r"what happens if|\bwill\b|future|\bcould\b|20(2[7-9]|3\d)|about to|is coming|coming|next|before it|is going to|starting|only getting started",re.I)
def sutun(t): return "C" if C.search(t) else ("A" if A.search(t) else "B")
def rap(ad,f):
    s=[x['skor'] for x in r if f(x)]
    if len(s)>=3: print(f"{ad:38} n={len(s):>3} medyan={statistics.median(s):5.2f} >=2x={sum(v>=2 for v in s):>3} ({sum(v>=2 for v in s)/len(s):.0%})")
print("niş alt küme n=",len(r),"kanal",len({x['kanal'] for x in r}))
for k in "ABC": rap(f"sütun {k}",lambda x,k=k:sutun(x['baslik'])==k)
P={"What Happens If / If X":r"what happens if|^if ","Why ... (soru/neden)":r"^why|\bwhy\b","Here's Why / What Happened":r"here'?s (why|what)","Nobody / No One":r"nobody|no one","Collapse/Crisis/Bubble/Crash":r"collapse|crisis|bubble|crash|apocalypse|panic","Tamamı BÜYÜK kelime (>=4 harf)":r"\b[A-Z]{4,}\b","Rakam/$ içeren":r"\$|\d","Soru işareti":r"\?","Ülke/şehir öznesi":r"america|canada|france|china|russia|saudi|italy|europe|japan|india|uk\b|britain|germany","Trump":r"trump","AI":r"\bai\b|anthropic|openai|oracle|nvidia"}
for k,p in P.items():
    rap(k,lambda x,p=p:re.search(p,x['baslik'],re.I if 'A-Z' not in p else 0)); rap("  değil: "+k,lambda x,p=p:not re.search(p,x['baslik'],re.I if 'A-Z' not in p else 0))
for lo,hi in [(4,10),(10,15),(15,20),(20,30),(30,60),(60,999)]: rap(f"süre {lo}-{hi} dk",lambda x,lo=lo,hi=hi:lo<=x['sure_dk']<hi)
print("B/C outlier (>=3x, >=20k):")
for x in sorted(r,key=lambda x:-x['skor']):
    if x['skor']>=3 and x['izlenme']>=20000 and sutun(x['baslik'])!="A": print(" ",sutun(x['baslik']),x['id'],x['skor'],x['kanal'],"|",x['baslik'][:70])
