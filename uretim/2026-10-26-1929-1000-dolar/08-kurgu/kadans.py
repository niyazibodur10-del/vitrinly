# Kadans ölçümü: altyazı bandı hariç (alt %28), 4 fps gri 192x108. Bir "görsel olay" = kare(t) ile kare(t-0.5 sn) arasında
# >45 parlaklık farkı olan piksel oranının >= ESIK olduğu ve 0.5 sn önce ESIK altında olduğu an (yükselen kenar) VEYA sahne kesmesi.
# Sürekli hareket (şerit yağmuru) yükselen kenar üretmez → muhafazakâr (olay sayısını az sayar).
import subprocess,sys,numpy as np,json
v=sys.argv[1]; dikey=len(sys.argv)>2 and sys.argv[2]=='dikey'
fps=4; W,H=(108,192) if dikey else (192,108); alt=0.72 if not dikey else 0.66
p=subprocess.run(['ffmpeg','-v','error','-i',v,'-vf',f'fps={fps},scale={W}:{H},format=gray','-f','rawvideo','-'],capture_output=True).stdout
F=np.frombuffer(p,np.uint8).reshape(-1,H,W).astype(np.int16)[:, :int(H*alt), :]
k=2; ESIK=0.004
fr=np.array([0.0]*k+[float((np.abs(F[i]-F[i-k])>45).mean()) for i in range(k,len(F))])
glob=np.array([0.0]+[float(np.abs(F[i]-F[i-1]).mean()) for i in range(1,len(F))])
ev=[]
for i in range(k,len(F)):
    kes=glob[i]>25
    yuk=fr[i]>=ESIK and fr[i-k]<ESIK
    if (kes or yuk) and (not ev or i/fps-ev[-1]>0.75): ev.append(i/fps)
son=len(F)/fps
gaps=[(round(a,2),round(b-a,2)) for a,b in zip([0.0]+ev,ev+[son])]
print(json.dumps({'sure':son,'olay':len(ev),'ilk_olay':ev[0] if ev else None,'ilk30':[round(x,2) for x in ev if x<30],
 'ilk30_sayi':sum(1 for x in ev if x<30),'en_uzun':sorted(gaps,key=lambda g:-g[1])[:8],
 'bosluk_gt10':[g for g in gaps if g[1]>10],'ortalama_aralik':round(son/max(1,len(ev)),2)}))
