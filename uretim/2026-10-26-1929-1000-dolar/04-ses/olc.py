#!/usr/bin/env python3
"""F4 ses ölçümü (ses-yonetmeni, 2026-10-27). Yalnız standart kütüphane.

Kullanım: python3 -I olc.py   (04-ses klasöründe; önce tts.py + tts-son.sh + yaziya-dok.py koşmuş olmalı)
Girdi: anlatim-ham.zaman.json (tts.py cümle zamanları; tts-son.sh zamanı kaydırmaz: yalnız yeniden örnekleme +
       doğrusal kazanç), sahne-esleme.json, kelimeler.json (Whisper), referans-metni.txt, 03-metin/metin.md.
Çıkış: sahne-zamanlari.json + stdout'a rapor tabloları (sahne süreleri gerçek/tahmin, sahne başına WER,
       bölüm zamanları, yeniden kanca aralıkları, düşük güvenli kelimeler).
"""
import importlib.util, json, re
from pathlib import Path

KOK = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("ho", KOK.parents[2] / "tools" / "ses" / "hata-orani.py")
ho = importlib.util.module_from_spec(spec); spec.loader.exec_module(ho)


def mmss(s):
    return f"{int(s // 60)}:{s % 60:05.2f}"


def wer(r, h):
    r, h = ho.norm(r), ho.norm(h)
    d = list(range(len(h) + 1))
    for i in range(1, len(r) + 1):
        o, d[0] = d[0], i
        for j in range(1, len(h) + 1):
            o, d[j] = d[j], min(d[j] + 1, d[j - 1] + 1, o + (r[i - 1] != h[j - 1]))
    return d[-1], len(r)


zaman = json.load(open(KOK / "anlatim-ham.zaman.json"))["cumleler"]
esl = json.load(open(KOK / "sahne-esleme.json"))["sahneler"]
kel = json.load(open(KOK / "kelimeler.json"))["words"]
ref = (KOK / "referans-metni.txt").read_text(encoding="utf-8").splitlines()
md = (KOK.parent / "03-metin" / "metin.md").read_text(encoding="utf-8")
tahmin = {m[0]: (m[1], int(m[2])) for m in re.findall(r"^\| (S\d\d) \| (\d+:\d\d)–\d+:\d\d \| (\d+) \| \d+ \|$", md, re.M)}
assert len(zaman) == sum(e["cumle_son"] - e["cumle_ilk"] + 1 for e in esl), "cümle sayısı eşleşmiyor"
toplam = zaman[-1]["son"]

sahneler, satir, hata_t, kel_t = [], [], 0, 0
for k, e in enumerate(esl):
    bas = zaman[e["cumle_ilk"]]["bas"]
    son_ses = zaman[e["cumle_son"]]["son"]
    bitis = zaman[esl[k + 1]["cumle_ilk"]]["bas"] if k + 1 < len(esl) else toplam  # kesme noktası = sonraki sahne başı
    hyp = " ".join(w["w"] for w in kel if bas - 0.15 <= (w["s"] + w["e"]) / 2 < bitis)
    h, n = wer(ref[k], hyp); hata_t += h; kel_t += n
    tb, ts = tahmin[e["sahne"]]
    sahneler.append({"sahne": e["sahne"], "bas": round(bas, 3), "bitis": round(bitis, 3),
                     "konusma_bitis": round(son_ses, 3), "sure": round(bitis - bas, 3),
                     "cumle_ilk": e["cumle_ilk"], "cumle_son": e["cumle_son"], "kelime": e["kelime"]})
    satir.append(f"| {e['sahne']} | {mmss(bas)} | {mmss(bitis)} | {bitis - bas:.1f} | {tb} | {ts} | {bitis - bas - ts:+.1f} | "
                 f"{e['kelime'] / (son_ses - bas) * 60:.0f} | {h}/{n} |")
json.dump({"kaynak": "anlatim.wav (48 kHz) — zamanlar sn; bas/bitis = kesme noktaları (sahne arası sessizlik "
           "öndeki sahnede), konusma_bitis = son kelimenin bitişi", "toplam_sn": round(toplam, 3),
           "sahneler": sahneler}, open(KOK / "sahne-zamanlari.json", "w"), indent=1, ensure_ascii=False)

print(f"Toplam süre: {mmss(toplam)} ({toplam:.1f} sn) · tahmin 11:54 (714 sn) · fark {toplam - 714:+.1f} sn")
print(f"Ortalama hız: {sum(e['kelime'] for e in esl) / toplam * 60:.1f} kelime/dk (duraklamalar dahil)\n")
print("| Sahne | Başlangıç | Bitiş | Süre sn | Tahmini başlangıç | Tahmini süre | Fark sn | Konuşma kpm | WER (hata/kelime) |")
print("|---|---|---|---|---|---|---|---|---|")
print("\n".join(satir))
print(f"\nSahne toplamı WER: {hata_t}/{kel_t} = %{hata_t / kel_t * 100:.2f}")

# bölümler (metin §4) ve yeniden kancalar (metin §13) gerçek zamanlarla
def cumle_zamani(ifade):
    for c in zaman:
        if ifade.lower().replace("…", "") in c["metin"].lower():
            return c["bas"]
bolum = {"S01": "The game: $1,000 and three doors", "S05": "Door 1: The stock market", "S08": "Door 2: The bank",
         "S12": "Door 3: The shoebox", "S15": "The bottom: July 1932", "S18": "March 1933: every door locked",
         "S20": "The twist: the same door in 2026", "S23": "What the game really tests"}
print("\nBölümler (gerçek ses):")
for s in sahneler:
    if s["sahne"] in bolum:
        t = int(s["bas"]); print(f"{t // 60}:{t % 60:02d} {bolum[s['sahne']]}")
print("\n| ↺ | İfade | Gerçek zaman | Önceki kancadan aralık sn |")
print("|---|---|---|---|")
onceki = 0.0
for no, sid, ifade in re.findall(r"^\| (↺\d+|hook|köprü) \| (S\d\d) \| ([^|]+?) \| \d+:\d\d \|", md, re.M):
    ifade = ifade.split("(")[0].strip().split("…")[0].strip()
    t = cumle_zamani(ifade)
    if t is None:  # ifade birden çok cümleye yayılıyorsa ilk parçasıyla ara
        t = cumle_zamani(re.split(r"[.?!]", ifade)[0])
    print(f"| {no} | {ifade} | {mmss(t)} | {t - onceki:.0f} |"); onceki = t

dus = [w for w in kel if w["p"] < 0.5]
print(f"\nWhisper kelime sayısı {len(kel)}, ortalama güven {sum(w['p'] for w in kel) / len(kel):.3f}, güven<0,5: {len(dus)}")
for w in dus:
    print(f"  {mmss(w['s'])} {w['w']} ({w['p']})")
