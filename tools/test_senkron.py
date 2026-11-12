#!/usr/bin/env python3
# senkron-testi.py testleri (sentetik ses + bilinen kaymalı ağız çizelgesi; ağsız, ~2 sn).
# Kullanım: python3 tools/test_senkron.py
import importlib.util
import io
import json
import os
import subprocess
import sys
import tempfile
import unittest
import wave
from contextlib import redirect_stdout

import numpy as np

B = os.path.dirname(os.path.abspath(__file__))
_s = importlib.util.spec_from_file_location("st", os.path.join(B, "senkron-testi.py"))
st = importlib.util.module_from_spec(_s); _s.loader.exec_module(st)
FPS, SR = 30, 16000


def hece_sesi(sure, rng):
    """Rastgele uzunlukta hece patlamaları (1 kHz taşıyıcı + gürültü) ve hece listesi (bas, son sn)."""
    a = np.zeros(int(sure * SR), np.float32); heceler = []; t = 0.1
    while t < sure - 0.4:
        d = rng.uniform(0.08, 0.3); g = rng.uniform(0.05, 0.25)
        i0, i1 = int(t * SR), int((t + d) * SR)
        zarf = np.hanning(i1 - i0)
        a[i0:i1] = 0.5 * zarf * (np.sin(2 * np.pi * 1000 * np.arange(i1 - i0) / SR) + 0.3 * rng.standard_normal(i1 - i0))
        heceler.append((t, t + d)); t += d + g
    return a, heceler


def cizelge(heceler, kayma_sn=0.0):
    cues, t = [], 0.0
    for s, e in heceler:
        s, e = s + kayma_sn, e + kayma_sn
        if s > t:
            cues.append({"start": round(t, 3), "end": round(s, 3), "value": "X"})
        cues.append({"start": round(max(s, t), 3), "end": round(e, 3), "value": "D"}); t = e
    return {"mouthCues": cues}


def wav_yaz(yol, a):
    with wave.open(yol, "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes((np.clip(a, -1, 1) * 32767).astype(np.int16).tobytes())


def calistir(*arg):
    f = io.StringIO()
    with redirect_stdout(f):
        kod = st.main([str(x) for x in arg])
    return kod, f.getvalue()


class SenkronTesti(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        rng = np.random.default_rng(7)
        a, h = hece_sesi(20.0, rng)
        cls.wav = os.path.join(cls.tmp.name, "s.wav"); wav_yaz(cls.wav, a)
        # 0–10 sn doğru, 10–20 sn ağız 5 kare (167 ms) erken (dış ses bölümü gibi)
        ilk = [x for x in h if x[1] <= 10.0]; son = [x for x in h if x[0] >= 10.0]
        c1, c2 = cizelge(ilk), cizelge(son, -5 / FPS)
        c = {"mouthCues": c1["mouthCues"] + [q for q in c2["mouthCues"] if q["start"] >= 10.0 - 5 / FPS]}
        cls.karisik = os.path.join(cls.tmp.name, "karisik.json"); json.dump(c, open(cls.karisik, "w"))
        cls.dogru = os.path.join(cls.tmp.name, "dogru.json"); json.dump(cizelge(h), open(cls.dogru, "w"))
        cls.gec = os.path.join(cls.tmp.name, "gec.json"); json.dump(cizelge(h, 4 / FPS), open(cls.gec, "w"))
        # sahne kesiti çizelgesi: 10 sn'den başlayan kesitte çalışmış gibi (zamanlar 0'dan)
        cls.kesit = os.path.join(cls.tmp.name, "kesit.json")
        json.dump(cizelge([(s - 10.0, e - 10.0) for s, e in son]), open(cls.kesit, "w"))

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_dogru_gecer(self):
        kod, out = calistir(self.wav, self.dogru)
        self.assertEqual(kod, 0, out); self.assertIn("en iyi gecikme: 0 kare", out)

    def test_bilinen_kayma_kalir(self):  # ağız 4 kare geç → gecikme -4, KALDI
        kod, out = calistir(self.wav, self.gec)
        self.assertEqual(kod, 1, out); self.assertIn("en iyi gecikme: -4 kare", out)

    def test_aralik_yalniz_dogru_bolge(self):
        self.assertEqual(calistir(self.wav, self.karisik, "--araliklar", "0.5-9.5")[0], 0)
        kod, out = calistir(self.wav, self.karisik, "--araliklar", "10.5-19.5")
        self.assertEqual(kod, 1); self.assertIn("en iyi gecikme: 5 kare", out)  # ağız erken → +5

    def test_coklu_aralik_satirlari(self):
        kod, out = calistir(self.wav, self.dogru, "--araliklar", "1-5,12-18")
        self.assertEqual(kod, 0); self.assertEqual(out.count("aralık "), 2); self.assertIn("[2 aralık, 10.0 sn]", out)

    def test_ofset(self):
        kod, out = calistir(self.wav, self.kesit, "--ofset", "10", "--araliklar", "10.5-19.5")
        self.assertEqual(kod, 0, out); self.assertIn("en iyi gecikme: 0 kare", out)

    def test_bant(self):
        kod, out = calistir(self.wav, self.dogru, "--bant", "formant")
        self.assertEqual(kod, 0, out); self.assertIn("bant: 700-3000 Hz", out)
        self.assertEqual(calistir(self.wav, self.gec, "--bant", "700-3000")[0], 1)

    def test_tam_pencere_eski_formulle_ayni(self):
        rms = st.rms_dizisi(self.wav, FPS); n = len(rms)
        m = st.agiz_dizisi(json.load(open(self.karisik))["mouthCues"], n, FPS)
        for lag in range(-8, 9):
            x, y = (rms[lag:], m[:n - lag]) if lag >= 0 else (rms[:n + lag], m[-lag:])
            self.assertAlmostEqual(st.korelasyon(rms, m, lag, [(0, n)]), np.corrcoef(x, y)[0, 1], places=6)  # rms float32

    def test_hatali_aralik(self):
        self.assertEqual(calistir(self.wav, self.dogru, "--araliklar", "30-45")[0], 2)
        r = subprocess.run([sys.executable, os.path.join(B, "senkron-testi.py"), self.wav, self.dogru, "--araliklar", "8-2"],
                           capture_output=True, text=True)
        self.assertEqual(r.returncode, 2); self.assertIn("başlangıç < bitiş", r.stderr)

    def test_eski_konum_fps(self):  # eski çağrı biçimi: <kaynak> <json> [fps]
        r = subprocess.run([sys.executable, os.path.join(B, "senkron-testi.py"), self.wav, self.dogru, "30"], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=1, warnings="ignore")
