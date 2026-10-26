#!/usr/bin/env python3
# YouTube yayın aracı: yayın paketi → doğrulama → (Niyazi onayıyla) yükleme veya Studio için manuel paket.
#
# Kullanım:
#   python3 tools/yayin/yukle.py uretim/<klasör>/yayin-paketi.json --dry-run        # yalnız doğrula, ağ yok
#   python3 tools/yayin/yukle.py uretim/<klasör>/yayin-paketi.json --manuel-paket    # Studio klasörü + YAYIN.md
#   python3 tools/yayin/yukle.py uretim/<klasör>/yayin-paketi.json                   # yükle (cihaz akışı)
#   python3 tools/yayin/yukle.py uretim/<klasör>/yayin-paketi.json --akis yerel      # Niyazi'nin bilgisayarında, altyazı dahil
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
# Token yalnız bellekte; iş bitince iptal edilir. Kimlik: YOUTUBE_OAUTH_CLIENT_ID / YOUTUBE_OAUTH_CLIENT_SECRET.
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
    ap = argparse.ArgumentParser(description="YouTube yayın aracı (Financial Rise)")
    ap.add_argument("paket", nargs="?", help="uretim/<klasör>/yayin-paketi.json")
    ap.add_argument("--dry-run", action="store_true", help="yalnız doğrula; ağ çağrısı yok")
    ap.add_argument("--manuel-paket", nargs="?", const="", metavar="KLASOR",
                    help="YouTube Studio'dan elle yükleme klasörü üret (varsayılan: <paket klasörü>/yayin-manuel)")
    ap.add_argument("--akis", choices=["cihaz", "yerel"], default="cihaz", help="OAuth akışı (varsayılan cihaz)")
    ap.add_argument("--erisim-testi", action="store_true", help="Google uç noktalarına kimliksiz erişim testi")
    a = ap.parse_args()

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
        cid, sec = api.kimlik_bilgisi()
        token, kapsam = (api.cihaz_akisi if a.akis == "cihaz" else api.yerel_akis)(cid, sec)
    except api.ApiHatasi as e:
        print(f"YETKİ HATASI: {e}"); return 4
    print(f"Yetki alındı (kapsam: {kapsam}); token yalnız bellekte.")
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
        print(f"Token iptal: HTTP {api.iptal(token)}")
        token = None


if __name__ == "__main__":
    sys.exit(main())
