#!/usr/bin/env python3
"""Kelime zamanlı transkript (faster-whisper, CPU int8; yerel model önbelleği).

Kullanım: ~/.finansal-arac/venv/bin/python tools/ses/yaziya-dok.py <ses> <cikis.json> [small.en|medium.en]
Çıkış: {"text": ..., "words": [{"w","s","e","p"}]}; metin stdout'a.

Model yükleme önce yalnız yerel önbellekten (local_files_only) denenir; önbellek yoksa indirir.
Neden (2026-10-27, uretim-muhendisi): ağ/proxy yavaşken HF etag sorgusu bekletiyordu ve hata
mesajsız çıkış "Whisper başarısız" diye raporlanıyordu. Önbellek kurulum.sh ile dolduruluyor.
Not: yeni açılan konteynerde ilk yükleme disk soğukken yavaştır (ölçüm: small.en 44 sn ilk / 3,5 sn
sonra; medium.en ilk 136 sn) — bu hata değildir, zaman aşımı koyan çağıran bunu hesaba katmalı.
"""
import json, os, subprocess, sys

if len(sys.argv) < 3:
    sys.exit(__doc__)
giris, cikis = sys.argv[1], sys.argv[2]
model_adi = sys.argv[3] if len(sys.argv) > 3 else "small.en"
if not os.path.isfile(giris):
    sys.exit(f"HATA: ses dosyası yok: {giris}")

import numpy as np
from faster_whisper import WhisperModel

try:
    m = WhisperModel(model_adi, device="cpu", compute_type="int8", local_files_only=True)
except Exception as e:  # önbellekte yok → indir
    print(f"[yaziya-dok] yerel önbellekte yok ({type(e).__name__}); indiriliyor: {model_adi}", file=sys.stderr)
    m = WhisperModel(model_adi, device="cpu", compute_type="int8")

r = subprocess.run(["ffmpeg", "-v", "error", "-i", giris, "-ac", "1", "-ar", "16000", "-f", "f32le", "-"],
                   capture_output=True)
if r.returncode != 0 or not r.stdout:
    sys.exit(f"HATA: ffmpeg sesi çözemedi: {r.stderr.decode(errors='replace').strip()[:300]}")
audio = np.frombuffer(r.stdout, dtype=np.float32)
segs, info = m.transcribe(audio, language="en", word_timestamps=True, beam_size=5, condition_on_previous_text=False)
words = []; text = []
for s in segs:
    text.append(s.text.strip())
    for w in s.words:
        words.append({"w": w.word.strip(), "s": round(w.start, 3), "e": round(w.end, 3), "p": round(w.probability, 3)})
if not words:
    print("[yaziya-dok] UYARI: hiç kelime çıkmadı (sessiz/boş ses?)", file=sys.stderr)
elif sum(w["p"] for w in words) / len(words) < 0.3:  # sessizlikte Whisper "You" gibi uydurur (p≈0,1)
    print("[yaziya-dok] UYARI: ortalama kelime güveni < 0,3 — sessiz/gürültülü ses veya halüsinasyon olabilir", file=sys.stderr)
with open(cikis, "w") as f:
    json.dump({"text": " ".join(text), "words": words}, f, indent=1)
print(" ".join(text))
