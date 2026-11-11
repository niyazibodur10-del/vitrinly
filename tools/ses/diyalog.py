#!/usr/bin/env python3
"""İki (veya daha çok) karakterli diyalog seslendirmesi — Flip By Vote dizisi (Kokoro-82M, Apache-2.0, yerel, ücretsiz).

Kullanım (kokoro-venv):
  ~/.finansal-arac/kokoro-venv/bin/python tools/ses/diyalog.py <diyalog.txt> <cikis.wav>
      [--ses JAKE=am_onyx:0.95 --ses MIKE=am_fenrir:1.05] [--ham]
Girdi satırları:
  JAKE: Hold on. A price is just a number until someone pays it.
  MIKE (0.15): Jake, we don't need more money, we need more guts!   <- parantez = bu satırdan ÖNCEKİ boşluk (sn), elle
  # ile başlayan ve boş satırlar atlanır. misaki fonetik işareti geçerli: [Toonomy](/tˈunəmi/) (JSON/txt'de düz yazıya döner).
Çıkışlar (cikis.wav = <ad>.wav):
  <ad>.wav              tüm diyalog, 48 kHz mono 24-bit, -14 LUFS, TP <= -1.5 (tools/ses/tts-son.sh zinciri)
  <ad>.zaman.json       {"sesler":..., "sure":..., "satirlar":[{"no","konusmaci","bas","bitis","metin"}]} (sn, son dosyada)
  <ad>-<KONUSMACI>.wav  aynı uzunlukta, yalnız o konuşmacı (diğerleri sıfır) → Rhubarb; zamanlar ana dosyayla birebir
  <ad>-<KONUSMACI>.txt  o konuşmacının replikleri (Rhubarb --dialogFile)
  --ham: ayrıca <ad>-ham.wav (24 kHz, işlem öncesi)
Boşluk kuralı (sahne yönetimi; elle parantezle ezilir):
  - konuşmacı değişimi: varsayılan 0.30 sn; yanıtlayan HIZLI karakterse (MIKE) 0.22, TEMKİNLİ karakterse (JAKE) 0.42
    (Jake düşünüp konuşur, Mike lafı kapar). --bosluk KONUSMACI=sn ile değişir.
  - aynı konuşmacı yeni satır: 0.45 · satır içi cümle arası: 0.28 · soru/ünlem sonrası cümle: 0.32
  - başta 0.15, sonda 0.30 sn sessizlik.
Seviye: her konuşmacının etkin (>-40 dBFS) RMS'i ortak hedefe eşitlenir (Kokoro sesleri arasında ~2–4 dB fark var), sonra
  tüm diyalog tts-son.sh'tan geçer (highpass 70, de-ess, hafif kompresör, sınırlayıcı, 2 geçişli loudnorm). Gürültü
  giderme (temizle.sh/RNNoise) TTS'te KULLANILMAZ — temiz kaynakta artefakt yapar (hafıza 2026-10-26).
  Konuşmacı izleri son işlenmiş dosyadan zaman maskesiyle kesilir (10 ms rampa) → seviye ve zaman ana dosyayla aynı.
Motorlar (2026-11-11): --ses JAKE=pocket:michael gibi "motor:ses[:hiz]" (tools/ses/gercekci_tts.py); gerçekçi motorlar için
  ~/.finansal-arac/gercekci-venv/bin/python ile çalıştır (kokoro da orada). Tam bölüm hattı: tools/ses/bolum-ses.sh.
Yazan: ses-yonetmeni 2026-11-10 (seçim raporu uretim/seri/sesler/rapor.md).
"""
import argparse, json, os, re, subprocess, sys, tempfile
import numpy as np, soundfile as sf

SR = 24000
VARSAYILAN_SES = {"JAKE": "pocket:george", "MIKE": "pocket:marius"}  # Niyazi seçimi 2026-11-11 (gercekci/rapor.md)
VARSAYILAN_BOSLUK = {"JAKE": 0.42, "MIKE": 0.22}  # konuşmacı değişiminde, yanıtlayanın karakterine göre
DIGER_BOSLUK, AYNI_KONUSMACI, CUMLE, CUMLE_VURGU, BAS, SON = 0.30, 0.45, 0.28, 0.32, 0.15, 0.30
SATIR = re.compile(r"^\s*([A-Za-z][\w ]*?)\s*(?:\(\s*([\d.]+)\s*\))?\s*:\s*(.+?)\s*$")
duz = lambda m: re.sub(r"\[([^\]]+)\]\((?:/[^)]*/|[+-]?\d+(?:\.\d+)?)\)", r"\1", m)


def oku(yol):
    satirlar = []
    for i, s in enumerate(open(yol, encoding="utf-8"), 1):
        if not s.strip() or s.lstrip().startswith("#"):
            continue
        m = SATIR.match(s)
        if not m:
            sys.exit(f"{yol}:{i}: 'KONUSMACI: metin' biçiminde değil: {s.strip()}")
        satirlar.append({"konusmaci": m.group(1).strip().upper(),
                         "bosluk": float(m.group(2)) if m.group(2) else None, "metin": m.group(3)})
    return satirlar


def cumleler(metin):
    c = [x.strip() for x in re.findall(r".+?(?:\.\.\.|[.!?…]+|$)(?=\s+|$)", metin) if x.strip()]
    return c or [metin]


def kirp(y):
    nz = np.where(np.abs(y) > 10 ** (-50 / 20))[0]  # tts.py ile aynı: baş 30 ms, son 50 ms pay
    if len(nz):
        y = y[max(nz[0] - 720, 0): nz[-1] + 1200].copy()
    f = min(120, len(y) // 4)
    y[:f] *= np.linspace(0, 1, f); y[-f:] *= np.linspace(1, 0, f)
    return y


def etkin_rms(y):
    k = 480  # 20 ms kare
    n = len(y) // k
    r = np.sqrt(np.mean(y[: n * k].reshape(n, k) ** 2, axis=1))
    r = r[r > 10 ** (-40 / 20)]
    return float(np.sqrt(np.mean(r ** 2))) if len(r) else 1e-6


def _olc(yol, ek=""):
    o = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", yol, "-af", ek + "loudnorm=I=-14:TP=-1.5:LRA=11:print_format=json",
                        "-f", "null", "-"], capture_output=True, text=True).stderr
    return json.loads(o[o.rindex("{"):o.rindex("}") + 1])


def lufs_duzelt(yol):
    """tts-son.sh tepe sınırına takılıp −14,5'in altında kalırsa (Pocket: tepe/ortalama oranı yüksek; 2026-11-11 Bölüm 1
    −14,6 LUFS) kazanç + 4x aşırı örneklemeli sınırlayıcı (true peak ≤ −1,5) uygular; I hedefe gelene kadar sınırı indirir."""
    I = float(_olc(yol)["input_i"])
    if I >= -14.5:
        return
    kaynak = yol + ".kaynak.wav"; os.replace(yol, kaynak)
    for ek_kazanc in (0.0, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0):
        g = -14.0 - I + ek_kazanc
        af = (f"volume={g:.2f}dB,aresample=192000,alimiter=limit=-2.2dB:attack=0.5:release=50:level=false,"
              "aresample=48000")
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", kaynak, "-af", af, "-ar", "48000", "-ac", "1",
                        "-c:a", "pcm_s24le", yol], check=True)
        j = _olc(yol)
        if float(j["input_i"]) >= -14.3 and float(j["input_tp"]) <= -1.0:
            break
    os.remove(kaynak)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("metin"); ap.add_argument("cikis")
    ap.add_argument("--ses", action="append", default=[], help="KONUSMACI=motor:ses[:hiz] (pocket:michael, supertonic:M4, am_onyx:0.95)")
    ap.add_argument("--bosluk", action="append", default=[], help="KONUSMACI=sn (bu konuşmacı yanıt verirken)")
    ap.add_argument("--ham", action="store_true")
    a = ap.parse_args()

    sesler = dict(VARSAYILAN_SES); sesler.update(dict(x.split("=", 1) for x in a.ses))
    bosluk = dict(VARSAYILAN_BOSLUK); bosluk.update({k: float(v) for k, v in (x.split("=", 1) for x in a.bosluk)})
    satirlar = oku(a.metin)
    eksik = {s["konusmaci"] for s in satirlar} - set(sesler)
    if eksik:
        sys.exit(f"ses tanımı yok: {sorted(eksik)} (--ses AD=pocket:michael)")
    import torch
    torch.set_num_threads(os.cpu_count() or 4)
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from gercekci_tts import Motor  # motor:ses:hiz (pocket/supertonic/kokoro); "am_x:hiz" = kokoro
    motor = {k: Motor(v) for k, v in sesler.items() if k in {s["konusmaci"] for s in satirlar}}

    # 1) satırları üret: gerçekçi motorlar satırı tek parça (doğal prozodi), Kokoro cümle cümle + duraklama
    for s in satirlar:
        mo = motor[s["konusmaci"]]
        metin = duz(s["metin"]) if mo.motor != "kokoro" else s["metin"]  # misaki IPA işareti yalnız Kokoro'da geçerli
        if mo.satir_butun:
            s["y"] = kirp(mo.uret(metin))
            continue
        parca = []
        for c in cumleler(metin):
            parca += [kirp(mo.uret(c)), np.zeros(int((CUMLE_VURGU if c[-1] in "!?" else CUMLE) * SR), np.float32)]
        s["y"] = np.concatenate(parca[:-1])

    # 2) konuşmacı seviyesi eşitle (etkin RMS, ortak hedef = konuşmacı ortalamalarının geometrik ortası)
    rms = {k: etkin_rms(np.concatenate([s["y"] for s in satirlar if s["konusmaci"] == k]))
           for k in {s["konusmaci"] for s in satirlar}}
    hedef = float(np.exp(np.mean(np.log(list(rms.values())))))
    for s in satirlar:
        s["y"] = s["y"] * (hedef / rms[s["konusmaci"]])

    # 3) zaman çizelgesi
    parcalar, t, onceki = [np.zeros(int(BAS * SR), np.float32)], BAS, None
    for i, s in enumerate(satirlar):
        if i:
            b = s["bosluk"]
            if b is None:
                b = AYNI_KONUSMACI if s["konusmaci"] == onceki else bosluk.get(s["konusmaci"], DIGER_BOSLUK)
            parcalar.append(np.zeros(int(round(b * SR)), np.float32)); t += int(round(b * SR)) / SR
        s["bas"], s["bitis"] = t, t + len(s["y"]) / SR
        parcalar.append(s["y"].astype(np.float32)); t = s["bitis"]; onceki = s["konusmaci"]
    parcalar.append(np.zeros(int(SON * SR), np.float32))
    ham = np.concatenate(parcalar)

    # 4) son işlem (mevcut TTS hattı) + konuşmacı izleri
    taban = re.sub(r"\.wav$", "", a.cikis)
    araclar = os.path.dirname(os.path.abspath(__file__))
    with tempfile.TemporaryDirectory() as tmp:
        hy = f"{taban}-ham.wav" if a.ham else os.path.join(tmp, "ham.wav")
        sf.write(hy, ham, SR, subtype="FLOAT")
        subprocess.run(["bash", os.path.join(araclar, "tts-son.sh"), hy, a.cikis], check=True)
    lufs_duzelt(a.cikis)
    son, sr2 = sf.read(a.cikis, dtype="float32")
    rampa = int(0.010 * sr2)
    for k in sorted(rms):
        maske = np.zeros(len(son), np.float32)
        for s in satirlar:
            if s["konusmaci"] != k:
                continue
            i0, i1 = max(int(s["bas"] * sr2) - rampa, 0), min(int(s["bitis"] * sr2) + rampa, len(son))
            maske[i0:i1] = 1.0
            maske[i0:i0 + rampa] = np.minimum(maske[i0:i0 + rampa], np.linspace(0, 1, min(rampa, i1 - i0)))
            maske[i1 - rampa:i1] = np.minimum(maske[i1 - rampa:i1], np.linspace(1, 0, rampa))
        sf.write(f"{taban}-{k}.wav", son * maske, sr2, subtype="PCM_24")
        open(f"{taban}-{k}.txt", "w", encoding="utf-8").write(
            "\n".join(duz(s["metin"]) for s in satirlar if s["konusmaci"] == k) + "\n")
    json.dump({"sesler": sesler, "sure": round(len(son) / sr2, 3),
               "satirlar": [{"no": i + 1, "konusmaci": s["konusmaci"], "bas": round(s["bas"], 3),
                             "bitis": round(s["bitis"], 3), "metin": duz(s["metin"])} for i, s in enumerate(satirlar)]},
              open(f"{taban}.zaman.json", "w"), indent=1, ensure_ascii=False)
    print(f"{os.path.basename(a.cikis)}: {len(son) / sr2:.2f} sn, {len(satirlar)} satır, "
          + ", ".join(f"{k}={sesler[k]}" for k in sorted(rms)) + " | seviye düzeltme "
          + ", ".join(f"{k} {20 * np.log10(hedef / rms[k]):+.1f} dB" for k in sorted(rms)))


if __name__ == "__main__":
    main()
