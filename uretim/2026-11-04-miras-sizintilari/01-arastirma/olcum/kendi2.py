#!/usr/bin/env python3
"""Kendi kanal (@toonomy) anlık sayım + izlenme/gün + yükleme listesi. Kullanım: python3 -I kendi2.py <cikti.json> <id1> <id2> ..."""
import json, os, sys, urllib.request, urllib.parse, datetime as dt
K = os.environ["YOUTUBE_API_KEY"]; B = "https://www.googleapis.com/youtube/v3/"
def api(ep, **p):
    p["key"] = K
    with urllib.request.urlopen(B + ep + "?" + urllib.parse.urlencode(p), timeout=30) as r: return json.load(r)
out_f, IDS = sys.argv[1], sys.argv[2:]
now = dt.datetime.now(dt.timezone.utc)
v = api("videos", part="snippet,statistics,contentDetails,status", id=",".join(IDS))["items"]
cid = v[0]["snippet"]["channelId"]
c = api("channels", part="statistics,snippet,contentDetails", id=cid)["items"][0]
up = api("playlistItems", part="contentDetails,status", playlistId=c["contentDetails"]["relatedPlaylists"]["uploads"], maxResults=50)["items"]
out = {"olcum_utc": now.isoformat(timespec="seconds"), "kaynak": "YouTube Data API v3",
       "kanal": {"id": cid, "ad": c["snippet"]["title"], "acilis": c["snippet"]["publishedAt"], **c["statistics"]},
       "yukleme_listesi_gorunen": [i["contentDetails"]["videoId"] for i in up], "videolar": []}
for x in v:
    pub = dt.datetime.fromisoformat(x["snippet"]["publishedAt"].replace("Z", "+00:00")); gun = (now - pub).total_seconds() / 86400
    s = x.get("statistics", {}); iz = int(s.get("viewCount", 0))
    out["videolar"].append({"id": x["id"], "baslik": x["snippet"]["title"], "publishedAt": x["snippet"]["publishedAt"],
        "yas_gun": round(gun, 2), "izlenme_gun": round(iz / gun, 1) if gun > 0 else None, "sure": x["contentDetails"]["duration"],
        "gizlilik": x["status"]["privacyStatus"], "publishAt": x["status"].get("publishAt"),
        "dil": x["snippet"].get("defaultAudioLanguage"), "kategori": x["snippet"].get("categoryId"), **s})
cm = {}
for x in v:
    try:
        t = api("commentThreads", part="snippet", videoId=x["id"], maxResults=50)["items"]
        cm[x["id"]] = {"toplam": len(t), "kendi": sum(1 for i in t if i["snippet"]["topLevelComment"]["snippet"].get("authorChannelId", {}).get("value") == cid)}
    except Exception as e: cm[x["id"]] = {"hata": str(e)[:80]}
out["yorum"] = cm
json.dump(out, open(out_f, "w"), ensure_ascii=False, indent=1)
print(json.dumps(out, ensure_ascii=False, indent=1))
