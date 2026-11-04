#!/usr/bin/env python3
"""Kanal sıralaması (90 g): A = medyan(izlenme)/abone, B = >=3x video oranı. Kullanım: sirala90.py delta90.json haric.txt"""
import json,statistics,sys
d=json.load(open(sys.argv[1])); H=set(open(sys.argv[2]).read().split("\n"))-{""}
R=[]
for cid,m in d['medyanlar'].items():
    if m['medyan']<1000 or m['abone']<1000 or any(m['ad'].startswith(h) for h in H): continue
    v=[x for x in d['videolar_90g'] if x['kanal_id']==cid and x['yas_gun']>=7]
    if len(v)<3: continue
    R.append(dict(ad=m['ad'],abone=m['abone'],acilis=m['acilis'],n=len(v),A=statistics.median(x['izlenme'] for x in v)/m['abone'],B=sum(x['skor_med']>=3 for x in v)/len(v),medyan=m['medyan'],sh=d['shorts'][cid]['n90']))
ra={r['ad']:i+1 for i,r in enumerate(sorted(R,key=lambda r:-r['A']))}; rb={r['ad']:i+1 for i,r in enumerate(sorted(R,key=lambda r:-r['B']))}
for r in sorted(R,key=lambda r:ra[r['ad']]+rb[r['ad']])[:15]:
    print(f"{r['ad'][:24]:24} ab={r['abone']:>8} açılış={r['acilis']} n90={r['n']:>3} A={r['A']:.2f}(#{ra[r['ad']]}) B={r['B']:.0%}(#{rb[r['ad']]}) medyan={int(r['medyan'])} shorts90={r['sh']}")
print("toplam kanal",len(R))
