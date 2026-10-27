#!/usr/bin/env python3
"""F4/F8 paket taslağı kapı betiği (youtube-paketleyici).

Okur: paket-taslak.md ve thumb-konsept.md içindeki `<!-- veri:ANAHTAR -->` + kod bloğu.
Ölçer: başlık ≤60, 1929 yıl sınırı, açıklama ilk 150 krk anahtar kelime, bayt sınırı,
yasal not birebir (03-metin/dogrulama.md §4), AI satırı, "Not financial advice", bölüm kuralları,
kaynak sayısı, etiket uzunluğu (tools/yayin/yayin_paket.py etiket_uzunlugu ile), 3 hashtag,
yasaklı/clickbait/tavsiye taraması, thumbnail metni ≤4 kelime ve 168x94 okunurluk modeli,
başlık puan tablosu (ölçüt puanları yargıdır, betik yalnız toplar).
Çıkış kodu: hata varsa 1.
"""
import re, sys, pathlib

BURA = pathlib.Path(__file__).resolve().parent
KOK = BURA.parents[2]
sys.path.insert(0, str(KOK / "tools" / "yayin"))
from yayin_paket import etiket_uzunlugu  # yükleme aracıyla aynı sayım

hatalar, satirlar = [], []
def ok(m): satirlar.append("  OK   " + m)
def hata(m): hatalar.append(m); satirlar.append("  HATA " + m)
def bilgi(m): satirlar.append("       " + m)

def bloklar(yol):
    s = yol.read_text(encoding="utf-8")
    return {k: v.rstrip("\n") for k, v in re.findall(r"<!-- veri:([\w-]+) -->\s*```[^\n]*\n(.*?)```", s, re.S)}

V = bloklar(BURA / "paket-taslak.md")
V.update(bloklar(BURA / "thumb-konsept.md"))

# --- yasaklı / clickbait / tavsiye desenleri ---
TAVSIYE = [r"\bshould\b", r"\bmust\b", r"\bneed to\b", r"\bbuy\b", r"\bsell\b", r"\binvest\w*", r"\bguarantee\w*",
           r"\brecommend\w*", r"keep your (cash|money)", r"cash is trash", r"where to (put|keep|park) (your )?money",
           r"which door wins today", r"banks? (are|is) safe (now|today)", r"protect your (money|savings)",
           r"safest place", r"best investment", r"get rich", r"\byou should\b", r"\bmove your (cash|money)"]
CLICKBAIT = [r"shock\w*", r"you won'?t believe", r"\binsane\b", r"\bcrazy\b", r"\bexposed\b", r"\bsecret\w*",
             r"nobody tells you", r"\btruth\b", r"gone wrong", r"\bdestroy\w*", r"risk[- ]free", r"100%",
             r"real reason", r"true origin", r"get wrong", r"what historians", r"welcome to", r"!{1,}"]
BUGUN = [r"\btoday\b", r"\b2026\b", r"\bnow\b"]  # uzun video başlığı + thumbnail için

LEGAL_SATIR = None
dog = (KOK / "uretim/2026-10-26-1929-1000-dolar/03-metin/dogrulama.md").read_text(encoding="utf-8")
m = re.search(r"Açıklama için yasal not.*?\n> (.+)", dog)
LEGAL_SATIR = m.group(1).strip() if m else None

def tara(ad, metin, bugun=False):
    t = metin
    if LEGAL_SATIR: t = t.replace(LEGAL_SATIR, "")  # yasal not "buy, sell" içerir: muaf
    bul = []
    for d in TAVSIYE: bul += [("tavsiye", x.group(0)) for x in re.finditer(d, t, re.I)]
    for d in CLICKBAIT: bul += [("clickbait", x.group(0)) for x in re.finditer(d, t, re.I)]
    if bugun:
        for d in BUGUN: bul += [("bugüne-dönük", x.group(0)) for x in re.finditer(d, t, re.I)]
    return bul

def kelime(s): return len([w for w in s.split() if re.search(r"\w", w)])

print("== paket-kontrol.py ==")
# 1) başlıklar
satirlar.append("[1] Başlıklar (≤60 krk, 1929, yasaklı 0, bugüne dönük 0)")
for grup in ("basliklar", "basliklar-elenen"):
    for b in V[grup].splitlines():
        n = len(b); bul = tara(b, b, bugun=True)
        if n > 60: hata(f"{grup}: {n} krk > 60: {b}")
        elif "1929" not in b: hata(f"{grup}: 1929 yok: {b}")
        elif "<" in b or ">" in b: hata(f"{grup}: < > var: {b}")
        elif bul and grup == "basliklar": hata(f"{grup}: yasaklı {bul}: {b}")
        else: ok(f"{n:2d} krk · {b}" + (f"  (elenen; bulgu {bul})" if bul else ""))

# 2) başlık puan tablosu (ölçüt puanları yargı [T]; ağırlıklar sabit)
W = {"merak": .30, "arama": .20, "thumb": .20, "politika": .20, "mobil": .10}
P = {  # merak (somut özne tavanı: özne yoksa ≤6), arama, thumbnail ile okunuş, politika/doğruluk
 "T1": ("You Have $1,000 in 1929. Can You Keep It?",           9, 6, 9, 9),
 "T2": ("Stocks, a Bank or a Shoebox: Who Survived 1929?",     8, 7, 7, 9),
 "T3": ("Stocks, a Bank or a Shoebox: $1,000 Through 1929",    7, 7, 7, 9),
 "T4": ("Surviving the 1929 Crash With $1,000: Three Doors",   6, 9, 7, 9),
 "T7": ("$1,000 in 1929: The Door Everyone Laughed At Won",    6, 6, 8, 8),
 "T5": ("1929: The Smartest Door Was the Worst One",           6, 5, 6, 9),
 "T6": ("The Shoebox That Beat the Stock Market in 1929",      7, 8, 6, 3),
}
satirlar.append("[2] Başlık puanı = .30 merak + .20 arama + .20 thumb + .20 politika + .10 mobil (mobil: ≤45 krk 10, ≤50 9, ≤60 7)")
puan = {}
for k, (b, me, ar, th, po) in P.items():
    if b not in V["basliklar"].splitlines() + V["basliklar-elenen"].splitlines(): hata(f"puan tablosu başlığı blokta yok: {b}")
    mo = 10 if len(b) <= 45 else 9 if len(b) <= 50 else 7
    puan[k] = round(me*W["merak"] + ar*W["arama"] + th*W["thumb"] + po*W["politika"] + mo*W["mobil"], 2)
for k in sorted(puan, key=lambda x: (-puan[x], x)):
    bilgi(f"{k} {puan[k]:.2f} · {P[k][0]}")
sira = sorted(puan, key=lambda x: (-puan[x], x))
if sira[0] == "T1": ok("en yüksek puan T1 (önerilen başlıkla tutarlı)")
else: hata(f"en yüksek puan {sira[0]}, önerilen T1 değil")
if set(sira[-2:]) == {"T5", "T6"}: ok("en düşük 2 = T5, T6 (elenenlerle tutarlı)")
else: hata(f"en düşük 2 {sira[-2:]} ≠ elenenler")

# 3) açıklama
a = V["aciklama"]
satirlar.append("[3] Açıklama")
ilk150 = a[:150]
ilk2 = "\n".join(a.split("\n\n")[0].splitlines()[:2])
bilgi(f"ilk paragraf {len(a.split(chr(10)*2)[0])} krk")
for anahtar in ("1929 stock market crash", "Great Depression", "$1,000"):
    (ok if anahtar.lower() in ilk150.lower() else hata)(f"ilk 150 krk içinde: {anahtar}")
if len(a.split("\n\n")[0]) <= 150: ok("ilk paragraf ≤150 krk (kesilmeden okunur)")
else: hata("ilk paragraf >150 krk")
nb = len(a.encode("utf-8"))
(ok if nb <= 5000 else hata)(f"açıklama {nb}/5000 bayt")
(ok if "<" not in a and ">" not in a else hata)("açıklamada < > yok")
(ok if "Not financial advice" in a else hata)('"Not financial advice" var')
AI = "Narration voice is AI-generated. Visuals are AI-assisted illustrations animated by our team."
(ok if AI in a else hata)("AI satırı birebir var")
(ok if LEGAL_SATIR and LEGAL_SATIR in a else hata)("yasal not (dogrulama.md §4) birebir var")
# bölümler
bol = re.findall(r"^(\d{1,2}):(\d{2}) (.+)$", a, re.M)
sn = [int(x)*60+int(y) for x, y, _ in bol]
kural = sn and sn[0] == 0 and len(sn) >= 3 and all(b2-b1 >= 10 for b1, b2 in zip(sn, sn[1:]))
(ok if kural else hata)(f"bölümler {len(sn)} adet, 0:00 ile başlıyor, artan, her biri ≥10 sn")
metin = (KOK / "uretim/2026-10-26-1929-1000-dolar/03-metin/metin.md").read_text(encoding="utf-8")
m4 = re.search(r"## 4\. YouTube bölümleri.*?```\n(.*?)```", metin, re.S)
(ok if m4 and [l for l in m4.group(1).splitlines() if l.strip()] == [f"{x}:{y} {t}" for x, y, t in bol] else hata)("bölümler metin.md §4 ile birebir (zamanlar F8'de gerçek sesle güncellenir)")
kay = [l for l in a.split("SOURCES")[1].split("\n\n")[0].splitlines() if l.startswith("•")]
(ok if len(kay) >= 10 else hata)(f"kaynak satırı {len(kay)} (9 + Hulbert = 10 beklenir)")
(ok if "Hulbert" in a else hata)("Hulbert kaynağı var")
bilgi("yer tutucu: " + ", ".join(sorted(set(re.findall(r"\[YER TUTUCU: ([^\]]{0,40})", a)))))
bul = tara("aciklama", a)
(ok if not bul else hata)(f"açıklama yasaklı/clickbait/tavsiye: {bul or 0}")

# 4) etiketler + hashtag
satirlar.append("[4] Etiketler ve hashtag'ler")
et = [t.strip() for t in V["etiketler"].split(",") if t.strip()]
n = etiket_uzunlugu(et)
(ok if n <= 500 else hata)(f"etiketler {len(et)} adet, {n}/500 (YouTube sayımı)")
(ok if not tara("etiket", V["etiketler"]) else hata)(f"etiket yasaklı: {tara('etiket', V['etiketler']) or 0}")
for ad in ("hashtagler",):
    h = V[ad].split()
    (ok if len(h) == 3 and all(re.fullmatch(r"#\w+", x) for x in h) else hata)(f"{ad}: {h}")
    (ok if a.rstrip().endswith(V[ad]) else hata)("açıklama aynı 3 hashtag ile bitiyor")

# 5) Shorts
satirlar.append("[5] Shorts")
for s in ("shorts1", "shorts2"):
    b = V[f"{s}-baslik"]; d = V[f"{s}-aciklama"]
    (ok if len(b) <= 60 else hata)(f"{s} başlık {len(b)} krk · {b}")
    bul = tara(s, b + "\n" + d)
    (ok if not bul else hata)(f"{s} yasaklı/clickbait/tavsiye: {bul or 0}")
    (ok if AI in d and "Not financial advice" in d else hata)(f"{s} AI satırı + Not financial advice")
    (ok if "uzun video bağlantısı" in d else hata)(f"{s} uzun videoya bağlantı yeri var (+ Studio related video adımı)")
    h = d.strip().splitlines()[-1].split()
    (ok if len(h) == 3 and h[0] == "#Shorts" else hata)(f"{s} hashtag: {h}")
(ok if "2026" not in V["shorts1-baslik"] else hata)("shorts1 başlığında bugün yok")

# 6) pinli yorum
satirlar.append("[6] Pinli yorum")
pin = V["pinli-yorum"]
(ok if "?" in pin else hata)("soru soruyor")
bul = tara("pin", pin, bugun=True)
(ok if not bul else hata)(f"tavsiye/clickbait/bugüne dönük: {bul or 0}")

# 7) thumbnail metni + okunurluk modeli
satirlar.append("[7] Thumbnail metni (≤4 kelime) + 168x94 okunurluk modeli (eşik ≥9 px büyük harf)")
BOX_W, BOX_H, MAXL, LH, CW = 704, 324, 3, 1.15, 0.55
OLCEK = 168 / 1280
def okunurluk(t):
    w = t.split(); en = 0; best = None
    for L in range(1, min(MAXL, len(w)) + 1):
        # dengeli bölme: en uzun satırı en kısa yapan bölüm (kaba arama)
        import itertools
        en_iyi = None
        for kes in itertools.combinations(range(1, len(w)), L - 1):
            parcalar = [" ".join(w[i:j]) for i, j in zip((0,) + kes, kes + (len(w),))]
            uz = max(len(p) for p in parcalar)
            if en_iyi is None or uz < en_iyi: en_iyi = uz
        cap = min(BOX_H / (L * LH), BOX_W / (en_iyi * CW))
        if cap > en: en, best = cap, L
    return en, en * OLCEK, best
def thumb(blok, kapi):
    for l in V[blok].splitlines():
        p = l.split("|"); ad, t = p[0], p[1]; ek = p[2:] if len(p) > 2 else []
        k = kelime(t) + sum(kelime(x) for x in ek)
        cap, mob, L = okunurluk(t)
        bul = tara(ad, t, bugun=True)
        durum = f"{ad}: \"{t}\"" + (f" + damga {ek}" if ek else "") + f" · {k} kelime · {L} satır · büyük harf {cap:.0f} px → 168x94'te {mob:.1f} px"
        if not kapi: bilgi(durum + (f" · bulgu {bul}" if bul else "")); continue
        if k > 4: hata(durum + " · >4 kelime")
        elif mob < 9: hata(durum + " · okunurluk eşiği altı")
        elif bul: hata(durum + f" · yasaklı {bul}")
        else: ok(durum)
thumb("thumb-metin-secilen", True)
bilgi("alternatifler ve rakip karşılaştırması (kapı değil, bilgi):")
thumb("thumb-metin-alternatif", False)

print("\n".join(satirlar))
print(f"SONUÇ: {len(hatalar)} hata")
sys.exit(1 if hatalar else 0)
