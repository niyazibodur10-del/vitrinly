import json,sys,soundfile as sf, numpy as np
from faster_whisper import WhisperModel
wav,zj=sys.argv[1],sys.argv[2]
y,sr=sf.read(wav); assert sr==24000

m=WhisperModel("small.en",device="cpu",compute_type="int8",local_files_only=True)
for c in json.load(open(zj))["cumleler"]:
    seg=y[int(c["bas"]*sr):int(c["son"]*sr)]
    a=np.interp(np.arange(0,len(seg),1.5),np.arange(len(seg)),seg).astype(np.float32)
    s,_=m.transcribe(a,language="en",word_timestamps=True,beam_size=5)
    ws=[w for x in s for w in x.words]
    print(f"{c['metin'][:60]!r:64} -> {' '.join(w.word.strip()+'('+format(w.probability,'.2f')+')' for w in ws)}")
