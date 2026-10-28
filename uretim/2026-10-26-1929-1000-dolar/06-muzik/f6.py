#!/usr/bin/env python3
"""F6 miks motoru — 1929-1000-dolar (muzik-ses-tasarimcisi).

Kullanım (Whisper venv'iyle; CPU'yu korumak için nice):
  nice -n 15 ~/.finansal-arac/venv/bin/python 06-muzik/f6.py test     # bölüm başına aday × 25 sn dilim, Whisper WER + seviye
  nice -n 15 ~/.finansal-arac/venv/bin/python 06-muzik/f6.py render   # stems + önizleme miksi + ölçüm + Shorts stem'leri
  nice -n 15 ~/.finansal-arac/venv/bin/python 06-muzik/f6.py wer      # önizleme miksinde tam dosya Whisper WER

Kurallar (adaylar.md / hafıza):
  - Müzik konuşma altında anlatımın (−14.2 LUFS) `duck` dB altına göre seviyelenir (varsayılan 22; Ragtime 23 + 3 kHz oyuk).
  - Konuşma boşluğu ≥0.9 sn ise müzik +6 dB açılır (0.25 sn önden iner, 0.5 sn sonra açılır) — kısa cümle aralarında pompalama yok.
  - Bölüm geçişleri 1.2 sn eşit güçte çapraz geçiş; "müzik keser" noktaları sert (0.25 sn) kesilir.
  - SFX'ler önce −3 dBFS tepeye normalize edilir, sonra olay kazancı uygulanır. Konuşmayla çakışan SFX'ler raporlanır.
  - Son normalizasyon render-son.sh'de; burada yalnız önizleme miksi −14 LUFS'a getirilir (2 geçişli loudnorm).
"""
import json, os, re, runpy, subprocess, sys
import numpy as np

SR = 48000
BURA = os.path.dirname(os.path.abspath(__file__))
UR = os.path.dirname(BURA)
REPO = os.path.abspath(os.path.join(UR, "..", ".."))
ANL = f"{UR}/04-ses/anlatim.wav"
KEL = json.load(open(f"{UR}/04-ses/kelimeler-hizali.json"))["words"]
CUM = json.load(open(f"{UR}/04-ses/anlatim-ham.zaman.json"))["cumleler"]
M, O, A, E, AE = (f"{BURA}/kaynak/muzik/", f"{BURA}/kaynak/ozgun/", f"{REPO}/assets/muzik/", f"{BURA}/kaynak/efekt/",
                  f"{REPO}/assets/efekt/")
GECICI = os.environ.get("F6_GECICI", "/tmp/f6-gecici")
os.makedirs(GECICI, exist_ok=True)
NARR_LUFS = -14.2
NOTCH = "equalizer=f=3000:t=o:w=1.2:g=-4"   # Ragtime: 2–4 kHz oyuk (F4 notu)
TOPLAM = 631.63

# ---------------- aday testleri (F6 adım 1) ----------------
ADAYLAR = {
    "B1": (0.0, 79.707, [("catchy-swing", M + "catchy-swing-doge.ogg", 22, None), ("ragtime-jazz", M + "ragtime-jazz-tarush-singhal.mp3", 23, NOTCH)]),
    "B2": (79.707, 114.9, [("ragtime-jazz", M + "ragtime-jazz-tarush-singhal.mp3", 23, NOTCH), ("osanpo-rag", M + "osanpo-rag-yubatake.ogg", 23, NOTCH)]),
    "B3": (166.502, 286.473, [("tension", M + "tension-komiku.mp3", 22, None), ("backup-plan", M + "backup-plan-zane-little.ogg", 22, None)]),
    "B4": (286.473, 372.712, [("fridge", M + "fridge-is-hungry-congusbongus.ogg", 22, None), ("black-tea-rag", M + "black-tea-rag-decimnet.mp3", 23, NOTCH)]),
    "B5": (372.712, 453.96, [("end-of-hope", M + "at-the-end-of-hope-emma-ma.mp3", 22, None), ("dip-drone", O + "ozgun-yatak-dip-drone.flac", 22, None)]),
    "B6": (453.96, 522.88, [("unsolved", A + "merak-unsolved-investigation-isaiah658.ogg", 22, None), ("kilit-saat", O + "ozgun-yatak-kilit-saat-100bpm.flac", 22, None)]),
    "B7": (522.88, 592.857, [("electro-swing", M + "electro-swing-type-gp.mp3", 22, None), ("the-way-it-is", M + "the-way-it-is-zane-little.mp3", 22, None)]),
    "B8": (592.857, 631.63, [("positive-melancholy", M + "positive-melancholy-dizzy-crow.ogg", 22, None), ("happy-moments", M + "happy-moments-centurion.ogg", 22, None)]),
}


def sh(*a, **k):
    return subprocess.run(list(a), capture_output=True, text=True, **k)


def coz(yol, af=None, sr=SR):
    kom = ["ffmpeg", "-v", "error", "-i", yol]
    if af:
        kom += ["-af", af]
    kom += ["-ac", "2", "-ar", str(sr), "-f", "f32le", "-"]
    r = subprocess.run(kom, capture_output=True, check=True).stdout
    return np.frombuffer(r, dtype=np.float32).reshape(-1, 2).copy()


def yaz(yol, x, bit=24):
    x = np.asarray(x, dtype=np.float32)
    if x.ndim == 1:
        x = np.stack([x, x], 1)
    kod = ["-c:a", "pcm_s24le"] if yol.endswith(".wav") else (["-c:a", "aac", "-b:a", "160k"] if yol.endswith(".m4a") else [])
    p = subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-", *kod, yol],
                       input=x.tobytes())
    assert p.returncode == 0, yol


def lufs_yol(yol, af=None):
    r = sh("ffmpeg", "-nostats", "-i", yol, "-af", (af + "," if af else "") + "ebur128=peak=true", "-f", "null", "-")
    oz = r.stderr[r.stderr.rfind("Summary:"):]
    g = lambda k: float(re.search(k + r":\s+(-?[\d.]+|-inf)", oz).group(1).replace("-inf", "-99"))
    return {"I": g("I"), "LRA": g("LRA"), "TP": g("Peak")}


def lufs_dizi(x):
    t = f"{GECICI}/olc.wav"
    yaz(t, x)
    return lufs_yol(t)


_LCACHE = {}


def parca_lufs(yol, af):
    k = (yol, af)
    if k not in _LCACHE:
        _LCACHE[k] = lufs_yol(yol, af)["I"]
    return _LCACHE[k]


def dongu(x, n, xf=1.0):
    """x'i n örneğe uzatır; tekrarlarda xf sn eşit güçte çapraz geçiş."""
    if len(x) >= n:
        return x[:n]
    k = int(xf * SR)
    out = x.copy()
    w = np.linspace(0, np.pi / 2, k)[:, None]
    while len(out) < n:
        bas = out[-k:] * np.cos(w) + x[:k] * np.sin(w)
        out = np.concatenate([out[:-k], bas, x[k:]])
    return out[:n]


# ---------------- konuşma zarfı ----------------
def konusma_maskesi(t0, t1, hiz=100, birlestir=0.9):
    """t0–t1 aralığında 100 Hz konuşma maskesi (kelimeler; <birlestir sn boşluklar konuşma sayılır)."""
    n = int(round((t1 - t0) * hiz))
    m = np.zeros(n, bool)
    for w in KEL:
        a, b = int((w["s"] - t0) * hiz), int((w["e"] - t0) * hiz) + 1
        if b > 0 and a < n:
            m[max(a, 0):min(b, n)] = True
    # kısa boşlukları kapat
    i = 0
    while i < n:
        if not m[i]:
            j = i
            while j < n and not m[j]:
                j += 1
            if 0 < i and j < n and (j - i) / hiz < birlestir:
                m[i:j] = True
            i = j
        else:
            i += 1
    return m


def duck_zarfi(t0, t1, acil_db=6.0, hiz=100):
    m = konusma_maskesi(t0, t1, hiz)
    # konuşmadan 0.25 sn önce in, 0.5 sn sonra aç
    gen = m.copy()
    for s in range(1, int(0.25 * hiz) + 1):
        gen[:-s] |= m[s:]
    for s in range(1, int(0.5 * hiz) + 1):
        gen[s:] |= m[:-s]
    db = np.where(gen, 0.0, acil_db)
    k = int(0.3 * hiz)
    db = np.convolve(np.pad(db, (k, k), mode="edge"), np.ones(k) / k, mode="same")[k:-k]
    tt = np.arange(int(round((t1 - t0) * SR))) / SR
    return 10 ** (np.interp(tt, np.arange(len(db)) / hiz, db) / 20).astype(np.float32)


def bolum_muzik(yol, af, duck, t0, t1, ofset=0.0, giris=1.0, cikis=1.0, acil_db=6.0):
    """t0–t1 için seviyelenmiş + duck'lı müzik (n,2)."""
    n = int(round((t1 - t0) * SR))
    x = coz(yol, af)
    x = x[int(ofset * SR):] if ofset else x
    x = dongu(x, n)
    hedef = NARR_LUFS - duck
    x = x * 10 ** ((hedef - parca_lufs(yol, af)) / 20)
    x = x * duck_zarfi(t0, t1, acil_db)[:, None]
    gi, ci = int(giris * SR), int(cikis * SR)
    if gi:
        x[:gi] *= np.sin(np.linspace(0, np.pi / 2, gi))[:, None]
    if ci:
        x[-ci:] *= np.cos(np.linspace(0, np.pi / 2, ci))[:, None]
    return x.astype(np.float32)


# ---------------- ölçümler ----------------
def momentary(yol):
    """ebur128 momentary (400 ms) değerleri, 100 ms adım."""
    r = sh("ffmpeg", "-nostats", "-i", yol, "-af", "ebur128=metadata=1,ametadata=print:key=lavfi.r128.M:file=-",
           "-f", "null", "-")
    v = [float(x) for x in re.findall(r"lavfi\.r128\.M=(-?[\d.]+|-inf)", r.stdout.replace("-inf", "-120"))]
    return np.array(v)


def seviye_farki(narr_yol, muz_yol, t0):
    """Konuşma varken ve yokken anlatım − müzik farkı (momentary, medyan)."""
    a, b = momentary(narr_yol), momentary(muz_yol)
    n = min(len(a), len(b))
    a, b = a[:n], b[:n]
    m = konusma_maskesi(t0, t0 + n / 10, hiz=10)[:n]
    m &= a > -40
    sessiz = ~konusma_maskesi(t0, t0 + n / 10, hiz=10, birlestir=0)[:n] & (b > -70)
    return {"konusma_alti_fark_db": round(float(np.median(a[m] - b[m])), 1) if m.any() else None,
            "muzik_konusmada_lufs_M": round(float(np.median(b[m])), 1) if m.any() else None,
            "muzik_boslukta_lufs_M": round(float(np.median(b[sessiz])), 1) if sessiz.sum() > 5 else None}


def wer_hesapla(ref_metin, hyp_metin):
    ns = runpy.run_path(f"{REPO}/tools/ses/hata-orani.py")
    r, h = ns["norm"](ref_metin), ns["norm"](hyp_metin)
    d = list(range(len(h) + 1))
    for i in range(1, len(r) + 1):
        onceki, d[0] = d[0], i
        for j in range(1, len(h) + 1):
            onceki, d[j] = d[j], min(d[j] + 1, d[j - 1] + 1, onceki + (r[i - 1] != h[j - 1]))
    return d[-1], len(r)


_MODEL = None


def whisper(yol):
    global _MODEL
    from faster_whisper import WhisperModel
    if _MODEL is None:
        _MODEL = WhisperModel("small.en", device="cpu", compute_type="int8", local_files_only=True, cpu_threads=2)
    x = coz(yol, sr=16000).mean(1)
    segs, _ = _MODEL.transcribe(x, language="en", beam_size=5, condition_on_previous_text=False)
    return " ".join(s.text.strip() for s in segs)


def ref_dilim(t0, t1):
    c = [x["metin"] for x in CUM if x["bas"] >= t0 - 0.05 and x["son"] <= t1 + 0.05]
    return " ".join(c), (min(x["bas"] for x in CUM if x["bas"] >= t0 - 0.05), max(x["son"] for x in CUM if x["son"] <= t1 + 0.05))


# ---------------- test ----------------
def test():
    narr = coz(ANL)
    sonuc = []
    for b, (bb, bs, liste) in ADAYLAR.items():
        uz = 25.0
        t0 = bb + max(0.0, 0.35 * (bs - bb - uz))
        t1 = min(t0 + uz, bs)
        ref, (r0, r1) = ref_dilim(t0, t1)       # dilim tam cümlelerden oluşsun
        t0, t1 = max(r0 - 0.2, 0), min(r1 + 0.3, TOPLAM)
        n0, n1 = int(t0 * SR), int(t1 * SR)
        nd = narr[n0:n1]
        ny = f"{GECICI}/{b}-anlatim.wav"
        yaz(ny, nd)
        h0 = whisper(ny)
        e0, k = wer_hesapla(ref, h0)
        satir = {"bolum": b, "dilim": [round(t0, 2), round(t1, 2)], "kelime": k, "anlatim_tek_hata": e0, "adaylar": []}
        for ad, yol, duck, af in liste:
            mz = bolum_muzik(yol, af, duck, t0, t1, ofset=10.0 if ad not in ("kilit-saat", "dip-drone") else 0.0,
                             giris=0.3, cikis=0.3)
            my = f"{GECICI}/{b}-{ad}-muzik.wav"
            karisim = f"{GECICI}/{b}-{ad}-miks.wav"
            mz = mz[:len(nd)]
            if len(mz) < len(nd):
                mz = np.pad(mz, ((0, len(nd) - len(mz)), (0, 0)))
            yaz(my, mz)
            yaz(karisim, nd + mz)
            h = whisper(karisim)
            e, _ = wer_hesapla(ref, h)
            sev = seviye_farki(ny, my, t0)
            satir["adaylar"].append({"aday": ad, "duck": duck, "oyuk": bool(af), "hata": e, "fark_hata": e - e0, **sev})
            print(b, ad, "hata", e, "(anlatım tek", e0, ")", sev, flush=True)
        sonuc.append(satir)
    json.dump(sonuc, open(f"{BURA}/olcum-f6-test.json", "w"), ensure_ascii=False, indent=1)


# ---------------- render ----------------
def cue_yukle():
    return json.load(open(f"{BURA}/cue.json"))


def render():
    cue = cue_yukle()
    narr = coz(ANL)
    n = len(narr)                       # stem'ler anlatımla örnek örnek aynı uzunlukta
    muz = np.zeros((n, 2), np.float32)
    for c in cue["muzik"]:
        yol = c["dosya"].replace("$M/", M).replace("$O/", O).replace("$A/", A)
        af = NOTCH if c.get("oyuk") else None
        t0, t1 = c["bas"], c["son"]
        t1 = min(t1, n / SR)
        x = bolum_muzik(yol, af, c["duck"], t0, t1, ofset=c.get("ofset", 0.0), giris=c.get("giris", 1.2),
                        cikis=c.get("cikis", 1.2), acil_db=c.get("acil_db", 6.0))
        i = int(round(t0 * SR))
        muz[i:i + len(x)] += x[:n - i]
    sfx = np.zeros((n, 2), np.float32)
    cakisma = []
    km = konusma_maskesi(0, TOPLAM, 100, birlestir=0.0)
    for s in cue["sfx"]:
        yol = s["dosya"].replace("$E/", E).replace("$O/", O).replace("$AE/", AE)
        x = coz(yol)
        if s.get("sure"):
            x = x[:int(s["sure"] * SR)]
            f = min(len(x), int(0.15 * SR))
            x[-f:] *= np.linspace(1, 0, f)[:, None]
        if s.get("perde"):
            # basit perde kaydırma (yeniden örnekleme; süre de değişir) — kahkaha katmanları için
            oran = 2 ** (s["perde"] / 12)
            idx = np.arange(0, len(x) - 1, oran)
            x = np.stack([np.interp(idx, np.arange(len(x)), x[:, ch]) for ch in (0, 1)], 1).astype(np.float32)
        x = x / (np.abs(x).max() + 1e-9) * 10 ** (-3 / 20) * 10 ** (s["db"] / 20)
        if s.get("pan"):
            a = (s["pan"] + 1) * np.pi / 4
            x = x * np.array([np.cos(a), np.sin(a)], np.float32) * np.sqrt(2)
        i = int(round(s["t"] * SR))
        j = min(n, i + len(x))
        sfx[i:j] += x[:j - i]
        # çakışma: SFX'in −30 dB üstü kısmı konuşmayla örtüşüyor mu
        env = np.abs(x).max(1)
        aktif = np.where(env > np.abs(x).max() * 10 ** (-30 / 20))[0]
        if len(aktif):
            a0, a1 = (i + aktif[0]) / SR, (i + aktif[-1]) / SR
            ort = km[int(a0 * 100):int(a1 * 100) + 1].mean() if a1 > a0 else 0
            if ort > 0:
                cakisma.append({"t": s["t"], "olay": s["olay"], "konusmayla_ortusme": round(float(ort), 2), "db": s["db"]})
    os.makedirs(f"{BURA}/stems", exist_ok=True)
    yaz(f"{BURA}/stems/muzik-stem.wav", muz)
    yaz(f"{BURA}/stems/sfx-stem.wav", sfx)
    ham = narr + muz + sfx
    yaz(f"{GECICI}/miks-ham.wav", ham)
    # 2 geçişli loudnorm → −14 LUFS, TP −1 (önizleme; son normalizasyon render-son.sh'de)
    r = sh("ffmpeg", "-nostats", "-i", f"{GECICI}/miks-ham.wav", "-af", "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json",
           "-f", "null", "-")
    j = json.loads(r.stderr[r.stderr.rfind("{"):r.stderr.rfind("}") + 1])
    af = (f"loudnorm=I=-14:TP=-1.5:LRA=11:measured_I={j['input_i']}:measured_TP={j['input_tp']}:"
          f"measured_LRA={j['input_lra']}:measured_thresh={j['input_thresh']}:offset={j['target_offset']}:linear=true")
    sh("ffmpeg", "-v", "error", "-y", "-i", f"{GECICI}/miks-ham.wav", "-af", af + ",aresample=48000", "-c:a", "pcm_s24le",
       f"{BURA}/stems/miks-onizleme.wav")
    sh("ffmpeg", "-v", "error", "-y", "-i", f"{BURA}/stems/miks-onizleme.wav", "-c:a", "aac", "-b:a", "128k",
       f"{BURA}/stems/miks-onizleme.m4a")
    yaz(f"{GECICI}/anlatim-st.wav", narr)
    olc = {
        "miks_onizleme_wav": lufs_yol(f"{BURA}/stems/miks-onizleme.wav"),
        "miks_onizleme_m4a": lufs_yol(f"{BURA}/stems/miks-onizleme.m4a"),
        "muzik_stem": lufs_yol(f"{BURA}/stems/muzik-stem.wav"),
        "sfx_stem": lufs_yol(f"{BURA}/stems/sfx-stem.wav"),
        "seviye_tum": seviye_farki(f"{GECICI}/anlatim-st.wav", f"{BURA}/stems/muzik-stem.wav", 0.0),
        "bolum_seviye": {},
        "sfx_konusma_cakismasi": cakisma,
    }
    for c in cue["muzik"]:
        a, b = c["bas"], c["son"]
        yaz(f"{GECICI}/d-n.wav", narr[int(a * SR):int(b * SR)])
        yaz(f"{GECICI}/d-m.wav", muz[int(a * SR):int(b * SR)])
        olc["bolum_seviye"][c["ad"]] = seviye_farki(f"{GECICI}/d-n.wav", f"{GECICI}/d-m.wav", a)
    json.dump(olc, open(f"{BURA}/olcum-f6-render.json", "w"), ensure_ascii=False, indent=1)
    print(json.dumps(olc, ensure_ascii=False, indent=1))
    shorts(cue)


def shorts(cue):
    """Shorts için kısa müzik stem'leri: sabit yatak (Shorts'ta konuşma neredeyse kesintisiz), 60 sn, sonda 2 sn sönüş.
    Seviye: konuşma altında 20 dB (mobil dinleme; ana videodan 2 dB yukarı). Hook öncesi giriş yok (ilk kare = konuşma)."""
    for s in cue["shorts"]:
        yol = s["dosya"].replace("$M/", M).replace("$O/", O).replace("$A/", A)
        x = dongu(coz(yol)[int(s.get("ofset", 0) * SR):], int(s["sure"] * SR))
        x = x * 10 ** ((NARR_LUFS - s["duck"] - parca_lufs(yol, None)) / 20)
        c = int(2.0 * SR)
        x[-c:] *= np.cos(np.linspace(0, np.pi / 2, c))[:, None]
        g = int(0.05 * SR)
        x[:g] *= np.linspace(0, 1, g)[:, None]
        yaz(f"{BURA}/stems/{s['ad']}-muzik-stem.wav", x)
        ek = f"{UR}/04-ses/{s['ad']}-ek.wav"
        if os.path.exists(ek):  # ek kayıt (hook) üstünde seviye kontrolü
            e = coz(ek)
            yaz(f"{GECICI}/s-n.wav", e)
            yaz(f"{GECICI}/s-m.wav", x[:len(e)])
            print(s["ad"], seviye_farki(f"{GECICI}/s-n.wav", f"{GECICI}/s-m.wav", 0.0) | {"not": "hook ek kaydı; konuşma maskesi ana videodan, yaklaşık"})
            ham = e + x[:len(e)]
            yaz(f"{GECICI}/{s['ad']}-hook-miks.wav", ham)


def wer_tam():
    yol = f"{BURA}/stems/miks-onizleme.wav"
    h = whisper(yol)
    ref = open(f"{UR}/04-ses/referans-metni.txt", encoding="utf-8").read()
    e, k = wer_hesapla(ref, h)
    h0 = json.load(open(f"{UR}/04-ses/kelimeler.json"))["text"]
    e0, _ = wer_hesapla(ref, h0)
    sonuc = {"kelime": k, "anlatim_tek_hata": e0, "anlatim_tek_wer": round(e0 / k * 100, 2),
             "miks_hata": e, "miks_wer": round(e / k * 100, 2), "fark_puan": round((e - e0) / k * 100, 2),
             "not": "anlatım-tek transkripti 04-ses/kelimeler.json (ses kolu, small.en); miks aynı model small.en"}
    open(f"{BURA}/stems/miks-onizleme-whisper.txt", "w").write(h)
    json.dump(sonuc, open(f"{BURA}/olcum-f6-wer.json", "w"), ensure_ascii=False, indent=1)
    print(sonuc)


if __name__ == "__main__":
    {"test": test, "render": render, "wer": wer_tam}[sys.argv[1]]()
