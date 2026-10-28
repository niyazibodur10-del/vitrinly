#!/usr/bin/env python3
"""kanal-analisti F1 delta: son 30 gün niş outlier'ları (B güncel / C gelecek).
Girdi: önceki kanal listesi JSON + hedefli arama. Çıktı: delta-veri-<tarih>.json
Kullanım: python3 delta30.py <onceki.json> <cikti.json> [--arama N]"""
import json, os, sys, re, statistics, urllib.request, urllib.parse, datetime as dt
K = os.environ["YOUTUBE_API_KEY"]; B = "https://www.googleapis.com/youtube/v3/"
def api(ep, **p):
    p["key"] = K
    with urllib.request.urlopen(B + ep + "?" + urllib.parse.urlencode(p), timeout=30) as r:
        return json.load(r)
def dur(s):
    m = re.match(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", s or "")
    d, h, mi, se = [int(x or 0) for x in m.groups()]; return d*86400+h*3600+mi*60+se
src, out = sys.argv[1], sys.argv[2]
now = dt.datetime(2026, 10, 28, tzinfo=dt.timezone.utc)
bas30 = (now - dt.timedelta(days=30)).isoformat().replace("+00:00", "Z")
kanallar = set(json.load(open(src))["kanallar"].keys())
QUERIES = ["what happens if economy explained", "economy news explained animated",
           "tariffs explained economy", "AI bubble explained", "recession 2027 explained",
           "the future of money explained", "gold price explained why", "national debt crisis explained"]
arama_log = []
nq = int(sys.argv[sys.argv.index("--arama")+1]) if "--arama" in sys.argv else len(QUERIES)
for q in QUERIES[:nq]:
    try:
        r = api("search", part="snippet", q=q, type="video", order="viewCount", publishedAfter=bas30,
                videoDuration="long", relevanceLanguage="en", maxResults=25)
        ids = {i["snippet"]["channelId"] for i in r.get("items", [])}
        kanallar |= ids; arama_log.append({"q": q, "kanal": len(ids)})
    except Exception as e:
        arama_log.append({"q": q, "hata": str(e)[:80]}); break
kan = {}
kl = list(kanallar)
for i in range(0, len(kl), 50):
    for c in api("channels", part="snippet,statistics,contentDetails", id=",".join(kl[i:i+50])).get("items", []):
        kan[c["id"]] = {"ad": c["snippet"]["title"], "abone": int(c["statistics"].get("subscriberCount", 0)),
                        "up": c["contentDetails"]["relatedPlaylists"]["uploads"]}
rows, med = [], {}
for cid, c in kan.items():
    try: pl = api("playlistItems", part="contentDetails", playlistId=c["up"], maxResults=50)
    except Exception: continue
    vids = [x["contentDetails"]["videoId"] for x in pl.get("items", [])]
    if not vids: continue
    vs = api("videos", part="snippet,statistics,contentDetails", id=",".join(vids)).get("items", [])
    uz = []
    for v in vs:
        s = dur(v["contentDetails"]["duration"])
        if s < 240: continue
        uz.append({"id": v["id"], "baslik": v["snippet"]["title"], "yayin": v["snippet"]["publishedAt"],
                   "sure_dk": round(s/60, 1), "izlenme": int(v["statistics"].get("viewCount", 0)),
                   "dil": v["snippet"].get("defaultAudioLanguage", "")})
    uz.sort(key=lambda x: x["yayin"], reverse=True)
    if not uz or uz[0]["yayin"] < bas30: continue
    taban = [x for x in uz if x["yayin"] < "2026-10-21"][:20]
    if len(taban) < 5: continue
    m = statistics.median(x["izlenme"] for x in taban)
    med[c["ad"]] = {"medyan": m, "n": len(taban), "abone": c["abone"]}
    for x in uz:
        if x["yayin"] >= bas30:
            x.update(kanal=c["ad"], abone=c["abone"], kanal_medyan=m, skor=round(x["izlenme"]/max(m, 1), 2),
                     yas_gun=round((now - dt.datetime.fromisoformat(x["yayin"].replace("Z", "+00:00"))).total_seconds()/86400, 1))
            rows.append(x)
rows.sort(key=lambda x: -x["skor"])
json.dump({"olcum_tarihi": now.date().isoformat(), "kaynak": "YouTube Data API v3", "pencere": [bas30, "2026-10-28"],
           "tanim": "skor = izlenme / kanalin 2026-10-21 oncesi son 20 uzun (>=4 dk) videosunun medyani",
           "arama": arama_log, "kanal_sayisi": len(med), "medyanlar": med, "videolar_30g": rows},
          open(out, "w"), ensure_ascii=False, indent=1)
print(len(kan), "kanal;", len(med), "aktif;", len(rows), "video (30g)"); print(arama_log)
