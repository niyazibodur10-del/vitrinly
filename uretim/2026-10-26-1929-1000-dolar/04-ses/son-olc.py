#!/usr/bin/env python3
"""ses-muhendisi son işlem ölçümü: ebur128 (I, LRA, TP), gürültü tabanı (cümle arası sessizlik RMS, zaman.json'dan),
spektral bant payı (sibilans 5-9 kHz, çamur 200-400 Hz, varlık 2-4 kHz; yalnız konuşma bölgeleri), tepe.
Kullanım: ~/.finansal-arac/venv/bin/python son-olc.py <wav> [anlatim-ham.zaman.json]"""
import sys, json, re, subprocess, numpy as np, soundfile as sf
wav = sys.argv[1]; zj = sys.argv[2] if len(sys.argv) > 2 else None
o = subprocess.run(["ffmpeg","-hide_banner","-nostats","-i",wav,"-af","ebur128=peak=true","-f","null","-"],capture_output=True,text=True).stderr
s = o[o.rfind("Summary"):]
I = float(re.search(r"I:\s+(-?[\d.]+)", s).group(1)); LRA = float(re.search(r"LRA:\s+(-?[\d.]+)", s).group(1))
TP = float(re.search(r"Peak:\s+(-?[\d.]+|-inf)", s).group(1))
y, sr = sf.read(wav, always_2d=True); y = y.mean(1)
r = {"dosya": wav, "sure": round(len(y)/sr, 2), "I": I, "LRA": LRA, "TP": TP, "ornek_tepe_dbfs": round(20*np.log10(np.abs(y).max()), 2)}
if zj:
    C = json.load(open(zj))["cumleler"]
    sess = [(C[i]["son"]+0.06, C[i+1]["bas"]-0.06) for i in range(len(C)-1) if C[i+1]["bas"]-C[i]["son"] > 0.25]
    seg = np.concatenate([y[int(a*sr):int(b*sr)] for a, b in sess])
    r["gurultu_tabani_dbfs"] = round(20*np.log10(np.sqrt(np.mean(seg**2))+1e-12), 1); r["sessiz_sn"] = round(len(seg)/sr, 1)
    kon = np.concatenate([y[int(c["bas"]*sr):int(c["son"]*sr)] for c in C])
    n = 4096; fr = np.lib.stride_tricks.sliding_window_view(kon, n)[::n]
    P = (np.abs(np.fft.rfft(fr*np.hanning(n), axis=1))**2).mean(0); f = np.fft.rfftfreq(n, 1/sr); tot = P[(f>60)&(f<16000)].sum()
    band = lambda a, b: round(10*np.log10(P[(f>=a)&(f<b)].sum()/tot), 2)
    r.update(camur_200_400_db=band(200,400), varlik_2k_4k_db=band(2000,4000), sibilans_5k_9k_db=band(5000,9000), hava_9k_16k_db=band(9000,16000))
    # sibilans tepe: 20 ms çerçevede 5-9 kHz enerjisinin tüm-bant enerjisine oranı, %99 dilimi (sert "s" anları)
    m = 960; fr2 = np.lib.stride_tricks.sliding_window_view(kon, m)[::m]; F = np.abs(np.fft.rfft(fr2*np.hanning(m), axis=1))**2; f2 = np.fft.rfftfreq(m, 1/sr)
    ss = F[:, (f2>=5000)&(f2<9000)].sum(1); tt = F[:, (f2>60)&(f2<16000)].sum(1)+1e-12; v = tt > np.percentile(tt, 30)
    r["sibilans_p99_db"] = round(10*np.log10(np.percentile(ss[v]/tt[v], 99)), 2)
print(json.dumps(r, ensure_ascii=False))
