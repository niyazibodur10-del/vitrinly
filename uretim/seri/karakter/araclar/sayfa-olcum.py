#!/usr/bin/env python3
"""Karakter sayfası ölçümü (Flip By Vote, gorsel-varlik-sanatcisi 2026-11-10).
Sayfa içi tutarlılık: ön görünüm yüzü ↔ 6 ifade yüzü HSV(H,S) histogram korelasyonu + ten/saç/giysi medyan Lab ΔE (hedef renge).
Kutular 1920x1080 J-A / M-A yerleşimine göre (sol 3 tam boy, sağ 3x2 portre). Yeni sayfada kutuları yeniden ayarla.
Kullanım: ~/.finansal-arac/venv/bin/python -I araclar/sayfa-olcum.py canva-ham <kontak.jpg>"""
import sys, cv2, numpy as np
D = sys.argv[1]
def lab(bgr): return cv2.cvtColor(np.uint8([[bgr]]), cv2.COLOR_BGR2LAB)[0,0].astype(float)*[100/255,1,1]-[0,128,128]
def hexbgr(h): h=h.lstrip('#'); return [int(h[4:6],16),int(h[2:4],16),int(h[0:2],16)]
def med(img,b,mask=None):
    x0,y0,x1,y1=b; r=img[y0:y1,x0:x1].reshape(-1,3)
    if mask is not None: r=r[mask(r)]
    return np.median(r,0), len(r)
def de(a,b): return float(np.linalg.norm(lab(a)-lab(b)))
def hist(img,b):
    x0,y0,x1,y1=b; h=cv2.cvtColor(img[y0:y1,x0:x1],cv2.COLOR_BGR2HSV)
    m=cv2.calcHist([h],[0,1],None,[30,32],[0,180,0,256]); return cv2.normalize(m,m).flatten()
S = {
 "J-A": dict(on=(118,78,208,188), cols=(1040,1390,1740), rows=((150,330),(640,820)), w=90,
   bolge={"hoodie":((40,250,110,450),"#1F2B47",None), "pantolon":((90,580,220,880),"#CDB48E",None),
          "sac":((130,48,200,72),"#3B2A20",None), "ayakkabi":((60,945,120,985),"#F2F2F0",None)}),
 "M-A": dict(on=(122,72,214,172), cols=(1055,1400,1748), rows=((150,320),(640,810)), w=90,
   bolge={"flanel_kirmizi":((40,200,120,480),"#B3272D",lambda r:(r[:,2]>120)&(r[:,1]<90)), "tisort":((145,230,185,450),"#F2F2F0",None),
          "jean":((80,560,250,880),"#23314D",None), "sac":((125,38,205,66),"#A07A4E",None), "bot":((45,935,105,995),"#5A3A24",None)}),
}
ad=["notr","gulen","saskin","endiseli","heyecanli","dusunceli"]
kontak=[]
for k,s in S.items():
    img=cv2.imread(f"{D}/{k}.png"); hon=hist(img,s["on"])
    yuz=[(c-s["w"],r0,c+s["w"],r1) for (r0,r1) in s["rows"] for c in s["cols"]]
    kor=[cv2.compareHist(hon,hist(img,b),cv2.HISTCMP_CORREL) for b in yuz]
    print(f"{k} {img.shape[1]}x{img.shape[0]} · ön yüz↔ifade kor.: "+", ".join(f"{a} {v:.2f}" for a,v in zip(ad,kor))+f" · ort {np.mean(kor):.2f}")
    print("   renk ΔE (hedef = kart hedef rengi, bilgi amaçlı): "+", ".join(f"{n} {de(med(img,b,m)[0],hexbgr(h)):.1f} (medyan #{int(med(img,b,m)[0][2]):02X}{int(med(img,b,m)[0][1]):02X}{int(med(img,b,m)[0][0]):02X})" for n,(b,h,m) in s["bolge"].items()))
    x0,y0,x1,y1=s["on"]; row=[cv2.resize(img[y0:y1,x0:x1],(180,180))]+[cv2.resize(img[b[1]:b[3],b[0]:b[2]],(180,180)) for b in yuz]
    kontak.append(np.hstack(row))
cv2.imwrite(sys.argv[2], np.vstack(kontak), [cv2.IMWRITE_JPEG_QUALITY, 88])
