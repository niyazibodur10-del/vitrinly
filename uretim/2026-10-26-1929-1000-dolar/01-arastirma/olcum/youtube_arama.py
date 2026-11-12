import json,os,sys,subprocess,urllib.request,urllib.parse,statistics,time
K=os.environ["YOUTUBE_API_KEY"]
def stats(ids):
    u="https://www.googleapis.com/youtube/v3/videos?"+urllib.parse.urlencode({"part":"statistics,snippet,contentDetails","id":",".join(ids),"key":K})
    return json.load(urllib.request.urlopen(u,timeout=30))["items"]
def search(q,n,mode):
    p="ytsearch%d:%s"%(n,q) if mode=="rel" else "ytsearchdate%d:%s"%(n,q)
    r=subprocess.run([sys.executable,"-m","yt_dlp","--flat-playlist","--print","%(id)s",p],capture_output=True,text=True,timeout=120)
    return [l.strip() for l in r.stdout.splitlines() if l.strip()]
qs=json.load(open(sys.argv[1])); outp=sys.argv[2]
out=json.load(open(outp)) if os.path.exists(outp) else {}
for key,q in qs.items():
    if key in out: continue
    rel=search(q,15,"rel"); rec=search(q,25,"date")
    allids=list(dict.fromkeys(rel+rec))
    items=[]
    for i in range(0,len(allids),50): items+=stats(allids[i:i+50])
    m={x["id"]:(int(x["statistics"].get("viewCount",0)),x["snippet"]["title"][:80],x["snippet"]["channelTitle"][:30],x["snippet"]["publishedAt"][:10],x["contentDetails"]["duration"]) for x in items}
    relv=[m[i][0] for i in rel if i in m]
    recent=sorted([(v[0],v[1],v[2],v[3],k) for k,v in m.items() if v[3]>="2025-10-27"],reverse=True)
    out[key]={"query":q,"measured":"2026-10-27","rel_n":len(relv),"rel_median":int(statistics.median(relv)) if relv else 0,"rel_ge1M":sum(1 for v in relv if v>=1e6),
      "rel_top3":sorted([(m[i][0],m[i][1],m[i][2],m[i][3],i) for i in rel if i in m],reverse=True)[:3],
      "recent12m_n":len(recent),"recent12m_top3":recent[:3]}
    json.dump(out,open(outp,"w"),indent=1,ensure_ascii=False)
    print(key,out[key]["rel_median"],out[key]["rel_ge1M"],"| 12m:",recent[:1],flush=True)
