#!/usr/bin/env python3
"""Grafik verisi → video/src/videolar/yeni-video/veri-grafik.ts (grafiklere elle rakam yazılmaz).
Kaynaklar: 03-metin/rakam-tablosu.md (kilitli R satırları, finans-dogrulayici) + 03-metin/veri/omb_t7_1_fy2025.xlsx (OMB T7.1).
Kullanım: python3 -I uretim/2026-10-28-yeni-video/07-animasyon/grafik-veri.py"""
import json, re, warnings
from pathlib import Path
import openpyxl
warnings.filterwarnings("ignore")
KOK = Path(__file__).resolve().parents[3]; M = KOK / "uretim/2026-10-28-yeni-video/03-metin"
R = {}
for satir in (M / "rakam-tablosu.md").read_text().splitlines():
    m = re.match(r"\| (R\d+b?) \| ([^|]+) \|", satir)
    if m:
        R[m.group(1)] = [float(x.replace(".", "").replace(",", ".")) for x in re.findall(r"\d[\d.]*,?\d*", m.group(2))]
butce = {"gelir": R["R01"][0], "gider": R["R02"][0], "acik": R["R03"][0], "ss": R["R09"][0], "medicare": R["R10"][0],
         "saglik": R["R11"][0], "savunma": R["R08"][0], "faiz": R["R06"][0]}
butce["diger"] = round(butce["gider"] - sum(butce[k] for k in ["ss", "medicare", "saglik", "savunma", "faiz"]), 1)
net_faiz = [{"fy": 2016 + i, "v": v} for i, v in enumerate(R["R18"])]
assert len(net_faiz) == 11 and net_faiz[-1]["v"] == butce["faiz"], net_faiz
ws = openpyxl.load_workbook(M / "veri/omb_t7_1_fy2025.xlsx", data_only=True).active
omb = []
for r in ws.iter_rows(values_only=True):
    if isinstance(r[0], str) and re.fullmatch(r"\d{4}", r[0].strip()) and int(r[0]) <= 2023 and isinstance(r[8], (int, float)):
        omb.append({"y": int(r[0]), "pct": r[8], "mlr": round(r[3] / 1000, 1)})
d = {o["y"]: o for o in omb}
assert abs(d[1946]["pct"] - R["R33"][0]) < 0.05 and abs(d[1974]["pct"] - R["R33"][1]) < 0.05, (d[1946], d[1974])
out = {"BUTCE": butce, "NET_FAIZ": net_faiz, "ORT_FAIZ": {"oca2022": R["R22"][0], "eyl2026": R["R22"][1]},
       "BORC_GSYH": omb, "BORC_GSYH_2026": R["R32"][0], "BORC_HALK_T": R["R28"][0], "HANE_BORC": R["R30"][0],
       "DGS10": R["R23"][0], "DTB3": R["R24"][0], "ENF1946": R["R35"][0]}
ts = "// Otomatik: uretim/2026-10-28-yeni-video/07-animasyon/grafik-veri.py (rakam-tablosu.md R satırları + OMB T7.1) — elle düzenleme.\n"
ts += "\n".join(f"export const {k} = {json.dumps(v)};" for k, v in out.items()) + "\n"
(KOK / "video/src/videolar/yeni-video/veri-grafik.ts").write_text(ts)
print(json.dumps({k: (v if not isinstance(v, list) else len(v)) for k, v in out.items()}))
