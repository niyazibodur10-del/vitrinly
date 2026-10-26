#!/usr/bin/env python3
# Kanal kimliği aracı: açıklama, anahtar kelimeler, dil/ülke, banner, oynatma listeleri, kanal fragmanı.
#
# Kullanım:
#   python3 tools/yayin/kanal.py uretim/kanal-kimligi/kanal-paketi.json                      # fark raporu (değiştirmez)
#   python3 tools/yayin/kanal.py uretim/kanal-kimligi/kanal-paketi.json --banner <jpg> --uygula --onayli
#
# Paket: {"aciklama", "anahtar_kelimeler", "varsayilan_dil", "ulke",
#         "oynatma_listeleri": [{"baslik", "aciklama", "gizlilik"}], "fragman_video_id": null}
# Kurallar: --uygula yalnız --onayli (Niyazi onayı) ile çalışır. channels.update brandingSettings parçasını BÜTÜN olarak
# değiştirir; bu yüzden mevcut ayarlar okunur, yalnız paketteki alanlar üzerine yazılır. Oynatma listeleri başlığa göre
# idempotent (aynı başlık varsa yeniden oluşturulmaz). Profil fotoğrafı, kanal adı ve @tanıtıcı API'de yok → Studio.
# Banner: channelBanners.insert (16:9, ≥2048x1152, ≤6 MB) → dönen url brandingSettings.image.bannerExternalUrl.
# Kaynak: developers.google.com/youtube/v3/docs/channels/update ve /channelBanners/insert (2026-10-26 okundu).
import argparse
import json
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import yayin_api as api  # noqa: E402

BANNER_MAX = 6 * 1024 * 1024


def kanal_oku(token):
    s, _, b = api.istek(f"{api.API}/channels?part=id,brandingSettings&mine=true", None, api._yetki(token))
    j = api._kontrol("channels.list", s, b)
    if not j.get("items"):
        raise api.ApiHatasi("bu hesapta kanal yok")
    return j["items"][0]


def listeler_oku(token):
    s, _, b = api.istek(f"{api.API}/playlists?part=snippet&mine=true&maxResults=50", None, api._yetki(token))
    return {p["snippet"]["title"]: p["id"] for p in api._kontrol("playlists.list", s, b).get("items", [])}


def dogrula(p, banner):
    hatalar = []
    if len(p.get("aciklama", "")) > 1000: hatalar.append(f"açıklama {len(p['aciklama'])} > 1000 karakter")
    if len(p.get("anahtar_kelimeler", "")) > 500: hatalar.append("anahtar kelimeler > 500 karakter")
    for k in ("<", ">"):
        if k in p.get("aciklama", ""): hatalar.append(f"açıklamada '{k}' var (YouTube kabul etmez)")
    if banner:
        if not os.path.isfile(banner): hatalar.append(f"banner yok: {banner}")
        elif os.path.getsize(banner) > BANNER_MAX: hatalar.append("banner > 6 MB")
        else:
            try:
                import subprocess
                wh = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries", "stream=width,height",
                                     "-of", "csv=p=0", banner], capture_output=True, text=True).stdout.strip()
                w, h = map(int, wh.split(","))
                if w < 2048 or h < 1152: hatalar.append(f"banner {w}x{h} < 2048x1152")
                if abs(w / h - 16 / 9) > 0.01: hatalar.append(f"banner oranı 16:9 değil ({w}x{h})")
            except Exception as e:  # ffprobe yoksa boyutu API denetler
                print(f"  (banner boyutu ölçülemedi: {e})")
    return hatalar


def banner_yukle(token, yol):
    tur = "image/png" if yol.lower().endswith(".png") else "image/jpeg"
    with open(yol, "rb") as f:
        veri = f.read()
    s, _, b = api.istek(f"{api.UPLOAD}/channelBanners/insert", veri, api._yetki(token, {"Content-Type": tur}))
    return api._kontrol("channelBanners.insert", s, b)["url"]


def main():
    ap = argparse.ArgumentParser(description="Kanal kimliği aracı (Toonomy)")
    ap.add_argument("paket")
    ap.add_argument("--banner", help="banner görseli (jpg/png)")
    ap.add_argument("--uygula", action="store_true", help="değişiklikleri kanala uygula")
    ap.add_argument("--onayli", action="store_true", help="Niyazi onayı (--uygula için şart)")
    a = ap.parse_args()

    p = json.load(open(a.paket, encoding="utf-8"))
    hatalar = dogrula(p, a.banner)
    for h in hatalar: print(f"  [HATA] {h}")
    if hatalar: return 2
    if a.uygula and not a.onayli:
        print("REDDEDİLDİ: --onayli yok. Kanal değişikliği yalnız Niyazi onayıyla yapılır."); return 3

    try:
        token, _, kalici = api.yetki_al()
    except api.ApiHatasi as e:
        print(f"YETKİ HATASI: {e}"); return 4
    try:
        k = kanal_oku(token)
        bs = k.get("brandingSettings", {})
        ch = dict(bs.get("channel", {}))
        yeni = dict(ch)
        for alan, anahtar in (("aciklama", "description"), ("anahtar_kelimeler", "keywords"),
                              ("varsayilan_dil", "defaultLanguage"), ("ulke", "country"),
                              ("fragman_video_id", "unsubscribedTrailer")):
            if p.get(alan): yeni[anahtar] = p[alan]
        print("Fark (mevcut → yeni):")
        for anahtar in ("description", "keywords", "defaultLanguage", "country", "unsubscribedTrailer"):
            if ch.get(anahtar) != yeni.get(anahtar):
                eski, yn = str(ch.get(anahtar))[:70], str(yeni.get(anahtar))[:70]
                print(f"  {anahtar}: {eski!r} → {yn!r}")
        mevcut_liste = listeler_oku(token)
        eklenecek = [l for l in p.get("oynatma_listeleri", []) if l["baslik"] not in mevcut_liste]
        print(f"Oynatma listeleri: {len(mevcut_liste)} mevcut, {len(eklenecek)} eklenecek: {[l['baslik'] for l in eklenecek]}")
        if a.banner: print(f"Banner: {a.banner} yüklenecek")
        if not a.uygula:
            print("Fark raporu; kanal değiştirilmedi (uygulamak için --uygula --onayli)."); return 0

        govde = {"id": k["id"], "brandingSettings": {"channel": yeni}}
        if a.banner:
            print("1) channelBanners.insert …")
            govde["brandingSettings"]["image"] = {"bannerExternalUrl": banner_yukle(token, a.banner)}
            print("   tamam")
        print("2) channels.update (brandingSettings) …")
        s, _, b = api.istek(f"{api.API}/channels?part=brandingSettings", json.dumps(govde).encode(),
                            api._yetki(token, {"Content-Type": "application/json; charset=UTF-8"}), yontem="PUT")
        api._kontrol("channels.update", s, b); print("   tamam")
        for l in eklenecek:
            g = {"snippet": {"title": l["baslik"], "description": l.get("aciklama", ""), "defaultLanguage": p.get("varsayilan_dil", "en")},
                 "status": {"privacyStatus": l.get("gizlilik", "public")}}
            s, _, b = api.istek(f"{api.API}/playlists?part=snippet,status", json.dumps(g).encode(),
                                api._yetki(token, {"Content-Type": "application/json; charset=UTF-8"}))
            print(f"3) liste oluşturuldu: {l['baslik']} → {api._kontrol('playlists.insert', s, b)['id']}")
        import time; time.sleep(15)  # channels.list güncellemeyi ~10-15 sn gecikmeyle döndürüyor (2026-10-26 ölçümü)
        print("Kontrol: " + json.dumps({kk: str(vv)[:60] for kk, vv in kanal_oku(token)["brandingSettings"]["channel"].items()},
                                       ensure_ascii=False))
        return 0
    except api.ApiHatasi as e:
        print(f"API HATASI: {e}"); return 5
    finally:
        if not kalici: print(f"Token iptal: HTTP {api.iptal(token)}")


if __name__ == "__main__":
    sys.exit(main())
