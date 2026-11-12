#!/usr/bin/env python3
"""SRT okuma hızı düzeltmesi (kurgu-editoru F7): >21 kr/sn bloğun BİTİŞİ sonraki bloğa kadar olan boşluğa uzatılır
(başlangıç = akustik kelime başı, değişmez; sonraki blok başından 0,1 sn önce durur). Kullanım: srt_uzat.py <girdi.srt> <cikis.srt>"""
import re, sys
def z(x):
    h, m, r = x.split(":"); return int(h) * 3600 + int(m) * 60 + float(r.replace(",", "."))
def y(t):
    ms = int(round(t * 1000)); return f"{ms//3600000:02d}:{ms//60000%60:02d}:{ms//1000%60:02d},{ms%1000:03d}"
B = []
for p in re.split(r"\n\s*\n", open(sys.argv[1], encoding="utf-8").read().strip()):
    s = p.split("\n"); a, b = s[1].split(" --> "); B.append([s[0], z(a), z(b), s[2:]])
n = 0
for i, blk in enumerate(B):
    L = len(" ".join(blk[3]))
    if L / (blk[2] - blk[1]) > 21 and i + 1 < len(B):
        yeni = min(B[i + 1][1] - 0.1, max(blk[2], blk[1] + L / 21))
        if yeni > blk[2] + 1e-3: blk[2] = yeni; n += 1
open(sys.argv[2], "w", encoding="utf-8").write("\n\n".join(f"{b[0]}\n{y(b[1])} --> {y(b[2])}\n" + "\n".join(b[3]) for b in B) + "\n")
print("uzatılan blok:", n)
