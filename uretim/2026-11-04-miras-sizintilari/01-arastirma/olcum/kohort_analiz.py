#!/usr/bin/env python3
"""kohort.json -> İngilizce, ≥8 dk uzun video, 3–21 gün yaşında videoların izlenme dağılımı + kanalın ilk uzun videosu.
Kullanım: python3 -I kohort_analiz.py <kohort.json>"""
import json, re, sys, statistics as st
def sn(s):
    m = re.match(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", s); d, h, mi, se = (int(x or 0) for x in m.groups()); return d*86400+h*3600+mi*60+se
d = json.load(open(sys.argv[1])); pool = []; ilk = []; kan = 0
for k in d["kohort"]:
    uz = [v for v in k["videolar"] if sn(v["sure"]) >= 480 and (v["dil"] or "").startswith("en") and v["baslik"].isascii()]
    if not uz: continue
    kan += 1; ilk.append((uz[0]["izlenme"], uz[0]["yas_gun"], k["kanal"]))
    pool += [(v["izlenme"], v["yas_gun"], k["kanal"], v["baslik"][:60]) for v in uz if 3 <= v["yas_gun"] <= 21]
def ozet(ad, xs):
    iz = sorted(x[0] for x in xs)
    if not iz: print(ad, "n=0"); return
    q = lambda p: iz[min(len(iz)-1, int(p*len(iz)))]
    print(f"{ad}: n={len(iz)} kanal={len({x[2] for x in xs})} medyan={st.median(iz)} p25={q(.25)} p75={q(.75)} ≤10:{sum(i<=10 for i in iz)} ≤208:{sum(i<=208 for i in iz)} >1165:{sum(i>1165 for i in iz)}")
print("İngilizce uzun videolu genç kanal:", kan)
ozet("3–21 g yaşında uzun videolar", pool)
ozet("3–8 g yaşında", [x for x in pool if x[1] <= 8])
ozet("8–21 g yaşında", [x for x in pool if x[1] > 8])
ozet("kanalın ilk uzun videosu (ömür boyu, yaş≤130 g)", ilk)
