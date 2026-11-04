#!/usr/bin/env python3
"""F2 senaryo kapısı (v3, 2026-11-04; v2 = 2026-10-28-yeni-video/02-senaryo/senaryo-kontrol.py).
v3 ekleri: --sutun birden çok sütun kabul eder ("A,C") · çalışma başlığında çıplak $rakam / yıl YASAK (kanal dersi 1; alternatiflerde UYARI)
· 2 Shorts kancası, her biri ≤30 kelime ve "?" ile biter (kanal dersi 2: cevap uzun videoda) · Vaat / Thumbnail / Outlier kanıtı alanı zorunlu
· A sütununda "Tarih→gelecek köprüsü" zorunlu (kanal dersi 1) · yayımlanmış videoların Leo rolleri ve açılış kalıpları (1929, S08) yasak
· "By the end, you'll know" vaat kalıbı yasak (hafıza 2026-11-02).
Kullanım: python3 senaryo-kontrol.py senaryolar.md --sutun A,C"""
import re, sys
YASAK = re.compile(r"\b(charts?|complicated|scenarios?|truth|crash(es|ed|ing)?|bold)\b", re.I)
KALIP_BASLIK = re.compile(r"\b(nobody|no one|real reason|true origin|get wrong)\b|\bAI bubble\b", re.I)
ESKI_ACILIS = re.compile(r"(it's september|you have one thousand|let's play|imagine waking|three doors|shrink the|let's sit at)", re.I)
VAAT_KALIP = re.compile(r"by the end,? you'?ll know", re.I)
CIPLAK = re.compile(r"\$\s?\d|\b(1[5-9]|20)\d\d\b")
YAYINLI_ROL = ("oyun sunucusu", "ev arkadaşı", "bütçe tutan")
args = sys.argv[1:]
sutun_hedef = set((args[args.index("--sutun") + 1] if "--sutun" in args else "A,C").split(","))
metin = open(args[0], encoding="utf-8").read()
govde = metin.split("## Test")[0]
bloklar = re.split(r"^### (S\d\d) — ", govde, flags=re.M)[1:]
hata = 0; uyari = 0; acilar = {}; sutun = {}; roller = {}
def kelime(s): return len(re.findall(r"[A-Za-z0-9$][\w$.,'’\-]*", s))
def satir(*h): print("| " + " | ".join(str(x) for x in h) + " |")
satir("ID", "Alan", "Metin", "Karakter", "Kelime", "Bulgu", "Sonuç"); satir(*["---"] * 7)
for i in range(0, len(bloklar), 2):
    sid, blok = bloklar[i], bloklar[i+1]
    basliklar = re.findall(r"^- \*\*(Çalışma başlığı|Alternatif 1|Alternatif 2):\*\* (.+)$", blok, re.M)
    if len(basliklar) != 3: satir(sid, "Başlık sayısı", len(basliklar), "—", "—", "3 gerekli", "KALDI"); hata += 1
    for alan, deger in basliklar:
        d = deger.strip(); n = len(d); k = KALIP_BASLIK.search(d); c = CIPLAK.search(d)
        ok = n <= 60 and not k and not (c and alan == "Çalışma başlığı")
        bulgu = ", ".join(x for x in [k.group(0) if k else "", f"çıplak {c.group(0)}" if c else ""] if x) or "yok"
        sonuc = "GEÇTİ" if ok else "KALDI"
        if ok and c: sonuc = "UYARI"; uyari += 1
        hata += not ok; satir(sid, alan, d, n, "—", bulgu, sonuc)
    h = re.search(r"^- \*\*Hook \(kelimesi kelimesine, 0–15 sn\):\*\* \"(.+)\"$", blok, re.M)
    if not h: satir(sid, "Hook", "YOK", "—", "—", "—", "KALDI"); hata += 1
    else:
        k = kelime(h.group(1)); y = sorted({m.group(0).lower() for m in YASAK.finditer(h.group(1))}); e = ESKI_ACILIS.search(h.group(1))
        ok = k <= 40 and not y and not e; hata += not ok
        satir(sid, "Hook", "(seçilen)", "—", k, ", ".join(y + ([e.group(0)] if e else [])) or "yok", "GEÇTİ" if ok else "KALDI")
    elenen = len(re.findall(r"^  - H\d .*\(elendi", blok, re.M)); ok = elenen >= 2; hata += not ok
    satir(sid, "Elenen hook varyantı", elenen, "—", "—", "≥2", "GEÇTİ" if ok else "KALDI")
    for no in ("1", "2"):
        sh = re.search(rf"^- \*\*Shorts kancası {no}:\*\* \"(.+?)\"", blok, re.M)
        if not sh: satir(sid, f"Shorts {no}", "YOK", "—", "—", "—", "KALDI"); hata += 1; continue
        t = sh.group(1); y = sorted({m.group(0).lower() for m in YASAK.finditer(t)})
        ok = not y and kelime(t) <= 30 and t.rstrip().endswith("?"); hata += not ok
        satir(sid, f"Shorts {no}", "açık soru" if t.rstrip().endswith("?") else "SORU YOK", "—", kelime(t), ", ".join(y) or "yok", "GEÇTİ" if ok else "KALDI")
    s = re.search(r"^- \*\*Sütun:\*\* (\w)", blok, re.M); sutun[sid] = s.group(1) if s else "?"
    alanlar = ["Vaat", "Thumbnail fikri", "Outlier kanıtı", "Risk notu", "Sonuçtan bağımsızlık"] + (["Tarih→gelecek köprüsü"] if sutun[sid] == "A" else [])
    for alan in alanlar:
        ok = bool(re.search(rf"^- \*\*{re.escape(alan)}[^:]*:\*\* \S", blok, re.M)); hata += not ok
        satir(sid, alan, "var" if ok else "YOK", "—", "—", "—", "GEÇTİ" if ok else "KALDI")
    v = VAAT_KALIP.search(blok)
    if v: satir(sid, "Vaat kalıbı", v.group(0), "—", "—", "eski kalıp", "KALDI"); hata += 1
    a = re.search(r"^- \*\*Açı türü:\*\* ([^(\n]+)", blok, re.M)
    r = re.search(r"^- \*\*Leo'nun rolü[^:]*:\*\* \*\*([^*]+)\*\*", blok, re.M)
    acilar[sid] = a.group(1).strip() if a else "?"
    roller[sid] = r.group(1).strip().lower() if r else "?"
n = len(acilar); farkli = len(set(acilar.values())); s_say = sum(1 for v in sutun.values() if v in sutun_hedef)
rol_farkli = len(set(roller.values())) == n and "?" not in roller.values()
rol_yayinli = [sid for sid, r in roller.items() if any(y in r for y in YAYINLI_ROL)]
print(f"\nSenaryo sayısı: {n} (kapı ≥10) · farklı açı türü: {farkli} (kapı ≥7) · {'/'.join(sorted(sutun_hedef))} sütunu: {s_say} (kapı ≥8) · Leo rolleri hepsi farklı: {rol_farkli} · yayımlanmış rol tekrarı: {rol_yayinli or 'yok'} · uyarı: {uyari}")
for sid in acilar: print(f"  {sid}: {sutun[sid]} · {acilar[sid]} · Leo: {roller[sid]}")
if n < 10 or farkli < 7 or s_say < 8 or not rol_farkli or rol_yayinli: hata += 1
print("KAPI:", "GEÇTİ" if hata == 0 else f"KALDI ({hata} hata)")
sys.exit(1 if hata else 0)
