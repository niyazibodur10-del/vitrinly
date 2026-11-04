# F1 rakip özeti (DELTA, 90 gün): küçük kanalın milyona çıkış desenleri

İLERLEME: tamam · Hazırlayan: kanal-analisti · **Ölçüm: 2026-11-04 04:31 UTC**, pencere 2026-08-06 → 2026-11-04 [API]
Ham veri `olcum/delta90-2026-11-04.json` (sha256 700788baba66). Betikler: `olcum/delta90.py` (toplama), `desen90.py` + `desen90b.py` (kalıp), `sirala90.py` (kanal sırası). Çıktılar `olcum/*-cikti.txt`. Hariç tutulan kanallar `olcum/haric.txt` (Hintçe, podcast, dil öğretimi, konu dışı).
Taban: `docs/rakip-analizi.md` (v2 bölümü bu ölçümle güncellendi) ve 10-28 deltası (`uretim/2026-10-28-yeni-video/01-arastirma/rakip-ozet.md`).

**ÖZET (karar için)**
1. Son 90 günde **7.840 aboneli False Profit 776.925 izlenme** aldı (364x medyan, izlenme/abone 99). Başlık "What Happens When Economists Run a Country", konu Şili 1973 [API][H]. Küçük kanalın tek videoyla patladığının en net kanıtı bu.
2. Bize format olarak en yakın kanal **Marcus Explains**: 2026-07-06'da açılmış, 30,7 B abone. Maskotlu çizgi sahneler kullanıyor. "How X Actually Make Money (It's Not Y)" ve "The Economics of X" başlıklarıyla 6 video 400–537 B izlendi [API][GÖZ].
3. En güçlü başlık kalıpları (kanal içi medyana göre skor): gizli iş modeli medyan 2,20, ancak yalnız 3 kanalda görülüyor (kanal etkisi). Tarih→gelecek 1,57 (9 kanal). Paradoks sorusu 1,29 (6 kanal). Tüm niş 1,06 [API][H].
4. Zayıf kalıplar: "Rakam/$" 0,95, "Yıl" 0,95, düz "Why…" 0,97 [API][H]. Bizim iki başlığımız da rakam/yıl taşıyordu.
5. Patlayan genç kanallar **Shorts kullanmıyor**: Markets of the Past 79 uzun / 0 Shorts, Why X 68 / 0, Marcus 40 / 2 (90 günde) [API]. Shorts→uzun köprüsünün kanıtı zayıf (§5-P5).

## 0. Etiketler ve yöntem
- [API] Data API v3, 2026-11-04 · [H] API sayılarından hesap · [GÖZ] i.ytimg.com mqdefault incelemesi, 2026-11-04 (12 thumbnail) · [ALT] yt-dlp altyazı denemesi, 2026-11-04 · [AÇK] video açıklama metninden hook çıkarımı (transkript değil) · [AÖ] WebSearch özeti, 2026-11-04 · [T] tahmin.
- Örneklem [API]: önceki 51 kanal + 10 hedefli `search` sorgusu (90 gün, uzun video, izlenmeye göre). Toplam 158 kanal, 125'i aktif, 3.366 uzun video. **Niş alt küme:** hariç listesi dışındaki, kanal medyanı ≥1.000 ve ≥7 günlük videolar: 959 video, 38 kanal [API][H].
- Skor [H]: `skor_med` = izlenme ÷ kanalın son ≤30 uzun (≥4 dk) ve ≥7 günlük videosunun medyanı; `izl/abone` = izlenme ÷ abone. Yaşlı videolar avantajlı. Pencere içindeki videolar medyana dahil, bu yüzden skor muhafazakâr.
- Hayatta kalan yanlılığı: arama izlenmeye göre sıralandığı için patlayan küçük kanallar fazla temsil ediliyor. Hiç tutmamış binlerce küçük kanal örneklemde yok [T].

## 1. Son 90 günün en büyük outlier'ları (niş, ≥30 B izlenme) [API][H]
| Video (id) | Kanal (abone, açılış) | Süre | İzlenme | skor_med | izl/abone |
|---|---|---|---|---|---|
| What Happens When Economists Run a Country (DoG6_3PFHN0) | False Profit (7,8 B, 2025-07) | 21,1 dk | 776.925 | 364x | 99,1 |
| What Happens If Trump Loses The Midterms? (AyMHJBLc_tA) | Finance Bureau (134 B, 2025-10) | 19,1 dk | 4.259.536 | 51,4x | 31,8 |
| Silver Is Running Out... So Why Is It Crashing? (ayTQn2jGtS0) | Why X (46 B, 2025-02) | 18,3 dk | 766.023 | 36,0x | 16,6 |
| The Real Reason Hitler Never Invaded Switzerland (36J1tL9ulGA) | Markets of the Past (108 B, 2026-04) | 30,9 dk | 1.691.726 | 33,3x | 15,7 |
| 'Big Short' Investor Explains How the AI Bubble Will Burst (Zw0I7kb6zg4) | New Money (1,11 M) | 44,2 dk | 4.600.075 | 31,9x | 4,1 |
| The Crash That Will Change A Generation (deeMYKK3-98) | Nolan Matthias (130 B) | 28,2 dk | 558.152 | 30,3x | 4,3 |
| This Is What "ALWAYS" Happens Before A Financial Crisis (aTaNYr_jkMY) | Nolan Matthias | 25,4 dk | 394.381 | 21,4x | 3,0 |
| 2030 Prediction: The Male Exodus Will BANKRUPT These 5 American Universities (_Ybq9G4zSKk) | theunfilteredguy (6,6 B) | 21,1 dk | 273.111 | 18,0x | 41,2 |
| How All-You-Can-Eat Buffets Make Money? (It's Not Food) (cdEGg2-C6bI) | Marcus Explains (30,7 B, 2026-07) | 24,1 dk | 537.283 | 16,2x | 17,5 |
| The Economics of Money Laundering (5lpKA72DQmo) | Marcus Explains | 25,1 dk | 511.522 | 15,4x | 16,7 |
| What if the AI Bubble Bursts (Day by Day) (T9d6lrvzM9o) | The Infographics Show (15,5 M) | 32,1 dk | 4.896.076 | 11,5x | 0,32 |
| How Did America Pay Off The National Debt Last Time? (52cVI0iERf8) | How Business Worked (299 B) | 23,7 dk | 1.186.935 | 4,7x | 4,0 |

## 2. En iyi 5 kanal (2 ölçüt, 38 kanal) [API][H]
Ölçüt A = 90 g medyan izlenme ÷ abone; ölçüt B = ≥3x video oranı. Kural: iki sıralamada da ilk 5'e girmeyen elenir.
| Kanal | A (sıra) | B (sıra) | Uzun / Shorts (90 g) | Neden seçildi |
|---|---|---|---|---|
| False Profit | 3,90 (#1) | %67 (#2) | 3 / 0 | En küçük → en büyük sıçrama |
| theunfilteredguy | 1,97 (#3) | %20 (#10) | 51 / 0 | C sütunu "20XX Prediction" serisi |
| How Business Worked | 1,56 (#5) | %17 (#13) | 6 / 0 | Tarih emsali → bugünkü sorun |
| Marcus Explains | 1,08 (#10) | %32 (#4) | 40 / 2 | Maskot formatı, 4 ayda 30 B abone |
| Nolan Matthias | 0,46 (#18) | %73 (#1) | 11 / 3 | Tarih→gelecek kalıbında en tutarlı |

Elenen: Who Gets Paid (A #2; 1,9 B abone, en iyi video 30 B, mutlak ölçek küçük → izlemede), GEN ve TechButMakeItReal (B #5 / #3; GEN büyük kanal, desenleri P1/P3'te örnek), Finance Bureau (A #14, B #8; ilk 5 dışı, yalnız 4,26 M outlier'ı için §1'de) [API][H].

## 3. Desen istatistiği (niş n=959, kanal içi skor) [API][H]
| Kalıp | n | Kanal | Medyan skor | ≥2x oranı |
|---|---|---|---|---|
| Gizli iş modeli (actually make money / economics of / business model) | 32 | 3 | 2,20 | %53 |
| Tarih→gelecek (before a / last time / always happens / prediction / about to) | 35 | 9 | 1,57 | %43 |
| How… | 51 | — | 1,44 | %35 |
| Here's / This is | 22 | — | 1,43 | %41 |
| Collapse/Crisis/Crash/Bubble | 108 | — | 1,35 | %36 |
| Paradoks (So why / Why hasn't / "..." + but) | 26 | 6 | 1,29 | %31 |
| What Happens If / When | 30 | — | 1,09 | %37 |
| Düz "Why…" | 144 | — | 0,97 | %17 |
| Rakam/$ | 183 | — | 0,95 | %19 |
| Yıl (19xx/20xx) | 65 | — | 0,95 | %22 |
| Tüm niş | 959 | 38 | 1,06 | %24 |
Süre [API][H]: 15–20 dk medyan 1,23 (≥2x %27) en iyi. 10–15 dk 1,11 (≥2x %18, n=83). 60+ dk 0,66. Bizim 10–14 dk hedefimiz ≥2x oranında geride.

## 4. Thumbnail ve hook desenleri
**Thumbnail [GÖZ] (12 outlier):** ana başlık metni ≤4 kelime: 11/12 (istisna 36J1tL9ulGA, 6 kelime). Tip (a) ayrıca küçük rakam etiketleri taşıyor. Üç tip öne çıkıyor:
- (a) Çizgi maskot + kalabalık illüstrasyon sahnesi + 4–6 küçük rakam etiketi + 3 kelimelik büyük başlık. Örnek: "BUFFET FOOD RIPOFF" (cdEGg2-C6bI), "THE MONEY LAUNDERING TRICK" (5lpKA72DQmo). Marcus'un maskotu beyaz, yuvarlak kafalı ve sinsi gülümseyen bir figür. [GÖZ]
- (b) İki çelişen gerçek, iki satır metin. Örnek: "Running Out. / Still Falling." (ayTQn2jGtS0); 1929 | 2027 bölünmüş kare (deeMYKK3-98). [GÖZ]
- (c) Tek kişi/yüz + yanan sembol, metin yok veya 1–2 kelime. Örnek: AyMHJBLc_tA, 36J1tL9ulGA "WHY NOT SWITZERLAND?". [GÖZ]
- Renk [GÖZ]: kırmızı ok/grafik düşüşü 4/12. Sarı vurgu metni 2/12.
**Hook (ilk 30 sn) [AÇK]:** yt-dlp altyazı 4/4 videoda bot kontrolüne takıldı. Açıklamanın ilk cümleleri hook'u yansıtıyorsa, iki tip var:
- **Paradoks sorusu:** "When something runs out, the price is supposed to go up. So how can a metal run out and crash at the same time?" (ayTQn2jGtS0). "You pay one price and eat as much as you want. So how do buffets still make money?" (cdEGg2-C6bI). [AÇK]
- **Somut anomali sahnesi:** "A shell company with no employees reported 40 million dollars… caught because the invoices used the same font twice" (5lpKA72DQmo). "One tiny country… remained completely untouched" (36J1tL9ulGA). [AÇK]
Kanıt dolaylı: transkript değil, açıklama metni. Etiket **orta-zayıf**.

## 5. Küçük kanalın milyona çıkması: kanıtlı 5 desen
**P1. "What Happens If/When <sistem değişirse>" (C senaryosu, bir sisteme somut müdahale).** False Profit 776 B (364x), Finance Bureau 4,26 M (51x), Infographics 4,9 M (11,5x), TechButMakeItReal "What happens to Life Insurance and Pensions If AI Bubble bursts?" 358 B (13x) [API][H]. Kalıbın ≥2x oranı %37, niş %24 [H]. Paket: tek yüz/sembol + yangın veya tarihsel fotoğraf + ≤2 kelime [GÖZ].
**P2. Tarih emsali → izleyicinin yakın geleceği (A→C köprüsü).** "The Crash That Will Change A Generation" 30x, thumbnail 1929 | 2027. "This Is What 'ALWAYS' Happens Before A Financial Crisis" 21x. "How Did America Pay Off The National Debt Last Time?" 1,19 M [API][GÖZ]. Kalıp 9 kanalda, medyan 1,57 [H]. Bizim 1929 videomuz tarihi kapalı bir oyun olarak anlattı, geleceğe bağlamadı. Fark bu [T].
**P3. Gizli iş modeli / "aslında nasıl para kazanıyor".** Marcus Explains (4 aylık): 6 video ≥400 B. Who Gets Paid "The Economics of Owning a Pirate Port Tavern" 3,4x [API]. Medyan 2,20 ama yalnız 3 kanal: kanal etkisi olabilir, **orta kanıt** [H]. Paket tipi (a): maskot sahnede bir işi yürütüyor, rakam etiketleri görünüyor. Leo'nun rolüne birebir uyuyor.
**P4. Paradoks sorusu (iki doğru gerçek çelişiyor).** "Silver Is Running Out... So Why Is It Crashing?" 36x. "If Housing is F*cked, Why Hasn't It Crashed?" GEN 1,51 M. "Central Banks Are Buying Gold... So Why Is It Falling?" 6,0x. "Why the Economy Hasn't Crashed Yet" 8,1x [API]. Kalıp 6 kanalda, medyan 1,29 [H]. Paket tipi (b): iki satır, iki çelişen kelime [GÖZ].
**P5. Seri (franchise) + uzun video odaklı büyüme; Shorts motor değil.** Patlayan genç kanallar 90 günde 40–79 uzun video yayınladı, Shorts'u 0–2 [API]. Seri başlığı tekrar ediyor: Markets of the Past "The True Origin of X: What Historians Get Wrong", theunfilteredguy "20XX Prediction: The Male Exodus…" (27 videonun 10'u ≥50 B) [API]. Shorts verisi: ≥10 Shorts atan 9 kanalda kanal medyanı/abone 0,46, <10 Shorts atan 31 kanalda 0,39 → fark yok [H]. Kendi verimiz: 341 Shorts izlenmesi uzun videoya +5 getirdi [API]. Related-links dönüşümü için resmi rakam yok; satıcı/yaratıcı iddiaları %1'in altı ile ~%10 arasında [AÖ]. **Köprü önerisi:** Shorts = uzun videonun açık sorusu ("cevabı videoda") + Related video bağlantısı + sabit yorum. Büyümeyi Shorts'a dayandırma.

## 6. Kopyalamama (desen → bizim özgün karşılığımız)
| Desen | Bizim karşılığımız |
|---|---|
| P1 What Happens If | Leo bir sistemi "deney masasında" açıp kapatır (ör. "What Happens If the Dollar Lost Reserve Status for One Year"). Gelecek her zaman "senaryo" etiketiyle sunulur. Kişi siyaseti yok [T: öneri] |
| P2 Tarih→gelecek | Kendi "Then / Next" bölünmüş kare dilimiz (1929 sahnemiz soğuk, gelecek sıcak renkte). 1929 | 2027 düzenini birebir alma [T: öneri] |
| P3 Gizli iş modeli | Leo işletmenin kasasının arkasına geçer. Rakam etiketleri bizim büyük sayı grafik stilimizle. Marcus'un beyaz yuvarlak maskotu ve "It's Not Y" ekini kopyalama [T: öneri] |
| P4 Paradoks | Hook'ta iki doğru rakam yan yana, ardından tek soru. Thumbnail'de iki kelime; "Running Out / Still Falling" kalıbını alma [T: öneri] |
| P5 Seri | Kendi seri adımız (ör. "Leo Runs the Numbers"). Tempo 2/hafta kalır: kalite kapısı ve seri üretim riski [T: öneri] |
Ayrışma uyarısı [GÖZ]: iki maskotlu rakip var, Fred (silindir şapka, takım elbise) ve Marcus (beyaz yuvarlak kafa, sinsi gülüş). Leo'nun silüeti ve renkleri ikisinden de ayrışmalı → thumbnail-tasarimcisi.

## 7. Erişim engelleri (2026-11-04)
| Yol | Sonuç |
|---|---|
| Data API v3 `search` (10 sorgu) / `playlistItems` / `videos` / `channels` | Çalıştı, 429 yok [API] |
| yt-dlp otomatik altyazı | 4/4 "Sign in to confirm you're not a bot" → hook transkripti YAPILAMADI [ALT] |
| i.ytimg.com thumbnail | Açık [GÖZ] |
| WebSearch (Shorts related links) | Açık; yalnız satıcı/yaratıcı verisi, resmi rakam yok [AÖ] |
Kaynaklar [AÖ]: vidiq.com/blog/post/youtube-related-links-connect-shorts-long-videos · subscribr.ai/youtube-strategy/youtube-shorts-hurting-long-form-views · spottercommunity.beehiiv.com/p/increase-views-from-related-shorts · metricool.com/youtube-trends/

## Test
Etiket ve tarih kapısı: `olcum/kapi-cikti.txt`.
