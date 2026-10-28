#!/usr/bin/env python3
"""Konuşan Leo'nun ağzının ekranda göründüğü aralıklar (anlatim.wav global sn) — b1–b4.tsx sahne mantığıyla aynı kelime çapaları.
Çıktı: agiz-gorunur.json + senkron-testi.py --araliklar dizgesi. Sahne kodu değişirse burası da güncellenir."""
import json, re
from pathlib import Path
U = Path(__file__).resolve().parents[1]
Z = {s["sahne"]: s for s in json.load(open(U / "04-ses/sahne-zamanlari.json"))["sahneler"]}
K = json.load(open(U / "04-ses/kelimeler-hizali.json"))["words"]
norm = lambda w: re.sub(r"[^a-z0-9$'-]", "", w.lower())
def an(sid, w, n=1):
    say = 0
    for k in K:
        if k["sahne"] == sid and norm(k["w"]) == norm(w):
            say += 1
            if say == n: return k["s"] - Z[sid]["bas"]
    raise SystemExit(f"{sid}: {w}#{n} yok")
tam = lambda s: (0, Z[s]["sure"])
A = {
    "S01": (2.1, Z["S01"]["sure"]), "S02": tam("S02"), "S03": tam("S03"),
    "S04": (an("S04", "remember") - 0.1, an("S04", "door", 4) - 0.1),
    "S08": (0, an("S08", "and", 1) - 0.2), "S11": (0, an("S11", "one", 2) - 0.2), "S13": (0, an("S13", "while") - 0.2),
    "S16": tam("S16"), "S17": tam("S17"), "S19": (an("S19", "now") - 0.2, an("S19", "let's", 2) - 0.2),
    "S21": tam("S21"), "S23": tam("S23"), "S24": tam("S24"),
}
out = [{"sahne": s, "bas": round(Z[s]["bas"] + a, 2), "bitis": round(Z[s]["bas"] + b, 2)} for s, (a, b) in A.items()]
json.dump(out, open(U / "07-animasyon/agiz-gorunur.json", "w"), indent=1)
print(",".join(f"{o['bas']}-{o['bitis']}" for o in out))
print(f"toplam {sum(o['bitis'] - o['bas'] for o in out):.1f} sn", flush=True)
