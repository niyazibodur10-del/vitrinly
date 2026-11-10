#!/usr/bin/env python3
"""Flip By Vote ses kimliği üretici — kendi üretimimiz (sentez, sabit tohum; aynı komut = aynı bayt).
Kullanım: ~/.finansal-arac/earshot-venv/bin/python uret.py <cikis_klasoru> [ad ...]
Adaylar: jingle-a/b/c, dongu-a/b/c, gerilim-a/b/c, sfx-tahta-kisa, sfx-tahta-uzun, sfx-plak-cizik, sfx-kutu-tikirti.
Çıktı: 48 kHz stereo 24-bit wav (kapalı döngüler dikişsiz)."""
import os, sys
import numpy as np
import soundfile as sf
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sentez import (SR, nota, filtre, ks, marimba, glock, kick, gurultu, snap, clap, shaker, pad,
                    yerlestir, dongu_kapat, tepe_norm, oda, zarf, yatak_eq)


def tuval(sn):
    return np.zeros((2, int(sn * SR)))


# ---------------------------------------------------------------- JINGLE (≤1,8 sn, ön yüklü: ana notalar 0–0,5 sn)
def jingle_a():
    """'coin flip': dönen bozuk para tınısı (3 ting hızlanarak) → marimba F5-A5-C6 → F majör akor + glock."""
    rng = np.random.default_rng(11); y = tuval(1.8)
    for i, (t, f) in enumerate([(0.00, 2637), (0.07, 2794), (0.12, 3136)]):
        yerlestir(y, glock(f, 0.25), t, 0.10, pan=-0.3 + 0.3 * i)
    for t, n in [(0.16, "F5"), (0.25, "A5"), (0.34, "C6")]:
        yerlestir(y, marimba(nota(n), 0.6), t, 0.55, pan=0.1)
    for n in ("F4", "A4", "C5", "F5"):
        yerlestir(y, marimba(nota(n), 1.4), 0.45, 0.30)
    yerlestir(y, glock(nota("C7"), 1.3), 0.45, 0.10, pan=0.25)
    yerlestir(y, ks(nota("F2"), 1.2, rng, 0.35, 0.995), 0.45, 0.55)
    yerlestir(y, kick(0.3), 0.45, 0.45)
    y = oda(y, rng, 0.15)
    y[:, -int(0.25 * SR):] *= np.linspace(1, 0, int(0.25 * SR))
    return tepe_norm(y, -1.0)


def jingle_b():
    """'slap + ka-ching': slap bas riff F2-F3-C3-Eb3 + şıklatma → kasa zili (glock + metal gürültü)."""
    rng = np.random.default_rng(12); y = tuval(1.8)
    for t, n in [(0.00, "F2"), (0.11, "F3"), (0.22, "C3"), (0.33, "Eb3")]:
        yerlestir(y, ks(nota(n), 0.35, rng, 0.8, 0.990), t, 0.7)
        yerlestir(y, gurultu(0.02, rng, "bp", (2000, 5000), cozul=0.006), t, 0.15)
    yerlestir(y, snap(rng), 0.22, 0.3, pan=0.3)
    yerlestir(y, kick(0.3), 0.44, 0.5)
    for f, g in [(nota("E6"), 0.25), (nota("B6"), 0.18), (nota("E7"), 0.10)]:
        yerlestir(y, glock(f, 1.3), 0.44, g, pan=0.15)
    yerlestir(y, gurultu(0.35, rng, "high", 5000, cozul=0.08), 0.44, 0.10)
    yerlestir(y, ks(nota("F2"), 1.2, rng, 0.5, 0.995), 0.44, 0.5)
    y = oda(y, rng, 0.12)
    y[:, -int(0.3 * SR):] *= np.linspace(1, 0, int(0.3 * SR))
    return tepe_norm(y, -1.0)


def jingle_c():
    """'ıslık': üç notalı ıslık C6-A5-F6 (vibrato + nefes) + pop + bas."""
    rng = np.random.default_rng(13); y = tuval(1.8)
    for t, n, d in [(0.00, "C6", 0.14), (0.16, "A5", 0.14), (0.32, "F6", 0.9)]:
        m = int(d * SR); tt = np.arange(m) / SR
        f = nota(n) * (1 + 0.012 * np.sin(2 * np.pi * 6 * tt) * np.clip(tt / 0.2, 0, 1))
        s = np.sin(2 * np.pi * np.cumsum(f) / SR) * zarf(m, 0.02, d * 1.5, 1.0)
        s *= np.clip((d - tt) / 0.05, 0, 1)
        nf = filtre(rng.standard_normal(m), "bp", (nota(n) * 0.9, nota(n) * 1.3)) * 0.05 * zarf(m, 0.02, d, 1)
        yerlestir(y, s + nf, t, 0.35)
    yerlestir(y, ks(nota("F2"), 1.2, rng, 0.4, 0.995), 0.32, 0.55)
    yerlestir(y, kick(0.3), 0.32, 0.4)
    for n in ("A4", "C5", "F5"):
        yerlestir(y, marimba(nota(n), 1.2), 0.32, 0.2)
    y = oda(y, rng, 0.18)
    y[:, -int(0.3 * SR):] *= np.linspace(1, 0, int(0.3 * SR))
    return tepe_norm(y, -1.0)


# ---------------------------------------------------------------- DÖNGÜLER (8 ölçü, dikişsiz)
def _dongu(bpm, akorlar, ciz, tohum, sw=0.0):
    rng = np.random.default_rng(tohum)
    vur = 60 / bpm; olc = 4 * vur; n = int(round(8 * olc * SR))
    y = np.zeros((2, n + int(3 * SR)))
    for b in range(8):
        ciz(y, b * olc, vur, akorlar[b % len(akorlar)], b, rng, sw)
    y = yatak_eq(oda(y, rng, 0.10))
    return tepe_norm(dongu_kapat(y, n), -1.0)


def _o(t0, vur, on6, sw):  # 16'lık konum → sn (8'lik swing)
    t = t0 + on6 * vur / 4
    if sw and on6 % 4 == 2:
        t += sw * vur / 4
    return t


def dongu_a():
    """'Garage Sale Strut' 112 BPM F majör: slap bas, şıklatma 2–4, shaker, marimba offbeat vuruşları (sitcom)."""
    ak = [("F2", ["A4", "C5", "F5"]), ("D2", ["A4", "D5", "F5"]), ("Bb1", ["Bb4", "D5", "F5"]), ("C2", ["G4", "C5", "E5"])]

    def ciz(y, t0, v, ak1, b, rng, sw):
        kok, ust = ak1; fk = nota(kok)
        for on6, carp, g in [(0, 1, 0.8), (3, 1, 0.45), (6, 2, 0.55), (8, 1.5, 0.6), (10, 1, 0.45), (12, 2, 0.35), (14, 1.5, 0.5)]:
            yerlestir(y, ks(fk * carp, 0.32, rng, 0.45, 0.991), _o(t0, v, on6, sw), g)
        for on6 in (4, 12):
            yerlestir(y, snap(rng), _o(t0, v, on6, sw), 0.22, pan=0.35)
        for on6 in range(0, 16, 2):
            yerlestir(y, shaker(rng), _o(t0, v, on6, sw), 0.05 if on6 % 4 else 0.03, pan=-0.4)
        for on6 in (0, 10):
            yerlestir(y, kick(0.3, 95, 45), _o(t0, v, on6, sw), 0.45)
        for on6 in (6, 14):
            for k, n in enumerate(ust):
                yerlestir(y, marimba(nota(n), 0.45, 0.6), _o(t0, v, on6, sw) + 0.004 * k, 0.11, pan=0.2)
        if b in (3, 7):  # ölçü sonu küçük dolgu (tek nota hattı, konuşmaya girmeyecek kadar kısa)
            for on6, n in [(12, "C5"), (13, "D5"), (14, "F5")]:
                yerlestir(y, marimba(nota(n), 0.4, 0.5), _o(t0, v, on6, sw), 0.12, pan=0.1)
    return _dongu(112, ak, ciz, 21)


def dongu_b():
    """'Flip Hustle' 124 BPM C majör: pizzicato arpej, yumuşak kick/clap, shaker 16'lık, seyrek glock."""
    ak = [("C2", ["C4", "E4", "G4", "C5"]), ("A1", ["A3", "C4", "E4", "A4"]), ("F1", ["F3", "A3", "C4", "F4"]), ("G1", ["G3", "B3", "D4", "G4"])]

    def ciz(y, t0, v, ak1, b, rng, sw):
        kok, ust = ak1; fk = nota(kok)
        for on6, carp, g in [(0, 1, 0.8), (6, 1, 0.5), (8, 2, 0.5), (14, 1.5, 0.45)]:
            yerlestir(y, ks(fk * carp, 0.4, rng, 0.5, 0.993), _o(t0, v, on6, sw), g)
        for i, on6 in enumerate(range(0, 16, 2)):
            n = ust[[0, 1, 2, 3, 2, 1, 2, 3][i]]
            yerlestir(y, ks(nota(n), 0.22, rng, 0.55, 0.975), _o(t0, v, on6, sw), 0.20, pan=-0.25 + 0.5 * (i % 2))
        for on6 in (0, 8):
            yerlestir(y, kick(0.3, 100, 48), _o(t0, v, on6, sw), 0.5)
        for on6 in (4, 12):
            yerlestir(y, clap(rng), _o(t0, v, on6, sw), 0.12, pan=0.1)
        for on6 in range(16):
            yerlestir(y, shaker(rng, 0.05), _o(t0, v, on6, sw), 0.035 if on6 % 2 else 0.02, pan=0.45)
        if b % 2 == 0:
            yerlestir(y, glock(nota(ust[-1]) * 2, 1.0), t0, 0.05, pan=0.3)
    return _dongu(124, ak, ciz, 22)


def dongu_c():
    """'Porch Shuffle' 96 BPM G majör swing: ukulele vuruşu (KS akor), bas 1–3, fırça 2–4."""
    ak = [("G2", ["G4", "B4", "D5", "G5"]), ("E2", ["G4", "B4", "E5", "G5"]), ("C2", ["G4", "C5", "E5", "G5"]), ("D2", ["F#4", "A4", "D5", "A5"])]

    def ciz(y, t0, v, ak1, b, rng, sw):
        kok, ust = ak1; fk = nota(kok)
        for on6, carp, g in [(0, 1, 0.75), (8, 1.5, 0.6), (14, 1, 0.35)]:
            yerlestir(y, ks(fk * carp, 0.5, rng, 0.4, 0.994), _o(t0, v, on6, sw), g)
        for on6, yon, g in [(0, 1, 1.0), (4, 1, 0.8), (6, -1, 0.55), (10, -1, 0.55), (12, 1, 0.8), (14, -1, 0.5)]:
            sira = ust if yon > 0 else ust[::-1]
            for k, n in enumerate(sira):
                yerlestir(y, ks(nota(n), 0.35, rng, 0.6, 0.982), _o(t0, v, on6, sw) + 0.007 * k, 0.07 * g, pan=-0.2)
        for on6 in (4, 12):
            yerlestir(y, gurultu(0.12, rng, "bp", (2500, 9000), atak=0.004, cozul=0.06), _o(t0, v, on6, sw), 0.10, pan=0.3)
    return _dongu(96, ak, ciz, 23, sw=0.33)


# ---------------------------------------------------------------- GERİLİM (karar anı; 8 ölçü dikişsiz, 4 ölçüde yoğunlaşır)
def gerilim_a():
    """'Game-show clock' 96 BPM D minör: saat tik-tak 8'lik, nabız bas her vuruşta, Dm pad tremolo + A–Bb yarım ton pizz."""
    rng = np.random.default_rng(31); bpm = 96; v = 60 / bpm; olc = 4 * v; n = int(round(8 * olc * SR))
    y = np.zeros((2, n + int(3 * SR)))
    for b in range(8):
        t0 = b * olc
        for i in range(8):
            f = 4800 if i % 2 == 0 else 4200
            m = int(0.02 * SR); tt = np.arange(m) / SR
            yerlestir(y, np.sin(2 * np.pi * f * tt) * np.exp(-tt * 400), t0 + i * v / 2, 0.10, pan=0.4 * (1 if i % 2 else -1))
        for i in range(4):
            yerlestir(y, kick(0.4, 70, 40), t0 + i * v, 0.55 if i == 0 else 0.35)
            yerlestir(y, ks(nota("D2"), 0.4, rng, 0.3, 0.992), t0 + i * v, 0.40)
            yerlestir(y, ks(nota("A3") if i % 2 == 0 else nota("Bb3"), 0.25, rng, 0.7, 0.98), t0 + i * v + v / 2, 0.16 + 0.02 * (b % 4), pan=0.2)
    p = pad([nota("D3"), nota("F3"), nota("A3")], 8 * olc, rng, kesim=900, atak=3.0, birak=0.01, trem=6.0)
    yerlestir(y, p, 0, 0.9)
    y = yatak_eq(oda(y, rng, 0.10))
    return tepe_norm(dongu_kapat(y, n), -1.0)


def gerilim_b():
    """'Sneaky pizz' 100 BPM D minör: kromatik iniş pizzicato 8'lik (D–F–A–G#–A–F–E–Eb), staccato bas, şıklatma 2–4."""
    rng = np.random.default_rng(32); bpm = 100; v = 60 / bpm; olc = 4 * v; n = int(round(8 * olc * SR))
    y = np.zeros((2, n + int(3 * SR)))
    hat = ["D4", "F4", "A4", "G#4", "A4", "F4", "E4", "Eb4"]
    for b in range(8):
        t0 = b * olc
        for i, nn in enumerate(hat):
            yerlestir(y, ks(nota(nn), 0.18, rng, 0.5, 0.97), t0 + i * v / 2, 0.22, pan=-0.2)
        for i in (0, 2):
            yerlestir(y, ks(nota("D2"), 0.25, rng, 0.5, 0.985), t0 + i * v, 0.6)
        for i in (1, 3):
            yerlestir(y, snap(rng), t0 + i * v, 0.18, pan=0.35)
    y = yatak_eq(oda(y, rng, 0.12))
    return tepe_norm(dongu_kapat(y, n), -1.0)


def gerilim_c():
    """'Heartbeat drone' 72 BPM: D1 sub dron + çift kalp atışı + üstte tremolo glock A5 seyrek."""
    rng = np.random.default_rng(33); bpm = 72; v = 60 / bpm; olc = 4 * v; n = int(round(8 * olc * SR))
    y = np.zeros((2, n + int(3 * SR)))
    tt = np.arange(n) / SR
    dr = (np.sin(2 * np.pi * nota("D2") * tt) + 0.4 * np.sin(2 * np.pi * nota("A2") * tt)) * 0.25
    yerlestir(y, dr, 0, 1.0)
    yerlestir(y, pad([nota("D3"), nota("A3"), nota("F4")], n / SR, rng, kesim=700, atak=2.0, birak=0.01, trem=4.0), 0, 0.8)
    for b in range(8):
        for i in range(4):
            t = b * olc + i * v
            yerlestir(y, kick(0.3, 80, 40), t, 0.6); yerlestir(y, kick(0.3, 70, 38), t + 0.18, 0.4)
        yerlestir(y, glock(nota("A5"), 1.5), b * olc + 2 * v, 0.06, pan=0.3)
    y = yatak_eq(oda(y, rng, 0.12))
    return tepe_norm(dongu_kapat(y, n), -1.0)


# ---------------------------------------------------------------- KENDİ SFX (earshot bankasında olmayanlar)
def _kalem(rng, vuruslar):
    """beyaz tahta kalemi: dar bantlı sürtünme gürültüsü + perde titreşimli gıcırtı; vuruşlar (bas, sure, f)."""
    y = tuval(max(b + d for b, d, _ in vuruslar) + 0.1)
    for b, d, f in vuruslar:
        m = int(d * SR); tt = np.arange(m) / SR
        e = np.sin(np.pi * np.clip(tt / d, 0, 1)) ** 0.6
        sur = filtre(rng.standard_normal(m), "bp", (1800, 6000)) * e * 0.5
        ff = f * (1 + 0.04 * np.sin(2 * np.pi * 23 * tt) + 0.02 * rng.standard_normal(m).cumsum() / np.sqrt(m))
        gic = np.sin(2 * np.pi * np.cumsum(ff) / SR) * e * 0.18
        yerlestir(y, sur + gic, b, 1.0, pan=0.1)
    return tepe_norm(y, -1.0)


def sfx_tahta_kisa():
    return _kalem(np.random.default_rng(41), [(0.0, 0.16, 2400), (0.2, 0.12, 2700), (0.36, 0.22, 2200)])


def sfx_tahta_uzun():
    return _kalem(np.random.default_rng(42), [(0.0, 0.18, 2400), (0.22, 0.10, 2800), (0.35, 0.25, 2300), (0.65, 0.12, 2600),
                                               (0.80, 0.14, 2500), (0.98, 0.30, 2150)])


def sfx_plak_cizik():
    """komedi freni: plak cızırtısı (ileri-geri perde süpürmesi, 0,45 sn)."""
    rng = np.random.default_rng(43); d = 0.45; m = int(d * SR); tt = np.arange(m) / SR
    hiz = np.interp(tt, [0, 0.12, 0.2, 0.33, 0.45], [1.0, 1.6, -1.2, 1.4, 0.0])
    f = 900 * np.abs(hiz) + 120
    ton = np.sin(2 * np.pi * np.cumsum(f) / SR) * 0.4
    g = filtre(rng.standard_normal(m), "bp", (600, 5000)) * (0.3 + 0.7 * np.abs(hiz) / 1.6)
    e = np.clip(tt / 0.005, 0, 1) * np.clip((d - tt) / 0.06, 0, 1)
    y = tuval(d + 0.05); yerlestir(y, (ton + g) * e, 0, 1.0)
    return tepe_norm(y, -1.0)


def sfx_kutu_tikirti():
    """kapalı kutu kapağı titremesi: 0,5 sn içinde 9 hızlı karton/plastik tıkırtı."""
    rng = np.random.default_rng(44); y = tuval(0.6)
    for i in range(9):
        m = int(0.03 * SR); tt = np.arange(m) / SR
        f = 600 + rng.uniform(-80, 80)
        k = (np.sin(2 * np.pi * f * tt) * 0.6 + filtre(rng.standard_normal(m), "bp", (800, 3000)) * 0.4) * np.exp(-tt * 180)
        yerlestir(y, k, i * 0.055 + rng.uniform(0, 0.01), 0.6 + 0.4 * np.sin(np.pi * i / 8), pan=rng.uniform(-0.2, 0.2))
    return tepe_norm(y, -1.0)


URET = {"jingle-a": jingle_a, "jingle-b": jingle_b, "jingle-c": jingle_c,
        "dongu-a": dongu_a, "dongu-b": dongu_b, "dongu-c": dongu_c,
        "gerilim-a": gerilim_a, "gerilim-b": gerilim_b, "gerilim-c": gerilim_c,
        "sfx-tahta-kisa": sfx_tahta_kisa, "sfx-tahta-uzun": sfx_tahta_uzun,
        "sfx-plak-cizik": sfx_plak_cizik, "sfx-kutu-tikirti": sfx_kutu_tikirti}

if __name__ == "__main__":
    cik = sys.argv[1]; os.makedirs(cik, exist_ok=True)
    for ad in (sys.argv[2:] or URET):
        y = URET[ad]()
        sf.write(f"{cik}/{ad}.wav", y.T.astype(np.float32), SR, subtype="PCM_24")
        print(f"{ad}\t{y.shape[1] / SR:.3f} sn")
