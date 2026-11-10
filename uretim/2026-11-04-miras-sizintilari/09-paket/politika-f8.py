#!/usr/bin/env python3
"""F8 paket politika denetimi v3 (S03 miras) — monetizasyon-uyum-uzmani. S08 v2'den: vaat listesi S03, havuz = önceki 2 final,
kmiras klasörü, [7] kanal tekrar desenleri (kapanış 4-gram + Leo kalıpları, önceki metinlere karşı).
Kullanım (üretim klasöründen): python3 -I 09-paket/politika-f8.py [--video 07-animasyon/tam-16x9.mp4]
[1] meta veri dili (1311392 AI persona, 6162278) + P1 siyaset · [2] AI beyanı (14328491) ·
[3] başlık/thumbnail/Shorts vaadi ↔ kilitli anlatım · [4] lisans: cue → kayıt → kanıt sayfası (Content ID) ·
[5] yeniden kullanılan sahne oranı: 1 fps dHash ≤6/64 aday + 32x18 MAD ≤5 doğrulama vs önceki 2 final (iç kural ≤ %20) ·
[6] dış klip: video/public/kmiras altında video dosyası. [7] kanal tekrar. Deterministik."""
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
    vaat = [("T1 baslik 'Has a Leak'", ["which leak is the biggest", "to see the real leaks"], ana),
            ("T3 yedek 'Boomers' Money … Go'", ["baby boomers", "where the boxes actually went"], ana),
            ("T4 yedek 'Smaller Than It Sounds'", ["less than the headline sounds"], ana),
            ("T7 yedek 'Not When You Think'", ["get it later", "they come late"], ana),
            ("T5 yedek 'Biggest Inheritance Ever'", ["biggest inheritance in history"], ana),
            ("thumb K1 WHO GETS IT? + $124T", ["one hundred twenty-four trillion", "so let's count what reaches the kids",
              "for a few families the truck is a whole convoy", "for most it's a few boxes and they come late"], ana),
            ("thumb K4 IT KEEPS LEAKING", ["it gives the other leaks more time", "i'm going to need more tape"], ana),
            ("thumb K3 SMALLER. LATER.", ["less than the headline sounds", "get it later"], ana),
            ("aciklama 'later, not never' (es)", ["it isn't a leak at all", "the detour doesn't take any boxes"], ana),
            ("shorts-1 spouse first", ["fifty-four trillion is expected to stop at a surviving husband or wife first", "it isn't lost"], sh[0]),
            ("shorts-2 taxes / where", ["u s federal estate tax only starts above fifteen million dollars per person", "where does the money really go"], sh[1]),
            ("shorts-2 niteleyici (US)", ["most american families", "federal estate tax stop"], sh[1]),
            ("pinli 6 durak", ["a long life", "stop two", "spouse first", "stop four is giving", "stop five is the house", "stop six"], ana)]
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
    onceki = ["uretim/2026-10-26-1929-1000-dolar/08-kurgu/final-16x9.mp4", "uretim/2026-10-28-yeni-video/08-kurgu/final-16x9.mp4"]
    havuz = []  # (dhash, video, saniye)
    for o in onceki:
        hs = [(h, o, j) for j, h in enumerate(dhash(os.path.join(REPO, o), "1")) if h]; havuz += hs
        print(f"  önceki {o}: {len(hs)} kare")
    bu = [(i, h) for i, h in enumerate(dhash(video, "1")) if h]
    es = []
    for i, h in bu:
        d, o, j = min((bin(h ^ p).count("1"), o, j) for p, o, j in havuz)
        if d <= 6: es.append((i, o, j))
    ust = 100.0 * len(es) / max(1, len(bu))
    # 2. aşama (v3): dHash koyu ortak zeminde (lacivert vinyet) yanlış alarm verir → aday çiftleri 32x18 gri
    # ortalama mutlak farkla doğrula. Eşik 5/255: pozitif kontrol (aynı plan, 0,2 sn ara) ≈ 2,8; S03 yanlış alarm min 6,6.
    k32 = lambda y, t: subprocess.run(["ffmpeg", "-v", "error", "-ss", str(t), "-i", y, "-frames:v", "1", "-vf",
                                       "scale=32:18,format=gray", "-f", "rawvideo", "-"], capture_output=True, check=True).stdout
    mad = lambda a, b: sum(abs(x - y) for x, y in zip(a, b)) / max(1, len(a))
    poz = mad(k32(video, 300), k32(video, 300.2))
    dog = [(i, o, j, m) for i, o, j in es if (m := mad(k32(video, i), k32(os.path.join(REPO, o), j))) <= 5]
    oran = 100.0 * len(dog) / max(1, len(bu))
    kaynak = sorted({(os.path.basename(os.path.dirname(os.path.dirname(o)))[:14], j) for _, o, j in es})
    print(f"  bu video geçerli {len(bu)} kare · dHash aday {len(es)} → üst sınır %{ust:.1f} · eşleşen kaynak kare {len(kaynak)} adet {kaynak[:8]}")
    print(f"  2. aşama 32x18 MAD ≤5 (pozitif kontrol {poz:.1f}): doğrulanmış {len(dog)} → %{oran:.1f} (≤ %20) · örnek {[(i, round(m, 1)) for i, _, _, m in dog[:10]]}")
    hata += oran > 20
    print("[6] Dış klip")
    dis = sorted(os.path.relpath(os.path.join(r, f), REPO) for r, _, fs in os.walk(os.path.join(REPO, "video/public/kmiras"))
                 for f in fs if f.lower().endswith((".mp4", ".mov", ".webm", ".gif")))
    print(f"  video/public/kmiras video klip: {dis or 0}")
    print("[7] Kanal tekrar desenleri (önceki 2 metne karşı; bilgi, hata saymaz)")
    def sahneler(y):
        return [norm(x) for x in re.findall(r"\| ANLATIM \| GÖRSEL \|\n\|---\|---\|\n\| ([^|]+)\|",
                open(os.path.join(REPO, y), encoding="utf-8").read())]
    g4 = lambda t: {tuple(t.split()[i:i + 4]) for i in range(len(t.split()) - 3)}
    bu_s = sahneler("uretim/2026-11-04-miras-sizintilari/03-metin/metin.md")
    for y in ["uretim/2026-10-26-1929-1000-dolar/03-metin/metin.md", "uretim/2026-10-28-yeni-video/03-metin/metin.md"]:
        o = sahneler(y)
        kap = sorted(" ".join(x) for x in g4(" ".join(bu_s[-3:])) & g4(" ".join(o[-3:])))
        tum = g4(" ".join(bu_s)) & g4(" ".join(o))
        print(f"  {y.split('/')[1][:24]:24s} sahne {len(o)} · kapanış(son 3) ortak 4-gram {len(kap)} {kap[:6]} · tüm metin ortak 4-gram {len(tum)}")
    for k in ["i'm leo", "thanks for playing", "story for another", "game for another", "in the comments", "just one letter",
              "keeps finding", "need more tape", "by the end you'll know", "a b or c", "three possibilities"]:
        print(f"  kalıp {k!r:26s} bu={sum(k in x for x in bu_s)} son_sahne={k in bu_s[-1]}")
    print(f"SONUC hata={hata}")
    return 1 if hata else 0


if __name__ == "__main__":
    sys.exit(main())
