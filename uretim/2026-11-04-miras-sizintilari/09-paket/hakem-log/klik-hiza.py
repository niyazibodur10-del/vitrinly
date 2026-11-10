#!/usr/bin/env python3
"""Hakem: abone düğmesi renk dönüş karesi (kırmızı→gri, 30 fps) ↔ klik sesi başlangıcı (2 kHz üstü enerji sıçraması).
Kullanım: klik-hiza.py video.mp4 taraf:yaklaşık_sn [...]   taraf = sol|sag|dikey"""
import subprocess, sys, numpy as np
v = sys.argv[1]
w, h = [int(x) for x in subprocess.check_output(["ffprobe","-v","error","-select_streams","v:0","-show_entries","stream=width,height","-of","csv=p=0",v]).decode().strip().split(",") if x][:2]
for arg in sys.argv[2:]:
    taraf, t0 = arg.split(":"); t0 = float(t0); bas = max(0, t0 - 1.5); sure = 3.0
    if taraf == "dikey": x0, x1 = 70+int(342*1.2), 70+int(592*1.2)
    elif taraf == "sol": x0, x1 = 398, 648
    else: x0, x1 = w-56-672+342, w-56-672+592
    raw = subprocess.run(["ffmpeg","-nostdin","-v","error","-ss",f"{bas}","-i",v,"-t",f"{sure}","-vf","fps=30","-f","rawvideo","-pix_fmt","rgb24","-"], capture_output=True).stdout
    kar = np.frombuffer(raw, np.uint8).reshape(-1, h, w, 3)[:, :, x0:x1].astype(int)
    kir = ((abs(kar[...,0]-227) < 30) & (kar[...,1] < 70) & (kar[...,2] < 80)).reshape(len(kar), -1).sum(1)
    tepe = kir.max(); i = int(np.argmax(kir)); 
    j = next((k for k in range(i, len(kir)) if kir[k] < 0.2 * tepe), None)
    gt = bas + j / 30 if j is not None else None
    a = subprocess.run(["ffmpeg","-nostdin","-v","error","-ss",f"{bas}","-i",v,"-t",f"{sure}","-af","highpass=f=2000,highpass=f=2000","-ac","1","-ar","48000","-f","s16le","-"], capture_output=True).stdout
    s = np.frombuffer(a, np.int16).astype(float); hop = 240
    e = np.array([np.sqrt((s[k:k+hop]**2).mean()) for k in range(0, len(s)-hop, hop)])
    d = np.diff(e); k = int(np.argmax(d)); at = bas + (k+1) * hop / 48000
    fark = (at - gt) * 30 if gt else float("nan")
    print(f"{v} {taraf}@{t0}: düğme dönüş {gt:.3f} sn · klik ses başı {at:.3f} sn · fark {fark:+.1f} kare {'OK' if abs(fark) <= 2 else 'KALDI'}")
