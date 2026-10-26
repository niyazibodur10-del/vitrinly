import sys, json
from faster_whisper import WhisperModel
m = WhisperModel(sys.argv[3] if len(sys.argv)>3 else "small.en", device="cpu", compute_type="int8")
import subprocess, numpy as np
raw=subprocess.run(["ffmpeg","-v","error","-i",sys.argv[1],"-ac","1","-ar","16000","-f","f32le","-"],capture_output=True,check=True).stdout
audio=np.frombuffer(raw,dtype=np.float32)
segs, info = m.transcribe(audio, language="en", word_timestamps=True, beam_size=5, condition_on_previous_text=False)
words=[]; text=[]
for s in segs:
    text.append(s.text.strip())
    for w in s.words: words.append({"w":w.word.strip(),"s":round(w.start,3),"e":round(w.end,3),"p":round(w.probability,3)})
json.dump({"text":" ".join(text),"words":words}, open(sys.argv[2],"w"), indent=1)
print(" ".join(text))
