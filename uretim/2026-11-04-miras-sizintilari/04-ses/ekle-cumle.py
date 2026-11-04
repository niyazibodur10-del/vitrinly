#!/usr/bin/env python3
"""Tek cümle değiştirme (ses-yonetmeni 2026-11-02): ham anlatımda cümle i'nin sesini başka bir tts.py çıktısındaki cümle j ile
değiştirir, sonraki zamanları kaydırır. Tam yeniden üretim (~6 dk) yerine. Kullanım:
  kokoro-venv/bin/python ekle-cumle.py <ham.wav> <ham.zaman.json> <i> <kaynak.wav> <kaynak.zaman.json> <j>"""
import json, sys, numpy as np, soundfile as sf
hw, hz, i, kw, kz, j = sys.argv[1], sys.argv[2], int(sys.argv[3]), sys.argv[4], sys.argv[5], int(sys.argv[6])
y, sr = sf.read(hw); k, sr2 = sf.read(kw); assert sr == sr2
Z = json.load(open(hz)); K = json.load(open(kz))["cumleler"][j]; c = Z["cumleler"][i]
a, b = round(c["bas"] * sr), round(c["son"] * sr); yeni = k[round(K["bas"] * sr):round(K["son"] * sr)]
d = (len(yeni) - (b - a)) / sr
sf.write(hw, np.concatenate([y[:a], yeni, y[b:]]), sr, subtype=sf.info(hw).subtype)
c["metin"] = K["metin"]; c["son"] = round(c["bas"] + len(yeni) / sr, 3)
for x in Z["cumleler"][i + 1:]:
    x["bas"] = round(x["bas"] + d, 3); x["son"] = round(x["son"] + d, 3)
json.dump(Z, open(hz, "w"), indent=1, ensure_ascii=False); print(f"cümle {i} değişti, kayma {d:+.3f} sn")
