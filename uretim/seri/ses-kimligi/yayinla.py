#!/usr/bin/env python3
"""Seçilen adayları şablon klasörüne yazar (16-bit FLAC, 48 kHz stereo). Önce: uret.py aday && earshot-uret.sh aday.
Kullanım: ~/.finansal-arac/earshot-venv/bin/python yayinla.py   → video/public/seri/ortak/{muzik,sfx}/ + sha256 listesi"""
import hashlib, os
import numpy as np, soundfile as sf
K = os.path.dirname(os.path.abspath(__file__)); A = f"{K}/aday"; P = os.path.abspath(f"{K}/../../../video/public/seri/ortak")
MUZIK = {"jingle-flip": "jingle-a", "dongu-strut-112": "dongu-a", "dongu-hustle-124": "dongu-b", "gerilim-saat-96": "gerilim-a"}
SFX = {"tahta-kalem-kisa": "sfx-tahta-kisa", "tahta-kalem-uzun": "sfx-tahta-uzun", "plak-cizik": "sfx-plak-cizik",
       "kutu-tikirti": "sfx-kutu-tikirti", "tik": "es-tik", "swipe": "es-swipe", "ding": "es-ding",
       "pop-yumusak": "es-pop-yumusak", "whoosh-kart": "es-whoosh-kart", "gerilim-dusus": "es-gerilim-dusus"}


def oku(ad):
    y, sr = sf.read(f"{A}/{ad}.wav", always_2d=True, dtype="float64"); assert sr == 48000
    return y if y.shape[1] == 2 else np.repeat(y, 2, 1)


def yaz(y, yol):
    y = y * (10 ** (-1 / 20) / np.max(np.abs(y)))            # tepe −1 dBFS (numpy, float girdi kırpılmaz)
    sf.write(yol, y.astype(np.float32), 48000, subtype="PCM_16", format="FLAC")
    return hashlib.sha256(open(yol, "rb").read()).hexdigest()[:12]


os.makedirs(f"{P}/muzik", exist_ok=True); os.makedirs(f"{P}/sfx", exist_ok=True)
out = []
for hedef, kaynak in MUZIK.items():
    out.append(f"muzik/{hedef}.flac\t{yaz(oku(kaynak), f'{P}/muzik/{hedef}.flac')}\t← {kaynak}")
for hedef, kaynak in SFX.items():
    out.append(f"sfx/{hedef}.flac\t{yaz(oku(kaynak), f'{P}/sfx/{hedef}.flac')}\t← {kaynak}")
# tezgâha çarpma: masa vuruşu + gövde darbesi katmanı (punch 25 ms geç → masa tepesi ile aynı anda)
d, p = oku("es-carpma-desk"), oku("es-carpma-punch")
n = max(len(d), len(p) + 1200); y = np.zeros((n, 2)); y[:len(d)] += d; y[:len(p)] += 0.55 * p[:n]
out.append(f"sfx/tezgah-carpma.flac\t{yaz(y, f'{P}/sfx/tezgah-carpma.flac')}\t← es-carpma-desk + 0.55·es-carpma-punch")
open(f"{K}/sha256.txt", "w").write("\n".join(out) + "\n"); print("\n".join(out))
