#!/usr/bin/env python3
"""Yaşıt kohort: son 30 günde uzun video yükleyen, ilk yüklemesi yakın tarihli, az videolu niş kanallar (Data API search + videos + channels).
Kullanım: python3 -I kohort.py <cikti.json> <publishedAfter ISO> <sorgu1> [sorgu2 ...]"""
import json, os, sys, urllib.request, urllib.parse, datetime as dt
K = os.environ["YOUTUBE_API_KEY"]; B = "https://www.googleapis.com/youtube/v3/"
def api(ep, **p):
    p["key"] = K
    with urllib.request.urlopen(B + ep + "?" + urllib.parse.urlencode(p), timeout=30) as r: return json.load(r)
out_f, after, Q = sys.argv[1], sys.argv[2], sys.argv[3:]
now = dt.datetime.now(dt.timezone.utc); kanal = {}; hata = []
for q in Q:
    for dur in ("medium", "long"):
        try:
            r = api("search", part="snippet", q=q, type="video", publishedAfter=after, videoDuration=dur, relevanceLanguage="en", maxResults=50)
            for i in r["items"]: kanal.setdefault(i["snippet"]["channelId"], set()).add(q)
        except Exception as e: hata.append(f"{q}/{dur}: {str(e)[:60]}")
ids = list(kanal); ch = {}
for k in range(0, len(ids), 50):
    for c in api("channels", part="snippet,statistics,contentDetails", id=",".join(ids[k:k+50]))["items"]: ch[c["id"]] = c
sonuc = []
for cid, c in ch.items():
    n = int(c["statistics"].get("videoCount", 0))
    if n == 0 or n > 25: continue
    up = api("playlistItems", part="contentDetails", playlistId=c["contentDetails"]["relatedPlaylists"]["uploads"], maxResults=50)["items"]
    vids = [i["contentDetails"]["videoId"] for i in up]
    vs = api("videos", part="snippet,statistics,contentDetails", id=",".join(vids))["items"] if vids else []
    vs.sort(key=lambda a: a["snippet"]["publishedAt"])
    if not vs or vs[0]["snippet"]["publishedAt"] < "2026-07-01": continue   # ilk herkese açık yükleme yeni olmalı
    sonuc.append({"kanal": c["snippet"]["title"], "id": cid, "acilis": c["snippet"]["publishedAt"], "abone": c["statistics"].get("subscriberCount"),
        "video_sayisi": n, "sorgular": sorted(kanal[cid]),
        "videolar": [{"id": a["id"], "baslik": a["snippet"]["title"], "yayin": a["snippet"]["publishedAt"], "sure": a["contentDetails"]["duration"],
                      "dil": a["snippet"].get("defaultAudioLanguage"), "izlenme": int(a["statistics"].get("viewCount", 0)),
                      "yas_gun": round((now - dt.datetime.fromisoformat(a["snippet"]["publishedAt"].replace("Z", "+00:00"))).total_seconds()/86400, 1)} for a in vs]})
json.dump({"olcum_utc": now.isoformat(timespec="seconds"), "kaynak": "YouTube Data API v3 search+channels+playlistItems+videos",
           "sorgular": Q, "publishedAfter": after, "aday_kanal": len(ch), "hata": hata, "kohort": sonuc}, open(out_f, "w"), ensure_ascii=False, indent=1)
print("aday", len(ch), "kohort", len(sonuc), "hata", hata)
