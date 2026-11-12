#!/usr/bin/env python3
"""Kritik test ekseni için ağız çizelgesi + ağız görünür aralıklar (S01 tamamı + S12 başı; sahneler.tsx kritikParcalar ile aynı).
Kullanım: python3 -I uretim/2026-11-04-miras-sizintilari/07-animasyon/kritik-agiz.py <S12_parca_sn>"""
import json, sys
from pathlib import Path
A = Path(__file__).resolve().parent
S = {s["sahne"]: s for s in json.load(open(A / "../04-ses/sahne-zamanlari.json"))["sahneler"]}
ag = json.load(open(A / "agiz-gorunur.json"))
p12 = float(sys.argv[1]); o12 = round(S["S01"]["sure"] * 30) / 30
cues, ara = [], []
for sid, ofs, son in (("S01", 0.0, S["S01"]["sure"]), ("S12", o12, p12)):
    for c in json.load(open(A / f"rhubarb/sahne/{sid}-kapili.json"))["mouthCues"]:
        if c["start"] < son: cues.append({"start": round(c["start"] + ofs, 3), "end": round(min(c["end"], son) + ofs, 3), "value": c["value"]})
    b = S[sid]["bas"]
    for x in ag:
        if x["sahne"] == sid and x["bas"] - b < son: ara.append(f"{x['bas'] - b + ofs:.2f}-{min(x['bitis'] - b, son) + ofs:.2f}")
json.dump({"mouthCues": cues}, open(A / "log/kritik-agiz.json", "w"))
print(",".join(ara))
