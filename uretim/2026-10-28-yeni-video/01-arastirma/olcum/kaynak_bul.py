#!/usr/bin/env python3
"""Konu başına açılan bağımsız kaynak bulur: Google News RSS -> gnewsdecoder -> curl (200 + anahtar) -> datePublished.
Kullanım: kaynak_bul.py konular.tsv cikti.json   (tsv: ID<TAB>sorgu<TAB>anahtar<TAB>gün)"""
import json,sys,re,time,html,subprocess,urllib.request,urllib.parse,xml.etree.ElementTree as ET,email.utils,os
from googlenewsdecoder import gnewsdecoder
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 Chrome/124 Safari/537.36"
KOT={"reuters.com","wsj.com","bloomberg.com","nytimes.com","barrons.com","economist.com","investopedia.com","seekingalpha.com"}
def alan(u):
    h=re.sub(r"^https?://","",u).split("/")[0].lower().split("."); 
    return ".".join(h[-3:]) if len(h)>=3 and h[-2] in("co","com","org","gov") and len(h[-1])==2 else ".".join(h[-2:])
def ac(u,k):
    r=subprocess.run(["curl","-s","-L","--compressed","-A",UA,"--max-time","25","-w","\n__KOD__%{http_code}",u],capture_output=True)
    t=r.stdout.decode("utf-8","ignore"); kod=t.rsplit("__KOD__",1)[-1].strip()
    m=re.search(r'"datePublished"\s*:\s*"(\d{4}-\d{2}-\d{2})|article:published_time"\s+content="(\d{4}-\d{2}-\d{2})|content="(\d{4}-\d{2}-\d{2})[^"]*"\s+(?:property|name)="article:published_time',t)
    d=next((g for g in m.groups() if g),None) if m else None
    x=html.unescape(re.sub(r"<[^>]+>"," ",re.sub(r"<script.*?</script>|<style.*?</style>","",t,flags=re.S)))
    return kod, kod=="200" and k.lower() in x.lower(), d
out=json.load(open(sys.argv[2])) if os.path.exists(sys.argv[2]) else {}
for line in open(sys.argv[1]):
    if not line.strip() or line.startswith("#"): continue
    tid,q,k,g=line.rstrip("\n").split("\t")
    if tid in out and len(out[tid]["ok"])>=3: continue
    u="https://news.google.com/rss/search?"+urllib.parse.urlencode({"q":f"{q} when:{g}d","hl":"en-US","gl":"US","ceid":"US:en"})
    root=ET.fromstring(urllib.request.urlopen(urllib.request.Request(u,headers={"User-Agent":UA}),timeout=30).read())
    items=list(root.iter("item")); ok=[]; tried=[]; doms=set()
    for it in items[:14]:
        s=it.find("source"); su=s.get("url","") if s is not None else ""
        if alan(su) in KOT or alan(su) in doms: continue
        try: dec=gnewsdecoder(it.findtext("link"),interval=1)
        except Exception: continue
        if not dec.get("success"): continue
        url=dec["decoded_url"]; kod,good,d=ac(url,k)
        rss_d=email.utils.parsedate_to_datetime(it.findtext("pubDate")).date().isoformat()
        rec={"t":it.findtext("title"),"url":url,"src":s.text if s is not None else "","kod":kod,"meta_d":d,"rss_d":rss_d}
        tried.append(rec)
        if good: ok.append(rec); doms.add(alan(url))
        if len(ok)>=3: break
    out[tid]={"q":q,"k":k,"n_rss":len(items),"ok":ok,"tried":len(tried)}
    print(tid,q,"| rss",len(items),"| ok",len(ok),[ (alan(x["url"]),x["meta_d"] or x["rss_d"]) for x in ok],flush=True)
    json.dump(out,open(sys.argv[2],"w"),indent=1,ensure_ascii=False)
