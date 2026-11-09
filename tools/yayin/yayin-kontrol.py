#!/usr/bin/env python3
# Planlı yayın bekçisi: yüklenen videonun privacyStatus/publishAt'ini plana karşı API ile doğrular + oynatma listesine
# eklemeyi açılış SONRASINA erteler. Etkileşimsiz: kod/cihaz akışı başlatmaz (send_later ile güvenle zamanlanır).
#
# Kullanım:
#   python3 tools/yayin/yayin-kontrol.py uretim/<klasör>/teslim/yayin-sonucu.txt     # dosyadaki tüm planlı videolar
#   python3 tools/yayin/yayin-kontrol.py ghLjMbrweCw [--plan ghLjMbrweCw=2026-11-04T17:00:00Z]
#   python3 tools/yayin/yayin-kontrol.py --liste-ekle LISTE_ID VIDEO_ID             # yalnız video public ise ekler (idempotent)
# Çıkış: 0 tamam/bekliyor · 1 KALDI (erken public, plan silinmiş/değişmiş, geç açılış) · 2 kullanım · 3 liste: video
#        henüz public değil (reddedildi) · 4 yetki yok · 5 API hatası. Zamanlama (koordinatör send_later):
#        yükleme +1 sa → kontrol · açılış −2 sa → kontrol · açılış +15 dk → kontrol + --liste-ekle.
#
# Kök neden (2026-11-09, uretim-muhendisi): 1929 (BVJwZ1C9R1U) ve S08 (ghLjMbrweCw) uzun videoları erken public oldu;
#   4 Shorts zamanında. Kanıt (API, salt okuma): yükleme sonrası her iki uzun video private+publishAt doğru
#   (yayin-sonucu.txt); videos.update kodda HİÇ yok; Shorts da AYNI araçla, AYNI şekilde yeni açılmış public listeye
#   açılıştan 10–58 sa önce eklendi ve tam saatinde açıldı → playlistItems.insert neden DEĞİL (4 karşı örnek). Liste
#   eklemesi → public arası 2 sa 9 dk / 3 sa 40 dk (anlık değil). Uzun videoya özel API adımı yalnız thumbnails.set
#   (yükleme anında; ardından durum hâlâ private+publishAt). Uzun videoya özel STUDIO adımları: Test & Compare
#   ("cannot use this feature on videos that ... are private", support.google.com/youtube/answer/13861714; Shorts'ta
#   hiç yok), sabit yorum, "plan/görünürlük kontrolü" (yukle.py eski UYARI satırı Studio'ya yönlendiriyordu).
#   En olası neden [T]: Studio'da görünürlük/plan alanının elle değiştirilmesi (1929 09:37:48Z yuvarlak değil → elle
#   "Public"; S08 12:00:11Z tam saat +11 sn → planlı açılış izi, plan Studio'da yanlış gün/saat dilimiyle yeniden
#   girilmiş olabilir). YouTube'da görünürlük değişikliği geçmişi API'de yok → kesin kanıt alınamaz; bu yüzden bekçi.
# Adaylar: A) bu bekçi (Data API videos.list, OAuth; yoksa API anahtarıyla yalnız "erken public" tespiti) — KAZANAN.
#   B) Studio'yu tamamen bırakıp yayını API ile anlık publish (zamanlama bizde) — ELENDİ (konteyner/oturum açılış
#   anında yaşamayabilir; YouTube'un kendi zamanlayıcısı daha güvenilir). C) PubSubHubbub bildirimi — ELENDİ (sunucu ister).
import argparse
import datetime as dt
import glob
import json
import os
import re
import sys
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import yayin_api as api  # noqa: E402

KOK = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", ".."))
ERKEN_TOL = dt.timedelta(seconds=60)
GEC_TOL = dt.timedelta(minutes=15)
SATIR = re.compile(r"^(\S+) video_id=(\S+) durum=(\S+) publishAt=(\S+)(?: plan=(\S+))?")


def zaman(s):
    if not s or s == "None": return None
    return dt.datetime.fromisoformat(s.replace("Z", "+00:00")).astimezone(dt.timezone.utc)


def z(t):
    return t.strftime("%Y-%m-%dT%H:%M:%SZ") if t else "—"


def sure(td):
    s = int(abs(td.total_seconds())); return f"{s // 3600} sa {s % 3600 // 60} dk"


def planlari_oku(yollar):
    """yayin-sonucu.txt → {video_id: {"plan": dt, "yukleme": dt, "dosya": yol}} (son satır geçerli; SİLİNDİ düşer)."""
    p = {}
    for y in yollar:
        for ln in open(y, encoding="utf-8"):
            m = SATIR.match(ln.strip())
            plan = m and zaman(m.group(5) or m.group(4))   # plan= (niyet) yoksa yükleme anındaki publishAt
            if plan:
                p[m.group(2)] = {"plan": plan, "yukleme": zaman(m.group(1)), "dosya": y}
            elif " SILINDI" in ln:
                p.pop(ln.split("video_id=")[1].split()[0], None)
    return p


def degerlendir(v, plan, simdi):
    """(sonuç, mesaj). sonuç: TAMAM | BEKLIYOR | KALDI. v = videos.list öğesi (status+snippet) veya None."""
    if not v:
        return "KALDI", "video bulunamadı (silinmiş ya da erişim yok)"
    st, sn = v.get("status", {}), v.get("snippet", {})
    ps, pa = st.get("privacyStatus"), zaman(st.get("publishAt"))
    pub = zaman(sn.get("publishedAt")) if ps == "public" else None
    if simdi < plan:
        if ps == "public":
            return "KALDI", f"ERKEN PUBLIC: açıldı {z(pub)}, plan {z(plan)} ({sure(plan - pub) if pub else '?'} erken)"
        if ps != "private":
            return "KALDI", f"görünürlük '{ps}' (beklenen private + publishAt)"
        if pa is None:
            return "KALDI", "publishAt SİLİNMİŞ: video private kalacak, planlı açılış yok"
        if pa != plan:
            return "KALDI", f"PLAN DEĞİŞMİŞ: publishAt {z(pa)} ≠ plan {z(plan)}"
        return "TAMAM", f"private + publishAt {z(pa)} (açılışa {sure(plan - simdi)})"
    if ps == "public":
        if pub and pub < plan - ERKEN_TOL:
            return "KALDI", f"ERKEN PUBLIC (geçmiş): açıldı {z(pub)}, plan {z(plan)} ({sure(plan - pub)} erken)"
        if pub and pub > plan + GEC_TOL:
            return "KALDI", f"GEÇ açıldı: {z(pub)} (plan {z(plan)}, {sure(pub - plan)} geç)"
        return "TAMAM", f"public, açılış {z(pub)} (plan {z(plan)})"
    if simdi < plan + GEC_TOL:
        return "BEKLIYOR", f"{ps}; açılış {z(plan)} bekleniyor (YouTube birkaç dk geciktirebilir)"
    return "KALDI", f"AÇILMADI: plan {z(plan)} geçti, durum {ps}, publishAt {z(pa)}"


def videolari_oku(ids, cikti=print):
    """{id: öğe}. OAuth yoksa API anahtarı (yalnız public videoları görür) → ('anahtar', ...)."""
    q = ",".join(ids)
    try:
        tok = api.sessiz_yetki(cikti)
        s, _, b = api.istek(f"{api.API}/videos?part=status,snippet&id={q}", None, api._yetki(tok))
        kip = "oauth"
    except api.ApiHatasi as e:
        anahtar = os.environ.get("YOUTUBE_API_KEY")
        if not anahtar: raise
        cikti(f"UYARI: OAuth yok ({str(e)[:60]}) → API anahtarı: yalnız 'erken public' görülebilir, publishAt doğrulanamaz.")
        s, _, b = api.istek(f"{api.API}/videos?part=status,snippet&id={q}&key={urllib.parse.quote(anahtar)}", None)
        kip = "anahtar"
    j = api._kontrol("videos.list", s, b)
    return kip, {i["id"]: i for i in j.get("items", [])}


def kontrol(planlar, simdi=None, cikti=print, oku=videolari_oku):
    simdi = simdi or dt.datetime.now(dt.timezone.utc)
    kip, vs = oku(list(planlar), cikti)
    kotu = 0
    for vid, p in planlar.items():
        v = vs.get(vid)
        if kip == "anahtar" and v is None:   # anahtar private videoyu göremez: açılış öncesi "görünmüyor" = beklenen
            sonuc, msj = ("BEKLIYOR", "public değil (anahtar kipi; publishAt doğrulanamadı)") if simdi < p["plan"] + GEC_TOL \
                else ("KALDI", f"AÇILMADI: plan {z(p['plan'])} geçti, public değil")
        else:
            sonuc, msj = degerlendir(v, p["plan"], simdi)
        kotu += sonuc == "KALDI"
        cikti(f"{sonuc:8} {vid}  {msj}")
        if sonuc != "KALDI" and simdi < p["plan"]:
            cikti(f"         sonraki: açılış −2 sa {z(p['plan'] - dt.timedelta(hours=2))} kontrol · "
                  f"+15 dk {z(p['plan'] + GEC_TOL)} kontrol (+ --liste-ekle)")
    cikti(f"SONUÇ: {'KALDI' if kotu else 'TAMAM'} ({len(planlar)} video, {kotu} sapma; ölçüm {z(simdi)}, kip {kip})")
    if kotu: cikti("→ Koordinatöre ESKALASYON: Studio'da görünürlük/plan alanına dokunulmasın; sapma ayrıntısı yukarıda.")
    return 1 if kotu else 0


def liste_ekle(liste, vid, cikti=print):
    tok = api.sessiz_yetki(cikti)
    s, _, b = api.istek(f"{api.API}/videos?part=status&id={vid}", None, api._yetki(tok))
    it = api._kontrol("videos.list", s, b).get("items") or [{}]
    ps = it[0].get("status", {}).get("privacyStatus")
    if ps != "public":
        cikti(f"REDDEDİLDİ: {vid} durumu '{ps}' — oynatma listesine yalnız açılıştan SONRA eklenir; publishAt+15 dk'da tekrar.")
        return 3
    s, _, b = api.istek(f"{api.API}/playlistItems?part=id&playlistId={liste}&videoId={vid}", None, api._yetki(tok))
    if api._kontrol("playlistItems.list", s, b).get("items"):
        cikti(f"Zaten listede: {vid} → {liste}"); return 0
    api.listeye_ekle(tok, liste, vid)
    cikti(f"Eklendi: {vid} → {liste}")
    for y in glob.glob(os.path.join(KOK, "uretim", "**", "yayin-sonucu.txt"), recursive=True):
        if f"video_id={vid} " in open(y, encoding="utf-8").read():
            with open(y, "a", encoding="utf-8") as f:
                f.write(f"{z(dt.datetime.now(dt.timezone.utc))} LISTE_EKLENDI liste={liste} video_id={vid}\n")
    return 0


def main():
    ap = argparse.ArgumentParser(description="Planlı yayın bekçisi (privacyStatus/publishAt) + ertelenmiş liste ekleme")
    ap.add_argument("hedef", nargs="*", help="yayin-sonucu.txt yolu(ları) veya video id(leri)")
    ap.add_argument("--plan", action="append", default=[], metavar="ID=ISO", help="planı elle ver (dosya yoksa)")
    ap.add_argument("--liste-ekle", nargs=2, metavar=("LISTE_ID", "VIDEO_ID"), help="yalnız public videoyu listeye ekle")
    a = ap.parse_args()
    try:
        if a.liste_ekle:
            return liste_ekle(*a.liste_ekle)
        dosyalar = [h for h in a.hedef if os.path.isfile(h)]
        ids = [h for h in a.hedef if not os.path.isfile(h)]
        if ids and not dosyalar:
            dosyalar = glob.glob(os.path.join(KOK, "uretim", "**", "yayin-sonucu.txt"), recursive=True)
        tum = planlari_oku(dosyalar)
        planlar = {i: tum[i] for i in ids if i in tum} if ids else tum
        for pv in a.plan:
            vid, _, t = pv.partition("=")
            if not zaman(t): ap.error(f"--plan biçimi ID=ISO: {pv}")
            planlar[vid] = {"plan": zaman(t), "yukleme": None, "dosya": None}
        eksik = [i for i in ids if i not in planlar]
        if eksik: ap.error(f"plan bulunamadı: {', '.join(eksik)} (--plan ID=ISO verin)")
        if not planlar: ap.error("kontrol edilecek planlı video yok")
        return kontrol(planlar)
    except api.ApiHatasi as e:
        print(f"HATA: {e}")
        return 4 if "yetki" in str(e) or "OAUTH" in str(e) else 5


if __name__ == "__main__":
    sys.exit(main())
