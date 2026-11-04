# Viralite modeli v0.2

Amaç: senaryoları üretmeden önce viral olma potansiyeline göre sıralamak.
Format kararı: **2D karakter anlatımlı, İngilizce uzun video** (≥10 dk).
**Durum:** Bütün ağırlıklar, bonuslar ve cezalar **tahmindir [T]**. v0.2 (2026-11-04) 90 günlük niş verisiyle (n=959) bir kez kalibre edildi; kendi kanal verisiyle henüz kalibre edilmedi. Bkz. "Kalibrasyon durumu".
Hesap elle yapılmaz, `tools/viralite.py` ile yapılır. Ağırlıklar betikte tek yerde tanımlı (`OLCUTLER`); bu tablo onunla
aynı olmalı (`python3 tools/viralite.py --dokuman docs/viralite-modeli.md` denetler).

## Temel ölçü: outlier skoru (kanıt için)
`outlier = video izlenmesi / yerel medyan`. Yerel medyan, aynı kanalda videonun **çevresindeki ~10 yüklemenin
(öncesi ve sonrası) medyan izlenmesidir**. Kanalın tüm zamanlar ortalaması kullanılmaz, çünkü kanal büyümesi ve tek
dev video bu ortalamayı bozar. ≥3x güçlü, ≥10x istisnai sayılır.
Veri sadece kanal ortalaması olarak bulunabildiyse skor "ort. bazlı" diye etiketlenir ve kanıt gücü bir kademe düşük sayılır.

## Ölçütler (1–10)
| # | Ölçüt | Ağırlık | Soru |
|---|---|---|---|
| 1 | Merak boşluğu | 0.25 | Başlık ve thumbnail "ne oldu / ne olacak?" dedirtiyor mu? |
| 2 | Kanıtlı talep | 0.15 | Konu veya açı rakiplerde outlier üretti mi, aramada ilgi var mı? |
| 3 | Hook gücü | 0.10 | İlk 15 sn'de net vaat ve gerilim kurulabilir mi? |
| 4 | Kişisel bağ | 0.15 | İzleyicinin cebine veya hayatına dokunuyor mu (global İngilizce izleyici)? |
| 5 | Zamanlama | 0.05 | Şu an konuşuluyor mu, tarihsel bir yıldönümü var mı? |
| 6 | Hikâye gerilimi | 0.15 | Kahraman, kötü adam, dönüm noktası var mı? Karakter oynayabiliyor mu? |
| 7 | Görselleştirilebilirlik | 0.10 | 2D animasyonla güçlü anlatılabilir mi (metafor, grafik)? |
| 8 | Raf ömrü | 0.05 | 1 yıl sonra da izlenir mi? |
| | **Toplam** | **1.00** | |

### Kanıtlı talep puan çapaları
| Puan | Kanıt |
|---|---|
| 9–10 | Aynı konu/açı ≥10x outlier (yerel medyan bazlı), en az 2 kanalda |
| 7–8 | ≥3x outlier (yerel medyan bazlı) en az 1 kanalda veya ≥10x ort. bazlı |
| 5–6 | Yalnızca ort. bazlı ≥3x ya da tek kaynaklı [AÖ] outlier |
| 3–4 | Konu nişte işleniyor ama outlier yok; aramada ilgi var |
| 1–2 | Kanıt yok |
Kanıt yalnızca [ÖB] (ajanın genel bilgisi) ise en fazla 4 puan verilir.
v0.2 ek kuralları: izlenmesi <30 B olan outlier çapaya sayılmaz (13x × 773 izlenme gürültüdür); ≤7 günlük video ve komşu sayısı <10 olan skor bir kademe zayıf sayılır; kanalın kendi rutin konusu (fern soygun 1,5x) outlier değil, mutlak talep kanıtıdır.
**Merak çapası (v0.2):** 90 g nişte tarih→gelecek (≥3x %39 ↔ %14), gizli iş modeli (%41, 3 kanal) ve "what happens if/when" (%28) çerçeveleri başlık düzeyinde ölçülen en güçlü sinyaller; bu çerçeveyi gerçekten taşıyan başlık merakta +1 hak eder, paradoks kalıbı (n=19, 0,98x) tek başına etmez.

## Hesap
1. **Merak tavanı: v0.2'de KAPALI.** (v0.1: somut özne yoksa merak ≤6.) 90 g nişte somut özneli başlık medyanı 1,07x, öznesiz 1,05x, ≥3x oranı ikisinde de %15 (n=456/503); 364x'lik en büyük outlier ("What Happens When Economists Run a Country") öznesiz. Somut özne merak puanında yargı olarak kalır, kural olarak değil. Betikte `MERAK_TAVANI_SOMUT_OZNE_YOK = None`.
2. **Ağırlıklı toplam** = Σ puan × ağırlık (1–10 aralığında).
3. **Seri bonusu: +0.3.** Konu, her biri tek başına izlenebilen ve kendi doruk noktası olan ≥2 bölüme bölünebiliyorsa verilir.
   Senaryo başına bir kez uygulanır. Sırf uzatmak için yapılan bölünme bonus almaz.
4. **Rakip benzerlik cezası** (yalnızca en ağır seviye uygulanır, cezalar toplanmaz):
   - `benzer_aci` **−1.5** (v0.2 tanımı, İngilizce kanal): çalışma başlığı, thumbnail metni veya tez kurgusu, aynı konudaki bir rakip outlier'ın başlık çekirdeğini ya da kurgusunu taşıyor (ör. "First to Go Broke" ↔ "Goes Broke First").
   - `dogrudan_ceviri` **−2.0** (v0.2 adı korunur, anlamı): başlık bir rakip başlığın neredeyse birebir aynısı (yalnız sözcük sırası/eşanlamlı değişmiş).
5. **Nihai puan** = ağırlıklı toplam + bonus − ceza, 0–10 aralığına kırpılır, 2 haneye yuvarlanır (ROUND_HALF_UP).
6. **Sert eleme:** Ana iddia doğrulanamıyorsa senaryo **elenir**. Puanı yine gösterilir ama sıralamaya girmez.
7. **Eşitlik:** Önce kanıtlı talep, sonra merak (tavan sonrası), sonra ID sırasına bakılır. Böylece sıralama deterministik olur.

**Milyon olasılığı (v0.2, ayrı etiket, puana girmez) [T]:** taban oran = 90 g nişte <10 B aboneli kanalların ≥1 M videosu 0/186 (≥100 B %3,8; arama yanlılığı nedeniyle üst sınır). Konu kademesi: son 12 ayda <50 B aboneli kanalda aynı konuda ≥500 B video sayısı k. k=0 → <%0,5 · k=1 → %0,5–1 · k≥2 → %1–3; küçük kanalda ≥1 M varsa bir kademe yukarı. 12 ay ufku.

**Eleme akışı:** 10 senaryo → nihai puana göre ilk 5 → finans doğrulama riski olanlar çıkar → ilk 3 → hakem.

**Hook kalite kapısı:** Hook ağırlığı düştü ama hook ortadan kalkmadı. Metin aşamasında ilk 15 sn'de net vaat yoksa
metin kapıdan geçmez (`kalite-kapilari.md` "Metin" satırına eklenmesi önerilir).

## v0 → v0.1 değişiklikleri ve rakip-analizi önerilerinin değerlendirmesi
Kaynak: `rakip-analizi.md` §7. Uyarı: Kanıt zayıf. n≈6 outlier var, medyan yok, sayıların çoğu arama özeti [AÖ].
Bu yüzden önerileri sadece veriye bakarak değil, **mantıkla da savunulabiliyorlarsa** kabul ettim.

| Ölçüt | v0 | v0.1 | Karar | Gerekçe |
|---|---|---|---|---|
| Merak boşluğu | 0.20 | 0.20 | Kabul (aynı) | Değiştirmek için kanıt yok. En büyük iki outlier merak sorusu taşıyor. |
| Kanıtlı talep | 0.15 | 0.15 | Kabul + ölçüm değişikliği | Yerel medyan tabanı yöntem olarak doğru (kanal büyümesini düzeltir). Ağırlık aynı kaldı. |
| Hook gücü | 0.15 | **0.10** | Kabul | Gerekçe veri değil mantık: hook rakiplerde ölçülmedi [ÖB]. Ama senaryo aşamasında hook her konuya yazılabiliyor, yani konular arasında ayırt edici değil. Asıl yeri metin kalite kapısı. |
| Kişisel bağ | 0.15 | 0.15 | Kabul (aynı) | Tek karşı örnek ($75K, ~0.37x, ort. bazlı) global kitleden geliyor ve TR'yi temsil etmiyor. |
| Zamanlama | 0.10 | 0.10 | **Ret** (öneri 0.05) | Seçilim yanlılığı var: outlier'lar "tüm zamanların en çok izlenenleri" özetlerinden toplandı. Ömür boyu izlenmede kalıcı konular yapısal olarak öne çıkar. 5/6 kalıcı sonucu bu yöntemle kaçınılmaz. Ayrıca sıfır aboneli yeni bir kanal için gündem, arama ve önerilerde bulunmanın başlıca yolu olabilir [T], ve formatımızın "haber" ayağı var. |
| Hikâye gerilimi | 0.10 | **0.15** | Kabul | Veri anekdot düzeyinde (BC, OS, EE), ama proje kararıyla örtüşüyor: 2D karakter formatında karakter ancak gerilimli bir olayda "oynayabilir". Hook'tan gelen 0.05 buraya verildi. |
| Görselleştirilebilirlik | 0.10 | 0.10 | Kabul (aynı) | Ayırt edici kanıt yok. |
| Raf ömrü | 0.05 | 0.05 | **Ret** (öneri 0.10) | Zamanlama önerisiyle aynı yanlı kanıta dayanıyor (ömür boyu izlenme listeleri). İkisini birlikte uygulamak aynı yanlılığı iki kez saymak olur. Son 20 videonun medyanı ölçülünce yeniden bakılacak. |

Ek öneriler:

| Öneri | Karar | Gerekçe |
|---|---|---|
| Seri bonusu +0.5 | **Kısmen kabul: +0.3** | Kanıt (OS'te Part 1 > Part 2, n=3, tek kanal) seri içindeki sıralamayı gösteriyor. "Seri, tekil videodan iyi" sonucunu göstermiyor. Küçük bonusun gerekçesi kanal stratejisi (geri dönen izleyici, bölüm sonu bağlantı) [T]. |
| Somut özne yoksa merak ≤6 | Kabul | Rakiplerin başlık çapaları (kişi, ülke, varsayım) [AÖ + ÖB] ile tutarlı ve Türkçe başlıkta da test edilebilir. Ağırlıktan önce tavan olarak uygulanır. |
| Doğrudan çeviri başlığa ceza | Kabul: −2.0 | Benzer açıdan (−1.5) daha ağır. Hem özgünlük hem kopya riski taşıyor. Cezalar toplanmaz, en ağırı uygulanır. |
| Outlier tabanı = yerel medyan | Kabul | Yöntem kaynağı tek (S11), ama tanım olarak ortalamadan sağlam. |
| Zamanlama yalnızca bonus olsun | Ret | Zamanlama ölçüt olarak kaldı (yukarıya bakın). |

## v0.1 → v0.2 kalibrasyonu (2026-11-04, viralite-analisti)
Veri: `uretim/2026-11-04-secim/01-arastirma/olcum/delta90-2026-11-04.json` (90 g, niş n=959, 38 kanal, kanal içi medyan skoru [API][H]). Betik ve çıktı: `uretim/2026-11-04-secim/02-senaryo/viralite-olcum/kalibrasyon90.py` → `kalibrasyon90-cikti.txt`.
| Değişiklik | v0.1 | v0.2 | Kanıt |
|---|---|---|---|
| Zamanlama | 0.10 | **0.05** | Gündem kelimeli başlık (AI/Trump/tarife/2026/Fed, n=158) 1,00x ↔ diğer 1,09x; ≥3x %12 ↔ %15. v0.1'de reddin gerekçesi "ömür boyu liste yanlılığı"ydı; 90 g pencere bu yanlılığı kaldırdı ve veri yine avantaj göstermedi → model değişti. |
| Merak | 0.20 | **0.25** | Çerçeve etkisi başlık düzeyinde en büyük ölçülen fark (tarih→gelecek ≥3x %39 ↔ %14, n=46; gizli iş modeli %41, n=29). Zamanlamadan gelen 0.05 buraya. |
| Somut özne tavanı | merak ≤6 | **kapalı** | 1,07x ↔ 1,05x, ≥3x %15 ↔ %15 (n=456/503). |
| Ceza tanımı | "TR'ye taşıma" | İngilizce rakip başlık/thumbnail/tez çekirdeği | Kanal İngilizce. |
| Talep çapası | — | <30 B izlenmeli outlier sayılmaz; ≤7 g / n<10 bir kademe zayıf | 2026-10-27 ve 11-04 ölçümleri. |
| Milyon olasılığı | yok | ayrı etiket (puana girmez) | Niyazi hedefi; taban 0/186. |
Değişmeyenler: talep 0.15, hook 0.10, kişisel 0.15, hikâye 0.15, görsel 0.10, raf 0.05 (90 g pencerede raf ömrü ölçülemez), seri +0.3 (n=4, kanıt yok, ne lehte ne aleyhte). Etki: 12 senaryoda v0.1 ↔ v0.2 ilk 2 aynı (S03, S01), 3. sıra S08 ↔ S06 yer değiştirdi (fark 0.05).
**Sınırlar:** başlık kalıbı regex'i yalnız başlığı ölçer, konuyu değil; kanal etkisi (gizli iş modeli 3 kanal) ayıklanmadı; ölçütlerin çoğu (hook, hikâye, görsel) başlıktan ölçülemez → bu ağırlıklar hâlâ kalibre edilmedi.

## Kalibrasyon durumu
- **Kalibre edildiği veri:** `rakip-analizi.md` v1 (2026-10-26). 5 global kanal, ≈6 outlier örneği. Hepsi üçüncü taraf
  arama özeti [AÖ] veya buradan yapılmış hesap [H]. Kanal medyanı ölçülemedi (YouTube engelli, API anahtarı yok).
  Hook, thumbnail ve tempo desenleri ölçülmedi [ÖB]. TR'de animasyonlu finans rakibi yok, dolayısıyla TR verisi sıfır.
- **v0.2 (2026-11-04):** 90 g niş verisi ile yalnız merak/zamanlama/tavan kalibre edildi (yukarıdaki tablo). Kendi kanal verisi (CTR/AVD/30 sn tutma) hâlâ yok: `yt-analytics.readonly` kapsamı alınmadı.
- **Güven düzeyi: DÜŞÜK.** Ağırlıklar ±0.05 belirsiz kabul edilmeli. Sıralamada 0.3 puandan küçük farklar anlamlı değil;
  böyle durumda hakem karar verir.
- **Yeniden kalibrasyon tetikleri:**
  1. **YouTube Data API v3 anahtarı** (Niyazi onayıyla, ücretsiz): 5 kanal × son 20 video → yerel medyan outlier'ları.
     Outlier'ların ölçüt puanlarıyla basit korelasyonuna bakılır. Zamanlama ve raf ömrü ağırlıkları ancak o zaman tekrar tartışılır.
  2. **Kendi videolarımızın Studio verisi:** CTR (merak ve thumbnail), ortalama izlenme süresi ve ilk 30 sn tutma (hook ve hikâye).
     İlk ≥5 videodan sonra tahmini puan ile gerçek izlenme/CTR sıralaması karşılaştırılır, ≥10 videoda ağırlıklar
     yeniden ayarlanır. Her kalibrasyon sürüm numarasını artırır (v0.2…) ve burada değişiklik tablosuyla kaydedilir.

## Test
Komutlar (repo kökünden):
```
python3 tools/viralite.py tools/ornek-senaryolar.json > /tmp/v1.txt
python3 tools/viralite.py tools/ornek-senaryolar.json > /tmp/v2.txt
diff /tmp/v1.txt /tmp/v2.txt && sha256sum /tmp/v1.txt /tmp/v2.txt
python3 -c "import sys; sys.path.insert(0,'tools'); import viralite as v; from decimal import Decimal; assert sum(v.AGIRLIK.values())==Decimal('1.00'); print('assert OK: toplam', sum(v.AGIRLIK.values()))"
python3 tools/viralite.py --dokuman docs/viralite-modeli.md
```
Not: Örnek girdideki puanlar betiği test etmek için uydurulmuş değerlerdir. Gerçek senaryo puanı değildir.

Test çıktısı (2026-11-04, **v0.2**, Python 3; aynı komutlar):
```
$ python3 tools/viralite.py tools/ornek-senaryolar.json   # 2 koşu, diff fark yok, sha256 ddece9ea8252 ×2
Viralite modeli v0.2 | ağırlık toplamı = 1.00 | puanlar TAHMİNDİR [T]

| Sıra | ID | Başlık | Ağırlıklı | Bonus | Ceza | Nihai | Not |
|---|---|---|---|---|---|---|---|
| 1 | ORN-1 | Bir simidin 20 yıllık fiyat yolculuğu | 7.05 | +0.00 | −0.00 | **7.05** | - |
| 2 | ORN-2 | Büyük Krizler, Bölüm 1: 2001 | 7.50 | +0.30 | −1.50 | **6.30** | seri +0.3; benzer_aci −1.5 |
| 3 | ORN-3 | Paran neden eriyor? | 7.45 | +0.00 | −2.00 | **5.45** | dogrudan_ceviri −2.0 |
$ ağırlık toplamı assert → assert OK: toplam 1.00
$ python3 tools/viralite.py --dokuman docs/viralite-modeli.md → Doküman tutarlı: 8 ağırlık betikle aynı, toplam 1.00
```
ORN-3 artık tavan almıyor (v0.2'de kapalı). Aşağıdaki çıktı v0.1 kaydıdır (tarihçe).

Test çıktısı (2026-10-26, Python 3.13):
```
$ python3 tools/viralite.py tools/ornek-senaryolar.json   # 1. çalıştırma
Viralite modeli v0.1 | ağırlık toplamı = 1.00 | puanlar TAHMİNDİR [T]

| Sıra | ID | Başlık | Ağırlıklı | Bonus | Ceza | Nihai | Not |
|---|---|---|---|---|---|---|---|
| 1 | ORN-1 | Bir simidin 20 yıllık fiyat yolculuğu | 7.00 | +0.00 | −0.00 | **7.00** | - |
| 2 | ORN-2 | Büyük Krizler, Bölüm 1: 2001 | 7.35 | +0.30 | −1.50 | **6.15** | seri +0.3; benzer_aci −1.5 |
| 3 | ORN-3 | Paran neden eriyor? | 6.80 | +0.00 | −2.00 | **4.80** | merak 9→6 (somut özne yok); dogrudan_ceviri −2.0 |

$ diff v1.txt v2.txt && sha256sum v1.txt v2.txt   # 2. çalıştırma ile karşılaştırma
diff: fark yok (iki çalıştırma aynı)
da1322b7a65e7cc9296d20bf321ef3ec87d7c84ffeb831caa53f08dacae53015  v1.txt
da1322b7a65e7cc9296d20bf321ef3ec87d7c84ffeb831caa53f08dacae53015  v2.txt

$ ağırlık toplamı assert
assert OK: toplam 1.00

$ python3 tools/viralite.py --dokuman docs/viralite-modeli.md
Doküman tutarlı: 8 ağırlık betikle aynı, toplam 1.00
```
Ek negatif kontroller (aynı gün): dokümanda Hook 0.15 yazılınca `--dokuman` "DOKÜMAN TUTARSIZ" verip 1 ile çıktı; 1–10 dışı puan (11) "GİRDİ HATASI" verip 2 ile çıktı; `ana_iddia_dogrulandi=false` olan senaryo "elendi" satırına düştü; 10 puan + seri bonusu 10.00'a kırpıldı; CSV girdisi JSON ile aynı biçimde okundu.
