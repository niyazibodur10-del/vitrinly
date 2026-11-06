#!/usr/bin/env python3
"""Hakem: abone kartı dedektörü (tüm kare tarama değil, kart düğmesi kutusu): düğme kırmızı #e3202a VEYA abone gri #3a3a3d,
kutu içinde ≥%35 doluluk; kutu x'i AboneOl.tsx yerleşiminden (sol/sağ/dikey), y her satırda kayan pencere. 4 fps, 1/2 ölçek.
Ek: aynı karede tüm görüntüdeki kırmızı piksel sayısı (yanlış pozitif kontrolü için). Kullanım: abone-say.py video.mp4"""
import subprocess, sys, numpy as np
v = sys.argv[1]
w, h = [int(x) for x in subprocess.check_output(["ffprobe","-v","error","-select_streams","v:0","-show_entries","stream=width,height","-of","csv=p=0",v]).decode().strip().split(",") if x][:2]
S = 2; W, H = w // S, h // S
if w > h: kutular = {"sol": (56+342, 56+342+250), "sag": (w-56-672+342, w-56-672+342+250)}; bh = 66
else:     kutular = {"dikey": (70+int(342*1.2), 70+int(592*1.2))}; bh = int(66*1.2)
p = subprocess.Popen(["ffmpeg","-nostdin","-v","error","-i",v,"-vf",f"fps=4,scale={W}:{H}","-f","rawvideo","-pix_fmt","rgb24","-"], stdout=subprocess.PIPE)
n, hits = 0, []
while True:
    b = p.stdout.read(W * H * 3)
    if len(b) < W * H * 3: break
    a = np.frombuffer(b, np.uint8).reshape(H, W, 3).astype(int)
    kir = (abs(a[...,0]-227) < 30) & (a[...,1] < 70) & (a[...,2] < 80)
    gri = (abs(a[...,0]-58) < 12) & (abs(a[...,1]-58) < 12) & (abs(a[...,2]-61) < 12)
    for ad, (x0, x1) in kutular.items():
        m = (kir | gri)[:, x0//S:x1//S]
        sat = m.sum(1); k = bh // S
        pen = np.convolve(sat, np.ones(k, int), "valid")
        y = int(pen.argmax()); dol = pen[y] / (k * (x1 - x0) / S)
        if dol >= 0.35:
            kr = kir[y:y+k, x0//S:x1//S].mean(); gr = gri[y:y+k, x0//S:x1//S].mean()
            hits.append((n/4, ad, y*S, round(dol,2), "KIRMIZI" if kr > gr else "GRI"))
    n += 1
olay = []
for t, ad, y, d, r in hits:
    if olay and t - olay[-1]["son"] <= 1.0 and olay[-1]["taraf"] == ad: olay[-1]["son"] = t; olay[-1]["durum"].append(r)
    else: olay.append({"bas": t, "son": t, "taraf": ad, "y": y, "dol": d, "durum": [r]})
print(f"{v}: {n} kare (4 fps), olay {len(olay)}")
for o in olay:
    gecis = "kırmızı→gri" if "KIRMIZI" in o["durum"] and o["durum"][-1] == "GRI" else ",".join(sorted(set(o["durum"])))
    print(f"  {o['bas']:7.2f}–{o['son']:7.2f} sn  {o['taraf']:5s} y≈{o['y']}  doluluk {o['dol']}  {gecis}")
