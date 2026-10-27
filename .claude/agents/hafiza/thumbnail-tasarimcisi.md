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
