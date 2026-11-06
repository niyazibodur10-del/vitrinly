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
    ("S01", "LhkuNV1RGfI", "Cin AI hisseleri, Palki Sharma (haber kanali)"),
    ("S01", "uU2WeAX2w8g", "Cin AI hisseleri, Reuters"),
    ("S01", "XEMvG2vulKg", "AI balonu cokusu, Damon Cassidy"),
    ("S01", "T9d6lrvzM9o", "AI balonu ne olur (C1 formati), Infographics Show"),
    ("S02", "tdXFaVaJfTo", "CoreWeave borcu, Prof G Markets"),
    ("S02", "o8ZGRemy4tM", "AI ozel kredi kacisi, Mark Tilbury"),
    ("S02", "qe9ePOlGdu4", "AI borc getirileri, Steve Eisman"),
    ("S03", "cO9NY1PeBZg", "Anthropic S-1 zarar, Breaking Points"),
    ("S03", "ilkjZXwb8dU", "Anthropic S-1, Prof G Markets"),
    ("S03", "n-JvcqJ5-oE", "Anthropic finansallari, Joseph Carlson"),
    ("S04", "B4PmR-bPMFk", "Yuksek Mahkeme tarife karari, CNN (Subat)"),
    ("S04", "Og49dNxv1I8", "tarife karari aciklama, Washington Gun Law"),
    ("S05", "AyMHJBLc_tA", "What Happens If Trump Loses The Midterms, Finance Bureau"),
    ("S05", "LaBiYw1ZKF4", "her ara secimden sonra borsa, ClearValue Tax"),
    ("S05", "8aRHUhVcSqQ", "her ara secim, Business With Brian"),
    ("S06", "9DTLfGiaNpc", "10 yillik %5, WhiteBoard Finance"),
    ("S06", "BMdLiG8J7-g", "tahviller, CNBC"),
    ("S07", "SJwCJXzgRME", "konut piyasasi garip donus, MHFIN"),
    ("S07", "BWNOdHB8TKA", "konut piyasasi, Graham Stephan"),
    ("S07", "Xj-IdfNnV08", "konut piyasasi, Damon Cassidy"),
    ("S08", "QmWyQ-BCD8E", "ABD borc temerrudu, How Money Works"),
    ("S08", "8M8U9Tj15bI", "ABD borcunu odemek, Infographics Show"),
    ("S09", "8PPXIQRB_4g", "Volcker belgeseli, FINAiUS (2022)"),
    ("S09", "9T3vPFgD5j8", "Volcker soku, Sleeping Economist"),
    ("S11", "hQpmpEalwIA", "rupi 100, Gaurav Thakur (2024)"),
    ("S11", "0SbRUdxrZQI", "dolar 100 rupi olursa, The News Minute"),
    ("S11", "1P3jK2wEaHc", "RBI rupiyi kurtarir mi, FinnovationZ"),
    ("S12", "RwZrPUh924M", "dizel krizi, Fred - Money Historian"),
    ("S12", "c_nSo7Rl74A", "100$ petrol Suudi, Fred - Money Historian"),
    ("S12", "oGsOAQORT1E", "benzin istasyonlari uyarisi, Eurodollar University"),
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
        sonra = [t for t in uzun if t[0] > v["yayin"] and t[0] < "2026-10-26"]
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
    print(json.dumps({"olcum_tarihi": "2026-11-02", "tanim": "izlenme / hedef haric cevredeki <=10 uzun (>=4 dk) yuklemenin medyani [API][H]", "sonuc": sonuc}, ensure_ascii=False, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
