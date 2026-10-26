# Google OAuth (cihaz akışı / yerel loopback) + YouTube Data API v3 çağrıları. Yalnız stdlib (urllib; HTTPS_PROXY'ye uyar).
# GÜVENLİK: istemci kimliği/sırrı yalnız ortam değişkeninden okunur; erişim tokenı yalnız bellekte tutulur,
# diske/loga yazılmaz ve iş bitince oauth2.googleapis.com/revoke ile iptal edilir. Yenileme tokenı kullanılmaz.
#
# Kapsam doğrulaması (developers.google.com/identity/protocols/oauth2/limited-input-device, "Allowed scopes",
# sayfa güncelleme 2026-10-16, 2026-10-26 okundu): cihaz akışı YouTube için YALNIZ
#   https://www.googleapis.com/auth/youtube ve .../youtube.readonly kapsamlarına izin verir.
#   videos.insert, thumbnails.set, playlistItems.insert → "youtube" kapsamını kabul eder (cihaz akışında çalışır).
#   captions.insert → yalnız youtube.force-ssl / youtubepartner (cihaz akışında YOK).
# Bu yüzden: --akis cihaz (varsayılan) altyazıyı yüklemez (manuel paket / Studio); --akis yerel (Niyazi'nin
# bilgisayarında, "Masaüstü uygulaması" türü istemciyle, PKCE + 127.0.0.1 loopback) youtube.force-ssl alır ve altyazıyı da yükler.
import base64
import hashlib
import http.server
import json
import os
import secrets
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
import webbrowser

CIHAZ_URL = "https://oauth2.googleapis.com/device/code"
TOKEN_URL = "https://oauth2.googleapis.com/token"
IPTAL_URL = "https://oauth2.googleapis.com/revoke"
YETKI_URL = "https://accounts.google.com/o/oauth2/v2/auth"
UPLOAD = "https://www.googleapis.com/upload/youtube/v3"
API = "https://www.googleapis.com/youtube/v3"
KAPSAM_CIHAZ = "https://www.googleapis.com/auth/youtube"
KAPSAM_YEREL = "https://www.googleapis.com/auth/youtube.force-ssl"
PARCA = 8 * 1024 * 1024  # 256 KB'nin katı olmalı (resumable protokolü)


class ApiHatasi(Exception):
    pass


class _YonlendirmeYok(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *a, **k):  # 308 Resume Incomplete yönlendirme değildir
        return None


_ACICI = urllib.request.build_opener(_YonlendirmeYok)


def istek(url, veri=None, basliklar=None, yontem=None, zaman_asimi=120):
    """(durum, başlıklar, gövde-bayt). HTTP hata kodları istisna değil, dönüş değeridir."""
    rq = urllib.request.Request(url, data=veri, headers=basliklar or {}, method=yontem)
    try:
        with _ACICI.open(rq, timeout=zaman_asimi) as r:
            return r.status, dict(r.headers), r.read()
    except urllib.error.HTTPError as e:
        return e.code, dict(e.headers or {}), e.read() or b""


def _form(d):
    return urllib.parse.urlencode(d).encode()


def _json(b):
    try: return json.loads(b.decode("utf-8") or "{}")
    except ValueError: return {"ham": b[:300].decode("utf-8", "replace")}


def kimlik_bilgisi():
    cid, sec = os.environ.get("YOUTUBE_OAUTH_CLIENT_ID"), os.environ.get("YOUTUBE_OAUTH_CLIENT_SECRET")
    if not cid or not sec:
        raise ApiHatasi("YOUTUBE_OAUTH_CLIENT_ID / YOUTUBE_OAUTH_CLIENT_SECRET ortam değişkenleri yok (bkz. docs/yayin-kurulumu.md)")
    return cid, sec


# ---------- yetkilendirme ----------
def cihaz_akisi(cid, sec, kapsam=KAPSAM_CIHAZ, cikti=print):
    s, _, b = istek(CIHAZ_URL, _form({"client_id": cid, "scope": kapsam}))
    j = _json(b)
    if s != 200:
        raise ApiHatasi(f"device/code {s}: {j.get('error')} {j.get('error_description', '')}")
    cikti("\n" + "=" * 60)
    cikti(f"  Telefondan aç: {j['verification_url']}")
    cikti(f"  Kodu gir:      {j['user_code']}")
    cikti(f"  (kod {int(j['expires_in'])//60} dk geçerli; Google hesabı = kanal sahibi hesabı)")
    cikti("=" * 60 + "\n")
    aralik, bitis = int(j.get("interval", 5)), time.time() + int(j["expires_in"])
    while time.time() < bitis:
        time.sleep(aralik)
        s, _, b = istek(TOKEN_URL, _form({"client_id": cid, "client_secret": sec, "device_code": j["device_code"],
                                           "grant_type": "urn:ietf:params:oauth:grant-type:device_code"}))
        t = _json(b)
        if s == 200 and "access_token" in t:
            return t["access_token"], t.get("scope", kapsam)
        hata = t.get("error")
        if hata == "authorization_pending": continue
        if hata == "slow_down": aralik += 5; continue
        if hata == "access_denied": raise ApiHatasi("kullanıcı izni reddetti")
        raise ApiHatasi(f"token {s}: {hata} {t.get('error_description', '')}")
    raise ApiHatasi("cihaz kodunun süresi doldu; yeniden çalıştırın")


def yerel_akis(cid, sec, kapsam=KAPSAM_YEREL, cikti=print):
    """Masaüstü istemcisi + PKCE + 127.0.0.1 loopback. Yalnız tarayıcısı olan bilgisayarda çalışır."""
    dogrulayici = base64.urlsafe_b64encode(secrets.token_bytes(48)).rstrip(b"=").decode()
    meydan = base64.urlsafe_b64encode(hashlib.sha256(dogrulayici.encode()).digest()).rstrip(b"=").decode()
    durum, sonuc = secrets.token_urlsafe(24), {}

    class H(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            q = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            if q.get("state", [""])[0] == durum:
                sonuc.update({k: v[0] for k, v in q.items()})
            self.send_response(200); self.send_header("Content-Type", "text/plain; charset=utf-8"); self.end_headers()
            self.wfile.write("Tamam, bu sekmeyi kapatabilirsiniz.".encode())

        def log_message(self, *a): pass

    sv = http.server.HTTPServer(("127.0.0.1", 0), H)
    yonlendir = f"http://127.0.0.1:{sv.server_port}"
    url = YETKI_URL + "?" + urllib.parse.urlencode({
        "client_id": cid, "redirect_uri": yonlendir, "response_type": "code", "scope": kapsam,
        "code_challenge": meydan, "code_challenge_method": "S256", "state": durum})
    cikti(f"\nTarayıcıda izin verin (açılmazsa bu adresi açın):\n{url}\n")
    webbrowser.open(url)
    th = threading.Thread(target=sv.handle_request, daemon=True); th.start(); th.join(300); sv.server_close()
    if "code" not in sonuc:
        raise ApiHatasi(f"yetki alınamadı: {sonuc.get('error', 'zaman aşımı/state uyuşmadı')}")
    s, _, b = istek(TOKEN_URL, _form({"client_id": cid, "client_secret": sec, "code": sonuc["code"],
                                       "code_verifier": dogrulayici, "grant_type": "authorization_code",
                                       "redirect_uri": yonlendir}))
    t = _json(b)
    if s != 200:
        raise ApiHatasi(f"token {s}: {t.get('error')} {t.get('error_description', '')}")
    return t["access_token"], t.get("scope", kapsam)


def iptal(token):
    s, _, _ = istek(IPTAL_URL, _form({"token": token}), {"Content-Type": "application/x-www-form-urlencoded"})
    return s


# ---------- YouTube çağrıları ----------
def _yetki(token, ek=None):
    h = {"Authorization": f"Bearer {token}"}
    h.update(ek or {})
    return h


def _kontrol(ad, s, b, beklenen=(200, 201)):
    if s not in beklenen:
        j = _json(b).get("error", {})
        neden = ",".join(e.get("reason", "") for e in j.get("errors", [])) if isinstance(j, dict) else ""
        raise ApiHatasi(f"{ad} HTTP {s} {neden}: {j.get('message', '') if isinstance(j, dict) else j}")
    return _json(b)


def video_yukle(token, yol, govde, cikti=print, deneme_max=8):
    """videos.insert, resumable protokol (Step 1 oturum, Step 2 parça PUT, 308 → Range ile devam, 5xx → üstel bekleme)."""
    boy = os.path.getsize(yol)
    s, h, b = istek(f"{UPLOAD}/videos?uploadType=resumable&part=snippet,status", json.dumps(govde).encode(),
                    _yetki(token, {"Content-Type": "application/json; charset=UTF-8",
                                   "X-Upload-Content-Length": str(boy), "X-Upload-Content-Type": "video/*"}))
    _kontrol("videos.insert (oturum)", s, b, (200,))
    oturum = h.get("Location") or h.get("location")
    if not oturum:
        raise ApiHatasi("resumable oturum adresi (Location) dönmedi")
    gonderilen, deneme, t0 = 0, 0, time.time()
    with open(yol, "rb") as f:
        while True:
            f.seek(gonderilen)
            parca = f.read(PARCA)
            son = gonderilen + len(parca) - 1
            try:
                s, h, b = istek(oturum, parca, _yetki(token, {"Content-Type": "application/octet-stream",
                                "Content-Range": f"bytes {gonderilen}-{son}/{boy}"}), "PUT", 600)
            except OSError as e:  # bağlantı koptu → durum sorgusu ile devam
                s, h, b = 0, {}, str(e).encode()
            if s in (200, 201):
                cikti(f"  yükleme %100 ({boy/1e6:.1f} MB, {time.time()-t0:.0f} sn)")
                return _json(b)
            if s == 308:
                r = h.get("Range") or h.get("range")
                gonderilen = int(r.split("-")[1]) + 1 if r else 0
                deneme = 0
                cikti(f"  yükleme %{100*gonderilen/boy:.0f}")
                continue
            if s == 0 or s >= 500:
                deneme += 1
                if deneme > deneme_max: raise ApiHatasi(f"yükleme {deneme_max} denemede tamamlanamadı (son {s})")
                bek = min(2 ** deneme, 64) + secrets.randbelow(1000) / 1000
                cikti(f"  geçici hata {s}; {bek:.1f} sn sonra durum sorgulanıyor")
                time.sleep(bek)
                s, h, b = istek(oturum, b"", _yetki(token, {"Content-Length": "0", "Content-Range": f"bytes */{boy}"}), "PUT")
                if s in (200, 201): return _json(b)
                if s == 308:
                    r = h.get("Range") or h.get("range"); gonderilen = int(r.split("-")[1]) + 1 if r else 0
                continue
            _kontrol("videos.insert (parça)", s, b)


def thumbnail_yukle(token, video_id, yol):
    tur = "image/png" if yol.lower().endswith(".png") else "image/jpeg"
    with open(yol, "rb") as f: veri = f.read()
    s, _, b = istek(f"{UPLOAD}/thumbnails/set?videoId={video_id}&uploadType=media", veri,
                    _yetki(token, {"Content-Type": tur}))
    return _kontrol("thumbnails.set", s, b)


def altyazi_yukle(token, video_id, yol, dil, ad=""):
    sinir = "yayin" + secrets.token_hex(8)
    meta = json.dumps({"snippet": {"videoId": video_id, "language": dil, "name": ad[:150], "isDraft": False}})
    with open(yol, "rb") as f: srt = f.read()
    govde = (f"--{sinir}\r\nContent-Type: application/json; charset=UTF-8\r\n\r\n{meta}\r\n"
             f"--{sinir}\r\nContent-Type: application/octet-stream\r\n\r\n").encode() + srt + f"\r\n--{sinir}--\r\n".encode()
    s, _, b = istek(f"{UPLOAD}/captions?uploadType=multipart&part=snippet", govde,
                    _yetki(token, {"Content-Type": f"multipart/related; boundary={sinir}"}))
    return _kontrol("captions.insert", s, b)


def listeye_ekle(token, liste_id, video_id):
    g = {"snippet": {"playlistId": liste_id, "resourceId": {"kind": "youtube#video", "videoId": video_id}}}
    s, _, b = istek(f"{API}/playlistItems?part=snippet", json.dumps(g).encode(),
                    _yetki(token, {"Content-Type": "application/json; charset=UTF-8"}))
    return _kontrol("playlistItems.insert", s, b)


def video_durumu(token, video_id):
    s, _, b = istek(f"{API}/videos?part=status,processingDetails&id={video_id}", None, _yetki(token))
    j = _kontrol("videos.list", s, b)
    return (j.get("items") or [{}])[0]


def video_basligi(token, video_id):
    s, _, b = istek(f"{API}/videos?part=snippet&id={video_id}", None, _yetki(token))
    j = _kontrol("videos.list", s, b)
    return ((j.get("items") or [{}])[0].get("snippet") or {}).get("title")


def video_sil(token, video_id):
    """videos.delete (geri alınamaz; 204 beklenir)."""
    s, _, b = istek(f"{API}/videos?id={video_id}", None, _yetki(token), yontem="DELETE")
    _kontrol("videos.delete", s, b, beklenen=(204,))


# ---------- erişim testi (kimliksiz; yalnız HTTP durum kodu) ----------
ERISIM_HEDEFLERI = [
    ("POST", CIHAZ_URL, _form({"client_id": "erisim-testi", "scope": KAPSAM_CIHAZ}), "401 invalid_client = erişim var"),
    ("POST", TOKEN_URL, _form({"grant_type": "authorization_code"}), "400 = erişim var"),
    ("POST", f"{UPLOAD}/videos?uploadType=resumable&part=snippet", b"{}", "401 = erişim var (kimlik yok)"),
    ("GET", f"{API}/videos?part=id&id=x", None, "403 = erişim var (anahtar yok)"),
    ("GET", "https://accounts.google.com/.well-known/openid-configuration", None, "200 = erişim var"),
    ("GET", "https://www.google.com/device", None, "200/302 = erişim var"),
]


def erisim_testi(cikti=print):
    sonuc = []
    for y, url, veri, beklenti in ERISIM_HEDEFLERI:
        t0 = time.time()
        try:
            s, _, b = istek(url, veri, {"Content-Type": "application/x-www-form-urlencoded"} if veri else {}, y, 20)
            hata = _json(b).get("error")
            hata = hata.get("status") if isinstance(hata, dict) else hata
        except OSError as e:
            s, hata = 0, type(e).__name__ + ": " + str(e)[:80]
        cikti(f"  {y:4} {url[:70]:70} → {s} {hata or ''} ({(time.time()-t0)*1000:.0f} ms; {beklenti})")
        sonuc.append((url, s))
    return sonuc
