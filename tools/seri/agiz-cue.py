#!/usr/bin/env python3
"""Flip By Vote — konuşmacı bazlı ağız şekli zaman çizelgesi (Rhubarb A–H/X) — şablonun "yama" ağız yolu için.

Kullanım:
  python3 -I tools/seri/agiz-cue.py <diyalog.wav> <satirlar.json> <agiz.json> [--is 2] [--pay 0.05]
  Girdi: ses-yonetmeni biçimi (satirlar.json: satirlar[] = konusmaci, bas, bitis, metin).
  Çıktı: {"kaynak": {...sha}, "jake": [{"bas","bitis","sekil"}], "mike": [...]} (saniye, wav başına göre; satır dışı = X).
Yöntem: her satır ±pay ile ffmpeg'le kesilir, Rhubarb (PocketSphinx + --dialogFile satır metni) ayrı koşar, ofset eklenir,
satır sınırına kırpılır. Seçim (2026-11-10, uretim-muhendisi): satır başına Rhubarb (konuşmacı ayrımı satır verisinden gelir,
çakışma yok) > tüm wav'a tek Rhubarb + satırla bölme (cümle sınırında ağız diğer konuşmacıya taşar, elendi) > phonetic
tanıyıcı (İngilizcede daha az isabetli, elendi). Rhubarb deterministik değil → çıktı bir kez üretilip git'e girer.
Çıkış kodu: 0 tamam, 1 Rhubarb hatası, 2 kullanım hatası.
"""
import argparse, hashlib, json, os, subprocess, sys, tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

RH = Path(os.environ.get("ARAC_DIZINI", Path.home() / ".finansal-arac")) / "rhubarb/build/rhubarb/rhubarb"


def sha12(p):
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()[:12]


def satir_isle(arg):
    i, s, wav, td, pay, esz = arg
    bas = max(0.0, s["bas"] - pay); bit = s["bitis"] + pay
    parca = os.path.join(td, f"s{i}.wav"); metin = os.path.join(td, f"s{i}.txt")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{bas:.3f}", "-to", f"{bit:.3f}", "-i", wav,
                    "-ac", "1", "-ar", "16000", "-c:a", "pcm_s16le", parca], check=True, stdin=subprocess.DEVNULL)
    Path(metin).write_text(s["metin"], encoding="utf-8")
    r = subprocess.run([str(RH), "-f", "json", "--extendedShapes", "GHX", "--threads", str(esz), "-q",
                        "--dialogFile", metin, parca], capture_output=True, text=True, stdin=subprocess.DEVNULL)
    if r.returncode != 0:
        raise RuntimeError(f"satır {i}: {r.stderr.strip()[:300]}")
    cues = []
    for c in json.loads(r.stdout)["mouthCues"]:
        cb = max(s["bas"], bas + c["start"]); cs = min(s["bitis"], bas + c["end"])
        if cs - cb > 1e-3:
            cues.append({"bas": round(cb, 3), "bitis": round(cs, 3), "sekil": c["value"]})
    return s["konusmaci"], cues


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("wav"); ap.add_argument("satirlar"); ap.add_argument("cikis")
    ap.add_argument("--is", dest="isci", type=int, default=2); ap.add_argument("--pay", type=float, default=0.05)
    a = ap.parse_args()
    if not RH.exists():
        print(f"HATA: Rhubarb yok ({RH}); önce tools/kurulum.sh", file=sys.stderr); sys.exit(2)
    try:
        sat = json.load(open(a.satirlar, encoding="utf-8"))["satirlar"]
    except (OSError, KeyError, ValueError) as e:
        print(f"HATA: satirlar.json okunamadı: {e}", file=sys.stderr); sys.exit(2)
    esz = max(1, (os.cpu_count() or 4) // a.isci)
    sonuc = {"kaynak": {"wav": sha12(a.wav), "satirlar": sha12(a.satirlar)}}
    with tempfile.TemporaryDirectory() as td, ThreadPoolExecutor(a.isci) as ex:
        try:
            for k, cues in ex.map(satir_isle, [(i, s, a.wav, td, a.pay, esz) for i, s in enumerate(sat)]):
                sonuc.setdefault(k, []).extend(cues)
        except (RuntimeError, subprocess.CalledProcessError) as e:
            print(f"HATA: {e}", file=sys.stderr); sys.exit(1)
    for k in list(sonuc):
        if k != "kaynak":
            sonuc[k].sort(key=lambda c: c["bas"])
    json.dump(sonuc, open(a.cikis, "w", encoding="utf-8"), indent=0, ensure_ascii=False)
    print(" ".join(f"{k}={len(v)} cue" for k, v in sonuc.items() if k != "kaynak"))


if __name__ == "__main__":
    main()
