#!/usr/bin/env python3
"""Ses gelmeden iskelet verisi (akış 0b): metin.md ANLATIM → 160 kpm tahmini cümle/kelime zamanı → veri-sahne.ts
(tools/animasyon/sahne-veri.py ile aynı biçim; agiz boş). Ses gelince sahne-veri.py çıktısı bunun üstüne yazar.
Model: kelime = 60/160 sn (harf sayısıyla orantılı paylaşım), cümle arası 0,35 sn, sahne arası 0,30 sn,
ABONE sahnesi (S05/S17/S30) sonunda +1,5 sn nefes (metin §3). Kaynak desen: uretim/2026-10-28-yeni-video/07-animasyon/tahmini-veri.py
Kullanım (repo kökü): python3 -I uretim/2026-11-04-miras-sizintilari/07-animasyon/tahmini-veri.py"""
import json, re
from pathlib import Path

KOK = Path(__file__).resolve().parents[3]
U = KOK / "uretim/2026-11-04-miras-sizintilari"
CIKIS = KOK / "video/src/videolar/miras-sizintilari/veri-sahne.ts"
KPM, NEFES, SAHNE_ARA, ABONE_NEFES = 160, 0.35, 0.30, 1.5
ABONE = {"S05", "S17", "S30"}
md = (U / "03-metin/metin.md").read_text()

bloklar = re.findall(r"^### (S\d\d) [^\n]*\n\| ANLATIM \| GÖRSEL \|\n\|---\|---\|\n\| (.+?) \| ", md, re.M)
assert len(bloklar) == 31 and [b[0] for b in bloklar] == [f"S{i:02d}" for i in range(1, 32)], [b[0] for b in bloklar]
# "U.S." / "U.K." cümle bölmez (korunur, sonra geri yazılır)
cumleler = lambda m: [c.strip().replace("§", ".") for c in re.findall(r"[^.?!]+[.?!]+", re.sub(r"\bU\.([SK])\.", r"U§\1§", m)) if c.strip()]


def zamanla(cs, t0):
    """Cümleleri t0'dan başlatır; kelime listesi (mutlak zaman) + bitiş döner."""
    ks, t = [], t0
    for c in cs:
        ws = c.split()
        d = len(ws) * 60 / KPM
        top = sum(len(w) + 2 for w in ws)
        lt = t
        for w in ws:
            dw = d * (len(w) + 2) / top
            ks.append({"w": w, "s": round(lt, 3), "e": round(lt + dw * 0.9, 3)})
            lt += dw
        t = lt + NEFES
    return ks, t - NEFES


sah, t = [], 0.0
for sid, metin in bloklar:
    bas = round(t, 3)
    ks, son = zamanla(cumleler(metin), bas + 0.1)
    bitis = round(son + SAHNE_ARA + (ABONE_NEFES if sid in ABONE else 0), 3)
    sah.append({"id": sid, "bas": bas, "bitis": bitis, "sure": round(bitis - bas, 3),
                "kelimeler": [{"w": k["w"], "s": round(k["s"] - bas, 3), "e": round(k["e"] - bas, 3)} for k in ks], "agiz": []})
    t = bitis

alt = []
for s in sah:
    ob = []
    for k in s["kelimeler"]:
        ob.append({"t": k["w"], "s": round(s["bas"] + k["s"], 3), "e": round(s["bas"] + k["e"], 3), "renk": None})
        if len(ob) >= 5 or k["w"][-1] in ".?!":
            alt.append(ob); ob = []
    if ob:
        alt.append(ob)

ek = {}
for n, m in enumerate(re.findall(r"\*\*Okunacak tam metin \(betik bunu sayar\):\*\* <<(.+?)>>", md), 1):
    z, lt = [], 0.1
    for c in cumleler(m):
        d = len(c.split()) * 60 / KPM
        z.append({"metin": c, "bas": round(lt, 3), "son": round(lt + d, 3)})
        lt += d + NEFES
    ek[f"sh{n}"] = {"sure": round(lt + 0.6, 3), "cumleler": z, "agiz": []}
assert set(ek) == {"sh1", "sh2"}

CIKIS.write_text(
    "// TAHMİNİ (uretim/2026-11-04-miras-sizintilari/07-animasyon/tahmini-veri.py, 160 kpm, kelime harf orantılı) — ses gelince tools/animasyon/sahne-veri.py üstüne yazar.\n"
    "export type Cue = {start: number; end: number; value: string};\n"
    "export type Kelime = {t: string; s: number; e: number; renk: string | null};\n"
    "export type SahneVeri = {id: string; bas: number; bitis: number; sure: number; kelimeler: {w: string; s: number; e: number}[]; agiz: Cue[]};\n"
    f"export const SAHNELER: SahneVeri[] = {json.dumps(sah, ensure_ascii=False)};\n"
    f"export const ALTYAZI: Kelime[][] = {json.dumps(alt, ensure_ascii=False)};\n"
    f"export const SHORTS_EK: Record<string, {{sure: number; cumleler: {{metin: string; bas: number; son: number}}[]; agiz: Cue[]}}> = {json.dumps(ek, ensure_ascii=False)};\n")
print(len(sah), "sahne", round(t, 1), "sn", {k: v["sure"] for k, v in ek.items()},
      "ABONE başı:", {s["id"]: round(s["bas"] + s["kelimeler"][-1]["e"] + 0.15, 2) for s in sah if s["id"] in ABONE})
