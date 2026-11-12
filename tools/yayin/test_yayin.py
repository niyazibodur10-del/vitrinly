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
import shutil
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


class KaliciYetki(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.eski = (api.YENILEME_DOSYASI, api.istek, api.time.sleep, os.environ.pop("YOUTUBE_OAUTH_REFRESH_TOKEN", None))
        api.YENILEME_DOSYASI = os.path.join(self.tmp, "yt")
        os.environ.setdefault("YOUTUBE_OAUTH_CLIENT_ID", "cid"); os.environ.setdefault("YOUTUBE_OAUTH_CLIENT_SECRET", "sec")
        api.time.sleep = lambda *_: None

    def tearDown(self):
        api.YENILEME_DOSYASI, api.istek, api.time.sleep, env = self.eski
        if env is not None: os.environ["YOUTUBE_OAUTH_REFRESH_TOKEN"] = env
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_ilk_sefer_kaydeder_sonra_kod_sormaz(self):
        cevaplar = [
            (200, {}, b'{"device_code":"D","user_code":"X","verification_url":"u","expires_in":1800,"interval":5}'),
            (200, {}, b'{"access_token":"A1","refresh_token":"R1","scope":"s"}'),
        ]
        api.istek = lambda *a, **k: cevaplar.pop(0)
        self.assertEqual(api.yetki_al(cikti=lambda *a: None), ("A1", "s", True))
        self.assertEqual(open(api.YENILEME_DOSYASI).read(), "R1")
        self.assertEqual(os.stat(api.YENILEME_DOSYASI).st_mode & 0o777, 0o600)
        govdeler = []
        api.istek = lambda url, veri=None, *a, **k: (govdeler.append(veri), (200, {}, b'{"access_token":"A2","scope":"s"}'))[1]
        self.assertEqual(api.yetki_al(cikti=lambda *a: None), ("A2", "s", True))
        self.assertIn(b"grant_type=refresh_token", govdeler[0])  # cihaz kodu istenmedi

    def test_gecersiz_yenilemede_cihaz_akisina_doner(self):
        api.yenileme_kaydet("ESKI")
        cevaplar = [
            (400, {}, b'{"error":"invalid_grant"}'),
            (200, {}, b'{"device_code":"D","user_code":"X","verification_url":"u","expires_in":1800,"interval":5}'),
            (200, {}, b'{"access_token":"A3","refresh_token":"R3","scope":"s"}'),
        ]
        api.istek = lambda *a, **k: cevaplar.pop(0)
        self.assertEqual(api.yetki_al(cikti=lambda *a: None)[0], "A3")
        self.assertEqual(open(api.YENILEME_DOSYASI).read(), "R3")

    def test_ortam_dusukse_dosyadaki_gecerli_token(self):
        # 2026-11-04: ortam değişkenindeki token invalid_grant; dosyadaki geçerli → cihaz akışı (kod) istenmemeli
        api.yenileme_kaydet("IYI"); os.environ["YOUTUBE_OAUTH_REFRESH_TOKEN"] = "DUSUK"
        try:
            denenen = []
            def sahte(url, veri=None, *a, **k):
                denenen.append(veri)
                if b"refresh_token=DUSUK" in veri: return 400, {}, b'{"error":"invalid_grant"}'
                if b"refresh_token=IYI" in veri: return 200, {}, b'{"access_token":"A4","scope":"s"}'
                raise AssertionError("cihaz akışına düşmemeli")
            api.istek = sahte
            self.assertEqual(api.yetki_al(cikti=lambda *a: None), ("A4", "s", True))
            self.assertEqual(len(denenen), 2)
            self.assertEqual([k for _, k in api.yenileme_kaynaklari()], ["ortam değişkeni", api.YENILEME_DOSYASI])
            os.environ["YOUTUBE_OAUTH_REFRESH_TOKEN"] = "IYI"   # aynı token iki kez denenmez
            self.assertEqual(len(api.yenileme_kaynaklari()), 1)
        finally:
            os.environ.pop("YOUTUBE_OAUTH_REFRESH_TOKEN", None)


# ---------- planlı yayın bekçisi (yayin-kontrol.py) ----------
import importlib.util as _iu  # noqa: E402
_sp = _iu.spec_from_file_location("yayin_kontrol", os.path.join(os.path.dirname(os.path.abspath(__file__)), "yayin-kontrol.py"))
yk = _iu.module_from_spec(_sp); _sp.loader.exec_module(yk)


def _v(ps, pa=None, pub=None):
    return {"status": {"privacyStatus": ps, **({"publishAt": pa} if pa else {})}, "snippet": {"publishedAt": pub or "2026-11-03T09:50:00Z"}}


class Bekci(unittest.TestCase):
    PLAN = yk.zaman("2026-11-04T17:00:00Z")

    def d(self, v, simdi):
        return yk.degerlendir(v, self.PLAN, yk.zaman(simdi))

    def test_gercek_vaka_s08_erken(self):   # 2026-11-03 gerçek veri: 29 sa erken public
        self.assertEqual(self.d(_v("public", pub="2026-11-03T12:00:11Z"), "2026-11-03T13:00:00Z")[0], "KALDI")
        r, m = self.d(_v("public", pub="2026-11-03T12:00:11Z"), "2026-11-09T07:00:00Z")
        self.assertEqual(r, "KALDI"); self.assertIn("28 sa 59 dk erken", m)

    def test_planli_dogru(self):
        self.assertEqual(self.d(_v("private", "2026-11-04T17:00:00Z"), "2026-11-04T15:00:00Z")[0], "TAMAM")

    def test_plan_silinmis_ve_degismis(self):
        self.assertIn("SİLİNMİŞ", self.d(_v("private"), "2026-11-04T15:00:00Z")[1])
        self.assertIn("DEĞİŞMİŞ", self.d(_v("private", "2026-11-03T12:00:00Z"), "2026-11-03T10:00:00Z")[1])

    def test_unlisted(self):
        self.assertEqual(self.d(_v("unlisted"), "2026-11-04T15:00:00Z")[0], "KALDI")

    def test_acilis_sonrasi(self):
        self.assertEqual(self.d(_v("public", pub="2026-11-04T17:00:28Z"), "2026-11-04T17:15:00Z")[0], "TAMAM")
        self.assertEqual(self.d(_v("private", "2026-11-04T17:00:00Z"), "2026-11-04T17:05:00Z")[0], "BEKLIYOR")
        self.assertIn("AÇILMADI", self.d(_v("private", "2026-11-04T17:00:00Z"), "2026-11-04T17:16:00Z")[1])
        self.assertIn("GEÇ", self.d(_v("public", pub="2026-11-04T18:00:00Z"), "2026-11-04T19:00:00Z")[1])
        self.assertEqual(self.d(None, "2026-11-04T15:00:00Z")[0], "KALDI")

    def test_sonuc_dosyasi_okuma(self):
        with tempfile.NamedTemporaryFile("w", suffix=".txt", delete=False) as f:
            f.write("2026-11-03T09:50:26Z video_id=A durum=private publishAt=2026-11-04T17:00:00Z\n"
                    "2026-11-03T09:50:27Z LISTE_BEKLIYOR liste=PL video_id=A\n"
                    "2026-10-26T17:50:19Z video_id=B durum=private publishAt=None\n"
                    "2026-10-26T17:50:19Z video_id=C durum=private publishAt=2026-11-05T14:00:00Z\n"
                    "2026-10-26T17:57:32Z video_id=C SILINDI\n"
                    "2026-11-09T07:00:00Z video_id=D durum=private publishAt=None plan=2026-11-04T17:00:00Z\n")
        try:
            p = yk.planlari_oku([f.name])
        finally:
            os.unlink(f.name)
        self.assertEqual(list(p), ["A", "D"]); self.assertEqual(p["A"]["plan"], self.PLAN)
        self.assertEqual(p["D"]["plan"], self.PLAN)   # publishAt düşmüş olsa da niyet (plan=) okunur

    def test_kontrol_cikis_ve_anahtar_kipi(self):
        pl = {"A": {"plan": self.PLAN}, "B": {"plan": self.PLAN}}
        cik = []
        r = yk.kontrol(pl, yk.zaman("2026-11-04T10:00:00Z"), cik.append,
                       oku=lambda ids, c: ("oauth", {"A": _v("private", "2026-11-04T17:00:00Z"), "B": _v("public", pub="2026-11-04T09:00:00Z")}))
        self.assertEqual(r, 1); self.assertTrue(any("ERKEN PUBLIC" in x and "8 sa 0 dk" in x for x in cik))
        r = yk.kontrol({"A": {"plan": self.PLAN}}, yk.zaman("2026-11-04T10:00:00Z"), cik.append, oku=lambda ids, c: ("anahtar", {}))
        self.assertEqual(r, 0)   # anahtar kipi: açılış öncesi görünmemek beklenen

    def test_liste_ekle_yalniz_public(self):
        eski = (api.istek, api.sessiz_yetki, yk.glob.glob)
        cagri = []
        def sahte(durum, listede):
            def f(url, veri=None, *a, **k):
                cagri.append((url.split("?")[0].rsplit("/", 1)[1], veri is not None))
                if "/videos?" in url: return 200, {}, json.dumps({"items": [{"status": {"privacyStatus": durum}}]}).encode()
                if veri is None: return 200, {}, json.dumps({"items": [{"id": "x"}] if listede else []}).encode()
                return 200, {}, b'{"id":"PI"}'
            return f
        api.sessiz_yetki = lambda *a: "T"; yk.glob.glob = lambda *a, **k: []
        try:
            api.istek = sahte("private", False); self.assertEqual(yk.liste_ekle("PL", "V", lambda *a: None), 3)
            self.assertFalse(any(post for _, post in cagri))   # private iken hiçbir yazma çağrısı yok
            cagri.clear(); api.istek = sahte("public", True); self.assertEqual(yk.liste_ekle("PL", "V", lambda *a: None), 0)
            self.assertFalse(any(post for _, post in cagri))   # zaten listede → tekrar eklemez
            cagri.clear(); api.istek = sahte("public", False); self.assertEqual(yk.liste_ekle("PL", "V", lambda *a: None), 0)
            self.assertEqual(cagri[-1], ("playlistItems", True))
        finally:
            api.istek, api.sessiz_yetki, yk.glob.glob = eski

    def test_sessiz_yetki_cihaz_akisi_baslatmaz(self):
        eski = (api.istek, api.yenileme_kaynaklari)
        api.yenileme_kaynaklari = lambda: [("R", "dosya")]
        api.istek = lambda url, *a, **k: (400, {}, b'{"error":"invalid_grant"}') if url == api.TOKEN_URL else (_ for _ in ()).throw(AssertionError(url))
        os.environ.setdefault("YOUTUBE_OAUTH_CLIENT_ID", "cid"); os.environ.setdefault("YOUTUBE_OAUTH_CLIENT_SECRET", "sec")
        try:
            with self.assertRaises(api.ApiHatasi): api.sessiz_yetki(lambda *a: None)
        finally:
            api.istek, api.yenileme_kaynaklari = eski


# ---------- analitik.py (yt-analytics.readonly; ağsız) ----------
import analitik as an  # noqa: E402


class Analitik(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.mkdtemp()
        self.eski = (an.TOKEN_DOSYASI, an.PKCE_DOSYASI, api.istek, {k: os.environ.get(k) for k in
                     ("YOUTUBE_ANALYTICS_CLIENT_ID", "YOUTUBE_ANALYTICS_CLIENT_SECRET", "YOUTUBE_ANALYTICS_REFRESH_TOKEN")})
        an.TOKEN_DOSYASI, an.PKCE_DOSYASI = os.path.join(self.tmp, "t"), os.path.join(self.tmp, "p.json")
        os.environ.update(YOUTUBE_ANALYTICS_CLIENT_ID="acid", YOUTUBE_ANALYTICS_CLIENT_SECRET="asec")
        os.environ.pop("YOUTUBE_ANALYTICS_REFRESH_TOKEN", None)

    def tearDown(self):
        an.TOKEN_DOSYASI, an.PKCE_DOSYASI, api.istek, env = self.eski
        for k, v in env.items():
            if v is None: os.environ.pop(k, None)
            else: os.environ[k] = v
        shutil.rmtree(self.tmp, ignore_errors=True)

    def test_url_kod_degisimi_ve_kayit(self):
        url = an.yetki_url(cikti=lambda *a: None)
        q = {k: v[0] for k, v in __import__("urllib.parse").parse.parse_qs(url.split("?", 1)[1]).items()}
        self.assertIn("yt-analytics.readonly", q["scope"]); self.assertEqual(q["code_challenge_method"], "S256")
        self.assertEqual((q["access_type"], q["prompt"], q["redirect_uri"]), ("offline", "consent", "http://127.0.0.1:8765"))
        self.assertEqual(os.stat(an.PKCE_DOSYASI).st_mode & 0o777, 0o600)
        with self.assertRaises(api.ApiHatasi):   # yanlış state reddedilir
            an.yetki_kod("http://127.0.0.1:8765/?state=BASKA&code=C", cikti=lambda *a: None)
        giden = []
        api.istek = lambda url, veri=None, *a, **k: (giden.append(veri), (200, {}, json.dumps(
            {"access_token": "A", "refresh_token": "R9", "scope": an.KAPSAM}).encode()))[1]
        self.assertEqual(an.yetki_kod(f"http://127.0.0.1:8765/?state={q['state']}&code=C1&scope=x", cikti=lambda *a: None), 0)
        self.assertIn(b"code_verifier=", giden[0]); self.assertIn(b"code=C1", giden[0])
        self.assertEqual(open(an.TOKEN_DOSYASI).read(), "R9"); self.assertFalse(os.path.exists(an.PKCE_DOSYASI))
        self.assertEqual(os.stat(an.TOKEN_DOSYASI).st_mode & 0o777, 0o600)

    def test_kapsam_eksikse_kaydetmez(self):
        url = an.yetki_url(cikti=lambda *a: None); st = url.split("state=")[1].split("&")[0]
        api.istek = lambda *a, **k: (200, {}, b'{"access_token":"A","refresh_token":"R","scope":"https://www.googleapis.com/auth/youtube.readonly"}')
        with self.assertRaises(api.ApiHatasi): an.yetki_kod(f"http://127.0.0.1:8765/?state={st}&code=C", cikti=lambda *a: None)
        self.assertFalse(os.path.exists(an.TOKEN_DOSYASI))

    def test_sorgu_ve_erisim_isi(self):
        def sahte(url, veri=None, *a, **k):
            if url == api.TOKEN_URL: return 200, {}, json.dumps({"access_token": "A", "scope": an.KAPSAM}).encode()
            if url.startswith(an.ANALYTICS):
                self.assertIn("filters=video%3D%3DV1%2CV2", url)
                return 200, {}, json.dumps({"columnHeaders": [{"name": "video"}, {"name": "averageViewDuration"}],
                                            "rows": [["V1", 95], ["V2", 40]]}).encode()
            if url.endswith("/jobs") and veri is None: return 200, {}, b'{"jobs":[]}'
            if url.endswith("/jobs"): return 200, {}, b'{"id":"J1"}'
            raise AssertionError(url)
        api.istek = sahte; os.environ["YOUTUBE_ANALYTICS_REFRESH_TOKEN"] = "R"
        tok = an.erisim_tokeni(lambda *a: None)
        r = an.sorgu(tok, "2026-10-01", "2026-11-09", "averageViewDuration", "video", "video==V1,V2")
        self.assertEqual(r, [{"video": "V1", "averageViewDuration": 95}, {"video": "V2", "averageViewDuration": 40}])
        self.assertEqual(an.erisim_isi(tok, cikti=lambda *a: None), "J1")

    def test_yukleme_tokeni_analitik_sayilmaz(self):   # youtube kapsamlı token analitik yerine geçmez
        api.istek = lambda *a, **k: (200, {}, b'{"access_token":"A","scope":"https://www.googleapis.com/auth/youtube"}')
        os.environ["YOUTUBE_ANALYTICS_REFRESH_TOKEN"] = "R"
        with self.assertRaises(api.ApiHatasi): an.erisim_tokeni(lambda *a: None)


if __name__ == "__main__":
    unittest.main(verbosity=2)
