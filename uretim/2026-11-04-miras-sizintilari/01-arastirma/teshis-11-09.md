# Teşhis: "videolar neredeyse izlenmedi" (@toonomy, 6 herkese açık video)

İLERLEME: tamam · Hazırlayan: kanal-analisti · **Ölçüm: 2026-11-09 07:18 UTC** [API] · ham `olcum/kendi-2026-11-09.json` (sha256 cdff8d0245ea, `olcum/kendi2.py`) · yaşıt kohort `olcum/kohort-2026-11-09.json` (2cec7fba1ca1, `olcum/kohort.py` + `olcum/kohort_analiz.py`)
Veri yolu: yalnız YouTube Data API v3. **Gösterim, CTR, AVD, tutma eğrisi, trafik kaynağı, abone kaynağı, Test & Compare: ÖLÇÜLEMEDİ** (`yt-analytics.readonly` kapsamı yok, Studio CSV gelmedi). Bu yüzden "gösterim mi, tıklama mı, tutma mı" sorusu **uzun videolar için ayırt edilemiyor**; aşağıda tahmin yoktur, yalnız sayımla ayırt edilebilenler var. [AÇK]

**ÖZET**
1. 12 günde 6 video, kanal toplamı 601 izlenme [API], abone **3 → 3** (10-28'den beri net 0) [API]. Organik yorum 0/6 video [API].
2. 1929 uzun video 208 izlenmede **5 gündür sabit** (0/gün); ilk 4,8 günde ~42/gün aldı, sonra kesildi [API][H]. S08 uzun video 5,8 günde **5 izlenme** [API].
3. Yaşıt kohort (ilk yüklemesi ≥2026-07-01, ≤25 videolu 122 İngilizce niş kanal, 3–21 günlük 400 uzun video): **medyan 57 izlenme**, kanalların medyan abonesi 7 [API][H]. 1929 bu dağılımda **%67'lik dilimde** (ortalamanın üstü), S08 **%9'luk dilimde** [H]. Yani "hiç izlenmedi" kanal düzeyinde yeni kanal tabanı; **asıl zayıf olan S08 ve Shorts köprüsü**.
4. Ayırt edilebilen tek kopuş: Shorts→uzun köprüsü. 1929 Shorts'u 342 izlenme aldı, aynı sürede uzun video +5 (≤%1,5) [API][H]. 4 Shorts açıklamasında uzun videoya bağlantı 0 [API: snippet.description]; Studio "Related video" yapıldığına dair kayıt yok (durum.md'lerde "Niyazi'ye kalan" listesinde duruyor) [AÇK].
5. **Erken yayın hatası 2/2 uzun videoda var** (önceki raporlar yalnız S08'i yakalamıştı): 1929 publishedAt 10-28 09:37:48Z (plan 16:00Z, 6 sa 22 dk erken), S08 11-03 12:00:11Z (plan 11-04 17:00Z, 29 sa erken). 4/4 Shorts tam planlı saatte açıldı [API][AÇK: teslim/yayin-sonucu.txt]. 3 aboneli kanalda etkisi küçük [T], ama süreç hatası.
6. En büyük tek eksik ölçüm: Analytics kapsamı. Niyazi'nin tek seferlik yeniden yetkisi (≈2 dk, ücretsiz) olmadan CTR/AVD dersi yazılamaz; bu, listenin 1. maddesi. [T]

## 1. Güncel veri ve izlenme eğrisi (anlık sayımlar) [API]
| Video | Tür, süre | Yayın (UTC) | Sayım (yaş, gün → izlenme) | İzlenme/gün (bugün) [H] | Beğeni | Organik yorum |
|---|---|---|---|---|---|---|
| BVJwZ1C9R1U 1929 "You Have $1,000 in 1929. Can You Keep It?" | uzun 10:32 | 10-28 09:37 | 4,8 g → 203 · 6,8 g → 208 · 11,9 g → 208 | ömür 17,5; son 5 g **0** | 1 (%0,5) | 0 (1 = kendi sabit yorumumuz) |
| QFC8GdDTW2c "$1,000 in 1929: Which Door Would You Pick?" | Shorts 0:50 | 11-02 14:00 | 1,6 g → 341 · 6,7 g → 342 | ömür 50,9; son 5 g **0,2** | 5 (%1,5) | 0 |
| 6LQGcQg4hpk "Same Box of Cash, Opposite Result: 1932 vs 2026" | Shorts 0:57 | 11-03 14:00 | 0,6 g → 22 · 5,7 g → 23 | 4,0 | 0 | 0 |
| ghLjMbrweCw S08 "If America Earned $5,400 a Month, Here's Its Budget" | uzun 11:19 | 11-03 12:00 | 0,7 g → 2 · 5,8 g → 5 | 0,9 | 1 | 0 |
| YLZQj6ecYE4 "Interest vs. the Military: Which US Bill Is Bigger?" | Shorts 0:58 | 11-05 14:00 | 3,7 g → **1** | 0,3 | 0 | 0 |
| 2kaz6kXdZlw "US Debt Was Bigger Than the Economy in 1946. What Happened?" | Shorts 0:42 | 11-07 14:00 | 1,7 g → 22 | 12,8 | 0 | 0 |
Kanal: 3 abone, 599 toplam izlenme (sayaç gecikmeli; video toplamı 601), 6 görünür video, kanal oluşturma 2013-09-11 [API]. Önceki sayımlar: `olcum/kendi-2026-11-04.json`, `uretim/2026-10-26-1929-1000-dolar/10-yayin-sonrasi/olcum/olcum-2026-11-02.json`.
**YPP:** 3/1.000 abone [API]; herkese açık uzun video izlenme saati ölçülemedi, tahmin ~11–18 saat / 8.000 [T: 213 uzun izlenme × 3–5 dk]. Shorts saatleri sayılmaz.

## 2. Yaşıt kıyas (aynı yaştaki benzer kanallar) [API][H]
`kohort.py`: 4 niş sorgusu × orta/uzun süre, publishedAfter 2026-10-01 → 336 aday kanal → ilk herkese açık yüklemesi ≥2026-07-01 ve ≤25 video → 122 kanal (İngilizce, ≥8 dk). Arama sonucu olduğu için kohort hafif **yukarı yanlı** (hiç görünmeyen kanallar yok) [T].
| Ölçü | Kohort | Biz |
|---|---|---|
| 3–21 günlük uzun video izlenmesi (n=400, 96 kanal) | medyan 57 · p25 12 · p75 407 · 1.165 üstü 54/400 | 1929: 208 (%67) · S08: 5 (%9) |
| Kanalın ilk uzun videosu (ömür boyu, n=122) | medyan 67,5 · 208 altı 89/122 | 208 |
| Abone (n=122) | medyan 7 · ≤10 abone 70/122 | 3 |
| ≥1.000 izlenmeli video çıkaran kanal, uzun video sayısına göre | 1–5 video: 9/74 (%12) · 6+ video: 22/48 (%46) | 2 uzun video |
| Shorts yükleyen / yüklemeyen kanalda ≥1.000'lü video oranı | 8/42 (%19) / 23/80 (%29) | 4 Shorts |
| Uzun video süresi medyanı | ≥1.000 olanlar 19,6 dk (n=84) · diğerleri 17,3 dk (n=606) | 10,5–11,3 dk |
Okuma [T]: 6+ video ile başarı arasındaki ilişki kısmen ters nedensellik (izlenen kanal yüklemeye devam eder). Shorts farkı korelasyon, nedensellik değil. Yine de iki sinyal de "uzun videoya kapasite" yönünde. 11-02 raporundaki "genç rakip ilk video medyanı 2.853" hayatta kalan yanlıydı (yalnız ≥1.000 aboneliler); doğru taban bu kohort.

## 3. Teşhis: nedenler kanıt sırasıyla
| # | Neden | Veriyle ayırt edilebilir mi? | Kanıt | Düzey |
|---|---|---|---|---|
| 1 | **Soğuk kanal tabanı** (3 abone, bildirim kitlesi yok, 2 uzun video) | Evet, kohortla | 1929 kohort medyanının 3,6 katı; kohortun yarısı ≤7 abone [API][H] | Güçlü |
| 2 | **Test dalgası sonrası dağıtım durdu** (1929: 4,8 g ~42/gün → 0) | Kısmen: düşüş görülüyor; nedeni (CTR mı AVD mi) **görülmüyor** | Eğri §1 [API]. Yeni videoya ilk gösterim grubu verilip yanıt zayıfsa kesilir [T] | Orta |
| 3 | **S08 konu/paket zayıf** (B haber sütunu, $ rakamlı başlık) | Hayır (gösterim mi tıklama mı bilinmiyor) | 5 izlenme = kohort %9 [H]; niş 90 g: başlıkta Rakam/$ 0,95x, gündem kelimesi avantajsız 1,00x↔1,09x [AÇK: `rakip-ozet.md`, ortak-dersler 2026-11-04]; n=1 | Orta-zayıf |
| 4 | **Shorts köprüsü yok** | Evet | 342 Shorts → uzun +5 (≤%1,5) [API][H]; açıklamada bağlantı 0/4 [API]; Related video kaydı yok [AÇK] | Güçlü |
| 5 | **Shorts akışı bizi seçmiyor** | Evet (Shorts'ta izlenme ≈ akış gösterimi) | 342 / 23 / 1 / 22: 4 Shorts'tan 1'i akış testini geçti, YLZ 3,7 günde 1 izlenme [API] | Orta |
| 6 | **Thumbnail tek tip** (Leo aynı şaşkın yüz) | Hayır (CTR yok) | S08 A1 ve miras K1/K4'te aynı "ağzı açık" yüz [GÖZ]; en iyi giden 1929 A2'de sahne + işaret eden, sakin Leo [GÖZ]; n=2 → zayıf kanıt | Zayıf |
| 7 | Etkileşim sinyali yok | Evet | beğeni/izlenme 1929 %0,5, QFC %1,5 (genel referans %2–4 [ÖB]); organik yorum 0/601 izlenme [API][H] | Orta |
| 8 | Kanal geçmişi (2013 hesabı, 2025-07'den 4 gizli eski video, ad değişimi) | Hayır | Oluşturma 2013-09-11 [API]; gizli videolar dağıtımı etkilemez denebilir ama ölçülemedi [T] | Zayıf |
| 9 | AI ses / inauthentic algısı | Hayır (AVD yok, yorum yok) | YouTube: "Disclosing AI content alone won't limit a video's audience" (support.google.com/youtube/answer/14328491, WebFetch 2026-11-09) [AÇK] → **beyan erişimi düşürmez**; sesin tutmaya etkisi ölçülemedi | Bilinmiyor |
| 10 | Erken public (2/2 uzun) | Evet (saat sapması) | §1; 3 abonede ilk saat kitlesi yok → izlenmeye etkisi küçük [T] | Süreç hatası |
| 11 | Tempo (Paz 11-08 slotu kaçtı; 12 günde 2 uzun) | Kısmen | Plan 2/hafta; gerçek 1,2/hafta [H]; kohortta 6+ video %46 vs ≤5 %12 [H] | Orta |
| 12 | Yayın saati/günü | Hayır | 3 abonede saat etkisi kanıtlanamaz; 1929 05:37 ET, S08 Salı 07:00 ET'de açıldı [API][H] | Zayıf |
**Erken public kök neden (ölçülemedi, 2 hipotez) [T]:** (a) Studio'da yapılan bir iş (Test & Compare yalnız public videoda kurulur, `ortak-dersler` Politika §) görünürlüğü "Public"e çekti; (b) Studio'da plan saati yanlış tarih/saat dilimiyle yeniden girildi (S08'in :00:11 saniyesi planlı açılış izi taşıyor; 1929'un 09:37:48'i taşımıyor). Yükleme anındaki publishAt doğru (`uretim/2026-10-28-yeni-video/teslim/yayin-sonucu.txt`) → araç yükleme anında doğru yazıyor.

## 4. (a) Miras videosu: yayından ÖNCE
| # | Ne | Sahibi | Beklenen etki | Kanıt | Maliyet |
|---|---|---|---|---|---|
| a1 | **Başlık:** T1 "The Great Wealth Transfer Has a Leak" kalsın (aranan kavram ilk 25 krk; soğuk kanalda arama tek güvenilir kapı). Açıklamanın ilk 2 satırında "Great Wealth Transfer" + "inheritance" geçsin | youtube-paketleyici | arama gösterimi ↑ [T] | Orta: 1929/S08'de arama kavramı yoktu [GÖZ]; T3 yedek | 0 |
| a2 | **Thumbnail:** K1'deki Leo yüzü S08 A1 ile aynı şaşkın ifade → farklı ifade/poz (1929 A2 gibi sahne + eylem); delikten akan para ve kamyon/kutu ana nesne, yüz ikincil. K1 yapısı (soru + $124T) korunur, Test & Compare sırası değişmez | thumbnail-tasarimcisi (Leo kesiti: gorsel-varlik-sanatcisi) | CTR ↑ bilinmiyor; kanal tek tipliği ↓ | Zayıf (n=2, CTR yok) [GÖZ] | 1 tur, Canva 0 ₺ |
| a3 | **İlk 30 sn:** değiştirme. Tutma verisi yokken yeniden TTS+render pahalı ve kanıtsız. Yalnız kontrol: 0–3 sn görsel ödül ve başlık = thumbnail = hook tek vaat (metin §1 bunu karşılıyor) | hakem (kontrol) | — | Ölçülemedi | 0 [T] |
| a4 | **Shorts:** Related video → uzun video, Shorts açılmadan **önce** Studio'da; Niyazi ekran görüntüsü atar, durum.md'ye yazılır. Shorts sonu "cevap uzun videoda" açık sorusuyla bitsin. Shorts uzun videodan **sonra** (+1 g, +3 g) | Niyazi (Studio) · kurgu-editoru · youtube-paketleyici | köprü 0 → ölçülebilir | Güçlü (köprü ≈0 ölçüldü) [API] | 2 dk Niyazi |
| a5 | **Gün/saat:** K3 kaçtı → stok kuralıyla **Çar 2026-11-11 12:00 ET (17:00Z)**. Yüklemeden 1 sa sonra ve açılıştan 2 sa önce `privacyStatus/publishAt` API kontrolü; Niyazi Studio'da görünürlük ve plan alanına dokunmaz; Test & Compare ve uç ekran **açıldıktan sonra** | uretim-muhendisi (kontrol betiği) · koordinatör | erken public 2/2 → 0 | Güçlü (2/2 sapma) [API] | ~30 dk betik |
| a6 | **Uç ekran:** Abone + 1929 videosu (kanalın en iyi uzun videosu, tarih→gelecek). S08'i (5 izlenme) gösterme | Niyazi (Studio) · youtube-paketleyici (zaman) | oturum süresi ↑ küçük [T] | Zayıf | 2 dk |
| a7 | **Sabit yorum:** yanıtlanabilir tek soru ("Which leak surprised you most?"), yorumlara ilk 24 saatte yanıt (`09-paket/yorum-yanitlari.md`) | youtube-paketleyici · koordinatör | yorum 0 → ilk sinyal | Zayıf [T] | 0 |

## 5. (b) Kanal düzeyinde kalıcı değişiklikler
| # | Ne | Sahibi | Beklenen etki | Kanıt | Maliyet |
|---|---|---|---|---|---|
| b1 | **Analytics kapsamı:** `yt-analytics.readonly` eklenip Niyazi bir kez yeniden yetki verir; olmazsa her videonun 48 sa/7 g Studio CSV'si (Erişim → Gösterim, CTR, AVD, trafik kaynağı) | uretim-muhendisi + **Niyazi** | Teşhis kör → ölçülür; bu olmadan "tıklama mı tutma mı" hep cevapsız | Güçlü (bu rapor) | ≈2 dk Niyazi, 0 ₺ [T] |
| b2 | **Tempo önce:** 2 uzun/hafta korunur; limit kesintisine karşı 1 video stokta beklesin (kaçan slot = kaybolan video). İlk hedef 6–10 uzun video | showrunner · koordinatör | kohortta 6+ video %46 vs %12 [H] | Orta (ters nedensellik olası) | kapasite |
| b3 | **Shorts sıklığı ↓:** uzun video başına 1 Shorts (köprü), kazanılan kapasite uzun videoya | showrunner · kurgu-editoru | köprü ≈0, Shorts'lu kohort %19 vs %29 [API][H] | Orta-zayıf | kapasite kazancı |
| b4 | **Seri:** 4 video boyunca iki slot da A/C (tarih→gelecek, "what if") ağırlıklı; B haber sütunu 28 g verisine kadar beklemede | showrunner · viralite-analisti | S08 (B) %9 vs 1929 (A) %67 [H]; niş tarih→gelecek 1,57x [AÇK: `rakip-ozet.md`] | Zayıf (n=1+1) | 0 |
| b5 | **Thumbnail sistemi:** Leo için 4–5 farklı ifade/poz havuzu; aynı yüz iki ardışık videoda yok; hikâye nesnesi ana öğe | thumbnail-tasarimcisi · gorsel-varlik-sanatcisi | kanal tanınırlığı; CTR etkisi ölçülecek | Zayıf [GÖZ] | 1 kez Canva üretimi |
| b6 | **Süre:** 10–14 dk korunur; AVD gelince yeniden bakılır (kohort medyanı ~17 dk) | senaryo-yazari · kanal-analisti | saat birikimi ↑ olası | Zayıf [H] | 0 |
| b7 | **Topluluk:** her videoda sabit soru, ilk 24 sa tüm yorumlara yanıt; sub4sub/yorum dilenciliği yok | koordinatör | etkileşim sinyali | Zayıf [T] | 0 |
| b8 | Eski 4 gizli video: gizli kalsın, silinmesin (etki kanıtı yok, silme geri alınamaz) | Niyazi | — | Zayıf [T] | 0 |
| b9 | AI ses: değiştirme; beyan erişimi düşürmez [AÇK]. AVD geldiğinde ilk 30 sn düşüşüne bakılır; Niyazi'nin kendi okuması yedek test yolu | ses-yonetmeni · kanal-analisti | bilinmiyor | Ölçülemedi | 0 |
| b10 | **Ücretli tohum** (Google Ads ile 1 videoya küçük test, ~20–50 $ [T]) veya dış paylaşım (Reddit vb.) — **Niyazi onayı gerekir** (para / dış mesaj) | koordinatör → Niyazi | ilk izleyici sinyali; organik etkisi tartışmalı [T] | Zayıf | 20–50 $ [T] |

## 6. Sonraki video için 3 ders (hafızalara yazıldı)
1. → **uretim-muhendisi:** 2/2 uzun video planlanandan erken public oldu, 4/4 Shorts zamanında. Yükleme +1 sa ve açılış −2 sa'da `privacyStatus/publishAt` API kontrolü teslim kapısı olsun; sapmada koordinatöre bildir. [API]
2. → **youtube-paketleyici (+ Niyazi'nin Studio listesi):** Related video, Shorts açılmadan önce yapılıp ekran görüntüsüyle kayda geçmeli. Köprü ölçümü 342 → +5. Shorts uzun videodan sonra açılsın. [API]
3. → **thumbnail-tasarimcisi:** Leo'nun aynı şaşkın yüzü S08 + miras finalistlerinin hepsinde var. İfade/poz döndür, hikâye nesnesi ana öğe olsun (en iyi giden 1929 A2: sahne + işaret eden Leo; zayıf kanıt). [GÖZ]
Ders 1 ve 2 iki videoda tekrarlandı (1929 + S08) → `docs/ogrenme/ortak-dersler.md`'ye taşındı. [AÇK]

## 7. Erişim engelleri (2026-11-09)
| Yol | Durum |
|---|---|
| Data API v3 (`videos`, `channels`, `playlistItems`, `commentThreads`, `search`) | Çalışıyor; search 8 çağrı [API] |
| YouTube Analytics API | Kapsam yok → CTR/AVD/tutma/trafik/abone kaynağı ölçülemedi |
| Studio CSV / ekran görüntüsü | Gelmedi (7 g raporu da bu yüzden yazılamadı) [AÇK] |
| Related video durumu | API'de alan yok; yalnız Studio |

## Test
`python3 etiket_test.py teshis-11-09.md 2026-11-09` → `olcum/kapi-cikti-11-09.txt`.
