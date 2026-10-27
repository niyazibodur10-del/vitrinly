#!/usr/bin/env python3
"""Cümle tek başına Whisper testi: tts.py ham wav + .zaman.json -> her cümle ayrı çözülür (tam dosya çözümündeki
bağlam yanlılığını/uydurmaları gerçek telaffuz hatasından ayırmak için; ses-yonetmeni dersi 2026-10-27).

Kullanım: ~/.finansal-arac/venv/bin/python tools/ses/cumle-whisper.py <ham.wav> <ham.zaman.json>
            [--cumleler 3,10-12] [--model small.en] [--json cikti.json]
Çıkış: stdout'ta cümle başına "metin -> kelime(olasılık) ..."; --json ile {"cumleler":[{i,metin,whisper,kelimeler:[{w,p}]}]}.
Ses her örnekleme hızında kabul edilir (16 kHz'e doğrusal ara değerleme; 24 kHz'te eski 04-ses/cumle-whisper.py ile
birebir aynı girdi). Model yerelden (local_files_only; ağ beklemesi yok). İlk çağrı soğuk önbellekte ~40 sn sürebilir.
Genelleştirildi 2026-10-27 (uretim-muhendisi): kaynak uretim/2026-10-26-1929-1000-dolar/04-ses/cumle-whisper.py.
"""
import argparse, json, sys


def secim(metin, n):
    if not metin:
        return list(range(n))
    out = []
    for p in metin.split(","):
        a, _, b = p.partition("-")
        out += list(range(int(a), int(b or a) + 1))
    bad = [i for i in out if not 0 <= i < n]
    if bad:
        sys.exit(f"HATA: cümle indeksi aralık dışı (0..{n - 1}): {bad}")
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("wav"); ap.add_argument("zaman_json")
    ap.add_argument("--cumleler", help="ör. 3,10-12 (0 tabanlı; varsayılan hepsi)")
    ap.add_argument("--model", default="small.en")
    ap.add_argument("--json", help="sonuçları JSON'a da yaz")
    a = ap.parse_args()
    import numpy as np, soundfile as sf
    from faster_whisper import WhisperModel
    y, sr = sf.read(a.wav)
    if y.ndim > 1:
        y = y.mean(axis=1)
    C = json.load(open(a.zaman_json))["cumleler"]
    m = WhisperModel(a.model, device="cpu", compute_type="int8", local_files_only=True)
    sonuc = []
    for i in secim(a.cumleler, len(C)):
        c = C[i]
        seg = y[int(c["bas"] * sr):int(c["son"] * sr)]
        x = np.interp(np.arange(0, len(seg), sr / 16000), np.arange(len(seg)), seg).astype(np.float32)
        s, _ = m.transcribe(x, language="en", word_timestamps=True, beam_size=5)
        ws = [w for q in s for w in q.words]
        print(f"{c['metin'][:60]!r:64} -> {' '.join(w.word.strip() + '(' + format(w.probability, '.2f') + ')' for w in ws)}", flush=True)
        sonuc.append({"i": i, "metin": c["metin"], "whisper": "".join(w.word for w in ws).strip(),
                      "kelimeler": [{"w": w.word.strip(), "p": round(w.probability, 3)} for w in ws]})
    if a.json:
        json.dump({"model": a.model, "cumleler": sonuc}, open(a.json, "w"), ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
