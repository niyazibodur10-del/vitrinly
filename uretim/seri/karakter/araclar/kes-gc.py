#!/usr/bin/env python3
"""Düz zeminli 9:16 taban kesimi: Lab tohumlu GrabCut + kenar yumuşatma (gorsel-varlik-sanatcisi, 2026-11-10).
Neden: T-J lacivert hoodie'nin ışıklı omzu slate-blue zemine ΔE≈8 → M4 renk anahtarı omzu yedi (kenar artığı 0,17).
Tohum: kesin ön plan = Lab uzaklığı >18 olan en büyük bileşen + delik doldurma, 25 px aşındırılmış; kesin zemin = uzaklık <4 ve
ön plana 60 px'ten uzak, kenara bağlı; arası GrabCut (5 tur). Alfa = maske, 2 px Gauss; renk arındırma (zemin rengi saçaktan çıkarılır).
Kullanım: python -I kes-gc.py <girdi.png> <cikis_rgba.png> <yesil.jpg> [gövde_baslangic_y: altı σ7 kontur yumuşatma] [--zarf]   ortam: SAC_PX (saç bölgesi yüksekliği, varsayılan 320)"""
import sys, os, json, cv2, numpy as np
def lab(i): return cv2.cvtColor(i, cv2.COLOR_BGR2LAB).astype(np.float32)*np.array([100/255,1,1],np.float32)-np.array([0,128,128],np.float32)
img=cv2.imread(sys.argv[1]); h,w=img.shape[:2]
c=np.concatenate([img[:30,:30].reshape(-1,3),img[:30,-30:].reshape(-1,3)]); bgc=np.median(c,0)
d=np.linalg.norm(lab(img)-lab(bgc.reshape(1,1,3).astype(np.uint8))[0,0],axis=2)
core=(d>18).astype(np.uint8); n,lb,st,_=cv2.connectedComponentsWithStats(core); core=(lb==1+np.argmax(st[1:,4])).astype(np.uint8)
ff=core.copy(); m2=np.zeros((h+2,w+2),np.uint8); cv2.floodFill(ff,m2,(0,0),1); core=core|(1-ff)
fg=cv2.erode(core,np.ones((51,51),np.uint8))
near=cv2.dilate(core,np.ones((121,121),np.uint8))
bg=((d<4)&(near==0)).astype(np.uint8)
mask=np.full((h,w),cv2.GC_PR_BGD,np.uint8); mask[core>0]=cv2.GC_PR_FGD; mask[fg>0]=cv2.GC_FGD; mask[bg>0]=cv2.GC_BGD
b=np.zeros((1,65)); f=np.zeros((1,65)); cv2.grabCut(img,mask,None,b,f,5,cv2.GC_INIT_WITH_MASK)
m=((mask==cv2.GC_FGD)|(mask==cv2.GC_PR_FGD)).astype(np.uint8)
n,lb,st,_=cv2.connectedComponentsWithStats(m); m=(lb==1+np.argmax(st[1:,4])).astype(np.uint8)
ff=m.copy(); m2=np.zeros((h+2,w+2),np.uint8); cv2.floodFill(ff,m2,(0,0),1); m=m|(1-ff)
Y0=int(sys.argv[4]) if len(sys.argv)>4 else h  # bu satırdan aşağısı gövde
HULL="--zarf" in sys.argv  # gövdede dışbükey zarf (kol-gövde boşluğu olmayan pozda: T-J)
if Y0<h:
    sm=(cv2.GaussianBlur(m.astype(np.float32),(0,0),7)>0.5).astype(np.uint8); m[Y0:]=sm[Y0:]
    if HULL:
        ys,xs=np.where(m[Y0:]>0); hull=cv2.convexHull(np.stack([xs,ys+Y0],1).astype(np.int32))
        hm=np.zeros_like(m); cv2.fillPoly(hm,[hull],1); m[Y0:]=np.maximum(m[Y0:],hm[Y0:])
# gerçek zemin cepleri (kol-gövde arası, kenara değse de): d<5 bileşen alanı >1500 → saydam
n,lb,st,_=cv2.connectedComponentsWithStats(((d<5)&(m>0)).astype(np.uint8))
cep=0
for i in range(1,n):
    if st[i,4]>1500: m[lb==i]=0; cep+=int(st[i,4])
a=cv2.GaussianBlur(m.astype(np.float32),(0,0),1.2)
# kafa bölgesinde (y<Y0) sınır bandında Lab yumuşak alfa: ince saç uçları yarı saydam
band=(cv2.dilate(m,np.ones((25,25),np.uint8))>0)&(cv2.erode(m,np.ones((25,25),np.uint8))==0)
soft=np.clip((d-3)/18,0,1); hb=band.copy(); hb[Y0:]=False; a[hb]=np.minimum(a[hb],soft[hb])
# renk arındırma: kenarda (0<a<1) zemin katkısını çıkar
out=img.astype(np.float32); edge=(a>0.02)&(a<0.98)
aa=np.clip(a[...,None],0.15,1); fix=(out-(1-aa)*bgc)/aa; out[edge]=np.clip(fix[edge],0,255)
# saç saçağı: saç bölgesinde (ön plan tepesinden 320 px) yarı saydam piksellerin renk tonunu saç medyanına çek (L korunur)
ty=int(np.where(m.any(1))[0][0]); hz=np.zeros((h,w),bool); SAC=int(os.environ.get("SAC_PX",320)); hz[ty:ty+SAC]=True
core_h=hz&(a>0.99)&(d>25); fr=hz&(a<0.99)&(a>0.01)
if core_h.any() and fr.any():
    L=cv2.cvtColor(np.clip(out,0,255).astype(np.uint8),cv2.COLOR_BGR2LAB); hab=np.median(L[core_h][:,1:],0)
    b40=hz&(cv2.erode(m,np.ones((81,81),np.uint8))==0)&(a>0.01)
    mavi=b40&(L[...,2].astype(np.float32)-128<float(hab[1])-128-12)  # saç tonundan belirgin mavi (zemin karışmış tel)
    a[mavi]=np.minimum(a[mavi],np.clip((d[mavi]-3)/30,0,1)); fr=fr|mavi
    L[fr,1:]=hab; out=cv2.cvtColor(L,cv2.COLOR_LAB2BGR).astype(np.float32)
rgba=np.dstack([out.astype(np.uint8),(a*255).astype(np.uint8)]); cv2.imwrite(sys.argv[2],rgba)
g=np.full_like(img,(64,200,60)); comp=(out*a[...,None]+g*(1-a[...,None])).astype(np.uint8); cv2.imwrite(sys.argv[3],comp,[cv2.IMWRITE_JPEG_QUALITY,88])
ring=(cv2.dilate(m,np.ones((7,7),np.uint8))-cv2.erode(m,np.ones((7,7),np.uint8)))>0
sacak=int(((a>0.5)&(d<6)&ring).sum())
ys,xs=np.where(m>0)
kenar={k:int(v) for k,v in {"sol_min_y":ys[xs==0].min() if (xs==0).any() else -1,"sag_min_y":ys[xs==w-1].min() if (xs==w-1).any() else -1}.items()}
print(json.dumps({"girdi":sys.argv[1],"zemin_bgr":bgc.tolist(),"on_plan_px":int(m.sum()),"bbox":[int(xs.min()),int(ys.min()),int(xs.max()),int(ys.max())],"sacak_px":sacak,"zemin_cebi_px":cep,"kenara_degme":kenar}))
