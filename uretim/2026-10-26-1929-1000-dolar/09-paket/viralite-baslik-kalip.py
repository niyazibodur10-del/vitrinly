#!/usr/bin/env python3
"""viralite-analisti (F8): paket başlığının (T1 ve yedekler) kalıplarını rakip 12 ay verisinde yerel medyanla ölçer.

Kanal listesi: 01-arastirma/rakip-veri-2026-10-27.json (kanal-analisti, 39 kanal).
Pencere: 2025-10-20 .. 2026-10-20 (son 7 gün hariç), uzun video (>=240 sn).
Skor = izlenme / aynı kanalda çevredeki 10 uzun yüklemenin medyanı (hedef hariç; 5 önce + 5 sonra, eksikse diğer
taraftan tamamlanır) = model v0.1 yerel medyan tanımı.
Yalnız channels / playlistItems / videos (1 birim/istek; search YOK). Anahtar ortam değişkeninden (YOUTUBE_API_KEY).

Kullanım:
  python3 viralite-baslik-kalip.py --cek  ham.json      # API'den çek (bir kez)
  python3 viralite-baslik-kalip.py ham.json             # deterministik analiz (2 koşu aynı olmalı)
"""
import json
import os
import re
import statistics
import sys
import urllib.parse
import urllib.request

API = "https://www.googleapis.com/youtube/v3/"
BAS, SON = "2025-10-20", "2026-10-20"
KOK = os.path.dirname(os.path.abspath(__file__))
KANAL_DOSYA = os.path.join(KOK, "..", "01-arastirma", "rakip-veri-2026-10-27.json")

KALIPLAR = [
    ("soru_isareti", r"\?"),
    ("ikinci_tekil (you/your)", r"\b(you|your|you're)\b"),
    ("dolar_tutari ($N)", r"\$\s?\d"),
    ("yil (1500-2029)", r"\b(1[5-9]\d\d|20[0-2]\d)\b"),
    ("can_you / could_you / would_you", r"\b(can|could|would) you\b"),
    ("survive / keep / save (kişisel sonuç fiili)", r"\b(surviv\w*|keep|kept|save[ds]?)\b"),
]
BILESIK = [
    ("T1 iskeleti: you + $N + yil", ["ikinci_tekil (you/your)", "dolar_tutari ($N)", "yil (1500-2029)"]),
    ("you + yil", ["ikinci_tekil (you/your)", "yil (1500-2029)"]),
    ("$N + yil", ["dolar_tutari ($N)", "yil (1500-2029)"]),
    ("you + soru", ["ikinci_tekil (you/your)", "soru_isareti"]),
]


def get(uc, **p):
    p["key"] = os.environ["YOUTUBE_API_KEY"]
    with urllib.request.urlopen(API + uc + "?" + urllib.parse.urlencode(p), timeout=30) as r:
        return json.load(r)


def sure_sn(iso):
    m = re.fullmatch(r"P(?:(\d+)D)?T?(?:(\d+)H)?(?:(\d+)M)?(?:(\d+)S)?", iso or "")
    if not m:
        return 0
    d, h, mi, s = (int(x or 0) for x in m.groups())
    return d * 86400 + h * 3600 + mi * 60 + s


def cek(cikis):
    kanallar = json.load(open(KANAL_DOSYA, encoding="utf-8"))["kanallar"]
    ham = {}
    for kid in sorted(kanallar):
        pl = "UU" + kid[2:]
        ids, token = [], None
        for _ in range(8):
            p = {"part": "contentDetails", "playlistId": pl, "maxResults": 50}
            if token:
                p["pageToken"] = token
            try:
                rr = get("playlistItems", **p)
            except Exception as e:  # kanal kapalı vb.
                print(f"{kid}: {e}", file=sys.stderr)
                break
            items = rr.get("items", [])
            ids += [x["contentDetails"]["videoId"] for x in items]
            token = rr.get("nextPageToken")
            tarih = [x["contentDetails"].get("videoPublishedAt", "")[:10] for x in items]
            # pencere öncesinden 6+ video (komşu için) görünce dur
            if not token or sum(1 for d in tarih if d and d < BAS) >= 6:
                break
        vids = []
        for i in range(0, len(ids), 50):
            r = get("videos", part="snippet,statistics,contentDetails", id=",".join(ids[i:i + 50]))
            for it in r.get("items", []):
                vids.append({
                    "id": it["id"], "baslik": it["snippet"]["title"], "yayin": it["snippet"]["publishedAt"][:10],
                    "izlenme": int(it["statistics"].get("viewCount", 0)),
                    "sure_sn": sure_sn(it["contentDetails"]["duration"]),
                })
        ham[kid] = {"ad": kanallar[kid]["ad"], "videolar": vids}
    json.dump({"olcum": "YouTube Data API v3, 2026-10-27", "kanallar": ham}, open(cikis, "w", encoding="utf-8"),
              ensure_ascii=False, indent=0, sort_keys=True)


def skorla(ham):
    satir = []
    for kid in sorted(ham["kanallar"]):
        k = ham["kanallar"][kid]
        uzun = sorted([v for v in k["videolar"] if v["sure_sn"] >= 240 and v["yayin"] < SON],
                      key=lambda v: (v["yayin"], v["id"]))
        for i, v in enumerate(uzun):
            if v["yayin"] < BAS:
                continue
            once, sonra = uzun[:i], uzun[i + 1:]
            s = sonra[:5]
            o = once[-(10 - len(s)):] if once else []
            if len(o) + len(s) < 10:
                s = sonra[:10 - len(o)]
            komsu = o + s
            if len(komsu) < 6:
                continue
            med = statistics.median([x["izlenme"] for x in komsu])
            if med < 1000:  # mikro kanallar gürültü
                continue
            satir.append({"kanal": k["ad"], "baslik": v["baslik"], "skor": v["izlenme"] / med})
    return satir


def ozet(satir, adlar):
    ic = [r for r in satir if all(re.search(dict(KALIPLAR)[a], r["baslik"], re.I) for a in adlar)]
    dis = [r for r in satir if r not in ic]

    def m(x):
        if not x:
            return "—", "—"
        return f"{statistics.median([r['skor'] for r in x]):.2f}", f"%{100 * sum(r['skor'] >= 3 for r in x) / len(x):.0f}"
    mi, oi = m(ic)
    md, od = m(dis)
    return len(ic), len({r["kanal"] for r in ic}), mi, oi, md, od, ic


def main():
    if len(sys.argv) == 3 and sys.argv[1] == "--cek":
        cek(sys.argv[2])
        return 0
    ham = json.load(open(sys.argv[1], encoding="utf-8"))
    satir = skorla(ham)
    print(f"Başlık kalıbı ölçümü [API][H] | pencere {BAS}..{SON} | uzun video, yerel medyan >=1000 | "
          f"n={len(satir)} video, {len({r['kanal'] for r in satir})} kanal")
    print(f"Tüm havuz: medyan skor {statistics.median([r['skor'] for r in satir]):.2f}, "
          f">=3x %{100 * sum(r['skor'] >= 3 for r in satir) / len(satir):.0f}")
    print()
    print("| Kalıp | n / kanal | Medyan skor | >=3x | Diğerleri medyan / >=3x |")
    print("|---|---|---|---|---|")
    ornek = {}
    for ad, _ in KALIPLAR:
        n, kn, mi, oi, md, od, _ic = ozet(satir, [ad])
        print(f"| {ad} | {n} / {kn} | {mi} | {oi} | {md} / {od} |")
    for ad, parca in BILESIK:
        n, kn, mi, oi, md, od, ic = ozet(satir, parca)
        print(f"| {ad} | {n} / {kn} | {mi} | {oi} | {md} / {od} |")
        ornek[ad] = sorted(ic, key=lambda r: (-r["skor"], r["baslik"]))[:6]
    print()
    for ad, lst in ornek.items():
        print(f"Örnekler — {ad}:")
        for r in lst:
            print(f"  {r['skor']:.2f}x | {r['kanal']} | {r['baslik']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
