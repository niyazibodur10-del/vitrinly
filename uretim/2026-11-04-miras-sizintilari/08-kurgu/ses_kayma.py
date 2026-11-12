#!/usr/bin/env python3
"""Son videonun sesi anlatim.wav ile aynı zamanda mı? 12 pencerede (8 sn) çapraz korelasyon → gecikme (ms).
Kullanım: ~/.finansal-arac/venv/bin/python ses_kayma.py <son.mp4> <anlatim.wav> [pencere başlangıçları...]
Altyazı (SRT) zamanları anlatim.wav eksenindedir; gecikme ≈0 ise SRT'nin son videoya hizası = anlatıma akustik hizası
(ses-muhendisi ölçümü: p95 7/15 ms). Whisper kelime başları cümle başında sessizliğe taştığı için (ör. "Quick" Whisper 268.44,
akustik 269.38) doğrudan Whisper karşılaştırması hiza kapısı için güvenilmez — yalnız bilgi amaçlı raporlanır."""
import subprocess, sys, json
import numpy as np
SR = 8000
def coz(y):
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", y, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"], capture_output=True, check=True).stdout
    return np.frombuffer(r, np.float32)
a = coz(sys.argv[1]); b = coz(sys.argv[2])
n = min(len(a), len(b)); out = []
bas = [float(x) for x in sys.argv[3:]] or list(np.linspace(5, n / SR - 15, 12))
for t in bas:
    i = int(t * SR); L = 8 * SR; m = int(0.25 * SR)
    x = a[i:i + L]; y = b[i - m:i + L + m]
    c = np.correlate(y, x, "valid")
    k = int(np.argmax(c)) - m
    out.append({"t": round(t, 1), "gecikme_ms": round(-k / SR * 1000, 1), "kor": round(float(c.max() / (np.linalg.norm(x) * np.linalg.norm(y[m + k:m + k + L]) + 1e-9)), 3)})
print(json.dumps(out))
print("maks |gecikme| ms:", max(abs(o["gecikme_ms"]) for o in out))
