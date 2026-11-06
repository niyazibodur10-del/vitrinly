#!/usr/bin/env python3
"""Tüm sahneler + Shorts ek kayıtları için Rhubarb (PocketSphinx, --dialogFile) + sessizlik kapısı.
Girdi: 04-ses/rhubarb/Sxx.wav/.txt (ses-muhendisi, 16 kHz kesitler; sahneler.json ofsetleri), 04-ses/shorts-*-ek.wav/.txt
Çıktı: 07-animasyon/rhubarb/sahne/<ad>.json (ham) ve <ad>-kapili.json; rhubarb/tum-kapili.json (anlatim.wav zamanında birleşik)
Kullanım: python3 rhubarb-tum.py [eşzamanlı=2]   (her iş ~5–25 sn; müzik/render ile CPU paylaşımı için 2)"""
import json, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from sessizlik_kapisi import sessizlik, uygula  # noqa: E402
U = Path(__file__).resolve().parents[1]
R = U / "04-ses/rhubarb"; O = U / "07-animasyon/rhubarb/sahne"; O.mkdir(parents=True, exist_ok=True)
RH = Path.home() / ".finansal-arac/rhubarb/build/rhubarb/rhubarb"
sah = json.load(open(R / "sahneler.json"))["sahneler"]
isler = [(s["sahne"], R / s["wav"], R / s["metin"], s["ofset_sn"]) for s in sah]
for n in (1, 2):
    isler.append((f"shorts-{n}-ek", U / f"04-ses/shorts-{n}-ek.wav", U / f"04-ses/shorts-{n}-ek.txt", None))

def calis(is_):
    ad, wav, txt, ofs = is_
    ham = O / f"{ad}.json"
    if not ham.exists():
        subprocess.run([str(RH), "-r", "pocketSphinx", "-f", "json", "--dialogFile", str(txt), "-o", str(ham), str(wav)], check=True, capture_output=True)
    c = uygula(json.load(open(ham))["mouthCues"], sessizlik(str(wav)))
    json.dump({"mouthCues": c}, open(O / f"{ad}-kapili.json", "w"))
    print(ad, len(c), flush=True)
    return ad, ofs, c

with ThreadPoolExecutor(int(sys.argv[1]) if len(sys.argv) > 1 else 2) as ex:
    sonuc = list(ex.map(calis, isler))
tum = []
for ad, ofs, c in sonuc:
    if ofs is None: continue
    tum += [{"start": round(x["start"] + ofs, 3), "end": round(x["end"] + ofs, 3), "value": x["value"]} for x in c]
json.dump({"mouthCues": tum}, open(U / "07-animasyon/rhubarb/tum-kapili.json", "w"))
print("toplam ipucu", len(tum))
