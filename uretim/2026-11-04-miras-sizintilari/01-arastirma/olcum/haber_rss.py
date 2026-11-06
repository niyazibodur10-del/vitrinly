#!/usr/bin/env python3
"""S1 haber akışı: Google News RSS (son N gün) + doğrudan yayıncı RSS. Kullanım: haber_rss.py sorgular.txt cikti.json [--gun 14]"""
import json,sys,time,urllib.request,urllib.parse,xml.etree.ElementTree as ET,email.utils,datetime as dt
UA={"User-Agent":"Mozilla/5.0 (X11; Linux x86_64) Chrome/124"}
gun=int(sys.argv[sys.argv.index("--gun")+1]) if "--gun" in sys.argv else 14
out={}
for q in [l.strip() for l in open(sys.argv[1]) if l.strip()]:
    u="https://news.google.com/rss/search?"+urllib.parse.urlencode({"q":f"{q} when:{gun}d","hl":"en-US","gl":"US","ceid":"US:en"})
    try: root=ET.fromstring(urllib.request.urlopen(urllib.request.Request(u,headers=UA),timeout=30).read())
    except Exception as e: out[q]={"err":str(e)};continue
    its=[]
    for it in root.iter("item"):
        s=it.find("source")
        d=email.utils.parsedate_to_datetime(it.findtext("pubDate")).date().isoformat()
        its.append({"t":it.findtext("title"),"d":d,"src":s.text if s is not None else "","srcurl":s.get("url") if s is not None else "","link":it.findtext("link")})
    out[q]={"n":len(its),"items":its[:25]}
    print(f"## {q} (n={len(its)})")
    for x in its[:8]: print(f"  {x['d']} | {x['t'][:120]}")
    time.sleep(1)
json.dump(out,open(sys.argv[2],"w"),indent=1,ensure_ascii=False)
