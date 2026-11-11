#!/usr/bin/env python3
"""Render edilmiş videodan ağız-ses senkronu (animasyon-yonetmeni 2026-11-11).
Veri değil, PİKSEL ölçer: yakın çekimlerde ağız kutusunun (kamera formülüyle kare kare ekrana taşınır) koyu piksel oranı
= ağız açıklığı; videonun KENDİ ses izinin 700–3000 Hz RMS'i ile ±8 kare gecikme korelasyonu. Kapı |gecikme| ≤ 2 kare.
Kullanım: python3 agiz-piksel-senkron.py <video.mp4> <aralik_json>   (aralık: [{"kim","bas","bitis","z0","z1"}], bölüm sn)
Kamera: Cekim.tsx yakin (odak = ((yuz.x+540)/2, yuz.y+120), zoom easeInOutQuad z0→z1, kadraj sınırı). Vuruşlu çekimler ölçülmez.
"""
import json, subprocess, sys
import numpy as np
FPS, W, H = 30, 1080, 1920
RIG = {"jake": {"yuz": (570, 560), "agiz": (479, 594, 208, 186), "merkez": (0.5, 0.27)}, "mike": {"yuz": (610, 500), "agiz": (555, 496, 204, 208), "merkez": (0.42, 0.33)}}
# merkez: ağız yaması kutusunda dudak ortası (oran) — kare üstünde kutu çizilerek doğrulandı

def ease(p): return 2 * p * p if p < 0.5 else 1 - (-2 * p + 2) ** 2 / 2

def kareler(video, k0, k1):
    n = k1 - k0
    cmd = ["ffmpeg", "-v", "error", "-ss", f"{k0 / FPS:.4f}", "-i", video, "-frames:v", str(n), "-vf", "format=gray", "-f", "rawvideo", "-"]
    b = subprocess.run(cmd, capture_output=True, check=True).stdout
    return np.frombuffer(b, np.uint8).reshape(-1, H, W)

def ses_rms(video):
    b = subprocess.run(["ffmpeg", "-v", "error", "-i", video, "-af", "highpass=f=700,lowpass=f=3000", "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True, check=True).stdout
    a = np.frombuffer(b, np.int16).astype(float)
    n = len(a) * FPS // 16000
    return np.array([np.sqrt(np.mean(a[int(i * 16000 / FPS):int((i + 1) * 16000 / FPS)] ** 2) + 1e-9) for i in range(n)])

def main():
    video, aralik = sys.argv[1], json.load(open(sys.argv[2]))
    rms = ses_rms(video)
    A, B = [], []
    for r in aralik:
        k0, k1 = round(r["bas"] * FPS), round(r["bitis"] * FPS)
        im = kareler(video, k0, k1)
        yz, (ax, ay, aw, ah) = RIG[r["kim"]]["yuz"], RIG[r["kim"]]["agiz"]
        acik = []
        for i in range(len(im)):
            p = (k0 + i - round(r.get("sahne_bas", r["bas"]) * FPS)) / max(1, round(r.get("sahne_bitis", r["bitis"]) * FPS) - round(r.get("sahne_bas", r["bas"]) * FPS))
            S = r["z0"] + (r["z1"] - r["z0"]) * ease(p)
            fx = min(W - W / (2 * S), max(W / (2 * S), (yz[0] + W / 2) / 2))
            fy = min(H - H / (2 * S), max(H / (2 * S), yz[1] + 120))
            mx, my = RIG[r["kim"]]["merkez"]
            cx, cy = W / 2 + (ax + aw * mx - fx) * S, H / 2 + (ay + ah * my - fy) * S
            x0, x1, y0, y1 = int(cx - 50 * S), int(cx + 50 * S), int(cy - 22 * S), int(cy + 22 * S)
            kutu = im[i, y0:y1, x0:x1].astype(float)
            acik.append(float(np.mean(kutu < 95)))
        a = np.array(acik); s = rms[k0:k0 + len(a)]
        if len(s) < len(a): a = a[:len(s)]
        A.append((a - a.mean()) / (a.std() + 1e-9)); B.append((s - s.mean()) / (s.std() + 1e-9))
        r["kare"] = len(a)
    sonuc = {}
    for lag in range(-8, 9):  # lag>0: görüntü sesten GEÇ
        num = den = 0
        for a, s in zip(A, B):
            if lag >= 0: x, y = a[lag:], s[:len(s) - lag]
            else: x, y = a[:lag], s[-lag:]
            num += float(np.sum(x * y)); den += len(x)
        sonuc[lag] = num / den
    en = max(sonuc, key=sonuc.get)
    print(json.dumps({"gecikme_kare": en, "korelasyon": round(sonuc[en], 3), "lag0": round(sonuc[0], 3), "aralik_kare": sum(r["kare"] for r in aralik),
                      "egri": {k: round(v, 3) for k, v in sonuc.items()}}))
    sys.exit(0 if abs(en) <= 2 else 1)

if __name__ == "__main__":
    main()
