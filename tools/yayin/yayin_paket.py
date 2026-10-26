# Yayın paketi şeması, doğrulama ve manuel (YouTube Studio) paket üretimi. Yalnız stdlib (+ varsa ffprobe).
# Şema: tools/yayin/README yerine bu dosyanın SEMA sözlüğü ve yukle.py başlık yorumu.
# Sınırlar resmi dokümandan (developers.google.com/youtube/v3/docs/videos, 2026-10-26 okundu):
#   title ≤100 karakter, < > yasak · description ≤5000 BAYT, < > yasak · tags toplam ≤500 karakter
#   (virgüller sayılır, boşluklu etiket tırnaklı sayılır) · publishAt ISO 8601, yalnız privacyStatus=private iken.
# Kanal kalite kapısı (API sınırı değil): thumbnail ≤2 MB, 1280x720, JPEG/PNG; Shorts ≤180 sn ve dikey.
import datetime as dt
import hashlib
import json
import os
import re
import shutil
import struct
import subprocess

SEMA_SURUM = "yayin-paketi/1"
BASLIK_MAX = 100
ACIKLAMA_MAX_BAYT = 5000
ETIKET_MAX = 500
THUMB_MAX_BAYT = 2 * 1024 * 1024
THUMB_BOYUT = (1280, 720)
SHORTS_MAX_SN = 180
UZUN_MIN_SN = 600  # kanal hedefi (CLAUDE.md): ana video en az 10 dk — uyarı
GECERLI_GIZLILIK = {"private", "unlisted", "public"}

# Şema: alan -> (tip, zorunlu, varsayılan). İç içe alanlar "nokta" ile.
SEMA = {
    "sema": (str, True, None),
    "tur": (str, True, None),  # "uzun" | "shorts"
    "dosyalar.video": (str, True, None),
    "dosyalar.thumbnail": (str, False, None),
    "dosyalar.altyazilar": (list, False, []),  # [{"dosya": "x.srt", "dil": "en", "ad": "English"}]
    "metadata.baslik": (str, True, None),
    "metadata.aciklama": (str, True, None),
    "metadata.etiketler": (list, False, []),
    "metadata.bolumler": (list, False, []),  # [{"zaman": "00:00", "baslik": "Intro"}]
    "metadata.kategori_id": (str, False, "27"),  # 27 = Education
    "metadata.varsayilan_dil": (str, False, "en"),
    "metadata.ses_dili": (str, False, "en"),
    "durum.gizlilik": (str, False, "private"),
    "durum.yayin_zamani": (str, False, None),  # ISO 8601, saat dilimli: "2026-11-02T18:00:00+03:00"
    "durum.cocuklara_ozel": (bool, False, False),
    "durum.sentetik_medya": (bool, False, True),
    "durum.lisans": (str, False, "youtube"),
    "durum.gomulebilir": (bool, False, True),
    "oynatma_listesi_id": (str, False, None),
    "onay.niyazi_onayi": (bool, False, False),
    "onay.tarih": (str, False, None),
}


class Rapor:
    def __init__(self):
        self.hatalar, self.uyarilar, self.tamam = [], [], []

    def hata(self, m): self.hatalar.append(m)
    def uyari(self, m): self.uyarilar.append(m)
    def ok(self, m): self.tamam.append(m)

    def yazdir(self):
        for m in self.tamam: print(f"  [OK]    {m}")
        for m in self.uyarilar: print(f"  [UYARI] {m}")
        for m in self.hatalar: print(f"  [HATA]  {m}")
        print(f"  Sonuç: {len(self.hatalar)} hata, {len(self.uyarilar)} uyarı, {len(self.tamam)} geçen kontrol")


def _al(d, yol):
    for p in yol.split("."):
        if not isinstance(d, dict) or p not in d:
            return KeyError
        d = d[p]
    return d


def _koy(d, yol, v):
    ps = yol.split(".")
    for p in ps[:-1]:
        d = d.setdefault(p, {})
    d[ps[-1]] = v


def yukle_paket(yol):
    with open(yol, encoding="utf-8") as f:
        p = json.load(f)
    p["_kok"] = os.path.dirname(os.path.abspath(yol))
    p["_yol"] = os.path.abspath(yol)
    return p


def dosya_yolu(p, rel):
    return rel if os.path.isabs(rel) else os.path.normpath(os.path.join(p["_kok"], rel))


# ---------- yardımcı ölçümler ----------
def resim_boyutu(yol):
    """PNG/JPEG genişlik, yükseklik, tür (stdlib başlık okuma)."""
    with open(yol, "rb") as f:
        b = f.read(26)
        if b[:8] == b"\x89PNG\r\n\x1a\n":
            w, h = struct.unpack(">II", b[16:24]); return w, h, "png"
        if b[:2] != b"\xff\xd8":
            return None
        f.seek(2)
        while True:
            m = f.read(2)
            if len(m) < 2 or m[0] != 0xFF:
                return None
            if m[1] in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                f.read(3); h, w = struct.unpack(">HH", f.read(4)); return w, h, "jpeg"
            if m[1] in (0xD8, 0x01) or 0xD0 <= m[1] <= 0xD7:
                continue
            (n,) = struct.unpack(">H", f.read(2)); f.seek(n - 2, 1)


def video_bilgi(yol):
    """ffprobe ile süre/genişlik/yükseklik; ffprobe yoksa None."""
    if not shutil.which("ffprobe"):
        return None
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                        "stream=width,height,codec_name:stream_side_data=rotation:format=duration",
                        "-of", "json", yol], capture_output=True, text=True)
    if r.returncode != 0:
        return None
    j = json.loads(r.stdout)
    s = (j.get("streams") or [{}])[0]
    w, h = s.get("width"), s.get("height")
    rot = next((abs(int(x.get("rotation", 0))) for x in s.get("side_data_list", []) if "rotation" in x), 0)
    if rot in (90, 270):
        w, h = h, w
    return {"sure": float(j.get("format", {}).get("duration", 0)), "w": w, "h": h, "codec": s.get("codec_name")}


def etiket_uzunlugu(etiketler):
    """YouTube kuralı: virgüller sayılır; boşluk içeren etiket tırnak içinde sayılır (+2)."""
    if not etiketler:
        return 0
    return sum(len(t) + (2 if " " in t else 0) for t in etiketler) + (len(etiketler) - 1)


_ZAMAN = re.compile(r"^(?:(\d{1,2}):)?(\d{1,2}):(\d{2})$")


def zaman_sn(z):
    m = _ZAMAN.match(z.strip())
    if not m:
        return None
    s, dk, sn = int(m.group(1) or 0), int(m.group(2)), int(m.group(3))
    return s * 3600 + dk * 60 + sn


def bolum_metni(bolumler):
    return "\n".join(f"{b['zaman']} {b['baslik']}" for b in bolumler)


def tam_aciklama(p):
    """Açıklama + (varsa) bölüm listesi. Açıklamada {BOLUMLER} varsa oraya, yoksa sona eklenir."""
    a = p["metadata"]["aciklama"]
    bl = p["metadata"].get("bolumler") or []
    if not bl:
        return re.sub(r"\n{3,}", "\n\n", a.replace("{BOLUMLER}", "")).strip()
    t = "Chapters:\n" + bolum_metni(bl)
    return a.replace("{BOLUMLER}", t) if "{BOLUMLER}" in a else a.rstrip() + "\n\n" + t


_SRT_ZAMAN = re.compile(r"(\d{2}):(\d{2}):(\d{2})[,.](\d{3})\s*-->\s*(\d{2}):(\d{2}):(\d{2})[,.](\d{3})")


def srt_kontrol(yol):
    """(blok sayısı, son bitiş sn, hata listesi)."""
    hatalar, onceki, son = [], -1.0, 0.0
    with open(yol, encoding="utf-8-sig") as f:
        t = f.read().replace("\r\n", "\n").strip()
    bloklar = [b for b in re.split(r"\n\s*\n", t) if b.strip()]
    for i, b in enumerate(bloklar, 1):
        m = _SRT_ZAMAN.search(b)
        if not m:
            hatalar.append(f"blok {i}: zaman satırı yok"); continue
        g = [int(x) for x in m.groups()]
        bas = g[0] * 3600 + g[1] * 60 + g[2] + g[3] / 1000
        bit = g[4] * 3600 + g[5] * 60 + g[6] + g[7] / 1000
        if bit <= bas: hatalar.append(f"blok {i}: bitiş ≤ başlangıç")
        if bas < onceki: hatalar.append(f"blok {i}: zaman geriye gidiyor")
        if not b[m.end():].strip(): hatalar.append(f"blok {i}: metin boş")
        onceki, son = bas, max(son, bit)
    return len(bloklar), son, hatalar


def zaman_parse(s):
    """ISO 8601 → aware datetime (saat dilimi zorunlu)."""
    d = dt.datetime.fromisoformat(s.replace("Z", "+00:00"))
    if d.tzinfo is None:
        raise ValueError("saat dilimi yok (ör. +03:00 veya Z ekleyin)")
    return d


# ---------- doğrulama ----------
def dogrula(p, simdi=None, video_olc=True):
    r = Rapor()
    simdi = simdi or dt.datetime.now(dt.timezone.utc)
    # 1) şema: tip/zorunluluk + varsayılanlar
    for alan, (tip, zorunlu, vars_) in SEMA.items():
        v = _al(p, alan)
        if v is KeyError or v is None:
            if zorunlu: r.hata(f"şema: '{alan}' zorunlu")
            elif vars_ is not None or v is KeyError: _koy(p, alan, vars_ if not isinstance(vars_, list) else list(vars_))
            continue
        if not isinstance(v, tip):
            r.hata(f"şema: '{alan}' tipi {tip.__name__} olmalı")
    bilinen_ust = {k.split(".")[0] for k in SEMA} | {"_kok", "_yol", "_not"}
    for k in p:
        if k not in bilinen_ust: r.uyari(f"şema: bilinmeyen alan '{k}' (yok sayılır)")
    if r.hatalar:
        return r
    if p["sema"] != SEMA_SURUM: r.hata(f"şema sürümü '{p['sema']}' ≠ '{SEMA_SURUM}'")
    if p["tur"] not in ("uzun", "shorts"): r.hata("tur 'uzun' veya 'shorts' olmalı")
    else: r.ok("şema geçerli")
    m, d = p["metadata"], p["durum"]

    # 2) başlık / açıklama / etiketler
    b = m["baslik"].strip()
    if not b: r.hata("başlık boş")
    elif len(b) > BASLIK_MAX: r.hata(f"başlık {len(b)} karakter > {BASLIK_MAX}")
    elif "<" in b or ">" in b: r.hata("başlıkta < veya > olamaz")
    else: r.ok(f"başlık {len(b)}/{BASLIK_MAX} karakter")
    a = tam_aciklama(p)
    ab = len(a.encode("utf-8"))
    if ab > ACIKLAMA_MAX_BAYT: r.hata(f"açıklama {ab} bayt > {ACIKLAMA_MAX_BAYT}")
    elif "<" in a or ">" in a: r.hata("açıklamada < veya > olamaz")
    else: r.ok(f"açıklama (bölümler dahil) {ab}/{ACIKLAMA_MAX_BAYT} bayt")
    if not re.search(r"not financial advice", a, re.I):
        r.uyari("açıklamada 'not financial advice' yasal notu yok (kanal kuralı)")
    et = m["etiketler"]
    if not all(isinstance(t, str) and t.strip() for t in et): r.hata("etiketler boş olmayan metin olmalı")
    else:
        n = etiket_uzunlugu(et)
        if n > ETIKET_MAX: r.hata(f"etiketler toplam {n} karakter > {ETIKET_MAX}")
        elif any("<" in t or ">" in t for t in et): r.hata("etikette < veya > olamaz")
        else: r.ok(f"etiketler {len(et)} adet, {n}/{ETIKET_MAX} karakter (YouTube sayımı)")
    if not re.fullmatch(r"\d{1,2}", m["kategori_id"]): r.hata("kategori_id sayısal olmalı (27 = Education)")
    for alan in ("varsayilan_dil", "ses_dili"):
        if not re.fullmatch(r"[a-z]{2,3}(-[A-Za-z0-9]{2,8})?", m[alan]): r.hata(f"{alan} BCP-47 olmalı (ör. en)")

    # 3) dosyalar
    vy = dosya_yolu(p, p["dosyalar"]["video"])
    vb = None
    if not os.path.isfile(vy): r.hata(f"video yok: {vy}")
    else:
        r.ok(f"video var: {os.path.relpath(vy)} ({os.path.getsize(vy)/1e6:.1f} MB)")
        vb = video_bilgi(vy) if video_olc else None
        if video_olc and vb is None: r.uyari("ffprobe yok/okunamadı: süre ve en-boy kontrol edilemedi")
    if vb:
        r.ok(f"video {vb['w']}x{vb['h']}, {vb['sure']:.1f} sn, {vb['codec']}")
        if p["tur"] == "shorts":
            if vb["sure"] > SHORTS_MAX_SN: r.hata(f"Shorts {vb['sure']:.0f} sn > {SHORTS_MAX_SN}")
            if vb["w"] > vb["h"]: r.hata("Shorts dikey (veya kare) olmalı")
            if "#shorts" not in (b + " " + a).lower(): r.hata("Shorts: başlık veya açıklamada #Shorts yok")
        else:
            if vb["w"] < vb["h"]: r.uyari("uzun video dikey görünüyor")
            if vb["sure"] < UZUN_MIN_SN: r.uyari(f"uzun video {vb['sure']:.0f} sn < hedef {UZUN_MIN_SN} sn (10 dk)")
    th = p["dosyalar"].get("thumbnail")
    if th:
        ty = dosya_yolu(p, th)
        if not os.path.isfile(ty): r.hata(f"thumbnail yok: {ty}")
        else:
            boy = os.path.getsize(ty); rb = resim_boyutu(ty)
            if rb is None: r.hata("thumbnail JPEG/PNG değil")
            elif boy > THUMB_MAX_BAYT: r.hata(f"thumbnail {boy/1024:.0f} KB > 2048 KB")
            elif (rb[0], rb[1]) != THUMB_BOYUT: r.hata(f"thumbnail {rb[0]}x{rb[1]} ≠ 1280x720")
            else: r.ok(f"thumbnail {rb[0]}x{rb[1]} {rb[2]}, {boy/1024:.0f} KB")
    elif p["tur"] == "uzun": r.uyari("uzun video için thumbnail verilmemiş")
    for i, al in enumerate(p["dosyalar"]["altyazilar"]):
        if not isinstance(al, dict) or "dosya" not in al:
            r.hata(f"altyazi[{i}]: 'dosya' zorunlu"); continue
        al.setdefault("dil", m["ses_dili"]); al.setdefault("ad", "")
        sy = dosya_yolu(p, al["dosya"])
        if not os.path.isfile(sy): r.hata(f"altyazı yok: {sy}"); continue
        if not sy.lower().endswith(".srt"): r.uyari(f"altyazı uzantısı .srt değil: {sy}")
        n, son, hs = srt_kontrol(sy)
        for h in hs[:5]: r.hata(f"SRT {os.path.basename(sy)}: {h}")
        if n == 0: r.hata(f"SRT {os.path.basename(sy)} boş")
        elif not hs:
            r.ok(f"SRT {os.path.basename(sy)}: {n} blok, son {son:.1f} sn, dil {al['dil']}")
            if vb and son > vb["sure"] + 0.5: r.hata(f"SRT video süresinden uzun ({son:.1f} > {vb['sure']:.1f} sn)")

    # 4) bölümler (YouTube: ilk 00:00, en az 3, her biri ≥10 sn, artan)
    bl = m["bolumler"]
    if bl:
        sn = [zaman_sn(x.get("zaman", "")) if isinstance(x, dict) else None for x in bl]
        if None in sn or not all(isinstance(x, dict) and x.get("baslik") for x in bl):
            r.hata("bölüm: her öğe {'zaman': 'MM:SS', 'baslik': '...'} olmalı")
        elif sn[0] != 0: r.hata("bölüm: ilk bölüm 00:00 olmalı")
        elif len(sn) < 3: r.hata("bölüm: en az 3 bölüm gerekir")
        elif any(b2 - b1 < 10 for b1, b2 in zip(sn, sn[1:])): r.hata("bölüm: her bölüm ≥10 sn ve artan sırada olmalı")
        elif vb and sn[-1] >= vb["sure"]: r.hata("bölüm: son bölüm video süresinden sonra başlıyor")
        else: r.ok(f"bölümler {len(sn)} adet, kurallara uygun")

    # 5) durum / zamanlama
    if d["gizlilik"] not in GECERLI_GIZLILIK: r.hata("gizlilik private|unlisted|public olmalı")
    if d["cocuklara_ozel"] is not False: r.uyari("cocuklara_ozel=true: kanal hedefi genel kitle; emin olun")
    if d["lisans"] not in ("youtube", "creativeCommon"): r.hata("lisans youtube|creativeCommon olmalı")
    yz = d.get("yayin_zamani")
    if yz:
        try:
            z = zaman_parse(yz)
            if d["gizlilik"] != "private": r.hata("yayin_zamani yalnız gizlilik=private ile kullanılabilir (YouTube kuralı)")
            elif z <= simdi: r.hata(f"yayin_zamani geçmişte ({yz}); YouTube geçmiş zamanı hemen yayınlar")
            else:
                saat = (z - simdi).total_seconds() / 3600
                if saat < 1: r.uyari("yayin_zamani 1 saatten yakın: yükleme+işleme yetişmeyebilir")
                r.ok(f"yayin_zamani gelecekte: {z.astimezone(dt.timezone.utc):%Y-%m-%dT%H:%M:%SZ} (+{saat:.1f} sa)")
        except ValueError as e:
            r.hata(f"yayin_zamani ISO 8601 değil: {yz} ({e})")
    else:
        r.uyari(f"yayin_zamani yok: video '{d['gizlilik']}' olarak kalır")
    if p.get("oynatma_listesi_id") and not re.fullmatch(r"[A-Za-z0-9_-]{10,64}", p["oynatma_listesi_id"]):
        r.hata("oynatma_listesi_id biçimi geçersiz")
    return r


# ---------- API gövdesi ----------
def api_govdesi(p):
    m, d = p["metadata"], p["durum"]
    st = {"privacyStatus": d["gizlilik"], "selfDeclaredMadeForKids": d["cocuklara_ozel"],
          "containsSyntheticMedia": d["sentetik_medya"], "license": d["lisans"], "embeddable": d["gomulebilir"]}
    if d.get("yayin_zamani"):
        st["publishAt"] = zaman_parse(d["yayin_zamani"]).astimezone(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return {"snippet": {"title": m["baslik"].strip(), "description": tam_aciklama(p), "tags": m["etiketler"],
                        "categoryId": m["kategori_id"], "defaultLanguage": m["varsayilan_dil"],
                        "defaultAudioLanguage": m["ses_dili"]},
            "status": st}


# ---------- manuel paket (YouTube Studio) ----------
def _sha256(yol):
    h = hashlib.sha256()
    with open(yol, "rb") as f:
        for c in iter(lambda: f.read(1 << 20), b""): h.update(c)
    return h.hexdigest()


def _kopyala(kaynak, hedef):
    if os.path.exists(hedef): os.remove(hedef)
    try: os.link(kaynak, hedef)  # aynı disk: anında, yer kaplamaz
    except OSError: shutil.copy2(kaynak, hedef)


KATEGORI = {"27": "Education", "25": "News & Politics", "22": "People & Blogs", "24": "Entertainment"}


def manuel_paket(p, cikis):
    os.makedirs(cikis, exist_ok=True)
    m, d = p["metadata"], p["durum"]
    vy = dosya_yolu(p, p["dosyalar"]["video"])
    vh = os.path.join(cikis, "video" + os.path.splitext(vy)[1]); _kopyala(vy, vh)
    th_ad = None
    if p["dosyalar"].get("thumbnail"):
        ty = dosya_yolu(p, p["dosyalar"]["thumbnail"])
        th_ad = "thumbnail" + os.path.splitext(ty)[1]; _kopyala(ty, os.path.join(cikis, th_ad))
    srtler = []
    for al in p["dosyalar"]["altyazilar"]:
        sy = dosya_yolu(p, al["dosya"]); ad = f"altyazi-{al['dil']}.srt"
        _kopyala(sy, os.path.join(cikis, ad)); srtler.append((ad, al))
    aciklama = tam_aciklama(p)
    tr = dt.timezone(dt.timedelta(hours=3))
    if d.get("yayin_zamani"):
        z = zaman_parse(d["yayin_zamani"])
        zaman = f"{z.astimezone(tr):%d.%m.%Y %H:%M} (Türkiye saati, UTC+3) — UTC {z.astimezone(dt.timezone.utc):%Y-%m-%d %H:%M}"
    else:
        zaman = "zamanlama yok — gizlilik: " + d["gizlilik"]
    kat = KATEGORI.get(m["kategori_id"], m["kategori_id"])
    sat = [f"# YAYIN — {m['baslik'].strip()}", "",
           f"Paket: `{os.path.relpath(p['_yol'])}` · üretildi {dt.datetime.now(tr):%d.%m.%Y %H:%M} · tür: **{p['tur']}**", "",
           "YouTube Studio (bilgisayar tarayıcısı önerilir; altyazı ve thumbnail yükleme mobil uygulamada sınırlı):",
           "studio.youtube.com → **Oluştur → Video yükle**. Aşağıdaki kutuları sırayla kopyala-yapıştır.", "",
           "## 1. Dosyalar", "",
           f"- Video: `video{os.path.splitext(vy)[1]}` (SHA-256 `{_sha256(vh)[:16]}…`, {os.path.getsize(vh)/1e6:.1f} MB)"]
    if th_ad: sat.append(f"- Thumbnail: `{th_ad}` → Ayrıntılar → Küçük resim → Yükle")
    for ad, al in srtler: sat.append(f"- Altyazı: `{ad}` (dil: {al['dil']}) → Altyazılar → Dil ekle → Yükle → *Zamanlamalı*")
    sat += ["", f"## 2. Başlık ({len(m['baslik'].strip())}/100)", "", "```", m["baslik"].strip(), "```", "",
            f"## 3. Açıklama ({len(aciklama.encode('utf-8'))}/5000 bayt, bölümler dahil)", "", "```", aciklama, "```", "",
            f"## 4. Etiketler ({etiket_uzunlugu(m['etiketler'])}/500) — Ayrıntılar → Daha fazla göster → Etiketler", "",
            "```", ", ".join(m["etiketler"]), "```", ""]
    if m["bolumler"]:
        sat += ["## 5. Bölümler (açıklamada zaten var; kontrol için)", "", "```", bolum_metni(m["bolumler"]), "```", ""]
    sat += ["## 6. Ayarlar (Studio'da işaretle)", "",
            "| Ayar | Değer |", "|---|---|",
            f"| Kitle | **Hayır, çocuklara özel değil** ({'EVET' if d['cocuklara_ozel'] else 'selfDeclaredMadeForKids=false'}) |",
            f"| Değiştirilmiş/yapay içerik (Altered content) | **{'Evet' if d['sentetik_medya'] else 'Hayır'}** |",
            f"| Kategori | {kat} ({m['kategori_id']}) |",
            f"| Video dili / Başlık-açıklama dili | {m['ses_dili']} / {m['varsayilan_dil']} |",
            f"| Lisans | {'Standart YouTube Lisansı' if d['lisans']=='youtube' else 'Creative Commons'} · Yerleştirmeye izin: {'Evet' if d['gomulebilir'] else 'Hayır'} |",
            f"| Görünürlük | **{d['gizlilik']}** → Planla: {zaman} |"]
    if p.get("oynatma_listesi_id"): sat.append(f"| Oynatma listesi | `{p['oynatma_listesi_id']}` |")
    if p["tur"] == "shorts": sat.append("| Shorts | dikey, ≤3 dk, başlık/açıklamada #Shorts var |")
    sat += ["", "## 7. Son kontrol", "", "- [ ] Hakem son kalite kontrolü geçti, Niyazi onayı verildi",
            "- [ ] Kontroller sekmesinde telif / uygunluk uyarısı yok", "- [ ] Planlanan saat doğru (Türkiye saati)", ""]
    n = 0
    for i, s in enumerate(sat):  # bölüm başlıklarını sırayla numarala (isteğe bağlı bölümler atlanınca boşluk kalmasın)
        if s.startswith("## "):
            n += 1; sat[i] = f"## {n}. " + s.split(". ", 1)[1]
    with open(os.path.join(cikis, "YAYIN.md"), "w", encoding="utf-8") as f:
        f.write("\n".join(sat))
    return os.path.join(cikis, "YAYIN.md")
