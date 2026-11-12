#!/usr/bin/env python3
"""Flip By Vote bölüm sesi: göreli cue → mutlak zaman (cevir) ve müzik + SFX stem'i (miks). Deterministik.

  cevir <ses-cue.json> <zaman.json> <satirlar.py> [--kelimeler words.json] [--sure S] [--karar-sure 7]
        [--gorsel olaylar.json] -o <ses-cue.mutlak.json>
      zaman.json = tools/ses/diyalog.py çıktısı (satirlar[i].no sırası = satirlar.py SATIRLAR sırası).
      Kelime çapası: zaman.json satır 'kelimeler' → Whisper words (--kelimeler, {w,s,e}) satır penceresinde → harf oranı
      (şablonun zaman.ts 'kelimeler' yedeğiyle aynı formül; görsel aynı yedeği kullanırsa birebir aynı an).
      Şablon çapaları video/src/seri/Bolum.tsx ile aynı: damga 0, karar = sure − kararSure, abone_klik = karar − 0,4 − 3,5 + 1,3.
      'en_az': satır çapasının alt sınırı (ör. ilk satırdan önce yer yoksa 0).
      --gorsel: {"olaylar":[{"id"|"cue": <cue id>, "t": sn}]} → aynı kimlikli SFX'in anı görsel olay anına ezilir.
  miks <ses-cue.mutlak.json> <diyalog.wav> <cikis_klasoru> [--public video/public]
      → muzik-stem.wav, sfx-stem.wav (48 kHz stereo 24-bit; tepe ≥0 dBFS ise HATA, bölüm süresi), test-muzik.wav, test-tam.wav (−14 LUFS),
        earshot-cues.json, olcum-miks.json. Seviye: BS.1770 K-ağırlıklı (kapısız) — konuşma satırları içinde/dışında.
"""
import argparse, json, os, re, runpy, subprocess, sys
import numpy as np

SR = 48000; FPS = 30
DAMGA, ABONE_SURE, ABONE_KLIK, KARAR_VARSAYILAN = 0.0, 3.5, 1.3, 7.0   # Bolum.tsx / AboneOl.tsx sabitleri (2026-11-10)
REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))


def norm(w):
    return re.sub(r"[^a-z0-9']", "", w.lower().replace("’", "'"))


# ------------------------------------------------------------------ cevir
def oran_kelimeler(s):
    parca = s["metin"].split()
    top = sum(len(p) + 1 for p in parca); t = s["bas"]; out = []
    for p in parca:
        d = (len(p) + 1) / top * (s["bitis"] - s["bas"]); out.append({"k": p, "bas": t, "bitis": t + d}); t += d
    return out


def kelime_an(s, kelime, words):
    hedef = norm(kelime)
    if s.get("kelimeler"):
        for k in s["kelimeler"]:
            if norm(k.get("k", "")) == hedef:
                return k["bas"], "kelime-zaman"
    if words:
        for w in words:
            if s["bas"] - 0.15 <= w["s"] <= s["bitis"] + 0.05 and norm(w["w"]) == hedef:
                return w["s"], "kelime-whisper"
    for k in oran_kelimeler(s):
        if norm(k["k"]) == hedef:
            return k["bas"], "kelime-oran"
    raise SystemExit(f"HATA: '{kelime}' satırda yok: {s['metin']}")


def cevir(a):
    cue = json.load(open(a.cue)); z = json.load(open(a.zaman))
    ns = runpy.run_path(a.satirlar); S = ns["SATIRLAR"]; tutus = sum(ns.get("SON_TUTUS", {}).values())
    zs = sorted(z["satirlar"], key=lambda s: s["no"])
    if len(zs) != len(S):
        raise SystemExit(f"HATA: zaman.json {len(zs)} satır, satirlar.py {len(S)} satır")
    satir = {}
    for (sid, _, kim, metin, _), s in zip(S, zs):
        if s["konusmaci"].upper() != kim:
            raise SystemExit(f"HATA: {sid} konuşmacı {kim} ≠ zaman.json {s['konusmaci']}")
        satir[sid] = s
    words = json.load(open(a.kelimeler))["words"] if a.kelimeler else None
    sure = a.sure or round(max(z["sure"], zs[-1]["bitis"] + tutus), 3)
    karar = sure - a.karar_sure
    sablon = {"damga": DAMGA, "karar": karar, "abone_klik": karar - 0.4 - ABONE_SURE + ABONE_KLIK}
    gorsel = {}
    if a.gorsel:
        for o in json.load(open(a.gorsel)).get("olaylar", []):
            k = o.get("id") or o.get("cue")
            if k: gorsel[k] = float(o["t"])

    def an(c, cid=None):
        if cid in gorsel:
            return gorsel[cid], "gorsel"
        if "sablon" in c:
            return sablon[c["sablon"]], "sablon"
        s = satir[c["satir"]]
        if "kelime" in c:
            t, k = kelime_an(s, c["kelime"], words); return t + c.get("ofset", 0), k
        return max(s[c.get("nokta", "bas")] + c.get("ofset", 0), c.get("en_az", -1e9)), "satir"

    m = cue["muzik"]; parcalar = []
    for p in m["parcalar"]:
        b, _ = an(p["bas"]); e = an(p["bitis"])[0] if "bitis" in p else None
        parcalar.append({**p, "bas": round(b, 3), "bitis": None if e is None else round(e, 3)})
    sfx = []
    for c in cue["sfx"]:
        t, k = an(c["an"], c["id"])
        sfx.append({**{x: c[x] for x in c if x != "an"}, "t": round(t, 3), "kare": int(round(t * FPS)), "kaynak": k})
    out = {"bolum": cue["bolum"], "sure": sure, "karar_bas": round(karar, 3), "fps": FPS,
           "konusma": [[round(s["bas"], 3), round(s["bitis"], 3)] for s in zs],
           "muzik": {**{x: m[x] for x in m if x != "parcalar"}, "parcalar": parcalar}, "sfx": sfx,
           "girdi": {"zaman": os.path.relpath(a.zaman, REPO), "cue": os.path.relpath(a.cue, REPO)}}
    json.dump(out, open(a.o, "w"), indent=1, ensure_ascii=False)
    kay = {}
    for x in sfx: kay[x["kaynak"]] = kay.get(x["kaynak"], 0) + 1
    print(f"cevir: sure {sure} sn, karar {karar:.2f}, {len(parcalar)} müzik, {len(sfx)} SFX; çapa {kay} → {a.o}")


# ------------------------------------------------------------------ miks
def yukle(yol):
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", yol, "-ac", "2", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True, check=True)
    return np.frombuffer(r.stdout, np.float32).reshape(-1, 2).T.astype(np.float64)


def kagirlik(y):
    from scipy.signal import lfilter
    y = lfilter([1.53512485958697, -2.69169618940638, 1.19839281085285], [1, -1.69065929318241, 0.73248077421585], y, axis=-1)
    return lfilter([1.0, -2.0, 1.0], [1, -1.99004745483398, 0.99007225036621], y, axis=-1)


def lufs(kw, maske=None):
    e = (kw ** 2).sum(0)
    if maske is not None: e = e[maske]
    return -0.691 + 10 * np.log10(e.mean() + 1e-12)


def hiza_ofset(x, tur):
    m = np.abs(x).max(0)
    if tur == "apex":
        w = int(0.01 * SR); env = np.convolve(m, np.ones(w) / w, "same"); return int(np.argmax(env))
    return int(np.argmax(m > m.max() * 0.1))


def kisa_tepe_db(x, w=int(0.1 * SR)):
    e = np.convolve((x ** 2).sum(0), np.ones(w) / w, "valid") if x.shape[1] > w else np.array([(x ** 2).sum(0).mean()])
    return 10 * np.log10(e.max() + 1e-12)


def miks(a):
    c = json.load(open(a.mutlak)); n = int(round(c["sure"] * SR))
    d = yukle(a.diyalog)
    d = np.pad(d, ((0, 0), (0, max(0, n - d.shape[1]))))[:, :n]
    konus = np.zeros(n, bool)
    for b, e in c["konusma"]:
        konus[int(b * SR):int(e * SR)] = True
    dkw = kagirlik(d); d_lufs = lufs(dkw, konus)
    # diyaloğun kısa tepe referansı: konuşmalı 100 ms pencerelerin %95'liği
    w = int(0.1 * SR); de = np.convolve((d ** 2).sum(0), np.ones(w) / w, "same")
    d_tepe = 10 * np.log10(np.percentile(de[konus], 95) + 1e-12); d_ornek_tepe = np.abs(d).max()
    m = c["muzik"]; alti = m["ses_lu"]; atak, birak = m["atak"], m["birak"]
    # boşluk aralıkları (müzik açılır): konuşma dışı ve ≥ acik_min_bosluk
    acik = np.zeros(n)
    ks = c["konusma"]; bosluk = [(0.0, ks[0][0])] + [(ks[i][1], ks[i + 1][0]) for i in range(len(ks) - 1)] + [(ks[-1][1], c["sure"])]
    for g0, g1 in bosluk:
        if g1 - g0 < m["acik_min_bosluk"]:
            continue
        i0, i1 = int(g0 * SR), int(g1 * SR); r = int(birak * SR); f = int(atak * SR)
        seg = np.ones(i1 - i0)
        if g0 > 0.01:
            up = min(r, len(seg)); seg[:up] = np.linspace(0, 1, up)
        if g1 < c["sure"] - 0.01:
            dn = min(f, len(seg)); seg[-dn:] = np.minimum(seg[-dn:], np.linspace(1, 0, dn))
        acik[i0:i1] = np.maximum(acik[i0:i1], seg)
    mz = np.zeros((2, n)); parca_olc = []
    for p in m["parcalar"]:
        x = yukle(os.path.join(a.public, p["dosya"]))
        x_l = lufs(kagirlik(x))
        b = int(p["bas"] * SR); e = int(p["bitis"] * SR) if p.get("bitis") is not None else b + x.shape[1]
        e = min(e, n); L = e - b
        if L <= 0: continue
        y = np.tile(x, (1, L // x.shape[1] + 1))[:, :L] if p.get("dongu") else np.pad(x, ((0, 0), (0, max(0, L - x.shape[1]))))[:, :L]
        fi, fo = int(p.get("fade_in", 0.01) * SR), int(p.get("fade_out", 0.05) * SR)
        if fi: y[:, :fi] *= np.linspace(0, 1, fi)
        if fo and not (p.get("dongu") is False and x.shape[1] < L): y[:, -fo:] *= np.linspace(1, 0, fo)
        acik_lu = p.get("ses_lu", alti + m["acik_db"])
        if p.get("duck", True):
            a_ = acik[b:e]; db = alti + (acik_lu - alti) * a_
        else:
            db = np.full(L, acik_lu)
        g = 10 ** ((d_lufs + db - x_l) / 20)
        mz[:, b:e] += y * g
        parca_olc.append({"id": p["id"], "dosya_lufs": round(x_l, 1), "alti_lu": alti, "acik_lu": acik_lu, "bas": p["bas"], "bitis": round(e / SR, 3)})
    sx = np.zeros((2, n)); cues = []
    for s in c["sfx"]:
        x = yukle(os.path.join(a.public, s["dosya"]))
        o = hiza_ofset(x, s["hiza"]); i = int(round(s["t"] * SR)) - o
        g = 10 ** ((d_tepe + s["db"] - kisa_tepe_db(x)) / 20)
        g = min(g, d_ornek_tepe * 10 ** (-3 / 20) / (np.abs(x).max() + 1e-12))   # tepe tavanı: diyalog tepesi − 3 dB (tık/klik krest)
        j0 = max(0, -i); k = min(x.shape[1], n - i)
        if k > j0: sx[:, i + j0:i + k] += x[:, j0:k] * g
        cues.append({"f": s["kare"], "kind": s.get("tur", "sfx"), "id": s["id"]})
    os.makedirs(a.cikis, exist_ok=True)
    import soundfile as sf
    yaz = lambda ad, y: sf.write(f"{a.cikis}/{ad}", y.T.astype(np.float32), SR, subtype="PCM_24")
    tepe = max(np.abs(mz).max(), np.abs(sx).max())
    if tepe >= 1.0:
        raise SystemExit(f"HATA: stem/miks tepesi {20 * np.log10(tepe):+.1f} dBFS (24-bit kırpar) → cue 'db' değerlerini düşür")
    yazf = lambda ad, y: sf.write(f"{a.cikis}/{ad}", y.T.astype(np.float32), SR, subtype="FLOAT")  # test miksleri: kırpılmasın
    yaz("muzik-stem.wav", mz); yaz("sfx-stem.wav", sx)
    yazf("test-muzik.wav", d + mz); ham = d + mz + sx; yazf("test-tam-ham.wav", ham)
    json.dump({"fps": FPS, "events": cues}, open(f"{a.cikis}/earshot-cues.json", "w"), indent=1)
    # ölçüm (K-ağırlıklı, kapısız): konuşma altında müzik − diyalog, boşlukta müzik − diyalog
    mkw = kagirlik(mz); var = np.abs(mz).sum(0) > 1e-6
    satir_fark = []
    for b, e in c["konusma"]:
        mk = np.zeros(n, bool); mk[int(b * SR):int(e * SR)] = True; mk &= var
        if mk.sum() > 0.3 * SR:
            satir_fark.append(round(lufs(mkw, mk) - lufs(dkw, mk), 1))
    gmask = (~konus) & var & (acik > 0.99)
    sonuc = {"diyalog_lufs_konusma": round(d_lufs, 2), "muzik_alti_fark_db": {"medyan": float(np.median(satir_fark)), "min": min(satir_fark), "max": max(satir_fark), "satir": satir_fark},
             "muzik_bosluk_fark_db": round(lufs(mkw, gmask) - d_lufs, 1) if gmask.any() else None,
             "sfx_sayisi": len(c["sfx"]), "parcalar": parca_olc, "stem_tepe_dbfs": round(20 * np.log10(tepe + 1e-12), 1)}
    json.dump(sonuc, open(f"{a.cikis}/olcum-miks.json", "w"), indent=1, ensure_ascii=False)
    # −14 LUFS test miksi (son normalizasyon render-son.sh'te; bu yalnız kapı kanıtı)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", f"{a.cikis}/test-tam-ham.wav", "-af", "loudnorm=I=-14:TP=-1:LRA=11",
                    "-ar", str(SR), f"{a.cikis}/test-tam.wav"], check=True)
    print(json.dumps({k: v for k, v in sonuc.items() if k != "parcalar"}, ensure_ascii=False))


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); sp = ap.add_subparsers(dest="kip", required=True)
    c1 = sp.add_parser("cevir"); c1.add_argument("cue"); c1.add_argument("zaman"); c1.add_argument("satirlar")
    c1.add_argument("--kelimeler"); c1.add_argument("--sure", type=float); c1.add_argument("--karar-sure", type=float, default=KARAR_VARSAYILAN)
    c1.add_argument("--gorsel"); c1.add_argument("-o", required=True)
    c2 = sp.add_parser("miks"); c2.add_argument("mutlak"); c2.add_argument("diyalog"); c2.add_argument("cikis")
    c2.add_argument("--public", default=os.path.join(REPO, "video", "public"))
    a = ap.parse_args()
    (cevir if a.kip == "cevir" else miks)(a)
