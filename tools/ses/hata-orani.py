import re, json, sys, difflib
ref=open(sys.argv[1]).read(); hyp=json.load(open(sys.argv[2]))["text"]
n=lambda s:re.sub(r"[^a-z0-9 ]"," ",s.lower().replace("you'll","you will").replace("we'll","we will").replace("that's","thats")).split()
r,h=n(ref),n(hyp)
d=[[0]*(len(h)+1) for _ in range(len(r)+1)]
for i in range(len(r)+1): d[i][0]=i
for j in range(len(h)+1): d[0][j]=j
for i in range(1,len(r)+1):
  for j in range(1,len(h)+1):
    d[i][j]=min(d[i-1][j]+1,d[i][j-1]+1,d[i-1][j-1]+(r[i-1]!=h[j-1]))
print(f"kelime={len(r)} hata={d[-1][-1]} WER=%{d[-1][-1]/len(r)*100:.1f}")
sm=difflib.SequenceMatcher(a=r,b=h,autojunk=False)
for op,a1,a2,b1,b2 in sm.get_opcodes():
  if op!='equal': print(op, ' '.join(r[a1:a2]), '->', ' '.join(h[b1:b2]))
