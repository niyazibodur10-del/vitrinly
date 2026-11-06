# Sessizlik kapısı (animasyon-yonetmeni 2026-10-27): Rhubarb çizelgesinde >=100 ms sessiz aralıkları X yapar.
import json,subprocess,sys,numpy as np
def sessizlik(wav,esik=0.012,minsure=0.10,hop=0.01):
    sr=16000
    a=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',wav,'-ac','1','-ar',str(sr),'-f','f32le','-'],capture_output=True,check=True).stdout,np.float32)
    h=int(sr*hop);n=len(a)//h
    r=np.array([np.sqrt((a[i*h:(i+1)*h]**2).mean()) for i in range(n)])
    s=r<esik;out=[];i=0
    while i<n:
        if s[i]:
            j=i
            while j<n and s[j]: j+=1
            if (j-i)*hop>=minsure: out.append((i*hop,j*hop))
            i=j
        else: i+=1
    return out
def uygula(cues,ss,pay=0.03):
    # sessiz aralıkları (başından pay sonra, sonundan pay önce) X yap
    ev=[]
    for c in cues: ev.append([c['start'],c['end'],c['value']])
    for a,b in ss:
        a2,b2=a+pay,b-pay
        if b2<=a2: continue
        new=[]
        for s,e,v in ev:
            if e<=a2 or s>=b2: new.append([s,e,v]); continue
            if s<a2: new.append([s,a2,v])
            if e>b2: new.append([b2,e,v])
        new.append([a2,b2,'X']); ev=sorted(new)
    return [{'start':round(s,3),'end':round(e,3),'value':v} for s,e,v in ev if e-s>1e-4]
if __name__=='__main__':
    wav,js,out=sys.argv[1:4]
    c=json.load(open(js))['mouthCues'];ss=sessizlik(wav)
    json.dump({'mouthCues':uygula(c,ss)},open(out,'w'));print(len(ss),'sessiz aralık')
