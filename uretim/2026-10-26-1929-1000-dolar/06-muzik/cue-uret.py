#!/usr/bin/env python3
"""cue.json + cue-listesi.md üretir (müzik bölümleri + SFX vuruşları), gerçek kelime zamanlarından.

Kullanım: python3 06-muzik/cue-uret.py
Çapalar: 04-ses/kelimeler-hizali.json içindeki ifade (ilk/son kelime zamanı) veya cümle (anlatim-ham.zaman.json).
Kare: 30 fps (Remotion) → kare = round(t*30).
"""
import json, os, re

BURA = os.path.dirname(os.path.abspath(__file__))
UR = os.path.dirname(BURA)
W = json.load(open(f"{UR}/04-ses/kelimeler-hizali.json"))["words"]
C = json.load(open(f"{UR}/04-ses/anlatim-ham.zaman.json"))["cumleler"]
S = {s["sahne"]: s for s in json.load(open(f"{UR}/04-ses/sahne-zamanlari.json"))["sahneler"]}
T = [re.sub(r"[^a-z0-9']", "", x["w"].lower()) for x in W]
FPS = 30


def ifade(f, kac=0):
    p = [re.sub(r"[^a-z0-9']", "", x) for x in f.lower().split()]
    r = [(W[i]["s"], W[i + len(p) - 1]["e"]) for i in range(len(T) - len(p) + 1) if T[i:i + len(p)] == p]
    assert r, f"çapa yok: {f}"
    return r[kac]


def cumle(parca):
    r = [x for x in C if parca in x["metin"]]
    assert r, parca
    return r[0]["bas"], r[0]["son"]


bas = lambda f, k=0: ifade(f, k)[0]
son = lambda f, k=0: ifade(f, k)[1]

# ---------------- müzik ----------------
nobody_son = son("nobody knows it yet")
MUZIK = [
    dict(ad="B1 oyun şovu", bas=2.4, son=S["S04"]["bitis"] + 0.6, dosya="$M/catchy-swing-doge.ogg", duck=22, giris=0.4, cikis=1.2,
         ruh="oyunbaz swing, parlak", tempo="swing (BPM tahmini güvenilmez)", kaynak="Catchy Swing — Doge (CC0)"),
    dict(ad="B2a borsa coşkusu", bas=S["S05"]["bas"] - 0.6, son=nobody_son + 0.25, dosya="$M/ragtime-jazz-tarush-singhal.mp3", duck=23,
         oyuk=True, ofset=0.0, giris=1.2, cikis=0.25, ruh="1920'ler ragtime coşkusu", tempo="≈103 BPM [tahmin]",
         kaynak="Ragtime! Jazz — Tarush Singhal (CC0)"),
    dict(ad="B2b çöküş nabzı", bas=bas("then october arrives") - 0.2, son=S["S07"]["bitis"] + 0.6, dosya="$O/ozgun-yatak-nabiz-90bpm.flac",
         duck=21, giris=1.5, cikis=1.2, ruh="kalp atışı + saat, gerilim", tempo="90 BPM", kaynak="kendi üretimimiz"),
    dict(ad="B3 banka paniği", bas=S["S08"]["bas"] - 0.6, son=S["S11"]["bitis"] + 0.6, dosya="$M/tension-komiku.mp3", duck=20, giris=1.2,
         cikis=1.2, ruh="yükselen panik", tempo="serbest", kaynak="Tension — Komiku (CC0)"),
    dict(ad="B4 kutu", bas=S["S12"]["bas"] - 0.6, son=S["S14"]["bitis"] - 0.3, dosya="$M/fridge-is-hungry-congusbongus.ogg", duck=22,
         giris=1.2, cikis=0.6, ruh="muzip, sıcak", tempo="orta", kaynak="The Fridge is Hungry — congusbongus (CC0)"),
    dict(ad="B5 dip 1932", bas=S["S15"]["bas"] - 0.2, son=S["S17"]["bitis"] + 0.6, dosya="$M/at-the-end-of-hope-emma-ma.mp3", duck=22,
         giris=1.5, cikis=1.2, ruh="ağır, buruk", tempo="≈107 BPM [tahmin]", kaynak="At the end of hope — Emma_MA (CC0)"),
    dict(ad="B6 Mart 1933 kilit", bas=S["S18"]["bas"] - 0.6, son=S["S19"]["bitis"] + 0.6,
         dosya="$A/merak-unsolved-investigation-isaiah658.ogg", duck=22, giris=1.2, cikis=1.2, ruh="mekanik gerilim, gizem",
         tempo="≈120 BPM [tahmin]", kaynak="Unsolved Investigation — isaiah658 (CC0)"),
    dict(ad="B6 katman saat", bas=S["S18"]["bas"] - 0.6, son=S["S19"]["bitis"] + 0.6, dosya="$O/ozgun-yatak-kilit-saat-100bpm.flac",
         duck=27, giris=2.0, cikis=1.2, ruh="saat tik-tak + bas ostinato (katman)", tempo="100 BPM", kaynak="kendi üretimimiz"),
    dict(ad="B7 2026 ters köşe", bas=S["S20"]["bas"] - 0.6, son=S["S22"]["bitis"] + 0.6, dosya="$M/electro-swing-type-gp.mp3", duck=22,
         giris=0.8, cikis=1.2, ruh="modern electro swing (açılış swing'inin bugünkü hali)", tempo="swing",
         kaynak="Electro Swing type — G_P (CC0)"),
    dict(ad="B8 kapanış", bas=S["S23"]["bas"] - 0.6, son=S["S24"]["bitis"], dosya="$M/positive-melancholy-dizzy-crow.ogg", duck=22,
         giris=1.5, cikis=2.0, ruh="sıcak, umutlu, düşündürücü", tempo="orta", kaynak="Piano & Drums, positive melancholy — Dizzy Crow (CC0)"),
]
for m in MUZIK:
    m["bas"], m["son"] = round(max(m["bas"], 0.0), 3), round(min(m["son"], 631.63), 3)

# ---------------- SFX ----------------
c39 = cumle("Monday, October twenty-eight")
c40 = cumle("On Tuesday")
champ = cumle("champion")
good = cumle("Good banks and bad banks")
SFX = [
    (0.0, "$O/ozgun-radyo-cizirti.flac", -30, "S01 sepya 1929 kartı: plak/radyo hışırtısı (2.3 sn)", {"sure": 2.3}),
    (2.25, "$O/ozgun-kapi-isik-acilis.flac", -14, "S01 kesme → stüdyo, üç kapı ışıkla açılır", {}),
    (bas("stock market"), "$AE/pop-pluck.flac", -20, "S01 mavi kapı yanar (STOCKS)", {"pan": -0.4}),
    (bas("a bank"), "$AE/pop-pluck.flac", -20, "S01 yeşil kapı yanar (BANK)", {}),
    (bas("shoebox under"), "$AE/pop-pluck.flac", -20, "S01 kahve kapı yanar (SHOEBOX)", {"pan": 0.4}),
    (son("let's play") + 0.02, "$O/ozgun-ding-oyunsovu.flac", -12, "S01 \"Let's play\" sunucu zili", {}),
    (bas("you can't switch") - 0.05, "$AE/pop-drop.flac", -16, "S04 kural kartı 1 çakılır", {}),
    (bas("can't see the future") - 0.05, "$AE/pop-drop.flac", -16, "S04 kural kartı 2 çakılır", {}),
    (bas("blue door"), "$AE/whoosh-kisa.flac", -22, "S04 Stock Leo mavi kapıya yürür", {"pan": -0.3}),
    (bas("green door"), "$AE/whoosh-kisa.flac", -22, "S04 Bank Leo yeşil kapıya", {}),
    (bas("brown one"), "$AE/whoosh-kisa.flac", -22, "S04 Box Leo kahve kapıya", {"pan": 0.3}),
    (son("audience laughs") + 0.05, "$E/kahkaha-nocturnal-vanguard-group_giggling.flac", -17, "S04 seyirci kahkahası katman 1", {"sure": 2.2}),
    (son("audience laughs") + 0.09, "$E/kahkaha-nocturnal-vanguard-group_giggling.flac", -19, "S04 kahkaha katman 2 (−2 yarım ton)", {"sure": 2.2, "perde": -2, "pan": -0.5}),
    (son("audience laughs") + 0.13, "$E/kahkaha-nocturnal-vanguard-group_giggling.flac", -19, "S04 kahkaha katman 3 (+2 yarım ton)", {"sure": 2.2, "perde": 2, "pan": 0.5}),
    (S["S04"]["bitis"] - 0.45, "$AE/whoosh-uzun.flac", -16, "S04→S05 bölüm geçişi (Door One)", {}),
    (bas("blue door", 1), "$E/kapi-rubberduck-door_open_01.flac", -18, "S05 Stock Leo mavi kapıdan geçer", {}),
    (nobody_son + 0.05, "$O/ozgun-gerilim-vurus.flac", -11, "S05 \"Nobody knows it yet\" — müzik keser + tek nota gerilim vuruşu", {}),
    (c39[0] + 0.1, "$AE/muhur-impact-plate.flac", -18, "S06 Kara Pazartesi çizgisi çakılır (−13%)", {}),
    (c40[0] + 0.1, "$AE/muhur-impact-plate.flac", -18, "S06 Kara Salı (−12%)", {}),
    (son("about five hundred") + 0.05, "$O/ozgun-buzzer-yanlis.flac", -15, "S06 \"$1,000 → $500\" yanlış-cevap buzzer'ı", {}),
    (bas("green door", 1), "$E/kasa-kapisi-rubberduck-metal_open_01.flac", -18, "S07 yeşil kapı açılır, banka kasası", {}),
    (son("right") + 0.02, "$O/ozgun-gerilim-vurus.flac", -11, "S07 \"Right?\" tek nota gerilim vuruşu (↺ Bölüm 3)", {}),
    (son("stops operating") + 0.05, "$E/kasa-kapisi-rubberduck-metal_slam_01.flac", -15, "S09 Bank of United States kapanır", {}),
    (bas("nine thousand banks") - 1.0, "$O/ozgun-sayac-tikirti.flac", -21, "S10 \"~9,000 BANKS\" sayacı döner", {}),
    (son("door two is the gamble") + 0.03, "$AE/muhur-impact-punch.flac", -11, "S10 \"GAMBLE\" damgası", {}),
    (S["S10"]["konusma_bitis"] + 0.05, "$O/ozgun-ding-ding-dogru.flac", -14, "S10 sonu ilk büyük ödül sonucu", {}),
    (bas("quick pause") - 0.1, "$AE/tik-click.flac", -16, "S11 \"Quick pause\" duraklatma tıkı", {}),
    (bas("back to the studio") - 0.3, "$AE/whoosh-kisa.flac", -18, "S11 stüdyoya dönüş", {}),
    (bas("twenty-one percent") - 1.2, "$O/ozgun-sayac-tikirti.flac", -21, "S12 \"−21%\" fiyat sayacı", {}),
    (son("money got stronger") + 0.03, "$O/ozgun-ka-ching.flac", -12, "S12 \"money got stronger\" ka-ching", {}),
    (champ[1] + 0.03, "$O/ozgun-buzzer-yanlis.flac", -16, "S14 \"champion?\" → buzzer, \"Not so fast\"", {"sure": 0.4}),
    (bas("it can burn"), "$AE/pop-pluck.flac", -19, "S14 tuzak kartı FIRE", {}),
    (bas("stolen"), "$AE/pop-pluck.flac", -19, "S14 tuzak kartı THEFT", {}),
    (bas("bill by bill"), "$AE/pop-pluck.flac", -19, "S14 tuzak kartı JOB LOSS", {}),
    (son("jump to the bottom") + 0.02, "$O/ozgun-ruzgar-dusus.flac", -11, "S14→S15 \"Let's jump to the bottom\": rüzgâr + düşüş", {}),
    (son("eighty-nine percent") + 0.03, "$AE/muhur-impact-plate.flac", -15, "S15 \"−89%\" çakılır", {}),
    (bas("scoreboard") - 0.2, "$O/ozgun-ding-oyunsovu.flac", -18, "S16 skor tablosu açılır", {}),
    (son("every door gets locked") + 0.03, "$O/ozgun-kasa-kilit.flac", -12, "S17 \"every door gets locked\" kasa kilidi", {}),
    (bas("closes every bank") - 2.5, "$O/ozgun-radyo-cizirti.flac", -30, "S18 Roosevelt radyo silueti hışırtısı", {"sure": 3.0}),
    (good[0] + 0.0, "$E/zincir-rubberduck-chain_01.flac", -19, "S18 kapı 1 zincir", {"pan": -0.5}),
    (good[0] + 0.08, "$E/kilit-rubberduck-lock_01.flac", -21, "S18 kapı 1 asma kilit", {"pan": -0.5}),
    (good[0] + 0.7, "$E/zincir-rubberduck-chain_02.flac", -19, "S18 kapı 2 zincir", {}),
    (good[0] + 0.78, "$E/kilit-rubberduck-lock_02.flac", -21, "S18 kapı 2 asma kilit", {}),
    (good[0] + 1.4, "$E/zincir-rubberduck-chain_03.flac", -19, "S18 kapı 3 zincir", {"pan": 0.5}),
    (good[1] + 0.02, "$E/kilit-rubberduck-lock_01.flac", -15, "S18 kapı 3 asma kilit (cümle sonunda, boşlukta)", {"pan": 0.5}),
    (bas("four thousand banks") - 1.0, "$O/ozgun-sayac-tikirti.flac", -21, "S18 \"~4,000 never reopen\" sayacı", {}),
    (son("nine insured") + 0.02, "$E/ding-pwl-bell_ding1.flac", -18, "S19 \"9 insured\" dilimi", {}),
    (son("move it to today") + 0.02, "$AE/riser.flac", -14, "S19→S20 kapı raylarda kayar, 1933→2026", {}),
    (bas("three point seven") - 1.0, "$O/ozgun-sayac-tikirti.flac", -21, "S20 \"+3.7%\" sayacı", {}),
    (son("they just buy less") + 0.02, "$AE/pop-drop.flac", -16, "S20 \"$964\" kartı düşer", {}),
    (son("opposite result") + 0.02, "$AE/muhur-impact-punch.flac", -12, "S21 \"Same box. Opposite result.\" vuruşu", {}),
    (son("two hundred fifty thousand") + 0.03, "$O/ozgun-ka-ching.flac", -16, "S22 \"$250,000\" sigorta tabelası", {}),
    (son("came out on top") + 0.02, "$O/ozgun-ding-ding-dogru.flac", -14, "S23 kazanan kapı", {}),
]
sfx = []
for t, d, db, olay, ek in SFX:
    sfx.append(dict(t=round(t, 3), kare=round(t * FPS), dosya=d, db=db, olay=olay, **ek))
sfx.sort(key=lambda x: x["t"])

SHORTS = [
    dict(ad="shorts-1", dosya="$M/catchy-swing-doge.ogg", duck=20, sure=60.0, ofset=0.0),
    dict(ad="shorts-2", dosya="$M/electro-swing-type-gp.mp3", duck=20, sure=60.0, ofset=0.0),
]
json.dump({"fps": FPS, "muzik": MUZIK, "sfx": sfx, "shorts": SHORTS}, open(f"{BURA}/cue.json", "w"), ensure_ascii=False, indent=1)

ss = lambda t: f"{int(t // 60)}:{t % 60:05.2f}"
L = ["# Cue listesi — 1929-1000-dolar (F6)", "",
     "Kaynak: `06-muzik/cue.json` (makine okunur; `cue-uret.py` gerçek kelime zamanlarından üretir). Zaman ekseni = `04-ses/anlatim.wav` (631.63 sn). Kare = 30 fps.",
     "Stem'ler: `stems/muzik-stem.wav`, `stems/sfx-stem.wav` (48 kHz stereo 24-bit, anlatımla aynı uzunluk; kurguda 0 noktası anlatımın 0 noktası). Montajda anlatımın başına boşluk eklenirse iki stem de aynı kadar kaydırılır.",
     "", "## Müzik bölümleri", "",
     "| # | Bölüm | Giriş → çıkış | Kare | Parça (lisans) | Ruh hali / tempo | Konuşma altı | Giriş/çıkış sönüşü |", "|---|---|---|---|---|---|---|---|"]
for i, m in enumerate(MUZIK, 1):
    L.append(f"| {i} | {m['ad']} | {ss(m['bas'])} → {ss(m['son'])} | {round(m['bas'] * FPS)}–{round(m['son'] * FPS)} | {m['kaynak']} | {m['ruh']} · {m['tempo']} | −{m['duck']} dB{' + 3 kHz oyuk' if m.get('oyuk') else ''} | {m['giris']} / {m['cikis']} sn |")
L += ["", "Notlar: 2:14 civarı (\"Nobody knows it yet\") müzik 0.25 sn'de **keser**, 6 sn sessizlik + gerilim vuruşu, ardından \"Then October arrives\"ta nabız girer. B6'da iki katman üst üste (Unsolved Investigation + saat yatağı −27 dB). Konuşma boşluğu ≥0.9 sn olunca müzik +6 dB açılır.", "",
      "## SFX vuruşları", "", "| Zaman | Kare | Olay | Dosya | Kazanç dB |", "|---|---|---|---|---|"]
for s in sfx:
    L.append(f"| {ss(s['t'])} | {s['kare']} | {s['olay']} | `{os.path.basename(s['dosya'])}` | {s['db']} |")
L += ["", "Kazanç = dosya önce −3 dBFS tepeye normalize edildikten sonra uygulanan değer. Konuşmayla çakışma raporu: `olcum-f6-render.json` → `sfx_konusma_cakismasi`.", "",
      "## Shorts", "", "| Shorts | Parça | Uzunluk | Seviye |", "|---|---|---|---|",
      "| Shorts 1 \"Pick a door\" | Catchy Swing (CC0) — `stems/shorts-1-muzik-stem.wav` | 60 sn, sonda 2 sn sönüş | konuşma altında −20 dB (sabit yatak) |",
      "| Shorts 2 \"Same box, opposite result\" | Electro Swing type (CC0) — `stems/shorts-2-muzik-stem.wav` | 60 sn, sonda 2 sn sönüş | −20 dB |",
      "", "Shorts'ta SFX: kurgu-editoru ana videodaki aynı olay dosyalarını aynı kazançla kullanır (ör. \"Let's play\" zili yok; skor tablosu `ozgun-ding-oyunsovu` −18, \"$500\" buzzer −15, \"Opposite result\" mühür −12). Kesim bitince Shorts stem'i kesit uzunluğuna kırpılır, son 2 sn sönüş korunur."]
open(f"{BURA}/cue-listesi.md", "w").write("\n".join(L) + "\n")
print(len(MUZIK), "müzik bölümü,", len(sfx), "SFX")
