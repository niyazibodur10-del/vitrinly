#!/usr/bin/env python3
"""F8 paket kapı betiği (youtube-paketleyici) — S03 miras sızıntıları. Kaynak: S08 paket-kontrol.py (2026-10-28).
Kip: varsayılan taslak/F8a (F3/F6/F7/F8 girdisi yok → BEKL); `--final` (F8b) → bekleyen = hata.
Ölçer: başlık ≤60 + çıplak $/yıl yok + yasaklı/kalıp/rakip çekirdeği; puan tablosu (ölçüt yargı, betik toplar);
açıklama ilk paragraf ≤150 + anahtar + Cerulli atfı/dönem (D1); "Bank of America says"/çift sayım (D2)/K1 kalıpları;
yasal not + AI + görsel satırı; bölüm kuralları (+ F3 metin §4 ve gerçek sahne bas varsa); etiket ≤500; SRT terim
taraması (varsa); Shorts (+ ilgili_video); pinli yorum tek soru + 1–6 + K1; yayın zamanı EST; JSON ↔ paket.md birebir.
"""
import re, sys, json, pathlib, datetime as dt
BURA = pathlib.Path(__file__).resolve().parent
KLAS = BURA.parent
KOK = BURA.parents[2]
sys.path.insert(0, str(KOK / "tools" / "yayin"))
from yayin_paket import etiket_uzunlugu, yukle_paket, tam_aciklama, SEMA
FINAL = "--final" in sys.argv
hatalar, bekleyen, satir = [], [], []
def ok(m): satir.append("  OK   " + m)
def hata(m): hatalar.append(m); satir.append("  HATA " + m)
def bekle(m):
    if FINAL: hata("(final) " + m)
    else: bekleyen.append(m); satir.append("  BEKL " + m)
def bilgi(m): satir.append("       " + m)
src = (BURA / "paket-uret.py").read_text(encoding="utf-8").split("V = bloklar(")[0]
ns = {"__file__": str(BURA / "paket-uret.py")}; exec(compile(src, "paket-uret.py", "exec"), ns)
bloklar, doldur, YER, YER_KAYNAK = ns["bloklar"], ns["doldur"], ns["YER"], ns["YER_KAYNAK"]
V = bloklar((BURA / "paket.md").read_text(encoding="utf-8"))
F3, F3_KIP = ns["f3"](V); M = {**ns["muzik"](), **F3}

TAVSIYE = [r"\bshould\b", r"\bmust\b", r"\bneed to\b", r"\bbuy\b", r"\bsell\b", r"\binvest\w*", r"\bguarantee\w*",
           r"\brecommend\w*", r"protect your (money|savings|inheritance)", r"set up a trust", r"gift (it )?now", r"avoid (the )?tax\w*",
           r"best way to", r"\byour money\b", r"get rich"]
CLICKBAIT = [r"shock\w*", r"you won'?t believe", r"\binsane\b", r"\bcrazy\b", r"\bexposed\b", r"\bsecret\w*", r"nobody tells you",
             r"\bno one\b", r"\btruth\b", r"\bdestroy\w*", r"100%", r"real reason", r"really happening", r"!", r"get wrong",
             r"\bcrash\w*", r"\bcollapse\w*", r"\bwiped out\b", r"\bsteal\w*", r"\brob\w*", r"\btrap\b"]
KALIP = [r"\bjust (hit|passed|crossed)\b", r"\bnow looks\b", r"genuinely possible",
         r"what happens (when|to) .{0,25}boomer", r"boomers are gone"]  # rakip çekirdekleri (AJ Osborne 953x)
K1 = [r"possibilit\w*", r"three ways", r"scenario (one|two|three|a|b|c)\b", r"\bpossibility [abc]\b", r"\bthree (outcomes|futures|paths)\b"]
SUCLAMA = [r"boomers? (ruin|ruined|stole|greedy|selfish)", r"\bok boomer\b", r"blame"]
BOFA = [r"bank of america (says|estimates|finds)", r"bofa (says|estimates|finds)"]
CIFT = [r"124\D{1,12}54\D{1,12}18", r"\b52 trillion\b", r"\$52\s?t"]  # D2 çıkarması
BUGUN = [r"\btoday\b", r"\btonight\b", r"\bthis week\b", r"\byesterday\b"]
GORSEL = "Visuals are AI-assisted illustrations animated by our team."
AI = "Narration voice is AI-generated."
LEGAL = F3["YASAL_NOT"]
def tara(t, bugun=False):
    t = t.replace(LEGAL, "")
    t = re.sub(r"https?://\S+", "", t)  # URL'ler muaf (investor.genworth.com)
    for k in ("MUZIK_UZUN", "MUZIK_SHORTS1", "MUZIK_SHORTS2"): t = t.replace(M[k], "")  # atıf satırları muaf
    bul = []
    gr = (("tavsiye", TAVSIYE), ("clickbait", CLICKBAIT), ("kalıp", KALIP), ("K1", K1), ("suçlama", SUCLAMA), ("D1", BOFA), ("D2", CIFT))
    for grup, ds in gr + ((("bugün", BUGUN),) if bugun else ()):
        for d in ds: bul += [(grup, x.group(0)) for x in re.finditer(d, t, re.I)]
    return bul
print(f"== paket-kontrol.py S03 ({'F8b --final' if FINAL else 'taslak/F8a'}) ==")

satir.append("[1] Başlıklar (≤60, < > yok, çıplak $ rakam / yıl yok, yasaklı/kalıp/K1 0)")
for g in ("basliklar", "basliklar-elenen"):
    for b in V[g].splitlines():
        bul = tara(b, True); n = len(b)
        cip = re.findall(r"\$\s?\d|\b(1[89]|20)\d\d\b", b)
        if n > 60 or "<" in b or ">" in b: hata(f"{g}: {n} krk / < >: {b}")
        elif g == "basliklar" and cip: hata(f"{g}: çıplak $/yıl (kanal dersi 1): {b}")
        elif g == "basliklar" and bul: hata(f"{g}: yasaklı {bul}: {b}")
        else: ok(f"{n:2d} krk · {b}" + (f"  (elenen; bulgu {bul})" if bul else ""))

W = (.30, .20, .20, .20, .10)
P = {"T1": ("The Great Wealth Transfer Has a Leak", 8, 8, 9, 8, 0),
     "T3": ("Where Will the Boomers' Money Actually Go?", 7, 9, 5, 9, 0),
     "T4": ("The Great Wealth Transfer Is Smaller Than It Sounds", 7, 8, 8, 7, 0),
     "T7": ("The Boomers' Money Is Coming. Just Not When You Think.", 8, 6, 7, 8, 0),
     "T5": ("The Biggest Inheritance Ever, and Why Heirs Might Miss It", 8, 6, 8, 5, 0),
     "T2": ("Your Parents' Money Is Taking the Long Way to You", 7, 4, 6, 8, 0),
     "T6": ("What Happens to Boomer Money Before It Reaches the Kids?", 8, 8, 6, 8, 1.5)}
satir.append("[2] Puan = .30 merak + .20 arama + .20 thumb + .20 politika + .10 mobil (≤45:10 ≤50:9 ≤60:7) − kalıp")
puan = {}
for k, (b, me, ar, th, po, ce) in P.items():
    if b not in V["basliklar"].splitlines() + V["basliklar-elenen"].splitlines(): hata(f"puan başlığı blokta yok: {b}")
    if ce == 0 and tara(b, True): hata(f"{k}: kalıp bulgusu var ama ceza 0")
    mo = 10 if len(b) <= 45 else 9 if len(b) <= 50 else 7
    puan[k] = round(me*W[0] + ar*W[1] + th*W[2] + po*W[3] + mo*W[4] - ce, 2)
sira = sorted(puan, key=lambda x: (-puan[x], x))
for k in sira: bilgi(f"{k} {puan[k]:.2f} · {P[k][0]}")
(ok if P[sira[0]][0] == V["basliklar"].splitlines()[0] else hata)(f"en yüksek {sira[0]} = önerilen başlık")
(ok if {P[k][0] for k in sira[-2:]} == set(V["basliklar-elenen"].splitlines()) else hata)(f"en düşük 2 {sira[-2:]} = elenenler")
(ok if [P[k][0] for k in sira[:5]] == V["basliklar"].splitlines() else hata)("varyant sırası = puan sırası")
(ok if len(P) >= 6 else hata)(f"{len(P)} aday ≥6")

a = V["aciklama"]; ad = doldur(a, M)
satir.append("[3] Açıklama")
p1 = a.split("\n\n")[0]
bilgi(f"ilk paragraf {len(p1)} krk: {p1}")
(ok if len(p1) <= 150 else hata)("ilk paragraf ≤150 krk (kesilmeden okunur)")
for k in ("great wealth transfer", "$124 trillion", "2048", "Cerulli"): (ok if k.lower() in a[:150].lower() else hata)(f"ilk 150 krk: {k}")
(ok if a.lower().find("great wealth transfer") <= 10 else hata)(f"arama ifadesi ilk 10 krk içinde (konum {a.lower().find('great wealth transfer')})")
(ok if V["basliklar"].splitlines()[0].lower() not in p1.lower() else hata)("ilk paragraf başlığı tekrar etmiyor")
(ok if "Not financial advice" in a else hata)('"Not financial advice" var')
(ok if "{YASAL_NOT} " + GORSEL in a and LEGAL.rstrip().endswith(AI) else hata)("yasal not sonu = AI satırı, görsel satırı aynı paragrafta")
(ok if re.search(r"(tax or legal|legal or tax) advice", LEGAL) else hata)("yasal not 'legal/tax advice' vurgusu (P3)")
(ok if re.search(r"illustration|example|fictional", LEGAL, re.I) else hata)("yasal not: kurgusal aile 'illustration' (P2)")
(ok if F3_KIP == "rakam-tablosu" else bekle)(f"yasal not kaynağı: {F3_KIP} (F3 rakam-tablosu.md §'Yasal not (açıklama)' birebir)")
(ok if "{BOLUMLER}" in a else hata)("{BOLUMLER} yer tutucusu (araç Chapters: basar)")
(ok if 0 <= a.find("LEGAL NOTE") < a.find("SOURCES") else hata)("LEGAL NOTE, SOURCES'ın üstünde")
(ok if "cerulli.com/press-releases/cerulli-anticipates-124-trillion" in a else hata)("Cerulli birincil kaynak bağlantısı (D1)")
(ok if YER_KAYNAK not in ad else bekle)("F3 ek kaynakları ({KAYNAK_F3}; D4–D6)")
nb = len(ad.encode()); (ok if nb <= 5000 and "<" not in ad and ">" not in ad else hata)(f"açıklama {nb}/5000 bayt, < > yok")
bul = tara(a); (ok if not bul else hata)(f"açıklama yasaklı/tavsiye/K1/D1/D2: {bul or 0}")
(ok if YER not in ad else bekle)("müzik atfı 06-muzik/atif-satirlari.md'den")

satir.append("[3b] Bölümler")
bol = re.findall(r"^(\d{2}):(\d{2}) (.+)$", V["bolumler"], re.M); sn = [int(x)*60+int(y) for x, y, _ in bol]
(ok if sn and sn[0] == 0 and len(sn) >= 3 and all(b2-b1 >= 10 for b1, b2 in zip(sn, sn[1:])) else hata)(f"{len(sn)} bölüm, 00:00, artan, ≥10 sn")
(ok if not tara(V["bolumler"], True) else hata)(f"bölüm adları yasaklı/K1: {tara(V['bolumler'], True) or 0}")
mtf = KLAS / "03-metin/metin.md"
m4 = re.search(r"## 4\. YouTube bölümleri.*?```\n(.*?)```", mtf.read_text(encoding="utf-8"), re.S) if mtf.is_file() else None
if m4: (ok if [l.split(" ", 1)[1] for l in m4.group(1).splitlines() if l.strip()] == [t for *_, t in bol] else hata)("bölüm adları metin.md §4 birebir")
else: bekle("03-metin/metin.md §4 yok (F3) → bölüm adları taslak")
sz = KLAS / "04-ses/sahne-zamanlari.json"
ACAN = ["S01", "S06", "S08", "S13", "S18", "S21", "S26"]  # metin §2 "## Bölüm n" altındaki ilk sahne
if sz.is_file():
    mtx = mtf.read_text(encoding="utf-8")
    ilk = [re.search(r"### (S\d\d)", b).group(1) for b in re.split(r"^## Bölüm \d", mtx, flags=re.M)[1:]]
    (ok if ilk == ACAN else hata)(f"ACAN = metindeki bölüm açan sahneler {ilk}")
    j = json.loads(sz.read_text()); bas = {x["sahne"]: x["bas"] for x in j["sahneler"]}
    of = 0.0  # kurgu ofseti (koordinatör 2026-11-09: 0); F7 kurgu-rapor.md ≠ 0 ise burada
    for (x, y, t), s_, s in zip(bol, ACAN, sn):
        f = s - (bas[s_] + of); (ok if -1 < f <= 0 else hata)(f"{x}:{y} {t:<28} ↔ {s_} bas {bas[s_]:7.2f} (fark {f:+.2f})")
    import subprocess
    fv = KLAS / "08-kurgu/final-16x9.mp4"
    if fv.is_file():
        sure = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(fv)], capture_output=True, text=True).stdout)
        (ok if abs(sure - j["toplam_sn"]) < 0.1 else hata)(f"final {sure:.3f} sn ↔ anlatım {j['toplam_sn']:.3f} sn → kurgu ofseti 0 (fark {sure - j['toplam_sn']:+.3f})")
        kl = KLAS / "08-kurgu/log/kapi-tur3.txt"
        tik = [float(x) for x in re.findall(r"görsel tık ([\d.]+) sn", kl.read_text(encoding="utf-8"))] if kl.is_file() else []
        a3 = (tik[-1] - 1.3 + 3.5) if tik else bas["S31"]  # AboneOl: kart bas = tık − 1,3 sn, süre 3,5 sn
        ue = max(bas["S31"], a3)
        bilgi(f"uç ekran başı = max(S31 {bas['S31']:.2f}, ABONE-son kart bitişi {a3:.2f}) = {ue:.2f} sn → {sure - ue:.1f} sn")
        (ok if 5 <= sure - ue <= 20 and tik else hata)(f"uç ekran ABONE kartından sonra, 5–20 sn ({len(tik)} abone tıkı okundu)")
    else: bekle("final-16x9.mp4 yok → ofset ve uç ekran F7'de")
else: bekle("gerçek sahne zamanları yok (04-ses/sahne-zamanlari.json, F4) → F8b'de kayar")

satir.append("[4] Etiket + hashtag + SRT terimleri")
et = [t.strip() for t in V["etiketler"].split(",") if t.strip()]
(ok if etiket_uzunlugu(et) <= 500 else hata)(f"etiket {len(et)} adet, {etiket_uzunlugu(et)}/500")
(ok if len(set(et)) == len(et) else hata)("etiket tekrarı yok")
(ok if not tara(V["etiketler"]) else hata)(f"etiket yasaklı: {tara(V['etiketler']) or 0}")
h = V["hashtagler"].split()
(ok if len(h) == 3 and all(re.fullmatch(r"#\w+", x) for x in h) and a.rstrip().endswith(V["hashtagler"]) else hata)(f"3 hashtag, açıklama sonu: {h}")
SRT_TERIM = ["one hundred twenty-four trillion", "inheritance", "boomer", "care", "charity", "spouse", "house", "tax", "Cerulli"]
srt = KLAS / "08-kurgu/final.en.srt"
if srt.is_file():
    st = srt.read_text(encoding="utf-8").lower()
    for t in SRT_TERIM: (ok if t.lower() in st else hata)(f"SRT'de geçiyor: {t} (yoksa etiket/açıklamadan çıkar)")
    bilgi("[T] 'great wealth transfer' SRT'de geçmiyor: Cerulli 124 T$ tahmininin yerleşik adı, videonun S01–S04 konusu (124 + Cerulli SRT'de) → başlık/etiket kalır; politika-raporu §3 vaat↔içerik ✓")
else: bekle("SRT yok → etiket/açıklama terimleri videoda geçiyor mu F8b'de")

satir.append("[5] Shorts")
REF = {"shorts1": ["fifty-four trillion", "forty trillion", "isn't lost", "cerulli"], "shorts2": ["fifteen million", "four hundred ten thousand", "twenty twenty-two", "estate tax"]}
for s in ("shorts1", "shorts2"):
    b, d = V[f"{s}-baslik"], V[f"{s}-aciklama"]
    (ok if len(b) <= 60 and "<" not in b and ">" not in b and b.endswith("?") else hata)(f"{s} başlık {len(b)} krk, soru · {b}")
    bul = tara(b + "\n" + d, True); (ok if not bul else hata)(f"{s} yasaklı: {bul or 0}")
    (ok if AI + " " + GORSEL in d and "Not financial advice" in d else hata)(f"{s} AI + görsel satırı + Not financial advice")
    (ok if V["basliklar"].splitlines()[0] in d and "youtube.com/@toonomy" in d and "http" not in d.replace("https://www.youtube.com/@toonomy", "") else hata)(f"{s} uzun video başlığı + kanal bağlantısı, URL yer tutucusu yok")
    (ok if "Source" in d and d.strip().splitlines()[0].rstrip().endswith("?") else hata)(f"{s} kaynak satırı + ilk paragraf soruyla biter (cevap uzun videoda)")
    sm = re.search(r"### Shorts %s .*?<<(.+?)>>" % s[-1], mtf.read_text(encoding="utf-8"), re.S) if mtf.is_file() else None
    if sm:
        eks = [w for w in REF[s] if w not in sm.group(1).lower()]
        (ok if not eks else hata)(f"{s} açıklama iddiaları Shorts metninde (metin §5 'Okunacak tam metin'): eksik {eks or 0}")
    else: bekle(f"{s}: metin §5 Shorts metni yok")
    hs = d.strip().splitlines()[-1].split(); (ok if len(hs) == 3 and hs[0] == "#Shorts" else hata)(f"{s} hashtag {hs}")
    (ok if len(doldur(d, M).encode()) <= 5000 else hata)(f"{s} açıklama bayt")
(ok if "isn't lost" in V["shorts1-aciklama"] and "delayed" in V["shorts1-aciklama"] else hata)("shorts1: eş payı gecikme, kayıp değil (D2)")
(ok if "as of 2026" in V["shorts2-aciklama"] and "US federal only" in V["shorts2-aciklama"] and "2022" in V["shorts2-aciklama"] else hata)("shorts2: 'as of 2026' + 'US federal only' + 2022 doları (R18/R19, Z2)")
for n in (1, 2):
    w = KLAS / f"08-kurgu/shorts-{n}-whisper.json"
    if not w.is_file(): bekle(f"shorts-{n} transkripti yok → açıklama iddiaları kesitte var mı F8b'de")

satir.append("[6] Pinli yorum")
pin = V["pinli-yorum"]
(ok if pin.count("?") == 1 else hata)(f"tek soru ({pin.count('?')} '?')")
(ok if re.findall(r"^(\d):", pin, re.M) == [str(i) for i in range(1, 7)] else hata)("1–6 numaralı sızıntı listesi")
(ok if not re.search(r"^[ABC]:", pin, re.M) else hata)("A/B/C üçlü yapı yok (K1)")
bul = tara(pin, True) + [("kişisel", w) for w in re.findall(r"\byou (inherit|expect)\w*|your (parents|family)'?s? (money|wealth)", pin, re.I)]
(ok if not bul else hata)(f"nötr (tavsiye/K1/kişisel servet/bugün 0): {bul or 0}")
if mtf.is_file():
    mt = mtf.read_text(encoding="utf-8").lower()
    eks = [x for x in re.findall(r"^\d: (.+)$", pin, re.M) if x.lower() not in mt]
    (ok if not eks else hata)(f"sızıntı adları metinde: eksik {eks or 0}")
else: bekle("sızıntı adları F3 metniyle karşılaştırılacak")

satir.append("[7] Yayın zamanı (EST −05:00, Çar 12:00 / Per + Cmt 09:00 ET; yedek Paz 12:00 / Pzt + Sal)")
Z = dict(l.split("|", 1) for l in V["yayin-zamani"].splitlines())
bek = {"uzun": (2, 12), "shorts-1": (3, 9), "shorts-2": (5, 9), "yedek-uzun": (6, 12), "yedek-shorts-1": (0, 9), "yedek-shorts-2": (1, 9)}
for k, (gun, saat) in bek.items():
    z = dt.datetime.fromisoformat(Z[k])
    (ok if z.weekday() == gun and z.hour == saat and z.utcoffset() == dt.timedelta(hours=-5) else hata)(f"{k}: {Z[k]} = {z.astimezone(dt.timezone.utc):%a %Y-%m-%d %H:%MZ}")
(ok if Z["uzun"] < Z["shorts-1"] < Z["shorts-2"] and Z["yedek-uzun"] < Z["yedek-shorts-1"] < Z["yedek-shorts-2"] else hata)("Shorts uzun videodan sonra")
(ok if Z["uzun"].startswith("2026-11-11T12:00") else hata)("slot = koordinatör 2026-11-09: Çar 2026-11-11 12:00 ET (17:00Z)")

satir.append("[8] JSON ↔ paket.md (yayin_paket.py)")
th = V.get("thumbnail-ana", "").strip()
for ad_, (tur, bas_, ac, zk) in {"yayin-paketi.json": ("uzun", V["basliklar"].splitlines()[0], V["aciklama"], "uzun"),
        "yayin-paketi-shorts-1.json": ("shorts", V["shorts1-baslik"], V["shorts1-aciklama"], "shorts-1"),
        "yayin-paketi-shorts-2.json": ("shorts", V["shorts2-baslik"], V["shorts2-aciklama"], "shorts-2")}.items():
    pk = yukle_paket(BURA / ad_); m_, d_ = pk["metadata"], pk["durum"]; sor = []
    if pk["tur"] != tur: sor.append("tur")
    if m_["baslik"] != bas_: sor.append("başlık")
    if m_["aciklama"] != doldur(ac, M): sor.append("açıklama")
    if d_["yayin_zamani"] != Z[zk]: sor.append("zaman")
    if d_["sentetik_medya"] is not ns["SENTETIK"]: sor.append("sentetik_medya")
    if d_["gizlilik"] != "private": sor.append("gizlilik")
    if pk["onay"]["niyazi_onayi"] is not False: sor.append("onay")
    if tur == "uzun":
        if [f"{b['zaman']} {b['baslik']}" for b in m_["bolumler"]] != V["bolumler"].splitlines(): sor.append("bölümler")
        if m_["etiketler"] != et: sor.append("etiketler")
        if (pk["dosyalar"].get("thumbnail") or "") != th: sor.append("thumbnail ≠ veri:thumbnail-ana")
    else:
        iv = pk.get("ilgili_video") or {}
        if iv.get("baslik") != V["basliklar"].splitlines()[0]: sor.append("ilgili_video ≠ önerilen uzun başlık")
    bil = [k for k in pk if k not in {x.split(".")[0] for x in SEMA} | {"_kok", "_yol", "_not", "ilgili_video"}]
    if bil: sor.append(f"bilinmeyen {bil}")
    ta = tam_aciklama(pk); nb_ = len(ta.encode())
    (ok if not sor and nb_ <= 5000 else hata)(f"{ad_}: başlık {len(m_['baslik'])} krk · tam açıklama {nb_}/5000 bayt · {d_['yayin_zamani']}" + (f" · SORUN {sor}" if sor else ""))
    if tur == "uzun": (ok if "Chapters:\n00:00 " in ta else hata)("tam açıklamada 'Chapters:' + 00:00")
if "ilgili_video" in {x.split(".")[0] for x in SEMA}: ok("SEMA'da ilgili_video alanı")
else:
    y_ = (BURA / "YAYIN.md").read_text(encoding="utf-8") if (BURA / "YAYIN.md").is_file() else ""
    (ok if "Related video" in y_ and "ZORUNLU" in y_ else hata)("ilgili_video araçta yok (talep açık, dry-run UYARI) → YAYIN.md'de ZORUNLU Studio Related video adımı var")
if th: (ok if (BURA / th.replace("../09-paket/", "")).is_file() else hata)(f"thumbnail dosyası var: {th}")
else: bekle("thumbnail finalisti yok (veri:thumbnail-ana boş) → thumbnail-tasarimcisi")
pr = BURA / "politika-raporu.md"
if pr.is_file():
    m_ = re.search(r"sentetik_medya\W{0,6}(true|false)", pr.read_text(encoding="utf-8"), re.I)
    (ok if m_ and (m_.group(1).lower() == "true") == ns["SENTETIK"] else hata)(f"sentetik_medya = politika-raporu.md kararı ({m_.group(1) if m_ else 'karar satırı yok'})")
else: bekle("politika-raporu.md yok (monetizasyon-uyum-uzmani) → sentetik_medya geçici true")
for n in (1, 2):
    sv = KLAS / f"08-kurgu/shorts-{n}.mp4"
    if sv.is_file():
        import subprocess
        d_ = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(sv)], capture_output=True, text=True).stdout)
        (ok if d_ <= 60 else hata)(f"shorts-{n}.mp4 {d_:.2f} sn ≤60 (kanal kuralı)")
for f in ("final-16x9.mp4", "final.en.srt", "shorts-1.mp4", "shorts-2.mp4"):
    if not (KLAS / "08-kurgu" / f).is_file(): bekle(f"08-kurgu/{f} yok (F7)")
print("\n".join(satir))
print(f"SONUÇ: {len(hatalar)} hata · {len(bekleyen)} bekleyen (F8b)")
sys.exit(1 if hatalar else 0)
