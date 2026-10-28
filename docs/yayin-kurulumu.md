# YouTube yayın kurulumu (Niyazi için, telefondan yapılabilir)

Amaç: Niyazi onay verdikten sonra videoyu sistemin yüklemesi (`tools/yayin/yukle.py`). Kimlik bilgisi asla repoya
veya sohbete yazılmaz; yalnız bulut ortamının ortam değişkeni ayarına girilir. Her yüklemede Niyazi telefonda
google.com/device adresine 8 haneli kodu girer (≈30 sn); ilk seferden sonra kalıcı yetki kullanılır (bkz. Güncel durum).

Kontrol tarihi: 2026-10-26. Bilgiler resmi Google sayfalarından okundu (kaynaklar en altta).

## Güncel durum (2026-10-26)
- Adım 1–8 tamam. Test yüklemesi (private) görünürlüğü değiştirilebildi → **kilit yok, Adım 9 gerekmez.** Test videosu silindi.
- **Kalıcı yetki** (Niyazi kararı): her yüklemede kod girilmez. `yukle.py --yetki-al` bir kez çalışır, yenileme tokenı
  `~/.finansal-arac/youtube-yenileme-tokeni` (600, repo dışı) dosyasına yazılır; oturumlar arası kalıcılık için değer
  bulut ortamına `YOUTUBE_OAUTH_REFRESH_TOKEN` olarak eklenir (yeni oturumda okunur). İptal: `--yetki-iptal`.
- **7 gün sınırı (doğrulandı, developers.google.com/identity/protocols/oauth2):** "Testing" yayın durumundaki harici
  uygulamaya verilen yenileme tokenı 7 günde dolar. Kalıcı olması için https://console.cloud.google.com/auth/audience →
  **Publish app**, sonra `--yetki-al` tekrar. Yayındaki uygulamada token 6 ay kullanılmazsa veya iptal edilirse düşer.
- Silme: `yukle.py --sil VIDEO_ID --onayli` (yalnız `yayin-sonucu.txt` kaydı olan kendi yüklemelerimiz).

## Önce bilmeniz gereken 3 şey (doğrulanmış)

1. **Cihaz akışı (TV kodu) YouTube'da yalnız `youtube` ve `youtube.readonly` kapsamlarına izin veriyor.**
   Video yükleme, thumbnail ve oynatma listesi bu kapsamla çalışır. **Altyazı yükleme (captions.insert) çalışmaz**
   (o yöntem yalnız `youtube.force-ssl` kabul ediyor). Altyazı: YouTube Studio'dan elle (araç hazır klasör verir)
   ya da yükleme betiği Niyazi'nin bilgisayarında `--akis yerel` ile çalıştırılır (aşağıda, Ek B).
2. **Denetim (audit) kilidi belirsiz.** 2020 duyurusu: 28 Temmuz 2020 sonrası açılan, denetimden geçmemiş projelerden
   yüklenen videolar "özel" kilitlenir. Ancak videos.insert başvuru sayfasının güncel hali (2026-10-15) tersini
   yazıyor: *"Videos uploaded from unverified API projects are not restricted to private viewing mode."*
   Duyuruyu geri alan bir sürüm notu bulunamadı. Bu yüzden önce **tek bir test yüklemesi** yapılır (Adım 8);
   kilit çıkarsa denetim başvurusu yapılır (Adım 9), o zamana kadar `--manuel-paket` ile Studio'dan yüklenir.
3. **Kota:** varsayılan günde 100 videos.insert çağrısı + diğer yöntemler için 10.000 birim
   (thumbnails.set ≈50, playlistItems.insert 50, captions.insert 400). Bizim ihtiyacımız (günde 1 uzun + 2 Shorts) bunun
   çok altında; kota için denetime gerek yok.

## Adım 1 — Google Cloud projesi (2 dk)
1. Telefonda Chrome → https://console.cloud.google.com/projectcreate (kanalın sahibi olan Google hesabıyla giriş).
   Ekran dar gelirse Chrome menüsü → "Masaüstü sitesi".
2. Proje adı: `financial-rise-yayin` → **Oluştur**. Faturalandırma hesabı gerekmez (YouTube Data API ücretsiz).
3. Proje numarasını not edin (ana sayfadaki "Proje bilgisi" kartı; denetim formunda istenir).

## Adım 2 — YouTube Data API v3'ü etkinleştir (30 sn)
https://console.cloud.google.com/apis/library/youtube.googleapis.com → üstte doğru proje seçili → **Etkinleştir**.

## Adım 3 — OAuth onay ekranı (Google Auth Platform) (3 dk)
1. https://console.cloud.google.com/auth/overview → **Başlayın / Get started**.
2. Uygulama adı: `Financial Rise Publisher` (**adında "YouTube" geçmemeli** — YouTube politikası).
   Destek e-postası: kendi adresiniz.
3. Kitle (Audience): **External / Harici**. İletişim e-postası: kendi adresiniz → koşulları kabul → **Oluştur**.
4. https://console.cloud.google.com/auth/audience → Yayın durumu **Testing / Test** olarak kalsın →
   **Test kullanıcıları → Kullanıcı ekle** → kanalın sahibi Google hesabınızın e-postası → Kaydet.
5. (Önerilir) Aynı menüde **Veri erişimi / Data Access** → **Kapsam ekle** →
   `https://www.googleapis.com/auth/youtube` (ve Ek B kullanılacaksa `.../auth/youtube.force-ssl`) → Kaydet.

Not: Uygulama "Test" durumunda ve doğrulanmamış olduğu için izin ekranında *"Google bu uygulamayı doğrulamadı"*
uyarısı çıkar; test kullanıcısı olarak **Devam**'a basabilirsiniz. Uygulama yalnız sizin hesabınızda çalışır.

## Adım 4 — Cihaz türü OAuth istemcisi (1 dk)
1. https://console.cloud.google.com/auth/clients → **İstemci oluştur / Create client**.
2. Uygulama türü: **TVs and Limited Input devices** (TV'ler ve Sınırlı Giriş cihazları). Ad: `yayin-cihaz` → **Oluştur**.
3. Açılan pencerede **İstemci kimliği** ve **İstemci sırrı** görünür. Bunları **sohbete yapıştırmayın**; doğrudan
   Adım 5'teki ayara kopyalayın. (Sır sonradan yalnız bir kez gösterilebilir; kaybolursa yeni sır eklenir.)

## Adım 5 — Ortam değişkenleri (1 dk)
Bulut ortamının ayarında, `YOUTUBE_API_KEY`'i eklediğiniz yere (ortam değişkenleri / secrets) iki satır ekleyin:
```
YOUTUBE_OAUTH_CLIENT_ID=<istemci kimliği>
YOUTUBE_OAUTH_CLIENT_SECRET=<istemci sırrı>
```
Yeni oturum açılınca değişkenler gelir. Sistem bunların varlığını yalnız "var/yok" olarak kontrol eder, değeri yazdırmaz.

## Adım 6 — Her yayında ne olur (30 sn)
1. Hakem son kontrolü + sizin "onaylıyorum" mesajınızdan sonra paketteki `onay.niyazi_onayi` true yapılır
   (araç bu alan false iken yüklemeyi reddeder).
2. Sistem `python3 tools/yayin/yukle.py uretim/<klasör>/yayin-paketi.json` çalıştırır ve size şunu gösterir:
   `Telefondan aç: https://www.google.com/device  ·  Kodu gir: ABCD-EFGH`
3. Telefonda o adresi açın → kodu girin → kanal sahibi hesabı seçin → kanal bir **Marka Hesabı** ise kanalı seçin →
   "doğrulanmamış uygulama" uyarısında **Devam** → izin ver. Kod 30 dk geçerlidir.
4. Video `private` + planlı yayın saatiyle yüklenir, thumbnail ve (varsa) oynatma listesi eklenir; token iptal edilir.
   Altyazı cihaz akışında yüklenemediği için YAYIN.md'deki adımla Studio'dan eklenir (ya da Ek B).

## Adım 7 — Telefon izin geçmişi (isteğe bağlı)
İzni istediğiniz an kaldırmak için: https://myaccount.google.com/permissions → Financial Rise Publisher → Erişimi kaldır.

## Adım 8 — İlk test yüklemesi (kilit kontrolü, 2 dk)
Pilot klip (`uretim/ses-testi/yayin-paketi.json`, 19 sn) **private** ve planlama olmadan yüklenir; ardından Studio'da
görünürlüğü "Liste dışı"na çevirmeyi deneyin. Çevrilebiliyorsa kilit yok → denetim gerekmez. "Bu video özel olarak
kilitlendi" e-postası/uyarısı gelirse Adım 9. Test videosu sonra silinir. (Bu adım da sizin onayınızla yapılır.)

## Adım 9 — YouTube API Services denetim başvurusu (yalnız kilit çıkarsa, 15 dk)
Form: https://support.google.com/youtube/contact/yt_api_form ("Audit and Quota Extension Form").
Formun istediği ve bizde henüz olmayanlar: **herkese açık bir Gizlilik Politikası URL'si** (ör. Google Sites'ta tek
sayfa) ve yükleme akışını gösteren **uçtan uca ekran kaydı** *veya* **çalışan tam yükleme betiği** (bizde var:
`tools/yayin/yukle.py`). Aşağıdaki taslaklar İngilizce (form İngilizce); köşeli parantezleri doldurun.

| Alan | Taslak cevap |
|---|---|
| Request type | Complete a compliance audit to request for additional quota (formdaki tek uygun seçenek; ek kota istemeyin → "No change / Default quota") |
| Applying as | As an individual user |
| Organization's legal name / Parent company | self |
| Primary website | https://www.youtube.com/@[kanal-tanıtıcısı] |
| Category | Education and E-Learning |
| Organization size | Independent Developer/Sole Proprietor |
| Describe your work as it relates to YouTube | "I run the Financial Rise YouTube channel, which publishes original long-form animated videos (10–14 minutes) explaining financial news, historical financial events and possible future scenarios for a general, global audience. The API client is a private, single-user command-line tool that uploads my own finished videos to my own channel: it inserts the video as private with a scheduled publish time, sets the custom thumbnail, uploads my caption file and adds the video to my playlist. It does not access, store or display any other user's data, and it is not offered to anyone else." |
| Target audience | Internal Users |
| Monetization | Free service (we do not charge users) |
| Google representative | No, I do not have a Google representative |
| Learned about the API | Google Developer Documentation |
| API Client name | Financial Rise Publisher ("YouTube" kelimesi yok) |
| Primary access URL | https://www.youtube.com/@[kanal-tanıtıcısı] (araç herkese açık değil) |
| Privacy policy URL | https://[gizlilik sayfası] |
| Publicly accessible? | No — internal single-user tool. Demo hesap yerine ekran kaydı/betik sunulur. |
| Project number | [Adım 1'deki numara] |
| Use case | Internal Company Tool + Video Uploading & Account Management |
| Users sign in with Google (OAuth)? | Yes — only the channel owner, via the OAuth 2.0 device authorization flow; access tokens are kept in memory only, never stored, and revoked after each upload. |
| Expected usage | Fewer than 1,000 requests per day |
| Endpoints | youtube.videos.insert, youtube.thumbnails.set, youtube.captions.insert, youtube.playlistItems.insert, youtube.videos.list |
| Quota | No change / Default quota |
| Data usage (gerekirse açıklama) | "The tool only writes my own content to my own channel and reads back the upload status of the video it just uploaded. No YouTube data is stored, aggregated, shared or displayed to third parties. No derived metrics." |
| Evidence | Privacy policy ekran görüntüsü; OAuth izin ekranı ve google.com/device ekran görüntüleri; tam betik (`tools/yayin/yukle.py` + `yayin_api.py`) veya yükleme akışının ekran kaydı |

## Ek A — Manuel yayın (API olmadan, her zaman çalışır)
Sistem `python3 tools/yayin/yukle.py <paket> --manuel-paket` ile `uretim/<klasör>/yayin-manuel/` üretir:
`video.mp4`, `thumbnail.jpg`, `altyazi-en.srt`, `YAYIN.md` (başlık/açıklama/etiket/bölüm kutuları + ayar tablosu).
studio.youtube.com (bilgisayar tarayıcısı önerilir) → Oluştur → Video yükle → YAYIN.md'yi sırayla kopyala-yapıştır.

## Ek B — Altyazı dahil tam otomatik (Niyazi'nin bilgisayarında)
Cihaz akışı altyazı kapsamı vermediği için alternatif: Adım 4'te ikinci bir istemci **Masaüstü uygulaması (Desktop app)**
oluşturulur; bilgisayarınızda repo + Python 3 ile ortam değişkenleri bu istemcinin değerleriyle ayarlanıp
`python3 tools/yayin/yukle.py uretim/<klasör>/yayin-paketi.json --akis yerel` çalıştırılır. Tarayıcı açılır, izin
verilir (127.0.0.1 geri dönüşü + PKCE), `youtube.force-ssl` ile altyazı da yüklenir. Video dosyasının bilgisayarda olması
gerekir; bu yüzden varsayılan yol cihaz akışı + Studio'dan altyazıdır.

## Kaynaklar (2026-10-26 okundu)
- Konsol adresleri (auth/overview, auth/audience, auth/clients): https://support.google.com/cloud/answer/15549257 ve https://support.google.com/cloud/answer/15549945
- Cihaz akışı ve izinli kapsamlar: https://developers.google.com/identity/protocols/oauth2/limited-input-device ("Allowed scopes")
- videos.insert (kapsamlar, publishAt, doğrulanmamış proje notu): https://developers.google.com/youtube/v3/docs/videos/insert
- captions.insert (yalnız youtube.force-ssl / youtubepartner): https://developers.google.com/youtube/v3/docs/captions/insert
- thumbnails.set: https://developers.google.com/youtube/v3/docs/thumbnails/set · playlistItems.insert: https://developers.google.com/youtube/v3/docs/playlistItems/insert
- Alan sınırları (başlık 100, açıklama 5000 bayt, etiket 500): https://developers.google.com/youtube/v3/docs/videos
- 2020 kilit duyurusu ve kota değişiklikleri: https://developers.google.com/youtube/v3/revision_history
- Kota ve denetim: https://developers.google.com/youtube/v3/guides/quota_and_compliance_audits
- Denetim formu: https://support.google.com/youtube/contact/yt_api_form
- Değiştirilmiş/yapay içerik beyanı: https://support.google.com/youtube/answer/14328491
- Geliştirici politikaları: https://developers.google.com/youtube/terms/developer-policies
