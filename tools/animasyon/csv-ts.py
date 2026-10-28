#!/usr/bin/env python3
"""Doğrulanmış CSV tablolarını Remotion TS sabitlerine çevirir (grafiklere elle rakam yazılmaz).

Kullanım: python3 -I tools/animasyon/csv-ts.py --cikis video/src/<kisa>/veri-grafik.ts \
            AD=dosya.csv[:sutun1,sutun2][@filtre_sutun=bas..son] ...
  Her AD için export const AD = [{...}] (sayısal görünen değerler sayıya çevrilir, boş hücreli satır atlanır).
  Örnek: CPI29=03-metin/veri/cpi.csv:observation_date,CPIAUCNS@observation_date=1929-09..1933-03
  Filtre metin karşılaştırmasıdır (ISO tarihlerde doğru çalışır). Kaynak dosya yolları TS başlığına yazılır.
Genelleştirildi 2026-10-28 (uretim-muhendisi): 1929 grafik-veri.py deseni (videoya özel dönüşümler — endeks, ay
ondalığı — gerekiyorsa çıktıyı TS tarafında veya video betiğinde yapın).
"""
import argparse, csv, json, os, re


def sayi(v):
    v = v.strip()
    return (int(v) if re.fullmatch(r"-?\d+", v) else float(v)) if re.fullmatch(r"-?\d+(\.\d+)?", v) else v


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--cikis", required=True); ap.add_argument("tablolar", nargs="+")
    a = ap.parse_args(); satirlar, kaynak = [], []
    for t in a.tablolar:
        m = re.fullmatch(r"(\w+)=([^:@]+)(?::([^@]+))?(?:@(\w+)=([^.]*)\.\.(.*))?", t)
        if not m:
            raise SystemExit(f"HATA: biçim AD=dosya.csv[:sutunlar][@sutun=bas..son]: {t}")
        ad, dosya, sut, fs, fb, fe = m.groups()
        out = []
        if not os.path.isfile(dosya):
            raise SystemExit(f"HATA: CSV yok: {dosya}")
        for r in csv.DictReader(open(dosya, encoding="utf-8")):
            if fs and not (fb <= r[fs] <= fe):
                continue
            secili = {k: r[k] for k in (sut.split(",") if sut else r.keys())}
            if any(not str(v).strip() for v in secili.values()):
                continue
            out.append({k: sayi(v) for k, v in secili.items()})
        satirlar.append(f"export const {ad} = {json.dumps(out, ensure_ascii=False)};"); kaynak.append(f"{ad}←{dosya}")
        print(ad, len(out), "satır")
    open(a.cikis, "w").write("// Otomatik: tools/animasyon/csv-ts.py (" + "; ".join(kaynak) + ")\n" + "\n".join(satirlar) + "\n")


if __name__ == "__main__":
    main()
