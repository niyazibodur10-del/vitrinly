# Bölüm 001 — fiyat ve risk doğrulaması (finans-dogrulayici, 2026-11-10)

İLERLEME: tamam.
**KARAR: DÜZELT** — 1 zorunlu düzeltme (bisiklet seçeneği BANK'a sığmıyor), 4 önerilen not. Metindeki 3 fiyat ABD ikinci el piyasası için gerçekçi.
- Girdi: `bolum-001/metin.md` sha256 af5e95aabb75 · `seri-incili.md` sha256 332561229d2e.
- Rakam kapsama testi (regex, §2–§6): `$100, $80, $20, $40, $1,000,000` + yazıyla `one hundred, eighty, forty, million` → 5/5 aşağıdaki tabloda, `[RAKAM?]` kalmadı.
- Hesap betikle tekrarlandı (`python3 -c` BANK zinciri, aşağıda §3).
- Tavsiye / hızlı zengin ol / yasa dışı / marka-karalama taraması: tavsiye dili 0, gerçek marka 0, kişi 0. 3 güvenlik notu Bölüm 2 metnine (§4).
- Etiketler: **[K]** kaynaklı (sayfa okundu) · **[AÖ]** arama özeti (çok kaynak, sayfa açılmadı) · **[T]** tahmin / bizim hesabımız.

---

## 1. Rakam tablosu
| # | İddia (metin) | Değer / birim | Kaynak | Durum | Düzeltme |
|---|---|---|---|---|---|
| R1 | BANK başlangıç | $100 nakit | Kurgu girdisi (konsept) | doğru | — |
| R2 | Hedef | $1,000,000 | Kurgu girdisi | doğru (hedef, vaat değil) | — |
| R3 | Patlak lastikli yol bisikleti ilanı | $80 alış | [AÖ] Bike Forums: $65 Fuji, $160 OBO çelik yol bisikleti; düz lastik fiyatı düşürür. [K] underpriced.app: ucuz bisiklet $50–100 bandında, "department store bikes… $50–100 profits", satış süresi 7–21 gün | doğru (fiyat) | Fiyat gerçekçi; **ama sonuç zarfı BANK'a sığmıyor → D1** |
| R4 | Tahta: $100 − $80 = $20 | $20 kalan | Aritmetik [T] | doğru | D1 seçilirse $40 olur |
| R5 | "That's most of our money" | 80/100 = %80 | Aritmetik | doğru | $60'ta da doğru (%60) |
| R6 | Bedava masif şifonyer (alış) | $0 | [AÖ] FB Marketplace "Free" filtresi; taşınan/yenilenen evlerden bedava masif mobilya yaygın (underpriced, Penny Hoarder, Sawdust2Stitches) | doğru | — |
| R7 | Şifonyer yeniden satış (Bölüm 2 için) | boyalı masif şifonyer $150–275 | [AÖ] Sawdust2Stitches $175 (birkaç saatte satıldı); underpriced 2026 rehberi $25 alış → $275 satış; Hometalk yorumcusu "$200+, ama Marketplace ucuza gider"; AptDeco ilan fiyatları $350–750 (ilan, satış değil) | doğru aralık | Bölüm 2'de **$150–200** önerilir (bkz. R9 kuralı) |
| R8 | "rent a truck, buy paint" (tutar yok) | kamyonet $19/75 dk (Home Depot Load 'N Go, sınırsız mil) veya U-Haul pickup $19,95 + ~$0,69–0,99/mil → yerel iş ~$30–45; boya + zımpara ~$25–40 | [AÖ] Home Depot: movebuddha, thisoldhouse, thepricer (2026); U-Haul: hireahelper 2026, thepricer. Boya [T] | doğru (metinde rakam yok) | Bölüm 2: toplam masraf **$45–85** yaz; kiralama ≥21 yaş + ehliyet + sigorta (Jake 26 → uygun) |
| R9 | §4.5 kâr tavanı ile şifonyer | maliyet $44–85 → kaynaksız tavan net ≤ $44–85 | Aritmetik [T] | dikkat | $150–200 satış R7 kaynaklarıyla savunulur; $275 üst uç "Marketplace ucuz gider" yorumuyla iyimser, kullanma |
| R10 | Garaj satışı kapalı oyun kutusu | $40 | [AÖ] racketboy forum: "big box of games marked $20" garaj satışında; Flip Weekly: garaj satışında $15 harcama → ~$285 liste değeri (anekdot); underpriced: "Typical Sourcing Cost $1–50", ortalama satış "$15–500+" | doğru | $30–50 bandının içinde, değişiklik gerekmez |
| R11 | "forty bucks of scratched discs" | $40 | R10 ile tutarlı | doğru | — |
| R12 | §9 "Marketplace yerel satışta ücret yok" | %0 yerel, %10 kargolu | [AÖ] vendoo, litcommerce, closo, inspiretothrive (2025–2026 tutarlı) | doğru | Kargolu satışta %10 yazılmalı (min. ücret kaynaklarda çelişkili: $0,40/$0,80 → rakam yazma) |
| R13 | Kutu tek tek eBay'de satılırsa (Bölüm 2) | eBay video oyun FVF ~%13,6 + $0,30–0,40/sipariş | [AÖ] litcommerce, ecomcalctools; çelişen %12 / %13,25 / %10,9 değerleri var | doğrulanamadı (tam oran) | Bölüm 2'de oran yazma, "eBay takes a cut" de; ya da yerel satış (ücretsiz) seç |
| R14 | §9 Apartment Therapy "bedava 6 çekmeceli + ~$40 yenileme" | — | Yazarın arama özeti, sayfa açılmadı | doğrulanamadı | R7 kaynaklarıyla değiştir |

## 2. Sonuç zarfı (§7) kontrolü — yön kilidi gerçekçi mi?
| Seçenek | Zarf | Hesap [T] | Durum |
|---|---|---|---|
| ROAD BIKE $80 | "lastik ve iç lastik beklenenden pahalı" | BANK $20. 2 iç lastik $10–24 [AÖ: $5–12/adet], 2 dış lastik + 2 iç $60–164 [AÖ: lastik $25–70/adet] → BANK **−$4 ile −$40** | **KIRMIZI**: §4.3 ve §4.8 ihlali (BANK eksiye düşer / gizli borç) |
| FREE DRESSER | kira + boya parayı yer, en yüksek fiyat, en geç nakit | masraf $44–85 → BANK $15–56; satış $150–200 → BANK ~$165–255 | YEŞİL (zarf tutarlı) |
| MYSTERY BOX $40 | çoğu sıradan, 1–2 iyi parça, başa baş–küçük kâr | BANK $60; sıradan disk $3–10 [T, kaynaklarda tekil örnek yok] | YEŞİL (anti-hype yön doğru) |
| Kutu + şifonyer | BANK'a sığarsa | $40 + $44–85 = $84–125 | SARI: üst uçta sığmaz; zarf "sığarsa" dediği için tutarlı |

## 3. DÜZELT listesi (satır satır)
**D1 (zorunlu) — bisiklet BANK uyumu.** Senaryo-yazari seçer:
- **A (önerilen): fiyatı $60 yap.** Gerçekçi [AÖ: $50–100 bandı], BANK $40 kalır, "beklenenden pahalı lastik" zarfı karşılanır. Değişecek satırlar: M06 "Eighty bucks." → "Sixty bucks." · S4 ilan kartı "ROAD BIKE · $80" → "$60" · tahta "$100 − $80 = $20" → "$100 − $60 = $40" · S8 seçim kartı "ROAD BIKE $80" → "$60" · §1 E1, §8 tablo, §9. J05 "most of our money" doğru kalır.
- B: $80 kalsın, zarf değişsin: "yalnız iç lastikler patlak, iki iç lastik ~$15–20 (kendileri takar), BANK ~$0–5'e iner, satış gecikir". Gerilim yüksek ama sıfır nakitle kalmak kötü örnek; §4.8 sınırında.
- C: $80 kalsın, lastik masrafı Bölüm 2'de "seçenek dışı" ek kararla karşılansın (ör. önce başka bir şey satmak). Hikâyeyi uzatır, önerilmez.
**D2 (önerilen) — §9 dayanak tablosu:** R14'ü R7 kaynaklarıyla değiştir; kutu satırı "[AÖ] $20–40 garaj kutuları" ile güncellenir; satırlar "[RAKAM?]" değil "[AÖ] doğrulandı" olur.
**D3 (önerilen) — incil §4.3 "satış vergisi" maliyet listesinde:** ABD'de eBay/Marketplace satış vergisini alıcıdan tahsil eder (marketplace facilitator); bireysel garaj satışında satıcı maliyeti değildir. "satış vergisi (alışlarda)" diye daralt. [AÖ, genel bilgi; kişiye özel vergi bilgisi verilmez]
**D4 (önerilen) — incil §4.7 "vergi aşama 4'ten":** yasal olarak kâr ilk satıştan vergiye tabidir; hikâyede anılmaması sorun değil ama "vergi yok" ima edilmesin (ör. "tax-free money" repliği yasak).
**D5 (önerilen) — incil §3 zaman çizelgesi** ($100 → ~$900k, 2–3 yıl): kurgu için kabul, ama "hızlı zengin ol" okumasını azaltmak için açıklamadaki "Fiction." satırı her bölümde kalmalı ve BANK aşama 4'ten sonra "şirket nakdi" diye etiketlenmeli (incil §3 aşama 4 satırı zaten "şirket nakdi" diyor). Ek değişiklik gerekmez.

## 4. Risk taraması
| Alan | Bulgu | Durum | Öneri |
|---|---|---|---|
| Yatırım tavsiyesi | "you should / buy / guaranteed / invest" 0; CTA açık uçlu soru | YEŞİL | — |
| Hızlı zengin ol | Başlık "$100 to $1,000,000" bir hedef; zarflar küçük/orta kâr, kayıp kuralı (§4.6) var; "Fiction. Not financial advice." 3 açıklamada var | YEŞİL | Alternatif güvenli başlık (isteğe bağlı): "Two Friends, $100, a Million-Dollar Goal — You Decide · Ep. 1" / "Can $100 Become $1,000,000? You Decide Every Move · Ep. 1" |
| Yasa dışı / güvensiz al-sat | Bisiklet: çalıntı riski. Şifonyer: CPSC geri çağrısı olan şifonyeri satmak federal yasaya aykırı [AÖ: cpsc.gov geri çağırma bildirimleri "do not sell or give away"]; devrilme riski; 1978 öncesi boyayı kuru zımparalama kurşun riski [T, EPA genel bilgisi]. Kutu: risk yok | SARI (Bölüm 2) | Bölüm 2 rutin olarak göster (tavsiye diye değil): Jake seri numarasını kontrol eder (çalıntı kaydı); şifonyer ilanında "solid wood, no brand" — geri çağrılmış model/marka gösterilmez; boyamada maske + açık hava |
| Marka / karalama | Gerçek marka, kişi, platform kötülemesi yok; ilan kartları logosuz; "telefon logosuz" | YEŞİL | Bölüm 2'de oyun kartuşlarında gerçek konsol/oyun logosu ve kamyonette U-Haul/Home Depot logosu kullanma |
| "Mystery box" | Kumar çağrışımı düşük: fiziksel lot, fiyat açık, zarf sıradan sonuç | YEŞİL | — |
| Yasal not | IG/YT/TikTok açıklamalarında "Fiction. Not financial advice." var | YEŞİL | İsteğe bağlı ek: "Prices are illustrative US secondhand estimates." (monetizasyon-uyum-uzmani ile) |

## 5. Kaynaklar
- Bisiklet: bikeforums.net/classic-vintage-bicycles-whats-worth-appraisals/799293 · m.bikeforums.net/showthread.php?p=23217920 · underpriced.app/blog/bicycles-flipping-guide [K]
- Lastik/iç lastik: favoritebikes.com (lastik maliyet rehberi) · leoguarbikes.com (2025) · bikeshop.as.ucsb.edu
- Şifonyer: sawdust2stitches.com/dresser-makeoverflip · underpriced.app/blog/how-to-flip-furniture-for-profit-complete-guide-2026 · hometalk.com (Solid Maple Dresser) · thepennyhoarder.com/make-money/side-gigs/flipping-furniture
- Kamyonet: movebuddha.com/blog/home-depot-truck-rental-review · thisoldhouse.com/moving/home-depot-truck-rental · hireahelper.com (U-Haul 2026) · thepricer.org
- Oyun kutusu: racketboy.com/forum/viewtopic.php?p=747762 · Flip Weekly (beehiiv) · underpriced.app/blog/video-games-flipping-guide [K] · jordoncox.com (bundle rehberi)
- Ücretler: blog.vendoo.co · litcommerce.com/blog/facebook-marketplace-fees · ecomcalctools.com (eBay video games)
- Geri çağırma: cpsc.gov/Recalls/2026 (şifonyer devrilme bildirimleri)
