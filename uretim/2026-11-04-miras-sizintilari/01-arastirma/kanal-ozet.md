# F1 kanal özeti: @toonomy güncel durum ve 3 ders (2026-11-04)

İLERLEME: tamam · Hazırlayan: kanal-analisti · **Ölçüm: 2026-11-04 04:29 UTC** [API] · ham veri `olcum/kendi-2026-11-04.json` (sha256 ac081ed01f8a, betik `olcum/kendi.py`)
Veri yolu: yalnız YouTube Data API v3 (herkese açık sayılar). **CTR, gösterim, AVD, tutma, trafik kaynağı, Test & Compare: ÖLÇÜLEMEDİ** (`yt-analytics.readonly` kapsamı yok, Studio CSV gelmedi). [API]

**ÖZET**
1. 1929 uzun videosu durdu: 7. gününde 208 izlenme; 2026-11-02'deki 203'ten bu yana 2 günde +5 [API][H]. Önerilen/göz atma akışı videoyu almıyor [T].
2. Shorts 1 (QFC8GdDTW2c) ~38 saatte 341 izlenme, 5 beğeni (%1,5): uzun videoyu 1,6 kat geçti [API][H]. Aynı sürede uzun video yalnız +5 aldı → **Shorts→uzun köprüsü ≈0** [API][H]. Studio'da "Related video" bağlantısı kurulmuş mu, doğrulanamadı.
3. Shorts 2 (6LQGcQg4hpk) ~14,5 saatte 22 izlenme [API]. Yaşları farklı, kıyas 48 saatte tekrarlanmalı.
4. **S08 (ghLjMbrweCw) ŞU AN HERKESE AÇIK görünüyor**: API `privacyStatus=public`, `publishAt` boş, `publishedAt` 2026-11-03T12:00:11Z, 2 izlenme, 1 beğeni [API]. Plan 2026-11-04 17:00Z idi (`uretim/2026-10-28-yeni-video/durum.md`). Koordinatör Studio'dan görünürlüğü doğrulasın. "İlk saat" verisi bu yüzden yok; erken açılmış olabilir.
5. Kanal: 3 abone, 548 toplam izlenme, 4 herkese açık video [API]. YPP: 3/1.000 abone. Herkese açık uzun video izlenme saati ölçülemedi; tahmin ~10–18 saat / 8.000 [T: 210 × 3–5 dk]. Shorts saatleri YPP'ye sayılmaz.

## 1. Video tablosu (2026-11-04 04:29 UTC) [API]
| Video | Tür | Süre | Yayın (publishedAt) | İzlenme | Beğeni | Organik yorum |
|---|---|---|---|---|---|---|
| BVJwZ1C9R1U "You Have $1,000 in 1929. Can You Keep It?" | uzun | 10:32 | 2026-10-28 (plan 16:00Z) | 208 [API] | 1 [API] | 0 (1 yorum = kendi sabit yorumumuz) [API] |
| QFC8GdDTW2c "$1,000 in 1929: Which Door Would You Pick?" | Shorts | 0:50 | 2026-11-02 14:00Z | 341 [API] | 5 [API] | 0 [API] |
| 6LQGcQg4hpk "Same Box of Cash, Opposite Result: 1932 vs 2026" | Shorts | 0:57 | 2026-11-03 14:00Z | 22 [API] | 0 [API] | 0 [API] |
| ghLjMbrweCw "If America Earned $5,400 a Month, Here's Its Budget" | uzun | 11:19 | 2026-11-03 12:00Z (plan 11-04 17:00Z) | 2 [API] | 1 [API] | 0 [API] |

Hız [H]: 1929 ilk 4,5 günde ~45/gün, son 2 günde ~2,5/gün. Shorts 1 ~215/gün [H: 341 ÷ 1,58 g].

## 2. Neyin işe yarayıp neyin yaramadığı: 3 ders (sonraki video için)
1. **→ youtube-paketleyici + senaryo-yazari: başlıkta "$ rakam + yıl" bırakılsın, "paradoks" ya da "bundan sonra ne olur" çerçevesi kullanılsın.** İki uzun başlığımız da rakam ve/veya yıl taşıyor. Son 90 günde niş verisinde "Rakam/$" medyan skoru 0,95 (n=183) ve "Yıl" 0,95 (n=65). Tüm niş 1,06 [API][H] (`rakip-ozet.md` §3). Kazanan 1929 paketi tarihi izleyicinin yakın geleceğine bağlıyor: "The Crash That Will Change A Generation", thumbnail'de 1929 | 2027 yan yana, 30,3x [API][GÖZ].
2. **→ kurgu-editoru + youtube-paketleyici: Shorts kendi başına çözülmemeli; cevabı yalnız uzun videoda olan açık bir soruyla bitmeli. "Related video" bağlantısı yüklemenin parçası olmalı.** 341 Shorts izlenmesi uzun videoya +5 getirdi [API][H]. Bağlantı kurulduysa yüzde 1,5 altı dönüşüm var; dış kaynaklar da %1'in altı ile ~%10 arası diyor [AÖ]. Shorts dağıtım alıyor, uzun video almıyor. Sorun paket/konu tarafında.
3. **→ senaryo-yazari (Shorts kancası): "seçim yap" etkileşimi, "karşılaştırma" çerçevesinden iyi göründü.** "Which Door Would You Pick?" 341, "Same Box of Cash, Opposite Result" 22 [API]. Ancak yaş farkı var (1,6 g / 0,6 g) ve n=2 → **zayıf kanıt**. 48 saatte yeniden ölçülecek.

## 3. Erişim engelleri (2026-11-04)
| Yol | Durum |
|---|---|
| Data API v3 (`videos`, `channels`, `commentThreads`) | Çalışıyor [API] |
| YouTube Analytics API | Kapsam yok (token yalnız `youtube`); CTR/AVD/tutma/trafik ölçülemedi |
| Studio CSV / ekran görüntüsü | Gelmedi. 7 g raporu (1929, 11-04 16:00 UTC sonrası) için gerekli [T] |

## Test
`python3 etiket_test.py kanal-ozet.md 2026-11-04` → sonuç dosya sonunda değil, `olcum/kapi-cikti.txt` içinde.
