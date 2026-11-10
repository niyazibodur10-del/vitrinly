# Bölüm 001: "Every Dollar We Have"

İLERLEME: tamam (metin v1). Sıradaki: finans-dogrulayici fiyat onayı (§9) ‖ monetizasyon-uyum-uzmani ‖ ses-yonetmeni iki ses.
**KAPI ÖZETİ** (`python3 veri/metin-kontrol.py --yaz`, girdi `veri/satirlar.py` sha256 952323bcb19b):
- Kelime **186** (Jake 98, Mike 79, birlikte 9). Süre: tek tip 160 kpm ile **83,2 sn**, karakter bazlı (Jake 150 / Mike 170) **84,1 sn** → GEÇTİ (60–90).
- İlk replik 0,4 sn'de, çarpma sesi 0,2 sn'de (≤2) → GEÇTİ. Seri tanıtımı 8,7 sn (≤10) → GEÇTİ.
- Son replik CTA = "What should we do? Tell us in the comments." → GEÇTİ. Yasak kelime (telaffuz + etkileşim yemi + yatırım), replikte rakam: 0 → GEÇTİ.
- BANK: $100 bütün bölüm (harcama yok). Mekân: yalnız L1 Kitchen (en ucuz pilot).
- Ses ölçülünce 88 sn'yi aşarsa kesme sırası: (1) M11 + J11 "fun part / scary part" (−3,3 sn) (2) J04 + M05 "hear me out" şakası (−5 sn).

---

## 1. Adaylar ve eleme

### 3 açılış/kanca (ölçüt: ilk 2 sn'de durdurma ×2, 3 sn'de konsept netliği, yorum çekme, üretim maliyeti, formata uyum; 1–5)
| Aday | Özet | Durdurma ×2 | Netlik | Yorum | Maliyet | Format | Toplam |
|---|---|---|---|---|---|---|---|
| **A1 ÇARPMA** ✔ | 0,2 sn: Mike 100 doları tezgâha çarpar (SLAM), BANK: $100 belirir. "That's it. Every dollar we have." Jake: "Rent's paid. Fridge has mustard." | 5×2 | 4 | 3 | 5 | 5 | **27** |
| A2 TAHTA SIFIRLARI | Mike tahtaya $1,000,000 yazar, Jake sıfırları tek tek siler: "$100. Let's start here." | 3×2 | 5 | 3 | 5 | 4 | 23 |
| A3 İLERİ SARMA | Gelecekte bir depoda kutlama, "Episode 100?", geri sarma: "But first… $100." | 4×2 | 3 | 2 | 2 | 1 | 16 |

Gerekçe: A1 tek karede hareket + ses + para nesnesi + çatışmanın tohumu verir. "Rent's paid" çizgisi, kiranın riske atılmadığını söyler (sorumsuz para örneği olmaz). A2'nin gagı güçlü ama ilk 2 sn yazı yazmakla geçiyor ve okunmayı gerektiriyor; tahta fikri tanıtıma (S2) taşındı. A3 ek mekân ister ve geleceği önceden gösterir; "kararı sen verirsin" vaadiyle çelişiyor → elendi.

### 3 bitiş/seçim (ölçüt: viral potansiyel, yorum çekme gücü, seçeneklerin eşit cazibesi, üretim, politika; 1–5)
| Aday | Özet | Viral | Yorum gücü | Eşit cazibe | Üretim | Politika | Toplam |
|---|---|---|---|---|---|---|---|
| **E1 ÜÇ İLAN** ✔ | Yol bisikleti $80 (lastik patlak) / bedava masif şifonyer (bugün alınmalı, araba küçük, boya + kamyonet) / garaj satışı kapalı kutu eski oyunlar $40 | 4 | 5 | 4 | 4 | 5 | **22** |
| E2 TAKIM JAKE – TAKIM MIKE | "Hepsini tek ürüne mi yatıralım, beşe mi bölelim, yoksa 50'şer dolarla yarışalım mı?" | 4 | 4 | 3 | 5 | 4 | 20 |
| E3 10 SANİYELİK TEKLİF | Garaj satışında satıcı: "$100, whole box, ten seconds." Al ya da yürü | 4 | 3 | 3 | 2 | 3 | 15 |

Gerekçe: E1 somut, görsel ve herkesin fikri olan üç eşya sunar. Seçenekler izleyiciye gerekçe yazdırır ("bike sells fast in spring", "box = sell games one by one") ve seçenek dışı fikre kapı açar (kutuyu al + şifonyeri de al). Her seçenekte artı ve bedel yüksek sesle söylenir. Bisiklet hız/Mike, şifonyer güvenlik/Jake, kutu merak/joker. E2 takım kimliği kuruyor ama soyut kalıyor; "all-in" çerçevesi kumar tınısı taşıyor. Takım dinamiği E1'e zaten gömülü (Mike'ın bisikleti, Jake'in şifonyeri). E3 ikili seçim yorumu daraltır. "10 saniye" baskısı 24 saatlik pencereyle çelişir, tüm BANK'ı tek kutuya yatırmak kötü örnek olur ve ek mekân (L3) ister → elendi.

---

## 2. Sahne sahne metin (9:16)

Zamanlar betikten (`veri/zaman.md`), karakter bazlı model. BANK her karede üst-solda.

| # | Zaman | Mekân / açı | Konuşan | Replik | Duygu / ifade | Kamera notu | BANK |
|---|---|---|---|---|---|---|---|
| S1 | 0,0–5,6 | L1-C insert → L1-A | — | *(0,2 sn: SLAM, banknot tezgâha)* | — | Tezgâh üstü sert insert, el + banknot. Darbede 2 karelik sarsıntı | **$100** sayaç "pop" ile belirir |
| | | | MIKE | That's it. Every dollar we have. | Kararlı, gözler parlak, avuç banknotun üstünde | Mike'ın yüzüne hızlı punch-in | $100 |
| | | | JAKE | Rent's paid. Fridge has mustard. That's everything. | Deadpan, mısır gevreği kasesi elinde, kaşık havada | Jake'e kesme. "Fridge" deyince açık buzdolabında tek hardal şişesi insert (0,5 sn) | $100 |
| S2 | 6,1–14,8 | L1-B buzdolabı tahtası | MIKE | Two best friends. One hundred bucks. | Kameraya, sırıtarak; tahtaya "$100" yazar | İkili, kameraya bakış (dördüncü duvar) | $100 |
| | | | JAKE | One slightly crazy goal. | Kuru, tek kaş kalkık | Jake yakın | $100 |
| | | | MIKE | A million dollars. | Coşkulu; tahtaya "$1,000,000" yazar, kalem gıcırdar | Tahtaya hızlı zoom, sıfırlar tek tek "tık" | $100 |
| | | | JAKE | And we don't make the moves. You do. | Ciddi-sıcak, kameraya parmakla işaret | "You do" anında kameraya doğru hafif dolly-in. Logo yok, ekranda "YOU DECIDE" yazısı 1 sn | $100 |
| S3 | 15,4–22,6 | L1-A tezgâh | MIKE | Okay. Three flips. Hear me out. | Telefonu iki eliyle uzatır, heyecanlı | Telefonla birlikte Mike'a kadraj, ekranda 3 ilan küçük kart | $100 |
| | | | JAKE | Every bad idea starts with hear me out. | Gözlerini devirir, kollar bağlı | Jake tek | $100 |
| | | | MIKE | And every good one! | Parmak kaldırır, sırıtır | Hızlı geri kesme | $100 |
| S4 | 23,1–35,0 | L1-A + telefon grafiği | MIKE | One. A road bike. Eighty bucks. Flat tires, but look at that frame! | Âşık gibi telefona bakar | Telefon ekranı tam kadraj: ilan kartı "ROAD BIKE · $80 · flat tires" | $100 |
| | | | JAKE | That's most of our money on a bike that can't roll. | Düz, kalemi tahtaya vurur | Tahtada "$100 − $80 = $20" yazar | $100 |
| | | | MIKE | Air is free, Jake. | Omuz silker, kendinden emin | İkili | $100 |
| | | | JAKE | Tires aren't. | Yüz ifadesiz, tek göz kırpışı | Jake yakın, 0,3 sn sessiz tutuş (gag) | $100 |
| S5 | 35,6–52,3 | L1-A + telefon + grafik | JAKE | Two. A solid wood dresser. Free. We paint it, flip it. | Hafif gülümseme: "benim seçeneğim" | Jake telefonu alır. İlan kartı "DRESSER · FREE · must go today" | $100 |
| | | | MIKE | Free? What's the catch? | Şüpheli, gözler kısılmış | Mike yakın | $100 |
| | | | JAKE | It has to go today. And we have a tiny car. | Biraz mahcup | Pencereden dışarı panlama → minik hatchback silueti + şifonyer silueti karşılaştırma grafiği (0,8 sn sessiz) | $100 |
| | | | MIKE | So we rent a truck, buy paint, and wait. Slow. | Parmakla sayar, sıkılmış | Ekranda üç ikon belirir: truck, paint, clock | $100 |
| | | | JAKE | Slow. But safe. | Sakin, kararlı | Jake yakın, hafif push-in | $100 |
| S6 | 52,9–64,6 | L1-A + telefon | MIKE | Three. A mystery box of old video games. Forty bucks. | Gizemli fısıltıyla eğilir | İlan kartı "GARAGE SALE BOX · $40 · old games". Kutu kapağı hafif sallanır (soru işareti) | $100 |
| | | | JAKE | Could be a gem. Could be forty bucks of scratched discs. | Kuşkulu, iki elini terazi gibi tartar | Split: altın parıltı / çizik disk yığını | $100 |
| | | | MIKE | That's the fun part! | Kollar açık, coşkulu | Mike yakın | $100 |
| | | | JAKE | That's the scary part. | Düz | Jake yakın, ayna kompozisyon | $100 |
| S7 | 65,8–76,7 | L1-A tezgâh | — | *(1,0 sn: ikisi aynı anda banknota uzanır, iki el banknotun iki ucunda)* | Gergin, gözler birbirinde | Tezgâh seviyesinden alçak açı, iki el yakın; gerilim sesi | $100 |
| | | | MIKE | Jake, we don't need more money. We need guts. | Ciddi, öne eğilmiş | Mike'a omuz üstü | $100 |
| | | | JAKE | A price tag is just a number. Value is what somebody actually pays. | Sakin, gözünü kaçırmaz | Jake'e omuz üstü | $100 |
| | | | JAKE | Fine. We let them decide. | İç çeker, banknotu bırakır | Banknot tezgâhta ikisinin ortasında kalır | $100 |
| S8 | 77,5–84,1 | L1-A → kameraya | BOTH | What should we do? Tell us in the comments. | İkisi aynı anda kameraya döner; Mike sırıtır, Jake kaşını kaldırır | İkili, merkez. Seçim kartı alt üçte birde belirir: **ROAD BIKE $80 · FREE DRESSER · MYSTERY BOX $40** | $100 |
| | 81,1–84,1 | kart | — | — | Kare donar | Kart: **"Ep. 2 drops tomorrow"** (2–3 sn), "ding" | $100 |

Seçim kartı kuralları: etiket isimdir, harf ya da numara değildir (seri incili §5.1). Ekranda "comment X" ya da oy talimatı yoktur.

---

## 3. Replikler (TTS'ye girecek temiz metin)

Dosyalar: `veri/jake.txt`, `veri/mike.txt`, `veri/both.txt` (betik üretir; ID sekmesi + metin). Sahne talimatı yok, sayılar yazıyla.

### JAKE (13 satır, 98 kelime)
```
J01 Rent's paid. Fridge has mustard. That's everything.
J02 One slightly crazy goal.
J03 And we don't make the moves. You do.
J04 Every bad idea starts with hear me out.
J05 That's most of our money on a bike that can't roll.
J06 Tires aren't.
J07 Two. A solid wood dresser. Free. We paint it, flip it.
J08 It has to go today. And we have a tiny car.
J09 Slow. But safe.
J10 Could be a gem. Could be forty bucks of scratched discs.
J11 That's the scary part.
J12 A price tag is just a number. Value is what somebody actually pays.
J13 Fine. We let them decide.
```
### MIKE (12 satır, 79 kelime)
```
M01 That's it. Every dollar we have.
M02 Two best friends. One hundred bucks.
M03 A million dollars.
M04 Okay. Three flips. Hear me out.
M05 And every good one!
M06 One. A road bike. Eighty bucks. Flat tires, but look at that frame!
M07 Air is free, Jake.
M08 Free? What's the catch?
M09 So we rent a truck, buy paint, and wait. Slow.
M10 Three. A mystery box of old video games. Forty bucks.
M11 That's the fun part!
M12 Jake, we don't need more money. We need guts.
```
### BOTH (ikisi de üretilir, üst üste miks; yedek yol: Mike ilk cümle, Jake ikinci)
```
B01 What should we do? Tell us in the comments.
```
TTS notları: J04'te "hear me out" alıntıdır, Jake hafif taklit tonuyla okur. J06 "Tires aren't." öncesi ve sonrası 0,3 sn boşluk. M03 "A million dollars." sonunda yükselen ton.

---

## 4. Görsel istek listesi (gorsel-varlik-sanatcisi)

Tek mekân: **L1 THE KITCHEN**, 3 sabit açı (A geniş tezgâh ikili, B buzdolabı tahtası, C tezgâh insert). Karakter görünüşü ve kıyafeti seri incili §1'e göre.

| Sahne | Arka plan / açı | JAKE poz + ifade | MIKE poz + ifade | Prop / grafik |
|---|---|---|---|---|
| S1 | L1-C insert, L1-A | Taburede oturur, kase + kaşık havada; deadpan | Ayakta, avucu banknotun üstünde, öne eğik; kararlı-heyecanlı | 100 dolar banknotu (yakın plan), mısır gevreği kasesi, açık buzdolabı içi (tek hardal) |
| S2 | L1-B | Tahtanın yanında, kollar bağlı → kameraya işaret; kuru → sıcak-ciddi | Kalemle tahtaya yazarken, kameraya dönük; sırıtma | Beyaz tahta: "$100" ve "$1,000,000" (iki durum), marker kalem, "YOU DECIDE" metin kartı |
| S3 | L1-A | Kollar bağlı, göz devirme | Telefonu iki eliyle uzatmış; heyecan. Parmak kaldırma | Telefon (logosuz) + 3 küçük ilan kartı |
| S4 | L1-A + telefon tam ekran | Kalemi tahtaya vurur; düz. Yüz ifadesiz yakın plan (Tires aren't) | Telefona hayran bakış; omuz silkme | İlan kartı: yol bisikleti, patlak lastik, "$80". Tahtada "$100 − $80 = $20" |
| S5 | L1-A + pencere dışı | Hafif gülümseme, telefon elinde; mahcup omuz; sakin-kararlı yakın | Şüpheli kısık göz; parmakla sayma, sıkılmış | İlan kartı: masif ahşap şifonyer "FREE · must go today"; minik hatchback ve şifonyer silueti grafiği; ikonlar: truck, paint can, clock |
| S6 | L1-A + telefon | İki eli terazi gibi; kuşkulu. Düz yakın plan | Öne eğilip fısıldama; kollar açık coşku | İlan kartı: karton kutu "GARAGE SALE BOX · $40"; split grafik: parlayan oyun kartuşu / çizik disk yığını |
| S7 | L1-A alçak açı | Eli banknotun ucunda, göz teması; iç çekip bırakma | Eli banknotun öbür ucunda, öne eğik, ciddi | Banknot yakın (iki el), tezgâh seviyesi |
| S8 | L1-A, kameraya | Kameraya dönmüş, tek kaş kalkık | Kameraya dönmüş, sırıtma | Seçim kartı (3 etiket), "Ep. 2 drops tomorrow" kartı, BANK sayacı (seri şablonu) |

Toplam benzersiz poz: Jake 10, Mike 10, ortak ikili 3. Tekrar kullanılacak seri varlıkları: L1 üç açı, BANK sayacı, seçim kartı, "Ep. N drops tomorrow" kartı, THE BOARD.

---

## 5. Başlık önerileri (3)
| # | Başlık | Karakter | Not |
|---|---|---|---|
| T1 ✔ | $100 to $1,000,000 — You Make Every Move · Ep. 1 | 48 | Formatı anlatır, pilot için en iyisi. YouTube Shorts başlığı |
| T2 | Bike, Dresser, or Mystery Box? You Pick Our First Flip | 54 | Somut merak + yorum çağrısı. IG/TikTok ilk satırı |
| T3 | Two Friends. $100. You Decide Everything. (Ep. 1) | 49 | Yedek / A-B testi |

## 6. Açıklama + hashtag taslakları

**Instagram (Reels)**
```
Bike, dresser, or mystery box? You pick our first flip. 🚲📦
Jake & Mike have $100 and one goal: $1,000,000. Every episode, the comments decide the next move.
What should they do? Tell us in the comments. Ep. 2 drops tomorrow.
Comments may be shown on screen with your username.
Fiction. Not financial advice. Voices are AI-generated.
#flipbyvote #animatedseries #sidehustle #flipping #youdecide
```
**YouTube Shorts** (başlık T1)
```
Jake & Mike start with $100. The goal: $1,000,000. You decide every move.
Episode 1: a road bike, a free dresser, or a mystery box of old games. What should they do? Tell us in the comments. Ep. 2 drops tomorrow.
Comments may be shown on screen with your username.
Fiction. Not financial advice. Voices are AI-generated.
#Shorts #flipbyvote #animation
```
**TikTok**
```
Bike, dresser, or mystery box? You pick our first flip. Ep. 1 of $100 → $1,000,000. Tell us in the comments. Fiction, not financial advice. AI voices.
#flipbyvote #animation #sidehustle #reselling #youdecide
```
(Emoji yalnız IG açıklamasında, isteğe bağlı. "Comment to win", ödül ya da etiketleme isteği yok.)

---

## 7. Sonuç zarfı (yayından önce kilitli; seri incili §5.4)
Yön kilitlidir; rakamlar finans-dogrulayici onayından sonra Bölüm 2 metninde yazılır.
- **ROAD BIKE:** lastik ve iç lastik beklenenden pahalıya gelir, zincir de yağ ister. Satılır ama ilk alıcı gelmez. Sonuç küçük kâr; BANK birkaç gün sonra biraz artar.
- **FREE DRESSER:** kamyonet kirası ve boya parayı yer; boyama bir hafta sonu sürer. Satış yavaştır ama en yüksek fiyatla olur. Sonuç orta kâr, en geç nakit.
- **MYSTERY BOX:** çoğu sıradan oyun çıkar, bir-iki iyi parça vardır. Tek tek satış emek ister. Sonuç başa baş ile küçük kâr arası.
- **Seçenek dışı ipucu:** "kutuyu al + şifonyeri de al" ($40 + kira/boya) BANK'a sığarsa kabul edilir (incil §7).

## 8. Seçenek dengesi (eşit cazibe testi)
| Seçenek | Artı (aloud) | Bedel (aloud) | Değer | Kimin |
|---|---|---|---|---|
| Road bike $80 | "look at that frame", hızlı satılır izlenimi | "most of our money", "Tires aren't" (free) | hız | Mike |
| Free dresser | bedava, "Slow. But safe." | bugün alınmalı, küçük araba, kamyonet + boya, yavaş | güvenlik | Jake |
| Mystery box $40 | ucuz, "could be a gem" | "scratched discs", belirsiz | merak | joker |

## 9. Fiyat dayanağı (finans-dogrulayici onayına) — bütün satırlar [tahmin], onay bekliyor
| Fiyat | Dayanak [arama özeti 2026-11-10] | Durum |
|---|---|---|
| Patlak lastikli yol bisikleti $80 (ilan fiyatı) | Bike Forums ve fleamarketflipper anekdotları: ucuz ikinci el bisikletler 50–100 dolar bandında alınıyor; Marketplace yerel satışta ücret yok | [RAKAM?] satılmış ilanlarla doğrulanacak |
| Bedava şifonyer | Apartment Therapy: Marketplace'te bedava 6 çekmeceli şifonyer + ~40 dolarlık yenileme. Underpriced: 30 dolarlık şifonyer + 25 dolar malzeme | kaynaklı örnek var; kamyonet kirası tutarı yazılmadı |
| Garaj satışı oyun kutusu $40 | kaynak yok | [RAKAM?] doğrulanacak; doğrulanamazsa $30–50 bandına çekilir |
Bölüm 1'de BANK değişmez; bu fiyatlar yalnız seçim kartında ve repliklerde geçer.

## 10. Test sonuçları
- `python3 veri/metin-kontrol.py --yaz` → çıkış 0; 5/5 kapı GEÇTİ (yukarıdaki özet).
- Telaffuz grep (charts|complicated|scenarios|truth|crashes|bold): 0. Etkileşim yemi grep (win, giveaway, prize, tag a friend, comment yes, like if, subscribe…): 0. Yatırım grep (invest, stock, crypto, guarantee): 0.
- İlk 2 sn: SLAM 0,2 sn, replik 0,4 sn. Tanıtım ≤10 sn: 8,7 sn. Son replik CTA, ardından "Ep. 2 drops tomorrow".
- Risk / sonraki ajana not: (1) Süre kpm tahmine dayanıyor; ses-yonetmeni gerçek TTS süresini ölçsün, >88 sn ise kesme sırası özetin başında. (2) Kutu fiyatı kaynaksız → finans-dogrulayici. (3) "Tell us in the comments" Meta etkileşim yemi tanımına yakın; hikâyeyi gerçekten değiştiren tek açık uçlu soru olarak bırakıldı, nihai karar monetizasyon-uyum-uzmani'nde.
