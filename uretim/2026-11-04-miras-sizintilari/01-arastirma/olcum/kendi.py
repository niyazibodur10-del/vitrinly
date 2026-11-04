#!/usr/bin/env python3
"""Kendi kanal (@toonomy) herkese açık sayıları. Kullanım: python3 kendi.py <cikti.json>"""
import json, os, sys, urllib.request, urllib.parse, datetime as dt
K = os.environ["YOUTUBE_API_KEY"]; B = "https://www.googleapis.com/youtube/v3/"
def api(ep, **p):
    p["key"] = K
    with urllib.request.urlopen(B + ep + "?" + urllib.parse.urlencode(p), timeout=30) as r: return json.load(r)
IDS = ["BVJwZ1C9R1U", "QFC8GdDTW2c", "6LQGcQg4hpk", "ghLjMbrweCw"]
now = dt.datetime.now(dt.timezone.utc)
v = api("videos", part="snippet,statistics,contentDetails,status,liveStreamingDetails", id=",".join(IDS))["items"]
cid = v[0]["snippet"]["channelId"]
c = api("channels", part="statistics,snippet", id=cid)["items"][0]
out = {"olcum_utc": now.isoformat(timespec="seconds"), "kaynak": "YouTube Data API v3",
       "kanal": {"id": cid, "ad": c["snippet"]["title"], **c["statistics"]}, "videolar": []}
for x in v:
    out["videolar"].append({"id": x["id"], "baslik": x["snippet"]["title"], "publishedAt": x["snippet"]["publishedAt"],
        "sure": x["contentDetails"]["duration"], "gizlilik": x["status"]["privacyStatus"],
        "publishAt": x["status"].get("publishAt"), **x.get("statistics", {})})
cm = {}
for x in v:
    try:
        t = api("commentThreads", part="snippet", videoId=x["id"], maxResults=50)["items"]
        cm[x["id"]] = {"toplam": len(t), "kendi": sum(1 for i in t if i["snippet"]["topLevelComment"]["snippet"].get("authorChannelId", {}).get("value") == cid)}
    except Exception as e: cm[x["id"]] = {"hata": str(e)[:60]}
out["yorum"] = cm
json.dump(out, open(sys.argv[1], "w"), ensure_ascii=False, indent=1)
print(json.dumps(out, ensure_ascii=False, indent=1))
