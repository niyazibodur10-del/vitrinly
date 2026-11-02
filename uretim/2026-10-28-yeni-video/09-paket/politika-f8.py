#!/usr/bin/env python3
"""F8 paket politika denetimi v2 (S08) — monetizasyon-uyum-uzmani. 1929 politika-f8.py'den türetildi.
Kullanım (üretim klasöründen): python3 -I 09-paket/politika-f8.py [--video 07-animasyon/tam-16x9.mp4]
[1] meta veri dili (1311392 AI persona, 6162278) + P1 siyaset · [2] AI beyanı (14328491) ·
[3] başlık/thumbnail/Shorts vaadi ↔ kilitli anlatım · [4] lisans: cue → kayıt → kanıt sayfası (Content ID) ·
[5] yeniden kullanılan sahne oranı: 1 fps dHash ≤6/64 vs önceki renderlar (iç kural ≤ %20) ·
[6] dış klip: video/public/kbutce altında video dosyası. Deterministik."""
import json, os, re, subprocess, sys

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPO = os.path.dirname(os.path.dirname(KOK))
ADVICE = [r"\byou should\b", r"\byou need to\b", r"\byou must\b", r"\brecommend", r"\bmy advice\b",
          r"\bbuy now\b", r"\bsell now\b", r"\bguarantee", r"\binvest in\b", r"\bbest investment\b",
          r"\btips?\b", r"\bput your (money|savings)\b", r"\bprotect your", r"\byour money\b",
          r"\bget rich\b", r"\bsecret\b", r"\bexpert\b", r"\bgold\b", r"\bsafest\b"]
SHOCK = [r"\bcollapse", r"\bcrash", r"\bdefault", r"\bbankrupt", r"\bdoom", r"\bspiral", r"\bdeath\b",
         r"\bkill", r"\bterror", r"\bshock", r"\bhorr", r"\bshit", r"\bfuck", r"\bdamn\b", r"\bhell\b"]
P1 = [r"\btrump", r"\bbiden", r"\bharris", r"\bdemocrat", r"\brepublican", r"\bgop\b", r"\bpresident",
      r"\belection", r"\bmidterm", r"\bvot(e|er)", r"\bparty\b", r"\bcongress", r"\bwhite house"]
AI_SATIR = "Narration voice is AI-generated. Visuals are AI-assisted illustrations animated by our team."


def norm(t):
    return " ".join(re.findall(r"[a-z0-9']+", t.lower().replace("’", "'")))


def bul(ds, t):
    return sorted({m.group(0).lower() for d in ds for m in re.finditer(d, t, re.I)})


def govde(a):
    a = re.sub(r"LEGAL NOTE\n.*?\n\n", "", a, flags=re.S)
    a = re.sub(r"(MUSIC & SOUND|SOURCES)\n.*?\n\n", "", a, flags=re.S)
    a = re.sub(r"Music: .*\n", "", a)
    for x in (AI_SATIR, "Not financial advice.", "not a financial adviser"):
        a = a.replace(x, "")
    return a


def anlatim():
    md = open(os.path.join(KOK, "03-metin/metin.md"), encoding="utf-8").read()
    ana = re.findall(r"\| ANLATIM \| GÖRSEL \|\n\|---\|---\|\n\| ([^|]+)\|", md)
    return norm(" ".join(ana)), [norm(s) for s in re.findall(r"Okunacak tam metin[^<]*<<(.*?)>>", md)]


def dhash(yol, fps):
    ham = subprocess.run(["ffmpeg", "-v", "error", "-i", yol, "-vf", f"fps={fps},scale=9:8,format=gray",
                          "-f", "rawvideo", "-"], capture_output=True, check=True).stdout
    hs = []
    for i in range(0, len(ham) - 71, 72):
        b, v = ham[i:i + 72], 0
        for r in range(8):
            for c in range(8):
                v = (v << 1) | (b[r * 9 + c] > b[r * 9 + c + 1])
        hs.append(v)
    return hs


def main():
    a = sys.argv[1:]
    video = os.path.join(KOK, a[a.index("--video") + 1] if "--video" in a else "07-animasyon/tam-16x9.mp4")
    hata, P = 0, os.path.join(KOK, "09-paket")
    pk = {k: json.load(open(os.path.join(P, f), encoding="utf-8")) for k, f in
          [("uzun", "yayin-paketi.json"), ("shorts-1", "yayin-paketi-shorts-1.json"), ("shorts-2", "yayin-paketi-shorts-2.json")]}
    md = open(os.path.join(P, "paket.md"), encoding="utf-8").read()
    blok = lambda ad: re.search(rf"<!-- veri:{ad} -->\n```text\n(.*?)```", md, re.S).group(1)
    print("[1] Meta veri dili (tavsiye · şok/korku · P1 siyaset)")
    parca = []
    for k, p in pk.items():
        m = p["metadata"]
        parca += [(k, "baslik", m["baslik"]), (k, "aciklama", govde(m["aciklama"])), (k, "etiket", ", ".join(m.get("etiketler", [])))]
    parca += [("paket.md", "yedek-baslik", blok("basliklar")), ("paket.md", "pinli", blok("pinli-yorum"))]
    for k, ad, t in parca:
        x = (bul(ADVICE, t), bul(SHOCK, t), bul(P1, t))
        print(f"  {k:9s} {ad:12s} {'0' if not any(x) else 'tavsiye=%s sok=%s P1=%s' % x}")
        hata += any(x)
    print("[2] AI beyanı")
    for k, p in pk.items():
        sm, ac = p["durum"].get("sentetik_medya"), p["metadata"]["aciklama"]
        print(f"  {k:9s} sentetik_medya={sm} ai_satiri={AI_SATIR in ac} not_financial_advice={'Not financial advice.' in ac} cocuk={p['durum'].get('cocuklara_ozel')}")
        hata += (sm is not True) + (AI_SATIR not in ac)
    print("[3] Vaat ↔ kilitli anlatım")
    ana, sh = anlatim()
    vaat = [("T1 baslik", ["five thousand four hundred dollars a month", "kitchen table"], ana),
            ("T2 yedek 'one kitchen table'", ["kitchen table"], ana),
            ("T3 yedek 'interest > military'", ["pays its lenders more than it pays for its whole military"], ana),
            ("T4 yedek '$7 for every $5'", ["seven thousand four hundred", "five thousand four hundred"], ana),
            ("T5 yedek 'tripled in five years'", ["in just five years, the interest bill roughly tripled"], ana),
            ("thumb A1 −$2,000 EVERY MONTH", ["every single month", "two thousand dollars short"], ana),
            ("thumb C1 INTEREST > MILITARY", ["more than it pays for its whole military"], ana),
            ("thumb B1 EVERY MONTH −2,000", ["every single month", "two thousand dollars"], ana),
            ("shorts-1 interest vs military", ["interest", "military", "more than it pays for its whole military"], sh[0]),
            ("shorts-2 1946 > economy", ["nineteen forty-six", "bigger than the whole economy", "nineteen seventy-four"], sh[1]),
            ("shorts-2 niteleyici", ["history, not a forecast"], sh[1]),
            ("pinli A/B/C", ["grow the paycheck", "change the envelopes", "let prices rise"], ana)]
    for ad, ifs, t in vaat:
        eks = [i for i in ifs if norm(i) not in t]
        print(f"  {ad:34s} {'VAR' if not eks else 'EKSIK ' + str(eks)}"); hata += bool(eks)
    print(f"  shorts okuma metni tavsiye: {[bul(ADVICE, s) for s in sh]}")
    print("[4] Lisans + Content ID kanıtı")
    kayit = open(os.path.join(KOK, "06-muzik/lisans-kaydi.md"), encoding="utf-8").read()
    lis_lib = open(os.path.join(REPO, "assets/LISANSLAR.md"), encoding="utf-8").read()
    cue = json.load(open(os.path.join(KOK, "06-muzik/cue.json"), encoding="utf-8"))
    kanit = set(os.listdir(os.path.join(REPO, "assets/lisans-kanit")))
    dos = sorted({os.path.basename(c["dosya"]) for c in cue["muzik"] + cue["sfx"] + cue["shorts"]})
    kayitsiz, kanitsiz, nc = [], [], []
    def acilmis(l):  # "paper_01/02/03" grup yazımını aç (lisans-kontrol.py ile aynı kural)
        for g in re.findall(r"([\w-]*?)(\d+)((?:/\d+)+)", l):
            l += " " + " ".join(g[0] + n for n in g[2].strip("/").split("/"))
        return l
    for d in dos:
        kok = d.rsplit(".", 1)[0]
        satir = next((l for l in map(acilmis, kayit.splitlines()) if kok in l), None) or next((l for l in lis_lib.splitlines() if kok in l), None)
        if satir is None:
            kayitsiz.append(d); continue
        if re.search(r"\b(NC|ND|SA)\b|BY-NC|BY-ND|BY-SA", satir): nc.append(d)
        if "Bizim" in satir or "ozgun" in kok: continue
        refs = re.findall(r"((?:oga|kenney|freesound|pd)-[\w.-]+?\.(?:html|txt))", satir)
        if refs and not all(r in kanit for r in refs): kanitsiz.append(d)
        if not refs and satir in kayit: kanitsiz.append(d + "(ref yok)")
    print(f"  cue dosyası {len(dos)} · kayıtsız {kayitsiz} · NC/ND/SA {nc} · kanıt eksik {kanitsiz}")
    hata += bool(kayitsiz) + bool(nc) + bool(kanitsiz)
    print("[5] Yeniden kullanılan sahne oranı (1 fps dHash ≤6/64)")
    onceki = ["uretim/ses-testi/pilot/pilot-v1.mp4", "uretim/ses-testi/pilot/pilot-v2.mp4",
              "uretim/ses-testi/yayin-manuel/video.mp4", "uretim/2026-10-26-1929-1000-dolar/08-kurgu/final-16x9.mp4"]
    havuz = []
    for o in onceki:
        hs = [h for h in dhash(os.path.join(REPO, o), "1") if h]; havuz += hs
        print(f"  önceki {o}: {len(hs)} kare")
    bu = [h for h in dhash(video, "1") if h]
    es = [i for i, h in enumerate(bu) if min(bin(h ^ p).count("1") for p in havuz) <= 6]
    oran = 100.0 * len(es) / max(1, len(bu))
    print(f"  bu video geçerli {len(bu)} kare, eşleşen {len(es)} → %{oran:.1f} (≤ %20) · eşleşen sn örnek {es[:15]}")
    hata += oran > 20
    print("[6] Dış klip")
    dis = sorted(os.path.relpath(os.path.join(r, f), REPO) for r, _, fs in os.walk(os.path.join(REPO, "video/public/kbutce"))
                 for f in fs if f.lower().endswith((".mp4", ".mov", ".webm", ".gif")))
    print(f"  video/public/kbutce video klip: {dis or 0}")
    print(f"SONUC hata={hata}")
    return 1 if hata else 0


if __name__ == "__main__":
    sys.exit(main())
