#!/usr/bin/env python3
"""Anlatıcı seslendirmesi (Kokoro-82M, Apache-2.0, yerel; para/ağ gerektirmez).

Kullanım:
  tts.py <metin.txt> <cikis.wav> [--ses am_michael] [--hiz 0.95] [--cumle 0.30] [--paragraf 0.65]
         [--soru 0.40] [--uc-nokta 0.55]

- Metin cümlelere bölünür, her cümle ayrı üretilir, aralarına doğal duraklama eklenir
  (Kokoro'nun kendi duraklamaları kısa; tek parça üretimde ~200+ kelime/dk çıkıyor).
- `--ses` iki sesin karışımı için `am_michael+am_puck` biçimini kabul eder (vektör ortalaması).
- Çıkış: 24 kHz mono float WAV (ham) + aynı adla `.zaman.json` (cümle başlangıç/bitiş).
  Yayın seviyesine getirmek için: tools/ses/tts-son.sh <ham.wav> <cikis.wav>  (48 kHz, -14 LUFS, TP -1)
Kurulum: pip install kokoro soundfile  (espeak-ng gerekmez; misaki + en_core_web_sm yeterli)
"""
import argparse, json, re
import numpy as np, soundfile as sf

SR = 24000


def cumlelere_bol(metin):
    """Paragrafları (boş satır/yeni satır) ve cümleleri ayırır; her cümleden sonra duraklama türünü döndürür."""
    parcalar = []
    paragraflar = [p.strip() for p in re.split(r"\n+", metin) if p.strip()]
    for pi, p in enumerate(paragraflar):
        cumleler = re.findall(r".+?(?:\.\.\.|[.!?…]+|$)(?=\s+|$)", p)
        cumleler = [c.strip() for c in cumleler if c.strip()]
        for ci, c in enumerate(cumleler):
            son = ci == len(cumleler) - 1
            if son and pi < len(paragraflar) - 1:
                tur = "paragraf"
            elif c.endswith("...") or c.endswith("…"):
                tur = "uc_nokta"
            elif c.endswith("?"):
                tur = "soru"
            else:
                tur = "cumle"
            parcalar.append((c, tur))
    return parcalar


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("metin"); ap.add_argument("cikis")
    ap.add_argument("--ses", default="am_michael")
    ap.add_argument("--hiz", type=float, default=0.95)
    ap.add_argument("--cumle", type=float, default=0.30)
    ap.add_argument("--soru", type=float, default=0.40)
    ap.add_argument("--uc-nokta", type=float, default=0.55)
    ap.add_argument("--paragraf", type=float, default=0.65)
    a = ap.parse_args()

    from kokoro import KPipeline
    ses = a.ses.replace("+", ",")  # kokoro virgülle verilen sesleri ortalar
    pipe = KPipeline(lang_code=ses[0], repo_id="hexgrad/Kokoro-82M")
    bosluk = {"cumle": a.cumle, "soru": a.soru, "uc_nokta": a.uc_nokta, "paragraf": a.paragraf}

    parcalar, zaman, t = [], [], 0.0
    for c, tur in cumlelere_bol(open(a.metin, encoding="utf-8").read()):
        ses_parca = [x.numpy() if hasattr(x, "numpy") else np.asarray(x)
                     for _, _, x in pipe(c, voice=ses, speed=a.hiz, split_pattern=None)]
        y = np.concatenate(ses_parca).astype(np.float32)
        # baş/son sessizliği kırp (-50 dB), 5 ms yumuşak geçiş
        nz = np.where(np.abs(y) > 10 ** (-50 / 20))[0]
        if len(nz):
            y = y[max(nz[0] - 120, 0): nz[-1] + 240]
        f = min(120, len(y) // 4)
        y[:f] *= np.linspace(0, 1, f); y[-f:] *= np.linspace(1, 0, f)
        zaman.append({"metin": c, "bas": round(t, 3), "son": round(t + len(y) / SR, 3)})
        parcalar += [y, np.zeros(int(bosluk[tur] * SR), np.float32)]
        t += len(y) / SR + bosluk[tur]
    sf.write(a.cikis, np.concatenate(parcalar[:-1]), SR, subtype="FLOAT")
    json.dump({"ses": a.ses, "hiz": a.hiz, "cumleler": zaman},
              open(re.sub(r"\.wav$", "", a.cikis) + ".zaman.json", "w"), indent=1, ensure_ascii=False)
    print(f"{a.ses} hiz={a.hiz}: {t:.1f} sn, {len(zaman)} cümle")


if __name__ == "__main__":
    main()
