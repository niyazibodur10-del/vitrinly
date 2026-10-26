# Viralite modeli v0.1

Amaç: senaryoları üretmeden önce viral olma potansiyeline göre sıralamak.
Format kararı: **2D karakter anlatımlı, Türkçe uzun video** (10–20 dk).
**Durum:** Bütün ağırlıklar, bonuslar ve cezalar **tahmindir [T]**. Bkz. "Kalibrasyon durumu".
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
| 1 | Merak boşluğu | 0.20 | Başlık ve thumbnail "ne oldu / ne olacak?" dedirtiyor mu? |
| 2 | Kanıtlı talep | 0.15 | Konu veya açı rakiplerde outlier üretti mi, aramada ilgi var mı? |
| 3 | Hook gücü | 0.10 | İlk 15 sn'de net vaat ve gerilim kurulabilir mi? |
| 4 | Kişisel bağ | 0.15 | İzleyicinin cebine veya hayatına dokunuyor mu (TR izleyici)? |
| 5 | Zamanlama | 0.10 | Şu an konuşuluyor mu, tarihsel bir yıldönümü var mı? |
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

## Hesap
1. **Merak tavanı:** Başlıkta somut bir özne (kişi, ülke, şehir, nesne, kurum) yoksa merak puanı **en fazla 6** olur.
   Bu kural ağırlıklandırmadan önce uygulanır.
2. **Ağırlıklı toplam** = Σ puan × ağırlık (1–10 aralığında).
3. **Seri bonusu: +0.3.** Konu, her biri tek başına izlenebilen ve kendi doruk noktası olan ≥2 bölüme bölünebiliyorsa verilir.
   Senaryo başına bir kez uygulanır. Sırf uzatmak için yapılan bölünme bonus almaz.
4. **Rakip benzerlik cezası** (yalnızca en ağır seviye uygulanır, cezalar toplanmaz):
   - `benzer_aci` **−1.5**: açı, bir rakip videonun kurgusunu veya başlık kalıbını TR'ye taşıyor (ör. "Herkes X'ten gidiyor").
   - `dogrudan_ceviri` **−2.0**: başlık, global bir başlığın doğrudan çevirisi (ör. "Dolar değersiz olsaydı ne olurdu?").
   Animasyonlu TR finans rakibi bulunmadığı için (rakip-analizi §1) bu ceza pratikte global kanallara karşı uygulanır.
5. **Nihai puan** = ağırlıklı toplam + bonus − ceza, 0–10 aralığına kırpılır, 2 haneye yuvarlanır (ROUND_HALF_UP).
6. **Sert eleme:** Ana iddia doğrulanamıyorsa senaryo **elenir**. Puanı yine gösterilir ama sıralamaya girmez.
7. **Eşitlik:** Önce kanıtlı talep, sonra merak (tavan sonrası), sonra ID sırasına bakılır. Böylece sıralama deterministik olur.

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

## Kalibrasyon durumu
- **Kalibre edildiği veri:** `rakip-analizi.md` v1 (2026-10-26). 5 global kanal, ≈6 outlier örneği. Hepsi üçüncü taraf
  arama özeti [AÖ] veya buradan yapılmış hesap [H]. Kanal medyanı ölçülemedi (YouTube engelli, API anahtarı yok).
  Hook, thumbnail ve tempo desenleri ölçülmedi [ÖB]. TR'de animasyonlu finans rakibi yok, dolayısıyla TR verisi sıfır.
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
