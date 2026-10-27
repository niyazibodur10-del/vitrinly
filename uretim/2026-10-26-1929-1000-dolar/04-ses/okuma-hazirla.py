#!/usr/bin/env python3
"""F4 ses — kilitli metinden (03-metin/metin.md) TTS okuma metni çıkarır (ses-yonetmeni, 2026-10-27).

Kullanım: python3 -I okuma-hazirla.py   (04-ses klasöründe)
Çıkış:
  okuma-metni.txt      Kokoro'ya verilen metin: sahne başına bir satır (satır sonu = paragraf duraklaması).
  referans-metni.txt   WER referansı: kilitli metnin AYNISI (telaffuz yazımı yok).
  sahne-esleme.json    sahne → cümle aralığı (tts.py'nin cümle bölmesiyle aynı kural) + kelime sayısı.
  shorts-1-ek.txt, shorts-2-ek.txt   Shorts'ta ana anlatımda olmayan cümleler (hook / kapanış).
Anlam DEĞİŞMEZ. Tek telaffuz yazımı: "U.S." → [U.S.](/jˌuˈɛs/) — nedeni: tts.py "U.S. " sonrasında cümleyi
bölüyordu (cümle ortasında 0,3 sn sessizlik); fonetik işaretleme hem bölünmeyi engeller hem "you-ess" okutur.
Telaffuz testi (FDIC / F D I C / F-D-I-C, Roosevelt, Dow, Toonomy, yıllar): ses-rapor.md §2.
"""
import json, re, sys
from pathlib import Path

KOK = Path(__file__).resolve().parent
MD = (KOK.parent / "03-metin" / "metin.md").read_text(encoding="utf-8")
SAHNE = re.compile(r"^### (S\d\d) · ([^\n]*)\n\| ANLATIM \| GÖRSEL \|\n\|---\|---\|\n\| (.+?) \| (.+?) \|$", re.M)
TELAFFUZ = [("U.S.", "[U.S.](/jˌuˈɛs/)")]


def cumleler(p):  # tools/ses/tts.py cumlelere_bol ile aynı desen
    return [c.strip() for c in re.findall(r".+?(?:\.\.\.|[.!?…]+|$)(?=\s+|$)", p) if c.strip()]


def okunus(t):
    for a, b in TELAFFUZ:
        t = t.replace(a, b)
    return t


sahneler = SAHNE.findall(MD)
if len(sahneler) != 24:
    sys.exit(f"HATA: 24 sahne bekleniyordu, {len(sahneler)} bulundu")
okuma, ref, esleme, i = [], [], [], 0
for sid, bas, anl, _ in sahneler:
    anl = anl.strip(); ok = okunus(anl); n = len(cumleler(ok))
    okuma.append(ok); ref.append(anl)
    esleme.append({"sahne": sid, "metin_basligi": bas.strip(), "cumle_ilk": i, "cumle_son": i + n - 1,
                   "kelime": len(anl.split())})
    i += n
(KOK / "okuma-metni.txt").write_text("\n".join(okuma) + "\n", encoding="utf-8")
(KOK / "referans-metni.txt").write_text("\n".join(ref) + "\n", encoding="utf-8")
json.dump({"kaynak": "03-metin/metin.md (kilitli)", "cumle_sayisi": i, "sahneler": esleme},
          open(KOK / "sahne-esleme.json", "w"), indent=1, ensure_ascii=False)

# Shorts: ana anlatımda birebir geçmeyen cümleler ayrı kayıt ister
tam = re.findall(r"\*\*Okunacak tam metin[^:]*:\*\* <<(.+?)>>", MD)
ana = " ".join(ref)
for k, metin in enumerate(tam, 1):
    eksik, gruplar, onceki = [], [], False
    for c in cumleler(metin):  # art arda gelen eksik cümleler tek satır (hook / kapanış birer parça)
        yok = c not in ana
        if yok:
            eksik.append(c)
            if onceki: gruplar[-1] += " " + c
            else: gruplar.append(c)
        onceki = yok
    (KOK / f"shorts-{k}-ek.txt").write_text("\n".join(okunus(g) for g in gruplar) + "\n", encoding="utf-8")
    print(f"Shorts {k}: {len(cumleler(metin))} cümle, ana anlatımda olmayan {len(eksik)}: {eksik}")
print(f"{len(sahneler)} sahne, {i} cümle, {sum(e['kelime'] for e in esleme)} kelime")
