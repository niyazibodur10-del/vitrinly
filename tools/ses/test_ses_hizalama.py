#!/usr/bin/env python3
# tools/ses/ hizalama betikleri testleri: hizala.py, hiza-dogrula.py, rhubarb-hazirla.py (cumle-whisper.py modelli → elle).
# Kullanım: ~/.finansal-arac/venv/bin/python tools/ses/test_ses_hizalama.py   (numpy + soundfile gerekir; ~5 sn)
# Sentetik testler her yerde koşar; 1929-1000-dolar kilitli çıktısıyla bayt karşılaştırması (git'teki json'lar) her zaman,
# wav gerektirenler (git dışı) wav yoksa atlanır.
import filecmp
import json
import os
import subprocess
import sys
import tempfile
import unittest

import numpy as np
import soundfile as sf

B = os.path.dirname(os.path.abspath(__file__))
KOK = os.path.abspath(os.path.join(B, "..", ".."))
V1929 = os.path.join(KOK, "uretim", "2026-10-26-1929-1000-dolar", "04-ses")
PY = sys.executable


def kos(betik, *arg):
    return subprocess.run([PY, "-I", os.path.join(B, betik), *map(str, arg)], capture_output=True, text=True)


def sentetik(d, kayma=0.0):
    """3 cümlelik TTS benzeri anlatım: cümle = ton patlaması, arada dijital sessizlik."""
    sr = 24000; y = np.zeros(int(6.0 * sr)); C = []; W = []
    metin = ["Hello there friend.", "It's September 3rd.", "You have $1,000."]
    for i, (bas, son) in enumerate([(0.2, 1.6), (2.2, 3.6), (4.2, 5.6)]):
        n = int((son - bas) * sr)
        y[int(bas * sr):int(bas * sr) + n] = 0.3 * np.sin(2 * np.pi * 220 * np.arange(n) / sr)
        C.append({"bas": bas - 0.03, "son": son + 0.05, "metin": metin[i]})
        kel = metin[i].split(); d_ = (son - bas) / len(kel)
        W += [{"w": k, "s": round(bas + j * d_ + kayma, 3), "e": round(bas + (j + 1) * d_ + kayma, 3), "p": 0.9} for j, k in enumerate(kel)]
    sf.write(os.path.join(d, "anlatim.wav"), y, sr)
    json.dump({"cumleler": C}, open(os.path.join(d, "anlatim-ham.zaman.json"), "w"))
    json.dump({"text": " ".join(metin), "words": W}, open(os.path.join(d, "kelimeler.json"), "w"))
    json.dump({"sahneler": [{"sahne": "S01", "bas": 0.0, "bitis": 2.1, "cumle_ilk": 0, "cumle_son": 0},
                            {"sahne": "S02", "bas": 2.1, "bitis": 6.0, "cumle_ilk": 1, "cumle_son": 2}]},
              open(os.path.join(d, "sahne-zamanlari.json"), "w"))
    open(os.path.join(d, "referans-metni.txt"), "w").write(" ".join(metin) + "\n")


class Sentetik(unittest.TestCase):
    def setUp(self):
        self.t = tempfile.TemporaryDirectory(); self.d = self.t.name; sentetik(self.d)

    def tearDown(self):
        self.t.cleanup()

    def test_hizala_ve_dogrula_gecer(self):
        r = kos("hizala.py", "--dizin", self.d); self.assertEqual(r.returncode, 0, r.stderr)
        out = json.load(open(os.path.join(self.d, "kelimeler-hizali.json")))["words"]
        self.assertEqual([o["w"] for o in out], open(os.path.join(self.d, "referans-metni.txt")).read().split())
        self.assertTrue(os.path.exists(os.path.join(self.d, "altyazi-remotion.json")))
        r = kos("hiza-dogrula.py", "--dizin", self.d); self.assertEqual(r.returncode, 0, r.stdout + r.stderr); self.assertIn("GEÇTİ", r.stdout)

    def test_kayik_hiza_kalir(self):  # bilinen-kötü girdi: hizalı kelimeler 0,3 sn geç → kapı KALDI (çıkış 1)
        kos("hizala.py", "--dizin", self.d)
        p = os.path.join(self.d, "kelimeler-hizali.json"); h = json.load(open(p))
        for o in h["words"]:
            o["s"] += 0.3; o["e"] += 0.3
        json.dump(h, open(p, "w"))
        r = kos("hiza-dogrula.py", "--dizin", self.d); self.assertEqual(r.returncode, 1, r.stdout); self.assertIn("KALDI", r.stdout)

    def test_cikis_dizini_ve_mutlak_yollar(self):
        c = os.path.join(self.d, "cikti")
        r = kos("hizala.py", "--kelimeler", os.path.join(self.d, "kelimeler.json"), "--zaman", os.path.join(self.d, "anlatim-ham.zaman.json"),
                "--sahneler", os.path.join(self.d, "sahne-zamanlari.json"), "--referans", os.path.join(self.d, "referans-metni.txt"), "--cikis", c)
        self.assertEqual(r.returncode, 0, r.stderr)
        self.assertEqual(sorted(os.listdir(c)), ["altyazi-remotion.json", "altyazi-taslak.en.srt", "kelimeler-hizali.json"])

    def test_rhubarb_hazirla(self):
        r = kos("rhubarb-hazirla.py", "--dizin", self.d); self.assertEqual(r.returncode, 0, r.stderr)
        o = os.path.join(self.d, "rhubarb")
        self.assertEqual(open(os.path.join(o, "S02.txt")).read(), "It's September 3rd. You have $1,000.\n")
        y, sr = sf.read(os.path.join(o, "S02.wav")); self.assertEqual(sr, 16000); self.assertAlmostEqual(len(y) / sr, 3.9, delta=0.01)
        self.assertEqual([s["ofset_sn"] for s in json.load(open(os.path.join(o, "sahneler.json")))["sahneler"]], [0.0, 2.1])
        r = kos("rhubarb-hazirla.py", "--dizin", self.d, "--sahne", "S09"); self.assertNotEqual(r.returncode, 0)


class Kilitli1929(unittest.TestCase):
    """Genel sürüm, eski video klasörü betiğinin kilitli çıktısını bozmadan yeniden üretir."""

    @unittest.skipUnless(os.path.exists(os.path.join(V1929, "kelimeler.json")), "1929 verisi yok")
    def test_hizala_eski_norm_bayt_ayni(self):
        with tempfile.TemporaryDirectory() as c:
            r = kos("hizala.py", "--dizin", V1929, "--cikis", c, "--norm", "eski"); self.assertEqual(r.returncode, 0, r.stderr)
            for f in ("altyazi-remotion.json", "altyazi-taslak.en.srt"):
                self.assertTrue(filecmp.cmp(os.path.join(c, f), os.path.join(V1929, f), shallow=False), f)
            yeni = json.load(open(os.path.join(c, "kelimeler-hizali.json"))); eski = json.load(open(os.path.join(V1929, "kelimeler-hizali.json")))
            self.assertEqual(yeni["words"], eski["words"])  # "kaynak" açıklaması genelleşti, kelimeler birebir

    @unittest.skipUnless(os.path.exists(os.path.join(V1929, "anlatim.wav")), "1929 wav yok (git dışı)")
    def test_yeni_norm_akustik_kapi(self):
        with tempfile.TemporaryDirectory() as c:
            self.assertEqual(kos("hizala.py", "--dizin", V1929, "--cikis", c).returncode, 0)
            r = kos("hiza-dogrula.py", "--dizin", V1929, "--hizali", os.path.join(c, "kelimeler-hizali.json"))
            self.assertEqual(r.returncode, 0, r.stdout)

    @unittest.skipUnless(os.path.exists(os.path.join(V1929, "rhubarb", "S04.wav")), "1929 rhubarb kesitleri yok (git dışı)")
    def test_rhubarb_kesit_bayt_ayni(self):
        with tempfile.TemporaryDirectory() as c:
            self.assertEqual(kos("rhubarb-hazirla.py", "--dizin", V1929, "--cikis", c, "--sahne", "S01,S04").returncode, 0)
            for f in ("S01.wav", "S01.txt", "S04.wav", "S04.txt", "anlatim.txt"):
                self.assertTrue(filecmp.cmp(os.path.join(c, f), os.path.join(V1929, "rhubarb", f), shallow=False), f)


if __name__ == "__main__":
    unittest.main(verbosity=1, warnings="ignore")
