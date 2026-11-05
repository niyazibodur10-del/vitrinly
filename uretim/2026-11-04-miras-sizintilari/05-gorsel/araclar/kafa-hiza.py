#!/usr/bin/env python3
"""Kafa bölgesi hizası (rig ağız/göz yamaları için): taban a ile faz korelasyonu kayması + ağız/göz bölgesi ortalama fark.
Kullanım: python -I kafa-hiza.py <a.png> <poz.png>... ; bölge 1920x1080 ölçeğinde (a'nın kafası x 800-1120, y 40-360)."""
import sys, cv2, numpy as np
KAFA=(800,40,1120,360); YUZ=(860,180,1060,330)
def g(p):
    im=cv2.imread(p); im=cv2.resize(im,(1920,1080),interpolation=cv2.INTER_AREA); return cv2.cvtColor(im,cv2.COLOR_BGR2GRAY).astype(np.float32)
a=g(sys.argv[1])
for p in sys.argv[2:]:
    b=g(p); x0,y0,x1,y1=KAFA
    (dx,dy),r=cv2.phaseCorrelate(a[y0:y1,x0:x1],b[y0:y1,x0:x1])
    X0,Y0,X1,Y1=YUZ; fark=float(np.abs(a[Y0:Y1,X0:X1]-b[Y0:Y1,X0:X1]).mean())
    ok=abs(dx)<=3 and abs(dy)<=3 and fark<=12
    print(f"{p.split('/')[-1]:12s} kayma ({dx:+.1f},{dy:+.1f}) px  tepe {r:.2f}  yüz bölgesi ort. fark {fark:.1f}  {'GEÇTİ' if ok else 'KALDI'}")
