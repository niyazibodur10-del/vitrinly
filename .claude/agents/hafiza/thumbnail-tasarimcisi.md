# thumbnail-tasarimcisi — hafıza

## Kurallar

## Dersler

### 2026-10-26 — kanal banner + profil (Financial Rise)
- Banner'da tasarımı belirleyen şey mobil/masaüstü bandı (y 508–931, 2560 tuvalde): jest/el bu bandın dışındaysa görünmez → işaret pozu ELENDİ (el ucu y=1006). Pozu seçmeden önce el/kafa koordinatını bantla ölç. Kaynak: YouTube answer/10456525 (2048'de 1235x338 → x1,25).
- Bel kesitli karakteri banner'da tuvalin altından taşacak kadar büyütmek (boy > H−üst) kafayı büyütür ve yarım kalan elleri bant dışına iter; "karakter alt kenara otursun" ölçeği yetersiz.
- Profil kontrastında yalnız WCAG parlaklığı yanıltır (ten–yeşil 1.11 ama ΔE 92): saç/gömlek siluet kontrastı + ΔE + daire kenarının açık/koyu tema kontrastını birlikte ölç. 36 px'te yüz dairenin ≥%40'ı olmalı; rozet/ikon eklemek 36 px'te okunmuyor (P3 elendi).
- Metni olan arka plan grafiği metnin arkasından geçirme: slogan en kötü %5 kontrast 1.94'e düştü; grafik metnin altına indirilince 12.4.
- Ad/slogan her zaman parametre: kanal adı değişebilir. Sığdırmada önce adı küçült, sloganı koru; tek satır vs iki satırı ayrı ayrı sığdırıp büyük olanı seç (6–20 karakter test).

### 2026-10-27 — S03 1929 thumbnail (F8, 3 finalist: A2 kapılar / B1 kutu / D1 kilitler)
- Mevcut Canva varlıkları yetti (yeni üretim 0): aynı kadrajlı bel üstü pozlarda kafa değişimi (C14 gövde + d-saskin kafa, satırlar ±3 px) duyguyu sıfır maliyetle değiştirir. Önce alfa satır genişliklerini karşılaştır; kayık pozlarda (c-isaret +50 px) yapma.
- Anton'un boşluğu dar: 168x94'te kelimeler birleşiyor (OCR "ONES A"). Kelime kelime çiz, boşluk 0,32 em → OCR 2/4 → 4/4. Kural: her thumbnail metninde geniş boşluk.
- Ölçülebilir okunurluk: 168x94 → x4 büyüt → tesseract (normal + ters çevrilmiş gri, psm 11); tam boyuttaki OCR'ı taban al (araç sınırı: sağa yaslı yığın metinde tam boyutta da kaçırıyor). `09-paket/thumbnail/thumb-test.py` yeniden kullanılabilir.
- Metin ↔ zemin kontrastını p5 (en kötü %5) ile ölç: zincir/kilit gibi kod grafikleri metne değince p5 1,1'e düştü; grafiği metnin altına al (yine aynı ders, ikinci kez — üretimden önce metin kutusunu yasak bölge yap).
- Anlam tutarlılığı: "EVERY DOOR LOCKED" derken görünen her kapı kilitli olmalı (ilk sürümde kahve kapı açıktı). Gerçek ama alarm dili ("EVERY BANK CLOSED") yerine videonun kendi bölüm/oyun dili seçildi. Çapa verisiyle çizilen grafik küçükte üçgen okunuyor → veri grafiği thumbnail'ın kahramanı olmaz. Rakip thumbnail'ları ve onları içeren ızgaralar repo dışında tutulur.

### 2026-11-02 — S08 bütçe thumbnail (F8, A1 −$2,000 / C1 faiz>ordu / B1 hesap makinesi)
- Siyah gömlekli Leo açık/doygun zeminde (sıcak masa, camgöbeği, mercan) kendiliğinden siluet verir; koyu zeminde kaybolur. Zemin rengini önce seç, koyu lacivert yalnız gerekçeyle. Açık zeminde yazı: koyu dolgu + beyaz kontur veya levha (p5 5–17).
- Sahne plakasını thumbnail'a alırken metin bölgesindeki nesneleri (kupa, lamba) kadraj dışına at (ölçek+kırpım), sonra metin arkasına sıcak ışık; p5 1,08 → 5,3.
- OCR psm 11 levhalı/karakterli karede metni kaçırıyor → `thumb-test.py` v2 (bölge OCR + "$→S"); bir sonraki sürüme satır kırpımı psm 7 ekle. Boyut kıyası gerçek oranı abartıyorsa (faiz/ordu %9) kullanma; tek nesne + metin.

### 2026-11-04 — S03 miras F4 erken konsept (K1 WHO GETS IT? / K2 IT LEAKS / K3 SMALLER. LATER. / K4 IT KEEPS LEAKING)
- Görsel yokken metni düz zemin + yer tutucu maketle ölç (`konsept-maket.py`, satır kırpımı psm 7): kesme işaretli kelime ("WHAT'S") 168'de OCR'ı bozuyor; Anton'da "≠" yok; beyaz yazı açık mercanda p5 2,85 → koyu tuğla (#C4402C) şart.
- Konuya özgü rakip ızgarası (8 mqdefault) klişeyi gösterdi (ev + FOR SALE, "BOOMERS", elden ele dolar) → senaryodaki "iki el" fikri rakibe yakın çıktı, elendi. Konsepte başlamadan sorgu kümesinin ızgarasına bak.
