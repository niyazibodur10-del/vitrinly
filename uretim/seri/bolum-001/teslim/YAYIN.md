# YAYIN — Flip By Vote · Bölüm 1 "Every Dollar We Have"

Dosyalar (bu klasör): `bolum-001.mp4` (83,2 sn, 1080x1920, sha256 23839dd0b183) · `kapak-1080x1920.jpg` · `kapak-1080x1350.jpg` · `yayin-paketi.json` · `platform-metinleri.md` (kopyalanacak tüm metinler).
YouTube yüklemesini biz yaparız. Instagram ve TikTok bağlanana kadar elle paylaşılır.

## Yayın saati önerisi: 12:00 ET (17:00 UTC, 20:00 Türkiye) — üç platformda aynı anda
- ABD'de iki kıyı da uyanık: Doğu'da öğle arası, Batı'da 09:00. Platformların ilk dağıtım testi ilk birkaç saatte olur; bu saatte iki kıyının akşam yoğunluğu da ilk 6–9 saate girer.
- 24 saatlik yorum penceresi ertesi gün 12:00 ET'de kapanır. Böylece pencere bir tam ABD akşamını ve bir sabahı kapsar.
- Kanalın mevcut saatiyle aynı (takvim v2: 12:00 ET). Her gün aynı saatte yayın alışkanlık yaratır.
- Kanıt düzeyi: [tahmin]. Bu kanalın Shorts/Reels saat verisi yok, bu yüzden 7 bölüm sonra kanal-analisti verisiyle yeniden bakılır. Elenen seçenek 18:00 ET: pencere Türkiye saatiyle 02:00'de kapanır ve sonraki bölümün üretimine yetişmez.
- Risk: Bölüm 2'nin üretimi pencere kapandıktan sonra başlarsa ertesi gün aynı saate yetişmeyebilir. Bu takvim kararı koordinatörde.

## A. Yayından önce (bir kez, kanal)
1. **YouTube Studio → Özelleştirme → Temel bilgiler**
   - Ad: `Flip By Vote`
   - Tanıtıcı: `@flipbyvote`. Eski @toonomy bir süre başkası tarafından alınamaz, sonra serbest kalır [ön bilgi].
   - Profil resmi: `uretim/kanal-kimligi/flipbyvote-profil-800.png`. Videodaki "FOLLOW" kartının avatarıyla aynıdır; aynı görseli Instagram ve TikTok'ta da kullan.
   - Banner: eski "TOONOMY · NEW VIDEOS EVERY WEEK" banner'ını **kaldır**. Eski adı ve gün sözünü taşıyor. Yeni banner görseli hazır olunca API ile yüklenir; metni `flipbyvote-kanal-paketi.json` → `banner_metni`.
2. **Kanal açıklaması ve anahtar kelimeler:** `uretim/kanal-kimligi/flipbyvote-kanal-paketi.json` taslağına onay ver. Sonra koordinatör `kanal.py` fark raporunu çalıştırır, ardından `--uygula --onayli` ile uygular. "Season 1" listesi Bölüm 1 yüklendikten sonra açılır.

## B. Bölüm 1 yayını
3. **Bitmiş videoyu ve yayın saatini onayla.** Koordinatör pakete `onay.niyazi_onayi=true` ve `yayin_zamani`'nı yazar (ör. `2026-11-12T12:00:00-05:00`), sonra `yukle.py` ile planlı ve private yükler. Videodaki ayarlar: made for kids **Hayır** · altered/synthetic **Evet** · kategori Entertainment · dil en.
   - Planlı videoda Studio'da görünürlük ve plan alanına **dokunma**.
   - Shorts kapağı: API ile yüklenen Short'ta kareyi YouTube seçer. Uygulamada kare seçimi açılırsa **1:21** (81,00 sn, kare 2430; alternatif 0:00, 0,10 sn)'i seç [doğrulanmadı].
4. **Instagram Reels** (aynı saatte, elle):
   - Video: `bolum-001.mp4`
   - Açıklama: `platform-metinleri.md` → Instagram
   - Kapak: "Edit cover" → "Add from camera roll" → `kapak-1080x1920.jpg`
   - Profil ızgarası: kırpımı `kapak-1080x1350.jpg` ile ayarla. Yazılar 4:5 ve 3:4 kırpımının ikisinin içinde kalıyor.
   - Advanced settings → **AI label AÇIK**
   - Müzik ekleme: platform müziği **kullanma**. Videonun sesi kendi üretimimiz.
5. **TikTok** (aynı saatte, elle):
   - Video ve açıklama: `platform-metinleri.md` → TikTok
   - Kapak: `kapak-1080x1920.jpg`
   - "AI-generated content" **AÇIK**
   - Platform müziği yok.

## C. Yayından hemen sonra
6. **Sabit yorum:** metin `platform-metinleri.md` içinde, üç platformda aynı.
   - YouTube: yorumu sistem gönderir, sen uygulamadan sabitlersin.
   - Instagram ve TikTok: yorumu kendin yazıp sabitlersin.
   - Private ya da planlı videoya yorum sabitlenemez; yorum açılıştan sonra gönderilir.
7. **TikTok yorumlarına otomatik yanıt verilmez** (politika §5). Yanıtı ya sen verirsin ya hiç verilmez. YouTube ve Instagram yanıtlarını sistem gönderir: bölüm başına en fazla 20 yanıt, finans tavsiyesi yok.
8. **Pencere kapanınca kazanan seçilir:** 24 saat sonra, 12:00 ET'de. Kazanana tek bildirim gider; kullanıcı adı yalnız vazgeçme yoluyla gösterilir (politika §4).
