#!/usr/bin/env python3
"""Ses gelmeden iskelet verisi (akış 0b): metin.md ANLATIM → ham TTS cümle zamanları (04-ses/anlatim-ham.zaman.json) + harf orantılı kelime → veri-sahne.ts
(tools/animasyon/sahne-veri.py ile aynı biçim; agiz boş). Ses gelince sahne-veri.py çıktısı bunun üstüne yazılır.
Kullanım: python3 -I uretim/2026-10-28-yeni-video/07-animasyon/tahmini-veri.py"""
import json, re
from pathlib import Path
KOK = Path(__file__).resolve().parents[3]; U = KOK / "uretim/2026-10-28-yeni-video"
md = (U / "03-metin/metin.md").read_text()
KPM, NEFES, ABONE = 160, 0.35, {"S07", "S12", "S26"}  # ABONE-n öncesi 1,5 sn nefes
Z = json.load(open(U / "04-ses/anlatim-ham.zaman.json"))["cumleler"]
E = json.load(open(U / "04-ses/sahne-esleme.json"))["sahneler"]
temiz = lambda c: re.sub(r"\[(.+?)\]\(.+?\)", r"\1", c)
sah = []
for i, e in enumerate(E):
    cs = Z[e["cumle_ilk"]: e["cumle_son"] + 1]
    bas = 0.0 if i == 0 else round((Z[e["cumle_ilk"] - 1]["son"] + cs[0]["bas"]) / 2, 3)
    son = Z[-1]["son"] + 0.6 if i == len(E) - 1 else round((cs[-1]["son"] + Z[e["cumle_son"] + 1]["bas"]) / 2, 3)
    ks = []
    for c in cs:  # cümle içinde kelimeler harf sayısıyla orantılı (Whisper hizası gelene kadar)
        ws = temiz(c["metin"]).split(); top = sum(len(w) + 2 for w in ws); lt = c["bas"]
        for w in ws:
            d = (c["son"] - c["bas"]) * (len(w) + 2) / top
            ks.append({"w": w, "s": round(lt - bas, 3), "e": round(lt + d * 0.9 - bas, 3)}); lt += d
    sah.append({"id": e["sahne"], "bas": bas, "bitis": son, "sure": round(son - bas, 3), "kelimeler": ks, "agiz": []})
t = sah[-1]["bitis"]
alt = []
for s in sah:
    ob = []
    for k in s["kelimeler"]:
        ob.append({"t": k["w"], "s": round(s["bas"] + k["s"], 3), "e": round(s["bas"] + k["e"], 3), "renk": None})
        if len(ob) >= 5 or k["w"][-1] in ".?!":
            alt.append(ob); ob = []
    if ob: alt.append(ob)
ek = {}
for n, m in enumerate(re.findall(r"\*\*Okunacak tam metin \(betik bunu sayar\):\*\* <<(.+?)>>", md), 1):
    cum = re.findall(r"[^.?!]+[.?!]", m); z = []; lt = 0.1
    for c in cum:
        d = len(c.split()) * 60 / KPM; z.append({"metin": c.strip(), "bas": round(lt, 3), "son": round(lt + d, 3)}); lt += d + NEFES
    ek[f"sh{n}"] = {"sure": round(lt, 3), "cumleler": z, "agiz": []}
(KOK / "video/src/videolar/yeni-video/veri-sahne.ts").write_text(
    "// TAHMİNİ (07-animasyon/tahmini-veri.py, ham TTS cümle zamanı, kelime orantılı) — ses gelince tools/animasyon/sahne-veri.py üstüne yazar.\n"
    "export type Cue = {start: number; end: number; value: string};\n"
    "export type Kelime = {t: string; s: number; e: number; renk: string | null};\n"
    "export type SahneVeri = {id: string; bas: number; bitis: number; sure: number; kelimeler: {w: string; s: number; e: number}[]; agiz: Cue[]};\n"
    f"export const SAHNELER: SahneVeri[] = {json.dumps(sah, ensure_ascii=False)};\n"
    f"export const ALTYAZI: Kelime[][] = {json.dumps(alt, ensure_ascii=False)};\n"
    f"export const SHORTS_EK: Record<string, {{sure: number; cumleler: {{metin: string; bas: number; son: number}}[]; agiz: Cue[]}}> = {json.dumps(ek, ensure_ascii=False)};\n")
print(len(sah), "sahne", round(t, 1), "sn", {k: v["sure"] for k, v in ek.items()})
