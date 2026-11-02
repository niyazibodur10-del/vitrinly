#!/usr/bin/env python3
"""F6 cue üretici — S08. Girdi: 04-ses/sahne-zamanlari.json (bölüm sınırları) + 06-muzik/animasyon-efekt-cue.json (SFX tek kaynağı,
animasyon-yonetmeni). Çıkış: 06-muzik/cue.json (f6.py render okur). Deterministik; animasyon cue'su değişince yeniden koş.

SFX kuralları (Kurzgesagt yoğunluğu, anlatımı örtmez):
  - tür + öneri metni → dosya/kazanç eşlemesi (ESLEME, anahtar kelime sırası önemli; ilk eşleşen kazanır)
  - öneri boş, "(sessiz)", abone (kurgu-editoru ozgun-fare-klik'i AboneOl bileşeniyle yerleştirir) → ses yok
  - kesme whoosh'ları: "kısa whoosh" yalnız önceki whoosh'tan ≥10 sn sonra; "sahne geçişi" ≥4 sn sonra
  - iki SFX arası ≥0.12 sn (aynı karede ikinci olay düşer); tekrarlı vuruşlar (×N) olay anından başlar
  - vuruş noktası hizası (kare doğruluğu; kapı ±2 kare, sfx-kare-kontrol.py): geçiş whoosh'larında (kesme/kamera/kay) zarfın
    TEPESİ, diğerlerinde sesin BAŞLANGICI (ilk örnek > tepe·0.1; OGA dosyalarındaki baştaki sessizlik) olay karesine oturur
"""
import json, os, re, subprocess
import numpy as np

B = os.path.dirname(os.path.abspath(__file__))
UR = os.path.dirname(B)
anim = json.load(open(f"{B}/animasyon-efekt-cue.json"))
sz = {s["sahne"]: s for s in json.load(open(f"{UR}/04-ses/sahne-zamanlari.json"))["sahneler"]}
TOPLAM = json.load(open(f"{UR}/04-ses/sahne-zamanlari.json"))["toplam_sn"]
KES = next(o["t"] for o in anim["olaylar"] if "MÜZİK KES" in o["oneri"])          # S06 kırmızı zarf: müzik keser
DONUS = 134.83                                                                    # "This household pays its lenders…" cümle başı (anlatim-ham.zaman.json)

muzik = [
    dict(ad="B1 mutfak masası", bas=0.0, son=sz["S05"]["bas"] + 0.6, dosya="$M/happy-lofi-day-tarush-singhal.mp3", duck=23, giris=0.4,
         cikis=1.2, ruh="merak + sıcak lo-fi, Rhodes", tempo="≈98 BPM [tahmin]", kaynak="happy lofi day — Tarush Singhal (CC0)"),
    dict(ad="B2a beş zarf", bas=sz["S05"]["bas"] - 0.6, son=KES, dosya="$M/jazz-spring-spring.ogg", duck=22, giris=1.2, cikis=0.25,
         ruh="hafif, sayan caz", tempo="≈90 BPM [tahmin]", kaynak="Jazz — spring spring (CC0)"),
    dict(ad="B2b faiz zarfı sonrası", bas=DONUS, son=sz["S08"]["bas"] + 0.6, dosya="$M/jazz-spring-spring.ogg", duck=22, ofset=20.0,
         giris=2.0, cikis=1.2, ruh="aynı caz, yeniden giriş", tempo="≈90 BPM [tahmin]", kaynak="Jazz — spring spring (CC0)"),
    dict(ad="B3 borç defteri", bas=sz["S08"]["bas"] - 0.6, son=sz["S12"]["bas"] + 0.6, dosya="$M/deliberate-concealment-northivanastan.ogg",
         duck=22, oyuk=True, giris=1.2, cikis=1.2, ruh="meraklı gerilim, pizzicato + celesta", tempo="≈103 BPM [tahmin]",
         kaynak="Deliberate Concealment — northivanastan (CC0)"),
    dict(ad="B4 zarfın içindeki zarf", bas=sz["S12"]["bas"] - 0.6, son=sz["S16"]["bas"] + 0.6, dosya="$A/gerilim-80s-mysterywave-desertdev.ogg",
         duck=21, giris=1.2, cikis=1.2, ruh="yükselen synth gerilimi", tempo="≈80 BPM [tahmin]", kaynak="80s Mysterywave — DesertDev (CC0)"),
    dict(ad="B5 bir ailenin yapamadığı üç şey", bas=sz["S16"]["bas"] - 0.6, son=sz["S21"]["bas"] + 0.6, dosya="$M/lofi-again-omfgdude.ogg",
         duck=22.5, giris=1.2, cikis=1.2, ruh="düşünceli lo-fi, nefes", tempo="yavaş [tahmin]", kaynak="Lofi again — omfgdude (CC0)"),
    dict(ad="B6 açığı kapatmanın üç yolu", bas=sz["S21"]["bas"] - 0.6, son=sz["S26"]["bas"] + 0.6, dosya="$A/the-way-it-is-zane-little.mp3",
         duck=22, giris=1.2, cikis=1.2, ruh="ileriye bakan, dengeli", tempo="orta [tahmin]", kaynak="The Way It Is — Zane Little Music (CC0)"),
    dict(ad="B7 kapanış", bas=sz["S26"]["bas"] - 0.6, son=TOPLAM, dosya="$M/a-small-fire-will-do-trex0n.ogg", duck=22, giris=1.2,
         cikis=2.5, ruh="sakin, sıcak kapanış", tempo="yavaş [tahmin]", kaynak="A Small Fire Will Do — trex0n (CC0)"),
]

E, O, AE = "$E/", "$O/", "$AE/"
# (anahtar kelime regex, [(dosya, db, gecikme_sn), ...], tekrar sayısı, tekrar aralığı)
ESLEME = [
    (r"MÜZİK KES", [(AE + "tik-select.flac", -14, 0)], 1, 0),
    (r"alçalan whoosh", [(AE + "whoosh-uzun.flac", -18, 0)], 1, 0),
    (r"dönen whoosh|koşu whoosh", [(AE + "whoosh-uzun.flac", -22, 0)], 1, 0),
    (r"^sahne geçişi", [(AE + "whoosh-kisa.flac", -25, 0)], 1, 0),
    (r"^kısa whoosh", [(AE + "whoosh-kisa.flac", -27, 0)], 1, 0),
    (r"whoosh", [(AE + "whoosh-kisa.flac", -23, 0)], 1, 0),
    (r"zarf thud", [(E + "zarf-spring-spring-snd_close_map.flac", -16, 0)], 1, 0),
    (r"ahşap gıcırtı|damga|^thud", [(AE + "muhur-impact-punch.flac", -18, 0)], 1, 0),
    (r"kâğıt düşme", [(E + "sayfa-starninjas-book_flip_2.flac", -18, 0)], 1, 0),
    (r"slap|yapışkan not", [(O + "ozgun-yapiskan-not.flac", -15, 0)], 1, 0),
    (r"zarf yırtma", [(E + "zarf-spring-spring-snd_use_map.flac", -16, 0)], 1, 0),
    (r"kart dağıtma", [(E + "sayfa-starninjas-book_flip_1.flac", -24, 0)], 6, 0.12),
    (r"kitap", [(E + "sayfa-starninjas-book_flip_3.flac", -18, 0)], 1, 0),
    (r"kâğıt \+ tık", [(E + "kagit-rubberduck-paper_04.flac", -22, 0), (AE + "tik-click.flac", -20, 0.08)], 1, 0),
    (r"etiket kopma", [(E + "kagit-rubberduck-paper_04.flac", -20, 0), (AE + "tik-click.flac", -20, 0.1)], 1, 0),
    (r"kâğıt yağmuru|kâğıt uçuşu", [(E + "sayfa-starninjas-book_flip_2.flac", -20, 0), (E + "sayfa-starninjas-book_flip_3.flac", -22, 0.25)], 1, 0),
    (r"kâğıt|kalem|çizim|makas", [(E + "kagit-rubberduck-paper_03.flac", -21, 0)], 1, 0),
    (r"fotokopi|yükselen ton|şişme", [(AE + "riser.flac", -24, 0)], 1, 0),
    (r"tuş tıkırtısı", [(O + "ozgun-hesap-tus-dizi.flac", -16, 0)], 1, 0),
    (r"tık ×11", [(O + "ozgun-hesap-tus.flac", -18, 0)], 11, 0.1),
    (r"tık ×6", [(O + "ozgun-hesap-tus.flac", -18, 0)], 6, 0.12),
    (r"tıkırtı ×5", [(O + "ozgun-hesap-tus.flac", -18, 0)], 5, 0.12),
    (r"tıkırtı \+ ding", [(AE + "ozgun-sayac-tikirti.flac", -19, 0), (AE + "ding-pwl-bell_ding1.flac", -21, 0.8)], 1, 0),
    (r"kasa ding|yazarkasa", [(AE + "ozgun-ka-ching.flac", -17, 0)], 1, 0),
    (r"gizem tını|hafif tını", [(AE + "ding-pwl-bell_ding1.flac", -25, 0)], 1, 0),
    (r"ding", [(AE + "ding-pwl-bell_ding1.flac", -21, 0)], 1, 0),
    (r"düdü", [(O + "ozgun-duduk.flac", -20, 0)], 1, 0),
    (r"alarm tik ×3", [(AE + "tik-click.flac", -17, 0)], 3, 0.25),
    (r"alarm tik|kadran tık-tık|tik ×2", [(AE + "tik-click.flac", -17, 0)], 2, 0.2),
    (r"cam çatlama|^vuruş", [(AE + "muhur-impact-plate.flac", -19, 0)], 1, 0),
    (r"olumsuz vuruş", [(AE + "ozgun-gerilim-vurus.flac", -18, 0)], 1, 0),
    (r"büzülme|kapı zili", [(AE + "pop-drop.flac", -20, 0)], 1, 0),
    (r"pop ×3", [(AE + "pop-pluck.flac", -20, 0)], 3, 0.15),
    (r"pop", [(AE + "pop-pluck.flac", -20, 0)], 1, 0),
    (r"^tap ×3", [(AE + "tik-select.flac", -18, 0)], 3, 0.12),
    (r"^tap|tok tap|tek tık|fren tık|tahta tık|^tik", [(AE + "tik-click.flac", -19, 0)], 1, 0),
]

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


sfx, atlanan, son_whoosh, son_t = [], [], -99.0, -99.0
for o in sorted(anim["olaylar"], key=lambda x: x["t"]):
    on = o["oneri"].strip()
    if o["tur"] == "abone" or not on or on == "(sessiz)":
        atlanan.append((o["t"], o["tur"], on or "boş", "kural: ses yok"))
        continue
    es = next((e for e in ESLEME if re.search(e[0], on)), None)
    if es is None:
        atlanan.append((o["t"], o["tur"], on, "eşleme yok"))
        continue
    whoosh = "whoosh" in es[1][0][0]
    if o["tur"] == "kesme" and whoosh:
        bosluk = 4.0 if on.startswith("sahne geçişi") else 10.0
        if o["t"] - son_whoosh < bosluk:
            atlanan.append((o["t"], o["tur"], on, f"whoosh aralığı <{bosluk} sn"))
            continue
    if o["t"] - son_t < 0.12:
        atlanan.append((o["t"], o["tur"], on, "önceki SFX'e <0.12 sn"))
        continue
    for k in range(es[2]):
        for dosya, db, gec in es[1]:
            tepe = "whoosh" in dosya and o["tur"] in ("kesme", "kamera", "kay")
            of = vurus_ofset(dosya, tepe)
            ts = o["t"] + gec + k * es[3] - of
            sfx.append(dict(t=round(max(0.0, ts), 4), kirp=round(max(0.0, -ts), 4), kare_olay=o["kare"], t_olay=o["t"], dosya=dosya, db=db,
                            hiza="tepe" if tepe else "baslangic", vurus_ofset=round(of, 4),
                            olay=f"{o['sahne']} {o['olay'][:70]}", oneri=on))
    son_t = o["t"]
    if whoosh:
        son_whoosh = o["t"]

shorts = [dict(ad="shorts-1", dosya="$M/deliberate-concealment-northivanastan.ogg", duck=20, sure=60.0, ofset=0.0),
          dict(ad="shorts-2", dosya="$A/the-way-it-is-zane-little.mp3", duck=20, sure=60.0, ofset=0.0)]
cue = dict(kaynak="cue-uret.py ← animasyon-efekt-cue.json (tahmini=%s) + sahne-zamanlari.json" % anim.get("tahmini"), fps=anim["fps"],
           toplam_sn=TOPLAM, muzik=muzik, sfx=sfx, shorts=shorts,
           atlanan=[dict(t=a, tur=b, oneri=c, neden=d) for a, b, c, d in atlanan])
json.dump(cue, open(f"{B}/cue.json", "w"), ensure_ascii=False, indent=1)
olay = len({s["t_olay"] for s in sfx})
print(f"olay {len(anim['olaylar'])} → sesli olay {olay}, vuruş {len(sfx)}, atlanan {len(atlanan)} "
      f"(eşleme yok: {sum(1 for a in atlanan if a[3] == 'eşleme yok')})")
