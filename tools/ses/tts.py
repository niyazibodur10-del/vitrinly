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
- `--is K` (varsayılan 2; 2026-10-28, uretim-muhendisi): cümleler K süreçte paralel üretilir (her süreç torch iş
  parçacığı = nproc/K, model her süreçte bir kez yüklenir); sıra ve duraklamalar aynı. Ölçüm (4 vCPU, 16 cümle, 55,6 sn ses,
  sıcak önbellek): --is 1 43,4 sn · --is 2 38,2 sn (SEÇİLDİ, −%12) · --is 4 41,1 sn. Bellek süreç başına ~1,4 GB.
  NOT: Kokoro deterministik DEĞİL (aynı ayarla iki --is 1 çalıştırması örnek düzeyinde farklı, süre ±2 ms/cümle) →
  paralel çıktı farkı paralellikten değil; anlatım bir kez üretilip kilitlenir, yeniden üretim git'teki m4a'dan yapılır.
Kurulum: pip install kokoro soundfile  (misaki G2P; sözlük dışı kelimeler için espeakng_loader paketiyle gelen espeak-ng)
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


_PIPE = None


def _isci_baslat(ses, esz):
    global _PIPE
    import torch
    torch.set_num_threads(esz)
    from kokoro import KPipeline
    _PIPE = KPipeline(lang_code=ses[0], repo_id="hexgrad/Kokoro-82M")


def _uret(pipe, c, ses, hiz):
    ses_parca = [x.numpy() if hasattr(x, "numpy") else np.asarray(x)
                 for _, _, x in pipe(c, voice=ses, speed=hiz, split_pattern=None)]
    return np.concatenate(ses_parca).astype(np.float32)


def _isci_uret(arg):
    return _uret(_PIPE, *arg)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("metin"); ap.add_argument("cikis")
    ap.add_argument("--ses", default="am_michael")
    ap.add_argument("--hiz", type=float, default=0.95)
    ap.add_argument("--cumle", type=float, default=0.30)
    ap.add_argument("--soru", type=float, default=0.40)
    ap.add_argument("--uc-nokta", type=float, default=0.55)
    ap.add_argument("--paragraf", type=float, default=0.65)
    ap.add_argument("--is", dest="isci", type=int, default=2)
    a = ap.parse_args()

    ses = a.ses.replace("+", ",")  # kokoro virgülle verilen sesleri ortalar
    cumleler = cumlelere_bol(open(a.metin, encoding="utf-8").read())
    if a.isci > 1:
        import multiprocessing as mp, os
        esz = max(1, (os.cpu_count() or 4) // a.isci)
        with mp.get_context("spawn").Pool(a.isci, initializer=_isci_baslat, initargs=(ses, esz)) as havuz:
            sesler = havuz.map(_isci_uret, [(c, ses, a.hiz) for c, _ in cumleler], chunksize=1)
    else:
        from kokoro import KPipeline
        pipe = KPipeline(lang_code=ses[0], repo_id="hexgrad/Kokoro-82M")
        sesler = [_uret(pipe, c, ses, a.hiz) for c, _ in cumleler]
    bosluk = {"cumle": a.cumle, "soru": a.soru, "uc_nokta": a.uc_nokta, "paragraf": a.paragraf}

    parcalar, zaman, t = [], [], 0.0
    for (c, tur), y in zip(cumleler, sesler):
        # baş/son sessizliği kırp (-50 dB); başta 30 ms, sonda 50 ms pay bırak
        # (5 ms pay "No ..." gibi nazal/yumuşak başlangıçları yiyordu: Whisper "news"/"videos" duydu)
        nz = np.where(np.abs(y) > 10 ** (-50 / 20))[0]
        if len(nz):
            y = y[max(nz[0] - 720, 0): nz[-1] + 1200]
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
