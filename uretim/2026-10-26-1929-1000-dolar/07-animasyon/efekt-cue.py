#!/usr/bin/env python3
"""Animasyondaki görsel olayların zamanları (anlatim.wav global sn, 30 fps kare) → muzik-ses-tasarimcisi için cue.
Zamanlar b1–b4.tsx'teki kelime çapaları + ofsetlerle aynı formülden hesaplanır (kod değişirse yeniden üret).
Çıktı: 07-animasyon/efekt-cue.json ve 06-muzik/animasyon-efekt-cue.json (aynı içerik)."""
import json, re
from pathlib import Path
U = Path(__file__).resolve().parents[1]
Z = {s["sahne"]: s for s in json.load(open(U / "04-ses/sahne-zamanlari.json"))["sahneler"]}
K = json.load(open(U / "04-ses/kelimeler-hizali.json"))["words"]
norm = lambda w: re.sub(r"[^a-z0-9$'-]", "", w.lower())
def an(sid, w, n=1, son=False):
    say = 0
    for k in K:
        if k["sahne"] == sid and norm(k["w"]) == norm(w):
            say += 1
            if say == n: return (k["e"] if son else k["s"]) - Z[sid]["bas"]
    raise SystemExit(f"{sid}: {w}#{n} yok")
O = []
def ev(sid, t, olay, tur, oneri=""):
    g = Z[sid]["bas"] + t
    O.append({"sahne": sid, "t": round(g, 3), "kare": round(g * 30), "olay": olay, "tur": tur, "oneri": oneri})
S = "S01"; ev(S, 0, "sepya sokak kartı + SEPT 1929 yazısı", "kart", "radyo hışırtısı")
ev(S, 2.1, "beyaz flaş + yatay kayma kesmesi (sokak → stüdyo)", "kesme", "whoosh")
ev(S, an(S, "one"), "$1,000 sayacı 0→1000 (0.5 sn)", "sayac", "tıkırtı / ding sonda")
for w in ["stock", "bank", "shoebox"]: ev(S, an(S, w), f"kapı levhası yanar ({w.upper()})", "pop", "pop-pluck")
for w in ["disaster", "gamble", "surprise"]: ev(S, an(S, w), f"{w.upper()}? yazısı", "pop", "hafif pop")
ev(S, an(S, "let's"), "üç kapı birlikte parlar + punch-in", "vurgu", "oyun şovu zili")
S = "S02"; ev(S, an(S, "real"), "takvim 1929→2026 çevrilir", "flip", "kâğıt çevirme"); ev(S, an(S, "people"), "takvim 2026→1929", "flip", "kâğıt çevirme")
ev(S, an(S, "where"), "ekrana punch-in + soru yazısı", "kamera", "")
S = "S03"; ev(S, an(S, "now") - 0.0, "G0 kartı açılır", "kart", "pop"); ev(S, an(S, "eight"), "12 ay kutusundan 8'i dolar", "sayac", "tık ×8")
S = "S04"; ev(S, an(S, "switch"), "kural kartı 1", "pop", "pop-drop"); ev(S, an(S, "future."), "kural kartı 2", "pop", "pop-drop")
ev(S, an(S, "stock") - 0.15, "Stock Leo yürüyüşe başlar (3.15 sn; varış)", "yurume", "ayak sesi/whoosh")
ev(S, an(S, "bank") - 0.15, "Bank Leo yürüyüşe başlar (2.6 sn)", "yurume", "")
ev(S, an(S, "box") - 0.25, "Box Leo kutuyla yürür (2.65 sn)", "yurume", "")
ev(S, an(S, "laughs") - 0.25, "kahve kapıya punch-in (0.4 sn) + Box Leo büzülür, HA! yazıları", "vurgu", "seyirci kahkahası")
ev(S, an(S, "remember") - 0.1, "kesme: yakın plan sunucu", "kesme", "")
ev(S, an(S, "laugh.") + 0.2, "tek göz kırpma (0.38 sn)", "vurgu", "ting")
ev(S, an(S, "door", 4) - 0.1, "mavi kapıya punch-in, kapı parlar", "kamera", "whoosh")
S = "S05"; ev(S, 0.5, "mavi kapı paneli açılır → C16 (1.1 sn), kamera içeri dalar", "gecis", "kapı açılış")
ev(S, an(S, "in") - 0.2, "G1a grafik kartı", "kart", ""); ev(S, an(S, "six"), "×6 yazısı", "pop", "")
ev(S, an(S, "ordinary") - 0.3, "C16 borsa önü + ticker şerit yağmuru + Stock Leo aşağıdan girer", "gecis", "kâğıt hışırtısı")
ev(S, an(S, "three", 2), "381.17 büyük sayı", "pop", ""); ev(S, an(S, "it's") - 0.4, "grafik geri: zirve etiketi THE TOP", "kart", "")
S = "S06"; ev(S, an(S, "october") - 0.1, "takvim SEP→OCT", "flip", "kâğıt koparma")
ev(S, an(S, "thirteen") - 0.3, "çubuk −13%", "pop", "darbe"); ev(S, an(S, "twelve") - 0.3, "çubuk −12%", "pop", "darbe")
for w in ["drop,", "lenders", "sell,", "again."]: ev(S, an(S, w), f"marjin sarmalı oku ({w.strip(',.')})", "pop", "")
ev(S, an(S, "now"), "$1,000 → ~$500 sayacı (≈1.1 sn)", "sayac", "aşağı inen ton / buzzer")
S = "S07"; ev(S, an(S, "over") - 0.2, "bölünmüş ekran kayar, banka içi", "gecis", "kasa kapısı"); ev(S, an(S, "right?"), "RIGHT? sallanan yazı", "vurgu", "gerilim vuruşu")
S = "S08"; ev(S, an(S, "insurance.") - 0.4, "boş INSURANCE kutusu", "pop", ""); ev(S, an(S, "and", 1) - 0.2, "kesme: ABD haritası", "kesme", "")
ev(S, an(S, "banks."), "2.400 banka noktası yanar (1.2 sn)", "parcacik", "tıkırtı yağmuru"); ev(S, an(S, "fail") + 0.2, "noktalar dalga dalga kırmızı söner (2.6 sn)", "parcacik", "")
S = "S09"; ev(S, an(S, "long") - 0.2, "Bank Leo sağdan girer (saatine bakar)", "giris", "")
ev(S, an(S, "here's") - 0.2, "kesme: mekanizma kartı", "kesme", ""); ev(S, an(S, "a", 2) - 0.1, "10 madeni para kasaya düşer (1.5 sn)", "parcacik", "para şıngırtısı")
ev(S, an(S, "lends"), "9 para LOANS okuyla akar", "hareket", "kayma"); ev(S, an(S, "cash."), "EMPTY damgası", "damga", "mühür"); ev(S, an(S, "next"), "kuyruk yan bankaya kayar", "hareket", "")
S = "S10"; ev(S, an(S, "from") - 0.2, "G2 çubukları büyür", "kart", "sayaç tıkırtısı"); ev(S, an(S, "twenty"), "~20¢ büyük sayı", "pop", "")
ev(S, an(S, "for", 2) - 0.2, "kesme: kasa önü Bank Leo", "kesme", ""); ev(S, an(S, "gamble."), "GAMBLE damgası", "damga", "mühür")
S = "S11"; ev(S, an(S, "if") - 0.2, "abone düğmesi (3 sn, SESSİZ — politika: ses yok)", "abone", "SES YOK")
ev(S, an(S, "now,"), "spot ışığı kahve kapıya kayar", "isik", "spot"); ev(S, an(S, "one", 2) - 0.2, "kahve kapı punch-in + DOOR 3", "kamera", "")
ev(S, an(S, "something"), "kutu sallanır + ?", "vurgu", "kutu sallama")
S = "S12"; ev(S, an(S, "but") - 0.2, "kesme: C19 vitrin", "kesme", ""); ev(S, an(S, "falling."), "fiyat etiketleri tek tek küçülür (≈2.3 sn)", "hareket", "küçülme pıt ×11")
ev(S, an(S, "the", 4) - 0.2, "G3 TÜFE kartı", "kart", ""); ev(S, an(S, "one"), "$1,000→$1,272 sayacı", "sayac", "yukarı ton")
ev(S, an(S, "stronger."), "banknot parıltısı", "vurgu", "parıltı")
S = "S13"; ev(S, an(S, "here's") - 0.15, "sunucuya punch-in", "kamera", ""); ev(S, an(S, "pulled"), "haritada kutular belirir, noktalar söner", "parcacik", "")
S = "S14"; ev(S, an(S, "not"), "NOT SO FAST damgası", "damga", "mühür")
for w in ["earns", "burn.", "stolen.", "lose"]: ev(S, an(S, w), f"tuzak kartı çevrilir ({w.strip('.')})", "flip", "kart çevirme")
ev(S, an(S, "spend"), "banknotlar tek tek uçar (2.5 sn)", "parcacik", "kâğıt uçuşu"); ev(S, an(S, "let's") + 0.3, "kamera aşağı düşer (whip-down 0.6 sn)", "gecis", "düşüş tonu")
S = "S15"; ev(S, an(S, "forty-one"), "41.22 dip etiketi", "pop", ""); ev(S, an(S, "eighty-nine"), "−89%", "vurgu", "darbe")
ev(S, an(S, "one"), "$1,000→$108 sayacı", "sayac", ""); ev(S, an(S, "november") - 0.3, "grafik 1954'e uzar", "hareket", ""); ev(S, an(S, "late"), "~LATE 1936 çizgisi", "pop", "")
S = "S16"
for w, n in [("stock", 1), ("bank", 1), ("box", 2)]: ev(S, an(S, w, n) - 0.1, f"skor sütunu ({w.upper()})", "pop", "pop")
ev(S, an(S, "decade."), "IN A DECADE OF FALLING PRICES şeridi", "pop", "")
S = "S17"
for w in ["every", "door", "locked."]: ev(S, an(S, w) - 0.05, f"zincir + asma kilit iner (sekme 0.28 sn) — {w}", "darbe", "metal zincir/kilit")
S = "S18"; ev(S, an(S, "panic"), "harita batıdan doğuya griye döner (~12 sn)", "hareket", "")
ev(S, an(S, "notes"), "otel notu kartı", "kart", "kâğıt"); ev(S, an(S, "two"), "MARCH 6: NATIONWIDE BANK HOLIDAY", "pop", ""); ev(S, an(S, "franklin"), "radyo silueti", "pop", "radyo cızırtısı")
ev(S, an(S, "good"), "tüm noktalar söner", "hareket", ""); ev(S, an(S, "bank", 3) - 0.05, "kasa kapısına kilit iner", "darbe", "kilit")
ev(S, an(S, "for", 2) - 0.2, "C15 sokak: Box Leo yürür", "gecis", "ayak sesi"); ev(S, an(S, "insurance."), "INSURANCE kutusuna tik", "vurgu", "onay tik")
S = "S19"; ev(S, an(S, "lock"), "kilit modern kilide dönüşür", "vurgu", "parıltı/tık"); ev(S, an(S, "move") - 0.2, "kahve kapı raylarda kayar", "hareket", "ray sürtünmesi"); ev(S, an(S, "today."), "takvim 1933→2026", "flip", "")
S = "S20"; ev(S, an(S, "three"), "+3.7%", "vurgu", ""); ev(S, an(S, "nine"), "$1,000→$964 sayacı", "sayac", "aşağı ton"); ev(S, an(S, "buys"), "banknot destesi küçülür (≈4 sn)", "hareket", "")
S = "S21"; ev(S, an(S, "from"), "panel 1 çizilir", "kart", ""); ev(S, an(S, "from", 2), "panel 2 çizilir", "kart", ""); ev(S, an(S, "same"), "SAME BOX. OPPOSITE RESULT.", "vurgu", "")
S = "S22"; ev(S, an(S, "today,"), "1934 kilidi modern kilide dönüşür", "vurgu", "tık + parıltı")
S = "S23"; ev(S, an(S, "hurt"), "DISASTER etiketi", "pop", ""); ev(S, an(S, "came") - 0.1, "GAMBLE etiketi", "pop", ""); ev(S, an(S, "top."), "SURPRISE etiketi", "pop", "")
ev(S, an(S, "that's") - 0.2, "ekran kararır + tez yazısı", "vurgu", "")
S = "S24"; ev(S, 0, "ışıklar kısılır (3 sn)", "isik", ""); ev(S, an(S, "history"), "dördüncü kapı silueti belirir", "vurgu", "gizem tonu"); ev(S, an(S, "thanks"), "el sallama + THANKS FOR PLAYING", "pop", "")
O.sort(key=lambda o: o["t"])
veri = {"kaynak": "07-animasyon/efekt-cue.py (animasyon-yonetmeni)", "eksen": "04-ses/anlatim.wav (0 = anlatım başı)", "fps": 30, "olaylar": O}
for p in [U / "07-animasyon/efekt-cue.json", U / "06-muzik/animasyon-efekt-cue.json"]:
    json.dump(veri, open(p, "w"), ensure_ascii=False, indent=1)
print(len(O), "olay")
