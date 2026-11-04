#!/usr/bin/env python3
"""Viralite puanlama betiği (model v0.1). Yalnızca standart kütüphane.

Ağırlıklar ve bonus/ceza kuralları YALNIZCA bu dosyada tanımlıdır.
`docs/viralite-modeli.md` tablosu bunlarla tutarlı olmalı; `--dokuman` ile denetlenir.

Kullanım:
  python3 tools/viralite.py tools/ornek-senaryolar.json
  python3 tools/viralite.py senaryolar.csv
  python3 tools/viralite.py --dokuman docs/viralite-modeli.md   # tablo ile betik aynı mı?

Girdi alanları (JSON: liste ya da {"senaryolar": [...]}; CSV: aynı adlı sütunlar):
  id, baslik,
  merak, talep, hook, kisisel, zamanlama, hikaye, gorsel, raf   (1–10)
  seri                  true/false  bağımsız izlenebilir ≥2 bölüme bölünebiliyor mu
  somut_ozne            true/false  başlıkta kişi / ülke / şehir / nesne / kurum var mı
  rakip_benzerlik       yok | benzer_aci | dogrudan_ceviri
  ana_iddia_dogrulandi  true/false  false ise senaryo elenir (puanı yine gösterilir)
"""
import argparse
import csv
import json
import re
import sys
from decimal import Decimal, ROUND_HALF_UP

MODEL_SURUMU = "v0.1"

# ---- Tek kaynak: ağırlıklar (anahtar, doküman adı, ağırlık) ----
OLCUTLER = [
    ("merak", "Merak boşluğu", Decimal("0.20")),
    ("talep", "Kanıtlı talep", Decimal("0.15")),
    ("hook", "Hook gücü", Decimal("0.10")),
    ("kisisel", "Kişisel bağ", Decimal("0.15")),
    ("zamanlama", "Zamanlama", Decimal("0.10")),
    ("hikaye", "Hikâye gerilimi", Decimal("0.15")),
    ("gorsel", "Görselleştirilebilirlik", Decimal("0.10")),
    ("raf", "Raf ömrü", Decimal("0.05")),
]
AGIRLIK = {k: w for k, _, w in OLCUTLER}

# ---- Tek kaynak: bonus / ceza kuralları ----
MERAK_TAVANI_SOMUT_OZNE_YOK = Decimal("6")   # merak puanı tavanı (ağırlıktan önce)
SERI_BONUSU = Decimal("0.3")                  # toplama eklenir
RAKIP_CEZASI = {                              # toplamdan düşülür, yalnız en ağır seviye
    "yok": Decimal("0"),
    "benzer_aci": Decimal("1.5"),
    "dogrudan_ceviri": Decimal("2.0"),
}
ALT, UST = Decimal("0"), Decimal("10")        # nihai puan bu aralığa kırpılır

assert sum(AGIRLIK.values()) == Decimal("1.00"), "Ağırlık toplamı 1.00 olmalı"
assert len(AGIRLIK) == len(OLCUTLER), "Yinelenen ölçüt anahtarı"

IKI = Decimal("0.01")


def _bool(v, alan, sid):
    if isinstance(v, bool):
        return v
    s = str(v).strip().lower()
    if s in ("true", "1", "evet", "e", "yes"):
        return True
    if s in ("false", "0", "hayir", "hayır", "h", "no", ""):
        return False
    raise ValueError(f"{sid}: '{alan}' true/false olmalı, gelen: {v!r}")


def _puan(v, alan, sid):
    try:
        d = Decimal(str(v).strip())
    except Exception:
        raise ValueError(f"{sid}: '{alan}' sayı olmalı, gelen: {v!r}")
    if not (Decimal(1) <= d <= Decimal(10)):
        raise ValueError(f"{sid}: '{alan}' 1–10 aralığında olmalı, gelen: {d}")
    return d


def oku(yol):
    if yol.lower().endswith(".csv"):
        with open(yol, encoding="utf-8", newline="") as f:
            return list(csv.DictReader(f))
    with open(yol, encoding="utf-8") as f:
        veri = json.load(f)
    return veri["senaryolar"] if isinstance(veri, dict) else veri


def puanla(s):
    sid = str(s.get("id", "?"))
    p = {k: _puan(s.get(k), k, sid) for k in AGIRLIK}
    somut = _bool(s.get("somut_ozne", True), "somut_ozne", sid)
    seri = _bool(s.get("seri", False), "seri", sid)
    dogru = _bool(s.get("ana_iddia_dogrulandi", True), "ana_iddia_dogrulandi", sid)
    benz = str(s.get("rakip_benzerlik", "yok")).strip() or "yok"
    if benz not in RAKIP_CEZASI:
        raise ValueError(f"{sid}: rakip_benzerlik {sorted(RAKIP_CEZASI)} olmalı, gelen: {benz!r}")

    notlar = []
    if not somut and p["merak"] > MERAK_TAVANI_SOMUT_OZNE_YOK:
        notlar.append(f"merak {p['merak']}→{MERAK_TAVANI_SOMUT_OZNE_YOK} (somut özne yok)")
        p["merak"] = MERAK_TAVANI_SOMUT_OZNE_YOK

    agirlikli = sum(p[k] * AGIRLIK[k] for k in AGIRLIK)
    bonus = SERI_BONUSU if seri else Decimal(0)
    ceza = RAKIP_CEZASI[benz]
    if bonus:
        notlar.append(f"seri +{SERI_BONUSU}")
    if ceza:
        notlar.append(f"{benz} −{ceza}")
    nihai = min(UST, max(ALT, agirlikli + bonus - ceza))
    if not dogru:
        notlar.append("ELENDİ: ana iddia doğrulanamadı")
    return {
        "id": sid,
        "baslik": s.get("baslik", ""),
        "agirlikli": agirlikli.quantize(IKI, ROUND_HALF_UP),
        "bonus": bonus.quantize(IKI),
        "ceza": ceza.quantize(IKI),
        "nihai": nihai.quantize(IKI, ROUND_HALF_UP),
        "elendi": not dogru,
        "talep": p["talep"],
        "merak": p["merak"],
        "not": "; ".join(notlar) or "-",
    }


def sirala(sonuclar):
    # Eşitlikte: kanıtlı talep, sonra merak, sonra id (deterministik).
    return sorted(sonuclar, key=lambda r: (r["elendi"], -r["nihai"], -r["talep"], -r["merak"], r["id"]))


def tablo(sonuclar):
    satirlar = [
        f"Viralite modeli {MODEL_SURUMU} | ağırlık toplamı = {sum(AGIRLIK.values())} | puanlar TAHMİNDİR [T]",
        "",
        "| Sıra | ID | Başlık | Ağırlıklı | Bonus | Ceza | Nihai | Not |",
        "|---|---|---|---|---|---|---|---|",
    ]
    sira = 0
    for r in sirala(sonuclar):
        if r["elendi"]:
            s = "elendi"
        else:
            sira += 1
            s = str(sira)
        satirlar.append(
            f"| {s} | {r['id']} | {r['baslik']} | {r['agirlikli']} | +{r['bonus']} | "
            f"−{r['ceza']} | **{r['nihai']}** | {r['not']} |"
        )
    return "\n".join(satirlar)


def dokuman_denetle(yol):
    """Dokümandaki ağırlık tablosunu betikteki ağırlıklarla karşılaştırır."""
    metin = open(yol, encoding="utf-8").read()
    hatalar = []
    for _, ad, w in OLCUTLER:
        m = re.search(r"^\|\s*\d+\s*\|\s*" + re.escape(ad) + r"\s*\|\s*([0-9.,]+)", metin, re.M)
        if not m:
            hatalar.append(f"'{ad}' satırı dokümanda bulunamadı")
            continue
        dw = Decimal(m.group(1).replace(",", "."))
        if dw != w:
            hatalar.append(f"'{ad}': doküman {dw} ≠ betik {w}")
    return hatalar


def main(argv=None):
    ap = argparse.ArgumentParser(description="Viralite puanlama (model " + MODEL_SURUMU + ")")
    ap.add_argument("girdi", nargs="?", help="JSON veya CSV senaryo dosyası")
    ap.add_argument("--dokuman", help="viralite-modeli.md ile ağırlık tutarlılığını denetle")
    a = ap.parse_args(argv)
    if not a.girdi and not a.dokuman:
        ap.error("girdi dosyası veya --dokuman gerekli")
    if a.dokuman:
        hatalar = dokuman_denetle(a.dokuman)
        if hatalar:
            print("DOKÜMAN TUTARSIZ:\n  " + "\n  ".join(hatalar))
            return 1
        print(f"Doküman tutarlı: {len(OLCUTLER)} ağırlık betikle aynı, toplam {sum(AGIRLIK.values())}")
    if a.girdi:
        try:
            print(tablo([puanla(s) for s in oku(a.girdi)]))
        except ValueError as e:
            print(f"GİRDİ HATASI: {e}", file=sys.stderr)
            return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
