#!/usr/bin/env python3
"""Gerçekçi ses adayı ölçümü (ses-yonetmeni 2026-11-11). venv: ~/.finansal-arac/venv/bin/python olc.py tarama/*.wav
Whisper small.en (16 kHz dizi) WER (hata-orani.py normu), kelime güveni, F0 ort/std (YIN), konuşma hızı (kpm),
kelime arası boşluk sayısı (>=150 ms; doğal nefes/duraklama göstergesi)."""
import json, sys, os, difflib, importlib.util, numpy as np
K = "/home/user/vitrinly/tools/ses/"
def yk(a, y):
    s = importlib.util.spec_from_file_location(a, y); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
so, ho = yk("so", K + "ses-olc.py"), yk("ho", K + "hata-orani.py")
from faster_whisper import WhisperModel
m = WhisperModel("small.en", device="cpu", compute_type="int8", local_files_only=True, cpu_threads=4)
REF = ("Every dollar we have. A hundred bucks. Jake, this is the start of something big. "
       "Or the start of a very short story. Hold on. A price is just a number until someone pays it.")
r = ho.norm(REF); sonuc = {}
for yol in sys.argv[1:]:
    x = so.yukle(yol).astype(np.float32)
    seg, _ = m.transcribe(x, beam_size=5, language="en", word_timestamps=True, condition_on_previous_text=False)
    w = [k for s in seg for k in s.words]; hyp = " ".join(k.word.strip() for k in w)
    h = ho.norm(hyp); sm = difflib.SequenceMatcher(a=r, b=h)
    hata = sum(max(i2 - i1, j2 - j1) for t, i1, i2, j1, j2 in sm.get_opcodes() if t != "equal")
    f = np.array([v for v in so.yin(x.astype(np.float64)) if v > 0]); g = np.exp(np.mean(np.log(f)))
    bos = sum(1 for a, b in zip(w, w[1:]) if b.start - a.end >= 0.15)
    kpm = 60 * len(r) / (w[-1].end - w[0].start)
    d = {"wer": round(hata / len(r), 3), "guven": round(float(np.mean([k.probability for k in w])), 3),
         "f0": round(float(g)), "f0_std_st": round(float(np.std(12 * np.log2(f / g))), 2), "kpm": round(kpm),
         "bosluk": bos, "whisper": hyp}
    sonuc[os.path.basename(yol)[:-4]] = d
    print(f"{os.path.basename(yol)[:-4]:26} WER {100*d['wer']:4.1f}%  güven {d['guven']:.3f}  F0 {d['f0']:3d} ±{d['f0_std_st']:.1f}st  {d['kpm']} kpm  boşluk {bos}", flush=True)
json.dump(sonuc, open("olcum-tarama.json", "w"), indent=1, ensure_ascii=False)
