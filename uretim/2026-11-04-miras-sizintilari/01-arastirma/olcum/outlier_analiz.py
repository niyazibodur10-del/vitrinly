#!/usr/bin/env python3
"""outlier-ham.json -> son 12 ay, uzun (>=8 dk), oran=izlenme/abone >=10 tablosu. Kullanım: outlier_analiz.py outlier-ham.json [--min-oran 10] > outlier.tsv"""
import json,sys,re
d=json.load(open(sys.argv[1]));mo=float(sys.argv[sys.argv.index("--min-oran")+1]) if "--min-oran" in sys.argv else 10
q_of={}
for q,ids in d["sorgular"].items():
    for i in ids:q_of.setdefault(i,[]).append(q)
rows=[]
for i,v in d["videolar"].items():
    s=d["kanallar"].get(v["cid"],0)
    if v["pub"]<"2025-11-04" or v["sn"]<480 or s<1000:continue
    r=v["v"]/s
    if r<mo:continue
    rows.append((r,v["v"],s,v["pub"],v["sn"]//60,v["dil"],v["ch"],v["t"],i,q_of.get(i,[""])[0]))
rows.sort(reverse=True)
print("oran\tizlenme\tabone\ttarih\tdk\tdil\tkanal\tbaslik\tid\tsorgu")
for r in rows:print("%.1f\t%d\t%d\t%s\t%d\t%s\t%s\t%s\t%s\t%s"%r)
n=sum(1 for i,v in d["videolar"].items() if v["pub"]>="2025-11-04" and v["sn"]>=480)
print(f"# toplam video {len(d['videolar'])}, son12ay+uzun {n}, oran>={mo}: {len(rows)}",file=sys.stderr)
