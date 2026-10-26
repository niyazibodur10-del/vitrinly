# Dudak senkronu testi: ses enerjisi (kare başına RMS) ile ağız açıklığı zaman çizelgesi arasındaki
# en iyi korelasyon gecikmesini bulur. Kalite kapısı: |gecikme| <= 2 kare.
# Kullanım: python senkron-testi.py <ses-veya-video> <rhubarb.json> [fps]   (çıkış kodu: 0 GEÇTİ, 1 KALDI)
# 2026-10-26 düzeltme: kare sayısı len//(sr//fps) idi (16000//30=533 ≠ 533,3) → son karelerde boş dilim, korelasyon NaN,
# en iyi gecikme NaN'lar arasından seçiliyordu (60 sn'lik seste 'gecikme 0'da nan'). Artık n = len*fps//sr ve NaN elenir.
import sys, json, subprocess, numpy as np
src, cues = sys.argv[1], json.load(open(sys.argv[2]))["mouthCues"]
fps = int(sys.argv[3]) if len(sys.argv) > 3 else 30
sr = 16000
raw = subprocess.run(["ffmpeg", "-v", "error", "-i", src, "-ac", "1", "-ar", str(sr), "-f", "f32le", "-"], capture_output=True, check=True).stdout
a = np.frombuffer(raw, dtype=np.float32)
n = len(a) * fps // sr
rms = np.array([np.sqrt((a[i * sr // fps:(i + 1) * sr // fps] ** 2).mean()) for i in range(n)])
acik = {"X": 0, "A": 0, "B": 0.3, "C": 0.6, "D": 1, "E": 0.7, "F": 0.4, "G": 0.3, "H": 0.6}
m = np.zeros(n)
for c in cues:
    m[int(c["start"] * fps):int(c["end"] * fps)] = acik[c["value"]]
def corr(lag):
    x, y = (rms[lag:], m[:n - lag]) if lag >= 0 else (rms[:n + lag], m[-lag:])
    return np.corrcoef(x, y)[0, 1]
lags = range(-8, 9)
r = {l: corr(l) for l in lags}
r = {l: v for l, v in r.items() if np.isfinite(v)}
if not r:
    sys.exit("HATA: korelasyon hesaplanamadı (sessiz ses veya boş ağız çizelgesi)")
best = max(r, key=r.get)
print(f"en iyi gecikme: {best} kare ({best / fps * 1000:.0f} ms), korelasyon {r[best]:.2f}, gecikme 0'da {r.get(0, float('nan')):.2f}")
print("GEÇTİ" if abs(best) <= 2 else "KALDI")
sys.exit(0 if abs(best) <= 2 else 1)
