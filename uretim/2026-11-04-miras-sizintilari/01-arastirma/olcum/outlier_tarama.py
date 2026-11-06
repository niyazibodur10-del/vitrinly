#!/usr/bin/env python3
"""trend-avcisi F1: nişte son 12 ay outlier taraması (izlenme / abone).
ID: yt-dlp YouTube arama (filtre 'bu yıl' + 'izlenme sırası', sp=CAMSAggF) — search.list kotası harcanmaz.
İstatistik: videos.list + channels.list (1 birim/50 ID). Anahtar ortamdan (YOUTUBE_API_KEY).
Kullanım: python3 outlier_tarama.py sorgular.txt outlier-ham.json"""
import json,os,re,sys,subprocess,urllib.request,urllib.parse
K=os.environ["YOUTUBE_API_KEY"];A="https://www.googleapis.com/youtube/v3/"
def api(ep,**p):
    p["key"]=K;return json.load(urllib.request.urlopen(A+ep+"?"+urllib.parse.urlencode(p),timeout=30))["items"]
def ids(q,n=30):
    u="https://www.youtube.com/results?search_query="+urllib.parse.quote_plus(q)+"&sp=CAMSAggF"
    r=subprocess.run([sys.executable,"-m","yt_dlp","--flat-playlist","--print","%(id)s","--playlist-end",str(n),u],capture_output=True,text=True,timeout=180)
    return [l.strip() for l in r.stdout.splitlines() if re.fullmatch(r"[\w-]{11}",l.strip())]
def dur(s):
    m=re.fullmatch(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?",s or "");
    return 0 if not m else sum(int(x or 0)*k for x,k in zip(m.groups(),(86400,3600,60,1)))
qs=[l.strip() for l in open(sys.argv[1]) if l.strip() and not l.startswith("#")];outp=sys.argv[2]
out=json.load(open(outp)) if os.path.exists(outp) else {"sorgular":{},"videolar":{},"kanallar":{}}
for q in qs:
    if q in out["sorgular"]:continue
    v=ids(q);out["sorgular"][q]=v;print(q,len(v),flush=True)
    new=[i for i in v if i not in out["videolar"]]
    for j in range(0,len(new),50):
        for x in api("videos",part="statistics,snippet,contentDetails",id=",".join(new[j:j+50])):
            s=x["snippet"];out["videolar"][x["id"]]={"t":s["title"],"ch":s["channelTitle"],"cid":s["channelId"],"pub":s["publishedAt"][:10],
              "v":int(x["statistics"].get("viewCount",0)),"sn":dur(x["contentDetails"].get("duration")),"dil":s.get("defaultAudioLanguage",s.get("defaultLanguage",""))}
    cids=list({x["cid"] for x in out["videolar"].values()}-set(out["kanallar"]))
    for j in range(0,len(cids),50):
        for c in api("channels",part="statistics",id=",".join(cids[j:j+50])):
            out["kanallar"][c["id"]]=int(c["statistics"].get("subscriberCount",0) or 0)
    json.dump(out,open(outp,"w"),ensure_ascii=False)
