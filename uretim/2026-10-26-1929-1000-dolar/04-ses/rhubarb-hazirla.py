#!/usr/bin/env python3
"""Rhubarb girdileri (ses-muhendisi): anlatim.wav + kilitli metin -> rhubarb/
  rhubarb/anlatim.txt          tüm anlatımın düz metni (telaffuz işaretsiz kilitli metin)
  rhubarb/Sxx.wav / Sxx.txt    sahne başına 16 kHz mono PCM16 kesit + o sahnenin düz metni (--dialogFile)
  rhubarb/sahneler.json        sahne -> kesit başlangıcı (sn, anlatim.wav ekseninde) — Rhubarb çıktısındaki zamanlara bu ofset eklenir
Kesitler sahne-zamanlari.json bas/bitis (sahne arası sessizlik öndeki sahnede) → kesitler uç uca, boşluk/çakışma yok.
Kullanım (04-ses içinde): python3 -I rhubarb-hazirla.py   (wav'lar git dışı; bu betikle yeniden üretilir)"""
import json, os, re, subprocess
B = os.path.dirname(os.path.abspath(__file__)); O = os.path.join(B, "rhubarb"); os.makedirs(O, exist_ok=True)
temiz = lambda m: re.sub(r"\[([^\]]+)\]\(/[^)]*/\)", r"\1", m)
C = json.load(open(os.path.join(B, "anlatim-ham.zaman.json")))["cumleler"]
SZ = json.load(open(os.path.join(B, "sahne-zamanlari.json")))["sahneler"]
open(os.path.join(O, "anlatim.txt"), "w").write(open(os.path.join(B, "referans-metni.txt")).read())
kayit = []
for s in SZ:
    metin = " ".join(temiz(C[i]["metin"]) for i in range(s["cumle_ilk"], s["cumle_son"] + 1))
    open(os.path.join(O, f"{s['sahne']}.txt"), "w").write(metin + "\n")
    subprocess.run(["ffmpeg", "-hide_banner", "-v", "error", "-y", "-ss", str(s["bas"]), "-to", str(s["bitis"]), "-i", os.path.join(B, "anlatim.wav"),
                    "-ar", "16000", "-ac", "1", "-c:a", "pcm_s16le", os.path.join(O, f"{s['sahne']}.wav")], check=True)
    kayit.append({"sahne": s["sahne"], "ofset_sn": s["bas"], "sure_sn": round(s["bitis"] - s["bas"], 3), "wav": f"{s['sahne']}.wav", "metin": f"{s['sahne']}.txt"})
json.dump({"kaynak": "anlatim.wav (48 kHz) -> 16 kHz PCM16 kesitler", "komut": "rhubarb -r pocketSphinx --dialogFile Sxx.txt -f json -o Sxx.json Sxx.wav", "sahneler": kayit},
          open(os.path.join(O, "sahneler.json"), "w"), ensure_ascii=False, indent=1)
print(f"{len(kayit)} sahne kesiti, toplam {sum(k['sure_sn'] for k in kayit):.2f} sn")
