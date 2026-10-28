#!/usr/bin/env python3
"""F3 metin politika denetimi — ölçüm betiği (monetizasyon-uyum-uzmani).

Kullanım:
  python3 -I politika-denetim.py metin.md [--kaynak DIR] [--onceki DOSYA ...]

Ölçer (çıkış deterministik; iki koşu aynı olmalı):
  1. Anlatım (ANLATIM sütunu) + ekran yazısı + Shorts satırları ayrıştırılır.
  2. Tavsiye / uzman / persona dili (answer/1311392 AI persona; Ö10).
  3. Reklam dostu: küfür, şok, hassas olay, tartışmalı konu kelimeleri — tüm metin
     ve ilk 30 sn ayrı (answer/6162278).
  4. Gerçek kişi / kurum adları (answer/14328491, karalama riski finans-dogrulayici'de).
  5. "Illustration" etiketi: gerçekçi olabilecek sahne (sepya/sokak/salon/banka içi/
     vitrin/bakkal/kuyruk) satırında etiket var mı (Ö11).
  6. Ö2: kaynak etiketli kendi veri grafikleri + veri dosyaları.
  7. Ö7: önceki metinlerle 5-gram örtüşmesi (iç kural ≤ %10).
  8. Ö8: kaynak metinlerle 8-gram örtüşmesi (≈0 beklenir; "yalnız okuma" değil).
  9. Shorts tek başına: kesitlerden kurulan Shorts metninde bağlam niteleyicisi
     ("decade", "prices were falling", "1929/1930s" vb.) var mı.
"""
import os
import re
import sys

ADVICE = [
    r"\byou should\b", r"\byou need to\b", r"\byou must\b", r"\bi recommend\b",
    r"\bmy advice\b", r"\bbuy now\b", r"\bsell now\b", r"\bguarantee", r"\binvest in\b",
    r"\bfinancial advi[cs]", r"\badvisor\b", r"\badviser\b", r"\bexpert\b",
    r"\bprofessional\b", r"\btrust me\b", r"\bdon'?t invest\b", r"\bbest investment\b",
    r"\btip\b", r"\btips\b", r"\bkeep (your )?cash\b", r"\bput your (money|savings)\b",
    r"\bmove your (money|savings)\b", r"\bpicked wrong\b", r"\bi believe\b",
    r"\bthe right (door|choice|move)\b", r"\bsafe (today|now)\b", r"\bin your portfolio\b",
    r"\bpull your money\b", r"\bdo not touch\b", r"\bplan\b", r"\brecommend",
]
PROFANITY = [r"\bshit", r"\bfuck", r"\bdamn\b", r"\bhell\b", r"\bcrap\b", r"\bbitch"]
SHOCK = [
    r"\bsuicid", r"\bkill", r"\bdeath\b", r"\bdead\b", r"\bdied\b", r"\bblood",
    r"\bcorpse", r"\bjump(ed)? from\b", r"\bwindow\b", r"\bleap", r"\bstarv",
    r"\bhunger\b", r"\bbreadline", r"\bhomeless", r"\bviolen", r"\briot",
    r"\bgun\b", r"\bweapon", r"\bwar\b", r"\bterror", r"\bdisaster\b", r"\bpanic\b",
    r"\bcollapse", r"\bcrash", r"\bruin", r"\bdestroy", r"\bshock", r"\bhorr",
]
REAL = [
    r"\broosevelt\b", r"\bhoover\b", r"\bbank of united states\b", r"\bfdic\b",
    r"\bfederal reserve\b", r"\bdow\b", r"\bbls\b", r"\bbea\b", r"\bhulbert\b",
    r"\bnew york times\b", r"\bjp ?morgan\b", r"\bmorgan\b",
]
REALISTIC = r"sepya|sokak|salon|banka içi|banka önü|vitrin|bakkal|kuyruk|mermer|otel"
QUALIFIER = [r"\bdecade\b", r"prices were falling", r"falling prices", r"\bin that\b",
             r"nineteen twenty-nine", r"nineteen thirty", r"\bin 1929\b"]


def norm(t):
    t = t.lower().replace("’", "'")
    return re.findall(r"[a-z0-9']+", t)


def ngrams(tokens, n):
    return {tuple(tokens[i:i + n]) for i in range(len(tokens) - n + 1)}


def overlap(a, b, n):
    ga, gb = ngrams(a, n), ngrams(b, n)
    if not ga:
        return 0.0, 0, 0, []
    ortak = ga & gb
    return 100.0 * len(ortak) / len(ga), len(ortak), len(ga), sorted(ortak)[:5]


def parse(md):
    sahneler = []  # (sid, baslangic_sn, anlatim, gorsel)
    for m in re.finditer(r"^### (S\d\d) · (\d+):(\d\d)–(\d+):(\d\d)[^\n]*\n(.*?)(?=^### |^## |\Z)",
                         md, flags=re.M | re.S):
        sid = m.group(1)
        bas = int(m.group(2)) * 60 + int(m.group(3))
        govde = m.group(6)
        satir = [s for s in govde.splitlines() if s.startswith("| ") and "ANLATIM" not in s
                 and not s.startswith("|---")]
        if not satir:
            continue
        hucre = satir[0].strip().strip("|").split(" | ", 1)
        sahneler.append((sid, bas, hucre[0].strip(), hucre[1].strip() if len(hucre) > 1 else ""))
    return sahneler


def ekran_yazilari(gorsel):
    out = []
    for m in re.finditer(r"\*\*Ekran:\*\*(.*?)(?=\*\*[A-ZÇĞİÖŞÜ][^*]{0,20}:\*\*|$)", gorsel):
        out += re.findall(r'"([^"]+)"', m.group(1))
    return out


def shorts_bolumu(md):
    m = re.search(r"^## 5\. Shorts.*?(?=^## 6\.)", md, flags=re.M | re.S)
    return m.group(0) if m else ""


def kesit_metni(sahneler, md_shorts):
    """Her Shorts için: hook + kesitler (baş… son ifadeleriyle) + kapanış."""
    anl = {s[0]: s[2] for s in sahneler}
    out = {}
    for blok in re.split(r"^### ", md_shorts, flags=re.M)[1:]:
        ad = blok.splitlines()[0].strip()
        parcalar = []
        hook = re.search(r"Kendi hook'u[^:]*:\*\*\s*\"([^\"]+)\"", blok)
        if hook:
            parcalar.append(("hook", hook.group(1)))
        kesit = re.search(r"\*\*Kesit[^:]*:\*\*(.*)", blok)
        if kesit:
            for sid, bas, son in re.findall(r"(S\d\d)[^(]*?\(\"(.+?)…(.+?)\"", kesit.group(1)):
                t = anl.get(sid, "")
                i = t.find(bas.strip())
                j = t.find(son.strip(), i if i >= 0 else 0)
                if i >= 0 and j >= 0:
                    parcalar.append((sid, t[i:j + len(son.strip())]))
                else:
                    parcalar.append((sid, "!!BULUNAMADI: " + bas + "…" + son))
        kap = re.search(r"Kapanış satırı[^:]*:\*\*\s*\"([^\"]+)\"", blok)
        if kap:
            parcalar.append(("kapanış", kap.group(1)))
        out[ad] = parcalar
    return out


def bul(desenler, metin):
    sonuc = []
    for d in desenler:
        for m in re.finditer(d, metin, flags=re.I):
            a, b = max(0, m.start() - 40), min(len(metin), m.end() + 40)
            sonuc.append((d, metin[a:b].replace("\n", " ")))
    return sonuc


def main():
    arg = sys.argv[1:]
    yol = arg[0]
    kaynak_dir, onceki = None, []
    if "--kaynak" in arg:
        kaynak_dir = arg[arg.index("--kaynak") + 1]
    if "--onceki" in arg:
        i = arg.index("--onceki") + 1
        while i < len(arg) and not arg[i].startswith("--"):
            onceki.append(arg[i])
            i += 1
    md = open(yol, encoding="utf-8").read()
    sahneler = parse(md)
    anlatim = " ".join(s[2] for s in sahneler)
    ekran = [e for s in sahneler for e in ekran_yazilari(s[3])]
    shorts = kesit_metni(sahneler, shorts_bolumu(md))
    shorts_yeni = " ".join(t for p in shorts.values() for k, t in p if k in ("hook", "kapanış"))
    tum = anlatim + " \n " + " \n ".join(ekran) + " \n " + shorts_yeni

    print(f"Sahne: {len(sahneler)} · anlatım kelime: {len(norm(anlatim))} · ekran yazısı: {len(ekran)} · Shorts: {len(shorts)}")

    print("\n[1] Tavsiye / uzman / persona dili (anlatım + ekran + Shorts yeni satırları)")
    t = bul(ADVICE, tum)
    for d, c in t:
        print(f"  {d:28s} … {c} …")
    print(f"  toplam eşleşme: {len(t)}")
    persona = bul([r"\bi'?m a cartoon\b", r"\byour host\b", r"\bi'?m leo\b"], anlatim)
    print(f"  persona-dışı (maskot) beyanı: {len(persona)} → " + "; ".join(c.strip() for _, c in persona))

    ilk30 = " ".join(s[2] for s in sahneler if s[1] < 30)
    # S02 0:17'de başlar; 30 sn ≈ 143 kpm × 0,5 = ~72 kelime
    ilk30_k = " ".join(norm(anlatim)[:72])
    print("\n[2] Reklam dostu dil")
    print(f"  küfür (tüm): {len(bul(PROFANITY, tum))} · küfür (ilk 30 sn): {len(bul(PROFANITY, ilk30_k))}")
    s_all = bul(SHOCK, tum)
    s_30 = bul(SHOCK, ilk30_k)
    print(f"  şok/hassas (tüm): {len(s_all)} · (ilk 30 sn ≈72 kelime): {len(s_30)}")
    for d, c in s_all:
        print(f"    {d:18s} … {c} …")

    print("\n[3] Gerçek kişi / kurum (anlatım + ekran)")
    for d in REAL:
        n = len(re.findall(d, anlatim + " " + " ".join(ekran), flags=re.I))
        if n:
            print(f"  {d:28s} {n}")

    print("\n[4] 'Illustration' etiketi (gerçekçi olabilecek sahneler)")
    eksik = 0
    for sid, bas, a, g in sahneler:
        if re.search(REALISTIC, g, flags=re.I):
            var = "Illustration" in g
            eksik += 0 if var else 1
            kelime = ",".join(sorted(set(m.group(0).lower() for m in re.finditer(REALISTIC, g, flags=re.I))))
            print(f"  {sid} ({kelime}): etiket {'VAR' if var else 'YOK'}")
    print(f"  etiketsiz gerçekçi-aday sahne: {eksik}")

    print("\n[5] Ö2 kendi veri grafikleri (kaynak etiketli)")
    gr = sorted(set(re.findall(r"\*\*Grafik (G\d+[a-z]?)", md)))
    src = sum(1 for s in sahneler if "Grafik G" in s[3] and "Source:" in s[3])
    print(f"  grafik kimlikleri: {', '.join(gr)} ({len(gr)}) · 'Source:' içeren grafik sahnesi: {src}")
    vd = os.path.join(os.path.dirname(os.path.abspath(yol)), "veri")
    if os.path.isdir(vd):
        print(f"  veri dosyaları: {', '.join(sorted(f for f in os.listdir(vd) if f.endswith('.csv')))}")

    print("\n[6] Ö7 önceki metinlerle 5-gram örtüşmesi (anlatım + Shorts yeni satırları)")
    tok = norm(anlatim + " " + shorts_yeni)
    for f in onceki:
        try:
            b = norm(open(f, encoding="utf-8", errors="ignore").read())
        except OSError:
            print(f"  {f}: OKUNAMADI")
            continue
        p, k, n, ornek = overlap(tok, b, 5)
        print(f"  {os.path.relpath(f)}: %{p:.1f} ({k}/{n}) {'GEÇTİ' if p <= 10 else 'KALDI'}"
              + (f" örnek: {[' '.join(o) for o in ornek]}" if ornek else ""))
    # metin içi kalıp tekrarı (aynı 6-gram ≥3 kez)
    from collections import Counter
    c = Counter(tuple(tok[i:i + 6]) for i in range(len(tok) - 5))
    tekrar = [(" ".join(g), n) for g, n in c.most_common() if n >= 3]
    print(f"  metin içi 6-gram ≥3 tekrar: {len(tekrar)} " + "; ".join(f"'{g}'×{n}" for g, n in tekrar[:6]))

    if kaynak_dir:
        print("\n[7] Ö8 kaynak metinlerle 8-gram örtüşmesi (anlatım)")
        ta = norm(anlatim)
        for f in sorted(os.listdir(kaynak_dir)):
            if f.endswith(".txt"):
                b = norm(open(os.path.join(kaynak_dir, f), encoding="utf-8", errors="ignore").read())
                p, k, n, ornek = overlap(ta, b, 8)
                print(f"  {f}: %{p:.2f} ({k}/{n})" + (f" örnek: {[' '.join(o) for o in ornek]}" if ornek else ""))

    print("\n[8] Shorts tek başına (bağlam niteleyicisi ve tavsiye dili)")
    for ad, parcalar in shorts.items():
        metin = " ".join(t for _, t in parcalar)
        k = len(norm(metin))
        q = [d for d in QUALIFIER if re.search(d, metin, flags=re.I)]
        adv = bul(ADVICE, metin)
        son = parcalar[-1][1] if parcalar else ""
        kh = len(re.findall(r"[A-Za-z0-9'’.-]+", metin))
        print(f"  {ad}: {k} kelime (tireli sayı tek kelime: {kh}) ≈{k / 143 * 60:.0f}/{kh / 143 * 60:.0f} sn · niteleyici: {q or 'YOK'} · tavsiye: {len(adv)}")
        for kk, tt in parcalar:
            print(f"    [{kk}] {tt}")
        qson = [d for d in QUALIFIER[:3] if re.search(d, " ".join(t for kk, t in parcalar if kk not in ('hook',)), flags=re.I)]
        print(f"    'o on yıl / fiyatlar düşüyordu' niteleyicisi (hook dışı): {qson or 'YOK'}")

    # [8b] Yetkili metin: §5'teki "Okunacak tam metin" <<...>> (RED-1 sonrası eklendi).
    # Kesit ayrıştırması biçime duyarlı; tam metin TTS'e gidecek metindir. Her cümlenin
    # kökeni (ana anlatım / yeni kayıt) ve tek başına okumada niteleyici + tavsiye ölçülür.
    print("\n[8b] Shorts yetkili tam metin (<<...>>) — köken + tek başına okuma")
    sb = shorts_bolumu(md)
    an = re.sub(r"\s+", " ", anlatim)
    for blok in re.split(r"^### ", sb, flags=re.M)[1:]:
        ad = blok.splitlines()[0].strip()
        m = re.search(r"<<(.+?)>>", blok, flags=re.S)
        if not m:
            print(f"  {ad}: tam metin YOK")
            continue
        tm = re.sub(r"\s+", " ", m.group(1)).strip()
        cumleler = [c.strip() for c in re.split(r"(?<=[.?!])\s+", tm) if c.strip()]
        yeni = [c for c in cumleler if c.rstrip(".?!") not in an]
        q = [d for d in QUALIFIER if re.search(d, tm, flags=re.I)]
        adv = bul(ADVICE, tm)
        kh = len(re.findall(r"[A-Za-z0-9'’.]+", tm.replace("-", " ")))
        print(f"  {ad}: {len(cumleler)} cümle · tireler ayrı {kh} birim ≈{kh / 143 * 60:.1f} sn · niteleyici: {q or 'YOK'} · tavsiye: {len(adv)}")
        for c in yeni:
            print(f"    ana anlatımda YOK (yeni kayıt): {c}")


if __name__ == "__main__":
    main()
