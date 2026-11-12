#!/usr/bin/env python3
"""Bölüm metin kapısı v2 (Bölüm 002). Kullanım: python3 metin-kontrol.py [--yaz] [--kalibre]
v2 (2026-11-12): Pocket TTS hızları — Bölüm 001 ölçümü (ses/bolum-001.zaman.json): Jake george 207 kpm,
Mike marius 170 kpm (satır içi cümle duraklaması dahil). Tek tip model 200 kpm (koordinatör). Boşluk modeli
tools/ses/diyalog.py ile aynı. Ek kapılar: kelime 200–260, BANK zinciri, önceki bölümle 5-gram örtüşmesi ≤%10.
--kalibre: aynı modeli Bölüm 001 satırlarına uygular, ölçülen ses süresiyle karşılaştırır."""
import re, sys, json, pathlib, importlib.util
B = pathlib.Path(__file__).parent
BOLUM = B.parent.name.split("-")[-1]  # "002"
SONRAKI = int(BOLUM) + 1
def yukle(p):
    spec = importlib.util.spec_from_file_location("s" + str(abs(hash(str(p)))), p); m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
s = yukle(B / "satirlar.py")
KPM_TEK = 200
KPM = {"JAKE": 207, "MIKE": 170}
BOSLUK = {"JAKE": 0.42, "MIKE": 0.22}; AYNI = 0.45; BAS = 0.15; SON = 0.30
KELIME_MIN, KELIME_MAX = 200, 260
YASAK_TEL = ["charts", "complicated", "scenarios", "truth", "crashes", "bold"]
YASAK_POL = ["win ", "winner", "giveaway", "prize", "tag a friend", "share this", "comment yes", "type ", "like if",
             "invest", "guarantee", "stock", "crypto", "financial advice", "subscribe", "follow for part",
             "tomorrow", "tax-free", "you should"]
CTA = "Tell us in the comments."
def kel(t): return len(re.findall(r"[A-Za-z0-9']+", t))
def modelle(satir, son_tutus):
    t_tek = t_kar = BAS; tablo = []; sb = {}; se = {}; ok = None
    for (i, sh, k, metin, sessiz) in satir:
        if ok is not None:
            g = AYNI if k == ok else BOSLUK[k]; t_tek += g; t_kar += g
        t_tek += sessiz; t_kar += sessiz
        sb.setdefault(sh, t_kar)
        w = kel(metin); bas = t_kar
        t_tek += w / KPM_TEK * 60; t_kar += w / KPM[k] * 60; se[sh] = t_kar
        tablo.append((i, sh, k, w, bas, t_kar, metin, sessiz)); ok = k
    t_tek += SON; t_kar += SON
    ses_kar = t_kar
    for sh, h in son_tutus.items(): t_tek += h; t_kar += h; se[sh] = t_kar
    return tablo, t_tek, t_kar, ses_kar, sb, se
if "--kalibre" in sys.argv:
    e = yukle(B.parent.parent / "bolum-001/veri/satirlar.py")
    _, _, _, ses_kar, _, _ = modelle(e.SATIRLAR, {})
    olc = json.load(open(B.parent.parent / "bolum-001/ses/bolum-001.zaman.json"))["sure"]
    print(f"Kalibrasyon B001: model ses {ses_kar:.1f} sn ↔ ölçülen diyalog wav {olc:.1f} sn (fark {ses_kar-olc:+.1f}); final video 74,6 sn = ses + kart/tutuş")
tablo, t_tek, t_kar, ses_kar, sahne_bas, sahne_bit = modelle(s.SATIRLAR, s.SON_TUTUS)
hata = []
W = sum(r[3] for r in tablo)
wj = sum(r[3] for r in tablo if r[2] == "JAKE"); wm = sum(r[3] for r in tablo if r[2] == "MIKE")
alt = "\n".join(r[6] for r in tablo).lower()
for y in YASAK_TEL:
    if re.search(r"\b" + y + r"\b", alt): hata.append(f"telaffuz yasağı: {y}")
for y in YASAK_POL:
    if y in alt: hata.append(f"politika yasağı: {y!r}")
if re.search(r"\d", alt): hata.append("replikte rakam var (TTS için yazıyla yaz)")
# BANK zinciri
bank = s.BANK_BAS; ids = {r[0] for r in tablo}
for sid, tutar in s.ISLEMLER:
    if sid not in ids: hata.append(f"BANK işlemi bilinmeyen satırda: {sid}")
    bank += tutar
    if bank < 0: hata.append(f"BANK eksiye düştü: {sid}")
bank_ok = bank == s.BANK_SON
# 5-gram örtüşmesi (önceki bölüm; CTA kuyruğu hariç)
def gram(metinler, n=5):
    toks = re.findall(r"[a-z0-9']+", " ".join(m for m in metinler if m != CTA).lower())
    return [tuple(toks[i:i + n]) for i in range(len(toks) - n + 1)]
onceki = B.parent.parent / f"bolum-{int(BOLUM)-1:03d}/veri/satirlar.py"
ort = 0.0
if onceki.exists():
    g_simdi = gram([r[6] for r in tablo]); g_onceki = set(gram([x[3] for x in yukle(onceki).SATIRLAR]))
    ort = sum(1 for g in g_simdi if g in g_onceki) / max(1, len(g_simdi))
print(f"Toplam kelime {W} (Jake {wj}, Mike {wm}) | süre tek-tip {KPM_TEK} kpm {t_tek:.1f} sn | karakter bazlı (J{KPM['JAKE']}/M{KPM['MIKE']}) {t_kar:.1f} sn (diyalog wav ≈{ses_kar:.1f} + son tutuş)")
print(f"İlk replik başlangıcı {tablo[0][4]:.2f} sn (≤2) | sıfır-oy/kabul satırı {sahne_bas['S2']:.1f}–{sahne_bit['S2']:.1f} sn (başlangıç ≤5)")
print(f"BANK {s.BANK_BAS} → {bank} (beklenen {s.BANK_SON}) | 5-gram örtüşmesi B{int(BOLUM)-1:03d} ile %{ort*100:.1f} (≤10)")
for sh in sahne_bas: print(f"  {sh}: {sahne_bas[sh]:5.1f}–{sahne_bit[sh]:5.1f}")
kap = [("süre 60–90 (iki model)", 60 <= t_tek <= 90 and 60 <= t_kar <= 90),
       (f"kelime {KELIME_MIN}–{KELIME_MAX}", KELIME_MIN <= W <= KELIME_MAX),
       ("ilk replik ≤2 sn", tablo[0][4] <= 2.0), ("sıfır-oy repliği ≤5 sn'de başlar (kart penceresi)", sahne_bas['S2'] <= 5.0),
       ("son: seçenekler adıyla soru + CTA", tablo[-2][6].endswith("?") and tablo[-1][6] == CTA),
       ("BANK zinciri tutarlı, eksi yok", bank_ok and not any("BANK" in h for h in hata)),
       ("5-gram örtüşmesi ≤%10", ort <= 0.10),
       ("yasak kelime/rakam yok", not [h for h in hata if "BANK" not in h])]
for ad, ok in kap: print(("GEÇTİ " if ok else "KALDI ") + ad)
for h in hata: print("  !", h)
if "--yaz" in sys.argv:
    for k in ("JAKE", "MIKE"):
        (B / f"{k.lower()}.txt").write_text("\n".join(f"{r[0]}\t{r[6]}" for r in tablo if r[2] == k) + "\n")
    bt = [f"# Flip By Vote — Bölüm {BOLUM} diyaloğu (tools/ses/diyalog.py girdisi). Kaynak: veri/satirlar.py (metin-kontrol.py --yaz üretir)"]
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
