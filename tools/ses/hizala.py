#!/usr/bin/env python3
"""Kilitli metin <-> Whisper kelime zamanları hizalaması (TTS anlatımı için; ses-muhendisi yöntemi 2026-10-27).

Kullanım: python3 -I tools/ses/hizala.py --dizin uretim/<video>/04-ses [--cikis DIZIN] [--norm yeni|eski]
  Girdi adları (dizine göre, ayrı ayrı değiştirilebilir): --kelimeler kelimeler.json (yaziya-dok.py)
  --zaman anlatim-ham.zaman.json (tts.py cümle sınırları) --sahneler sahne-zamanlari.json (cumle_ilk/cumle_son)
  --referans referans-metni.txt (kilitli metin; boşlukla ayrılmış kelimeler çıktıyla birebir eşleşmeli)
Çıkış (--cikis, varsayılan --dizin):
  kelimeler-hizali.json   {"words":[{w,s,e,p,sahne,cumle,kaynak}]} — w = kilitli metindeki kelime,
                          kaynak: whisper (birebir) | bolme (Whisper'ın farklı yazdığı aralık bölündü) | ara (atlanan kelime, komşular arası)
  altyazi-remotion.json   @remotion/captions Caption[] ({text,startMs,endMs,timestampMs,confidence})
  altyazi-taslak.en.srt   cümle-farkında bloklar (<=2x42 karakter, <=6 sn)
Yöntem: anchor = TTS'in kendi cümle sınırları. Whisper kelimesi bitiş tarafı örtüşmesiyle en yakın cümleye atanır; cümle içinde
alt-kelime düzeyinde difflib (tools/ses/hata-orani.py norm_alt: rakam/sıra sayısı -> İngilizce söz); metinde karşılığı olmayan
Whisper kelimeleri (uydurma "Yes." vb.) atılır ve listelenir. Doğrulama: tools/ses/hiza-dogrula.py (akustik, p95 <= 150 ms).
--norm eski: 2026-10-26 normalizasyonu (1929-1000-dolar çıktısını bayt bayt yeniden üretir); yeni (varsayılan) sıra sayılarını
da eşler (1929'da bolme 30 -> 26, whisper 1669 -> 1673).
Genelleştirildi 2026-10-27 (uretim-muhendisi): kaynak uretim/2026-10-26-1929-1000-dolar/04-ses/hizala.py. Yalnız standart kütüphane.
"""
import argparse, difflib, importlib.util, json, re, sys, os
_spec = importlib.util.spec_from_file_location("ho", os.path.join(os.path.dirname(os.path.abspath(__file__)), "hata-orani.py"))
ho = importlib.util.module_from_spec(_spec); _spec.loader.exec_module(ho)
temiz = lambda m: re.sub(r"\[([^\]]+)\]\(/[^)]*/\)", r"\1", m)


def main():
    ap = argparse.ArgumentParser(description="Kilitli metin <-> Whisper kelime hizalaması")
    ap.add_argument("--dizin", default=".")
    ap.add_argument("--kelimeler", default="kelimeler.json"); ap.add_argument("--zaman", default="anlatim-ham.zaman.json")
    ap.add_argument("--sahneler", default="sahne-zamanlari.json"); ap.add_argument("--referans", default="referans-metni.txt")
    ap.add_argument("--cikis"); ap.add_argument("--srt-adi", default="altyazi-taslak.en.srt")
    ap.add_argument("--norm", choices=["yeni", "eski"], default="yeni")
    a = ap.parse_args()
    yol = lambda p: p if os.path.isabs(p) else os.path.join(a.dizin, p)
    O = a.cikis or a.dizin; os.makedirs(O, exist_ok=True)
    NORM = ho.norm_eski if a.norm == "eski" else ho.norm_alt
    W0 = json.load(open(yol(a.kelimeler)))["words"]
    W = []  # Whisper "$1" + ",000" gibi bölünmüş sayı parçalarını birleştir
    for w in W0:
        if W and re.match(r"^[,.]\d", w["w"]) and re.search(r"\d$", W[-1]["w"]):
            W[-1] = {**W[-1], "w": W[-1]["w"] + w["w"], "e": w["e"], "p": min(W[-1]["p"], w["p"])}
        else:
            W.append(dict(w))
    C = json.load(open(yol(a.zaman)))["cumleler"]
    SZ = json.load(open(yol(a.sahneler)))["sahneler"]
    sahne_of = {i: s["sahne"] for s in SZ for i in range(s["cumle_ilk"], s["cumle_son"] + 1)}
    PAY_ON, PAY_SON = 0.12, 0.20
    def uzak(w, c):
        # kelimenin son <=0.3 sn'lik kısmının cümle penceresiyle örtüşmesi (Whisper duraklama sonrası ilk kelimenin başını
        # sessizliğe doğru erken koyar; bitiş güvenilir). Örtüşme yoksa bitişin pencereye uzaklığı.
        s0 = max(w["s"], w["e"] - 0.3); ort = min(w["e"], c["son"]) - max(s0, c["bas"])
        return -ort if ort > 0 else min(abs(w["e"] - c["bas"]), abs(w["e"] - c["son"]))
    ata = {}  # her Whisper kelimesi en yakın cümle penceresine (boşluk yok; yanlış zamanlı ilk kelime de kaybolmaz)
    for i, w in enumerate(W):
        ata.setdefault(min(range(len(C)), key=lambda k: uzak(w, C[k])), []).append(i)
    kullanilan = set(); atilan = []; out = []; say = {"whisper": 0, "bolme": 0, "ara": 0}
    for ci, c in enumerate(C):
        bas, son = c["bas"], c["son"]
        ust = C[ci + 1]["bas"] if ci + 1 < len(C) else son + 5
        alt = C[ci - 1]["son"] if ci else -1
        wi = ata.get(ci, [])
        ref = temiz(c["metin"]).split()
        # alt-kelimeler
        ra, rb = [], []  # (alt, ref_idx)
        for k, r in enumerate(ref):
            for x in NORM(r) or [re.sub(r"\W", "", r.lower()) or "_"]:
                ra.append(x); rb.append(k)
        wa, wt, wsrc = [], [], []  # alt, (s,e,p), Whisper indeksi
        for i in wi:
            w = W[i]; parts = NORM(w["w"]) or ["_"]; n = len(parts); d = (w["e"] - w["s"]) / n
            for j, x in enumerate(parts):
                wa.append(x); wt.append((w["s"] + j * d, w["s"] + (j + 1) * d, w["p"])); wsrc.append(i)
        zam = [None] * len(ra); kay = [None] * len(ra)
        for op, a1, a2, b1, b2 in difflib.SequenceMatcher(a=ra, b=wa, autojunk=False).get_opcodes():
            if op in ("equal", "replace"):
                kullanilan.update(wsrc[j] for j in range(b1, b2))
            if op == "equal":
                for k in range(a2 - a1):
                    zam[a1 + k] = wt[b1 + k]; kay[a1 + k] = "whisper"
            elif op == "insert":  # metinde karşılığı olmayan Whisper kelimesi (uydurma / normalizasyon artığı) -> atılır
                atilan.extend(wsrc[j] for j in range(b1, b2))
            elif op == "replace":
                s, e = wt[b1][0], wt[b2 - 1][1]; p = min(t[2] for t in wt[b1:b2])
                L = [len(x) for x in ra[a1:a2]]; T = sum(L); acc = 0
                for k in range(a2 - a1):
                    zam[a1 + k] = (s + (e - s) * acc / T, s + (e - s) * (acc + L[k]) / T, p); acc += L[k]; kay[a1 + k] = "bolme"
        # ref kelime düzeyine topla
        R = []
        for k, r in enumerate(ref):
            idx = [j for j in range(len(ra)) if rb[j] == k]
            z = [zam[j] for j in idx if zam[j]]
            if z:
                ks = {kay[j] for j in idx if zam[j]}
                R.append([r, min(t[0] for t in z), max(t[1] for t in z), min(t[2] for t in z), "whisper" if ks == {"whisper"} else "bolme"])
            else:
                R.append([r, None, None, None, "ara"])
        # ara kelimeler: komşular arasına (cümle penceresi içinde)
        for k, x in enumerate(R):
            if x[1] is None:
                onceki = next((R[j][2] for j in range(k - 1, -1, -1) if R[j][1] is not None), bas)
                sonraki = next((R[j][1] for j in range(k + 1, len(R)) if R[j][1] is not None), son)
                gap = [j for j in range(len(R)) if R[j][1] is None]
                x[1], x[2], x[3] = onceki, max(onceki + 0.05, min(sonraki, onceki + 0.35)), 0.0
        # sıkıştır: cümle penceresi, monoton, s<e
        t0 = bas
        for k, x in enumerate(R):
            x[1] = min(max(x[1], t0, bas), son - 0.03); x[2] = min(max(x[2], x[1] + 0.03), son + 0.05)
            t0 = x[1]
        for k in range(len(R) - 1):
            if R[k][2] > R[k + 1][1]: R[k][2] = max(R[k][1] + 0.02, R[k + 1][1])
        # cümle uçlarını TTS sınırına oturt (tts.py kırpma payı: ön 30 ms, son 50 ms; örnek doğruluğunda)
        if abs(R[0][1] - (bas + 0.03)) < 0.4:
            R[0][1] = bas + 0.03; R[0][2] = max(R[0][2], R[0][1] + 0.12)
            for k in range(1, len(R)):  # ilk kelime uzadıysa ardındakileri it (kelime sırası korunur)
                if R[k][1] >= R[k - 1][2]: break
                R[k][1] = R[k - 1][2]; R[k][2] = max(R[k][2], R[k][1] + 0.06)
        if abs(R[-1][2] - (son - 0.05)) < 0.8 and son - 0.05 > R[-1][1] + 0.05: R[-1][2] = son - 0.05
        # çok kısa (<60 ms) kelimeler: komşudan pay al
        for k, x in enumerate(R):
            if x[2] - x[1] < 0.06:
                sonraki = R[k + 1][1] if k + 1 < len(R) else son
                x[2] = min(max(x[2], x[1] + 0.08), max(sonraki, x[1] + 0.03))
                if x[2] - x[1] < 0.06 and k > 0:
                    x[1] = max(R[k - 1][1] + 0.04, x[2] - 0.08); R[k - 1][2] = min(R[k - 1][2], x[1])
        for k in range(len(R) - 1):  # son geçiş: çakışma yok, en kısa 40 ms
            if R[k + 1][1] < R[k][1] + 0.04: R[k + 1][1] = R[k][1] + 0.04
            if R[k][2] > R[k + 1][1]: R[k][2] = R[k + 1][1]
        for x in R:
            say[x[4]] += 1
            out.append({"w": x[0], "s": round(x[1], 3), "e": round(x[2], 3), "p": round(x[3], 3), "sahne": sahne_of.get(ci), "cumle": ci, "kaynak": x[4]})
    atilan = [W[i] for i in sorted(set(atilan) - kullanilan)]
    ref_tum = open(yol(a.referans)).read().split()
    assert [o["w"] for o in out] == ref_tum, "hizalı kelimeler kilitli metinle birebir değil"
    BAD = [(i, out[i]) for i in range(len(out)) if out[i]["e"] - out[i]["s"] < 0.039 or (i + 1 < len(out) and out[i]["e"] > out[i + 1]["s"] + 1e-9)]
    if BAD: print("HATA kelime zamanı:", BAD[:8])
    assert all(o["e"] - o["s"] >= 0.039 for o in out) and all(out[i]["e"] <= out[i + 1]["s"] + 1e-9 for i in range(len(out) - 1)) and all(o["s"] < o["e"] for o in out) and all(out[i]["s"] <= out[i + 1]["s"] for i in range(len(out) - 1))
    json.dump({"kaynak": f"kilitli metin ({os.path.basename(a.referans)}) + Whisper zamanları ({os.path.basename(a.kelimeler)}) + TTS cümle sınırları ({os.path.basename(a.zaman)}); norm={a.norm}", "words": out},
              open(os.path.join(O, "kelimeler-hizali.json"), "w"), ensure_ascii=False, indent=0)
    cap = [{"text": (" " if i else "") + o["w"], "startMs": round(o["s"] * 1000), "endMs": round(o["e"] * 1000),
            "timestampMs": round((o["s"] + o["e"]) * 500), "confidence": o["p"]} for i, o in enumerate(out)]
    json.dump(cap, open(os.path.join(O, "altyazi-remotion.json"), "w"), ensure_ascii=False)
    def ts(x):
        ms = int(round(x * 1000)); h, ms = divmod(ms, 3600000); m, ms = divmod(ms, 60000); sn, ms = divmod(ms, 1000)
        return f"{h:02}:{m:02}:{sn:02},{ms:03}"
    KAR, SN = 42, 6.0
    def bol(ws):  # cümleyi <=2x42 karakter ve <=6 sn bloklara böl; noktalamada, ortaya en yakın yerden; <3 kelimelik artık yok
        metin = " ".join(o["w"] for o in ws)
        if (max(map(len, iki_satir(ws).split("\n"))) <= KAR and ws[-1]["e"] - ws[0]["s"] <= SN) or len(ws) < 6:
            return [ws]
        aday = [k for k in range(3, len(ws) - 2)]
        def puan(k):
            sol = len(" ".join(o["w"] for o in ws[:k])); return abs(sol - len(metin) / 2) - (25 if ws[k - 1]["w"][-1] in ",;:" else 0)
        k = min(aday, key=puan); return bol(ws[:k]) + bol(ws[k:])
    def iki_satir(ws):
        t = [o["w"] for o in ws]; m = " ".join(t)
        if len(m) <= KAR: return m
        k = min(range(1, len(t)), key=lambda k: abs(len(" ".join(t[:k])) - len(" ".join(t[k:]))) - (6 if t[k - 1][-1] in ",;:" else 0))
        return " ".join(t[:k]) + "\n" + " ".join(t[k:])
    bloklar = [b for ci in range(len(C)) for b in bol([o for o in out if o["cumle"] == ci])]
    srt = [f"{n}\n{ts(b[0]['s'])} --> {ts(max(b[-1]['e'], b[0]['s'] + 0.8))}\n{iki_satir(b)}\n" for n, b in enumerate(bloklar, 1)]
    open(os.path.join(O, a.srt_adi), "w").write("\n".join(srt))
    ust_uste = sum(bloklar[i][-1]["e"] > bloklar[i + 1][0]["s"] for i in range(len(bloklar) - 1))
    print(f"srt blok={len(bloklar)} maks satır={max(len(l) for x in srt for l in x.split(chr(10))[2:])} kar, maks süre={max(b[-1]['e']-b[0]['s'] for b in bloklar):.1f} sn, çakışma={ust_uste}")
    print("ara (tahmini zamanlı):", [(o["w"], o["s"]) for o in out if o["kaynak"] == "ara"])
    print(f"kelime={len(out)} (kilitli metin {len(ref_tum)}) whisper={say['whisper']} bolme={say['bolme']} ara={say['ara']}")
    print("atilan Whisper kelimeleri (metinde karşılığı yok):", [(round(w['s'], 2), w['w'], w['p']) for w in atilan])


if __name__ == "__main__":
    main()
