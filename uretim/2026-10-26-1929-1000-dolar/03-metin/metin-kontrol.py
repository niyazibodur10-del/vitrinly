#!/usr/bin/env python3
"""F3 Metin + Retention (metin) kapısı.
Kullanım: python3 -I metin-kontrol.py metin.md [--yaz]   (--yaz: sahne başlıklarındaki zamanları betik ölçümüyle günceller)
Ölçüm: ANLATIM sütunu (her sahne tablosunun ilk hücresi), kelime = boşlukla ayrılmış birim, hız 143 kpm (am_fenrir 0.9).
Kapılar: toplam ≥1500 kelime ve hedef 12 dk ±%10 (1544–1888); ilk 15 sn'de vaat; ↺ yeniden kancalar arası ≤90 sn;
abone çağrısı ≥60 sn ve ilk büyük ödülden sonra; telaffuz yasak kelimesi 0; tavsiye kalıbı 0; mit kalıbı 0;
ilk 30 sn'de kanal tanıtımı yok; tez başta (≤60 sn) ve sonda; bölümler ≥10 sn; Shorts ≤60 sn; önceki metinlerle 5-gram örtüşmesi ≤%10.
"""
import re, sys, os

KPM = 143.0
HEDEF_DK = 12.0
YASAK = re.compile(r"\b(charts?|complicated|scenarios?|truth|crash(es|ed|ing)?|bold)\b", re.I)
TAVSIYE = [r"\byou should\b", r"\bi recommend\b", r"\bbuy now\b", r"\bsell now\b", r"\bguaranteed?\b",
           r"\binvest in\b", r"\bfinancial advi[cs]", r"\badvis[oe]r\b", r"\bexpert\b", r"\bdon'?t invest\b",
           r"\bbest investment\b", r"\btip\b", r"\bterrible bet\b", r"\bbad investment\b", r"\bdo not touch\b",
           r"\bkeep (your )?cash\b", r"\bpicked wrong\b", r"\bi believe now\b", r"\byou need to\b",
           r"\bthe best place\b", r"\bput your money\b", r"\bnot (financial )?advice\b", r"\bthis isn'?t advice\b",
           r"\bmy advice\b", r"\bwe recommend\b"]
MIT = re.compile(r"\b(suicid\w*|jump(ed|ing)? from|window|leap(ed|t)?)\b", re.I)
INTRO = re.compile(r"\b(hi guys|hey guys|welcome (back )?to|toonomy|channel|subscribe|like button)\b", re.I)
ABONE = re.compile(r"\bsubscri\w*|\blike button\b|\bbell\b", re.I)
TEZ = "a safe place for money isn't really a place"
ONCEKI = ["../../ses-testi/okuma-metni.md", "../../ses-testi/tts/anlatici-v1-metin.txt"]

def mmss(s):
    s = int(round(s)); return f"{s//60}:{s%60:02d}"

def kelimeler(t):
    return t.split()

def main():
    yol = sys.argv[1]; yaz = "--yaz" in sys.argv
    md = open(yol, encoding="utf-8").read()
    govde = md.split("## 2. TAM METİN")[1].split("## 3. Retention")[0]
    # sahneler
    sahne_re = re.compile(r"^### (S\d\d) · ([^\n]*)\n\| ANLATIM \| GÖRSEL \|\n\|---\|---\|\n\| (.+?) \| (.+?) \|$", re.M)
    sahneler = []
    bolum_bas = {}
    poz = 0
    for m in re.finditer(r"^## (Bölüm \d+ — [^\n]+)$|" + sahne_re.pattern, govde, re.M):
        if m.group(1):
            bolum_bas[m.group(1)] = len(sahneler); continue
        sid, bas, anl, gor = m.group(2), m.group(3), m.group(4), m.group(5)
        sahneler.append(dict(id=sid, baslik=bas, anl=anl.strip(), gor=gor, k=len(kelimeler(anl))))
    t = 0.0; kum = 0
    for s in sahneler:
        s["bas_k"] = kum; s["t0"] = kum / KPM * 60; kum += s["k"]; s["t1"] = kum / KPM * 60
    toplam = kum; sure = toplam / KPM * 60
    hata = []
    print("## Test kapısı çıktısı (metin-kontrol.py)\n")
    print(f"Hız varsayımı: {KPM:.0f} kpm (am_fenrir 0.9 ölçümü). Sahne sayısı: {len(sahneler)}.\n")
    print("| Sahne | Başlangıç–bitiş | Süre sn | Kelime |"); print("|---|---|---|---|")
    for s in sahneler:
        print(f"| {s['id']} | {mmss(s['t0'])}–{mmss(s['t1'])} | {s['t1']-s['t0']:.0f} | {s['k']} |")
    alt, ust = HEDEF_DK * KPM * 0.9, HEDEF_DK * KPM * 1.1
    tire = sum(len(re.findall(r"\w-\w", s["anl"])) for s in sahneler)
    ok = toplam >= 1500 and alt <= toplam <= ust and sure >= 600
    print(f"\n**Toplam kelime:** {toplam} · **tahmini süre:** {mmss(sure)} ({sure/60:.1f} dk) · kapı ≥1500 ve hedef {HEDEF_DK:.0f} dk ±%10 = {alt:.0f}–{ust:.0f} kelime → {'GEÇTİ' if ok else 'KALDI'}")
    print(f"  (Not: tireli sayı kelimesi {tire} adet; tireler ayrı sayılırsa {toplam+tire} birim ≈ {mmss((toplam+tire)/KPM*60)} — üst sınır tahmini.)")
    if not ok: hata.append("kelime/süre")
    # ilk 15 sn
    tum = " ".join(s["anl"] for s in sahneler).split()
    n15 = int(15 * KPM / 60)
    ilk15 = " ".join(tum[:n15])
    vaat = all(w in ilk15.lower() for w in ["door", "disaster", "gamble"]) and "thousand dollars" in ilk15.lower()
    print(f"\n**İlk 15 sn ({n15} kelime):** \"{ilk15}\"")
    print(f"  somut özne (thousand dollars + door) ve vaat (disaster/gamble) ilk 15 sn içinde: {'GEÇTİ' if vaat else 'KALDI'} · 'surprise' kelime sırası: {tum.index('surprise.')+1 if 'surprise.' in tum else '-'}")
    if not vaat: hata.append("ilk 15 sn vaat")
    ilk30 = " ".join(tum[:int(30 * KPM / 60)])
    intro = INTRO.findall(ilk30)
    print(f"  İlk 30 sn kanal tanıtımı/abone kalıbı: {len(intro)} {'GEÇTİ' if not intro else 'KALDI'}")
    if intro: hata.append("ilk 30 sn intro")
    # yeniden kancalar
    print("\n**Yeniden kancalar (↺):**\n\n| # | Sahne | İfade | Zaman | Önceki kancadan aralık sn | Sonuç |\n|---|---|---|---|---|---|")
    kancalar = [("hook", "S01", "It's September nineteen twenty-nine", 0.0)]
    for s in sahneler:
        for m in re.finditer(r"↺ ?\d+:\d\d\*?\*? \"([^\"]+)\"", s["gor"]):
            ifade = m.group(1).split("…")[0].strip()
            i = s["anl"].find(ifade)
            if i < 0:
                hata.append(f"kanca ifadesi bulunamadı {s['id']}"); print(f"| ? | {s['id']} | {ifade} | BULUNAMADI | - | KALDI |"); continue
            kpos = s["bas_k"] + len(s["anl"][:i].split())
            kancalar.append((f"↺{len(kancalar)}", s["id"], ifade, kpos / KPM * 60))
    onceki = None; maxar = 0
    for ad, sid, ifade, z in kancalar:
        ar = z - onceki if onceki is not None else 0; maxar = max(maxar, ar)
        okk = ar <= 90
        if not okk: hata.append(f"kanca aralığı {sid}")
        print(f"| {ad} | {sid} | {ifade[:48]} | {mmss(z)} | {ar:.0f} | {'GEÇTİ' if okk else 'KALDI'} |")
        onceki = z
    son = sure - onceki
    # Son kancadan sonra metin sonuna kadar olan kısım: döngü kapanışı + köprü; yine ≤90 sn olmalı mı? Kapanış bölümü
    # (twist ödülü + tez) ölçülür ve raporlanır; köprü cümlesi son kancadır.
    kopru_i = next(s for s in sahneler if s["id"] == "S24")
    kz = kopru_i["t0"]
    ar = kz - onceki; okk = ar <= 90
    if not okk: hata.append("köprü aralığı")
    print(f"| köprü | S24 | Falling prices made a shoebox the winner (uç ekran) | {mmss(kz)} | {ar:.0f} | {'GEÇTİ' if okk else 'KALDI'} |")
    maxar = max(maxar, ar)
    print(f"\n  Kanca sayısı: {len(kancalar)-1} ↺ + hook + köprü · en uzun aralık {maxar:.0f} sn (kapı ≤90)")
    # abone
    ab = [(s["id"], s["bas_k"] + len(s["anl"][:m.start()].split())) for s in sahneler for m in ABONE.finditer(s["anl"])]
    odul = next(s for s in sahneler if "İLK BÜYÜK ÖDÜL" in s["baslik"])
    print(f"\n**Abone çağrısı:** {len(ab)} adet · " + ", ".join(f"{sid} @ {mmss(k/KPM*60)}" for sid, k in ab))
    okab = len(ab) >= 1 and all(k / KPM * 60 >= 60 for _, k in ab) and all(k >= odul["bas_k"] + odul["k"] for _, k in ab)
    print(f"  ilk 60 sn'de yok ve ilk büyük ödülden ({odul['id']}, bitiş {mmss(odul['t1'])}) sonra: {'GEÇTİ' if okab else 'KALDI'}")
    if not okab: hata.append("abone konumu")
    # yasak kelimeler / tavsiye / mit — anlatım + Shorts hook'ları
    shorts = re.findall(r"\*\*Kendi hook'u[^:]*:\*\* \"([^\"]+)\"", md) + re.findall(r"\*\*Kapanış satırı[^:]*:\*\* \"([^\"]+)\"", md)
    anlatim = " ".join(s["anl"] for s in sahneler) + " " + " ".join(shorts)
    y = YASAK.findall(anlatim)
    print(f"\n**Telaffuz yasak listesi** (charts, complicated, scenarios, truth, crash*, bold) anlatım+Shorts: {len(y)} → {'GEÇTİ' if not y else 'KALDI ' + str(y)}")
    if y: hata.append("yasak kelime")
    tv = [(d, len(re.findall(d, anlatim, re.I))) for d in TAVSIYE]
    tvs = [(d, n) for d, n in tv if n]
    print(f"**Tavsiye kalıbı taraması** ({len(TAVSIYE)} desen): {sum(n for _, n in tvs)} eşleşme → {'GEÇTİ' if not tvs else 'KALDI ' + str(tvs)}")
    if tvs: hata.append("tavsiye kalıbı")
    should = re.findall(r"\bshould\b|\bmust\b|\bneed to\b", anlatim, re.I)
    print(f"  ek: should/must/need to: {len(should)}")
    mit = MIT.findall(anlatim)
    print(f"**Mit taraması** (suicide|jump from|window|leap): {len(mit)} → {'GEÇTİ' if not mit else 'KALDI'}")
    if mit: hata.append("mit")
    # tez
    tz = []
    for s in sahneler:
        i = s["anl"].lower().find(TEZ)
        if i >= 0:
            k0 = s["bas_k"] + len(s["anl"][:i].split()); tz.append((s["id"], k0 / KPM * 60, (k0 + len(TEZ.split())) / KPM * 60))
    bas = any(t1 <= 60 for _, _, t1 in tz); sonda = any(t0 >= sure - 90 for _, t0, _ in tz)
    print(f"**Tez (Ö1)** \"{TEZ}\": " + ", ".join(f"{sid} @ {mmss(t0)}–{mmss(t1)}" for sid, t0, t1 in tz) + f" · başta (cümle ≤60 sn'de biter) {'✓' if bas else '✗'} · sonda (son 90 sn) {'✓' if sonda else '✗'}")
    if not (bas and sonda): hata.append("tez")
    # bölümler
    print("\n**YouTube bölümleri (betik zamanı):**\n```")
    bz = []
    for ad, i in bolum_bas.items():
        z = sahneler[i]["t0"]; bz.append(z); print(f"{mmss(z)} {ad.split(' — ',1)[1]}")
    print("```")
    okb = bz and bz[0] == 0 and all(b - a >= 10 for a, b in zip(bz, bz[1:])) and len(bz) >= 3
    print(f"  ilk 0:00, ≥3 bölüm, aralar ≥10 sn: {'GEÇTİ' if okb else 'KALDI'}")
    if not okb: hata.append("bölümler")
    # Shorts hook'ları
    print("\n**Shorts hook'ları:** " + " · ".join(f"\"{h}\" = {len(h.split())} kelime" for h in shorts))
    # 5-gram örtüşme
    def ng(t, n=5):
        w = re.findall(r"[a-z0-9']+", t.lower()); return {tuple(w[i:i+n]) for i in range(len(w)-n+1)}
    a = ng(anlatim)
    taban = os.path.dirname(os.path.abspath(yol))
    for o in ONCEKI:
        p = os.path.normpath(os.path.join(taban, o))
        if os.path.exists(p):
            b = ng(open(p, encoding="utf-8").read()); oran = len(a & b) / max(1, len(a)) * 100
            print(f"**Ö7 5-gram örtüşmesi** vs `{os.path.relpath(p, os.path.join(taban,'../..'))}`: {oran:.1f}% ({len(a & b)}/{len(a)}) → {'GEÇTİ' if oran <= 10 else 'KALDI'}")
            if oran > 10: hata.append("Ö7")
    # başlık zamanları
    fark = []
    for s in sahneler:
        m = re.match(r"(\d+:\d\d)–(\d+:\d\d)", s["baslik"])
        if not m or m.group(1) != mmss(s["t0"]) or m.group(2) != mmss(s["t1"]):
            fark.append(s["id"])
    print(f"\n**Sahne başlığı zamanları betikle uyumlu:** {'GEÇTİ' if not fark else 'FARK: ' + ', '.join(fark)}")
    if yaz and fark:
        for s in sahneler:
            yeni = re.sub(r"^\S+–\S+ · \d+ sn", f"{mmss(s['t0'])}–{mmss(s['t1'])} · {s['t1']-s['t0']:.0f} sn", s["baslik"])
            md = md.replace(f"### {s['id']} · {s['baslik']}\n", f"### {s['id']} · {yeni}\n", 1)
        open(yol, "w", encoding="utf-8").write(md); print("  (--yaz: başlıklar güncellendi; betiği yeniden çalıştırın)")
    if fark and not yaz: hata.append("başlık zamanı")
    print(f"\n**KAPI: {'GEÇTİ' if not hata else 'KALDI → ' + '; '.join(hata)}**")
    sys.exit(1 if hata else 0)

main()
