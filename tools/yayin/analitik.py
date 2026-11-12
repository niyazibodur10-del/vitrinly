#!/usr/bin/env python3
# YouTube Analytics (AVD, tutma, izlenme süresi, abone) + Reporting API (gösterim ve CTR) — salt okuma.
# Kapsam: yt-analytics.readonly + youtube.readonly. Yükleme yetkisinden AYRI kimlik (en az yetki; yükleme tokenı etkilenmez).
#
# DOĞRULANDI (2026-11-09):
#   - Cihaz akışı yt-analytics.readonly'yi REDDEDER: device/code → 400 invalid_scope "Invalid device flow scope"
#     (canlı deneme, kod yoklanmadı) + developers.google.com/identity/protocols/oauth2/limited-input-device "Allowed scopes".
#     → yukle.py --yetki-al'a bu kapsam EKLENEMEZ.
#   - Analytics API v2 metriklerinde gösterim/CTR YOK (developers.google.com/youtube/analytics/metrics): AVD
#     (averageViewDuration), averageViewPercentage, estimatedMinutesWatched, audienceWatchRatio var.
#   - Gösterim + CTR yalnız Reporting API "channel_reach_basic_a1" (video_thumbnail_impressions,
#     video_thumbnail_impressions_ctr); kapsam yt-analytics.readonly. Rapor işi açıldıktan sonra günlük üretilir.
# Yetki yolları (adaylar):
#   Y1 OAuth Playground + kendi "Web uygulaması" istemcisi — KAZANAN (kalıcılık): yenileme tokenı Niyazi'nin tarayıcısında
#      çıkar, doğrudan bulut ortamı ayarına YOUTUBE_ANALYTICS_REFRESH_TOKEN olarak yapıştırılır; sohbete/repoya hiç girmez,
#      konteyner silinince gitmez. Kendi kimliğiyle Playground 24 sa otomatik iptal UYGULAMAZ (Playground sayfası).
#   Y2 --yetki-url / --yetki-kod (aynı Web istemcisi, 127.0.0.1 geri dönüş + PKCE, elle yapıştırma) — YEDEK: koordinatör
#      adresi gösterir, Niyazi izin verir, açılmayan 127.0.0.1 sayfasının adresini geri yapıştırır. Kod tek kullanımlık,
#      dakikalar içinde düşer ve PKCE doğrulayıcısı olmadan işe yaramaz; token yalnız ~/.finansal-arac'a yazılır
#      (konteynerle gider → kalıcılık için yine Y1).
#   Y3 --akis yerel Niyazi'nin bilgisayarında — ELENDİ (repo + Python kurulumu ister).
# Gizlilik: istemci sırrı ve tokenlar yalnız ortam değişkeni / 600 izinli dosya; ekrana/loga yazılmaz.
import argparse
import base64
import datetime as dt
import hashlib
import json
import os
import secrets
import sys
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import yayin_api as api  # noqa: E402

KAPSAM = "https://www.googleapis.com/auth/yt-analytics.readonly https://www.googleapis.com/auth/youtube.readonly"
ANALYTICS = "https://youtubeanalytics.googleapis.com/v2/reports"
REPORTING = "https://youtubereporting.googleapis.com/v1"
ERISIM_RAPORU = "channel_reach_basic_a1"
ARAC = os.environ.get("ARAC_DIZINI", os.path.expanduser("~/.finansal-arac"))
TOKEN_DOSYASI = os.path.join(ARAC, "youtube-analitik-tokeni")
PKCE_DOSYASI = os.path.join(ARAC, "analitik-pkce.json")
VARSAYILAN_PORT = 8765


def kimlik():
    cid, sec = os.environ.get("YOUTUBE_ANALYTICS_CLIENT_ID"), os.environ.get("YOUTUBE_ANALYTICS_CLIENT_SECRET")
    if not cid or not sec:
        raise api.ApiHatasi("YOUTUBE_ANALYTICS_CLIENT_ID / _SECRET yok (Web uygulaması istemcisi; docs/yayin-kurulumu.md Ek C)")
    return cid, sec


def _yaz600(yol, veri):
    os.makedirs(os.path.dirname(yol), exist_ok=True)
    fd = os.open(yol, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    with os.fdopen(fd, "w") as f: f.write(veri)
    os.chmod(yol, 0o600)


def token_kaynaklari():
    k, gor = [], set()
    for t, ad in ((os.environ.get("YOUTUBE_ANALYTICS_REFRESH_TOKEN", "").strip(), "ortam değişkeni"),
                  (open(TOKEN_DOSYASI).read().strip() if os.path.isfile(TOKEN_DOSYASI) else "", TOKEN_DOSYASI)):
        if t and t not in gor: k.append((t, ad)); gor.add(t)
    return k


def erisim_tokeni(cikti=print):
    """Etkileşimsiz: geçerli ilk yenileme tokenı. Kapsamda yt-analytics yoksa hata."""
    cid, sec = kimlik()
    for yt, ad in token_kaynaklari():
        try:
            tok, kapsam = api.yenile(cid, sec, yt)
        except api.ApiHatasi as e:
            cikti(f"Analitik yetki geçersiz ({ad}): {str(e)[:90]}"); continue
        if "yt-analytics" not in kapsam:
            cikti(f"Analitik yetki ({ad}) kapsamı eksik: {kapsam}"); continue
        return tok
    raise api.ApiHatasi("geçerli analitik yetkisi yok → Ek C (Y1 Playground) veya analitik.py --yetki-url")


# ---------- Y2: elle geri dönüş (PKCE) ----------
def yetki_url(port=VARSAYILAN_PORT, cikti=print):
    cid, _ = kimlik()
    dog = base64.urlsafe_b64encode(secrets.token_bytes(48)).rstrip(b"=").decode()
    meydan = base64.urlsafe_b64encode(hashlib.sha256(dog.encode()).digest()).rstrip(b"=").decode()
    durum, yon = secrets.token_urlsafe(24), f"http://127.0.0.1:{port}"
    _yaz600(PKCE_DOSYASI, json.dumps({"dogrulayici": dog, "durum": durum, "yonlendirme": yon,
                                      "zaman": dt.datetime.now(dt.timezone.utc).isoformat()}))
    url = api.YETKI_URL + "?" + urllib.parse.urlencode({
        "client_id": cid, "redirect_uri": yon, "response_type": "code", "scope": KAPSAM, "access_type": "offline",
        "prompt": "consent", "code_challenge": meydan, "code_challenge_method": "S256", "state": durum})
    cikti(url)
    return url


def yetki_kod(adres, cikti=print):
    if not os.path.isfile(PKCE_DOSYASI):
        raise api.ApiHatasi("önce --yetki-url çalıştırılmalı (PKCE kaydı yok)")
    pk = json.load(open(PKCE_DOSYASI))
    q = urllib.parse.parse_qs(urllib.parse.urlparse(adres.strip()).query)
    if q.get("error"): raise api.ApiHatasi(f"Google: {q['error'][0]}")
    if q.get("state", [""])[0] != pk["durum"]: raise api.ApiHatasi("state uyuşmadı (eski/başka adres) → --yetki-url yeniden")
    if "code" not in q: raise api.ApiHatasi("adreste code= yok; tarayıcı adres çubuğunun TAMAMI yapıştırılmalı")
    cid, sec = kimlik()
    s, _, b = api.istek(api.TOKEN_URL, api._form({
        "client_id": cid, "client_secret": sec, "code": q["code"][0], "code_verifier": pk["dogrulayici"],
        "grant_type": "authorization_code", "redirect_uri": pk["yonlendirme"]}))
    t = api._json(b)
    if s != 200: raise api.ApiHatasi(f"token {s}: {t.get('error')} {t.get('error_description', '')}")
    if not t.get("refresh_token"): raise api.ApiHatasi("yenileme tokenı gelmedi (prompt=consent ile yeniden deneyin)")
    if "yt-analytics" not in t.get("scope", ""):
        raise api.ApiHatasi(f"izin ekranında Analytics kutusu işaretlenmemiş; gelen kapsam: {t.get('scope')}")
    _yaz600(TOKEN_DOSYASI, t["refresh_token"]); os.remove(PKCE_DOSYASI)
    cikti(f"Analitik yetkisi kaydedildi: {TOKEN_DOSYASI} (600, repo dışı). Kapsam: {t.get('scope')}")
    cikti("Kalıcılık: bu dosya konteynerle gider → Ek C Y1 ile YOUTUBE_ANALYTICS_REFRESH_TOKEN ortam ayarına.")
    return 0


# ---------- sorgular ----------
def _get(url, tok):
    s, _, b = api.istek(url, None, api._yetki(tok))
    return api._kontrol(url.split("?")[0].rsplit("/", 1)[-1], s, b)


def sorgu(tok, bas, son, metrikler, boyut=None, filtre=None):
    q = {"ids": "channel==MINE", "startDate": bas, "endDate": son, "metrics": metrikler}
    if boyut: q["dimensions"] = boyut
    if filtre: q["filters"] = filtre
    j = _get(ANALYTICS + "?" + urllib.parse.urlencode(q), tok)
    adlar = [h["name"] for h in j.get("columnHeaders", [])]
    return [dict(zip(adlar, r)) for r in j.get("rows", [])]


def erisim_isi(tok, olustur=True, cikti=print):
    """Reporting API: channel_reach_basic_a1 işi (gösterim + CTR) yoksa açar; iş kimliğini döndürür."""
    for i in _get(f"{REPORTING}/jobs", tok).get("jobs", []):
        if i.get("reportTypeId") == ERISIM_RAPORU: return i["id"]
    if not olustur: return None
    s, _, b = api.istek(f"{REPORTING}/jobs", json.dumps({"reportTypeId": ERISIM_RAPORU, "name": "toonomy-erisim"}).encode(),
                        api._yetki(tok, {"Content-Type": "application/json"}))
    j = api._kontrol("jobs.create", s, b)
    cikti(f"Erişim (CTR) rapor işi açıldı: {j['id']} — ilk günlük rapor ~24–48 sa içinde [T].")
    return j["id"]


def erisim_indir(tok, klasor, cikti=print):
    iid = erisim_isi(tok, olustur=False)
    if not iid: cikti("Rapor işi yok → önce --ctr-isi"); return 1
    os.makedirs(klasor, exist_ok=True)
    n = 0
    for r in _get(f"{REPORTING}/jobs/{iid}/reports", tok).get("reports", []):
        yol = os.path.join(klasor, f"{ERISIM_RAPORU}-{r['startTime'][:10]}-{r['id']}.csv")
        if os.path.exists(yol): continue
        s, _, b = api.istek(r["downloadUrl"], None, api._yetki(tok))
        if s != 200: cikti(f"indirme {s}: {r['id']}"); continue
        open(yol, "wb").write(b); n += 1
    cikti(f"{n} yeni rapor → {klasor}"); return 0


ERISIM_HEDEFLERI = [(ANALYTICS + "?ids=channel==MINE", "401 = erişim var"), (f"{REPORTING}/jobs", "401 = erişim var")]


def main():
    ap = argparse.ArgumentParser(description="YouTube Analytics/Reporting (salt okuma)")
    ap.add_argument("--yetki-url", action="store_true", help="Y2: izin adresini üret (koordinatör Niyazi'ye gösterir)")
    ap.add_argument("--port", type=int, default=VARSAYILAN_PORT)
    ap.add_argument("--yetki-kod", metavar="ADRES", help="Y2: Niyazi'nin yapıştırdığı 127.0.0.1 adresi")
    ap.add_argument("--yetki-iptal", action="store_true")
    ap.add_argument("--dogrula", action="store_true", help="yetkiyi test et: kanal son 28 gün özeti")
    ap.add_argument("--video", nargs="+", metavar="ID", help="video başına izlenme/AVD/izlenme yüzdesi/abone")
    ap.add_argument("--bas", default=None); ap.add_argument("--son", default=None)
    ap.add_argument("--ctr-isi", action="store_true", help="Reporting API erişim (gösterim+CTR) işini aç")
    ap.add_argument("--ctr-indir", metavar="KLASOR")
    ap.add_argument("--erisim-testi", action="store_true", help="kimliksiz uç nokta erişimi")
    a = ap.parse_args()
    bugun = dt.date.today()
    son, bas = a.son or bugun.isoformat(), a.bas or (bugun - dt.timedelta(days=28)).isoformat()
    try:
        if a.erisim_testi:
            for url, bek in ERISIM_HEDEFLERI:
                s, _, _ = api.istek(url, None, {}, None, 20); print(f"  GET {url[:70]:70} → {s} ({bek})")
            return 0
        if a.yetki_url: yetki_url(a.port); return 0
        if a.yetki_kod: return yetki_kod(a.yetki_kod)
        if a.yetki_iptal:
            for yt, ad in token_kaynaklari(): print(f"Google iptal: HTTP {api.iptal(yt)} ({ad})")
            if os.path.isfile(TOKEN_DOSYASI): os.remove(TOKEN_DOSYASI)
            return 0
        tok = erisim_tokeni()
        if a.dogrula:
            r = sorgu(tok, bas, son, "views,estimatedMinutesWatched,averageViewDuration,subscribersGained")
            print(f"Analitik yetkisi ÇALIŞIYOR · {bas}→{son} kanal: {json.dumps(r[0] if r else {}, ensure_ascii=False)}")
            print(f"Erişim (CTR) rapor işi: {erisim_isi(tok, olustur=False) or 'yok (→ --ctr-isi)'}")
            return 0
        if a.video:
            r = sorgu(tok, bas, son, "views,estimatedMinutesWatched,averageViewDuration,averageViewPercentage,subscribersGained",
                      "video", "video==" + ",".join(a.video))
            print(json.dumps({"bas": bas, "son": son, "satirlar": r}, ensure_ascii=False, indent=1)); return 0
        if a.ctr_isi: print(erisim_isi(tok)); return 0
        if a.ctr_indir: return erisim_indir(tok, a.ctr_indir)
        ap.error("bir komut verin (--dogrula, --video, --yetki-url …)")
    except api.ApiHatasi as e:
        print(f"HATA: {e}"); return 4


if __name__ == "__main__":
    sys.exit(main())
