#!/usr/bin/env python3
# YouTube yayın aracı: yayın paketi → doğrulama → (Niyazi onayıyla) yükleme veya Studio için manuel paket.
#
# Kullanım:
#   python3 tools/yayin/yukle.py uretim/<klasör>/yayin-paketi.json --dry-run        # yalnız doğrula, ağ yok
#   python3 tools/yayin/yukle.py uretim/<klasör>/yayin-paketi.json --manuel-paket    # Studio klasörü + YAYIN.md
#   python3 tools/yayin/yukle.py uretim/<klasör>/yayin-paketi.json                   # yükle (cihaz akışı)
#   python3 tools/yayin/yukle.py uretim/<klasör>/yayin-paketi.json --akis yerel      # Niyazi'nin bilgisayarında, altyazı dahil
#   python3 tools/yayin/yukle.py --sil VIDEO_ID [--onayli]                         # bizim yüklediğimiz videoyu sil (Niyazi onayıyla)
#   python3 tools/yayin/yukle.py --yetki-al / --yetki-iptal                         # kalıcı yetkiyi bir kez al / kaldır
#   python3 tools/yayin/yukle.py --erisim-testi                                      # kimliksiz uç nokta erişimi
#
# Paket şeması (yollar paket dosyasına göre göreli; ayrıntı ve varsayılanlar: yayin_paket.SEMA):
#   {"sema": "yayin-paketi/1", "tur": "uzun"|"shorts",
#    "dosyalar": {"video": "...mp4", "thumbnail": "...jpg", "altyazilar": [{"dosya": "...srt", "dil": "en", "ad": "English"}]},
#    "metadata": {"baslik", "aciklama" ({BOLUMLER} yer tutucu isteğe bağlı), "etiketler": [], "bolumler": [{"zaman","baslik"}],
#                 "kategori_id": "27", "varsayilan_dil": "en", "ses_dili": "en"},
#    "durum": {"gizlilik": "private", "yayin_zamani": "2026-11-02T18:00:00+03:00", "cocuklara_ozel": false,
#              "sentetik_medya": true, "lisans": "youtube", "gomulebilir": true},
#    "oynatma_listesi_id": null, "onay": {"niyazi_onayi": false, "tarih": null}}
#
# Onay kapısı: gerçek yükleme yalnız paket "onay.niyazi_onayi": true ise başlar; ayrıca cihaz kodunu Niyazi girer.
# Kalıcı yetki: ilk seferde kod girilir, yenileme tokenı repo dışında saklanır (yayin_api başlığı); sonra kod sorulmaz. Kimlik: YOUTUBE_OAUTH_CLIENT_ID / YOUTUBE_OAUTH_CLIENT_SECRET.
#
# Adaylar ve eleme (2026-10-26):
#   Yetki  A) cihaz akışı, "youtube" kapsamı — KAZANAN (telefondan 30 sn; tarayıcı/sunucu gerekmez; konteynerde çalışır).
#             Sınır: captions.insert force-ssl ister, cihaz akışında yok → altyazı Studio'dan veya B ile.
#          B) yerel loopback + PKCE, "youtube.force-ssl" — YEDEK (altyazı dahil hepsi; ama Niyazi'nin bilgisayarında
#             repo + Python + video gerekir).
#          C) Yenileme tokenını saklayıp otomatik yükleme — ELENDİ (kural: token diske/repoya yazılmaz).
#   HTTP   stdlib urllib — KAZANAN (bağımlılık yok, HTTPS_PROXY'ye uyar, denetlenebilir ~250 satır).
#          google-api-python-client + google-auth-oauthlib — ELENDİ (≈10 transitif paket, cihaz akışını hazır
#          sunmuyor, token önbelleğe yazma eğilimi). requests — ELENDİ (ek fayda yok; 308 yönetimi zaten elle).
import argparse
import datetime as dt
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import yayin_api as api  # noqa: E402
import yayin_paket as pk  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description="YouTube yayın aracı (Toonomy)")
    ap.add_argument("paket", nargs="?", help="uretim/<klasör>/yayin-paketi.json")
    ap.add_argument("--dry-run", action="store_true", help="yalnız doğrula; ağ çağrısı yok")
    ap.add_argument("--manuel-paket", nargs="?", const="", metavar="KLASOR",
                    help="YouTube Studio'dan elle yükleme klasörü üret (varsayılan: <paket klasörü>/yayin-manuel)")
    ap.add_argument("--akis", choices=["cihaz", "yerel"], default="cihaz", help="OAuth akışı (varsayılan cihaz)")
    ap.add_argument("--erisim-testi", action="store_true", help="Google uç noktalarına kimliksiz erişim testi")
    ap.add_argument("--sil", metavar="VIDEO_ID", help="yayin-sonucu.txt kaydı olan videoyu sil (geri alınamaz)")
    ap.add_argument("--onayli", action="store_true", help="--sil için: Niyazi silmeyi onayladı")
    ap.add_argument("--yetki-al", action="store_true", help="kalıcı yetkiyi bir kez al (cihaz kodu) ve sakla")
    ap.add_argument("--yetki-iptal", action="store_true", help="kalıcı yetkiyi Google'da iptal et ve yerel dosyayı sil")
    a = ap.parse_args()

    if a.yetki_al:
        try:
            _, kapsam, kalici = api.yetki_al(a.akis)
        except api.ApiHatasi as e:
            print(f"YETKİ HATASI: {e}"); return 4
        print(f"Tamam (kapsam: {kapsam}, kalıcı: {kalici})."); return 0 if kalici else 4
    if a.yetki_iptal:
        yt, kaynak = api.yenileme_tokeni()
        if not yt:
            print("Kayıtlı kalıcı yetki yok."); return 0
        print(f"Google iptal: HTTP {api.iptal(yt)} ({kaynak})")
        if os.path.isfile(api.YENILEME_DOSYASI): os.remove(api.YENILEME_DOSYASI)
        if kaynak == "ortam değişkeni":
            print("Not: YOUTUBE_OAUTH_REFRESH_TOKEN ortam ayarından da silinmeli.")
        return 0

    if a.sil:
        return sil(a.sil, a.onayli, a.akis)

    if a.erisim_testi:
        print("Erişim testi (kimlik bilgisi yok; yalnız HTTP durum kodu):")
        sonuc = api.erisim_testi()
        return 0 if all(s > 0 for _, s in sonuc) else 1
    if not a.paket:
        ap.error("paket yolu gerekli")

    p = pk.yukle_paket(a.paket)
    print(f"Paket: {os.path.relpath(p['_yol'])}")
    r = pk.dogrula(p)
    r.yazdir()
    if r.hatalar:
        print("DOĞRULAMA BAŞARISIZ — yükleme/paket üretimi yapılmadı.")
        return 2
    govde = pk.api_govdesi(p)

    if a.manuel_paket is not None:
        cikis = a.manuel_paket or os.path.join(p["_kok"], "yayin-manuel")
        yol = pk.manuel_paket(p, cikis)
        print(f"Manuel paket: {os.path.relpath(cikis)}/ ({', '.join(sorted(os.listdir(cikis)))})")
        print(f"Kopyala-yapıştır rehberi: {os.path.relpath(yol)}")
        if not a.dry_run:
            return 0

    if a.dry_run:
        import json
        g = json.loads(json.dumps(govde)); g["snippet"]["description"] = g["snippet"]["description"][:80] + "…"
        print("DRY-RUN: videos.insert gövdesi (ağ çağrısı yapılmadı):")
        print(json.dumps(g, ensure_ascii=False, indent=2))
        plan = ["videos.insert (resumable)"]
        if p["dosyalar"].get("thumbnail"): plan.append("thumbnails.set")
        if p["dosyalar"]["altyazilar"]:
            plan.append("captions.insert" if a.akis == "yerel" else "captions.insert ATLANIR (cihaz akışı kapsamı yok → Studio/--akis yerel)")
        if p.get("oynatma_listesi_id"): plan.append("playlistItems.insert")
        print("Plan: " + " → ".join(plan))
        if not p["onay"]["niyazi_onayi"]:
            print("Not: onay.niyazi_onayi=false → gerçek yükleme reddedilir.")
        return 0

    # ---- gerçek yükleme ----
    if p["onay"]["niyazi_onayi"] is not True:
        print("REDDEDİLDİ: paket 'onay.niyazi_onayi' true değil. Yükleme yalnız Niyazi onayıyla yapılır.")
        return 3
    try:
        token, kapsam, kalici = api.yetki_al(a.akis)
    except api.ApiHatasi as e:
        print(f"YETKİ HATASI: {e}"); return 4
    print(f"Yetki alındı (kapsam: {kapsam}); erişim tokenı yalnız bellekte.")
    kok = p["_kok"]
    try:
        print("1) videos.insert …")
        v = api.video_yukle(token, pk.dosya_yolu(p, p["dosyalar"]["video"]), govde)
        vid = v["id"]
        print(f"   video id: {vid} · https://youtu.be/{vid} · gizlilik {v.get('status', {}).get('privacyStatus')}"
              f" · publishAt {v.get('status', {}).get('publishAt')}")
        if p["dosyalar"].get("thumbnail"):
            print("2) thumbnails.set …")
            api.thumbnail_yukle(token, vid, pk.dosya_yolu(p, p["dosyalar"]["thumbnail"])); print("   tamam")
        for al in p["dosyalar"]["altyazilar"]:
            if "force-ssl" in kapsam:
                print(f"3) captions.insert ({al['dil']}) …")
                api.altyazi_yukle(token, vid, pk.dosya_yolu(p, al["dosya"]), al["dil"], al.get("ad", "")); print("   tamam")
            else:
                print(f"3) ALTYAZI ATLANDI ({al['dosya']}): cihaz akışı captions.insert kapsamı vermiyor → Studio'dan yükleyin "
                      "(--manuel-paket) veya --akis yerel")
        if p.get("oynatma_listesi_id"):
            print("4) playlistItems.insert …")
            api.listeye_ekle(token, p["oynatma_listesi_id"], vid); print("   tamam")
        d = api.video_durumu(token, vid).get("status", {})
        print(f"Son durum: uploadStatus={d.get('uploadStatus')} privacyStatus={d.get('privacyStatus')} "
              f"publishAt={d.get('publishAt')} madeForKids={d.get('selfDeclaredMadeForKids')}")
        print("UYARI: Denetimsiz API projelerinde video 'private' kilitlenebilir; Studio'da görünürlük ve planı kontrol edin.")
        with open(os.path.join(kok, "yayin-sonucu.txt"), "a", encoding="utf-8") as f:  # yalnız id/zaman; token yok
            f.write(f"{dt.datetime.now(dt.timezone.utc):%Y-%m-%dT%H:%M:%SZ} video_id={vid} durum={d.get('privacyStatus')} "
                    f"publishAt={d.get('publishAt')}\n")
        return 0
    except api.ApiHatasi as e:
        print(f"API HATASI: {e}"); return 5
    finally:
        if not kalici: print(f"Token iptal: HTTP {api.iptal(token)}")
        token = None


def sil(vid, onayli, akis):
    """Yalnız bu aracın yüklediği (uretim/**/yayin-sonucu.txt'de kaydı olan) videoyu, Niyazi onayıyla siler."""
    import glob
    kok = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "uretim")
    kayitlar = [y for y in glob.glob(os.path.join(kok, "**", "yayin-sonucu.txt"), recursive=True)
                if f"video_id={vid} " in open(y, encoding="utf-8").read()]
    if not kayitlar:
        print(f"REDDEDİLDİ: {vid} için yayin-sonucu.txt kaydı yok; yalnız bu aracın yüklediği videolar silinir."); return 3
    if not onayli:
        print("REDDEDİLDİ: --onayli yok. Silme geri alınamaz; yalnız Niyazi onayıyla yapılır."); return 3
    try:
        token, _, kalici = api.yetki_al(akis)
    except api.ApiHatasi as e:
        print(f"YETKİ HATASI: {e}"); return 4
    try:
        baslik = api.video_basligi(token, vid)
        if baslik is None:
            print(f"Video bulunamadı (zaten silinmiş olabilir): {vid}"); return 5
        print(f"Siliniyor: {vid} · {baslik}")
        api.video_sil(token, vid)
        kalan = api.video_basligi(token, vid)
        print("Silindi (videos.list boş döndü)." if kalan is None else f"UYARI: video hâlâ listede: {kalan}")
        for y in kayitlar:
            with open(y, "a", encoding="utf-8") as f:
                f.write(f"{dt.datetime.now(dt.timezone.utc):%Y-%m-%dT%H:%M:%SZ} video_id={vid} SILINDI\n")
        return 0 if kalan is None else 5
    except api.ApiHatasi as e:
        print(f"API HATASI: {e}"); return 5
    finally:
        if not kalici: print(f"Token iptal: HTTP {api.iptal(token)}")


if __name__ == "__main__":
    sys.exit(main())
