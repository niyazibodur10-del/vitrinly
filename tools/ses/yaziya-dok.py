#!/usr/bin/env python3
"""Kelime zamanlı transkript (faster-whisper, CPU int8; yerel model önbelleği).

Kullanım:
  ~/.finansal-arac/venv/bin/python tools/ses/yaziya-dok.py <ses> <cikis.json> [small.en|medium.en]
  ~/.finansal-arac/venv/bin/python tools/ses/yaziya-dok.py --model small.en [--is 2] a.wav a.json b.wav b.json ...
Çıkış: {"text": ..., "words": [{"w","s","e","p"}]}; tek dosyada metin stdout'a, toplu modda dosya başına özet satırı.

TOPLU MOD (2026-10-28, uretim-muhendisi): model BİR KEZ yüklenir, tüm dosyalar sırayla/paralel çözülür.
  Neden: her çağrı modeli yeniden yükler (sıcak 3,4 sn, soğuk diskte 44 sn small / 136 sn medium; 1929'da F6 testleri,
  Shorts, final, sahne kesitleri ayrı ayrı çağrıldı). --is K (varsayılan 2): K iş parçacığı (num_workers=K,
  cpu_threads=nproc/K). Ölçüm 2026-10-28 (4 vCPU, small.en, çıktılar bayt bayt aynı): 3 dosya ayrı çağrı 43,7 sn →
  toplu --is 1 36,7 sn → toplu --is 2 26,7 sn; TEK 60 sn dosyada da cpu_threads 2 (22,3 sn) > 4 (29,1);
  CTranslate2 bu VM'de 2 iş parçacığında doyuyor. docs/uretim-kapasitesi.md §1. Transkripsiyon ayarları tek dosya moduyla aynı (beam 5, kelime zamanı,
  condition_on_previous_text=False) → aynı dosya için aynı çıktı.
Model yükleme önce yalnız yerel önbellekten (local_files_only) denenir; önbellek yoksa indirir.
Neden (2026-10-27): ağ/proxy yavaşken HF etag sorgusu bekletiyordu ve hata mesajsız çıkış "Whisper başarısız" diye
raporlanıyordu. Önbellek kurulum.sh ile dolduruluyor; SessionStart kancası model dosyalarını sayfa önbelleğine ısıtır.
"""
import argparse, json, os, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor

MODELLER = {"tiny.en", "base.en", "small.en", "medium.en", "small", "medium", "large-v3", "distil-large-v3"}


def model_yukle(ad, isci):
    from faster_whisper import WhisperModel
    ek = {"num_workers": isci, "cpu_threads": max(1, (os.cpu_count() or 4) // isci)}
    try:
        return WhisperModel(ad, device="cpu", compute_type="int8", local_files_only=True, **ek)
    except Exception as e:  # önbellekte yok → indir
        print(f"[yaziya-dok] yerel önbellekte yok ({type(e).__name__}); indiriliyor: {ad}", file=sys.stderr)
        return WhisperModel(ad, device="cpu", compute_type="int8", **ek)


def coz(m, giris, cikis):
    import numpy as np
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", giris, "-ac", "1", "-ar", "16000", "-f", "f32le", "-"], capture_output=True)
    if r.returncode != 0 or not r.stdout:
        raise RuntimeError(f"ffmpeg sesi çözemedi ({giris}): {r.stderr.decode(errors='replace').strip()[:300]}")
    audio = np.frombuffer(r.stdout, dtype=np.float32)
    segs, info = m.transcribe(audio, language="en", word_timestamps=True, beam_size=5, condition_on_previous_text=False)
    words, text = [], []
    for s in segs:
        text.append(s.text.strip())
        for w in s.words:
            words.append({"w": w.word.strip(), "s": round(w.start, 3), "e": round(w.end, 3), "p": round(w.probability, 3)})
    if not words:
        print(f"[yaziya-dok] UYARI: hiç kelime çıkmadı (sessiz/boş ses?): {giris}", file=sys.stderr)
    elif sum(w["p"] for w in words) / len(words) < 0.3:  # sessizlikte Whisper "You" gibi uydurur (p≈0,1)
        print(f"[yaziya-dok] UYARI: ortalama kelime güveni < 0,3 — sessiz/gürültülü ses veya halüsinasyon olabilir: {giris}", file=sys.stderr)
    with open(cikis, "w") as f:
        json.dump({"text": " ".join(text), "words": words}, f, indent=1)
    return " ".join(text), len(words), len(audio) / 16000


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", default=None)
    ap.add_argument("--is", dest="isci", type=int, default=2)
    ap.add_argument("dosyalar", nargs="+")
    a = ap.parse_args()
    d = a.dosyalar
    if a.model is None and len(d) == 3 and d[2] in MODELLER:  # eski çağrı biçimi: <ses> <cikis> <model>
        a.model, d = d[2], d[:2]
    model_adi = a.model or "small.en"
    if len(d) % 2:
        sys.exit("HATA: dosyalar <ses> <cikis.json> çiftleri halinde verilmeli")
    ciftler = list(zip(d[0::2], d[1::2]))
    for g, _ in ciftler:
        if not os.path.isfile(g):
            sys.exit(f"HATA: ses dosyası yok: {g}")
    t0 = time.time(); m = model_yukle(model_adi, a.isci); t1 = time.time()
    tek = len(ciftler) == 1
    def is_(c):
        s = time.time(); metin, n, sure = coz(m, *c)
        if tek:
            print(metin)
        else:
            print(f"[yaziya-dok] {c[0]} → {c[1]}: {n} kelime, {sure:.1f} sn ses, {time.time() - s:.1f} sn", file=sys.stderr)
    try:
        if a.isci > 1 and not tek:
            with ThreadPoolExecutor(a.isci) as ex:
                list(ex.map(is_, ciftler))
        else:
            for c in ciftler:
                is_(c)
    except RuntimeError as e:
        sys.exit(f"HATA: {e}")
    if not tek:
        print(f"[yaziya-dok] {len(ciftler)} dosya, model yükleme {t1 - t0:.1f} sn, toplam {time.time() - t0:.1f} sn", file=sys.stderr)


if __name__ == "__main__":
    main()
