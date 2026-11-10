#!/usr/bin/env python3
"""Diyalog aday ölçümü (ses-yonetmeni 2026-11-10).
Kullanım: ~/.finansal-arac/venv/bin/python -I olc.py aday/*.wav  → olcum.json + tablo (stdout)
Her aday için: konuşmacı izinde (tools/ses/diyalog.py çıktısı) F0 ort/std (YIN, ses-olc.py), spektral merkez;
ayrışma = |12·log2(F0_mike/F0_jake)| yarım ton + merkez farkı; satır başına Whisper small.en WER (hata-orani.py normu);
kpm (konuşmacı başına: kelime / konuşma süresi); tam dosya LUFS + true peak (ffmpeg ebur128).
"""
import json, os, re, subprocess, sys, tempfile, importlib.util
import numpy as np, soundfile as sf
K = "/home/user/vitrinly/tools/ses/"
def yukle(ad, yol):
    s = importlib.util.spec_from_file_location(ad, yol); m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
so, ho = yukle("so", K + "ses-olc.py"), yukle("ho", K + "hata-orani.py")
sys.path.insert(0, K); from importlib import import_module

from faster_whisper import WhisperModel
model = WhisperModel("small.en", device="cpu", compute_type="int8", local_files_only=True, cpu_threads=4)

def f0(y16):
    f = so.yin(y16); f = np.array([x for x in f if x > 0])
    return float(np.exp(np.mean(np.log(f)))), float(np.std(12 * np.log2(f / np.exp(np.mean(np.log(f))))))
def merkez(y, sr):
    k = 2048; S = np.abs(np.fft.rfft(y[: len(y) // k * k].reshape(-1, k) * np.hanning(k), axis=1))
    e = S.sum(1); S = S[e > np.percentile(e, 40)]; fr = np.fft.rfftfreq(k, 1 / sr)
    return float((S * fr).sum() / S.sum())
def lufs(yol):
    o = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", yol, "-af", "ebur128=peak=true", "-f", "null", "-"], capture_output=True, text=True).stderr
    o = o[o.rfind("Summary"):]
    return float(re.search(r"I:\s+(-?[\d.]+)", o).group(1)), float(re.search(r"Peak:\s+(-?[\d.]+)", o).group(1))
def norm(t): return ho.norm(t) if hasattr(ho, "norm") else t.lower().split()

sonuc = {}
for yol in sys.argv[1:]:
    ad = os.path.basename(yol)[:-4]; z = json.load(open(yol[:-4] + ".zaman.json"))
    y, sr = sf.read(yol, dtype="float32"); r = {"sure": z["sure"], "sesler": z["sesler"]}
    r["lufs"], r["tp"] = lufs(yol)
    for k in ("JAKE", "MIKE"):
        yk = sf.read(yol[:-4] + f"-{k}.wav", dtype="float32")[0]
        y16 = so.yukle(yol[:-4] + f"-{k}.wav")
        r[k] = dict(zip(("f0_hz", "f0_std_st"), f0(y16))); r[k]["merkez_hz"] = merkez(yk, sr)
        sat = [s for s in z["satirlar"] if s["konusmaci"] == k]
        r[k]["kpm"] = 60 * sum(len(s["metin"].split()) for s in sat) / sum(s["bitis"] - s["bas"] for s in sat)
    hata = top = 0; r["satir_hata"] = []
    for s in z["satirlar"]:
        parca = y[int(s["bas"] * sr): int(s["bitis"] * sr)]
        with tempfile.NamedTemporaryFile(suffix=".wav") as f:
            sf.write(f.name, parca, sr); seg, _ = model.transcribe(so.yukle(f.name).astype(np.float32), beam_size=5, language="en", condition_on_previous_text=False)
            hyp = " ".join(x.text for x in seg).strip()
        a, b = ho.norm(s["metin"]), ho.norm(hyp)
        import difflib
        sm = difflib.SequenceMatcher(a=a, b=b); h = sum(max(i2 - i1, j2 - j1) for t, i1, i2, j1, j2 in sm.get_opcodes() if t != "equal")
        hata += h; top += len(a)
        if h: r["satir_hata"].append({"no": s["no"], "ref": s["metin"], "whisper": hyp})
    r["wer"] = hata / top
    r["ayrisma_st"] = abs(12 * np.log2(r["MIKE"]["f0_hz"] / r["JAKE"]["f0_hz"]))
    sonuc[ad] = r
    print(f"{ad}: {r['sesler']['JAKE']:>16} {r['JAKE']['f0_hz']:5.0f}Hz ±{r['JAKE']['f0_std_st']:.1f}st {r['JAKE']['merkez_hz']:5.0f}c {r['JAKE']['kpm']:4.0f}kpm | "
          f"{r['sesler']['MIKE']:>15} {r['MIKE']['f0_hz']:5.0f}Hz ±{r['MIKE']['f0_std_st']:.1f}st {r['MIKE']['merkez_hz']:5.0f}c {r['MIKE']['kpm']:4.0f}kpm | "
          f"ayr {r['ayrisma_st']:.1f}st  WER {100*r['wer']:.1f}%  {r['sure']:.1f}s  {r['lufs']}LUFS TP{r['tp']}", flush=True)
json.dump(sonuc, open("olcum.json", "w"), indent=1, ensure_ascii=False)
