#!/usr/bin/env python3
"""Grafik verisi (finans-dogrulayici tablolarından, 03-metin/veri/*.csv) → video/src/k1929/veri-grafik.ts. Elle rakam yazılmaz."""
import csv, json
from pathlib import Path
KOK = Path(__file__).resolve().parents[3]; V = KOK / "uretim/2026-10-26-1929-1000-dolar/03-metin/veri"
def cpi(dosya, bas, son):
    out = []
    for r in csv.DictReader(open(V / dosya)):
        d = r["observation_date"][:7]
        if bas <= d <= son and r["CPIAUCNS"].strip():
            y, m = int(d[:4]), int(d[5:7]); out.append({"x": round(y + (m - 1) / 12, 4), "y": float(r["CPIAUCNS"]), "ay": d})
    return out
c29 = cpi("cpi-1928-1934-CPIAUCNS.csv", "1929-09", "1933-03")
c22 = cpi("cpi-2019-2026-CPIAUCNS.csv", "2022-09", "2026-09")
fdic = [{"yil": int(r["yil"]), "banka": int(r["askiya_alinan_banka"]), "mevduat": int(r["mevduat_bin_usd"]), "kayip": int(r["mudi_kaybi_bin_usd"])} for r in csv.DictReader(open(V / "fdic-tablo5-askiya-alma-1921-1933.csv"))]
dow = [r for r in csv.DictReader(open(V / "dow-capalari-FRH.csv"))]
idx = lambda s: [{"x": p["x"], "y": round(p["y"] / s[0]["y"] * 100, 2), "ay": p["ay"]} for p in s]
(KOK / "video/src/k1929/veri-grafik.ts").write_text(
    "// Otomatik: 07-animasyon/grafik-veri.py (kaynak 03-metin/veri/*.csv — FRED CPIAUCNS, FDIC Tablo 5, FRH Dow çapaları)\n"
    f"export const CPI29 = {json.dumps(c29)};\nexport const CPI22 = {json.dumps(c22)};\n"
    f"export const CPI29_IDX = {json.dumps(idx(c29))};\nexport const CPI22_IDX = {json.dumps(idx(c22))};\n"
    f"export const FDIC = {json.dumps(fdic)};\nexport const DOW = {json.dumps(dow, ensure_ascii=False)};\n")
print(len(c29), c29[0], c29[-1], len(c22), c22[0], c22[-1], idx(c29)[-1], idx(c22)[-1])
