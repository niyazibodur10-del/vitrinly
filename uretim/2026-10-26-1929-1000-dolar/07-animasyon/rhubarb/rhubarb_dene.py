# Rhubarb aday denemeleri (A parça, B parça+0.5 sn boşluk, C tam sahne, D tam sahne+boşluk, E phonetic). animasyon-yonetmeni 2026-10-27
import json,subprocess,sys
RH='/root/.finansal-arac/rhubarb/build/rhubarb/rhubarb'
W='/home/user/vitrinly/uretim/2026-10-26-1929-1000-dolar/04-ses/anlatim.wav'
K=json.load(open('/home/user/vitrinly/uretim/2026-10-26-1929-1000-dolar/04-ses/kelimeler.json'))['words']
def metin(a,b):
    m=" ".join(x['w'] for x in K if a<=x['s']<b).replace(" ,",",").replace("$1,000","one thousand dollars")
    return m.replace("1929","nineteen twenty-nine").replace("1933","nineteen thirty-three").replace("Door 1","Door one")
def calis(ad,a,b,pad=0.0,rec='pocketSphinx',dlg=True):
    w=f'{ad}.wav'
    f=f"adelay={int(pad*1000)},apad=pad_dur={pad}" if pad else "anull"
    subprocess.run(['ffmpeg','-v','error','-y','-i',W,'-ss',str(a),'-to',str(b),'-af',f,'-ac','1',w],check=True)
    open(f'{ad}.txt','w').write(metin(a,b))
    cmd=[RH,'-r',rec,'-f','json','-o',f'{ad}.json',w]+(['--dialogFile',f'{ad}.txt'] if dlg else [])
    subprocess.run(cmd,check=True,capture_output=True)
    c=json.load(open(f'{ad}.json'))['mouthCues']
    return c
def kes(c,ofs,a,b):
    # ofs: cue zamanı → anlatım zamanı farkı; [a,b) anlatım aralığını 0'dan başlat
    out=[]
    for x in c:
        s=x['start']+ofs; e=x['end']+ofs
        if e<=a or s>=b: continue
        out.append({'start':round(max(s,a)-a,3),'end':round(min(e,b)-a,3),'value':x['value']})
    return out
def test(ad,cues,a,b):
    subprocess.run(['ffmpeg','-v','error','-y','-i',W,'-ss',str(a),'-to',str(b),'-ac','1',f'{ad}-t.wav'],check=True)
    json.dump({'mouthCues':cues},open(f'{ad}-t.json','w'))
    r=subprocess.run(['python3','/home/user/vitrinly/tools/senkron-testi.py',f'{ad}-t.wav',f'{ad}-t.json'],capture_output=True,text=True)
    print(ad,r.stdout.strip().replace('\n',' | '))
