#!/usr/bin/env python3
"""kanal-analisti F1 delta (90 gün): niş outlier'ları, iki skor:
 skor_med = izlenme / kanal medyanı (kanalın son <=30 uzun (>=4 dk), >=7 günlük videosu)
 skor_abone = izlenme / abone
Kullanım: python3 delta90.py <rakip-veri.json> <cikti.json> [--arama N]  (search 100 birim/sorgu)"""
import json, os, sys, re, statistics, urllib.request, urllib.parse, datetime as dt
K = os.environ["YOUTUBE_API_KEY"]; B = "https://www.googleapis.com/youtube/v3/"
def api(ep, **p):
    p["key"] = K
    with urllib.request.urlopen(B + ep + "?" + urllib.parse.urlencode(p), timeout=30) as r: return json.load(r)
def dur(s):
    m = re.match(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", s or "")
    d, h, mi, se = [int(x or 0) for x in m.groups()]; return d*86400+h*3600+mi*60+se
src, out = sys.argv[1], sys.argv[2]
now = dt.datetime.now(dt.timezone.utc).replace(microsecond=0)
bas = (now - dt.timedelta(days=90)).isoformat().replace("+00:00", "Z")
yedi = (now - dt.timedelta(days=7)).isoformat().replace("+00:00", "Z")
kanallar = set(json.load(open(src))["kanallar"].keys())
QUERIES = ["animated economics explained", "economy explained cartoon", "what happens if economy",
           "why is everything so expensive explained", "history of money animated", "how the rich avoid taxes explained",
           "stock market crash explained animation", "national debt explained animated", "dollar collapse explained",
           "housing market explained animated"]
nq = int(sys.argv[sys.argv.index("--arama")+1]) if "--arama" in sys.argv else len(QUERIES)
arama_log, arama_vid = [], {}
for q in QUERIES[:nq]:
    try:
        r = api("search", part="snippet", q=q, type="video", order="viewCount", publishedAfter=bas,
                videoDuration="long", relevanceLanguage="en", maxResults=25)
        ids = {i["snippet"]["channelId"] for i in r.get("items", [])}
        for i in r.get("items", []): arama_vid[i["id"]["videoId"]] = q
        kanallar |= ids; arama_log.append({"q": q, "kanal": len(ids)})
    except Exception as e:
        arama_log.append({"q": q, "hata": str(e)[:80]}); break
kan = {}; kl = list(kanallar)
for i in range(0, len(kl), 50):
    for c in api("channels", part="snippet,statistics,contentDetails", id=",".join(kl[i:i+50])).get("items", []):
        kan[c["id"]] = {"ad": c["snippet"]["title"], "abone": int(c["statistics"].get("subscriberCount", 0)),
                        "acilis": c["snippet"]["publishedAt"][:10], "up": c["contentDetails"]["relatedPlaylists"]["uploads"]}
rows, med, shorts = [], {}, {}
for cid, c in kan.items():
    vids, tok = [], None
    try:
        for _ in range(2):
            p = dict(part="contentDetails", playlistId=c["up"], maxResults=50)
            if tok: p["pageToken"] = tok
            pl = api("playlistItems", **p); vids += [x["contentDetails"]["videoId"] for x in pl.get("items", [])]
            tok = pl.get("nextPageToken")
            if not tok or pl["items"][-1]["contentDetails"].get("videoPublishedAt", "9") < bas: break
    except Exception: continue
    vs = []
    for j in range(0, len(vids), 50):
        vs += api("videos", part="snippet,statistics,contentDetails", id=",".join(vids[j:j+50])).get("items", [])
    uz, sh = [], []
    for v in vs:
        s = dur(v["contentDetails"]["duration"]); iz = int(v["statistics"].get("viewCount", 0))
        rec = {"id": v["id"], "baslik": v["snippet"]["title"], "yayin": v["snippet"]["publishedAt"], "sure_dk": round(s/60, 1),
               "izlenme": iz, "dil": v["snippet"].get("defaultAudioLanguage", "")}
        (uz if s >= 240 else sh).append(rec)
    uz.sort(key=lambda x: x["yayin"], reverse=True)
    if not uz or uz[0]["yayin"] < bas: continue
    taban = [x for x in uz if x["yayin"] < yedi][:30]
    if len(taban) < 5: continue
    m = statistics.median(x["izlenme"] for x in taban)
    med[cid] = {"ad": c["ad"], "medyan": m, "n": len(taban), "abone": c["abone"], "acilis": c["acilis"]}
    sh90 = [x for x in sh if x["yayin"] >= bas]
    shorts[cid] = {"n90": len(sh90), "medyan90": statistics.median([x["izlenme"] for x in sh90]) if sh90 else 0,
                   "uzun_n90": sum(1 for x in uz if x["yayin"] >= bas)}
    for x in uz:
        if x["yayin"] >= bas:
            x.update(kanal=c["ad"], kanal_id=cid, abone=c["abone"], kanal_medyan=m, skor_med=round(x["izlenme"]/max(m, 1), 2),
                     skor_abone=round(x["izlenme"]/max(c["abone"], 1), 2), aramadan=arama_vid.get(x["id"]),
                     yas_gun=round((now - dt.datetime.fromisoformat(x["yayin"].replace("Z", "+00:00"))).total_seconds()/86400, 1))
            rows.append(x)
rows.sort(key=lambda x: -x["skor_med"])
json.dump({"olcum_utc": now.isoformat(), "kaynak": "YouTube Data API v3", "pencere": [bas, now.isoformat()],
           "tanim": "skor_med = izlenme / kanalin son <=30 uzun (>=4 dk) ve >=7 gunluk videosunun medyani; skor_abone = izlenme / abone",
           "arama": arama_log, "kanal_sayisi": len(med), "medyanlar": med, "shorts": shorts, "videolar_90g": rows},
          open(out, "w"), ensure_ascii=False, indent=1)
print(len(kan), "kanal;", len(med), "aktif;", len(rows), "video (90g)"); print(arama_log)
