#!/usr/bin/env python3
"""Tüm sahneler (+ ek kayıtlar) için Rhubarb (PocketSphinx, --dialogFile) + sessizlik kapısı, paralel.

Kullanım:
  python3 -I tools/animasyon/rhubarb-toplu.py --girdi uretim/<video>/04-ses/rhubarb/sahneler.json \
      --cikis uretim/<video>/07-animasyon/rhubarb [--ek ad:ses.wav:metin.txt ...] [--is 2] [--yeniden]
  Girdi: tools/ses/rhubarb-hazirla.py çıktısı (sahneler.json: sahne, wav, metin, ofset_sn).
  Çıktı: <cikis>/sahne/<ad>.json (ham Rhubarb), <ad>-kapili.json (≥100 ms sessizlik → X), <cikis>/tum-kapili.json
         (yalnız sahneler, anlatım zamanında birleşik). Ham çıktı varsa ve --yeniden yoksa Rhubarb atlanır (önbellek).
Genelleştirildi 2026-10-28 (uretim-muhendisi): kaynak uretim/2026-10-26-1929-1000-dolar/07-animasyon/rhubarb-tum.py
(aynı girdiyle aynı çıktı; test: aşağıdaki ölçüm). --is K: K sahne aynı anda, her biri --threads nproc/K.
Ölçüm ve seçim (paralel sahne vs Rhubarb'ın kendi --threads'i): docs/uretim-kapasitesi.md §1.
"""
import argparse, json, os, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent))
from sessizlik_kapisi import sessizlik, uygula  # noqa: E402

RH = Path(os.environ.get("ARAC_DIZINI", Path.home() / ".finansal-arac")) / "rhubarb/build/rhubarb/rhubarb"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--girdi", required=True); ap.add_argument("--cikis", required=True)
    ap.add_argument("--ek", action="append", default=[], help="ad:ses.wav:metin.txt (ofsetsiz, tum-kapili'ye girmez)")
    ap.add_argument("--is", dest="isci", type=int, default=2); ap.add_argument("--yeniden", action="store_true")
    a = ap.parse_args()
    if not RH.exists():
        sys.exit(f"HATA: Rhubarb yok ({RH}) → tools/kurulum.sh")
    g = Path(a.girdi); R = g.parent; O = Path(a.cikis) / "sahne"; O.mkdir(parents=True, exist_ok=True)
    isler = [(s["sahne"], R / s["wav"], R / s["metin"], s["ofset_sn"]) for s in json.load(open(g))["sahneler"]]
    for e in a.ek:
        ad, wav, txt = e.split(":")
        isler.append((ad, Path(wav), Path(txt), None))
    esz = max(1, (os.cpu_count() or 4) // a.isci)

    def calis(is_):
        ad, wav, txt, ofs = is_
        ham = O / f"{ad}.json"; t = time.time()
        if a.yeniden or not ham.exists():
            subprocess.run([str(RH), "-q", "-r", "pocketSphinx", "-f", "json", "--threads", str(esz), "--dialogFile", str(txt),
                            "-o", str(ham), str(wav)], check=True, capture_output=True)
        c = uygula(json.load(open(ham))["mouthCues"], sessizlik(str(wav)))
        json.dump({"mouthCues": c}, open(O / f"{ad}-kapili.json", "w"))
        print(f"{ad} {len(c)} ipucu {time.time() - t:.1f} sn", flush=True)
        return ad, ofs, c

    t0 = time.time()
    with ThreadPoolExecutor(a.isci) as ex:
        sonuc = list(ex.map(calis, isler))
    tum = []
    for ad, ofs, c in sonuc:
        if ofs is None:
            continue
        tum += [{"start": round(x["start"] + ofs, 3), "end": round(x["end"] + ofs, 3), "value": x["value"]} for x in c]
    json.dump({"mouthCues": tum}, open(Path(a.cikis) / "tum-kapili.json", "w"))
    print(f"toplam ipucu {len(tum)}, {len(isler)} iş, {time.time() - t0:.1f} sn (is={a.isci}, threads={esz})")


if __name__ == "__main__":
    main()
