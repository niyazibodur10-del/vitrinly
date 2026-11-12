"""F12 ölçüm: kendi video + kanal + yorumlar + genç rakiplerin ilk 3 uzun videosu (Data API v3).
Kullanım: python3 -I olc.py <video_id> <rakip_json> <cikti_json>   (YOUTUBE_API_KEY ortamdan)"""
import json, os, re, sys, urllib.request, datetime as dt
K = os.environ["YOUTUBE_API_KEY"]; B = "https://www.googleapis.com/youtube/v3/"
def g(ep, **p):
    p["key"] = K; q = "&".join(f"{k}={urllib.parse.quote(str(v))}" for k, v in p.items())
    return json.load(urllib.request.urlopen(B + ep + "?" + q))
import urllib.parse
def sure(s):
    m = re.match(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", s); h, mi, se = (int(x or 0) for x in m.groups()); return h*3600+mi*60+se
vid, rj, out = sys.argv[1:4]
now = dt.datetime.now(dt.timezone.utc).isoformat()
v = g("videos", part="snippet,statistics,contentDetails,status", id=vid)["items"][0]
ch = g("channels", part="statistics", id=v["snippet"]["channelId"])["items"][0]["statistics"]
cm = g("commentThreads", part="snippet", videoId=vid, maxResults=100).get("items", [])
yorum = [{"t": c["snippet"]["topLevelComment"]["snippet"]["publishedAt"],
          "kanal_sahibi": c["snippet"]["topLevelComment"]["snippet"].get("authorChannelId", {}).get("value") == v["snippet"]["channelId"],
          "yanit": c["snippet"]["totalReplyCount"], "metin": c["snippet"]["topLevelComment"]["snippet"]["textOriginal"][:300]} for c in cm]
rk = json.load(open(rj))["kanallar"]
genc = {cid: x for cid, x in rk.items() if x["acilis"] >= "2025-05-01" and x["abone"] >= 1000}
rakip = []
for cid, x in genc.items():
    pl = "UU" + cid[2:]; ids = []; tok = None
    while True:
        p = dict(part="contentDetails", playlistId=pl, maxResults=50)
        if tok: p["pageToken"] = tok
        r = g("playlistItems", **p); ids += [i["contentDetails"]["videoId"] for i in r["items"]]
        tok = r.get("nextPageToken")
        if not tok or len(ids) >= 400: break
    eski = ids[-50:][::-1]  # en eski 50, eskiden yeniye
    vs = g("videos", part="snippet,statistics,contentDetails", id=",".join(eski))["items"]
    vs.sort(key=lambda a: a["snippet"]["publishedAt"])
    uzun = [a for a in vs if sure(a["contentDetails"]["duration"]) >= 240][:3]
    rakip.append({"kanal": x["ad"].strip(), "acilis": x["acilis"], "abone_2026_10_27": x["abone"], "video_sayisi": x["video"],
                  "tam_liste": tok is None,
                  "ilk_uzunlar": [{"id": a["id"], "yayin": a["snippet"]["publishedAt"], "baslik": a["snippet"]["title"],
                                   "sure_sn": sure(a["contentDetails"]["duration"]), "izlenme": int(a["statistics"].get("viewCount", 0))} for a in uzun]})
json.dump({"olcum_utc": now, "kaynak": "YouTube Data API v3 (videos, channels, commentThreads, playlistItems)",
           "video": {"id": vid, "baslik": v["snippet"]["title"], "publishedAt": v["snippet"]["publishedAt"], "sure": v["contentDetails"]["duration"],
                     "durum": v["status"]["privacyStatus"], **{k: int(x) for k, x in v["statistics"].items()}},
           "kanal": {k: x for k, x in ch.items()}, "yorumlar": yorum, "rakip_ilk_videolar": rakip}, open(out, "w"), ensure_ascii=False, indent=1)
print("ok", len(rakip))
