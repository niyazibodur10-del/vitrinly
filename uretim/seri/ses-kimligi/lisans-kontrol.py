#!/usr/bin/env python3
"""Flip By Vote lisans kapısı: video/public/seri/ortak altındaki her ses dosyası ve her bolum-*/ses-cue.json'daki her dosya
uretim/seri/lisans-kaydi.md'de mi; kayıt tablolarında yasak lisans (CC BY, NC/ND/SA, platform kütüphanesi) var mı. Çıkış 0 = GEÇTİ.
Negatif test: --ek <dosya_adı> (sahte kayıtsız dosya ekler → çıkış 1 beklenir)."""
import glob, json, os, re, sys
K = os.path.dirname(os.path.abspath(__file__)); SERI = os.path.dirname(K); R = os.path.abspath(f"{SERI}/../..")
metin = open(f"{SERI}/lisans-kaydi.md", encoding="utf-8").read()
kayit = metin.split("## Değerlendirilip alınmayan")[0]
adlar = set(re.findall(r"`([^`]+\.(?:flac|wav|ogg|mp3))`", kayit))
dosyalar = sorted({os.path.basename(p) for p in glob.glob(f"{R}/video/public/seri/ortak/**/*", recursive=True)
                   if p.rsplit(".", 1)[-1] in ("flac", "wav", "ogg", "mp3")})
for c in glob.glob(f"{SERI}/bolum-*/ses-cue.json"):
    j = json.load(open(c))
    dosyalar += [os.path.basename(x["dosya"]) for x in j["muzik"]["parcalar"] + j["sfx"]]
if "--ek" in sys.argv:
    dosyalar.append(sys.argv[sys.argv.index("--ek") + 1])
eksik = sorted({d for d in dosyalar if d not in adlar})
satirlar = [l for l in kayit.splitlines() if l.startswith("| `")]
yasak = [l[:70] for l in satirlar if re.search(r"CC[ -]BY(?![ -]?\w*0)|non-?commercial|no ?deriv|share ?alike|Audio Library|TikTok|Instagram", l.split("|")[4], re.I)]
print(json.dumps({"dosya": len(set(dosyalar)), "kayitli": len(adlar), "eksik": eksik, "yasak_lisans": yasak}, ensure_ascii=False))
sys.exit(1 if eksik or yasak else 0)
