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

# (senaryo, video id, neden yakin) — id'ler 01-arastirma/olcum/youtube-arama.json ve rakip-ozet.md
HEDEFLER = [
    ("S01", "5eZj1OnC1C4", "Binance 6,3 milyar, Gloam (5 gunluk)"),
    ("S01", "PSHQ_MuxxNw", "The Bank Heist of the Century, fern"),
    ("S01", "WyQ7z8BMwwk", "Hackers stole 1B from banks, fern"),
    ("S01", "aM-W59jNwxU", "Smartest bank heist, Joe Bartolozzi"),
    ("S01", "C5eoTRUZzCo", "Hacker stole 1,5B (Bybit), Lume"),
    ("S02", "ZJNQrpEhAd4", "Where did Madoff's 65B go, Sticks and Cents"),
    ("S02", "ByO51GD0D84", "Madoff final victims payout, Facts Verse"),
    ("S03", "wuJfl4Xuj9Q", "Boomers gone, AJ Osborne"),
    ("S03", "OSF3n3Btz7k", "Everybody blames boomers, Philosophase"),
    ("S03", "84mdMwgrks8", "Boomers GONE, Austin Williams"),
    ("S03", "KUx-H5A6b6Y", "After boomers die off, Infographics"),
    ("S04", "gL8dtgfhhn0", "Who will buy boomers houses, Hawk Live"),
    ("S04", "09FevuUtoOc", "Boomers sell houses Gen Z, Casey Simpson"),
    ("S04", "U12TK2Sa5HQ", "Real estate when boomers die, How Money Works (2024)"),
    ("S05", "zhQVjly5Gos", "Which rich country bankrupt first, OBF"),
    ("S05", "I-YTP-P_ujw", "Which rich country broke first, Broke Economy"),
    ("S05", "1nJaHq_lnpc", "Which G7 bankrupt first, Economics Help"),
    ("S05", "lL14_pa32j8", "Countries bankrupt first, Finance Stack (3 gunluk)"),
    ("S06", "TmlvDH0ZFB4", "Who does America owe 40T, PENNY"),
    ("S06", "7SZsXdxhG_U", "Every nation in debt who paying, Hidden Capital"),
    ("S06", "-AU8-Vg6f2M", "Who is lending the money, Invisible Hand"),
    ("S07", "AE-zDmbokos", "Man who stole 65B, Built on Lies"),
    ("S07", "5bxmfEuHk8c", "Man who stole 65B, Infographics (2018)"),
    ("S08", "sD0RcD9rq_c", "AI bubble will burst what next, Not Unprecedented"),
    ("S08", "zWJ-g5u9Rqs", "AI vs dot com, Infographics"),
    ("S08", "T9d6lrvzM9o", "AI bubble bursts day by day, Infographics"),
    ("S09", "eQ7nWjVbte0", "Mansa Musa gold, Documentary Empire"),
    ("S09", "4HQGHR5qUcQ", "Mansa Musa far from richest, hoser"),
    ("S09", "WqFWvk-Vv5c", "Richest person in history, jack pockets"),
    ("S10", "iDDjFwnO0xU", "Most expensive mistakes pt2, BE AMAZED"),
    ("S10", "BXlR9t7RTHc", "Mistakes that cost billions, BE AMAZED"),
    ("S11", "_LFyZurFt18", "What if world dumps US debt, Infographics (yakin ama bank run degil)"),
    ("S11", "C9k3Pg4kNww", "Fed warning savings account, Epic Real Estate"),
    ("S12", "sAABDnmn29Y", "Bought nearly all world's silver, Investigate Money"),
    ("S12", "03kaX3zvZ1g", "Trade so profitable regulators banned, Hamish Hodder"),
    ("S12", "ayTQn2jGtS0", "Silver running out why crashing, Why X"),
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
        sonra = [t for t in uzun if t[0] > v["yayin"] and t[0] < "2026-10-28"]
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
    print(json.dumps({"olcum_tarihi": "2026-11-04", "tanim": "izlenme / hedef haric cevredeki <=10 uzun (>=4 dk) yuklemenin medyani [API][H]", "sonuc": sonuc}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
