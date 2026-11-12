#!/usr/bin/env python3
"""F8a/F8b paket kapı betiği (youtube-paketleyici) — S08 kitchen-table.
Kip: varsayılan F8a (bekleyen = thumbnail/müzik/gerçek zaman yok → BEKLİYOR, hata değil); `--final` (F8b) → bekleyen = hata.
Ölçer: başlık ≤60 + somut özne + yasaklı/kalıp; puan tablosu (ölçüt puanı yargı, betik toplar); açıklama ilk paragraf
≤150 + anahtarlar; 5000 bayt; yasal not (rakam-tablosu §6) birebir + AI/görsel satırı birebir; "Not financial advice";
"$7 for $5" yalnız "Nearly" ile; bölüm kuralları + metin §4 birebir + (varsa) gerçek sahne bas; etiket ≤500 (araç sayımı);
3 hashtag; Shorts; pinli yorum tek A/B/C + nötr; yayın zamanı ofseti EST; JSON ↔ paket.md birebir. Çıkış: hata → 1.
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
def bloklar(s): return {k: v.rstrip("\n") for k, v in re.findall(r"<!-- veri:([\w-]+) -->\s*```[^\n]*\n(.*?)```", s, re.S)}
V = bloklar((BURA / "paket.md").read_text(encoding="utf-8"))
src = (BURA / "paket-uret.py").read_text(encoding="utf-8").split("V = bloklar(")[0]
ns = {"__file__": str(BURA / "paket-uret.py")}; exec(compile(src, "paket-uret.py", "exec"), ns)
M = ns["muzik"](); YER = ns["YER"]; doldur = ns["doldur"]

TAVSIYE = [r"\bshould\b", r"\bmust\b", r"\bneed to\b", r"\bbuy\b", r"\bsell\b", r"\binvest\w*", r"\bguarantee\w*",
           r"\brecommend\w*", r"protect your (money|savings)", r"safest", r"best investment", r"get rich", r"\byour money\b",
           r"buy gold", r"\bgold\b"]
CLICKBAIT = [r"shock\w*", r"you won'?t believe", r"\binsane\b", r"\bcrazy\b", r"\bexposed\b", r"\bsecret\w*", r"nobody tells you",
             r"\btruth\b", r"\bdestroy\w*", r"risk[- ]free", r"100%", r"real reason", r"really happening", r"!",
             r"\bdefault\w*", r"\bcrash\w*", r"\bcollapse\w*", r"\bspiral\b", r"\bbankrupt\w*", r"credit card", r"first time ever"]
KALIP = [r"\bjust (hit|passed|crossed)\b", r"\bnow looks\b", r"genuinely possible"]  # WhiteBoard Finance / How Money Works kalıpları
SIYASI = [r"\b(trump|biden|harris|vance|democrat\w*|republican\w*|gop|congress\w*|election\w*|vot\w+|party)\b"]
BUGUN = [r"\btoday\b", r"\btonight\b", r"\bthis week\b", r"\byesterday\b"]
rt = (KLAS / "03-metin/rakam-tablosu.md").read_text(encoding="utf-8")
LEGAL = re.search(r"\*\*Yasal not \(açıklama\):\*\* \"(.+?)\"", rt).group(1)
AI = "Narration voice is AI-generated."
GORSEL = "Visuals are AI-assisted illustrations animated by our team."
def tara(t, bugun=False):
    t = t.replace(LEGAL, "")
    for v in M.values(): t = t.replace(v, "")  # üçüncü taraf eser adları aynen: muaf
    bul = []
    for grup, ds in (("tavsiye", TAVSIYE), ("clickbait", CLICKBAIT), ("kalıp", KALIP), ("siyasi", SIYASI)) + ((("bugün", BUGUN),) if bugun else ()):
        for d in ds: bul += [(grup, x.group(0)) for x in re.finditer(d, t, re.I)]
    if re.search(r"\$7 for every \$5", t, re.I) and not re.search(r"nearly \$7 for every \$5", t, re.I): bul.append(("R04", "$7/$5 'Nearly' yok"))
    return bul
print(f"== paket-kontrol.py ({'F8b --final' if FINAL else 'F8a'}) ==")

satir.append("[1] Başlıklar (≤60, < > yok, somut özne America/US, yasaklı/kalıp 0)")
for g in ("basliklar", "basliklar-elenen"):
    for b in V[g].splitlines():
        bul = tara(b, True); n = len(b)
        if n > 60 or "<" in b or ">" in b: hata(f"{g}: {n} krk / < >: {b}")
        elif g == "basliklar" and not re.search(r"\b(America|US)\b", b): hata(f"{g}: somut özne yok: {b}")
        elif g == "basliklar" and bul: hata(f"{g}: yasaklı {bul}: {b}")
        else: ok(f"{n:2d} krk · {b}" + (f"  (elenen; bulgu {bul})" if bul else ""))

W = (.30, .20, .20, .20, .10)
P = {"T1": ("If America Earned $5,400 a Month, Here's Its Budget", 9, 6, 9, 9, 0),
     "T4": ("America's Budget, Shrunk to One Kitchen Table", 7, 8, 8, 9, 0),
     "T3": ("America Pays More in Interest Than for Its Military", 8, 7, 7, 8, 0),
     "T2": ("The US Spends Nearly $7 for Every $5 It Earns. Then What?", 8, 6, 7, 8, 0),
     "T7": ("America's Interest Bill Tripled in Five Years. Why?", 7, 7, 6, 8, 0),
     "T5": ("A Country Isn't a Family. Its Interest Bill Is.", 6, 4, 6, 9, 0),
     "T6": ("US Interest Payments Just Passed the Military", 8, 7, 6, 4, 1.5)}
satir.append("[2] Puan = .30 merak + .20 arama + .20 thumb + .20 politika + .10 mobil (≤45:10 ≤50:9 ≤60:7) − kalıp")
puan = {}
for k, (b, me, ar, th, po, ce) in P.items():
    if b not in V["basliklar"].splitlines() + V["basliklar-elenen"].splitlines(): hata(f"puan başlığı blokta yok: {b}")
    mo = 10 if len(b) <= 45 else 9 if len(b) <= 50 else 7
    puan[k] = round(me*W[0] + ar*W[1] + th*W[2] + po*W[3] + mo*W[4] - ce, 2)
sira = sorted(puan, key=lambda x: (-puan[x], x))
for k in sira: bilgi(f"{k} {puan[k]:.2f} · {P[k][0]}")
(ok if P[sira[0]][0] == V["basliklar"].splitlines()[0] else hata)(f"en yüksek {sira[0]} = önerilen başlık")
(ok if {P[k][0] for k in sira[-2:]} == set(V["basliklar-elenen"].splitlines()) else hata)(f"en düşük 2 {sira[-2:]} = elenenler")
(ok if [P[k][0] for k in sira[:5]] == V["basliklar"].splitlines() else hata)("varyant sırası = puan sırası")

a = V["aciklama"]; ad = doldur(a, M)
satir.append("[3] Açıklama")
p1 = a.split("\n\n")[0]
bilgi(f"ilk paragraf {len(p1)} krk: {p1}")
(ok if len(p1) <= 150 else hata)("ilk paragraf ≤150 krk (kesilmeden okunur)")
for k in ("US federal budget", "deficit", "$5,400"): (ok if k.lower() in a[:150].lower() else hata)(f"ilk 150 krk: {k}")
(ok if a.lower().find("us federal budget") <= 10 else hata)(f"arama ifadesi ilk 10 krk içinde (konum {a.lower().find('us federal budget')})")
(ok if "Not financial advice" in a else hata)('"Not financial advice" var')
(ok if LEGAL in a else hata)("yasal not rakam-tablosu §6 birebir")
(ok if LEGAL + " " + GORSEL in a else hata)("AI satırı (yasal notun sonu) + görsel satırı aynı paragrafta birebir")
(ok if "$1 a month here = $1 billion a year" in a else hata)("ölçek notu var")
(ok if "{BOLUMLER}" in a else hata)("{BOLUMLER} yer tutucusu (araç Chapters: basar)")
(ok if 0 <= a.find("LEGAL NOTE") < a.find("SOURCES") else hata)("LEGAL NOTE, SOURCES'ın üstünde")
kay = [l for l in a.split("SOURCES")[1].split("\n\n")[0].splitlines() if l.startswith("•")]
(ok if len(kay) >= 8 and all("http" in l for l in kay) else hata)(f"kaynak satırı {len(kay)}, hepsi bağlantılı (MTS, DttP, ort. faiz, OMB, FRED×3, Shiller)")
nb = len(ad.encode()); (ok if nb <= 5000 and "<" not in ad and ">" not in ad else hata)(f"açıklama {nb}/5000 bayt, < > yok")
bul = tara(a); (ok if not bul else hata)(f"açıklama yasaklı/tavsiye/siyasi: {bul or 0}")
(ok if YER not in ad else bekle)("müzik atfı 06-muzik/atif-satirlari.md'den (yoksa yer tutucu)")

satir.append("[3b] Bölümler")
bol = re.findall(r"^(\d{2}):(\d{2}) (.+)$", V["bolumler"], re.M); sn = [int(x)*60+int(y) for x, y, _ in bol]
(ok if sn and sn[0] == 0 and len(sn) >= 3 and all(b2-b1 >= 10 for b1, b2 in zip(sn, sn[1:])) else hata)(f"{len(sn)} bölüm, 00:00, artan, ≥10 sn")
mt = (KLAS / "03-metin/metin.md").read_text(encoding="utf-8")
m4 = re.search(r"## 4\. YouTube bölümleri.*?```\n(.*?)```", mt, re.S).group(1)
(ok if [l.split(" ", 1)[1] for l in m4.splitlines() if l.strip()] == [t for *_, t in bol] else hata)("bölüm adları metin.md §4 birebir")
ACAN = ["S01", "S05", "S08", "S12", "S16", "S21", "S26"]
sz = KLAS / "04-ses/sahne-zamanlari.json"
if sz.is_file():
    j = json.loads(sz.read_text()); bas = {x["sahne"]: x["bas"] for x in j["sahneler"]}
    for (x, y, t), s_, s in zip(bol, ACAN, sn):
        f = s - bas[s_]; (ok if -1 < f <= 0 else hata)(f"{x}:{y} {t:<34} ↔ {s_} bas {bas[s_]:7.2f} (fark {f:+.2f})")
else:
    mz = {x: (int(a_)*60+int(b_)) for x, a_, b_ in re.findall(r"### (S\d\d) · (\d+):(\d\d)–", mt)}
    (ok if [mz[s] for s in ACAN] == sn else hata)("bölümler metin §2 sahne başlangıçlarıyla aynı (betik zamanı)")
    bekle("gerçek sahne zamanları yok (04-ses/sahne-zamanlari.json) → F8b'de kayar")

satir.append("[4] Etiket + hashtag")
et = [t.strip() for t in V["etiketler"].split(",") if t.strip()]
(ok if etiket_uzunlugu(et) <= 500 else hata)(f"etiket {len(et)} adet, {etiket_uzunlugu(et)}/500")
(ok if not tara(V["etiketler"]) else hata)(f"etiket yasaklı: {tara(V['etiketler']) or 0}")
h = V["hashtagler"].split()
(ok if len(h) == 3 and all(re.fullmatch(r"#\w+", x) for x in h) and a.rstrip().endswith(V["hashtagler"]) else hata)(f"3 hashtag, açıklama sonu: {h}")

satir.append("[5] Shorts")
for s in ("shorts1", "shorts2"):
    b, d = V[f"{s}-baslik"], V[f"{s}-aciklama"]
    (ok if len(b) <= 60 and "<" not in b and ">" not in b else hata)(f"{s} başlık {len(b)} krk · {b}")
    bul = tara(b + "\n" + d, True); (ok if not bul else hata)(f"{s} yasaklı: {bul or 0}")
    (ok if AI + " " + GORSEL in d and "Not financial advice" in d else hata)(f"{s} AI + görsel satırı + Not financial advice")
    (ok if V["basliklar"].splitlines()[0] in d and "youtube.com/@toonomy" in d and "http" not in d.replace("https://www.youtube.com/@toonomy", "") else hata)(f"{s} uzun video başlığı + kanal bağlantısı, URL yer tutucusu yok")
    hs = d.strip().splitlines()[-1].split(); (ok if len(hs) == 3 and hs[0] == "#Shorts" else hata)(f"{s} hashtag {hs}")
    (ok if YER not in doldur(d, M) else bekle)(f"{s} müzik atfı")
(ok if "1946" in V["shorts2-baslik"] and "1974" in V["shorts2-aciklama"] and "even though the debt itself grew" in V["shorts2-aciklama"] else hata)("shorts2: oran küçüldü, borç büyüdü (R33/R34) ifadesi")

satir.append("[6] Pinli yorum")
pin = V["pinli-yorum"]
(ok if pin.count("?") == 1 else hata)(f"tek soru ({pin.count('?')} '?')")
(ok if re.findall(r"^([ABC]):", pin, re.M) == ["A", "B", "C"] else hata)("A/B/C seçenekleri")
bul = tara(pin, True) + [("siyasi", w) for w in re.findall(r"\b(tax\w*|cut\w*|blame)\b", pin, re.I)]
(ok if not bul else hata)(f"nötr (tavsiye/siyasi/vergi-kesinti/bugün 0): {bul or 0}")

satir.append("[7] Yayın zamanı (EST −05:00, Çar 12:00 / Per + Cmt 09:00 ET)")
Z = dict(l.split("|", 1) for l in V["yayin-zamani"].splitlines())
bek = {"uzun": (2, 12), "shorts-1": (3, 9), "shorts-2": (5, 9), "yedek-uzun": (6, 12), "yedek-shorts-1": (0, 9), "yedek-shorts-2": (1, 9)}
for k, (gun, saat) in bek.items():
    z = dt.datetime.fromisoformat(Z[k])
    (ok if z.weekday() == gun and z.hour == saat and z.utcoffset() == dt.timedelta(hours=-5) else hata)(f"{k}: {Z[k]} = {z.astimezone(dt.timezone.utc):%a %Y-%m-%d %H:%MZ}")
(ok if Z["uzun"] < Z["shorts-1"] < Z["shorts-2"] else hata)("Shorts uzun videodan sonra")

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
    if d_["sentetik_medya"] is not True: sor.append("sentetik_medya")
    if pk["onay"]["niyazi_onayi"] is not False: sor.append("onay")
    if tur == "uzun":
        if [f"{b['zaman']} {b['baslik']}" for b in m_["bolumler"]] != V["bolumler"].splitlines(): sor.append("bölümler")
        if m_["etiketler"] != et: sor.append("etiketler")
        if (pk["dosyalar"].get("thumbnail") or "") != th: sor.append("thumbnail ≠ veri:thumbnail-ana")
    bil = [k for k in pk if k not in {x.split(".")[0] for x in SEMA} | {"_kok", "_yol", "_not"}]
    if bil: sor.append(f"bilinmeyen {bil}")
    ta = tam_aciklama(pk); nb_ = len(ta.encode())
    (ok if not sor and nb_ <= 5000 else hata)(f"{ad_}: başlık {len(m_['baslik'])} krk · tam açıklama {nb_}/5000 bayt · {d_['yayin_zamani']}" + (f" · SORUN {sor}" if sor else ""))
    if tur == "uzun": (ok if "Chapters:\n00:00 " in ta else hata)("tam açıklamada 'Chapters:' + 00:00")
if th: (ok if (BURA / th.replace("../09-paket/", "")).is_file() else hata)(f"thumbnail dosyası var: {th}")
else: bekle("thumbnail finalisti yok (veri:thumbnail-ana boş) → thumbnail-tasarimcisi raporundan")
pr = BURA / "politika-raporu.md"
if pr.is_file():
    m_ = re.search(r"sentetik_medya\W{0,6}(true|false)", pr.read_text(encoding="utf-8"), re.I)
    (ok if m_ and (m_.group(1).lower() == "true") == ns.get("SENTETIK", True) else hata)(f"sentetik_medya = politika-raporu.md kararı ({m_.group(1) if m_ else 'karar satırı yok'})")
else: bekle("politika-raporu.md yok (monetizasyon-uyum-uzmani) → sentetik_medya geçici true")
for f in ("final-16x9.mp4", "final.en.srt", "shorts-1.mp4", "shorts-2.mp4"):
    if not (KLAS / "08-kurgu" / f).is_file(): bekle(f"08-kurgu/{f} yok (F7)")
print("\n".join(satir))
print(f"SONUÇ: {len(hatalar)} hata · {len(bekleyen)} bekleyen (F8b)")
sys.exit(1 if hatalar else 0)
