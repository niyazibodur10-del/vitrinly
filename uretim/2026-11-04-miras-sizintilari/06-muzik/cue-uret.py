#!/usr/bin/env python3
"""F6b cue üretici — S03 miras-sizintilari (S08 v2'den uyarlandı). Girdi: 06-muzik/animasyon-efekt-cue.json (= 07-animasyon/efekt-cue.json,
SFX tek kaynağı) + 06-muzik/cue.json'daki F6a müzik/shorts bölümleri (korunur). Çıkış: 06-muzik/cue.json. Deterministik.

SFX kuralları (anlatımı örtmez):
  - tür + öneri → dosya/kazanç (ESLEME, ilk eşleşen kazanır); boş öneri, "vuruş yok", abone (kurgu-editoru yerleştirir), MÜZİK KES → ses yok
  - "MÜZİK KES" olayı: B5 o karede sert keser (0.05 sn), B6 1.0 sn sonra 2 sn'de girer
  - kesme whoosh'ları: "kısa whoosh" ≥10 sn arayla, "sahne geçişi" ≥4 sn arayla; iki SFX arası ≥0.12 sn
  - whoosh/swish/swipe dosyalarında zarf TEPESİ olay karesine (earshot --apex ile üretildi, tepe dosyada bilinen yerde), diğerlerinde
    ses BAŞLANGICI (ilk örnek > tepe·0.1)
"""
import json, os, re, subprocess
import numpy as np

B = os.path.dirname(os.path.abspath(__file__))
UR = os.path.dirname(B)
anim = json.load(open(f"{B}/animasyon-efekt-cue.json"))
TOPLAM = json.load(open(f"{UR}/04-ses/sahne-zamanlari.json"))["toplam_sn"]
eski = json.load(open(f"{B}/cue.json"))
muzik, shorts = eski["muzik"], eski["shorts"]
KES = next(o["t"] for o in anim["olaylar"] if "MÜZİK KES" in o["oneri"])
for m in muzik:                      # F6a sınırları sabit; yalnız MÜZİK KES uygulanır (tekrar koşuda aynı sonuç)
    if m["ad"].startswith("B5"):
        m.update(son=KES, cikis=0.05)
    if m["ad"].startswith("B6"):
        m.update(bas=round(KES + 1.0, 3), giris=2.0)

E, O, AE = "$E/", "$O/", "$AE/"
W = [O + "es-whoosh-whip.flac", O + "es-whoosh-tight.flac"]      # kısa whoosh dönüşümlü
# (öneri regex, [(dosya, db, gecikme_sn), ...], tekrar, aralık)
ESLEME = [
    (r"MÜZİK KES|vuruş yok", [], 0, 0),
    (r"metal kapı \+ sürgü", [(E + "kamyon-ggbotnet-car_trunk_open.flac", -18, 0), (O + "es-toggle-latch.flac", -22, 0.3)], 1, 0),
    (r"metal kapı", [(E + "kamyon-ggbotnet-car_trunk_open.flac", -18, 0)], 1, 0),
    (r"damla / kâğıt", [(O + "es-drip-drop.flac", -18, 0), (E + "para-owlishmedia-money_33.flac", -24, 0.05)], 1, 0),
    (r"^damla", [(O + "es-drip-plink.flac", -18, 0)], 1, 0),
    (r"kâğıt kayma|fırça|^kâğıt$", [(O + "es-swipe-paper.flac", -24, 0)], 1, 0),
    (r"sinyal tık-tık", [(O + "es-click-thock.flac", -24, 0)], 2, 0.35),
    (r"karton pop ×10", [(O + "es-knock-wood.flac", -24, 0)], 10, 0.08),
    (r"karton tok ×4", [(O + "es-knock-wood.flac", -21, 0)], 4, 0.15),
    (r"karton tok ×2", [(O + "es-knock-wood.flac", -21, 0)], 2, 0.15),
    (r"gizem tını", [(O + "es-shimmer.flac", -27, 0)], 1, 0),
    (r"^motor SFX", [(E + "motor-looneybits-startengine.flac", -20, 0)], 1, 0),
    (r"motor \+ korna", [(E + "kamyon-ggbotnet-car_horn.flac", -24, 0), (E + "kamyon-ggbotnet-car_engine_start_up.flac", -24, 0.3)], 1, 0),
    (r"bariyer \+ motor", [(O + "es-toggle-latch.flac", -21, 0), (E + "kamyon-ggbotnet-car_engine_start_up.flac", -25, 0.2)], 1, 0),
    (r"lastik \+ motor", [(E + "kamyon-ggbotnet-car_engine_start_up.flac", -24, 0)], 1, 0),
    (r"pop ×3", [(O + "es-pop-0.flac", -21, 0)], 3, 0.15),
    (r"pop ×2", [(O + "es-pop-0.flac", -21, 0)], 2, 0.15),
    (r"^hafif pop", [(O + "es-ui-pop-soft.flac", -25, 0)], 1, 0),
    (r"^pop$", [(O + "es-pop-0.flac", -21, 0)], 1, 0),
    (r"tabela tok|levha tok|tok vuruş|^tok$", [(O + "es-knock-desk.flac", -19, 0)], 1, 0),
    (r"whoosh ×2", [(O + "es-whoosh-tight.flac", -25, 0)], 2, 0.5),
    (r"yükselen whoosh|rüzgâr", [(O + "es-whoosh-yukselen.flac", -24, 0)], 1, 0),
    (r"kısa whoosh / tık|whoosh kısa", [(O + "es-whoosh-whip.flac", -27, 0)], 1, 0),
    (r"^sahne geçişi", [(O + "es-whoosh-gecis.flac", -28, 0)], 1, 0),
    (r"^kısa whoosh", [W[0], -29, 0], 1, 0),
    (r"keçeli", [(E + "kalem-owlishmedia-stationery_04.flac", -27, 0)], 1, 0),
    (r"kalem tık ×6", [(O + "es-click-soft.flac", -21, 0)], 6, 0.25),
    (r"damga thud ×2", [(O + "es-impact-punch.flac", -20, 0)], 2, 0.4),
    (r"tıkırtı", [(O + "es-typing-run.flac", -23, 0)], 1, 0),
    (r"yazar kasa", [(AE + "ozgun-ka-ching.flac", -18, 0)], 1, 0),
    (r"etiket yapışma", [(E + "bant-owlishmedia-stationery_27.flac", -20, 0)], 1, 0),
    (r"etiket tap", [(O + "es-tap-table.flac", -20, 0)], 1, 0),
    (r"^ding", [(O + "es-mallet-glock.flac", -21, 0)], 1, 0),
    (r"koli bandı çekme", [(E + "bant-owlishmedia-stationery_26.flac", -20, 0)], 1, 0),
    (r"incelmiş rulo", [(E + "bant-owlishmedia-stationery_08.flac", -24, 0)], 1, 0),
    (r"kum saati", [(O + "es-notify-wood.flac", -22, 0)], 1, 0),
    (r"bayrak devri", [(O + "es-swish-soft.flac", -23, 0)], 1, 0),
    (r"sıcak tını", [(O + "es-mallet-celesta.flac", -25, 0)], 1, 0),
    (r"kısa müzik vurgusu", [(O + "es-mallet-glock.flac", -22, 0)], 1, 0),
    (r"maket bıçağı", [(E + "bant-owlishmedia-stationery_27.flac", -19, 0)], 1, 0),
    (r"anahtar", [(AE + "kilit-rubberduck-lock_01.flac", -21, 0)], 1, 0),
    (r"gök gürültüsü", [(O + "es-impact-deep.flac", -16, 0)], 1, 0),
    (r"zaman atlaması", [(O + "es-riser-build.flac", -25, 0)], 1, 0),
    (r"^vuruş", [(O + "es-impact-punch.flac", -19, 0)], 1, 0),
    (r"yükselen tık", [(O + "es-zip-up.flac", -25, 0)], 1, 0),
    (r"inen tık|inen ton", [(O + "es-zip-down.flac", -22, 0)], 1, 0),
    (r"tık ×2", [(O + "es-click-soft.flac", -20, 0)], 2, 0.2),
    (r"^tik|saat tik|ince tık|küçük tık", [(O + "es-hover-tick.flac", -22, 0)], 1, 0),
    (r"tık", [(O + "es-click-soft.flac", -21, 0)], 1, 0),
]
ESLEME = [(r, [tuple(x) for x in (d if isinstance(d[0], (list, tuple)) else [d])], n, a) for r, d, n, a in
          [(r, d if d else [("", 0, 0)], n, a) for r, d, n, a in ESLEME]]

REPO = os.path.abspath(os.path.join(UR, "..", ".."))
YOL = {"$E/": f"{B}/kaynak/efekt/", "$O/": f"{B}/kaynak/ozgun/", "$AE/": f"{REPO}/assets/efekt/"}
_OF = {}


def vurus_ofset(dosya, tepe):
    """Dosya içinde vuruş noktası (sn): tepe=True → 20 ms RMS zarfının tepesi, aksi halde ilk örnek > tepe·0.1."""
    k = (dosya, tepe)
    if k not in _OF:
        yol = next(dosya.replace(a, b) for a, b in YOL.items() if dosya.startswith(a))
        x = np.abs(np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", yol, "-ac", "1", "-ar", "48000", "-f", "f32le", "-"],
                                                capture_output=True, check=True).stdout, np.float32))
        if tepe:
            e = np.convolve(x ** 2, np.ones(960) / 960, mode="same")
            _OF[k] = float(np.argmax(e)) / 48000
        else:
            _OF[k] = float(np.argmax(x > x.max() * 0.1)) / 48000
    return _OF[k]


sfx, atlanan, son_whoosh, son_t, son_tur = [], [], -99.0, -99.0, ""
for o in sorted(anim["olaylar"], key=lambda x: (x["t"], x["tur"] in ("yazi", "kesme"))):   # aynı karede özgül olay genel pop/whoosh'tan önce
    on = o["oneri"].strip()
    if o["tur"] == "abone" or not on or on == "(sessiz)":
        atlanan.append((o["t"], o["tur"], on or "boş", "kural: ses yok"))
        continue
    es = next((e for e in ESLEME if re.search(e[0], on)), None)
    if es is None:
        atlanan.append((o["t"], o["tur"], on, "eşleme yok"))
        continue
    if es[2] == 0:
        atlanan.append((o["t"], o["tur"], on, "kural: ses yok (müzik kesme / vuruşsuz)"))
        continue
    if es[0] == r"^kısa whoosh":                  # iki whoosh dosyası dönüşümlü (aynı ses tekrarı duyulmasın)
        es = (es[0], [(W[sum(1 for x in sfx if x["dosya"] in W) % 2], -29, 0)], 1, 0)
    whoosh = "whoosh" in es[1][0][0]
    if o["tur"] == "kesme" and whoosh:
        bosluk = 4.0 if on.startswith("sahne geçişi") else 10.0
        if o["t"] - son_whoosh < bosluk:
            atlanan.append((o["t"], o["tur"], on, f"whoosh aralığı <{bosluk} sn"))
            continue
    if o["t"] - son_t < 0.12:
        onceki = [x for x in sfx if x["t_olay"] == son_t]
        if o["tur"] != "kesme" and onceki and all(any(k in x["dosya"] for k in ("whoosh", "swish", "swipe")) for x in onceki) \
                and son_tur in ("kesme", "kamera", "kay"):
            sfx = [x for x in sfx if x["t_olay"] != son_t]          # anlamlı olay (kapı, bant, kalem) kesme whoosh'unun yerine geçer
            atlanan.append((son_t, son_tur, "whoosh", "yerine 0.12 sn içindeki anlamlı olay"))
        else:
            atlanan.append((o["t"], o["tur"], on, "önceki SFX'e <0.12 sn"))
            continue
    for k in range(es[2]):
        for dosya, db, gec in es[1]:
            tepe = any(k in dosya for k in ("whoosh", "swish", "swipe"))
            of = vurus_ofset(dosya, tepe)
            ts = o["t"] + gec + k * es[3] - of
            sfx.append(dict(t=round(max(0.0, ts), 4), kirp=round(max(0.0, -ts), 4), kare_olay=o["kare"], t_olay=o["t"], dosya=dosya, db=db,
                            hiza="tepe" if tepe else "baslangic", vurus_ofset=round(of, 4),
                            olay=f"{o['sahne']} {o['olay'][:70]}", oneri=on))
    son_t, son_tur = o["t"], o["tur"]
    if whoosh:
        son_whoosh = o["t"]

cue = dict(kaynak="cue-uret.py ← animasyon-efekt-cue.json (tahmini=%s) + F6a müzik" % anim.get("tahmini"), fps=anim["fps"],
           toplam_sn=TOPLAM, muzik=muzik, sfx=sfx, shorts=shorts,
           atlanan=[dict(t=a, tur=b, oneri=c, neden=d) for a, b, c, d in atlanan])
json.dump(cue, open(f"{B}/cue.json", "w"), ensure_ascii=False, indent=1)
olay = len({s["t_olay"] for s in sfx})
print(f"olay {len(anim['olaylar'])} → sesli olay {olay}, vuruş {len(sfx)}, atlanan {len(atlanan)} "
      f"(eşleme yok: {sum(1 for a in atlanan if a[3] == 'eşleme yok')})")
