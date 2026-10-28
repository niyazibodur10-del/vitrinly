import json,subprocess,sys,numpy as np
sys.path.insert(0,'.')
from rhubarb_dene import calis, metin
sys.path.insert(0, "..")
from sessizlik_kapisi import sessizlik,uygula
Z=json.load(open('/home/user/vitrinly/uretim/2026-10-26-1929-1000-dolar/04-ses/sahne-zamanlari.json'))['sahneler']
acik={"X":0,"A":0,"B":0.3,"C":0.6,"D":1,"E":0.7,"F":0.4,"G":0.3,"H":0.6}
def lag(w,cues,band=None):
  fps=30;sr=16000
  a=np.frombuffer(subprocess.run(['ffmpeg','-v','error','-i',w]+(['-af',band] if band else [])+['-ac','1','-ar','16000','-f','f32le','-'],capture_output=True).stdout,np.float32)
  n=len(a)*fps//sr;rms=np.array([np.sqrt((a[i*sr//fps:(i+1)*sr//fps]**2).mean()) for i in range(n)])
  m=np.zeros(n)
  for c in cues: m[int(c['start']*fps):int(c['end']*fps)]=acik[c['value']]
  def corr(l):
    x,y=(rms[l:],m[:n-l]) if l>=0 else (rms[:n+l],m[-l:]);return np.corrcoef(x,y)[0,1]
  cs={l:corr(l) for l in range(-8,9)};b=max(cs,key=cs.get);return b,round(cs[b],2)
for sc in sys.argv[1:]:
  z=[x for x in Z if x['sahne']==sc][0]
  c=calis(sc,z['bas'],z['bitis']);g=uygula(c,sessizlik(sc+'.wav'))
  print(sc,'genis',lag(sc+'.wav',g),'formant',lag(sc+'.wav',g,'highpass=f=700,lowpass=f=3000'),flush=True)
