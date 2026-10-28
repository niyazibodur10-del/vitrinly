#!/usr/bin/env python3
"""Rhubarb girdileri: anlatım wav + kilitli metin + sahne zamanları -> <cikis>/
  anlatim.txt          tüm anlatımın düz metni (referans metin)
  Sxx.wav / Sxx.txt    sahne başına 16 kHz mono PCM16 kesit + o sahnenin düz metni (--dialogFile)
  sahneler.json        sahne -> kesit başlangıcı (sn, anlatım ekseninde): Rhubarb çıktısındaki zamanlara bu ofset eklenir
                       (tools/senkron-testi.py --ofset ile aynı değer)
Kesitler sahne-zamanlari.json bas/bitis (sahne arası sessizlik öndeki sahnede) → uç uca, boşluk/çakışma yok.

Kullanım: python3 -I tools/ses/rhubarb-hazirla.py --dizin uretim/<video>/04-ses [--sahne S01,S04] [--cikis DIZIN]
  Girdi adları (dizine göre, ayrı ayrı değiştirilebilir): --ses anlatim.wav --zaman anlatim-ham.zaman.json
  --sahneler sahne-zamanlari.json --referans referans-metni.txt ; --cikis varsayılan <dizin>/rhubarb
Genelleştirildi 2026-10-27 (uretim-muhendisi): kaynak uretim/2026-10-26-1929-1000-dolar/04-ses/rhubarb-hazirla.py
(aynı girdiyle bayt bayt aynı .txt/.wav/.json; test: tools/ses/test_ses_hizalama.py).
"""
import argparse, json, os, re, subprocess

temiz = lambda m: re.sub(r"\[([^\]]+)\]\(/[^)]*/\)", r"\1", m)


def main():
    ap = argparse.ArgumentParser(description="Rhubarb sahne kesitleri + diyalog metinleri")
    ap.add_argument("--dizin", default=".")
    ap.add_argument("--ses", default="anlatim.wav"); ap.add_argument("--zaman", default="anlatim-ham.zaman.json")
    ap.add_argument("--sahneler", default="sahne-zamanlari.json"); ap.add_argument("--referans", default="referans-metni.txt")
    ap.add_argument("--cikis"); ap.add_argument("--sahne", help="yalnız bu sahneler, ör. S01,S04")
    a = ap.parse_args()
    yol = lambda p: p if os.path.isabs(p) else os.path.join(a.dizin, p)
    O = a.cikis or os.path.join(a.dizin, "rhubarb"); os.makedirs(O, exist_ok=True)
    C = json.load(open(yol(a.zaman)))["cumleler"]
    SZ = json.load(open(yol(a.sahneler)))["sahneler"]
    if a.sahne:
        iste = set(a.sahne.split(",")); bilinmeyen = iste - {s["sahne"] for s in SZ}
        if bilinmeyen:
            raise SystemExit(f"HATA: bilinmeyen sahne: {sorted(bilinmeyen)}")
        SZ = [s for s in SZ if s["sahne"] in iste]
    open(os.path.join(O, "anlatim.txt"), "w").write(open(yol(a.referans)).read())
    kayit = []
    for s in SZ:
        metin = " ".join(temiz(C[i]["metin"]) for i in range(s["cumle_ilk"], s["cumle_son"] + 1))
        open(os.path.join(O, f"{s['sahne']}.txt"), "w").write(metin + "\n")
        subprocess.run(["ffmpeg", "-hide_banner", "-v", "error", "-y", "-ss", str(s["bas"]), "-to", str(s["bitis"]), "-i", yol(a.ses),
                        "-ar", "16000", "-ac", "1", "-c:a", "pcm_s16le", os.path.join(O, f"{s['sahne']}.wav")], check=True)
        kayit.append({"sahne": s["sahne"], "ofset_sn": s["bas"], "sure_sn": round(s["bitis"] - s["bas"], 3), "wav": f"{s['sahne']}.wav", "metin": f"{s['sahne']}.txt"})
    json.dump({"kaynak": f"{os.path.basename(a.ses)} -> 16 kHz PCM16 kesitler", "komut": "rhubarb -r pocketSphinx --dialogFile Sxx.txt -f json -o Sxx.json Sxx.wav", "sahneler": kayit},
              open(os.path.join(O, "sahneler.json"), "w"), ensure_ascii=False, indent=1)
    print(f"{len(kayit)} sahne kesiti, toplam {sum(k['sure_sn'] for k in kayit):.2f} sn -> {O}")


if __name__ == "__main__":
    main()
