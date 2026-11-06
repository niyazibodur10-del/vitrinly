# YAYIN — "You Have $1,000 in 1929. Can You Keep It?" + 2 Shorts (TASLAK, teslim için)

**Hazırlayan:** youtube-paketleyici · 2026-10-27 · Koordinatör F10'da `teslim/`e kopyalar. Paketler: `yayin-paketi.json`, `yayin-paketi-shorts-1.json`, `yayin-paketi-shorts-2.json` (yollar `../08-kurgu/`, `../09-paket/` → `teslim/`den de geçerli).
**Kural:** hiçbir adım Niyazi onayı olmadan yapılmaz. Onaydan sonra API adımlarını koordinatör, Studio adımlarını (API'de karşılığı yok veya doğrulanmadı) Niyazi ya da Niyazi'nin izniyle koordinatör yapar. Yorum yazmak ve yanıtlamak dışarıya mesajdır, yalnız Niyazi yapar.

## 0. Takvim (Pazar A slotu, takvim v2)

| Video | Dosya | Yayın (ET) | UTC | TRT | Gizlilik → planlı |
|---|---|---|---|---|---|
| Uzun (10:31,6) | `08-kurgu/final-16x9.mp4` | **Çar 28.10.2026 12:00 EDT** | 16:00 | **19:00** | private + publishAt |
| Shorts 1 (49,6 sn) | `08-kurgu/shorts-1.mp4` | Pzt 02.11.2026 09:00 EST | 14:00 | 17:00 | private + publishAt |
| Shorts 2 (56,0 sn) | `08-kurgu/shorts-2.mp4` | Sal 03.11.2026 09:00 EST | 14:00 | 17:00 | private + publishAt |

- Uzun video 28.10 yaz saatinde → **UTC−4** (`-04:00`); ABD 1 Kasım'da kış saatine geçer → Shorts **UTC−5** (`-05:00`). Takvim Niyazi onayıyla (2026-10-28) Pazar slotundan bugüne alındı.
- **Onay:** Niyazi 28.10.2026'da bugünkü yayını onayladı. Yükleme slottan önce yapılmalı (işleme payı); slot kaçarsa koordinatör `yayin_zamani`'yı yeni saate alır. Shorts hiçbir zaman uzun videodan önce yayınlanmaz.

## 1. Yükleme (API — koordinatör, Niyazi "yayınla" dedikten sonra)

1. Üç pakette `onay.niyazi_onayi: true`, `onay.tarih: <bugün>`.
2. Önce kuru çalıştırma (0 hata beklenir): `python3 tools/yayin/yukle.py <paket> --dry-run`.
3. Sırayla uzun video, Shorts 1, Shorts 2: `python3 tools/yayin/yukle.py <paket>`. Araç başlığı, açıklamayı (bölümler dahil), etiketleri, kategoriyi (27), dili (en), çocuklara özel = hayır, **AI beyanını (`containsSyntheticMedia: true`)**, planlı yayın zamanını ve uzun videoda ana thumbnail **A2**'yi gönderir.
4. Video ID'leri `yayin-sonucu.txt`'ye düşer. SRT cihaz akışında **yüklenmez** → adım 2.2.

## 2. Studio adımları — uzun video (yüklemeden hemen sonra, yayından önce)

studio.youtube.com, bilgisayar tarayıcısı → İçerik → video.

1. **AI beyanı kontrolü:** Ayrıntılar → "Değiştirilmiş veya yapay içerik" (Altered content) = **Evet** olmalı (API gönderdi; Studio'da gözle doğrula). Açıklamadaki "Narration voice is AI-generated…" satırı yerinde.
2. **Altyazı:** Altyazılar → Dil: İngilizce → Dosya yükle → **Zamanlamalı** → `08-kurgu/final.en.srt` (228 blok, 10:31,6'ya kadar). Otomatik altyazı yerine bu yayınlanır.
3. **Thumbnail Test & Compare:** Ayrıntılar → Küçük resim → **Test & compare** → `09-paket/thumbnail/A2-kapilar.jpg` (ana, yüklü), `B1-kutu.jpg`, `D1-kilitler.jpg`. Ölçüt Studio'nun "izlenme süresi payı". Seçenek görünmüyorsa (özellik kanal/hesap erişimine bağlı olabilir, bu kanalda doğrulanmadı): A2 kalır, B1/D1 F12'de CTR düşükse elle denenir.
4. **Uç ekran:** Düzenleyici → Bitiş ekranı → **10:18,4 → 10:31,6 (~13 sn)**, S24 "Falling prices made a shoebox the winner…" ile başlar. Öğeler: **Abone ol** + **Video: "İzleyici için en uygun"**. Kutular sağ yarıya (Leo solda, sağ taraf bu iş için boş bırakıldı). "THANKS FOR PLAYING" yazısının üstüne gelmesin; önizlemede bak.
5. **Kart:** yok (kanalda bağlanacak ikinci video yok).
6. **Bölümler:** açıklamadan otomatik (00:00 / 01:19 / 02:46 / 04:46 / 06:12 / 07:33 / 08:42 / 09:52; kurgu ofseti 0). Yayından sonra izleme sayfasında ilerleme çubuğunun 8 parçaya bölündüğüne bak.
7. **Reklam uygunluğu öz beyanı:** `09-paket/politika-raporu.md` §5'teki yanıtlar (tümü "None"). Kanal henüz YPP'de değilse bu ekran çıkmayabilir; çıkınca aynı yanıtlar.
8. **Kontroller sekmesi:** telif/uygunluk uyarısı yok olmalı. "Tension" (Komiku) için iddia gelirse Niyazi onayıyla itiraz; kanıt politika-raporu §5'te.

## 3. Oynatma listeleri (koordinatör, `tools/yayin/kanal.py`)

- Uzun video yüklenince **"The Collapse: Financial History Explained"** listesi açılır ve video eklenir (boş liste kuralı: listeyi bu video açar). Liste ID'si pakete (`oynatma_listesi_id`) ve `uretim/kanal-kimligi/mevcut-durum.md`'ye yazılır.
- Shorts 1 ve 2 → **"Money Stories in 60 Seconds | Shorts"** (ilk Shorts bu listeyi açar).
- "Start Here: Best of Toonomy" henüz açılmaz (3 sütundan birer video gerekir).

## 4. Studio adımları — Shorts

1. **AI beyanı:** her Short'ta "Altered content" = Evet (API gönderdi; gözle doğrula).
2. **Related video (uzun videoya bağlantı):** Data API karşılığı doğrulanmadı → Studio → İçerik → **Shorts** → Short → Ayrıntılar → **İlgili video** → "You Have $1,000 in 1929. Can You Keep It?".
   - **Zaman penceresi:** uzun video herkese açık olduktan sonra (01.11 20:00 TRT) ve Shorts 1 yayınlanmadan önce (02.11 17:00 TRT). Planlı/özel videonun listede çıkıp çıkmadığı doğrulanmadı, bu yüzden 01.11 akşamı yapılır.
   - Shorts 2 için de aynı adım (03.11 17:00 TRT'den önce).
3. Shorts açıklamalarında uzun videonun adı + kanal bağlantısı zaten var. URL bilerek yazılmadı (ID yüklemeden önce yok).

## 5. Yayından sonra (ilk 48 saat)

- **Pinli yorum:** Niyazi kanal hesabıyla `paket.md` §7'deki metni yorum olarak yazar → ⋮ → **Sabitle**.
- **Yorum yanıtları:** `09-paket/yorum-yanitlari.md` (10 tür). Yanıtları Niyazi onaylar ve gönderir; spam yanıtlanmaz, gizlenir/bildirilir.
- **Engellenen kelimeler önerisi** (Studio → Ayarlar → Topluluk): whatsapp, telegram, mentor, "dm me", signal.
- **Kontrol:** bölümler görünüyor, altyazı İngilizce seçili, uç ekran öğeleri doğru videoyu gösteriyor, Shorts'ta "ilgili video" bağlantısı görünüyor.
- **F12:** 48 sa / 7 g / 28 g → kanal-analisti raporu (CTR, AVD, Test & Compare sonucu, yorum türleri).

## 6. Kuru çalıştırma kanıtı (2026-10-27, gerçek F7 dosyaları, yükleme yok)

`09-paket/kapi-cikti.txt`: üç paket **0 hata, exit 0**. Uzun: 1920x1080, 631,6 sn, A2 1280x720 jpeg, SRT 228 blok, 8 bölüm kurallara uygun, açıklama 3.370/5.000 bayt. Shorts 1: 1080x1920, 49,6 sn. Shorts 2: 1080x1920, 56,0 sn. Planlı yayın zamanları gelecekte. `paket-kontrol.py` 0 hata.
