#!/usr/bin/env python3
"""Flip By Vote — iki sesli diyalog üretici (Kokoro-82M, yerel). Seri şablonunun test/demo sesi ve ses-yonetmeni'nin
çıktı biçimi örneği. Gerçek bölüm sesini ses-yonetmeni üretir; biçim aynı olmalıdır.

Kullanım:
  ~/.finansal-arac/kokoro-venv/bin/python -I tools/seri/demo-diyalog.py <satirlar-girdi.json> <diyalog.wav> <satirlar.json>
      [--bas 0.5] [--bosluk 0.25] [--ses jake=am_michael:1.0 --ses mike=am_puck:1.05]
  Girdi: [{"konusmaci": "jake", "metin": "..."} , ...]
  Çıktı: diyalog.wav (48 kHz mono PCM16) + satirlar.json:
    {"ses": "diyalog.wav", "sure": 12.3, "satirlar": [{"konusmaci","bas","bitis","metin","kelimeler":[{"k","bas","bitis"}]}]}
    Zamanlar saniye, wav başına göre. "kelimeler" Kokoro token zamanlarıdır (yoksa alan yazılmaz; şablon orantılı dağıtır).
Seçim (2026-11-10): Kokoro satır satır + sabit boşluk (aday 2: tek parça üretip Whisper ile bölme — satır sınırı ve konuşmacı
bilgisi kaybolur, elendi; aday 3: espeak — kalite düşük, elendi).
"""
import argparse, json
import numpy as np, soundfile as sf

SR = 24000


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("girdi"); ap.add_argument("wav"); ap.add_argument("json")
    ap.add_argument("--bas", type=float, default=0.5)
    ap.add_argument("--bosluk", type=float, default=0.25)
    ap.add_argument("--ses", action="append", default=[])
    a = ap.parse_args()
    sesler = {"jake": ("am_michael", 1.0), "mike": ("am_puck", 1.05)}
    for s in a.ses:
        k, v = s.split("=", 1); ad, hiz = v.split(":")
        sesler[k] = (ad, float(hiz))
    satirlar = json.load(open(a.girdi, encoding="utf-8"))
    import torch
    torch.set_num_threads(2)
    from kokoro import KPipeline
    pipe = KPipeline(lang_code="a", repo_id="hexgrad/Kokoro-82M")
    parcalar = [np.zeros(int(a.bas * SR), np.float32)]
    t = a.bas; cikis = []
    for s in satirlar:
        ses, hiz = sesler[s["konusmaci"]]
        ys, kel, ofs = [], [], 0.0
        for r in pipe(s["metin"], voice=ses, speed=hiz, split_pattern=None):
            y = r.audio.numpy() if hasattr(r.audio, "numpy") else np.asarray(r.audio)
            for tok in (r.tokens or []):
                if tok.start_ts is not None and tok.end_ts is not None and any(c.isalnum() for c in tok.text):
                    kel.append({"k": tok.text, "bas": ofs + tok.start_ts, "bitis": ofs + tok.end_ts})
            ys.append(y.astype(np.float32)); ofs += len(y) / SR
        y = np.concatenate(ys)
        nz = np.where(np.abs(y) > 10 ** (-50 / 20))[0]
        kirp = max(nz[0] - 720, 0) if len(nz) else 0
        if len(nz):
            y = y[kirp: nz[-1] + 1200]
        f = min(120, len(y) // 4); y[:f] *= np.linspace(0, 1, f); y[-f:] *= np.linspace(1, 0, f)
        d = len(y) / SR; k0 = kirp / SR
        sat = {"konusmaci": s["konusmaci"], "bas": round(t, 3), "bitis": round(t + d, 3), "metin": s["metin"]}
        if kel:
            sat["kelimeler"] = [{"k": w["k"], "bas": round(t + max(0, w["bas"] - k0), 3),
                                 "bitis": round(t + min(d, w["bitis"] - k0), 3)} for w in kel]
        cikis.append(sat)
        parcalar += [y, np.zeros(int(a.bosluk * SR), np.float32)]
        t += d + a.bosluk
    ses = np.concatenate(parcalar)
    import subprocess, tempfile, os
    with tempfile.TemporaryDirectory() as td:
        ham = os.path.join(td, "ham.wav"); sf.write(ham, ses, SR, subtype="FLOAT")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", ham, "-ar", "48000", "-ac", "1", "-c:a", "pcm_s16le", a.wav], check=True)
    json.dump({"ses": os.path.basename(a.wav), "sure": round(len(ses) / SR, 3), "satirlar": cikis},
              open(a.json, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(f"{len(cikis)} satır, {len(ses) / SR:.2f} sn")


if __name__ == "__main__":
    main()
