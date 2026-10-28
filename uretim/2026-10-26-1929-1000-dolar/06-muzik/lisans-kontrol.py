#!/usr/bin/env python3
"""Kapı: 06-muzik/kaynak altındaki her ses dosyası lisans-kaydi.md'de geçiyor mu, NC/ND/SA lisans var mı.
Grup yazımı ("lock_01/02/03", "tick1/2") açılarak eşlenir. Çıkış kodu 0 = GEÇTİ."""
import glob, os, re, sys
d = os.path.dirname(os.path.abspath(__file__))
metin = open(f"{d}/lisans-kaydi.md", encoding="utf-8").read()
adlar = set(re.findall(r"[\w.-]+", metin))
for g in re.findall(r"([\w-]*?)(\d+)((?:/\d+)+)", metin):       # "lock_01/02/03" → lock_01, lock_02, lock_03
    for n in [g[1]] + g[2].strip("/").split("/"):
        adlar.add(g[0] + n)
eksik = []
dosyalar = sorted(p for p in glob.glob(f"{d}/kaynak/**/*", recursive=True) if p.rsplit(".", 1)[-1] in ("ogg", "mp3", "flac", "wav"))
for p in dosyalar:
    b = os.path.basename(p)
    kok = b.rsplit(".", 1)[0]
    if b not in adlar and kok not in adlar:
        eksik.append(b)
# yasak lisans: kayıt tablolarının "Lisans" hücrelerinde NC/ND/SA (elenenler bölümü hariç)
kayit = metin.split("## Değerlendirilip alınmayan")[0]
satirlar = [l for l in kayit.splitlines() if l.startswith("|")]
yasak = [l[:60] for l in satirlar if re.search(r"CC[ -]BY[ -](?:NC|ND|SA)|non-?commercial|no ?deriv", l, re.I)]
# F6: cue.json'daki (kurguya giren) her dosya bu kayıtta veya kanal kaydında (assets/LISANSLAR.md) olmalı
cue_eksik = []
if os.path.exists(f"{d}/cue.json"):
    import json
    kanal = open(os.path.join(d, "..", "..", "..", "assets", "LISANSLAR.md"), encoding="utf-8").read()
    c = json.load(open(f"{d}/cue.json"))
    for x in c["muzik"] + c["sfx"] + c.get("shorts", []):
        b = x["dosya"].split("/")[-1]
        if b not in metin + kanal and b.rsplit(".", 1)[0] not in metin + kanal:
            cue_eksik.append(b)
print(f"dosya: {len(dosyalar)} · kayıtsız: {len(eksik)} {eksik} · yasak lisans (kayıt bölümünde): {yasak} · cue kayıtsız: {cue_eksik}")
sys.exit(1 if eksik or yasak or cue_eksik else 0)
