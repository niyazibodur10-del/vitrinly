#!/usr/bin/env python3
# Yayın aracı testleri (ağsız): şema/sınır doğrulaması + resumable yükleme protokolü (yerel sahte sunucu,
# 308 Resume Incomplete, 503 sonrası durum sorgusu ve kaldığı yerden devam) + cihaz akışı yoklama mantığı.
# Kullanım: python3 tools/yayin/test_yayin.py
import copy
import datetime as dt
import http.server
import json
import os
import struct
import sys
import tempfile
import threading
import unittest
import zlib

os.environ["no_proxy"] = os.environ["NO_PROXY"] = "127.0.0.1,localhost"
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import yayin_api as api  # noqa: E402
import yayin_paket as pk  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
ORNEK = os.path.join(ROOT, "uretim/ses-testi/yayin-paketi.json")
SIMDI = dt.datetime(2026, 10, 26, 12, 0, tzinfo=dt.timezone.utc)


def png(yol, w, h, dolgu=0):
    sat = b"".join(b"\x00" + bytes(w * 3) for _ in range(h))
    def ch(t, d): return struct.pack(">I", len(d)) + t + d + struct.pack(">I", zlib.crc32(t + d))
    with open(yol, "wb") as f:
        f.write(b"\x89PNG\r\n\x1a\n" + ch(b"IHDR", struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0))
                + ch(b"IDAT", zlib.compress(sat)) + (ch(b"tEXt", b"x\x00" + os.urandom(dolgu)) if dolgu else b"")
                + ch(b"IEND", b""))


class Dogrulama(unittest.TestCase):
    def setUp(self):
        self.p = pk.yukle_paket(ORNEK)

    def hatalar(self, p=None):
        return pk.dogrula(p or self.p, simdi=SIMDI).hatalar

    def bul(self, parca, p=None):
        h = self.hatalar(p)
        self.assertTrue(any(parca in x for x in h), f"'{parca}' beklenirdi, hatalar: {h}")

    def test_ornek_paket_gecer(self):
        self.assertEqual(self.hatalar(), [])

    def test_baslik_100(self):
        self.p["metadata"]["baslik"] = "x" * 101; self.bul("başlık 101")

    def test_baslik_acili_parantez(self):
        self.p["metadata"]["baslik"] = "a <b>"; self.bul("< veya >")

    def test_aciklama_5000_bayt(self):
        self.p["metadata"]["aciklama"] = "ş" * 2501  # 5002 bayt, 2501 karakter
        self.bul("açıklama 5002 bayt")

    def test_etiket_sayimi_resmi_ornek(self):
        self.assertEqual(pk.etiket_uzunlugu(["Foo-Baz"]), 7)
        self.assertEqual(pk.etiket_uzunlugu(["Foo Baz"]), 9)
        self.assertEqual(pk.etiket_uzunlugu(["a", "b c"]), 1 + 1 + 5)

    def test_etiket_500(self):
        self.p["metadata"]["etiketler"] = ["abcdefghi"] * 50  # 450 + 49 virgül = 499
        self.assertEqual(self.hatalar(), [])
        self.p["metadata"]["etiketler"].append("ab"); self.bul("etiketler toplam 502")

    def test_publishat_gecmis(self):
        self.p["durum"]["yayin_zamani"] = "2026-10-25T10:00:00+03:00"; self.bul("geçmişte")

    def test_publishat_saat_dilimi_yok(self):
        self.p["durum"]["yayin_zamani"] = "2026-11-02T18:00:00"; self.bul("ISO 8601 değil")

    def test_publishat_iso_degil(self):
        self.p["durum"]["yayin_zamani"] = "2 Kasım 18:00"; self.bul("ISO 8601 değil")

    def test_publishat_public_ile(self):
        self.p["durum"]["gizlilik"] = "public"; self.bul("yalnız gizlilik=private")

    def test_publishat_utc_cevrimi(self):
        self.assertEqual(pk.api_govdesi(self.p)["status"]["publishAt"], "2026-11-02T15:00:00Z")

    def test_api_govdesi_alanlar(self):
        g = pk.api_govdesi(self.p)
        self.assertEqual(g["snippet"]["categoryId"], "27")
        self.assertEqual((g["snippet"]["defaultLanguage"], g["snippet"]["defaultAudioLanguage"]), ("en", "en"))
        self.assertIs(g["status"]["selfDeclaredMadeForKids"], False)
        self.assertIs(g["status"]["containsSyntheticMedia"], True)
        self.assertEqual(g["status"]["privacyStatus"], "private")

    def test_varsayilanlar(self):
        p = copy.deepcopy(self.p)
        del p["metadata"]["kategori_id"]; del p["durum"]["sentetik_medya"]; del p["durum"]["cocuklara_ozel"]
        self.assertEqual(self.hatalar(p), [])
        g = pk.api_govdesi(p)
        self.assertEqual(g["snippet"]["categoryId"], "27"); self.assertIs(g["status"]["containsSyntheticMedia"], True)
        self.assertIs(g["status"]["selfDeclaredMadeForKids"], False)

    def test_sema_zorunlu_ve_tip(self):
        del self.p["metadata"]["baslik"]; self.bul("'metadata.baslik' zorunlu")
        p = pk.yukle_paket(ORNEK); p["metadata"]["etiketler"] = "a,b"; self.bul("tipi list", p)

    def test_video_yok(self):
        self.p["dosyalar"]["video"] = "yok.mp4"; self.bul("video yok")

    def test_thumbnail_boyut_ve_2mb(self):
        with tempfile.TemporaryDirectory() as d:
            png(os.path.join(d, "k.png"), 640, 360)
            self.p["dosyalar"]["thumbnail"] = os.path.join(d, "k.png"); self.bul("640x360 ≠ 1280x720")
            png(os.path.join(d, "b.png"), 1280, 720, dolgu=2_200_000)
            p = pk.yukle_paket(ORNEK); p["dosyalar"]["thumbnail"] = os.path.join(d, "b.png"); self.bul("> 2048 KB", p)
            png(os.path.join(d, "i.png"), 1280, 720)
            p = pk.yukle_paket(ORNEK); p["dosyalar"]["thumbnail"] = os.path.join(d, "i.png")
            self.assertEqual(self.hatalar(p), [])

    def test_shorts_yatay_ve_etiket(self):
        self.p["tur"] = "shorts"
        h = self.hatalar()
        self.assertTrue(any("dikey" in x for x in h) and any("#Shorts" in x for x in h), h)

    def test_bolumler(self):
        self.p["metadata"]["bolumler"] = [{"zaman": "00:05", "baslik": "a"}]; self.bul("00:00")
        p = pk.yukle_paket(ORNEK); p["metadata"]["bolumler"] = [{"zaman": "0:00", "baslik": "a"}, {"zaman": "0:05", "baslik": "b"}, {"zaman": "0:15", "baslik": "c"}]
        self.bul("≥10 sn", p)
        p = pk.yukle_paket(ORNEK); p["metadata"]["bolumler"] = [{"zaman": "0:00", "baslik": "a"}, {"zaman": "0:10", "baslik": "b"}]
        self.bul("en az 3", p)

    def test_bolum_aciklamaya_eklenir(self):
        self.p["metadata"]["bolumler"] = [{"zaman": "00:00", "baslik": "Intro"}, {"zaman": "01:00", "baslik": "B"}]
        a = pk.tam_aciklama(self.p)
        self.assertIn("Chapters:\n00:00 Intro\n01:00 B", a); self.assertNotIn("{BOLUMLER}", a)

    def test_srt_bozuk(self):
        with tempfile.TemporaryDirectory() as d:
            s = os.path.join(d, "x.srt")
            with open(s, "w") as f: f.write("1\n00:00:05,000 --> 00:00:04,000\nmerhaba\n\n2\n00:00:01,000 --> 00:00:02,000\nb\n")
            self.p["dosyalar"]["altyazilar"] = [{"dosya": s, "dil": "en"}]
            h = self.hatalar()
            self.assertTrue(any("bitiş ≤ başlangıç" in x for x in h) and any("geriye" in x for x in h), h)

    def test_manuel_paket(self):
        with tempfile.TemporaryDirectory() as d:
            self.assertEqual(self.hatalar(), [])
            yol = pk.manuel_paket(self.p, d)
            self.assertEqual(sorted(os.listdir(d)), ["YAYIN.md", "altyazi-en.srt", "thumbnail.jpg", "video.mp4"])
            with open(yol, encoding="utf-8") as f: t = f.read()
            for s in (self.p["metadata"]["baslik"], "not financial advice", "hyperinflation, Weimar Germany", "18:00 (Türkiye"):
                self.assertIn(s, t)


# ---------- resumable yükleme: yerel sahte sunucu ----------
class Sahte(http.server.BaseHTTPRequestHandler):
    alinan, boy, hata_ver, kayit = bytearray(), 0, 1, []

    def log_message(self, *a): pass

    def _yanit(self, kod, govde=b"", basliklar=()):
        self.send_response(kod)
        for k, v in basliklar: self.send_header(k, v)
        self.send_header("Content-Length", str(len(govde))); self.end_headers(); self.wfile.write(govde)

    def do_POST(self):
        n = int(self.headers.get("Content-Length", 0)); j = json.loads(self.rfile.read(n))
        assert self.headers["Authorization"] == "Bearer T" and self.headers["X-Upload-Content-Length"] == str(Sahte.boy)
        Sahte.kayit.append(("POST", j["status"]["privacyStatus"]))
        self._yanit(200, b"", [("Location", f"http://127.0.0.1:{self.server.server_port}/oturum")])

    def do_PUT(self):
        n = int(self.headers.get("Content-Length", 0)); veri = self.rfile.read(n)
        cr = self.headers["Content-Range"]; Sahte.kayit.append(("PUT", cr))
        if cr.startswith("bytes */"):
            return self._yanit(308, b"", [("Range", f"bytes=0-{len(Sahte.alinan)-1}")] if Sahte.alinan else [])
        bas = int(cr.split()[1].split("-")[0])
        assert bas == len(Sahte.alinan), (bas, len(Sahte.alinan))
        if len(Sahte.alinan) > 0 and Sahte.hata_ver:  # ikinci parçada bir kez 503
            Sahte.hata_ver -= 1; return self._yanit(503, b"{}")
        Sahte.alinan += veri[: max(1, len(veri) // 2)] if len(Sahte.alinan) == 0 else veri  # ilk parçanın yarısını kabul et
        if len(Sahte.alinan) >= Sahte.boy:
            return self._yanit(200, json.dumps({"id": "VID123", "status": {"privacyStatus": "private"}}).encode())
        self._yanit(308, b"", [("Range", f"bytes=0-{len(Sahte.alinan)-1}")])


class Yukleme(unittest.TestCase):
    def test_resumable_308_ve_503_devam(self):
        sv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Sahte)
        threading.Thread(target=sv.serve_forever, daemon=True).start()
        eski_upload, eski_parca, eski_uyku = api.UPLOAD, api.PARCA, api.time.sleep
        api.UPLOAD, api.PARCA = f"http://127.0.0.1:{sv.server_port}", 256 * 1024
        api.time.sleep = lambda s: None
        try:
            with tempfile.NamedTemporaryFile(delete=False) as f:
                veri = os.urandom(700_000); f.write(veri)
            Sahte.boy = len(veri)
            v = api.video_yukle("T", f.name, {"snippet": {}, "status": {"privacyStatus": "private"}}, cikti=lambda *a: None)
            self.assertEqual(v["id"], "VID123")
            self.assertEqual(bytes(Sahte.alinan), veri)  # kısmi kabul + 503 sonrası bayt kaybı/tekrarı yok
            self.assertIn(("PUT", f"bytes */{len(veri)}"), Sahte.kayit)  # 503 sonrası durum sorgusu yapıldı
        finally:
            api.UPLOAD, api.PARCA, api.time.sleep = eski_upload, eski_parca, eski_uyku
            sv.shutdown(); sv.server_close(); os.unlink(f.name)


class CihazAkisi(unittest.TestCase):
    def test_yoklama(self):
        cevaplar = [
            (200, {}, json.dumps({"device_code": "D", "user_code": "ABCD-EFGH", "verification_url": "https://www.google.com/device",
                                  "expires_in": 1800, "interval": 5}).encode()),
            (428, {}, b'{"error":"authorization_pending"}'),
            (403, {}, b'{"error":"slow_down"}'),
            (200, {}, b'{"access_token":"ERISIM","scope":"https://www.googleapis.com/auth/youtube","expires_in":3599}'),
        ]
        bekleme, eski_istek, eski_uyku = [], api.istek, api.time.sleep
        api.istek = lambda *a, **k: cevaplar.pop(0)
        api.time.sleep = bekleme.append
        try:
            tok, kapsam = api.cihaz_akisi("cid", "sec", cikti=lambda *a: None)
        finally:
            api.istek, api.time.sleep = eski_istek, eski_uyku
        self.assertEqual((tok, kapsam), ("ERISIM", api.KAPSAM_CIHAZ))
        self.assertEqual(bekleme, [5, 5, 10])  # slow_down sonrası aralık +5 sn

    def test_kimlik_yoksa_hata(self):
        eski = {k: os.environ.pop(k, None) for k in ("YOUTUBE_OAUTH_CLIENT_ID", "YOUTUBE_OAUTH_CLIENT_SECRET")}
        try:
            with self.assertRaises(api.ApiHatasi): api.kimlik_bilgisi()
        finally:
            for k, v in eski.items():
                if v is not None: os.environ[k] = v


if __name__ == "__main__":
    unittest.main(verbosity=2)
