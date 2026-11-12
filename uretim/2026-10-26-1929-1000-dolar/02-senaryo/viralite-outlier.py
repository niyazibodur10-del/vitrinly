#!/usr/bin/env python3
"""viralite-analisti: senaryo konularına en yakın rakip videoların YEREL MEDYAN outlier skoru.

Model v0.1 tanımı (docs/viralite-modeli.md): outlier = izlenme / videonun çevresindeki ~10 uzun yüklemenin
(öncesi + sonrası, hedef hariç, >=4 dk) medyan izlenmesi. Sonrası yetmezse öncesinden tamamlanır.
Yalnız YouTube Data API v3 (videos, channels, playlistItems; search KULLANILMAZ, 1 birim/istek).
Anahtar ortam değişkeninden okunur (YOUTUBE_API_KEY), dosyaya yazılmaz.

Kullanım: python3 viralite-outlier.py > viralite-outlier.json
"""
import json
import os
import re
import statistics
import sys
import urllib.parse
import urllib.request

KEY = os.environ.get("YOUTUBE_API_KEY")
API = "https://www.googleapis.com/youtube/v3/"

# (senaryo, video id, neden yakın) — id'ler F1 ölçümlerinden (olcum/youtube-arama*.json, rakip-ozet.md)
HEDEFLER = [
    ("S01/S02/S03", "jwmdk6-X6LM", "1929 / Great Depression, Markets of the Past"),
    ("S01/S02/S03", "KRQDfe8Mh2A", "1929 / Great Depression, SLICE History"),
    ("S01/S02/S03", "VsH2FXOi1PQ", "1929 + bugün köprüsü, The Money Files"),
    ("S01/S02/S03", "qF3ekm9Gx_E", "1929 / Great Depression, Casual Economics (2025-03)"),
    ("S02", "uYKq1xrZmt0", "banka kaçışı (1907), Investigate Money"),
    ("S04", "ICjjCMsaKBA", "Weimar 1923, gündelik hayat anlatısı"),
    ("S05", "F9hSsmd49p8", "petrol şoku (2026 bağlamı), Asian Boss"),
    ("S05", "q1Ol9G-2WTc", "petrol arzı tarihi, How Business Worked"),
    ("S05/S06", "DKyJABtbF2o", "1973 borsa çöküşü / Nifty Fifty, Casual Finance"),
    ("S07", "n4vssvd2d8k", "Black Monday 1987, Finance Bureau"),
    ("S08", "sAABDnmn29Y", "Hunt kardeşler gümüş, Investigate Money"),
    ("S08", "mQL1TQCpzhQ", "Hunt kardeşler gümüş, History Meets Finance"),
    ("S09", "w5kdK-dQ414", "2008 krizi, Fred - Money Historian"),
    ("S09", "v1s5qXyxmVo", "2008 krizi, MonkeyExplains"),
    ("S10", "vTPpF3G3wJ0", "Japonya balonu, How Business Worked"),
    ("S11", "vXQdYFcT_uE", "LTCM, Hamish Hodder"),
]


def get(ucnokta, **p):
    p["key"] = KEY
    url = API + ucnokta + "?" + urllib.parse.urlencode(p)
    with urllib.request.urlopen(url, timeout=30) as r:
        return json.load(r)


def sure_sn(iso):
    m = re.fullmatch(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", iso or "")
    if not m:
        return 0
    d, h, mi, s = (int(x or 0) for x in m.groups())
    return d * 86400 + h * 3600 + mi * 60 + s


def videolar(ids):
    out = {}
    for i in range(0, len(ids), 50):
        r = get("videos", part="snippet,statistics,contentDetails", id=",".join(ids[i:i + 50]), maxResults=50)
        for it in r.get("items", []):
            out[it["id"]] = {
                "baslik": it["snippet"]["title"],
                "kanal": it["snippet"]["channelTitle"],
                "kanal_id": it["snippet"]["channelId"],
                "yayin": it["snippet"]["publishedAt"][:10],
                "izlenme": int(it["statistics"].get("viewCount", 0)),
                "sure_sn": sure_sn(it["contentDetails"]["duration"]),
            }
    return out


def yuklemeler(kanal_id, hedef_tarih, sayfa_max=6):
    r = get("channels", part="contentDetails,statistics", id=kanal_id)
    it = r["items"][0]
    pl = it["contentDetails"]["relatedPlaylists"]["uploads"]
    abone = int(it["statistics"].get("subscriberCount", 0))
    ids, token = [], None
    for _ in range(sayfa_max):
        p = {"part": "contentDetails", "playlistId": pl, "maxResults": 50}
        if token:
            p["pageToken"] = token
        rr = get("playlistItems", **p)
        page = [x["contentDetails"]["videoId"] for x in rr.get("items", [])]
        ids += page
        token = rr.get("nextPageToken")
        # hedeften 6+ eski video görünce dur
        dates = [x["contentDetails"].get("videoPublishedAt", "")[:10] for x in rr.get("items", [])]
        if not token or sum(1 for d in dates if d and d < hedef_tarih) >= 8:
            break
    return ids, abone


def main():
    if not KEY:
        print("YOUTUBE_API_KEY yok", file=sys.stderr)
        return 2
    hedef_bilgi = videolar([h[1] for h in HEDEFLER])
    sonuc = []
    for senaryo, vid, neden in HEDEFLER:
        v = hedef_bilgi.get(vid)
        if not v:
            sonuc.append({"senaryo": senaryo, "id": vid, "hata": "video bulunamadı"})
            continue
        ids, abone = yuklemeler(v["kanal_id"], v["yayin"])
        info = videolar(ids)
        uzun = sorted(
            [(x["yayin"], k, x["izlenme"]) for k, x in info.items() if x["sure_sn"] >= 240 and k != vid],
            key=lambda t: (t[0], t[1]),
        )
        once = [t for t in uzun if t[0] <= v["yayin"]]
        sonra = [t for t in uzun if t[0] > v["yayin"] and t[0] < "2026-10-20"]
        s = sonra[:5]
        o = once[-(10 - len(s)):] if once else []
        if len(o) + len(s) < 10:
            s = sonra[: 10 - len(o)]
        komsu = o + s
        med = statistics.median([t[2] for t in komsu]) if komsu else None
        sonuc.append({
            "senaryo": senaryo,
            "neden_yakin": neden,
            "id": vid,
            "baslik": v["baslik"],
            "kanal": v["kanal"],
            "abone": abone,
            "yayin": v["yayin"],
            "sure_dk": round(v["sure_sn"] / 60, 1),
            "izlenme": v["izlenme"],
            "komsu_n": len(komsu),
            "yerel_medyan": med,
            "skor": round(v["izlenme"] / med, 2) if med else None,
        })
    print(json.dumps({"olcum_tarihi": "2026-10-27", "tanim": "izlenme / hedef haric cevredeki <=10 uzun (>=4 dk) yuklemenin medyani [API][H]", "sonuc": sonuc}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
