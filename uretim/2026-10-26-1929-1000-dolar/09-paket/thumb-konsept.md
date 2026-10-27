# F4 — Thumbnail konseptleri (taslak) · S03 "You Have $1,000 in 1929. Can You Keep It?"

**Hazırlayan:** youtube-paketleyici (bu tur; koordinatör kararı) · **Tarih:** 2026-10-27
**Devir:** thumbnail-tasarimcisi F8'de render karelerinden (ya da Canva `generate-image`, referans = karakter sayfası) 3 varyantı 1280x720 üretir, 168x94 / kontrast / rakip yan yana testlerini **gerçek görsel üzerinde** yapar. Bu dosya konsept yazısıdır; metin ölçüleri bir okunurluk modelinden gelir [Ö-model], piksel ölçümü değildir.
**Başlık sabit:** "You Have $1,000 in 1929. Can You Keep It?" (H5). 3 thumbnail YouTube Studio "Test & Compare" ile denenir; tek değişken thumbnail. Başarı ölçütü Studio'nun izlenme süresi payı (viralite.md §7).
Etiketler: **[RÖ]** rakip-ozet.md (2026-10-27) · **[Ö]** betik · **[Ö-model]** betikteki okunurluk modeli · **[T]** yargı.

---

## 0. Karar: rakipte 6–11 kelime gözlemi ↔ bizim "≤4 kelime" kuralı

**Gözlem [RÖ D4]:** Aile 1 (belgesel portre) thumbnail'larında metin 6–11 kelime (ör. "THE TRUE ORIGIN OF THE GREAT DEPRESSION: WHAT HISTORIANS GET WRONG"); bu videolar 199–873 B izlenmede.
**Karar: ≤4 kelime kuralı korunur; uzun metinli varyant Test & Compare'e girmez.** Gerekçe:
1. **Uzun metin bir kanal ailesinin imzası, nişin kuralı değil.** 7 örneğin 5'i tek kanaldan (Markets of the Past), 2'si Uncover Things'ten [RÖ D4] → kanal etkisi ayrılamıyor. Aynı aileden 4 kelimelik varyant da 199 B yaptı ("1929 WASN'T THE REAL CAUSE"). Aile 2'nin outlier'ları (Financial Dynasty 349 B "WHO OWNS LONDON?", 3 kelime) kısa metinli [RÖ D4].
2. **Uzun metin o kalıbın parçası ve kalıp doygun.** "Real reason / true origin / get wrong" başlıkları n=119'da medyan 0,55 [RÖ §4]; Aile 1 şablonu küçük konuda 12.809'da kaldı (Income Tax). Siyah-beyaz yüz + beyaz kutulu uzun metin, rakip-özet §6'da "yapma" listesinde (kopyalamama).
3. **168x94'te okunmuyor (ölçüldü, model).** 1280x720 tuvalde metin kutusu Leo'nun yüzüne yer bırakacak şekilde (genişlik %55, yükseklik %45, en çok 3 satır) sınırlanınca, 66 karakterlik rakip metni yalnız ~58 px büyük harf yüksekliğine sığıyor → 168x94'te **~7,6 px** (eşik ≥9 px) [Ö-model, §4]. Bizim 3 finalistin en küçüğü 14,0 px (B), A ve C 18,5 px.
4. **Başlığı tekrar etme kuralı.** Uzun metin, başlığın zaten söylediğini ikinci kez söyler; thumbnail'ın işi başlığı tamamlamak.
**Gerekçeli istisna yok.** Uzun metin ancak F12'de kendi CTR verimiz kısa metnin altında kalırsa, ayrı bir testte yeniden düşünülür (veri olmadan kural değişmez).

**Viralite §7 önerisiyle fark:** viralite-analisti (c) "rakip Aile 1 tipi uzun metin" önermişti. Yukarıdaki 4 gerekçeyle yerine **(C) karşıtlık/kanıt sayısı** konsepti kondu: rakibin çalışan kısmı (tek kanıt nesnesi + tek büyük sayı) alındı, kopya riski taşıyan kısmı (portre + uzun metin) alınmadı.

---

## 1. Ortak kurallar (3 konsept)

- **Tek özne + tek kanıt nesnesi** [RÖ D4]: özne her zaman Leo (sıcak ışıkta, renkli), kanıt nesnesi her varyantta tek: A kapılar (tek blok), B ayakkabı kutusu, C borsa çizgisi.
- **Leo karakter kartına birebir** (`assets/karakter/karakter-karti.md`): siyah yakası açık gömlek, kollar sıvalı, sol bilekte siyah saat, kısa koyu sakal. Yüz kare yüksekliğinin **≥%30'u** (≥216 px/720) → 168x94'te yüz ≥28 px [T].
- **Sunucu Leo kaybetmez** (H2): üzüntü, aşağılanma, panik ifadesi yok. Şaşkınlık/merak/ciddiyet var.
- **Renk dili videoyla aynı:** mavi = borsa, yeşil = banka, kahve = ayakkabı kutusu; soğuk arka plan + sıcak karakter (stil kararı). Metin beyaz, siyah kontur (≥8 px) veya koyu bant üstünde; vurgu rengi tek: sıcak sarı `#FFD23F` (koyu lacivertte yüksek parlaklık kontrastı; kırmızı lacivert üstünde düşük kalır [T, F8'de ölçülecek]).
- **Yerleşim:** metin üst yarıda ve Leo'nun karşı tarafında; **sağ alt köşe boş** (süre damgası ~%15 x %12) [T]. Kenar güvenli payı ≥%5.
- **Metin kodla yazılır**, AI'ye yazdırılmaz (thumbnail-tasarimcisi kuralı). Yazı tipi yerel, kalın/dar (ör. `video/public/fonts` içindeki kanal başlık fontu).
- **Politika (F8 monetizasyon kontrolü için):** kan, çöküş felaketi, ağlayan yüz, gerçek kişi (Roosevelt dahil), gerçek banka adı/logosu yok (G1, G6). "Kutu kazandı" bugüne dönük okunmasın diye B'de yıl çapası görselde var (1929 damgası). Videoda olmayan nesne/olay yok.

---

## 2. Konseptler

### A — "Üç kapı" (obje/oyun açısı; hook'un ilk karesi)
- **Kompozisyon:** koyu lacivert yarışma stüdyosu, üstten sıcak spot. Sağ üçte birde Leo (bel üstü, 3/4 dönük), sol üçte ikide yan yana **üç dev kapı**: mavi / yeşil / kahve. Kapılarda yazı yok; her kapının üstünde tek, basit ikon (düşen çizgi / sütunlu bina / kutu) ve büyük beyaz "?" (videodaki "DISASTER? GAMBLE? SURPRISE?" anının sadeleşmiş hali). Kahve kapının aralığından ince sıcak ışık sızıyor (sürpriz ipucu, cevabı vermez).
- **Leo pozu:** sunum/işaret pozu: bir kolu kapılara uzanmış, kaşlar kalkık, yarım gülüş ("Let's play" anı, S01). Karakter sayfasındaki "işaret etme" pozu.
- **Kanıt nesnesi:** üç kapı (tek blok olarak okunur), Leo'nun öbür elinde ince bir banknot destesi ($1,000; üstünde rakam yok).
- **Metin (2 alternatif):** A1 "PICK A DOOR" (3 kelime) · **A2 "ONE IS A DISASTER" (4 kelime) → SEÇİLDİ.** Gerekçe: görüntü "kapı seç"i zaten söylüyor; A1 bilgi eklemiyor. A2 bahsi (stakes) ekliyor ve videonun kendi etiketi (S01 "one door is a disaster"; G1: mecaz, görsel şok yok). Okunurluk ikisinde de eşiğin üstünde (§4). Metin üstte, kapıların üzerinde tek satır; "DISASTER" sarı.
- **Başlıkla okunuş:** "You have $1,000 in 1929. Can you keep it?" + "ONE IS A DISASTER" + 3 kapı → "hangisi?" sorusu. Başlığı tekrar etmiyor, tamamlıyor.
- **168x94 düşüncesi:** üç kapı renk bloğu olarak okunur (kapı ~25 px genişlik); ikonlar ~10 px'te sınırda → ikon yerine "?" işaretleri büyük tutulur. Leo yüzü sağda ≥28 px.
- **Kaynak kare:** S01 0:02–0:17 stüdyo/kapı sahnesi (F7 render) veya S04 klonlar kapılarda (klonlar thumbnail'da yok; tek Leo).

### B — "Ayakkabı kutusu" (duygu açısı; yakın plan yüz)
- **Kompozisyon:** Leo göğüs üstü yakın plan, kadrajın sol yarısı; yüz kare yüksekliğinin ~%40'ı. Ellerinde açık ayakkabı kutusu, içinden sıcak altın ışık yüzüne vuruyor (banknotlar kutuda, rakam yok). Arka plan: soğuk, flu sepya 1929 sokağı + arkada aralık duran kahve kapı. Kutunun yan yüzünde damga "1929" (yıl çapası; görselin parçası, metin sayısına girmez mi? → **sayılır**, aşağıya bakın).
- **Leo pozu:** şaşkın → sevinçli geçiş anı (S12 "his money got stronger"): kaşlar kalkık, ağız hafif açık, gözler kutuda. Aşırı sevinç/zafer pozu değil (tavsiye okumasını azaltmak için) [T].
- **Kanıt nesnesi:** ayakkabı kutusu.
- **Metin (2 alternatif):** **B1 "THE SURPRISE DOOR" (3 kelime) → SEÇİLDİ** · B2 "1929'S SURPRISE WINNER" (3 kelime). Gerekçe: B2 cevabı veriyor (kutu kazandı) ve "winner + parlayan nakit" ikilisi bugüne dönük "nakit kazanır" okumasına en yakın kombinasyon (G4). B1 hook'taki "one is a surprise" ile aynı dili kullanıyor, merakı açık bırakıyor. Kutunun üstündeki "1929" damgası metinle birlikte **4 kelime** eder (sınırın içinde).
- **Başlıkla okunuş:** "Can you keep it?" + parlayan kutu + "THE SURPRISE DOOR" → "kutu mu? nasıl?" Başlığı tekrar etmiyor.
- **168x94 düşüncesi:** en güçlü küçük boyut adayı: büyük yüz + tek parlak nesne. Risk: sepya arka plan Leo'nun siyah gömleğiyle birleşebilir → saç/gömlek kenarına sıcak arka ışık (rim light).
- **Kaynak kare:** S12 Box Leo kutu anı (render) veya Canva "taban + düzenleme" ile yeni poz (karakter kartı yöntemi).

### C — "Borsa grafiği" (karşıtlık/kanıt sayısı açısı)
- **Kompozisyon:** koyu lacivert zemin. Sol yarıda büyük mavi Dow çizgisi: önce yukarı (1921–29), tepe noktası, sonra derin düşüş (1932 dibi); çizginin dibinde büyük sayı. Sağda Leo (bel üstü), çizginin dibini işaret ediyor. Arkada çok soluk üç kapı silueti (seri bağı; okunmasa da olur).
- **Leo pozu:** ciddi/şaşkın sunucu (S15 düşünen ciddi poz değil, sunucu işaret pozu + kaşlar yukarı). Kaybeden değil, gösteren (H2). Stock Leo klonu kullanılmaz.
- **Kanıt nesnesi:** Dow çizgisi + tek sayı.
- **Metin (2 alternatif):** **C1 "STOCKS −89%" (2 kelime) → SEÇİLDİ** · C2 "$1,000 → $108" (2 kelime). Gerekçe: C2'deki 108 $ yalnız "price only, before dividends" alt notuyla doğru (D1); thumbnail'da bu not 168x94'te okunamaz → **yanıltıcı sayı riski**, elendi. C1'deki −89 % Dow fiyat endeksinin tepe→dip düşüşü (381.17 → 41.22, FRH-29), alt not gerektirmez. "−89%" sarı, "STOCKS" beyaz.
- **Başlıkla okunuş:** "You have $1,000 in 1929. Can you keep it?" + "STOCKS −89%" → ilk kapının sonucunu gösterir, diğer ikisini açık bırakır (merak: "banka? kutu?"). Spoiler kapı 1 için: videoda 2:53'te zaten açıklanıyor [T].
- **168x94 düşüncesi:** en kısa metin, en büyük punto. Risk: rakip Aile 1'e (düşen grafik + kırmızı ok) benzeyebilir → kırmızı yerine sarı/mavi, renkli Leo, portre yok. F8 yan yana testinde karışırsa C değiştirilir (yedek fikir: Bank Leo kilitli kapı önünde + "MARCH 1933").
- **Kaynak kare:** S15 G1 tam grafik (render) + sunucu Leo (S16 sunum pozu).

---

## 3. Elenen konseptler

| Konsept | Neden elendi |
|---|---|
| Rakip Aile 1 tipi uzun metin (viralite §7 c) | §0: 168x94'te ~7,6 px [Ö-model], kanal etkisi, doygun kalıp, kopyalamama listesi |
| Üç Leo klonu yan yana (Stock/Bank/Box) | Aynı karede 3 karakter tek özne kuralını bozar; Canva'nın en zayıf noktası (H4), 168x94'te üç küçük yüz okunmaz |
| Skor tablosu ($108 / ? / $1,272) | 3 sayı + alt notlar: 168x94'te okunmaz, ayrıca $108 alt not gerektirir (D1); kutunun "kazanan" sayısı bugüne dönük okunabilir |
| 1929 vs 2026 ayna grafiği | Uzun videonun vaadi 1929; 2026'yı thumbnail'a taşımak G4 kırmızı çizgisine yaklaşır ve başlığın yıl sınırını bozar (Shorts 2'nin işi) |

---

## 4. Test (kapı: metin ≤4 kelime ya da gerekçeli istisna; yasaklı/clickbait/tavsiye 0)

Betik: `09-paket/paket-kontrol.py` (aşağıdaki `veri` bloklarını okur). **Okunurluk modeli [Ö-model]:** 1280x720 tuvalde metin kutusu genişlik 704 px (%55), yükseklik 324 px (%45), en çok 3 satır, satır aralığı 1,15, kalın-dar yazı tipinde harf genişliği ≈ 0,55 × büyük harf yüksekliği; kelimeler satırlara dengeli bölünür, sığan en büyük punto seçilir; 168/1280 ölçeğiyle mobil büyük harf yüksekliği hesaplanır; eşik ≥9 px [T: 168x94'te kalın büyük harfin okunur alt sınırı varsayımı; F8'de gerçek küçültmeyle doğrulanacak]. Kutudaki "1929" damgası B için ayrıca sayılır.

<!-- veri:thumb-metin-secilen -->
```text
A|ONE IS A DISASTER
B|THE SURPRISE DOOR|1929
C|STOCKS −89%
```

<!-- veri:thumb-metin-alternatif -->
```text
A1|PICK A DOOR
B2|1929'S SURPRISE WINNER
C2|$1,000 → $108
RAKIP-AILE1|THE TRUE ORIGIN OF THE GREAT DEPRESSION: WHAT HISTORIANS GET WRONG
```

Çıktı: `paket-taslak.md` §8.1 (aynı betik, tek koşu iki dosyayı da ölçer).

**F8'e devir (thumbnail-tasarimcisi'nin gerçek testleri):** 168x94 küçültme kontrol sayfası (3 varyant + başlık metniyle birlikte), metin/zemin kontrast oranı (≥4.5:1 hedef) ve Leo silueti ΔE, rakip outlier thumbnail'larıyla yan yana ızgara (i.ytimg.com, repoya girmez), dosya ≤2 MB. Konsept değişikliği gerekirse gerekçe `thumb-rapor.md`'ye.
