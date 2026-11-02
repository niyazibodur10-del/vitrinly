#!/usr/bin/env python3
"""Ses gelmeden iskelet verisi (akış 0b): metin.md ANLATIM → 160 kpm tahmini kelime zamanları → veri-sahne.ts
(tools/animasyon/sahne-veri.py ile aynı biçim; agiz boş). Ses gelince sahne-veri.py çıktısı bunun üstüne yazılır.
Kullanım: python3 -I uretim/2026-10-28-yeni-video/07-animasyon/tahmini-veri.py"""
import json, re
from pathlib import Path
KOK = Path(__file__).resolve().parents[3]; U = KOK / "uretim/2026-10-28-yeni-video"
md = (U / "03-metin/metin.md").read_text()
KPM, NEFES, ABONE = 160, 0.35, {"S07", "S12", "S26"}  # ABONE-n öncesi 1,5 sn nefes
sah, t = [], 0.0
for m in re.finditer(r"^### (S\d\d)[^\n]*\n[^\n]*\n\|---\|---\|\n\| (.+?) \| \*\*", md, re.M):
    sid, metin = m.group(1), m.group(2)
    ws = metin.split(); ks = []; lt = 0.15
    for w in ws:
        d = 60 / KPM * (1.0 + 0.04 * max(0, len(w) - 6))
        ks.append({"w": w, "s": round(lt, 3), "e": round(lt + d * 0.92, 3)}); lt += d
        if w[-1] in ".?!:": lt += NEFES
    sure = round(lt + 0.3 + (1.5 if sid in ABONE else 0), 3)
    sah.append({"id": sid, "bas": round(t, 3), "bitis": round(t + sure, 3), "sure": sure, "kelimeler": ks, "agiz": []}); t += sure
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
    "// TAHMİNİ (07-animasyon/tahmini-veri.py, 160 kpm, ses yok) — ses gelince tools/animasyon/sahne-veri.py üstüne yazar.\n"
    "export type Cue = {start: number; end: number; value: string};\n"
    "export type Kelime = {t: string; s: number; e: number; renk: string | null};\n"
    "export type SahneVeri = {id: string; bas: number; bitis: number; sure: number; kelimeler: {w: string; s: number; e: number}[]; agiz: Cue[]};\n"
    f"export const SAHNELER: SahneVeri[] = {json.dumps(sah, ensure_ascii=False)};\n"
    f"export const ALTYAZI: Kelime[][] = {json.dumps(alt, ensure_ascii=False)};\n"
    f"export const SHORTS_EK: Record<string, {{sure: number; cumleler: {{metin: string; bas: number; son: number}}[]; agiz: Cue[]}}> = {json.dumps(ek, ensure_ascii=False)};\n")
print(len(sah), "sahne", round(t, 1), "sn", {k: v["sure"] for k, v in ek.items()})
