# Etkileşim teşhisi: Bölüm 001 (@flipbyvote), yayından ≈12 saat sonra

Hazırlayan: kanal-analisti · ölçüm 2026-11-12 05:02Z [API] · İLERLEME: tamam
Etiketler: **[API]** bu oturumda ölçüldü (YouTube Data API v3 / Graph API) · **[AÖ]** arama özeti veya üçüncü taraf kaynak; birincil sayfa açıldıysa "sayfa açıldı" yazıyor · **[T]** tahmin · **[ÖB]** ön bilgi (repodaki eski ölçüm, bu oturumda yeniden doğrulanmadı) · **[AN]** anekdot (yalnız açıklama metninde kullanılıyor, rakam taşımıyor).

## 0. Karar (tek paragraf)
**Sorun önce dağıtımda, etkileşimde değil.** YouTube'da 10 izlenme var [API]. Shorts'ta yorum oranını kabaca 1.000 izlenmede 1–5 alırsak [T], 10 izlenmeden beklenen yorum sayısı 0,01–0,05'tir. Bu durumda "0 yorum" bir başarısızlık işareti sayılmaz, beklenen sonuçtur. Instagram'da izlenme sayısını hiç bilmiyoruz: insights izni yok (#10) [API]. Bu yüzden kancanın mı, dağıtımın mı tuttuğunu ayıramıyoruz. 7 günde yapılacak üç iş var: (1) gösterim sayısını artırmak, (2) ölçümü açmak, (3) bölümü tek başına izlenince de anlaşılır kılmak (ilk 2 sn'de seçim, ardından "previously"). Format kararı 7. bölümden sonra §4'teki eşiklerle verilecek. Daha erken verilen her karar 10 izlenmelik bir örnekleme dayanır ve gürültüden ibaret olur.

## 1. Canlı durum (2026-11-12 05:02Z)
| Platform | Ölçüm | Değer | Kaynak |
|---|---|---|---|
| YouTube Shorts bjRc7yhTpKE | izlenme / beğeni / yorum | 10 / 1 / 0 [API] | `videos?part=statistics` |
| | yayın zamanı (plan 17:00Z) | 2026-11-11T17:00:14Z, public, madeForKids=false, 75 sn [API] | plana uygun |
| YouTube kanalı UC1XHl… "Flip By Vote" | abone / video | 3 / 1 [API]; kanal viewCount alanı henüz 0 (gecikmeli) [API] | `channels` |
| Instagram @flipbyvote | takipçi / gönderi | 0 / 1 [API] | Graph API |
| Reel 17968514064237066 | beğeni / yorum | 0 / 1 [API]; o 1 yorum bizim sabit yorumumuz (`bolum-001/yorum-log.md`) | Graph API |
| | yayın zamanı | 2026-11-11T17:10:03Z [API]; plandan 10 dk sonra | |
| | views / reach | **ölçülemedi**: `(#10) Application does not have permission` [API] | token'da `instagram_manage_insights` yok |
| TikTok | yükleme | kayıt yok: `teslim/yayin-sonucu.txt` yalnız YouTube'u gösteriyor [AÇK] | CLAUDE.md "üç platform aynı anda" diyor; yapılmadıysa en ucuz eksik bu |

## 2. Gerçekçi beklenti: sıfır takipçili yeni hesap, ilk 1–7 gün
| Ne | Değer | Etiket ve not |
|---|---|---|
| YouTube Shorts, yeni kanalın **ilk** Shorts'u, 30. gün medyanı | **1.362** izlenme; 10. Shorts 1.344; ilk 10'un en iyisi 8.832; Shorts'ların %56,6'sı ≥1.000 | [AÖ: vidIQ Research, Temmuz 2026, sayfa açıldı; 367.243 kanal, 2025 H1'de açılmış, ilk 90 günde ≥10 Shorts yüklemiş]. **Benchmark**, ama **30 günlük** değer ve yalnız ≥10 Shorts yükleyen kanallar sayılıyor: hayatta kalan yanlılığı var, 12 saatle doğrudan kıyaslanmaz |
| YouTube Shorts, <1.000 aboneli kanal, ilk 48 saat | 50–500 izlenme; "sıfır izlenme" çoğu zaman 10–30 demek | [AÖ: humbleandbrag blogu; yöntem yok]. Benchmark sayılmaz, blog görüşü |
| Bizim eski kanaldaki Shorts | 341 izlenme | [ÖB: kanal-analisti hafızası 2026-11-04, Toonomy] |
| Instagram Reels ortalama etkileşim oranı | %0,45–0,52 (2026) | [AÖ: Socialinsider aktarımları]. Takipçi paydalı, **0 takipçide anlamsız** |
| Instagram, 0 takipçili hesabın ilk Reels'i | yayımlanmış bir benchmark **bulunamadı** | Bloglar yalnız "soğuk başlangıç" diyor, sayı yok [AÖ] |
| Bölüm başına bizim beklentimiz, gün 1–7 | YT Shorts 48 saatte 20–300 izlenme; IG 50–300 (insights açılınca ölçülür); **0–2 izleyici yorumu**; ilk 3–5 bölüm boyunca 0 yorum olasılığı yüksek | [T]. Dayanak: üstteki iki aralığın alt yarısı + 1.000 izlenmede 1–5 yorum varsayımı [T] |
| 12. saatteki 10 izlenme nerede duruyor | 48 saatlik blog aralığının (50–500) altında, ama ölçüm 12. saatte [API + AÖ] | Shorts'ta gecikmeli test dağıtımı sık anlatılıyor [AN]. **48. saat ölçümünden önce "başarısız" denmez** |

**Etiket ayrımı [AÖ]:** benchmark olarak vidIQ'nun 30 günlük medyanı (kohortu tanımlı) kullanılabilir. humbleandbrag aralığı blog. "Gecikmeli patlama" hikâyeleri anekdot. Bizim aralığımız tahmin.

## 3. Olası sebepler (olasılık sırasıyla)
| # | Sebep | Kanıt | Güç |
|---|---|---|---|
| 1 | **Dağıtım: soğuk hesap.** IG'de 0 takipçi, YT'de 3 abone ve 1 video [API]. İlk gösterim havuzu tümüyle algoritmanın test grubundan geliyor | YT 10 izlenme [API]. 10 izlenmeden beklenen yorum ≈0 [T] | **Güçlü.** Sonuçların çoğunu açıklıyor |
| 2 | **Ölçüm körlüğü** (sebep değil, teşhisi engelliyor). IG views okunamıyor [API]. YT "izlendi / kaydırıldı" oranı yalnız Studio'da var (Analytics kapsamı yok, CLAUDE.md) | — | Kanca hakkında ancak bu açılınca hüküm verilebilir |
| 3 | **Seri formatının ilk bölümü + CTA'nın yeri.** Seçim sorusu ancak ≈70. saniyede geliyor; 75 sn'lik Shorts'u sonuna kadar izleyen azınlık olur [T]. 6,4–15,4 sn arası 9 sn konuşmalı tanıtım ("Two best friends… You do") [AÇK: `bolum-001/metin.md` S2]. Karakterler tanınmadığı için tanıtım gerekli, ama soru gelmeden önce kaydırma riski doğuruyor [T] | Kaydırma oranı ölçülemedi | **Orta.** Etkileşimi (yorumu) en çok etkileyecek kalem bu |
| 4 | **Kanca.** 0,2 sn'de SLAM + "$100" sayacı + "That's it. Every dollar we have." [AÇK: metin S1]. Hareket ve ses var, ama ilk karede izleyicinin **neye karar vereceği** görünmüyor | Ölçülemedi | Orta-zayıf. Kendi başına kötü değil; seçim ilk 2 sn'ye girerse güçlenir |
| 5 | **Konu doygunluğu.** YT araması (2025-11 sonrası, ilk 25 sonuç) [API]: "turning $100 into $1000 flipping" sorgusunda medyan 4.002, ≥100 B olan 5 video, **animasyon 0/25**. "100 dollars to 1 million challenge" sorgusunda medyan 809.786, ≥100 B olan 21 video, animasyon 2/25; sonuçlara MrBeast ve Nick DiGiovanni hâkim | Tür **gerçek kişi** videolarıyla dolu ve talebi kanıtlanmış [API]. Animasyonlu, izleyicinin karar verdiği versiyon neredeyse yok [API, n=50, zayıf kanıt] | **Zayıf.** Shorts akışı arama değil ilgi alanıyla dağıtılıyor [T]. Doygunluk 10 izlenmeyi açıklamaz. Risk: "$100 → X" başlığı kumar ve trading videolarıyla aynı kümeye düşebilir (aynı sorguda "by Gambling", "Forex" çıktı [API]) |
| 6 | **AI etiketi.** Erişimi düşürdüğüne dair birincil kaynak yok (`politika-format.md` §3) [ÖB] | Kanıt yok | **Zayıf.** Etiket AÇIK kalır; IG'de ses gerekçesiyle zorunlu okunuyor |

## 4. Bugün başlayan 5 aksiyon (ücretsiz, politika uyumlu, yem yok)
| # | Aksiyon | Kim | Beklenen etki |
|---|---|---|---|
| A1 | **İlk 2 sn'de seçim ekranda.** Kare 1'den itibaren üç seçenek ikonlarıyla gösterilir ("$100 · BIKE · DRESSER · BOX?"). Konuşmalı tanıtım 9 sn'den ≤4 sn'ye iner. Soru ilk 3 sn'de bir kez, sonda bir kez sorulur | senaryo-yazari → kurgu-editoru | Kaydırma oranı düşer ve soruyu duyan izleyici oranı belirgin biçimde artar [T: etki büyüklüğü ölçülmedi]. En büyük **etkileşim** kaldıracı |
| A2 | **"Previously" ≤3 sn (Bölüm 2'den itibaren):** "Last episode: bike, dresser, or box. You picked…" (0 yorum varsa: "No votes yet. Jake picked…" kuralı). Ekranda ilerleme çubuğu: "Ep. 2 · BANK $100 → $1,000,000" | senaryo-yazari ‖ kurgu-editoru | Her bölüm, önceki bölümü bilmeyen izleyici için de anlaşılır olur. Soğuk hesapta izleyicilerin neredeyse tamamı ilk kez görüyor [T] |
| A3 | **TikTok'a aynı saatte yükleme** (yapılmadıysa) + YouTube'da oynatma listesi "Flip By Vote — Season 1" (koordinatörün kanal ayarı yetkisi kapsamında) | koordinatör / Niyazi (TikTok yüklemesi elle) | Fazladan bir dağıtım havuzu: bölüm başına +50–500 izlenme [T]. Liste, sonradan gelen izleyiciyi Bölüm 1'e taşır |
| A4 | **Paket:** YT Shorts başlığı soruyla başlar: "Bike, dresser, or mystery box? You pick · Ep. 2". IG altyazısının ilk satırı aynı soru. Hashtag 3–5, niş: #flipping #animatedseries #flipbyvote (+ bölüme özgü 1 tane). #Shorts gerekmiyor | youtube-paketleyici | Küçük [T]. Mosseri'ye göre hashtag'in katkısı az [ÖB]. Asıl işlevi soruyu altyazıda ve başlıkta görünür kılmak |
| A5 | **Ölçümü aç [T: öneri]:** IG token'ına `instagram_manage_insights` eklenir (views, reach, ortalama izlenme, kaydetme, gönderme). Niyazi her 48 saatte YT Studio'daki Shorts "Viewed vs swiped away" ekranının görüntüsünü verir | uretim-muhendisi + Niyazi (yetki) | Doğrudan erişim getirmez. Ama A1'in işe yarayıp yaramadığını ve §5 eşiklerini **ancak bu ölçer** |

**Sorulan diğer kalemler:**
- **Trial Reels:** uygun değil. 0 takipçide hem anlamsız hem görünmüyor; ayrıca ilk Reels'i ızgaradan gizler (`reels-paylasim-yolu.md`) [API: 0 takipçi]. 200–1.000 takipçiden sonra alternatif kancalı ikinci kesit için kullanılabilir [AÖ].
- **"Comment BIKE" gibi tek kelimelik komut: YASAK.** Instagram'ın kendi açıklaması, engagement bait örneği olarak "asking people to comment with a specific word, number, or emoji" gösteriyor [AÖ: Social Media Today 2024-06-05, sayfa açıldı, Instagram'dan alıntı]. `politika-format.md` §1 de "comment A/B/1/2"yi yasaklıyor. **Uyumlu yol** şu anki soru biçimi: "Bike, dresser, or mystery box?" Soruya tek kelimeyle cevap verilebiliyor, ama izleyiciye bir kelime **dayatılmıyor**. Her gün seçenek adları değişiyor.
- **Story + anket çıkartması:** kural olarak devam. Ancak 0 takipçide hikâyeyi kimse görmüyor [T]; erişim etkisi takipçi gelene kadar ≈0.
- **Collab (IG ortak gönderi):** başka bir hesaba mesaj atmak gerekiyor, bu dış mesaj sayılır ve **Niyazi onayı** ister. 0 takipçili hesabın teklifini kabul eden çıkma olasılığı düşük [T]. 14. günden sonra değerlendirilir.
- **Paylaşım saati:** 20:00 TSİ = 12:00 ET (Niyazi kararı). Değiştirmeyi gerektiren bir kanıt yok. Saatin etkisi, soğuk hesabın etkisinin yanında küçük kalır [T]. IG 10 dk geç çıktı [API]; bundan sonra üç platform aynı dakikada çıkmalı.
- **Ek seçenek (Niyazi kararı gerekir):** dağıtım havuzu küçük olduğu için günde 1 bölüm dışında 15–20 sn'lik "Meet Jake & Mike" tanıtım Shorts'u. Fazladan bir gösterim şansı verir [T]. Format kuralı "günde 1 bölüm" olduğundan karar koordinatörden Niyazi'ye gider.

## 5. 7 günlük ölçüm hedefi ve "format değiştir" eşiği [T: eşik önerisi]
Her bölüm 24. ve 48. saatte, üç platformda ölçülür: views, izleyici yorumu (bizim sabit yorumumuz hariç), beğeni, IG reach ve ortalama izlenme, YT izlendi/kaydırıldı oranı.

| Gün 7 hedefi (Bölüm 1–7) | Eşik | Etiket |
|---|---|---|
| YT Shorts 48. saat izlenme medyanı | ≥150; en az 1 bölüm ≥500 | [T: vidIQ 30 g medyanı 1.362 ve blog aralığı 50–500'den türetildi] |
| IG 48. saat views medyanı | ≥150 (insights açılınca) | [T] |
| YT izlendi oranı ("viewed") | ≥%60 | [T: eşik önerisi] |
| Gerçek izleyici yorumu (3 platform toplamı, 7 bölüm) | ≥5; en az 1 bölümün seçimi bir izleyici yorumuyla yapılmış | [T] |
| 1.000 izlenmede yorum | ≥2 | [T] |

**Eşikler (7. bölümden sonra, koordinatör → Niyazi):**
- **D: Dağıtım sorunu.** Views medyanı <50 (YT) ve IG <100 iken yorum 0 → **format değiştirilmez**, çünkü format henüz test bile edilmemiş olur. Yapılacaklar: kanca (A1), paket (A4), TikTok (A3) ve ek tanıtım Shorts'u kararı. 14. günde tekrar bakılır.
- **K: Kanca sorunu.** Views ≥150 ama izlendi oranı <%50 veya IG ortalama izlenme <%30 → ilk 3 sn yeniden tasarlanır (senaryo-yazari + kurgu-editoru). Format korunur.
- **F: Format sorunu.** Views ≥300 ve izlendi oranı ≥%60, ama 1.000 izlenmede yorum <1 (7 bölümde toplam ≤2 yorum) → **format değiştir sinyali.** İzleyici izliyor ama karar vermek istemiyor demektir. Seçenekler: iki seçenekli karar, soru başta, karar mekanizması IG anketine taşınır. Bu karar Niyazi'ye getirilir.
- Tek bölümlük patlama (≥5.000) olursa eşikler o bölümün izleyici kaynağına göre yeniden okunur.

## 6. Sonraki bölüm için 3 ders [T: öneri]
1. **senaryo-yazari:** seçim ilk 3 sn'de sorulsun; konuşmalı tanıtım ≤4 sn olsun; Bölüm 2'den itibaren "previously" ≤3 sn.
2. **kurgu-editoru:** kare 1'den itibaren üç seçenek ikonu ve BANK ekranda; yorum sorusu altyazıda büyük punto.
3. **youtube-paketleyici:** başlığın ve IG altyazısının ilk satırı bölümün seçim sorusu olsun; "comment X" asla yazılmasın.

## Kaynaklar [AÖ]
- vidIQ Research, "YouTube first 10 videos study", Temmuz 2026 (sayfa açıldı): https://vidiq.com/research/youtube-first-10-videos-study/
- humbleandbrag, Shorts benchmarks (blog): https://humbleandbrag.com/blog/youtube-shorts-benchmarks
- Social Media Today, 2024-06-05, Instagram'ın tek kelimelik CTA açıklaması (sayfa açıldı): https://www.socialmediatoday.com/news/instagram-clarifies-advice-on-single-word-ctas-and-longer-reels/718151/
- Socialinsider, 2026 Reels benchmark'ları (arama özeti): https://www.socialinsider.io/blog/instagram-reels-benchmarks/
- Yeni hesapta soğuk başlangıç (blog, rakam yok): https://bosswallah.com/blog/creator-hub/why-reels-are-not-getting-views-on-new-instagram-accounts-the-real-reasons-beginners-struggle/
- Repo: `uretim/seri/politika-format.md` §1, §3 · `uretim/seri/reels-paylasim-yolu.md` · `uretim/seri/bolum-001/metin.md` · `uretim/seri/bolum-001/teslim/platform-metinleri.md`

## Erişim engelleri (2026-11-12) [API]
- IG insights: `(#10)` izin yok. Token'a `instagram_manage_insights` eklenmeli (uretim-muhendisi + Niyazi).
- YT Analytics (CTR, kaydırma oranı, AVD): `yt-analytics.readonly` kapsamı yok. Yerine Studio ekran görüntüsü kullanılır.
- Instagram'da 0 takipçili hesap için birincil benchmark bulunamadı. Meta yardım sayfaları WebFetch'te boş dönüyor (hafıza).
- TikTok yükleme durumu repoda kayıtlı değil.

## Test
Etiket kapısı: `uretim/2026-11-04-miras-sizintilari/01-arastirma/etiket_test.py uretim/seri/etkilesim-teshis-001.md 2026-11-12` → rakamlı satır 55, etiketsiz 0 · `grep -c AIza` → 0.
