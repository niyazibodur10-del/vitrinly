# Bölüm 001: "Every Dollar We Have"

İLERLEME: tamam (metin v2, koordinatör düzeltmeleri 2026-11-10 uygulandı). Sıradaki: ses-yonetmeni `bolum.txt` → `tools/ses/diyalog.py`.
**KAPI ÖZETİ** (`python3 veri/metin-kontrol.py --yaz`, girdi `veri/satirlar.py` sha256 f43b288eb7f1, çıkış 0):
- Kelime **179** (Jake 99, Mike 80). Süre: tek tip 160 kpm ile **82,6 sn**, karakter bazlı (Jake 150 / Mike 170) **83,4 sn** → GEÇTİ (60–90). Boşluk modeli `tools/ses/diyalog.py` ile aynı: yanıtlayan Jake 0,42, Mike 0,22, aynı konuşmacı 0,45.
- Çarpma sesi 0,2 sn'de, ilk replik 0,6 sn'de (≤2) → GEÇTİ. Seri tanıtımı 9,0 sn (≤10) → GEÇTİ.
- Son: soru seçenekleri adıyla soruyor ("Bike, dresser, or mystery box?") + "Tell us in the comments." → GEÇTİ. Yasak kelime/rakam taraması: 0 → GEÇTİ.
- BANK: $100 bütün bölüm boyunca. Mekân: yalnız L1 Kitchen (geniş + buzdolabı/tahta).
- v2 değişiklikleri: bisiklet $80 → $60 (doğrulama D1-A); bölüme özgü kapanış sorusu; "Ep. 2: YOUR call" kartı; paket metni; görsel kısıta göre sadeleştirme; M11 + J11 ("fun part / scary part") yeni boşluk modelinde süre payı için çıkarıldı (87,0 → 83,4 sn).
- Ses ölçümü 88 sn'yi aşarsa sıradaki kesme: J04 + M05 "hear me out" şakası (−5 sn).

---

## 1. Adaylar ve eleme

### 3 açılış/kanca (ölçüt 1–5: ilk 2 sn'de durdurma ×2, 3 sn'de konsept netliği, yorum çekme, üretim maliyeti, formata uyum)
| Aday | Özet | Durdurma ×2 | Netlik | Yorum | Maliyet | Format | Toplam |
|---|---|---|---|---|---|---|---|
| **A1 ÇARPMA** ✔ | 0,2 sn: 100 dolar tezgâha çarpar (SLAM), BANK: $100 belirir. Mike: "That's it. Every dollar we have." Jake: "Rent's paid. Fridge has mustard." | 5×2 | 4 | 3 | 5 | 5 | **27** |
| A2 TAHTA SIFIRLARI | Mike tahtaya $1,000,000 yazar, Jake sıfırları tek tek siler: "$100. Let's start here." | 3×2 | 5 | 3 | 5 | 4 | 23 |
| A3 İLERİ SARMA | Gelecekte bir depoda kutlama, "Episode 100?", geri sarma: "But first… $100." | 4×2 | 3 | 2 | 2 | 1 | 16 |

Gerekçe: A1 tek karede hareket, ses, para nesnesi ve çatışmanın tohumunu verir. "Rent's paid" kiranın riske atılmadığını söyler (sorumsuz para örneği olmaz). A2'nin gag'ı güçlü ama ilk 2 sn yazı yazmakla geçiyor; tahta fikri tanıtıma (S2) taşındı. A3 ek mekân istiyor ve geleceği önceden gösterip "kararı sen verirsin" vaadiyle çelişiyor; elendi.

### 3 bitiş/seçim (ölçüt 1–5: viral potansiyel, yorum çekme gücü, eşit cazibe, üretim, politika)
| Aday | Özet | Viral | Yorum gücü | Eşit cazibe | Üretim | Politika | Toplam |
|---|---|---|---|---|---|---|---|
| **E1 ÜÇ İLAN** ✔ | Yol bisikleti $60 (lastikler patlak) / bedava masif şifonyer (bugün alınmalı, araba küçük, boya ve kamyonet gerekir) / garaj satışından kapalı kutu eski oyunlar $40 | 4 | 5 | 4 | 4 | 5 | **22** |
| E2 TAKIM JAKE – TAKIM MIKE | "Hepsini tek ürüne mi yatıralım, beşe mi bölelim, yoksa 50'şer dolarla yarışalım mı?" | 4 | 4 | 3 | 5 | 4 | 20 |
| E3 10 SANİYELİK TEKLİF | Garaj satışında satıcı: "$100, whole box, ten seconds." Al ya da yürü | 4 | 3 | 3 | 2 | 3 | 15 |

Gerekçe: E1 somut, görsel ve herkesin fikri olan üç eşya sunuyor. İzleyiciye gerekçe yazdırıyor ve seçenek dışı fikre kapı açıyor. Bisiklet hızı (Mike), şifonyer güvenliği (Jake), kutu merakı (joker) temsil ediyor. E2 soyut kalıyor ve "all-in" çerçevesi kumar tınısı taşıyor; takım dinamiği zaten E1'e gömülü. E3 yorumu ikili seçime daraltıyor, 24 saatlik pencereyle çelişiyor, bütün BANK'ı tek kutuya bağlıyor ve ek mekân istiyor; elendi.

---

## 2. Sahne sahne metin (9:16)

**Görsel kısıt (koordinatör 2026-11-10):** her karakter için 1 konuşma tabanı (bel üstü; Jake kadraj sağına, Mike soluna dönük), 3 ağız durumu (kapalı / yarı / açık) ve sayfadaki 6 ifade portresi (önden). Portreler: nötr, sıcak gülümseme, şaşkın, endişeli, heyecanlı, düşünceli. Mekân: L1 geniş plan + buzdolabı/tahta plakası. Banknot, telefon, kalem, ilan kartı, ikon ve tahta yazısı **kodla** eklenir. Yeni poz yok.

**Çekim sözlüğü:**
- GENİŞ: mutfak geniş plakası, iki konuşma tabanı karşılıklı (Jake solda, Mike sağda), ağızlar Rhubarb'la oynar.
- YAKIN-J / YAKIN-M: aynı tabana kodla punch-in.
- PORTRE-J:ifade / PORTRE-M:ifade: önden ifade portresi. Ağzı oynamaz, yalnız konuşmayan tepki anında veya kısa kesmede kullanılır (≤1 sn).
- TAHTA: buzdolabı/tahta plakası, yazı kodla "elle yazılıyor" efektiyle.
- KOD-PROP: kadraja kodla giren nesne.
- Kod hareketi: punch-in, sarsıntı, nefes salınımı, eğilme (ölçek/kaydırma).

Zamanlar betikten (`veri/zaman.md`, karakter bazlı model). BANK her karede üst-solda.

| # | Zaman sn | Çekim | Konuşan | Replik | Duygu / ifade | Kamera + kod-prop | BANK |
|---|---|---|---|---|---|---|---|
| S1 | 0,0–0,6 | GENİŞ | — | *(0,2 sn: SLAM)* | — | KOD-PROP 100 dolar banknotu üstten düşüp tezgâha çarpar; 2 karelik kamera sarsıntısı | **$100** sayaç "pop" ile belirir |
| | 0,6–2,7 | YAKIN-M | MIKE | That's it. Every dollar we have. | kararlı, heyecanlı | Hızlı punch-in | $100 |
| | 3,1–5,9 | YAKIN-J | JAKE | Rent's paid. Fridge has mustard. That's everything. | kuru, düz | "mustard" anında KOD-PROP küçük hardal şişesi ikonu Jake'in yanında "pop" (0,5 sn) | $100 |
| S2 | 6,4–8,5 | TAHTA → YAKIN-M | MIKE | Two best friends. One hundred bucks. | heyecanlı | Tahtada kodla "$100" yazılır, sonra Mike'a kesme | $100 |
| | 8,9–10,5 | YAKIN-J | JAKE | One slightly crazy goal. | düz → (kesme) PORTRE-J:düşünceli 0,5 sn | Yakın, hafif push-in | $100 |
| | 10,8–11,8 | TAHTA | MIKE (dış ses) | A million dollars. | — | Tahtada kodla "$1,000,000" yazılır, sıfırlar tek tek "tık"; hızlı zoom | $100 |
| | 12,2–15,4 | YAKIN-J → PORTRE-J:sıcak gülümseme | JAKE | And we don't make the moves. You do. | ciddi, sonra sıcak | "You do" anında portreye kesme (önden = kameraya bakış), ekranda "YOU DECIDE" yazısı 1 sn | $100 |
| S3 | 16,0–18,1 | GENİŞ | MIKE | Okay. Three flips. Hear me out. | heyecanlı | KOD-PROP telefon alttan kadraja girer, ekranında 3 küçük ilan kartı | $100 |
| | 18,5–21,7 | YAKIN-J | JAKE | Every bad idea starts with hear me out. | düz, gözler hafif kısık (taban) | Statik | $100 |
| | 21,9–23,3 | PORTRE-M:sıcak gülümseme → YAKIN-M | MIKE | And every good one! | sırıtma | Portreden konuşan tabana kesme | $100 |
| S4 | 24,0–28,6 | Telefon tam ekran → YAKIN-M | MIKE | One. A road bike. Sixty bucks. Flat tires, but look at that frame! | heyecanlı | KOD-PROP ilan kartı "ROAD BIKE · $60 · flat tires" tam kadraj, sonra Mike | $100 |
| | 29,0–33,4 | YAKIN-J + TAHTA ek | JAKE | That's most of our money on a bike that can't roll. | düz | Kadraj köşesinde tahta: kodla "$100 − $60 = $40" | $100 |
| | 33,6–35,0 | GENİŞ | MIKE | Air is free, Jake. | kendinden emin | Nefes salınımı | $100 |
| | 35,4–36,2 | YAKIN-J | JAKE | Tires aren't. | düz | Sert punch-in, sonra 0,3 sn sessiz tutuş (gag) | $100 |
| S5 | 37,0–41,4 | YAKIN-J → telefon | JAKE | Two. A solid wood dresser. Free. We paint it, flip it. | düz-memnun → PORTRE-J:sıcak gülümseme 0,5 sn | KOD-PROP ilan kartı "DRESSER · FREE · must go today" | $100 |
| | 41,6–43,0 | PORTRE-M:şaşkın → YAKIN-M | MIKE | Free? What's the catch? | şüpheli | Portre 0,5 sn, sonra konuşan taban | $100 |
| | 43,4–47,8 | YAKIN-J | JAKE | It has to go today. And we have a tiny car. | düz → PORTRE-J:endişeli (sessiz arada) | Ardından 0,8 sn sessiz grafik: minik hatchback silueti ↔ şifonyer silueti (kod) | $100 |
| | 48,9–52,4 | YAKIN-M | MIKE | So we rent a truck, buy paint, and wait. Slow. | sıkılmış | KOD-PROP üç ikon sırayla: truck, paint can, clock | $100 |
| | 52,8–54,0 | YAKIN-J | JAKE | Slow. But safe. | sakin | Hafif push-in | $100 |
| S6 | 54,5–58,1 | YAKIN-M → telefon | MIKE | Three. A mystery box of old video games. Forty bucks. | gizemli, sesi alçalır | Kod eğilme (Mike kadraja doğru ölçeklenir). KOD-PROP ilan kartı "GARAGE SALE BOX · $40 · old games", kutu kapağı titrer | $100 |
| | 58,5–62,9 | YAKIN-J | JAKE | Could be a gem. Could be forty bucks of scratched discs. | kuşkulu | Split KOD-PROP: parlayan kartuş ikonu / çizik disk yığını ikonu | $100 |
| S7 | 62,9–64,1 | GENİŞ | — | *(1,0 sn sessiz)* | iki taban birbirine bakar | KOD-PROP banknot ikisinin ortasında tezgâhta; yavaş push-in, gerilim sesi | $100 |
| | 64,1–67,3 | YAKIN-M | MIKE | Jake, we don't need more money. We need guts. | ciddi | Omuz hizası, kod eğilme öne | $100 |
| | 67,7–72,9 | YAKIN-J | JAKE | A price tag is just a number. Value is what somebody actually pays. | sakin, kararlı | Statik, banknot kadraj altında | $100 |
| | 73,4–75,4 | PORTRE-J:düşünceli → YAKIN-J | JAKE | Fine. We let them decide. | iç çeker | Portre 0,5 sn (sessiz kısım), konuşan tabana kesme | $100 |
| S8 | 76,2–77,9 | GENİŞ | MIKE | Bike, dresser, or mystery box? | heyecanlı | Kod: kamera ikisinin ortasına ilerler. Seçim kartı alt üçte birde belirir: **ROAD BIKE $60 · FREE DRESSER · MYSTERY BOX $40** | $100 |
| | 78,4–80,4 | GENİŞ | JAKE | Tell us in the comments. | düz-sıcak | Kart açık kalır | $100 |
| | 80,4–83,4 | PORTRE-M:heyecanlı + PORTRE-J:düşünceli (yan yana) | — | — | ikisi kameraya bakar (önden portreler = dönüş anı) | Kare donar. Kart: **"Ep. 2: YOUR call"**, "ding" | $100 |

Seçim kartı kuralları: etiket isimdir, harf ya da numara değildir (incil §5.1). Ekranda "comment X" ya da oy talimatı yoktur. Kapanış kartında gün sözü yoktur (incil §5.7).

---

## 3. Replikler (TTS'ye girecek temiz metin)

- **Ses-yonetmeni girdisi:** `bolum.txt` (JAKE:/MIKE: biçimi, `tools/ses/diyalog.py`). Parantez, yalnız ek sessizlik gereken satırda boşluğu ezer (otomatik boşluk + sessiz vuruş). Betik üretir, elle düzenlenmez.
- Karakter listeleri: `veri/jake.txt`, `veri/mike.txt` (ID sekmesi + metin). Sahne talimatı yok, sayılar yazıyla.
- Kapanış sorusunu Mike sorar, Jake bitirir: diyalog.py iki sesi üst üste desteklemiyor.

### JAKE (13 satır, 99 kelime)
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
J12 A price tag is just a number. Value is what somebody actually pays.
J13 Fine. We let them decide.
B02 Tell us in the comments.
```
### MIKE (12 satır, 80 kelime)
```
M01 That's it. Every dollar we have.
M02 Two best friends. One hundred bucks.
M03 A million dollars.
M04 Okay. Three flips. Hear me out.
M05 And every good one!
M06 One. A road bike. Sixty bucks. Flat tires, but look at that frame!
M07 Air is free, Jake.
M08 Free? What's the catch?
M09 So we rent a truck, buy paint, and wait. Slow.
M10 Three. A mystery box of old video games. Forty bucks.
M12 Jake, we don't need more money. We need guts.
B01 Bike, dresser, or mystery box?
```
TTS notları: J04'te "hear me out" alıntıdır, Mike'ı hafifçe taklit eder. J06 "Tires aren't." sonrası 0,3 sn gag boşluğu kurguda eklenir. M03 dış sestir (tahta çekimi).

---

## 4. Görsel istek listesi (gorsel-varlik-sanatcisi) — yeni poz: 0
| Sahne | Plaka | JAKE varlığı | MIKE varlığı | Kod-prop / grafik |
|---|---|---|---|---|
| S1 | GENİŞ | konuşma tabanı | konuşma tabanı | 100 dolar banknotu (düz, logosuz illüstrasyon), hardal ikonu, BANK sayacı |
| S2 | TAHTA, GENİŞ | taban; portre düşünceli, sıcak gülümseme | taban | Tahta yazıları "$100", "$1,000,000" (kodla yazılır), "YOU DECIDE" metni |
| S3 | GENİŞ | taban | taban; portre sıcak gülümseme | Telefon (logosuz) + 3 mini ilan kartı |
| S4 | GENİŞ, TAHTA köşe | taban | taban | İlan kartı "ROAD BIKE · $60 · flat tires" (bisiklet ikonu/illüstrasyonu), tahta "$100 − $60 = $40" |
| S5 | GENİŞ | taban; portre sıcak gülümseme, endişeli | taban; portre şaşkın | İlan kartı "DRESSER · FREE · must go today", hatchback ↔ şifonyer silueti, ikonlar truck / paint can / clock |
| S6 | GENİŞ | taban | taban (kodla eğilme) | İlan kartı "GARAGE SALE BOX · $40 · old games" (karton kutu), parlayan kartuş ikonu / çizik disk yığını ikonu (logosuz) |
| S7 | GENİŞ | taban; portre düşünceli | taban | Banknot tezgâhta (S1 varlığı) |
| S8 | GENİŞ | taban; portre düşünceli | taban; portre heyecanlı | Seçim kartı (3 etiket), "Ep. 2: YOUR call" kartı |

Kullanılan portreler: Jake 3 (düşünceli, sıcak gülümseme, endişeli), Mike 3 (sıcak gülümseme, şaşkın, heyecanlı). Seri varlığı olarak kalanlar: BANK sayacı, seçim kartı, "Ep. N: YOUR call" kartı, ilan kartı şablonu, tahta yazı efekti. Gerçek marka, konsol ya da oyun logosu yok (doğrulama §4).

---

## 5. Başlık önerileri (3)
| # | Başlık | Karakter | Not |
|---|---|---|---|
| T1 ✔ | $100 to $1,000,000 — You Make Every Move · Ep. 1 | 48 | Formatı anlatır, pilot için en iyisi. YouTube Shorts başlığı. Uyum: YEŞİL (politika §7.4) |
| T2 | Bike, Dresser, or Mystery Box? You Pick Our First Flip | 54 | Somut merak ve yorum çağrısı. IG/TikTok ilk satırı |
| T3 | Two Friends. $100. You Decide Everything. (Ep. 1) | 49 | Yedek / A-B testi |

## 6. Açıklama + hashtag taslakları

**Instagram (Reels)**
```
Bike, dresser, or mystery box? You pick our first flip.
Jake & Mike have $100 and one goal: $1,000,000. Every episode, the comments decide the next move.
Bike, dresser, or mystery box? Tell us in the comments.
We may feature your comment in the next episode. Prefer to stay anonymous? Just say so in your comment.
Fiction. Not financial advice. Voices and visuals are AI-generated.
#flipbyvote #animatedseries #sidehustle #flipping #youdecide
```
**YouTube Shorts** (başlık T1)
```
Jake & Mike start with $100. The goal: $1,000,000. You decide every move.
Episode 1: a road bike, a free dresser, or a mystery box of old games. Tell us in the comments.
We may feature your comment in the next episode. Prefer to stay anonymous? Just say so in your comment.
Fiction. Not financial advice. Voices and visuals are AI-generated.
#Shorts #flipbyvote #animation
```
**TikTok**
```
Bike, dresser, or mystery box? You pick our first flip. Ep. 1 of $100 → $1,000,000. Tell us in the comments.
We may feature your comment in the next episode. Prefer to stay anonymous? Just say so in your comment.
Fiction. Not financial advice. Voices and visuals are AI-generated.
#flipbyvote #animation #sidehustle #reselling #youdecide
```
Açıklamalarda "comment to win", ödül, etiketleme isteği ya da gün sözü yok.

---

## 7. Sonuç zarfı (yayından önce kilitli; incil §5.4)
Yönler kilitli. Rakamlar Bölüm 2 metninde, doğrulama.md aralıklarıyla yazılır.
- **ROAD BIKE ($60, BANK $40 kalır):** lastik ve iç lastik beklenenden pahalı çıkar, zincir de yağ ister. Bisiklet satılır ama ilk alıcı gelmez. Sonuç: küçük kâr, BANK birkaç gün sonra biraz artar. Jake seri numarasını rutin olarak kontrol eder (doğrulama §4).
- **FREE DRESSER:** kamyonet kirası ve boya toplam $45–85 tutar (doğrulama R8), boyama bir hafta sonu sürer. Satış yavaştır ama en yüksek fiyatla olur ($150–200, R7). Sonuç: orta kâr, nakit en geç gelir. Boyama açık havada ve maskeyle yapılır.
- **MYSTERY BOX ($40):** çoğu sıradan oyun çıkar, bir-iki iyi parça vardır. Tek tek satış emek ister. Sonuç: başa baş ile küçük kâr arası. eBay oranı yazılmaz (R13).
- **Seçenek dışı ipucu:** "kutuyu al + şifonyeri de al" $84–125 tutar. Kabul ancak BANK'a sığarsa olur (incil §7).

## 8. Seçenek dengesi (eşit cazibe testi)
| Seçenek | Artı (yüksek sesle söylenir) | Bedel (yüksek sesle söylenir) | Değer | Kimin |
|---|---|---|---|---|
| Road bike $60 | "look at that frame" | "most of our money", "Tires aren't" (free) | hız | Mike |
| Free dresser | bedava, "Slow. But safe." | bugün alınmalı, küçük araba, kamyonet + boya, yavaş | güvenlik | Jake |
| Mystery box $40 | ucuz, "could be a gem" | "scratched discs", belirsiz | merak | joker |

## 9. Fiyat dayanağı (finans-dogrulayici, `dogrulama.md`)
| Fiyat | Dayanak | Durum |
|---|---|---|
| Patlak lastikli yol bisikleti $60 | R3 [AÖ/K]: underpriced.app ucuz bisiklet bandı $50–100; Bike Forums ilanları. D1-A ile BANK $40 kalır, lastik masrafını karşılar | [AÖ] doğrulandı |
| Tahta "$100 − $60 = $40" | R4 aritmetik | doğru |
| Bedava masif şifonyer | R6 [AÖ]: Marketplace "Free" filtresi; satış $150–200 (R7: Sawdust2Stitches, underpriced 2026) | [AÖ] doğrulandı (eski Apartment Therapy satırı R14 gereği kaldırıldı) |
| Garaj satışı oyun kutusu $40 | R10 [AÖ]: racketboy "big box of games marked $20"; underpriced kaynak maliyeti $1–50 | [AÖ] doğrulandı |
Bölüm 1'de BANK değişmez; bu fiyatlar yalnız ilan kartlarında, seçim kartında ve repliklerde geçer.

## 10. Test sonuçları
- `python3 veri/metin-kontrol.py --yaz` → çıkış 0. 5/5 kapı GEÇTİ (yukarıdaki özet). Çıktılar: `bolum.txt`, `veri/jake.txt`, `veri/mike.txt`, `veri/zaman.md`.
- Taramalar: telaffuz (charts|complicated|scenarios|truth|crashes|bold) 0; etkileşim yemi (win, giveaway, prize, tag a friend, comment yes, like if, subscribe…) 0; yatırım (invest, stock, crypto, guarantee) 0; repliklerde rakam 0.
- Gün sözü taraması: "tomorrow|drops" metin ve paketlerde 0 (bkz. commit kontrolü).
- Risk / sonraki ajana not: (1) Süre kelime/dk tahmine dayanıyor; kazanan sesler (onyx 0,95 / fenrir 1,05) için ses-yonetmeni gerçek süreyi ölçsün. (2) Konuşan taban kameraya 20° dönük; kameraya bakış anları yalnız portrelerle (ağız oynamaz) verildi, bu yüzden portreler hep sessiz anlarda. (3) Etkileşim yemi nihai kararı monetizasyon-uyum-uzmani'nde; kapanış sorusu artık bölüme özgü.
