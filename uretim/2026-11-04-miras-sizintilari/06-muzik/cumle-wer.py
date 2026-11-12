#!/usr/bin/env python3
"""F6 anlaşılırlık kapısı (cümle tek başına): tools/ses/cumle-whisper.py çıktıları (anlatım / müzik-tek miks / tam miks) cümle cümle
referansla kıyaslanır. Tam dosya Whisper'ı segment düşürmeleri yüzünden aynı sese ±6 kelime oynuyor (S03 F6b ölçümü) → kapı cümle bazında.
Kullanım: cumle-wer.py <cw-anlatim.json> <cw-muzik.json> <cw-tam.json> [--sfx cue.json]
Çıktı: toplam hata (her biri), tam miks'in anlatımdan kötü olduğu cümleler + o cümle aralığındaki SFX'ler. Çıkış 0 = tam−anlatım ≤ 2."""
import json, re, runpy, sys, os
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
ns = runpy.run_path(f"{REPO}/tools/ses/hata-orani.py")
def mesafe(r, h):
    d = list(range(len(h) + 1))
    for i in range(1, len(r) + 1):
        o, d[0] = d[0], i
        for j in range(1, len(h) + 1):
            o, d[j] = d[j], min(d[j] + 1, d[j - 1] + 1, o + (r[i - 1] != h[j - 1]))
    return d[-1]
a, m, t = (json.load(open(p))["cumleler"] for p in sys.argv[1:4])
cue = json.load(open(sys.argv[sys.argv.index("--sfx") + 1])) if "--sfx" in sys.argv else None
top = {"anlatim": 0, "muzik": 0, "tam": 0}; kelime = 0; kotu = []
for ca, cm, ct in zip(a, m, t):
    r = ns["norm"](re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", ca["metin"]))
    e = {k: mesafe(r, ns["norm"](c["whisper"])) for k, c in (("anlatim", ca), ("muzik", cm), ("tam", ct))}
    for k in e: top[k] += e[k]
    kelime += len(r)
    if e["tam"] > e["anlatim"]:
        kotu.append({"i": ca["i"], "metin": ca["metin"][:70], "anlatim": ca["whisper"][:70], "tam": ct["whisper"][:70], **{f"h_{k}": v for k, v in e.items()}})
print(json.dumps({"kelime": kelime, "hata": top, "wer_%": {k: round(v / kelime * 100, 2) for k, v in top.items()},
                  "tam_anlatimdan_kotu_cumle": kotu}, ensure_ascii=False, indent=1))
sys.exit(0 if top["tam"] - top["anlatim"] <= 2 else 1)
