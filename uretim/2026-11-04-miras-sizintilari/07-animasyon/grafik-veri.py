#!/usr/bin/env python3
"""Grafik rakamları → video/src/videolar/miras-sizintilari/veri-grafik.ts (tek yön: kilitli 03-metin/rakam-tablosu.md → ekran).
Her değer R-kodlu; betik her değerin tablo satırında (o R satırında) geçtiğini assert eder → tabloda olmayan rakam ekrana çıkamaz.
KAYNAK: R-kodu → ekrandaki kaynak satırı (tablo "ekran" sütunu / metin GÖRSEL Kaynak notu). Okafor kutuları [ÖRNEK] (veri/kutu-hesap.py).
Kullanım (repo kökü): python3 -I uretim/2026-11-04-miras-sizintilari/07-animasyon/grafik-veri.py"""
import json, re
from pathlib import Path

KOK = Path(__file__).resolve().parents[3]
U = KOK / "uretim/2026-11-04-miras-sizintilari"
tablo = (U / "03-metin/rakam-tablosu.md").read_text()
satir = {}
for m in re.finditer(r"^\| (R\d\d[a-g]?) \|(.*)$", tablo, re.M):
    satir.setdefault(m.group(1), "")
    satir[m.group(1)] += m.group(2)

# (R-kodu, tablodaki ham yazım) → ekrandaki değer
def r(kod, ham, deger):
    assert kod in satir, f"{kod} tabloda yok"
    assert ham in satir[kod], f"{kod}: '{ham}' satırda yok"
    return deger

G = {
    "toplam": r("R01", "124", 124), "mirasci": r("R02", "105", 105), "bagis": r("R03", "18", 18),
    "es": r("R04", "54", 54), "dul": r("R05", "~40", 40), "boomer": r("R06", "~100", 100), "boomerPay": r("R06", "%81", 81),
    "yari": r("R07", "62", 62), "haneYuzde": r("R07", "%2", 2),
    "millennial": r("R08", "46", 46), "genx10": r("R08", "14", 14),
    "hazir2024": r("R09", "%55 (2024)", 55), "hazir2026": r("R09", "%47 (2026)", 47), "orneklem": r("R09", "1,431", 1431), "esikMilyon": r("R09", "$3M+", 3),
    "omur": r("R14", "~20", 20), "huzurevi": r("R13", "129.575", 129575),
    "bakimYuzde": r("R16", "%56", 56), "bakim5yil": r("R16", "%22", 22), "cepten": r("R17", "%14 ≥100.000", 14),
    "esikVergi": r("R18", "15.000.000", 15_000_000), "medyan": r("R19", "409.900", 409_900),
    "alimGucu": r("R21", "0,67", 0.67), "enflasyon": r("R21", "%2", 2),
    "boomerEmlak": r("R23", "%41,3", 41.3), "ust10": r("R24", "%68,9", 68.9), "alt50": r("R24", "%2,3", 2.3),
    "ukEsik": r("R26", "325.000", 325_000),
}
KAYNAK = {
    "R01": "Estimate: Cerulli Associates, Dec 2024 · through 2048", "R02": "Cerulli Associates (Dec 2024) · rounded",
    "R03": "Cerulli Associates (Dec 2024)", "R04": "Cerulli Associates (Dec 2024) · a stop, not a loss",
    "R05": "Cerulli Associates (Dec 2024)", "R06": "Cerulli Associates (Dec 2024)", "R07": "Cerulli Associates (Dec 2024)",
    "R08": "Cerulli Associates (Dec 2024)", "R09": "BofA Private Bank survey · 1,431 people with $3M+ investable assets · 2026",
    "R13": "CareScout 2025 Cost of Care Survey · US median", "R14": "CDC / HHS ASPE · US average at 65",
    "R16": "HHS/ASPE estimate (2022)", "R17": "HHS/ASPE estimate · 2020 dollars", "R18": "IRS · US federal, 2026",
    "R19": "Federal Reserve SCF 2022 · 2022 dollars", "R20": "Some states have their own taxes", "R21": "Fed 2% target · own calculation",
    "R23": "Federal Reserve DFA · Q2 2026", "R24": "Federal Reserve DFA · Q2 2026", "R25": "medicare.gov · medicaid.gov",
    "R26": "gov.uk · 2026", "R28": "IRS · Retirement topics – Beneficiary", "ORNEK": "Example family · illustration, not an average",
}
for k in KAYNAK:
    assert k == "ORNEK" or k in satir, k
# Okafor kutuları [ÖRNEK]: 03-metin/veri/kutu-hesap-cikti.txt ile aynı (LIVING −2, CARE −1, SPOUSE 0, GIVING −1, HOUSE dilim, TAX 0 → 6 − dilim)
cikti = (U / "03-metin/veri/kutu-hesap-cikti.txt").read_text()
DURAK = [["LIVING", -2], ["CARE", -1], ["SPOUSE", 0], ["GIVING", -1], ["HOUSE", 0], ["TAX & TIME", 0]]
kalan = 10
for ad, d in DURAK:
    kalan += d
    isaret = f"+{d}" if d == 0 else str(d)
    assert re.search(re.escape(ad.split(" ")[0]) + r".*?" + re.escape(f"{isaret} → {kalan}"), cikti), (ad, d, kalan)
assert kalan == 6
out = KOK / "video/src/videolar/miras-sizintilari/veri-grafik.ts"
out.write_text(
    "// Otomatik: uretim/2026-11-04-miras-sizintilari/07-animasyon/grafik-veri.py (rakam-tablosu.md R satırlarıyla assert) — elle düzenleme.\n"
    f"export const G = {json.dumps(G)} as const;\n"
    f"export const KAYNAK: Record<string, string> = {json.dumps(KAYNAK, ensure_ascii=False)};\n"
    f"export const DURAK: [string, number][] = {json.dumps(DURAK)};\n")
print("GEÇTİ", len(G), "değer,", len(KAYNAK), "kaynak satırı, kutu", kalan)
