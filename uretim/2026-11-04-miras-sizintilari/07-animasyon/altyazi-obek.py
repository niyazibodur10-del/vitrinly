#!/usr/bin/env python3
"""kelimeler-hizali.json → altyazi-parcalar.json (öbek ≤5 kelime / cümle sonu / ≤1,9 sn; sayı kelimeleri hl) + Shorts ek
zaman dosyaları (ham cümle zamanı) → 07-animasyon/ses-girdi/ (tools/animasyon/sahne-veri.py girdisi).
Kullanım: python3 -I uretim/2026-11-04-miras-sizintilari/07-animasyon/altyazi-obek.py"""
import json, re, shutil
from pathlib import Path
U = Path(__file__).resolve().parents[1]; G = U / "07-animasyon/ses-girdi"
SAYI = set("one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty thirty forty fifty sixty seventy eighty ninety hundred thousand million billion trillion percent half quarter".split())
w = json.load(open(U / "04-ses/kelimeler-hizali.json"))["words"]
ob, out = [], []
for i, k in enumerate(w):
    parcalar = re.split(r"-", re.sub(r"[^a-z-]", "", k["w"].lower()))
    hl = any(p in SAYI for p in parcalar) or "$" in k["w"]
    ob.append({"t": k["w"], "s": k["s"], "e": k["e"], **({"hl": True} if hl else {})})
    son = k["w"][-1] in ".?!:" or i + 1 == len(w) or w[i + 1]["sahne"] != k["sahne"]
    if son or len(ob) >= 5 or (ob[-1]["e"] - ob[0]["s"] > 1.9 and k["w"][-1] == ","):
        out.append(ob); ob = []
json.dump(out, open(G / "altyazi-parcalar.json", "w"))
for n in (1, 2):  # ek kayıt: ham cümle zamanları (ses-muhendisi son işlemi süre değiştirmiyorsa birebir)
    z = json.load(open(U / f"04-ses/shorts-{n}-ek-ham.zaman.json"))
    for c in z["cumleler"]:
        c["metin"] = re.sub(r"\[(.+?)\]\(.+?\)", r"\1", c["metin"])
    json.dump(z, open(G / f"shorts-{n}-ek-ham.zaman.json", "w"))
print(len(out), "öbek")
