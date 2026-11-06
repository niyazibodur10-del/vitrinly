# Dudak senkronu testi: ses enerjisi (kare başına RMS) ile ağız açıklığı zaman çizelgesi arasındaki
# en iyi korelasyon gecikmesini bulur. Kalite kapısı: |gecikme| <= 2 kare.
# Kullanım: python senkron-testi.py <ses-veya-video> <rhubarb.json> [fps] [--araliklar 2.1-8.0,30-45] [--bant 700-3000|formant]
#           [--ofset SN] [--esik 2]          (çıkış kodu: 0 GEÇTİ, 1 KALDI, 2 kullanım hatası)
#   --araliklar  yalnız ağzın ekranda göründüğü aralıklarda ölç (sn, ses/video ekseninde). Her aralık kendi içinde
#                z-normalize edilip birleştirilir (= aralık korelasyonlarının uzunluk ağırlıklı ortalaması); ses kayması
#                aralık dışına taşabilir (gecikme sınırı ±8 kare). Aralık başına sonuç da yazılır; kapı birleşik sonuca bakar.
#   --bant       RMS'ten önce bant geçiren süzgeç (ffmpeg highpass+lowpass, 2 kutup). "formant" = 700-3000 Hz.
#   --ofset      çizelge zamanlarına eklenecek sn (Rhubarb sahne kesitinde çalıştıysa kesitin ses eksenindeki başı).
# 2026-10-26 düzeltme: kare sayısı len//(sr//fps) idi (16000//30=533 ≠ 533,3) → son karelerde boş dilim, korelasyon NaN,
# en iyi gecikme NaN'lar arasından seçiliyordu (60 sn'lik seste 'gecikme 0'da nan'). Artık n = len*fps//sr ve NaN elenir.
# 2026-10-27 (1929-1000-dolar F5, animasyon-yonetmeni talebi): tüm-video ölçümü ekranda ağız olmayan dış ses bölümünden
#   (klonlar yürürken) −4 kare KALDI veriyordu; ekranda ağız aralığı −1 GEÇTİ. Aralık ve bant seçeneği eklendi.
#   Adaylar: A) aralıkları kesip ayrı dosyada ölçmek (ffmpeg -ss; kesit ucunda kayma payı kaybolur, aralıklar ayrı
#   kapı) — elendi; B) tek ses, aralık maskeli birleşik korelasyon (seçilen: kayma aralık dışına taşabilir, tek kapı);
#   bant: ffmpeg süzgeci (seçilen; animasyon-yonetmeni ölçümüyle birebir) vs numpy FFT maskesi (bağımlılık yok ama
#   farklı sonuç → iki ölçüm karşılaştırılamaz) — elendi. Seçenek verilmezse sonuç eski sürümle aynı (test: tools/test_senkron.py).
import argparse, json, subprocess, sys
import numpy as np

ACIK = {"X": 0, "A": 0, "B": 0.3, "C": 0.6, "D": 1, "E": 0.7, "F": 0.4, "G": 0.3, "H": 0.6}
SR = 16000
LAGS = range(-8, 9)


def araliklari_coz(metin):
    out = []
    for parca in filter(None, (x.strip() for x in metin.split(","))):
        try:
            a, b = (float(v) for v in parca.split("-"))
        except ValueError:
            raise argparse.ArgumentTypeError(f"aralık '{parca}' anlaşılmadı (ör. 2.1-8.0)")
        if not 0 <= a < b:
            raise argparse.ArgumentTypeError(f"aralık '{parca}': başlangıç < bitiş ve >= 0 olmalı")
        out.append((a, b))
    if not out:
        raise argparse.ArgumentTypeError("boş aralık listesi")
    return out


def bant_coz(metin):
    if metin == "formant":
        metin = "700-3000"
    try:
        lo, hi = (float(v) for v in metin.split("-"))
    except ValueError:
        raise argparse.ArgumentTypeError(f"bant '{metin}' anlaşılmadı (ör. 700-3000 veya formant)")
    if not 0 < lo < hi < SR / 2:
        raise argparse.ArgumentTypeError(f"bant {lo}-{hi}: 0 < alt < üst < {SR // 2} olmalı")
    return lo, hi


def rms_dizisi(src, fps, bant=None):
    af = ["-af", f"highpass=f={bant[0]:g},lowpass=f={bant[1]:g}"] if bant else []
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", src] + af + ["-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    a = np.frombuffer(raw, dtype=np.float32)
    n = len(a) * fps // SR
    return np.array([np.sqrt((a[i * SR // fps:(i + 1) * SR // fps] ** 2).mean()) for i in range(n)])


def agiz_dizisi(cues, n, fps, ofset=0.0):
    m = np.zeros(n)
    for c in cues:
        m[max(0, int((c["start"] + ofset) * fps)):max(0, int((c["end"] + ofset) * fps))] = ACIK[c["value"]]
    return m


def korelasyon(rms, m, lag, pencereler):
    """pencereler: [(i0, i1)] ağız kare indeksleri. Çiftler (rms[i+lag], m[i]); her pencere kendi içinde z-normalize."""
    n = len(rms); xs, ys = [], []
    for i0, i1 in pencereler:
        i = np.arange(max(i0, -lag, 0), min(i1, n - lag, n))
        if len(i) < 3:
            continue
        x, y = rms[i + lag], m[i]
        if x.std() == 0 or y.std() == 0:
            continue
        xs.append((x - x.mean()) / x.std()); ys.append((y - y.mean()) / y.std())
    if not xs:
        return float("nan")
    x, y = np.concatenate(xs), np.concatenate(ys)
    return float(np.mean(x * y))


def olc(rms, m, pencereler):
    r = {l: korelasyon(rms, m, l, pencereler) for l in LAGS}
    r = {l: v for l, v in r.items() if np.isfinite(v)}
    if not r:
        return None, r
    return max(r, key=r.get), r


def main(argv=None):
    p = argparse.ArgumentParser(description="Dudak senkronu kapısı (|gecikme| <= eşik kare)")
    p.add_argument("kaynak"); p.add_argument("cizelge"); p.add_argument("fps", nargs="?", type=int, default=30)
    p.add_argument("--araliklar", type=araliklari_coz, help="ör. 2.1-8.0,30-45 (sn)")
    p.add_argument("--bant", type=bant_coz, help="ör. 700-3000 veya formant")
    p.add_argument("--ofset", type=float, default=0.0, help="çizelge zamanlarına eklenecek sn")
    p.add_argument("--esik", type=int, default=2, help="kapı eşiği, kare (varsayılan 2)")
    a = p.parse_args(argv)
    fps = a.fps
    rms = rms_dizisi(a.kaynak, fps, a.bant)
    n = len(rms)
    m = agiz_dizisi(json.load(open(a.cizelge))["mouthCues"], n, fps, a.ofset)
    if a.araliklar:
        pencereler = [(int(round(s * fps)), min(n, int(round(e * fps)))) for s, e in a.araliklar]
        bos = [f"{s:g}-{e:g}" for (s, e), (i0, i1) in zip(a.araliklar, pencereler) if i1 - i0 < 3]
        if bos:
            print(f"HATA: aralık ses süresinin ({n / fps:.2f} sn) dışında veya çok kısa: {', '.join(bos)}", file=sys.stderr)
            return 2
    else:
        pencereler = [(0, n)]
    if a.bant:
        print(f"bant: {a.bant[0]:g}-{a.bant[1]:g} Hz")
    if a.araliklar and len(pencereler) > 1:
        for (s, e), pw in zip(a.araliklar, pencereler):
            b, r = olc(rms, m, [pw])
            print(f"  aralık {s:g}-{e:g} sn: " + (f"gecikme {b} kare, korelasyon {r[b]:.2f}" if b is not None else "ölçülemedi (sessiz/ağız sabit)"))
    best, r = olc(rms, m, pencereler)
    if best is None:
        sys.exit("HATA: korelasyon hesaplanamadı (sessiz ses veya boş ağız çizelgesi)")
    kapsam = f" [{len(pencereler)} aralık, {sum(i1 - i0 for i0, i1 in pencereler) / fps:.1f} sn]" if a.araliklar else ""
    print(f"en iyi gecikme: {best} kare ({best / fps * 1000:.0f} ms), korelasyon {r[best]:.2f}, gecikme 0'da {r.get(0, float('nan')):.2f}{kapsam}")
    gecti = abs(best) <= a.esik
    print("GEÇTİ" if gecti else "KALDI")
    return 0 if gecti else 1


if __name__ == "__main__":
    sys.exit(main())
