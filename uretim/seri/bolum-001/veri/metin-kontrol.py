#!/usr/bin/env python3
"""Bölüm metin kapısı. Kullanım: python3 metin-kontrol.py [--yaz]
Süre: kelime / kpm (iki model: tek tip 160 ve karakter bazlı) + sıra arası 0.25 sn + sessiz vuruşlar.
--yaz: jake.txt, mike.txt, both.txt ve zaman tablosu (zaman.md) üretir."""
import re, sys, pathlib, importlib.util
B = pathlib.Path(__file__).parent
spec = importlib.util.spec_from_file_location("s", B / "satirlar.py"); s = importlib.util.module_from_spec(spec); spec.loader.exec_module(s)
KPM_TEK = 160
KPM = {"JAKE": 150, "MIKE": 170}  # tahmin (kelime/dk, cümle içi duraklama dahil); ses-yonetmeni ölçünce güncellenir
# Boşluk modeli tools/ses/diyalog.py ile aynı: konuşmacı değişiminde yanıtlayana göre, aynı konuşmacıda 0.45, başta 0.15
BOSLUK = {"JAKE": 0.42, "MIKE": 0.22}; AYNI = 0.45; BAS = 0.15
YASAK_TEL = ["charts", "complicated", "scenarios", "truth", "crashes", "bold"]
YASAK_POL = ["win ", "winner", "giveaway", "prize", "tag a friend", "share this", "comment yes", "type ", "like if",
             "invest", "guarantee", "stock", "crypto", "financial advice", "subscribe", "follow for part"]
def kel(t): return len(re.findall(r"[A-Za-z0-9']+", t))
hata = []
satir = s.SATIRLAR
t_tek = t_kar = BAS; tablo = []; sahne_bas = {}; sahne_bit = {}
onceki = None; onceki_k = None
for (i, sh, k, metin, sessiz) in satir:
    if onceki is not None:
        g = AYNI if k == onceki_k else BOSLUK[k]; t_tek += g; t_kar += g
    t_tek += sessiz; t_kar += sessiz
    sahne_bas.setdefault(sh, t_kar)
    w = kel(metin); d_tek = w / KPM_TEK * 60; d_kar = w / KPM[k] * 60
    bas = t_kar; t_tek += d_tek; t_kar += d_kar; sahne_bit[sh] = t_kar
    tablo.append((i, sh, k, w, bas, t_kar, metin, sessiz)); onceki = i; onceki_k = k
for sh, h in s.SON_TUTUS.items(): t_tek += h; t_kar += h; sahne_bit[sh] = t_kar
W = sum(r[3] for r in tablo)
wj = sum(r[3] for r in tablo if r[2] == "JAKE"); wm = sum(r[3] for r in tablo if r[2] == "MIKE")
alt = "\n".join(r[6] for r in tablo).lower()
for y in YASAK_TEL:
    if re.search(r"\b" + y + r"\b", alt): hata.append(f"telaffuz yasağı: {y}")
for y in YASAK_POL:
    if y in alt: hata.append(f"politika yasağı: {y!r}")
if re.search(r"\d", alt): hata.append("replikte rakam var (TTS için yazıyla yaz)")
print(f"Toplam kelime {W} (Jake {wj}, Mike {wm}) | süre tek-tip 160 kpm {t_tek:.1f} sn | karakter bazlı {t_kar:.1f} sn")
print(f"İlk replik başlangıcı {tablo[0][4]:.1f} sn (≤2) | S2 tanıtım {sahne_bas['S2']:.1f}–{sahne_bit['S2']:.1f} sn = {sahne_bit['S2']-sahne_bas['S2']:.1f} sn (≤10)")
for sh in sahne_bas: print(f"  {sh}: {sahne_bas[sh]:5.1f}–{sahne_bit[sh]:5.1f}")
kap = [("süre 60–90 (iki model)", 60 <= t_tek <= 90 and 60 <= t_kar <= 90),
       ("ilk replik ≤2 sn", tablo[0][4] <= 2.0), ("tanıtım ≤10 sn", sahne_bit['S2'] - sahne_bas['S2'] <= 10),
       ("son: seçenekler adıyla soru + CTA", tablo[-2][6].endswith("?") and tablo[-1][6] == "Tell us in the comments."),
       ("yasak kelime/rakam yok", not hata)]
for ad, ok in kap: print(("GEÇTİ " if ok else "KALDI ") + ad)
for h in hata: print("  !", h)
if "--yaz" in sys.argv:
    for k in ("JAKE", "MIKE"):
        (B / f"{k.lower()}.txt").write_text("\n".join(f"{r[0]}\t{r[6]}" for r in tablo if r[2] == k) + "\n")
    # tools/ses/diyalog.py girdisi: "KONUSMACI (boşluk): replik"; parantez yalnız ek sessizlik olan satırda
    bt = ["# Flip By Vote — Bölüm 001 diyaloğu (tools/ses/diyalog.py girdisi). Kaynak: veri/satirlar.py (metin-kontrol.py --yaz üretir)"]
    ok_ = None
    for r in tablo:
        if r[7] > 0:
            g = 0.0 if ok_ is None else (AYNI if r[2] == ok_ else BOSLUK[r[2]])
            bt.append(f"# {r[0]} {r[1]}"); bt.append(f"{r[2]} ({g + r[7]:.2f}): {r[6]}")
        else:
            bt.append(f"{r[2]}: {r[6]}")
        ok_ = r[2]
    (B.parent / "bolum.txt").write_text("\n".join(bt) + "\n")
    z = ["| ID | Sahne | Konuşan | Kelime | Başlangıç sn | Bitiş sn | Replik |", "|---|---|---|---|---|---|---|"]
    z += [f"| {r[0]} | {r[1]} | {r[2]} | {r[3]} | {r[4]:.1f} | {r[5]:.1f} | {r[6]} |" for r in tablo]
    (B / "zaman.md").write_text("\n".join(z) + "\n")
sys.exit(0 if all(ok for _, ok in kap) else 1)
