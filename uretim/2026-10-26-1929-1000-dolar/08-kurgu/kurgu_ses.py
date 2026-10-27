#!/usr/bin/env python3
"""F7 kurgu sesi — 1929-1000-dolar (kurgu-editoru).

Kullanım:
  python3 08-kurgu/kurgu_ses.py ana      # sfx-kurgu stem'i + final miks (anlatım + müzik stem + sfx-kurgu) → git dışı wav
  python3 08-kurgu/kurgu_ses.py shorts   # Shorts yerleşimi (video/src/k1929/kurgu-veri.ts) + Shorts müzik/efekt wav'ları

Neden yeni SFX izi: F6 sfx-stem.wav'daki 53 vuruş kelime zamanına (cue-uret.py) bağlıydı; F5'in görsel olay listesi
(06-muzik/animasyon-efekt-cue.json, 109 olay) gerçek render'a göre. Karşılaştırma (kurgu-rapor.md §ses): 20+ vuruş
görselden 0.4–3 sn kayık (ör. S06 −13% çubuğu ses 122.28 / görüntü 125.08; S17 üç kilit sesi 476–478'de, görüntüde
harita varken; kilitler 451.8–452.7'de sessiz). Bu yüzden F6'nın dosya seçimi ve kazançları korunur, ZAMAN görsel
olaya taşınır; görseli olup sesi olmayan önemli olaylara aynı kütüphaneden (assets/efekt, 06-muzik/kaynak) düşük
kazançlı vuruş eklenir. Müzik stem'i (ducking dahil) olduğu gibi kullanılır.
İşleme f6.py ile aynı: dosya −3 dBFS tepeye normalize → olay kazancı (dB). Toplam = anlatım + müzik + sfx (ham);
son −14 LUFS normalizasyonu render-parca.sh / render-son.sh'de.
"""
import json, os, subprocess, sys
import numpy as np

SR = 48000
BURA = os.path.dirname(os.path.abspath(__file__))
UR = os.path.dirname(BURA)
REPO = os.path.abspath(os.path.join(UR, "..", ".."))
E, O, AE = f"{UR}/06-muzik/kaynak/efekt/", f"{UR}/06-muzik/kaynak/ozgun/", f"{REPO}/assets/efekt/"
CIKIS = os.environ.get("KURGU_CIKIS", os.path.expanduser("~/.finansal-arac/kurgu-1929"))
os.makedirs(CIKIS, exist_ok=True)


def coz(yol):
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", yol, "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(r, dtype=np.float32).reshape(-1, 2).copy()


def yaz(yol, x):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-", "-c:a", "pcm_s24le", yol],
                   input=np.ascontiguousarray(x, dtype=np.float32).tobytes(), check=True)


def dosya(ad):
    for d in (O, E, AE):
        if os.path.exists(d + ad):
            return d + ad
    raise FileNotFoundError(ad)


ONBELLEK = {}


def vurus(ad, db, sure=None, perde=None):
    k = (ad, db, sure, perde)
    if k in ONBELLEK:
        return ONBELLEK[k]
    x = coz(dosya(ad))
    if sure:
        x = x[:int(sure * SR)]
        f = min(len(x), int(0.15 * SR))
        x[-f:] *= np.linspace(1, 0, f)[:, None]
    if perde:
        oran = 2 ** (perde / 12)
        idx = np.arange(0, len(x) - 1, oran)
        x = np.stack([np.interp(idx, np.arange(len(x)), x[:, ch]) for ch in (0, 1)], 1).astype(np.float32)
    x = x / (np.abs(x).max() + 1e-9) * 10 ** (-3 / 20) * 10 ** (db / 20)
    ONBELLEK[k] = x
    return x


# ---- F6 cue.json vuruşlarının görsel olaya göre yeni zamanı (indeks → yeni t; None = F6 zamanı korunur, "SIL" = atılır)
# Eşleme kaynağı: animasyon-efekt-cue.json + render kare kontrolü (08-kurgu/kareler/ses-kontrol-*.jpg)
YENI_ZAMAN = {
    1: 2.08,      # kesme → stüdyo (flaş 2.10)
    6: 57.66, 7: 59.50,                       # kural kartları
    8: 61.88, 9: 63.80, 10: 65.87,            # klon yürüyüşleri başlar
    11: 70.62, 12: 70.66, 13: 70.70,          # kahkaha: punch-in 70.51 + "laughs"
    14: 80.00,    # bölüm geçişi whoosh → mavi panel 80.21
    15: "SIL",    # S05 106.32 "kapı açılır" sesi: o anda ekranda kapı yok (Stock Leo sokakta) → atıldı
    17: 125.08, 18: 129.16,                   # −13% / −12% çubukları
    19: 148.60,   # $500 buzzer: sayaç 147.52 + 1.1 sn sonunda
    20: 157.30,   # bölünmüş ekran → banka kasası açılır
    21: 165.40,   # RIGHT? sallanır (gerilim vuruşu "Right?" kelimesiyle aynı an)
    23: 234.17,   # G2 çubukları büyür (sayaç tıkırtısı)
    24: 263.88,   # GAMBLE damgası
    27: 275.66,   # spot kahve kapıya
    29: 318.52,   # banknot parıltısı (ka-ching)
    30: 354.25,   # "champion?" buzzer → NOT SO FAST damgası 354.43
    31: 359.36, 33: 362.12,                   # tuzak kartları (burn / lose)
    34: 370.95,   # whip-down 371.10 (rüzgâr + düşüş)
    35: 378.96,   # −89%
    37: 478.81,   # S17 "kasa kilidi" sesi → S18 kasa kapısına kilit iner (görsel 478.81)
    38: 473.06,   # radyo silueti
    39: 451.83, 40: 451.91, 41: 452.25, 42: 452.33, 43: 452.65, 44: 452.73,   # S18 üç kapı zincir+kilit → S17 kilit görseli
    45: 489.00,   # "~4,000 BANKS NEVER REOPENED" yazısı 489.0–489.2'de gelir (F6 488.2'de ekran boştu)
    47: 520.70,   # riser → kapı raylarda 521.02 / takvim 521.70 (yükselme görselden önce)
    48: 531.12,   # +3.7%
    49: 541.70,   # $964 kartı (sayaç 540.54 sonu)
    50: 565.25,   # SAME BOX. OPPOSITE RESULT.
    51: 588.50,   # $250,000 kartı 588.53'te belirir
}

# ---- Görseli olup sesi olmayan olaylara eklenen vuruşlar (t, dosya, dB, olay). Konuşma altı: kısa, −20..−24 dB.
EK = [
    (2.04, "whoosh-kisa.flac", -20, "S01 flaş kesmesi whoosh"),
    (10.92, "pop-pluck.flac", -22, "S01 DISASTER?"), (11.70, "pop-pluck.flac", -22, "S01 GAMBLE?"), (13.00, "pop-pluck.flac", -22, "S01 SURPRISE?"),
    (20.36, "tik-select.flac", -20, "S02 takvim 1929→2026"), (21.675, "tik-select.flac", -20, "S02 takvim 2026→1929"),
    (25.50, "whoosh-kisa.flac", -22, "S02 ekrana punch-in + soru (vaat)"),
    (42.29, "pop-pluck.flac", -22, "S03 G0 kartı"),
    (72.20, "whoosh-kisa.flac", -22, "S04 kesme: yakın plan sunucu"),
    (73.16, "ding-pwl-bell_ding1.flac", -24, "S04 göz kırpma ting"),
    (81.84, "pop-pluck.flac", -22, "S05 G1a grafik kartı"), (92.36, "pop-drop.flac", -20, "S05 ×6"),
    (109.96, "pop-drop.flac", -18, "S05 381.17 büyük sayı"),
    (120.72, "tik-select.flac", -20, "S06 takvim SEP→OCT"),
    (178.40, "whoosh-kisa.flac", -22, "S08 kesme: ABD haritası"),
    (212.50, "whoosh-kisa.flac", -21, "S09 ↺5 'Here's the problem' mekanizma kartı"),
    (214.04, "para-coin-drop.flac", -20, "S09 madeni paralar kasaya"),
    (223.68, "muhur-impact-punch.flac", -16, "S09 EMPTY damgası"),
    (251.06, "pop-drop.flac", -19, "S10 ~20¢ büyük sayı"),
    (277.16, "whoosh-kisa.flac", -22, "S11 kahve kapı punch-in"),
    (285.85, "ozgun-gerilim-vurus.flac", -17, "S11 ↺7 'something strange' sonrası"),
    (299.27, "pop-pluck.flac", -22, "S12 G3 TÜFE kartı"),
    (337.80, "whoosh-kisa.flac", -22, "S13 ↺8 sunucuya punch-in"),
    (357.85, "pop-pluck.flac", -19, "S14 tuzak kartı (earns)"),
    (375.58, "pop-pluck.flac", -21, "S15 41.22 dip etiketi"),
    (397.00, "pop-pluck.flac", -20, "S15 ↺10 BACK TO $1,000?"),
    (415.30, "pop-pluck.flac", -21, "S15 ~LATE 1936 çizgisi"),
    (422.56, "pop-pluck.flac", -20, "S16 skor sütunu STOCK"), (426.54, "pop-pluck.flac", -20, "S16 skor sütunu BANK"),
    (434.31, "pop-pluck.flac", -20, "S16 skor sütunu BOX"),
    (470.92, "pop-drop.flac", -20, "S18 MARCH 6 bank holiday"),
    (496.04, "tik-click.flac", -18, "S18 INSURANCE tik"),
    (510.58, "tik-click.flac", -18, "S19 kilit modern kilide"),
    (551.19, "pop-pluck.flac", -22, "S21 panel 1"), (558.07, "pop-pluck.flac", -22, "S21 panel 2"),
    (584.67, "tik-click.flac", -18, "S22 1934 kilidi modern kilide"),
    (592.80, "whoosh-kisa.flac", -21, "S23 ↺13 kesme: final kapılar"),
    (597.06, "pop-pluck.flac", -20, "S23 DISASTER"), (599.44, "pop-pluck.flac", -20, "S23 GAMBLE"),
    (630.65, "pop-pluck.flac", -20, "S24 THANKS FOR PLAYING"),
]


def ana_plan():
    cue = json.load(open(f"{UR}/06-muzik/cue.json"))
    plan = []
    for i, s in enumerate(cue["sfx"]):
        yt = YENI_ZAMAN.get(i)
        if yt == "SIL":
            continue
        ad = os.path.basename(s["dosya"].split("/", 1)[1])
        t = s["t"] if yt is None else yt
        plan.append({"t": round(t, 3), "dosya": ad, "db": s["db"], "sure": s.get("sure"), "perde": s.get("perde"),
                     "olay": s["olay"], "kaynak": "F6" if yt is None else f"F6→{s['t']}"})
    for t, ad, db, olay in EK:
        plan.append({"t": t, "dosya": ad, "db": db, "sure": None, "perde": None, "olay": olay, "kaynak": "F7 ek"})
    return sorted(plan, key=lambda p: p["t"])


def ana():
    narr = coz(f"{UR}/04-ses/anlatim.wav")
    n = len(narr)
    muz = coz(f"{UR}/06-muzik/stems/muzik-stem.wav")[:n]
    sfx = np.zeros((n, 2), np.float32)
    plan = ana_plan()
    for p in plan:
        x = vurus(p["dosya"], p["db"], p["sure"], p["perde"])
        i = int(round(p["t"] * SR)); j = min(n, i + len(x))
        sfx[i:j] += x[:j - i]
    yaz(f"{CIKIS}/sfx-kurgu-stem.wav", sfx)
    yaz(f"{CIKIS}/final-miks.wav", narr + muz + sfx)
    json.dump(plan, open(f"{BURA}/sfx-kurgu-plan.json", "w"), ensure_ascii=False, indent=0)
    print(f"vuruş {len(plan)} (F6 korunan/taşınan {sum(p['kaynak'] != 'F7 ek' for p in plan)}, ek {len(EK)}) → {CIKIS}/final-miks.wav")


# ---------------- Shorts ----------------
# Her parça: (tür, kaynak, global/yerel başlangıç, bitiş). Sahne başları altyazı öbeği başına (öbek ilk kelimesi −0.08 sn) oturtulur:
# daha erken kesilirse önceki cümlenin son kelimesi 1–2 kare görünür (ilk render: Shorts 2 S20 başında "TWENTY-FIVE.").
# "ek" = DEk kaydı (yerel zaman), "sahne" = dikey sahne (global zaman)
SHORTS = {
    "sh1": {"muzik": "shorts-1-muzik-stem.wav", "kopru": 1.4, "erken": 2.48, "parcalar": [
        ("ek", "sh1", 0.0, 3.96),
        ("sahne", "S01", 2.10, 8.03),
        ("sahne", "S06", 145.45, 149.30),
        ("sahne", "S10", 230.118, 240.35),
        ("sahne", "S16", 419.767, 438.65),
        ("ek", "sh1", 4.30, 9.62),
    ]},
    "sh2": {"muzik": "shorts-2-muzik-stem.wav", "kopru": 2.6, "parcalar": [
        ("ek", "sh2", 0.0, 6.66),
        ("sahne", "S12", 301.45, 316.30),
        ("sahne", "S20", 528.13, 543.95),
        ("sahne", "S20", 546.94, 548.45),     # atlama kesmesi (banknot görseli üstünde; "Nothing was stolen…" çıkarıldı)
        ("sahne", "S21", 565.17, 579.75),
    ]},
}
# Shorts efektleri: (global zaman veya ("ek", yerel), dosya, dB) — ana videodaki aynı olay dosyası ve kazancı
SHORTS_SFX = {
    "sh1": [(4.94, "pop-pluck.flac", -20), (5.82, "pop-pluck.flac", -20), (6.62, "pop-pluck.flac", -20),
            (148.60, "ozgun-buzzer-yanlis.flac", -15), (234.17, "ozgun-sayac-tikirti.flac", -21),
            (419.80, "ozgun-ding-oyunsovu.flac", -18), (422.56, "pop-pluck.flac", -20), (426.54, "pop-pluck.flac", -20), (434.31, "pop-pluck.flac", -20)],
    "sh2": [(312.16, "ozgun-sayac-tikirti.flac", -21), (531.12, "ozgun-sayac-tikirti.flac", -21), (541.70, "pop-drop.flac", -16),
            (565.25, "muhur-impact-punch.flac", -12)],
}
FPS = 30


def shorts():
    veri = {}
    for ad, sh in SHORTS.items():
        bas_k = 0; parcalar = []
        for tur, kay, a, b in sh["parcalar"]:
            ka, kb = round(a * FPS), round(b * FPS)
            parcalar.append({"tur": tur, "kaynak": kay, "bas": a, "son": b, "kareBas": ka, "sure": kb - ka, "yer": bas_k})
            bas_k += kb - ka
        kopru = round(sh["kopru"] * FPS)
        son = parcalar[-1]
        if son["tur"] == "ek":
            son["sure"] += kopru   # ek kaydın sesi bitmiş olur → köprü aynı görüntü üstünde
        else:
            # sahne parçası uzatılırsa anlatımın SONRAKİ cümlesi sızar (ilk render'da "…too" duyuldu) → sessiz, altyazısız kuyruk
            parcalar.append({"tur": "kuyruk", "kaynak": son["kaynak"], "bas": son["son"], "son": son["son"] + sh["kopru"],
                             "kareBas": son["kareBas"] + son["sure"], "sure": kopru, "yer": son["yer"] + son["sure"]})
        toplam = sum(p["sure"] for p in parcalar)
        # köprü kartı: Shorts 1'de kapanış cümlesi "Why that flips today is in the full video" (ek 7.14 sn) ile birlikte girer
        veri[ad] = {"toplam": toplam, "kopruBas": toplam - kopru - round(sh.get("erken", 0) * FPS), "parcalar": parcalar}
        # ses: müzik yatağı kesit uzunluğuna kırpılır, son 2 sn sönüş korunur; efektler kesit zamanına taşınır
        n = int(round(toplam / FPS * SR))
        m = coz(f"{UR}/06-muzik/stems/{sh['muzik']}")
        m = m[:n].copy() if len(m) >= n else np.pad(m, ((0, n - len(m)), (0, 0)))
        c = int(2.0 * SR); m[-c:] *= np.cos(np.linspace(0, np.pi / 2, c))[:, None]
        for t, f_, db in SHORTS_SFX[ad]:
            for p in parcalar:
                if p["tur"] == "sahne" and p["bas"] <= t < p["son"]:
                    i = int(round((p["yer"] / FPS + t - p["bas"]) * SR))
                    x = vurus(f_, db); j = min(n, i + len(x)); m[i:j] += x[:j - i]
        kb = int(round(veri[ad]["kopruBas"] / FPS * SR))
        x = vurus("whoosh-kisa.flac", -20); j = min(n, kb + len(x)); m[kb:j] += x[:j - kb]
        yaz(f"{REPO}/video/public/k1929t/{ad}-yatak.wav", m)
        print(ad, "toplam", toplam, "kare =", round(toplam / FPS, 2), "sn")
    ts = ("// Otomatik üretildi: uretim/2026-10-26-1929-1000-dolar/08-kurgu/kurgu_ses.py shorts — elle düzenleme.\n"
          "export type KParca = {tur: string; kaynak: string; bas: number; son: number; kareBas: number; sure: number; yer: number};\n"
          f"export const KURGU_SHORTS: Record<string, {{toplam: number; kopruBas: number; parcalar: KParca[]}}> = {json.dumps(veri)};\n")
    open(f"{REPO}/video/src/k1929/kurgu-veri.ts", "w").write(ts)


if __name__ == "__main__":
    {"ana": ana, "shorts": shorts}[sys.argv[1]]()
