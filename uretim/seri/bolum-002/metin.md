# Bölüm 002: "Meet Brenda"

İLERLEME: tamam (metin v1 + koordinatör A1/A2/A4 teşhis düzeltmesi, 2026-11-12). Sıradaki: finans-dogrulayici (3 `[RAKAM?]`) ‖ monetizasyon-uyum-uzmani → kilit → ses-yonetmeni `bolum.txt`.
**KAPI ÖZETİ** (`python3 veri/metin-kontrol.py --yaz`, satirlar.py sha256 c3b53f17a3b3 (Z1), metin-kontrol.py v2 d1b6859b17bb, çıkış 0; iki koşu aynı md5):
- Kelime **202** (Jake 102, Mike 100). Süre: tek tip 200 kpm **78,9 sn**; karakter bazlı (Jake 207 / Mike 170, Bölüm 1 Pocket TTS ölçümü) **83,2 sn** (diyalog wav ≈80,2 + 3 sn kart) → GEÇTİ (60–90). Kalibrasyon: aynı model Bölüm 1'de 69,8 sn tahmin etti, ölçülen wav 69,3 (+0,4 sn).
- Kanca: ilk replik 0,3–2,8 sn (kare 0'da Mike'ın yüzü + yuvarlanan bisiklet, "flap" SFX 0,1 sn) → GEÇTİ. Previously/sıfır oy ≤3 sn, konuşmalı tanıtım yok (A1/A2).
- Sıfır oy esprili ve suçlamasız: "No comments, so I picked." (Z1) + Jake: "Next time, you decide. Please." → GEÇTİ.
- BANK $100 → $40 → **$24** (2 işlem, eksi yok). 5-gram örtüşmesi B001 ile %0,0. Yasak kelime/rakam/tavsiye 0.
- Son: "Take the ninety, hold out, or counter?" + "Tell us in the comments." + "Ep. 3: YOUR call" (gün sözü yok) → GEÇTİ.
- Açık: liste/teklif fiyatları $140 / $90 / $115 `[RAKAM?]` → finans-dogrulayici (§7). Ses ölçümü 88 sn'yi aşarsa kesme: M04 + J06'nın "though" kısmı (−2 sn) ve M02 (−1,3 sn).

---

## 0. Sıfır oy kararı: neden BİSİKLET? (az yorum kuralı, `bolum-001/kazanan.md`)
Bölüm 1'e 0 izleyici yorumu geldi → karakterler karar verir. Ölçüt (1–5): hikâye gerilimi ×2, karakter mantığı, gerçek kayıp/hata, sonraki ikilemi doğurma, görsel kısıta uyum (≤2 Canva).
| Seçenek | Gerilim ×2 | Karakter mantığı | Gerçek kayıp | Sonraki ikilem | Görsel | Toplam |
|---|---|---|---|---|---|---|
| **ROAD BIKE $60** ✔ | 5×2 | 5 | 5 | 5 | 4 | **29** |
| FREE DRESSER | 3×2 | 3 | 3 | 2 | 2 | 16 |
| MYSTERY BOX $40 | 4×2 | 3 | 2 | 3 | 2 | 18 |

Gerekçe:
1. **Karakter:** oy yokken ilk hamleyi aceleci olan yapar. Mike'ın zayıf yönü (incil §1: "fazla öder, kontrol etmeden alır") hemen sahneye çıkar: pazarlık etmeden $60 öder ("He seemed nice."). Jake'in Bölüm 1 uyarısı ("Tires aren't.") karşılığını bulur. Geri dönen izleyiciye bu bir ödül olur.
2. **Gerilim ve gerçek kayıp:** BANK'ın %76'sı tek eşyaya bağlanır. Kilitli zarftaki iki hata da gerçek ve paraya ya da zamana mal olur: iç lastik masrafı (−$16) ve gelmeyen alıcı.
3. **Sonraki karar kendiliğinden doğar:** gelmeyen alıcının ardından düşük teklif gelir: "$90 şimdi mi, $140'ı beklemek mi, pazarlık mı?" Jake ilk kez "hızlı" tarafta durur ("Fast. And safe."), rolleri ters çeviren bir gerilim.
4. Şifonyer: kamyonet, boya ve hafta sonu boyama gerektirir. Bu yavaş bir hikâye ve en az 3 yeni görsel ister (limit 2), bölüm de ikilemsiz biter. Kutu: sonucu başa baştır, logosuz oyun görselleri gerekir ve eBay oranı yazılamaz (R13).
5. "Mike picked" çerçevesi sıfır yorumu bir şakaya çevirir: Jake izleyiciden yardım ister ("Please."). İzleyici suçlanmaz, yorum yapmak için bir nedeni olur.

## 1. Kanca adayları (ölçüt 1–5: kare 0'da yüz+aksiyon ×2, 2 sn netlik, previously ≤3 sn uyumu (A1/A2), karakter, üretim)
| Aday | Özet | Yüz+aksiyon ×2 | Netlik | Previously | Karakter | Üretim | Toplam |
|---|---|---|---|---|---|---|---|
| **K1 BRENDA GİRİŞİ** ✔ | Kare 0: YAKIN-M yüz + bisiklet sağdan kadraja yuvarlanır, patlak lastik "flap-flap". Mike: "No comments, so I picked. Meet Brenda!" Üstte önceki seçim kartı (BIKE ✓ · DRESSER · BOX, rozet yok) + ilerleme şeridi. Jake: "Was he right?" | 5×2 | 5 | 5 | 5 | 4 | **29** |
| K2 SIFIR TAHTASI | Kare 0: YAKIN-J, tahtaya "VOTES: 0" yazılır; "Zero votes." → Mike: "So I picked!" bisiklet çarpar | 3×2 | 4 | 4 | 4 | 4 | 22 |
| K3 PATLAYAN İÇ LASTİK | Kare 0: Mike pompalar, PAT!, şaşkın portre: "Air is free?!" (olayın ortasından başlar) | 5×2 | 2 | 1 | 4 | 4 | 21 |

Elenen: K2 ilk 2 sn'yi yazıya harcıyor (Bölüm 1 A2 dersi) ve "0 oy"u kancanın kendisi yapıyor; yeni izleyiciye "kimse izlemiyor" sinyali veriyor. K3 en güçlü fiziksel an, ama hangi eşyanın seçildiği ve sıfır oy bilgisi 5 sn'den sonraya kayıyor (kart penceresi, A2). K3'ün patlaması S4'te kalıyor (17,9–22,9 sn ikinci kanca).

## 2. Bitiş/seçim adayları (viral, yorum gücü, eşit cazibe, üretim, politika)
| Aday | Özet | Viral | Yorum | Eşit cazibe | Üretim | Politika | Toplam |
|---|---|---|---|---|---|---|---|
| **E1 FİYAT İKİLEMİ** ✔ | Alıcı gelmedi → yeni mesaj "$90 cash, today". **TAKE $90 · HOLD OUT $140 · COUNTER $115** | 4 | 5 | 5 | 5 | 5 | **24** |
| E2 SONRAKİ ALIM | Bisiklet beklerken BANK $24 ile ne alınır (garaj kutusu / bedava şifonyer / bekle) | 3 | 3 | 3 | 3 | 5 | 17 |
| E3 BRENDA KALSIN MI | Mike bisikleti kendine saklamak ister | 3 | 3 | 1 | 5 | 5 | 17 |

Gerekçe: E1 herkesin yaşadığı bir pazarlık anı ("lowball" mesajı); rakamlı ve somut. Seçenekler hız (Jake), kâr (Mike) ve risk (joker) arasında dengeli. E2'de bisiklet hikâyesi kapanmadan yeni iş açılıyor ve $24 şifonyer masrafına ($45–85) yetmiyor (§4.8). E3'te para kararı yok, eşit cazibe testi düşüyor.

---

## 3. Sahne sahne metin (9:16)
Çekim sözlüğü Bölüm 1 ile aynı (GENİŞ / YAKIN-J / YAKIN-M / PORTRE-x:ifade / TAHTA / KOD-PROP). Portreler: nötr, gülen, şaşkın, endişeli, heyecanlı, düşünceli (karakter başına 6). Önden portre ağız oynatmaz, yalnız sessiz tepkide kullanılır. Zamanlar betikten (`veri/zaman.md`). BANK üst-solda, her karede.

| # | Zaman sn | Çekim | Konuşan | Replik | İfade | Kamera + kod-prop | BANK |
|---|---|---|---|---|---|---|---|
| S1 | 0,0–0,3 | YAKIN-M (L1-A) | — | *(0,1 sn: "flap-flap" patlak lastik)* | heyecanlı | **Kare 0: Mike'ın yüzü kadrajda, G1 bisiklet sağ kenardan hareket halinde girer** (kodla kaydırma + hafif zıplama). Üst bant 0–3 sn: önceki seçim kartı `BIKE ✓ · DRESSER · BOX`; ilerleme şeridi `Ep. 2 · BANK $100 → $1,000,000` | $100 |
| | 0,3–2,8 | YAKIN-M | MIKE | No comments, so I picked. Meet Brenda! | heyecanlı | "picked" anında karttaki BIKE'a ✓ "pop"; "Brenda" anında bisikletin üstüne el yazısı isim etiketi "BRENDA" | $100 |
| S2 | 3,2–5,5 | YAKIN-J | JAKE | Was he right? Brenda has two flat tires. | düz | "flat tires" anında lastiklere iki kırmızı halka (kod). Merak döngüsü açılır: "Was he right?" (S7'de hâlâ açık) | $100 |
| | 5,7–6,8 | YAKIN-M | MIKE | Brenda couldn't wait! | sırıtma | Bisikleti okşar gibi kod eğilme | $100 |
| | 7,2–8,7 | YAKIN-J → PORTRE-J:nötr 0,6 sn | JAKE | Next time, you decide. Please. | düz → kameraya bakış | "Please" sonrası sessiz önden portre (dördüncü duvar, kazanan kartı anı §6) | $100 |
| S3 | 9,4–10,9 | GENİŞ + TAHTA köşe | JAKE | Sixty dollars. Did you haggle? | kuru | "Sixty" anında BANK kırmızı **−$60**, "thud" → **$40**. Küçük "Day 2" çipi üst bantta 2 sn | $40 |
| | 11,1–12,1 | YAKIN-M | MIKE | He seemed nice. | masum | — | $40 |
| | 12,6–13,1 | PORTRE-J:düşünceli → YAKIN-J | JAKE | So, no. | düz | Sert punch-in (gag) | $40 |
| | 13,6–15,9 | YAKIN-J | JAKE | I checked the serial number, though. Not stolen. | sakin | KOD-PROP telefon: "SERIAL CHECK ✓ not reported stolen" (rutin; tavsiye değil) | $40 |
| | 16,1–17,2 | YAKIN-M | MIKE | See? Brenda's innocent. | gururlu | — | $40 |
| S4 | 17,9–21,5 | GENİŞ | MIKE | Now we pump her up. Air is free. Easy money! | heyecanlı | KOD-PROP el pompası ikonu, ritmik "pşş" ×3 | $40 |
| | 21,5–22,9 | PORTRE-M:şaşkın | — | *(1,0 sn: PAT! + uzun hışırtı)* | şaşkın | **↺ ikinci kanca:** 2 karelik sarsıntı, iç lastik ikonu sönerek düşer | $40 |
| | 22,9–24,6 | YAKIN-J | JAKE | Air is free. Tubes are not. | düz | — | $40 |
| | 25,1–28,0 | YAKIN-J + KOD-PROP | JAKE | Both tubes are torn. New ones are eight bucks each. | düz | İki yırtık iç lastik ikonu + etiket "$8 × 2". "each" anında BANK **−$16** → **$24** | $24 |
| | 28,2–30,0 | YAKIN-M | MIKE | Sixteen dollars for rubber donuts? | öfkeli-şaşkın | Kod: iç lastik ikonları bir an "donut"a döner (0,4 sn) | $24 |
| | 30,4–32,4 | YAKIN-J → PORTRE-J:gülen 0,5 sn | JAKE | Tires aren't free. I did say that. | kuru, sonra küçük zafer | Bölüm 1 geri çağrısı | $24 |
| S5 | 33,0–36,9 | TAHTA → YAKIN-M | MIKE | Okay, Brenda rides! I'm listing her for a hundred and forty. | heyecanlı | KOD-PROP ilan kartı "ROAD BIKE · $140 · rides great" (G1 görseli) | $24 |
| | 37,3–40,8 | TAHTA | JAKE | She cost us seventy-six. So, sixty-four profit. If she sells. | düz | Tahtaya kodla: `$60 + $16 = $76` · `$140 − $76 = $64?` (soru işareti kırmızı) | $24 |
| | 41,0–44,9 | YAKIN-M | MIKE | Oh, she sells. A guy already wrote back. On my way! | kendinden emin | KOD-PROP mesaj balonu (düz metin, emojisiz): "On my way!" | $24 |
| S6 | 44,9–46,3 | GENİŞ L3 (G2) | — | *(1,0 sn sessiz)* | — | **↺ mekân değişimi:** garaj yolu, gündüz, bisiklet ortada (G1). Saat kartı `2:00 PM` → hızlı ileri → `2:45 PM` | $24 |
| | 46,3–47,8 | YAKIN-J (L3) | JAKE | He's not on his way. | düz | Taban kadraj altında bel hizasından kesik; uymazsa PORTRE-J:endişeli inset | $24 |
| | 48,0–48,7 | YAKIN-M | MIKE | Maybe traffic? | umutlu | — | $24 |
| | 49,1–50,6 | YAKIN-J | JAKE | Forty-five minutes of traffic? | kaş kalkık | — | $24 |
| | 50,6–51,4 | KOD-PROP telefon | — | *(ding)* | — | Mesaj: "sorry, found one cheaper" | $24 |
| | 51,4–54,6 | PORTRE-M:endişeli → YAKIN-M | MIKE | He says, sorry, found one cheaper. Brenda deserved better. | kırgın | Bisiklete yavaş push-in, hüzünlü tek nota | $24 |
| S7 | 54,6–55,6 | KOD-PROP telefon | — | *(ding)* | — | **↺ üçüncü kanca:** yeni mesaj "$90 cash, today?" | $24 |
| | 55,6–58,1 | YAKIN-M | MIKE | Wait. New message. Ninety bucks, cash, today. | şaşkın | — | $24 |
| | 58,5–60,8 | YAKIN-J | JAKE | Ninety is still fourteen profit. Fast. And safe. | sakin | Tahta: `$90 − $76 = $14` | $24 |
| | 61,0–65,3 | YAKIN-M | MIKE | Fourteen? She's worth a hundred and forty! We wait. Trust the vibe. | heyecanlı | Kod eğilme öne | $24 |
| | 65,7–68,0 | YAKIN-J | JAKE | And if the next guy doesn't show either? | düz | Saat ikonu | $24 |
| | 68,2–71,8 | YAKIN-M | MIKE | Then we counter. Meet him at a hundred and fifteen. | kurnaz | Tahta: `$115?` | $24 |
| | 72,2–74,5 | YAKIN-J → PORTRE-J:düşünceli | JAKE | And maybe he walks. Then Brenda lives here. | düz | Telefonda "yazıyor…" üç nokta, gerilim sesi | $24 |
| S8 | 75,5–78,0 | GENİŞ (L1-A) | MIKE | Take the ninety, hold out, or counter? | heyecanlı | Seçim kartı: **TAKE $90 · HOLD OUT $140 · COUNTER $115** | $24 |
| | 78,4–79,9 | GENİŞ | JAKE | Tell us in the comments. | düz-sıcak | Kart açık kalır | $24 |
| | 79,9–83,2 | PORTRE-M:heyecanlı + PORTRE-J:düşünceli | — | — | kameraya bakış | **"Ep. 3: YOUR call"** kartı + takip kartı (Shorts kuralı: en fazla 1, sonda) | $24 |

Not: mesaj balonları düz metin, emojisiz. Kartlarda harf/numara ve gün sözü yok (incil §5.1, §5.7). Sabit kalıp süresi (previously 3 + Ep. kartı 3,3 + CTA 4,4) ≈10,7/83 sn = %13 (≤%20, politika §2.3).

**Merak döngüleri:** A "Was he right?" (3,2 sn açılır → kısmi yanıt 24,6 ve 50,6 sn → Bölüm 3'e açık). B "If she sells" (40,8 → 51,4 gelmeyen alıcı). C "yazıyor…" (74,5 → izleyiciye). Yeniden kancalar: 21,5 PAT · 44,9 mekân değişimi · 54,6 yeni mesaj (aralık ≤23 sn).

## 4. Replikler (TTS girdisi)
Ses-yonetmeni girdisi: `bolum.txt` (betik üretir, elle düzenlenmez). Karakter listeleri `veri/jake.txt`, `veri/mike.txt`. Komut: `tools/ses/bolum-ses.sh uretim/seri/bolum-002 --ses JAKE=pocket:george --ses MIKE=pocket:marius`.
TTS notları: "a hundred and forty / fifteen" yazıyla (rakam okuma hatası riski yok). M01'de "picked" vurgulu. J07 "Air is free." Mike'ı düz taklit eder. S4 PAT sesi 1,0 sn ek sessizliğe kurguda oturur.

## 5. Görsel istek listesi (gorsel-varlik-sanatcisi) — Canva yeni görsel: **2** (limit 2), yeni poz 0
| Kod | Görsel | Kullanım | Şart |
|---|---|---|---|
| **G1** (öncelik 1) | Eski çelik yol bisikleti, yan görünüm, iki lastik belirgin şekilde sönük/basık, logosuz, marka yazısız; düz yeşil/açık zeminde (kesilecek), karakterlerle aynı 3D-görünümlü çizgi stil | S1 giriş, S4, S5 ilan kartı, S6, Bölüm 3'te tekrar (lastikler kodla "dolu" sürümüne yamanır ya da ikinci kare: aynı bisiklet şişik lastikli; Canva tek istekte 2 varyant verirse) | Kask yok, kişi yok, marka/logo yok |
| **G2** (öncelik 2) | L3-A garaj yolu geniş plaka, 9:16, gündüz, banliyö sokağı, uzakta yürüyen insanlar/araba (kalabalık, gündüz = güvenli buluşma rutini), orta alan boş (bisiklet + taban yerleşimi için), ev numarası ve tabela yok | S6 gelmeyen alıcı (44,9–54,6). İncil §2 L3 bölüm 1–10'da kullanılacak, Bölüm 3'te satış buluşmasında yeniden kullanılır | Tabanlar kadraj altından bel hizasında kesilebilsin; uymazsa yalnız portre inset |
Yedek: G2 üretilemezse S6 L1-A'da kalır, saat kartı + telefon mesajı yeterli (mekân değişimi kancası zayıflar).
Kodla eklenecek: önceki seçim kartı (BIKE ✓ · DRESSER · BOX; sayı rozeti yok, Z1), ilerleme şeridi `Ep. 2 · BANK $100 → $1,000,000`, "BRENDA" isim etiketi, lastik halkaları, "Day 2" çipi, seri no kontrol ekranı, pompa ikonu, iki iç lastik ikonu + "$8 × 2", ilan kartı $140, tahta hesapları, mesaj balonları (3), saat kartı, "yazıyor…" noktaları, seçim kartı, "Ep. 3: YOUR call", BANK −$60 / −$16 animasyonları. Kullanılan portreler: Jake nötr, düşünceli, gülen, endişeli; Mike şaşkın, endişeli, heyecanlı. Logo/marka yok.

## 6. Paket metinleri (A4: başlık ve IG ilk satırı = seçim sorusu; 3–5 niş hashtag; "comment X" yok)
**Başlıklar (3)**
| # | Başlık | Krk | Not |
|---|---|---|---|
| T1 ✔ | Take $90, Hold Out, or Counter? You Pick · Ep. 2 | 48 | YouTube Shorts (A4) |
| T2 | Take the $90 or Wait for $140? You Pick Our Next Move · Ep. 2 | 60 | Yedek |
| T3 | No Comments, So Mike Picked the Bike · Ep. 2 | 44 | Yedek; "Was he right?" açısı |

**YouTube Shorts** (başlık T1)
```
Take $90, hold out for $140, or counter at $115? You pick.
Jake & Mike have $100 and one goal: $1,000,000. Nobody commented last time, so Mike picked the bike. Two torn tubes and one no-show buyer later, Brenda finally has an offer.
Take the ninety, hold out, or counter? Tell us in the comments.

We may show winning comments on screen with your username. Prefer to stay anonymous? Just say so in your comment.

Fiction. Not financial advice. Voices and visuals are AI-generated.
Voices: Kyutai Pocket TTS (CC BY 4.0); VCTK corpus (CC BY 4.0).

#flipbyvote #flipping #animatedseries #bikeflip
```
**Instagram Reels**
```
Take $90, hold out for $140, or counter at $115? You pick · Ep. 2
Nobody commented last time, so Mike picked the bike. Then the tubes tore and the buyer never showed.
Take the ninety, hold out, or counter? Tell us in the comments.

We may show winning comments on screen with your username. Prefer to stay anonymous? Just say so in your comment.

Fiction. Not financial advice. Voices and visuals are AI-generated.
Voices: Kyutai Pocket TTS (CC BY 4.0); VCTK corpus (CC BY 4.0).

#flipbyvote #flipping #animatedseries #bikeflip
```
**TikTok**
```
Take $90, hold out for $140, or counter at $115? Ep. 2 of $100 → $1,000,000. Tell us in the comments.
We may show winning comments on screen with your username. Prefer to stay anonymous? Just say so in your comment.
Fiction. Not financial advice. Voices and visuals are AI-generated.
Voices: Kyutai Pocket TTS (CC BY 4.0); VCTK corpus (CC BY 4.0).
#flipbyvote #flipping #animatedseries #bikeflip
```
**Sabit yorum (IG/YT)**
```
Jake wants the sure $90. Mike swears Brenda is worth $140. Would you take the deal, wait, or counter? Got a smarter move? Tell us that too.

We may show winning comments on screen with your username. Prefer to stay anonymous? Just say so in your comment.
```
Yok: ödül, "comment X", etiketleme isteği, gün sözü, "kids", #Shorts (A4).

## 7. Rakam tablosu (finans-dogrulayici onayı gerekir)
| # | Rakam | Dayanak | Durum |
|---|---|---|---|
| N1 | BANK başlangıç $100 | `defter.csv` 001 | doğru |
| N2 | Bisiklet alış $60 | fiyat-referans: kusurlu yol bisikleti $50–100 [AÖ][K]; B1 D1-A | doğru |
| N3 | İç lastik $8 × 2 = $16 | fiyat-referans: $5–12/adet [AÖ] | doğru |
| N4 | BANK $40, $24; maliyet $76 | aritmetik (betik `ISLEMLER` assert) | doğru |
| N5 | İlan $140; kâr $64 | **[RAKAM?]** Dayanak önerisi: underpriced.app ucuz bisiklet "$50–100 profits" [K, B1 R3] → satış $126–176; BikeForums ilan örnekleri $150 / $180 (istenen fiyat, satış değil) [AÖ, 2026-11-12 arama]. Kâr $64 ≤ maliyet $76 (§4.5) | doğrulayıcı |
| N6 | Teklif $90; kâr $14 | **[RAKAM?]** Düşük teklif (ilanın %64'ü) [T] | doğrulayıcı |
| N7 | Karşı teklif $115; kâr $39 | **[RAKAM?]** ilan ile teklifin ortası [T] | doğrulayıcı |
| N8 | 45 dk bekleme | anlatı, fiyat değil | — |
Not: lastik dışı masraf (zincir yağı) yazılmadı: fiyat-referansta yok. Bölüm 1 zarfı "zincir yağ ister" diyordu. Bölüm 3'te gerekirse eklenir, yoksa "evdeki yağ" (masrafsız).

`defter.csv` eklenecek satırlar (koordinatör/doğrulayıcı onayından sonra):
```
002,yol bisikleti alis,-60,40,fiyat-referans: kusurlu yol bisikleti $50-100
002,ic lastik x2,-16,24,fiyat-referans: ic lastik $5-12
```

## 8. Sonuç zarfı (yayından önce kilitli; incil §5.4)
| Seçenek | Artı (söylenir) | Bedel (söylenir) | Değer | Kimin | Sonuç (Bölüm 3) |
|---|---|---|---|---|---|
| TAKE $90 | "still fourteen profit. Fast. And safe." | en düşük kâr ("Fourteen?") | hız/güvenlik | Jake | Alıcı gündüz, kalabalık yerde gelir, nakit. BANK $24 → **$114**. Flip net +$14. Jake haklı (hız), Mike fiyatın düşük kaldığını söyler |
| HOLD OUT $140 | "She's worth a hundred and forty!" | "if the next guy doesn't show either?" | kâr | Mike | 1–3 hafta sürer [K: satış 7–21 gün]. Bir alıcı daha pazarlık eder, satış $120–140 aralığında olur (kesin rakam doğrulayıcı onayıyla). BANK → **$144–164**. Bedeli: o süre boyunca BANK $24'te kilitli kalır ve yeni alım yapılamaz |
| COUNTER $115 | orta yol | "maybe he walks" | risk/pazarlık | joker | Alıcı $100'e iner, kabul edilir. BANK → **$124**. Flip net +$24 |
Üçü de Bölüm 1 zarfındaki "küçük kâr" yönüyle tutarlı. Seçenek dışı fikirler (ör. "fix the brakes, sell higher", "sell parts") §7'ye göre değerlendirilir. Masraf getiren fikir BANK $24'e sığmalıdır. Haklı sayımı (sezon-takip): Bölüm 2'de lastik konusunda Jake haklı çıktı. "Was he right?" sorusu Bölüm 3'ün sonucuna bağlı.

## 9. Test sonuçları
- `python3 veri/metin-kontrol.py --yaz` → çıkış 0, 9/9 GEÇTİ (özet en üstte). İki koşu: md5 3cca742066c9 = 3cca742066c9 (yeni betik determinizmi).
- `python3 veri/metin-kontrol.py --kalibre` → B001 model 69,8 sn ↔ ölçülen 69,3 sn (+0,4).
- Betiğin taradığı listeler: telaffuz (charts|complicated|scenarios|truth|crashes|bold) 0; politika (win, giveaway, prize, tag a friend, like if, invest, stock, crypto, guarantee, subscribe, tomorrow, tax-free, you should…) 0; replikte rakam 0.
- Paket taraması (elle): "comment " + harf/numara kalıbı 0, "tomorrow/drops" 0, hashtag 4/platform, AI + ses atfı + anonim satırı 3/3.
- Koordinatör teşhisi: A1 (seçim 0–3 sn'de ekranda ve sözde, konuşmalı tanıtım yok) ✓ · A2 (previously ≤3 sn + ilerleme şeridi) ✓ · A4 (başlık/IG ilk satırı = seçim sorusu, 4 niş hashtag) ✓.
