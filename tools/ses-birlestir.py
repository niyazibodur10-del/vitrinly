# Ses yama/birleştirme: plan JSON [[kaynak, başlangıç, bitiş], ...] (o=ana kayıt, d=düzeltme kaydı), 12 ms fade ile uç uca ekler.
# Kullanım: python ses-birlestir.py <plan-json> <cikis.wav>   (ana/düzeltme dosya yolları betikte; ileride parametre olacak)
import subprocess, numpy as np, json, sys, soundfile as sf
sr=48000
def load(f):
    raw=subprocess.run(["ffmpeg","-v","error","-i",f,"-ac","1","-ar",str(sr),"-f","f32le","-"],capture_output=True,check=True).stdout
    return np.frombuffer(raw,dtype=np.float32).copy()
def seg(a,t0,t1,fade=0.012):
    s=a[int(t0*sr):int(t1*sr)].copy(); n=int(fade*sr)
    s[:n]*=np.linspace(0,1,n); s[-n:]*=np.linspace(1,0,n); return s
o=load("/home/user/vitrinly/uretim/ses-testi/ses/temiz-v1.wav"); d=load("duz-temiz.wav")
plan=json.loads(sys.argv[1]); out=[]
for src,t0,t1 in plan:
    out.append(seg(o if src=="o" else d,t0,t1))
y=np.concatenate(out); sf.write(sys.argv[2],y,sr,subtype="FLOAT")
print(sys.argv[2], round(len(y)/sr,2))
