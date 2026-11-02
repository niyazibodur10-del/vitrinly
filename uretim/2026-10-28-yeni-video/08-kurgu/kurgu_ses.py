#!/usr/bin/env python3
"""F7 kurgu sesi + yerleşim — 2026-10-28-yeni-video (S08 Kitchen Table Budget), kurgu-editoru.
Kaynak desen: uretim/2026-10-26-1929-1000-dolar/08-kurgu/kurgu_ses.py (v2: SFX yeniden zamanlanmaz, yalnız doğrulanır).

Kullanım (repo kökünden, $PY = ~/.finansal-arac/venv/bin/python):
  $PY 08-kurgu/kurgu_ses.py veri     # kurgu-veri.ts (abone + Shorts yerleşimi) — render'dan önce
  $PY 08-kurgu/kurgu_ses.py ana      # final miks = anlatım + müzik stem + sfx stem (F6, dokunulmaz) + abone klikleri → git dışı wav
  $PY 08-kurgu/kurgu_ses.py shorts   # Shorts yatakları (shorts müzik stem + ana sfx-stem dilimleri + abone klik + köprü whoosh)
  $PY 08-kurgu/kurgu_ses.py dogrula  # SFX hizası (±2 kare, görsel olaya) + klik ↔ görsel tıklama karesi

SFX: F6 sfx-stem.wav olduğu gibi (vuruşlar animasyon-efekt-cue.json görsel olaylarına bağlı, F6 kendi kapısı 0 kayık).
Burada bağımsız doğrulama: cue.json'daki her vuruşun t_olay'ı animasyon-efekt-cue.json'da bir görsel olay mı (≤0,5 kare) +
F6'nın stem çapraz ilinti kontrolü (06-muzik/sfx-kare-kontrol.py) yeniden koşar. Kayık vuruş çıkarsa liste muzik-ses-tasarimcisi'ne.
Shorts SFX = ana sfx-stem'in aynı zaman dilimi (dikey sahneler aynı zaman planını — zaman.ts — kullanır → aynı olay karesi).
Son −14 LUFS normalizasyonu render-parca.sh / render-son.sh'de.
"""
import json, os, subprocess, sys
import numpy as np

SR, FPS = 48000, 30
BURA = os.path.dirname(os.path.abspath(__file__))
UR = os.path.dirname(BURA)
REPO = os.path.abspath(os.path.join(UR, "..", ".."))
AE = f"{REPO}/assets/efekt/"
CIKIS = os.environ.get("KURGU_CIKIS", os.path.expanduser("~/.finansal-arac/kurgu-kbutce"))
PUB = f"{REPO}/video/public/kbutce"
TS = f"{REPO}/video/src/videolar/yeni-video/kurgu-veri.ts"


def coz(yol):
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", yol, "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(r, dtype=np.float32).reshape(-1, 2).copy()


def yaz(yol, x):
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-", "-c:a", "pcm_s24le", yol],
                   input=np.ascontiguousarray(x, dtype=np.float32).tobytes(), check=True)


def vurus(ad, db):
    x = coz(AE + ad)
    return x / (np.abs(x).max() + 1e-9) * 10 ** (-3 / 20) * 10 ** (db / 20)


# ---------------- Abone ol (video/src/ortak/AboneOl.tsx) ----------------
# Bileşende tıklama karesi = Sequence başı + round(ABONE_KLIK_SN*30) = +39 kare. Yerleşim tamsayı KARE ile → ses aynı kareye örnek-doğru.
ABONE_KLIK_KARE = 39
ABONE_KLIK = ("ozgun-fare-klik.flac", -17)   # 1929 ile aynı kazanç (klik_maske kapısından geçmişti)
ABONE_ANA = [  # (bas kare, süre kare, taraf, üst px | None) — gerekçe kurgu-rapor.md §4
    (5266, 105, "sag", None),  # ABONE-1 175.547 (S07 sonu nefes → S08 "Let's open the loan statement"); defter kartı solda
    (9152, 105, "sol", None),  # ABONE-2 305.082 (S12 doruk sonrası nefes); S13'te kırmızı INTEREST zarfı SAĞ altta → kart solda
    (13488, 105, "sag", 640),  # ABONE-4 449.6 (S18 "Which one is better is an argument for voters…" — tarafsızlık notu, doruk/açıklama değil);
                               #   Leo yakın plan, sağ el y≈830 → kart üst 640; S19 doruğu (454.87) başlamadan biter (453.1)
    (19878, 105, "sol", None), # ABONE-3 662.614 (S26 sonu nefes → S27 köprü); sağda kupa
]

# ---------------- Shorts ----------------
# Parça: (tür, kaynak, baş, son) — "ek" = DEk kaydı yerel sn; "sahne" = dikey sahne, GLOBAL sn (anlatim.wav ekseni).
# Sahne başları altyazı öbeği başına (öbek ilk kelimesi −0,08 sn), sonları sonraki öbek başından önce (cümle sızmaz).
SHORTS = {
    "sh1": {"muzik": "shorts-1-muzik-stem.wav", "ekses": "shorts-1-ek.wav", "kopru": 0.9, "parcalar": [
        ("ek", "sh1", 0.0, 6.80),                 # HOOK: "If the U.S. were a family earning $5,400 a month, this is its interest bill."
        ("sahne", "S06", 112.006, 115.30),        # "Envelope four: defense. The entire military."
        ("sahne", "S06", 117.594, 119.55),        # "Nine hundred sixty-five dollars."  (Ships/planes… atlandı)
        ("sahne", "S06", 119.678, 122.40),        # "Now look at envelope five. No logo."
        ("sahne", "S06", 123.715, 127.70),        # "Just one word: interest. About one thousand fifty dollars."
        ("sahne", "S06", 134.776, 139.25),        # "This household pays its lenders more than it pays for its whole military."
        ("sahne", "S12", 275.995, 281.30),        # "Watch what happens when I open it. Inside, there's another envelope. It says: borrowed."
        ("sahne", "S12", 282.49, 305.30),         # "The monthly gap… Interest, inside borrowed, inside interest." ("Here's why." atlandı)
        ("ek", "sh1", 6.906, 12.006),             # "Interest is the one bill that buys nothing. The whole kitchen table is in the long video."
    ], "abone": ("ek_bas", 0.0, 78, None)},       # 2. ek parçasının başından, 2,6 sn; köprü cümlesinden (9,56) önce biter
    "sh2": {"muzik": "shorts-2-muzik-stem.wav", "ekses": "shorts-2-ek.wav", "kopru": 2.4, "parcalar": [
        ("ek", "sh2", 0.0, 4.45),                 # HOOK: "In 1946, U.S. debt was bigger than the whole economy."
        ("sahne", "S19", 468.146, 476.20),        # "By 1974, it was under a quarter of it. And here's the strange part. The debt itself didn't shrink. It actually grew."
        ("ek", "sh2", 4.514, 8.60),               # "The economy grew around it, and prices rose too. How?"
        ("sahne", "S16", 390.969, 400.25),        # "Thing one: it borrows in its own money. A family borrows dollars… its own currency."
        ("sahne", "S17", 418.006, 425.20),        # "Thing two: it never retires. A family has to pay off… A country has no last payday."
        ("sahne", "S19", 482.987, 487.40),        # "A family can't grow its way out of a loan like that. A country did."
        ("ek", "sh2", 12.997, 14.983),            # "This is history, not a forecast."
    ], "abone": ("son", 0.0, 78, None)},          # köprü kartından hemen önce biter
}


def kare(s):
    return int(round(s * FPS))


def sahne_bas():
    import re
    s = open(f"{REPO}/video/src/videolar/yeni-video/veri-sahne.ts").read()
    S = json.loads(re.search(r"export const SAHNELER[^=]*=\s*(\[.*?\]);\n", s, re.S).group(1))
    return {x["id"]: x["bas"] for x in S}


def shorts_plan():
    veri = {}
    for ad, sh in SHORTS.items():
        yer = 0; parcalar = []
        for tur, kay, a, b in sh["parcalar"]:
            ka, kb = kare(a), kare(b)
            parcalar.append({"tur": tur, "kaynak": kay, "bas": a, "son": b, "kareBas": ka, "sure": kb - ka, "yer": yer})
            yer += kb - ka
        kopru = kare(sh["kopru"])
        son = parcalar[-1]
        if son["tur"] == "ek":
            son["sure"] += kopru          # ek sesi bitmiş olur → köprü aynı görüntü üstünde (ek DEk görüntüsü sürer)
        toplam = sum(p["sure"] for p in parcalar)
        tip, ofs, sure, ust = sh["abone"]
        if tip == "ek_bas":
            ab = parcalar[-1]["yer"] + kare(ofs)
            kopru_bas = parcalar[-1]["yer"] + kare(9.50 - 6.906)   # köprü cümlesi "The whole kitchen table…" ek 9,558
        else:
            kopru_bas = toplam - kopru
            ab = kopru_bas - sure
        assert ab + sure <= kopru_bas, f"{ad}: abone köprüye biniyor"
        veri[ad] = {"toplam": toplam, "kopruBas": kopru_bas, "parcalar": parcalar, "abone": {"kare": ab, "sure": sure, "ust": ust}}
    return veri


def veri():
    v = shorts_plan()
    for ad, x in v.items():
        print(ad, "toplam", x["toplam"], "kare =", round(x["toplam"] / FPS, 2), "sn · abone", x["abone"], "· köprü", x["kopruBas"])
    ts = ("// Otomatik üretildi: uretim/2026-10-28-yeni-video/08-kurgu/kurgu_ses.py veri — elle düzenleme.\n"
          "export type KParca = {tur: string; kaynak: string; bas: number; son: number; kareBas: number; sure: number; yer: number};\n"
          "export type KShorts = {toplam: number; kopruBas: number; parcalar: KParca[]; abone: {kare: number; sure: number; ust: number | null}};\n"
          f"export const KURGU_SHORTS: Record<string, KShorts> = {json.dumps(v)};\n"
          f"export const ABONE_ANA: {{kare: number; sure: number; taraf: \"sol\" | \"sag\"; ust: number | null}}[] = "
          f"{json.dumps([{'kare': b, 'sure': d, 'taraf': k, 'ust': u} for b, d, k, u in ABONE_ANA])};\n")
    open(TS, "w").write(ts)


def ana():
    os.makedirs(CIKIS, exist_ok=True)
    narr = coz(f"{UR}/04-ses/anlatim.wav")
    n = len(narr)
    muz = coz(f"{UR}/06-muzik/stems/muzik-stem.wav")
    sfx = coz(f"{UR}/06-muzik/stems/sfx-stem.wav")
    assert len(muz) == n == len(sfx), (len(muz), n, len(sfx))
    klik = np.zeros((n, 2), np.float32)
    x = vurus(*ABONE_KLIK)
    for b, _, _, _ in ABONE_ANA:
        i = int(round((b + ABONE_KLIK_KARE) / FPS * SR)); j = min(n, i + len(x)); klik[i:j] += x[:j - i]
    yaz(f"{CIKIS}/final-miks-kliksiz.wav", narr + muz + sfx)
    yaz(f"{CIKIS}/final-miks.wav", narr + muz + sfx + klik)
    print("klik (sn):", [round((b + ABONE_KLIK_KARE) / FPS, 3) for b, *_ in ABONE_ANA], "→", f"{CIKIS}/final-miks.wav")


def shorts():
    v = shorts_plan()
    sfx_ana = coz(f"{UR}/06-muzik/stems/sfx-stem.wav")
    for ad, sh in SHORTS.items():
        p = v[ad]
        n = int(round(p["toplam"] / FPS * SR))
        m = coz(f"{UR}/06-muzik/stems/{sh['muzik']}")
        m = m[:n].copy() if len(m) >= n else np.pad(m, ((0, n - len(m)), (0, 0)))
        c = int(1.5 * SR); m[-c:] *= np.cos(np.linspace(0, np.pi / 2, c))[:, None]
        g = int(0.01 * SR)
        for q in p["parcalar"]:
            if q["tur"] != "sahne":
                continue
            a = int(round(q["kareBas"] / FPS * SR)); L = int(round(q["sure"] / FPS * SR))
            d = sfx_ana[a:a + L].copy(); d[:g] *= np.linspace(0, 1, g)[:, None]; d[-g:] *= np.linspace(1, 0, g)[:, None]
            i = int(round(q["yer"] / FPS * SR)); m[i:i + len(d)] += d[:n - i]
        i = int(round((p["abone"]["kare"] + ABONE_KLIK_KARE) / FPS * SR)); x = vurus(*ABONE_KLIK); j = min(n, i + len(x)); m[i:j] += x[:j - i]
        kb = int(round(p["kopruBas"] / FPS * SR)); x = vurus("whoosh-kisa.flac", -20); j = min(n, kb + len(x)); m[kb:j] += x[:j - kb]
        yaz(f"{PUB}/{ad}-yatak.wav", m)
        print(ad, round(p["toplam"] / FPS, 2), "sn →", f"{PUB}/{ad}-yatak.wav")


def dogrula():
    cue = json.load(open(f"{UR}/06-muzik/cue.json"))
    olay = json.load(open(f"{UR}/06-muzik/animasyon-efekt-cue.json"))["olaylar"]
    gorsel = np.array([o["t"] for o in olay if o["tur"] != "abone"])
    kayik = []; ilk = {}
    for s in cue["sfx"]:   # olay başına İLK vuruş kapıya girer; aynı olayın sonraki vuruşları tasarlanmış dizi (sayaç tıkırtısı, yanıp sönme)
        ilk.setdefault(s["t_olay"], s)
    for s in ilk.values():
        d = np.abs(gorsel - s["t_olay"]).min() * FPS
        vur = (s["t"] - s.get("kirp", 0) + s["vurus_ofset"] - s["t_olay"]) * FPS
        if d > 0.5 or abs(vur) > 2:
            kayik.append((s["t"], s["olay"], round(float(d), 2), round(vur, 2)))
    print(f"cue vuruş {len(cue['sfx'])} ({len(ilk)} olay; dizi devamı {len(cue['sfx']) - len(ilk)}) · ilk vuruş görsel olaya bağlı (≤0,5 kare) + vuruş noktası ±2 kare · kayık: {len(kayik)} {kayik[:8]}")
    r = subprocess.run([sys.executable, f"{UR}/06-muzik/sfx-kare-kontrol.py"], capture_output=True, text=True)
    print("stem:", r.stdout.strip())
    # klik: ses başlangıcı (final miks − kliksiz miks farkı, ilk −30 dB aşımı) ↔ görsel tıklama karesi
    a, b = coz(f"{CIKIS}/final-miks-kliksiz.wav"), coz(f"{CIKIS}/final-miks.wav")
    fark = np.abs(b - a).max(1)
    for k, *_ in ABONE_ANA:
        tv = (k + ABONE_KLIK_KARE) / FPS
        i0 = int((tv - 0.5) * SR); w = fark[i0:i0 + SR]
        on = i0 + int(np.argmax(w > w.max() * 10 ** (-30 / 20)))
        print(f"abone kare {k}: görsel tık {tv:.3f} sn · ses başı {on / SR:.3f} sn · fark {(on / SR - tv) * FPS:+.2f} kare")
    sys.exit(1 if kayik or r.returncode else 0)


if __name__ == "__main__":
    {"veri": veri, "ana": ana, "shorts": shorts, "dogrula": dogrula}[sys.argv[1]]()
