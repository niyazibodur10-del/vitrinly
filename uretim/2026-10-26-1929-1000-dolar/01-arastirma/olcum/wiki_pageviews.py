import json,sys,time,urllib.request,urllib.parse
UA="ToonomyBot/0.1 (https://youtube.com/@toonomy; research)"
arts=[l.strip() for l in open(sys.argv[1]) if l.strip()]
out={}
for a in arts:
    u="https://wikimedia.org/api/rest_v1/metrics/pageviews/per-article/en.wikipedia/all-access/user/%s/daily/20260728/20261026"%urllib.parse.quote(a,safe='')
    for t in range(4):
        try:
            r=urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":UA}),timeout=20)
            d=json.load(r)["items"];break
        except Exception as e:
            d=None;err=str(e);time.sleep(5*2**(t+1))
    if d is None: out[a]={"err":err};print(a,"ERR",err);continue
    v=[x["views"] for x in d]
    last30=sum(v[-30:]);prev60=sum(v[:-30])
    out[a]={"days":len(v),"sum90":sum(v),"last30":last30,"daily_avg30":round(last30/30),"prev60_avg":round(prev60/max(1,len(v)-30)),"peak":max(v),"peakday":d[v.index(max(v))]["timestamp"][:8]}
    print(a,out[a]);time.sleep(8)
json.dump(out,open(sys.argv[2],"w"),indent=1)
