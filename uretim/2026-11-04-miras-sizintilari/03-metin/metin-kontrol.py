#!/usr/bin/env python3
"""F3 Metin + Retention kapısı — v4, S03 miras sızıntıları (2026-11-04). v3 (uretim/2026-10-28-yeni-video/03-metin/) uyarlaması:
2080–2400 kelime (13–15 dk), K1 üç-olasılık kalıp yasağı, olgu-kaynak etiketi kontrolü, D2 çift sayım kalıpları, rakam-tablosu yoksa [R?] sayımı.
Kullanım: python3 -I metin-kontrol.py metin.md [--yaz]   (--yaz: sahne başlık zamanlarını betik ölçümüyle günceller)
Ölçüm: ANLATIM sütunu, kelime = boşlukla ayrılmış birim, 160 kpm (am_fenrir 0.9 uzun metin ölçümü).
Kapılar: 1750–2100 kelime (≥10 dk); ilk 15 sn somut özne + vaat; ilk 30 sn intro yok; ↺ aralığı ≤90 sn (hedef ≤75, uyarı);
ABONE 3–4 satır, çapası metinde, ≥60 sn, DORUK sahnesinde değil; sesli abone kalıbı ilk 60 sn'de yok; telaffuz yasak 0; tavsiye 0;
H7 zaman sözcüğü 0; rakam-tablosu yasakları (credit card, first time, 7 for every 5, toplam borç) 0; tez ≤60 sn ve son 90 sn;
bölümler; Shorts ≤60 sn; ANLATIM+Shorts sayıları rakam-tablosu.md / veri/olcek-cikti.txt ile ±tolerans; 1929 metniyle 5-gram ≤%10.
"""
import re, sys, os

KPM = 160.0
ALT, UST = 2080, 2400
YASAK = re.compile(r"\b(charts?|complicated|scenarios?|truth|crash(es|ed|ing)?|bold)\b", re.I)
TAVSIYE = [r"\byou should\b", r"\bi recommend\b", r"\bbuy now\b", r"\bsell now\b", r"\bguaranteed?\b", r"\binvest in\b",
           r"\bfinancial advi[cs]", r"\badvis[oe]r\b", r"\bexpert\b", r"\bdon'?t invest\b", r"\bbest investment\b", r"\btip\b",
           r"\byou need to\b", r"\bput your money\b", r"\bprotect (your|yourself)\b", r"\byour money\b", r"\bbuy gold\b",
           r"\bgold\b", r"\bmy advice\b", r"\bwe recommend\b", r"\bset up a trust\b", r"\bgift (it|them) now\b", r"\bestate plan", r"\bshould you\b"]
H7 = re.compile(r"\b(today|tonight|this week|this month|this year|yesterday|tomorrow|right now|just (ended|announced|released))\b", re.I)
TABLO_YASAK = re.compile(r"\b(bank of america (says|estimates)|fifty-two trillion|biggest handover|death tax|minus fifty-four|minus eighteen trillion|lost fifty-four)\b", re.I)
K1 = re.compile(r"\b(possibility (a|b|c|one|two|three)|three (ways|possibilities|paths|roads) |scenario (one|two|three|a|b|c)|option (a|b|c)|three ways this could go)\b", re.I)
PARTI = re.compile(r"\b(democrat\w*|republican\w*|gop|trump|biden|harris|vance|congress(wo)?man|senator|president)\b", re.I)
INTRO = re.compile(r"\b(hi guys|hey guys|welcome (back )?to|toonomy|channel|subscribe|like button)\b", re.I)
ABONE_SOZ = re.compile(r"\bsubscri\w*|\blike button\b|\bbell\b", re.I)
TEZ = "an inheritance isn't a number. it's whatever is left at the end of a long road"
TEZ2 = "it's whatever is left at the end of a long road"
HOOK = "One hundred twenty-four trillion dollars is expected to pass down"
ONCEKI = ["../../2026-10-26-1929-1000-dolar/03-metin/metin.md", "../../2026-10-28-yeni-video/03-metin/metin.md"]

def mmss(s):
    s = int(round(s)); return f"{s//60}:{s%60:02d}"

# --- sayı kelimesi ayrıştırıcı ---
BIR = {w: i for i, w in enumerate("zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split())}
ONLAR = {w: (i + 2) * 10 for i, w in enumerate("twenty thirty forty fifty sixty seventy eighty ninety".split())}
OLCEK = {"thousand": 1e3, "million": 1e6, "billion": 1e9, "trillion": 1e12}
YAKLASIK = ("about", "nearly", "roughly", "almost", "close to", "more than", "under", "around")

def sayilar(metin):
    w = re.findall(r"[a-z]+(?:'[a-z]+)?|[.,:;!?]", metin.lower().replace("-", " "))
    out, i = [], 0
    while i < len(w):
        if w[i] in BIR or w[i] in ONLAR:
            j = i; seq = []
            while j < len(w) and (w[j] in BIR or w[j] in ONLAR or w[j] in OLCEK or w[j] == "hundred" or w[j] == "point"
                                  or (w[j] == "and" and j + 1 < len(w) and (w[j+1] in BIR or w[j+1] in ONLAR or w[j+1] == "a"))):
                if w[j] == "and" and w[j+1] == "a" and j + 2 < len(w) and w[j+2] == "half":
                    seq += ["and", "a", "half"]; j += 3; break
                seq.append(w[j]); j += 1
            seq = [s for s in seq]
            once = " ".join(w[max(0, i-2):i]); sonra = w[j] if j < len(w) else ""
            yil = (len(seq) >= 2 and "hundred" not in seq and not any(s in OLCEK for s in seq) and "point" not in seq and "and" not in seq
                   and (13 <= BIR.get(seq[0], 0) <= 19 or seq[0] == "twenty") and (seq[1] in ONLAR or 10 <= BIR.get(seq[1], 0) <= 19))
            if yil:
                bas = BIR.get(seq[0], 20); son = sum(BIR.get(s, ONLAR.get(s, 0)) for s in seq[1:]); out.append(("yil", bas * 100 + son, once, sonra))
            else:
                tot = cur = 0.0; dec = None; half = False
                for s in seq:
                    if s == "point": dec = ""; continue
                    if s == "half": half = True; continue
                    if s in ("and", "a"): continue
                    if dec is not None: dec += str(BIR.get(s, 0)); continue
                    if s in BIR: cur += BIR[s]
                    elif s in ONLAR: cur += ONLAR[s]
                    elif s == "hundred": cur *= 100
                    elif s in OLCEK: tot += cur * OLCEK[s]; cur = 0
                v = tot + cur
                if dec: 
                    # ondalık, son ölçekten önce gelir (thirty-two point four trillion)
                    v = float(f"{int(tot + cur) if not tot else int(cur)}.{dec}") * (1 if not tot else 1)
                if half: v += 0.5
                out.append(("sayi", v, once, sonra))
            i = j
        else:
            i += 1
    return out

def mantis(x):
    x = abs(x)
    while x >= 1000: x /= 1000
    return x

def izinli(taban):
    vals = []
    rt = os.path.join(taban, "rakam-tablosu.md")
    t = open(rt, encoding="utf-8").read() if os.path.exists(rt) else ""
    for m in re.finditer(r"(?<![\w.])(\d{1,3}(?:\.\d{3})+(?:,\d+)?|\d+,\d+|\d+)(?![\w])", t):
        s = m.group(1).replace(".", "").replace(",", "."); vals.append((float(s), "rakam-tablosu"))
    p = os.path.join(taban, "veri", "olcek-cikti.txt")
    if os.path.exists(p):
        for m in re.finditer(r"\d[\d,]*\.?\d*", open(p, encoding="utf-8").read()):
            try: vals.append((float(m.group(0).replace(",", "")), "olcek-hesap [H]"))
            except ValueError: pass
    return vals

def eslestir(v, once, vals, yuzde):
    """Tam değer karşılaştırması; yalnız 1000'in kuvveti kadar ölçek farkına izin (milyar $/yıl = $/ay). Yıllar ve <13 değerler aday değil."""
    tol = 0.07 if any(y in once for y in YAKLASIK) else 0.02
    for a, src in vals:
        if not a or (1900 <= a <= 2100 and a == int(a)): continue
        if yuzde:
            if a < 200 and abs(a - v) / a <= tol: return src, a, tol
            continue
        if a < 13: continue
        for k in (1, 1e3, 1e6, 1e9, 1e12, 1e-3):
            if abs(a * k - v) / (a * k) <= tol: return src, a, tol
    return None, None, tol

def main():
    yol = sys.argv[1]; yaz = "--yaz" in sys.argv
    taban = os.path.dirname(os.path.abspath(yol))
    md = open(yol, encoding="utf-8").read()
    govde = md.split("## 2. TAM METİN")[1].split("## 3. Retention")[0]
    sahne_re = r"^### (S\d\d) · ([^\n]*)\n\| ANLATIM \| GÖRSEL \|\n\|---\|---\|\n\| (.+?) \| (.+?) \|$"
    sahneler, bolum_bas = [], {}
    for m in re.finditer(r"^## (Bölüm \d+ — [^\n]+)$|" + sahne_re, govde, re.M):
        if m.group(1): bolum_bas[m.group(1)] = len(sahneler); continue
        sahneler.append(dict(id=m.group(2), baslik=m.group(3), anl=m.group(4).strip(), gor=m.group(5), k=len(m.group(4).split())))
    kum = 0
    for s in sahneler:
        s["bas_k"] = kum; s["t0"] = kum / KPM * 60; kum += s["k"]; s["t1"] = kum / KPM * 60
    toplam = kum; sure = toplam / KPM * 60; hata = []; uyari = []
    zaman = lambda s, i: (s["bas_k"] + len(s["anl"][:i].split())) / KPM * 60
    print("## Test kapısı çıktısı (metin-kontrol.py)\n")
    print(f"Hız: {KPM:.0f} kpm. Sahne: {len(sahneler)}.\n")
    print("| Sahne | Başlangıç–bitiş | Süre sn | Kelime |"); print("|---|---|---|---|")
    for s in sahneler: print(f"| {s['id']} | {mmss(s['t0'])}–{mmss(s['t1'])} | {s['t1']-s['t0']:.0f} | {s['k']} |")
    tire = sum(len(re.findall(r"\w-\w", s["anl"])) for s in sahneler)
    ok = ALT <= toplam <= UST
    print(f"\n**Toplam kelime:** {toplam} · **süre:** {mmss(sure)} ({sure/60:.1f} dk) · kapı {ALT}–{UST} → {'GEÇTİ' if ok else 'KALDI'}  (tireler ayrı: {toplam+tire} birim ≈ {mmss((toplam+tire)/KPM*60)})")
    if not ok: hata.append("kelime/süre")
    tum = " ".join(s["anl"] for s in sahneler).split()
    ilk15 = " ".join(tum[:int(15 * KPM / 60)]).lower()
    vaat = all(x in ilk15 for x in ["trillion", "charity", "spouse", "family", "kids"])
    print(f"\n**İlk 15 sn ({int(15*KPM/60)} kelime):** \"{ilk15}\" → somut özne + vaat: {'GEÇTİ' if vaat else 'KALDI'}")
    if not vaat: hata.append("ilk 15 sn")
    intro = INTRO.findall(" ".join(tum[:int(30 * KPM / 60)]))
    print(f"  İlk 30 sn kanal tanıtımı/abone kalıbı: {len(intro)} → {'GEÇTİ' if not intro else 'KALDI'}")
    if intro: hata.append("intro")
    # ↺
    print("\n**Yeniden kancalar (↺):**\n\n| # | Sahne | İfade | Zaman | Aralık sn | Sonuç |\n|---|---|---|---|---|---|")
    kancalar = [("hook", "S01", HOOK, 0.0)]
    for s in sahneler:
        for m in re.finditer(r"↺ ?\d+:\d\d\*?\*? \"([^\"]+)\"", s["gor"]):
            ifade = m.group(1).split("…")[0].strip(); i = s["anl"].find(ifade)
            if i < 0: hata.append(f"kanca yok {s['id']}"); print(f"| ? | {s['id']} | {ifade} | BULUNAMADI | - | KALDI |"); continue
            kancalar.append((f"↺{len(kancalar)}", s["id"], ifade, zaman(s, i)))
    kopru = next(s for s in sahneler if "KÖPRÜ" in s["baslik"])
    kancalar.append(("köprü", kopru["id"], kopru["anl"][:40], kopru["t0"]))
    kancalar.sort(key=lambda x: x[3]); onceki = None; maxar = 0
    for ad, sid, ifade, z in kancalar:
        ar = z - onceki if onceki is not None else 0; maxar = max(maxar, ar)
        sonuc = "GEÇTİ" if ar <= 75 else ("UYARI >75" if ar <= 90 else "KALDI")
        if ar > 90: hata.append(f"kanca aralığı {sid}")
        if 75 < ar <= 90: uyari.append(f"kanca {sid} {ar:.0f} sn")
        print(f"| {ad} | {sid} | {ifade[:46]} | {mmss(z)} | {ar:.0f} | {sonuc} |"); onceki = z
    print(f"\n  ↺ sayısı {len(kancalar)-2} + hook + köprü · en uzun aralık {maxar:.0f} sn (kapı ≤90, hedef ≤75) · köprüden sona {sure-kopru['t0']:.0f} sn")
    # ABONE
    ab = re.findall(r"^\| (ABONE-\d) \| [^|]* \| \"([^\"]+)\" \|", md, re.M)
    print(f"\n**ABONE satırları:** {len(ab)} (kapı 3–4)")
    if not 3 <= len(ab) <= 4: hata.append("ABONE sayısı")
    abz = {}
    for ad, capa in ab:
        bul = [(s, s["anl"].find(capa)) for s in sahneler if capa in s["anl"]]
        if len(bul) != 1: hata.append(f"{ad} çapası"); print(f"  {ad}: çapa bulunamadı/çoklu → KALDI"); continue
        s, i = bul[0]; z = zaman(s, i); abz[ad] = z
        dorukta = "DORUK" in s["baslik"] and i > 0
        okk = z >= 60 and not dorukta and (i == 0)
        if not okk: hata.append(f"{ad} konum")
        print(f"  {ad} @ {mmss(z)} · {s['id']} başı (önceki sahnenin nefesi) · \"{capa[:50]}\" · ≥60 sn, doruk üstünde değil, sahne başında: {'GEÇTİ' if okk else 'KALDI'}")
    sesli = [(s["id"], zaman(s, m.start())) for s in sahneler for m in ABONE_SOZ.finditer(s["anl"])]
    print(f"  Sesli abone kalıbı: {len(sesli)} (ilk 60 sn'de: {sum(1 for _, z in sesli if z < 60)}) → {'GEÇTİ' if not any(z < 60 for _, z in sesli) else 'KALDI'}")
    if any(z < 60 for _, z in sesli): hata.append("sesli abone ilk 60 sn")
    odul = next(s for s in sahneler if "İLK BÜYÜK ÖDÜL" in s["baslik"])
    if ab and min(abz.values(), default=0) < odul["t1"]: hata.append("ABONE ödülden önce")
    print(f"  İlk ABONE ilk büyük ödülden ({odul['id']} bitiş {mmss(odul['t1'])}) sonra: {'GEÇTİ' if abz and min(abz.values()) >= odul['t1'] else 'KALDI'}")
    # Shorts metinleri
    tam = re.findall(r"\*\*Okunacak tam metin[^:]*:\*\* <<(.+?)>>", md)
    anlatim = " ".join(s["anl"] for s in sahneler)
    hepsi = anlatim + " " + " ".join(tam)
    for ad, rx in (("Telaffuz yasak listesi", YASAK), ("H7 yayın gününe bağlı zaman sözcüğü", H7), ("Rakam tablosu yasakları (credit card / first time / 7-for-5 / toplam borç)", TABLO_YASAK), ("P1 parti/kişi adı", PARTI), ("K1 üç-olasılık kalıbı", K1)):
        y = [m.group(0) for m in rx.finditer(hepsi)]
        print(f"**{ad}** (anlatım+Shorts): {len(y)} → {'GEÇTİ' if not y else 'KALDI ' + str(y)}")
        if y: hata.append(ad)
    tvs = [(d, len(re.findall(d, hepsi, re.I))) for d in TAVSIYE]; tvs = [x for x in tvs if x[1]]
    print(f"**Tavsiye kalıbı** ({len(TAVSIYE)} desen): {sum(n for _, n in tvs)} → {'GEÇTİ' if not tvs else 'KALDI ' + str(tvs)}")
    if tvs: hata.append("tavsiye")
    nsh = len(re.findall(r"\bshould\b|\bmust\b|\bneed to\b", hepsi, re.I)); nsp = len(re.findall(r"spiral", hepsi, re.I))
    print(f"  ek: should/must/need to: {nsh}")
    # olgu-kaynak: sayı taşıyan her sahnenin GÖRSEL'inde "Kaynak:" etiketi
    eks = [x["id"] for x in sahneler if [y for y in sayilar(x["anl"]) if y[0] == "yil" or y[1] > 12] and "Kaynak:" not in x["gor"]]
    print(f"**Olgu-kaynak etiketi** (sayılı sahnede GÖRSEL 'Kaynak:'): eksik {len(eks)} → {'GEÇTİ' if not eks else 'KALDI ' + str(eks)}")
    if eks: hata.append("kaynak etiketi")
    # tez
    tz = []
    for s in sahneler:
        for t in (TEZ, TEZ2):
            i = s["anl"].lower().find(t)
            if i >= 0: tz.append((s["id"], zaman(s, i), zaman(s, i) + len(t.split()) / KPM * 60)); break
    bas = any(t1 <= 60 for _, _, t1 in tz); sonda = any(t0 >= sure - 90 for _, t0, _ in tz)
    print(f"**Tez (H1):** " + ", ".join(f"{sid} @ {mmss(a)}–{mmss(b)}" for sid, a, b in tz) + f" · ≤60 sn {'✓' if bas else '✗'} · son 90 sn {'✓' if sonda else '✗'}")
    if not (bas and sonda): hata.append("tez")
    # bölümler
    print("\n**YouTube bölümleri (betik zamanı):**\n```")
    bz = []
    for ad, i in bolum_bas.items():
        z = sahneler[i]["t0"]; bz.append(z); print(f"{mmss(z)} {ad.split(' — ',1)[1]}")
    print("```")
    okb = bz and bz[0] == 0 and all(b - a >= 10 for a, b in zip(bz, bz[1:])) and len(bz) >= 3
    print(f"  ilk 0:00, ≥3, aralar ≥10 sn: {'GEÇTİ' if okb else 'KALDI'}")
    if not okb: hata.append("bölümler")
    # Shorts
    if len(tam) < 2: hata.append("Shorts eksik")
    for i, tx in enumerate(tam, 1):
        k = len(tx.split()); b = k + len(re.findall(r"\w-\w", tx)); sn = b / KPM * 60
        if sn > 60: hata.append(f"Shorts {i} süre")
        print(f"**Shorts {i}:** {k} kelime · tireler ayrı {b} birim → ≈{sn:.1f} sn (kapı ≤60) {'GEÇTİ' if sn <= 60 else 'KALDI'}")
    # rakam eşleşmesi
    vals = izinli(taban); izin_yil = {int(a) for a, _ in vals if 1900 <= a <= 2100 and a == int(a)}
    print("\n**Rakam eşleşmesi** (ANLATIM + Shorts → rakam-tablosu.md + veri/olcek-cikti.txt; 'about/nearly/more than…' ile ±%7, yoksa ±%2):\n")
    print("| Kaynak | Sayı | Önce | Eşleşen | Sonuç |\n|---|---|---|---|---|")
    bulunmayan = 0; n = 0
    for etiket, metin in [(s["id"], s["anl"]) for s in sahneler] + [(f"Shorts{i}", t) for i, t in enumerate(tam, 1)]:
        for tur, v, once, sonra in sayilar(metin):
            if tur == "yil":
                okk = v in izin_yil; n += 1
                if not okk: bulunmayan += 1; hata.append(f"yıl {v} {etiket}")
                print(f"| {etiket} | yıl {v} | {once} | {'tabloda' if okk else '-'} | {'GEÇTİ' if okk else 'KALDI'} |"); continue
            if v <= 12 and sonra != "percent": continue
            n += 1; src, a, tol = eslestir(v, once, vals, sonra == "percent")
            if not src: bulunmayan += 1; hata.append(f"rakam {v:g} {etiket}")
            print(f"| {etiket} | {v:g}{' %' if sonra == 'percent' else ''} | {once} | {f'{a:g} ({src}, ±{tol*100:.0f}%)' if src else '-'} | {'GEÇTİ' if src else 'KALDI'} |")
    acik = govde.count("[R?")
    print(f"\n  {n} sayı kontrol edildi, tabloda olmayan: {bulunmayan} · metinde açık [RAKAM?]: {acik}")
    # 5-gram
    def ng(t, k=5):
        w = re.findall(r"[a-z0-9']+", t.lower()); return {tuple(w[i:i+k]) for i in range(len(w)-k+1)}
    a = ng(hepsi)
    for o in ONCEKI:
        p = os.path.normpath(os.path.join(taban, o))
        if os.path.exists(p):
            b = ng(open(p, encoding="utf-8").read()); oran = len(a & b) / max(1, len(a)) * 100
            print(f"**Özgünlük 5-gram** vs {os.path.basename(os.path.dirname(os.path.dirname(p)))}: {oran:.1f}% ({len(a & b)}/{len(a)}) → {'GEÇTİ' if oran <= 10 else 'KALDI'}")
            if oran > 10: hata.append("5-gram")
    # başlık zamanları
    fark = [s["id"] for s in sahneler if not re.match(rf"{mmss(s['t0'])}–{mmss(s['t1'])} · ", s["baslik"])]
    print(f"\n**Sahne başlığı zamanları betikle uyumlu:** {'GEÇTİ' if not fark else 'FARK: ' + ', '.join(fark)}")
    if yaz:
        for s in sahneler:
            yeni = re.sub(r"^\S+–\S+ · \d+ sn", f"{mmss(s['t0'])}–{mmss(s['t1'])} · {s['t1']-s['t0']:.0f} sn", s["baslik"])
            md = md.replace(f"### {s['id']} · {s['baslik']}\n", f"### {s['id']} · {yeni}\n", 1)
            for m in re.finditer(r"↺ \d+:\d\d \"([^\"]+)\"", s["gor"]):
                i = s["anl"].find(m.group(1).split("…")[0].strip())
                if i >= 0: md = md.replace(m.group(0), f"↺ {mmss(zaman(s, i))} \"{m.group(1)}\"", 1)
        open(yol, "w", encoding="utf-8").write(md); print("  (--yaz: başlık ve ↺ zamanları güncellendi; betiği yeniden çalıştırın)")
    elif fark: hata.append("başlık zamanı")
    if uyari: print(f"\n**Uyarılar:** {'; '.join(uyari)}")
    print(f"\n**KAPI: {'GEÇTİ' if not hata else 'KALDI → ' + '; '.join(hata)}**")
    sys.exit(1 if hata else 0)

main()
