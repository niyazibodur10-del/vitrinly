# F2 viralite — 12 senaryo (viralite-analisti) · 2026-11-04 · model **v0.2**

İLERLEME: tamam. Yeniden üretim: `python3 tools/viralite.py 02-senaryo/viralite-girdi.json` (girdi sha256 a592f38df757).
**Karar (ilk 3, Paz 2026-11-08 A/C slotu):** **S03 8.10** (miras sızıntıları) · **S01 8.00** (soygun rekorları) · **S06 7.50** (ABD'nin alacaklı kuyruğu). Puanlar **TAHMİN [T]**, model güveni DÜŞÜK.
**Farklar:** S03−S01 0.10 (<0.3, anlamsız → hakem riskle seçer; benim eğilimim S03: 3 kanalda ≥10x, risk YEŞİL, raf ömrü 8; S01 haber dalgası 10 günde soğuyabilir ve SARI). S01−S06 0.50 anlamlı. **3. sıra kırılgan:** S06 = S08 7.50 (eşitlik talep 9>8 ile S06'ya).
**Milyon olasılığı (12 ay, TAHMİN):** S03 %1–3 · S01 %1–3 · S06 %1–3 · diğerleri ≤%1. Taban: 90 g nişte <10 B aboneli kanalların ≥1 M videosu **0/186** [API][H].
**Kapılar:** 2 koşu aynı (sha256 c05b477c2c9b ×2) ✓ · ağırlık toplamı 1.00 assert ✓ · `--dokuman` tutarlı ✓ · duyarlılık: 56 durumun 23'ünde 3. sıra değişiyor (S06→S08 veya S07), **ilk 2 (S03, S01) 56/56 sağlam**.
**Kalibrasyon:** v0.1 → v0.2 (90 g niş n=959): zamanlama 0.10→0.05, merak 0.20→0.25, somut özne tavanı kapatıldı (veri yalanladı). v0.1 ile de ilk 2 aynı.
**S02 talebi ölçüldü:** "geri dönüş" açısına özgü aramalar medyan 472 ve 131 izlenme; doğrudan aynı açı (Sticks and Cents) 773 izlenme → talep 4. Genel sorgular soygun talebini döndürüyor, geri dönüşü değil.
**Hakeme not:** S05'in çalışma başlığı "First to Go Broke" = OBF/Broke Economy çekirdeği → −1.5 (6.45). Alt-2 başlıkla **7.70**: S06'nın 0.20 üstü (anlamsız); S05 seçilecekse yalnız Alt-2 ile.

## 1. v0.2 kalibrasyonu (bir kez, 90 günlük rakip verisi)
`viralite-olcum/kalibrasyon90.py` (delta90-2026-11-04.json sha256 700788baba66, desen90.py ile aynı niş filtresi) → `kalibrasyon90-cikti.txt`. Skor = kanal içi medyan oranı [API][H].
| Model kuralı | Test | Sonuç | Karar |
|---|---|---|---|
| Somut özne yoksa merak ≤6 | somut özneli 456 ↔ öznesiz 503 başlık | 1,07x ↔ 1,05x; ≥3x %15 ↔ %15 | **Kapatıldı** (en büyük outlier 364x öznesiz) |
| Zamanlama 0.10 | gündem kelimeli 158 ↔ 801 | 1,00x ↔ 1,09x; ≥3x %12 ↔ %15 | **0.05** (v0.1'deki ret gerekçesi, liste yanlılığı, 90 g pencerede yok) |
| Merak 0.20 | tarih→gelecek 46 · gizli iş modeli 29 · what happens 29 | ≥3x %39 · %41 · %28 (niş %15) | **0.25** + çerçeve çapası |
| Paradoks kalıbı | n=19 | 0,98x | tek başına merak +1 almaz |
| Seri bonusu | n=4 | ölçülemez | +0.3 aynen |
Sınır: başlık regex'i konuyu ve kanal etkisini ayıklamaz; hook/hikâye/görsel başlıktan ölçülemez → hâlâ kalibre değil. Doküman: `docs/viralite-modeli.md` "v0.1 → v0.2" bölümü.

## 2. Kanıt: en yakın rakip outlier'ı (yerel medyan, API 2026-11-04) [API][H]
`viralite-olcum/viralite-outlier.py` (2026-10-28 betiği, yalnız HEDEFLER + "sonrası" kesimi 10-28) → `viralite-outlier.json` (sha256 2a57b4fc3a9f). Skor = izlenme ÷ çevredeki ≤10 uzun yüklemenin medyanı. **k** = son 12 ayda <50 B aboneli kanalda aynı konuda ≥500 B video.
| ID | En yakın outlier (kanal, abone) | Skor | Diğer komşular | Talep | k → milyon [T] |
|---|---|---|---|---|---|
| S03 | What Happens When All the Baby Boomers Are Gone? (AJ Osborne, 4,9 B) 595 B | **953x** | Philosophase (22 B) 928 B 137x · Austin Williams 13x | 9 | 2 → %1–3 |
| S01 | How Binance Lost $6,300,000,000 in One Night (Gloam, 6,1 B) **1,90 M** | yerel medyan yok (tek uzun video); izl/abone 310x | fern 1,5x (rutin konu) · Joe Bartolozzi 1,5x; sorgu medyanı 2,05 M | 8 | 1 + küçük kanalda ≥1 M → %1–3 |
| S06 | If Every Nation Is in Debt… Who Are They Paying? (Hidden Capital, 7,1 B) 807 B | **229x** (n=8) | PENNY (5,1 B) 863 B 91x (n=4, zayıf) · Invisible Hand 6,3x | 9 | 2 → %1–3 |
| S08 | The AI Bubble Will Burst. Here's What Happens Next (Not Unprecedented, 2,3 B) 736 B | 38,9x (n=2, zayıf) | Infographics 7,2x · 1,8x | 8 | 1 → %0,5–1 |
| S07 | The Man Who Stole $65 Billion (Infographics, 2018) 3,99 M | 11,9x (komşu ölçümü şüpheli: 300 video sınırı) | Built on Lies 3,0x; sorgu medyanı 1,18 M | 7 | 0 → <%0,5 |
| S09 | Where Did Mansa Musa Get So Much Gold? (Documentary Empire, 14 B) 943 B | 5,4x | hoser 0,97x · jack pockets 1,6x | 7 | 1 → %0,5–1 |
| S02 | Where Did Bernie Madoff's $65 Billion Actually Go? (Sticks and Cents, 22 abone) 773 | 13x (<30 B, sayılmaz) | Facts Verse 0,24x; açıya özgü sorgu medyanları 472 / 131 | 4 | 0 → <%0,5 |
| S11 | Fed Issues WARNING to Every American With a Savings Account (Epic Real Estate) 1,79 M | 44,9x (komşu açı) | Infographics 3,4x (şüpheli); SVB'ye özgü outlier yok | 5 | 0 → <%0,5 |
| S05 | Which Rich Country Goes Bankrupt First? (OBF, 741 B) **8,64 M** | 18,3x | Broke Economy 14,0x · Economics Help 3,3x · Finance Stack 21x (3 günlük, sayılmaz) | 9 | 0 → <%0,5 |
| S10 | Most Expensive Mistakes in History - Part 2 (BE AMAZED) 1,16 M | 1,9x | 1,9x; sorgu medyanı 625 B | 4 | 0 → <%0,5 |
| S04 | How Do Boomers Expect To Sell Their Houses If Gen Z Can't Buy Them? (Casey Simpson) 3,46 M | 6,6x | Hawk Live (17 B) 540 B 5,1x (n=7) · HMW 2,6x | 8 | 1 → %0,5–1 |
| S12 | They Bought Nearly All the World's Silver (Investigate Money, 26 B) 313 B | 30,5x | Why X (46 B) 766 B 39,8x (komşu açı) · Hamish Hodder 0,7x | 8 | 1 → %0,5–1 |
Milyon kuralı ve taban: `docs/viralite-modeli.md` (puana girmez). Arama sıralaması izlenmeye göre olduğundan taban oran üst sınırdır; kanal 3 abone ile başlıyor [KÖ].

## 3. Puan tablosu (temel; aralık = kötümser–iyimser) [T]
| ID | Merak | Talep | Hook | Kişisel | Zaman | Hikâye | Görsel | Raf | Seri | Ceza | Nihai (köt./tem./iyi.) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| S03 | 8 | 9 (8–9) | 7 (7–8) | 9 (8–9) | 6 (5–7) | 6 (5–7) | 8 | 8 | ✓ | — | 7.60 / **8.10** / 8.40 |
| S01 | 8 (7–8) | 8 (7–9) | 9 | 5 (4–6) | 8 (7–9) | 8 | 9 | 7 | ✓ | — | 7.40 / **8.00** / 8.35 |
| S06 | 8 (8–9) | 9 (8–9) | 8 | 6 (5–7) | 7 | 6 | 9 | 6 | — | — | 7.20 / **7.50** / 7.90 |
| S08 | 8 (8–9) | 8 (7–9) | 7 | 7 (6–8) | 8 | 7 | 8 | 6 | — | — | 7.20 / **7.50** / 8.05 |
| S07 | 7 (6–8) | 7 (6–8) | 8 | 6 | 4 | 9 | 8 | 9 | — | — | 6.90 / **7.30** / 7.70 |
| S09 | 9 (8–9) | 7 (6–7) | 9 | 3 (3–4) | 3 | 7 | 7 | 9 | — | — | 6.60 / **7.00** / 7.15 |
| S02 | 8 (7–8) | 4 (3–5) | 8 (7–8) | 5 (4–6) | 7 | 7 | 8 | 7 | ✓ | — | 6.35 / **7.00** / 7.30 |
| S11 | 7 (6–7) | 5 (4–6) | 8 | 8 (7–8) | 5 (4–6) | 6 | 9 | 8 | — | — | 6.35 / **6.95** / 7.15 |
| S05 | 9 (8–9) | 9 (8–10) | 9 | 7 (6–8) | 8 (7–9) | 6 | 8 | 6 | — | −1.5 | 5.85 / **6.45** / 6.80 |
| S10 | 7 | 4 (4–5) | 8 | 5 | 3 | 6 | 8 | 9 | — | — | 6.20 / **6.20** / 6.35 |
| S04 | 7 | 8 (7–8) | 7 | 8 (7–9) | 5 | 5 | 8 | 8 | ✓ | −1.5 | 5.55 / **5.85** / 6.00 |
| S12 | 7 | 8 (7–9) | 8 | 4 | 6 | 9 | 9 | 9 | — | −1.5 | 5.70 / **5.85** / 6.00 |
Seri: S01↔S02 (soygun → geri dönüş) ve S03↔S04 (miras → evler) her biri tek başına izlenebilen ikili. Belirsiz ölçüt gerekçeleri (iyimser / temel / kötümser):
- **S03 talep 9/9/8:** 3 kanalda ≥10x / temel / outlier'lar "boomers gone" genel açısı, "miras sızıntısı" değil. **Hikâye 7/6/5:** Leo'nun bant gag'i + Okafor ailesi / temel / kötü adam yok, liste gibi akabilir.
- **S01 zamanlama 9/8/7 ve talep 9/8/7:** Binance dalgası 11-08'de sürer / temel / Gloam ve CNN dalgayı aldı, 10 gün sonra soğuk (varyant: zamanlama 5 + talep 7 → **7.70**, yine 2.). **Kişisel 6/5/4:** kripto sahipleri / temel / cebe dokunmuyor.
- **S06 kişisel 7/6/5:** "öndeki kendi emeklilik fonun" ters köşesi / temel / ABD dışı izleyiciye soyut.
- **S08 talep 9/8/7:** 38,9x tam sayılır / n=2 bir kademe düşük / nişte "AI bubble" doymuş (Infographics 8 gün önce 4,24 M).
Merak gerekçesi (marketing-psychology, bilgi boşluğu): bilinen bir inancı kıran başlık (S09 "website list", S05 paradoks) en yüksek; boşluğu adlandırmayan genel "What if everyone…" (S11) ve "Buy a Whole Market" (S12) orta.

## 4. Eleme turları (12 → 3)
**Tur 1 — sert eleme / ceza:** sert eleme yok (finans-dogrulayici paralel; `ana_iddia_dogrulandi` geçici true). Ceza (−1.5, `benzer_aci`):
- S05: "First to Go Broke" çalışma başlığı OBF/Broke Economy outlier'larının çekirdeği; kopya dalgasının içinde (Alt-2 ile 7.70, yedek).
- S04: thumbnail metni "WHO BUYS THEM?" Hawk Live başlığının çekirdeği (cezasız 7.35; yine ilk 5 dışı).
- S12: thumbnail "ALL THE SILVER" Investigate Money başlığının çekirdeği (cezasız 7.35; sorgu medyanı yalnız 20 B).
**Tur 2 — puan, ilk 5 (S03, S01, S06, S08, S07):**
- S09 (7.00): merak ve hook en yüksek ama kişisel bağ 3 ve tek ≥3x kanıt 5,4x; F3 yükü yüksek.
- S02 (7.00): talep ölçüldü, zayıf (açıya özgü medyan 472); S01 seçilirse doğal 2. bölüm.
- S11 (6.95): SVB'ye özgü outlier yok, en yakın kanıt komşu açı.
- S10 (6.20): nişte outlier yok (1,9x), talebi büyük genel eğlence kanalları tutuyor.
**Tur 3 — risk ve kırılganlık (ilk 5 → 3):**
- S08 (7.50, S06 ile eşit): eşitlik kuralı talep 9>8; ayrıca konu son 8 günde Infographics 4,24 M + Fireship 2,56 M ile doymuş.
- S07 (7.30): S06'nın 0.20 altı (anlamsız) ama hassas konu (mağdurlar) ve komşu ölçümü şüpheli; hakem S06'yı risk raporuyla düşürürse 4. aday.

## 5. Duyarlılık (`viralite-olcum/viralite-duyarlilik.py` → `duyarlilik-cikti.txt`)
- 56 ağırlık durumunda ilk 3 kümesi 23 kez değişiyor; değişenlerin hepsi 3. sırada (S08 21, S07 2), **S03 ve S01 56/56 ilk 2'de** (9 durumda yalnız sıraları yer değiştiriyor). → **"3. sıra kırılgan"**, ilk 2 sağlam.
- Çapraz test (hedef kötümser, diğerleri iyimser): her üçü de tek başına düşebiliyor; S08 her durumda ilk 3'e giriyor → hakemin yedeği S08 veya S05-Alt2.
- v0.1 ile karşılaştırma (`viralite-olcum/viralite_v01.py`): S03 8.00 = S01 8.00, 3. S08 7.50, 4. S06 7.45 → kalibrasyon ilk 2'yi değiştirmedi.
- Varyantlar (`viralite-girdi-varyant.json`): seri bonusu olmasaydı S03 7.80, S01 7.70 (ikisi yine 1–2); S05 cezasız 7.95 (3. olurdu) → **ilk 3'ü değiştiren tek yargı S05 cezası**, hakeme açıkça.

## Test
```
python3 tools/viralite.py 02-senaryo/viralite-girdi.json   # ×2 → diff yok, sha256 c05b477c2c9b ×2
python3 -c "...assert sum(v.AGIRLIK.values())==Decimal('1.00')"   # assert OK: toplam 1.00
python3 tools/viralite.py --dokuman docs/viralite-modeli.md       # Doküman tutarlı: 8 ağırlık, toplam 1.00
python3 tools/viralite.py tools/ornek-senaryolar.json            # ×2 aynı (betik değişti → determinizm testi yapıldı)
```
Betik çıktısı (v0.2, temel girdi):
```
| 1 | S03 | The Biggest Inheritance Ever, and Why Heirs Might Miss It | 7.80 | +0.30 | −0.00 | **8.10** | seri +0.3 |
| 2 | S01 | Bigger Heists, Fewer Thieves: How Stealing Money Changed | 7.70 | +0.30 | −0.00 | **8.00** | seri +0.3 |
| 3 | S06 | What If Everyone America Owes Asked for It Back? | 7.50 | +0.00 | −0.00 | **7.50** | - |
| 4 | S08 | The Last Tech Boom Ended Like This. Could AI Follow? | 7.50 | +0.00 | −0.00 | **7.50** | - |
| 5 | S07 | The Fraud Was Hiding in a Line That Was Too Smooth | 7.30 | +0.00 | −0.00 | **7.30** | - |
| 6 | S09 | Mansa Musa's Famous Fortune Came From a Website List | 7.00 | +0.00 | −0.00 | **7.00** | - |
| 7 | S02 | What Happens to Stolen Money After the Heist? | 6.70 | +0.30 | −0.00 | **7.00** | seri +0.3 |
| 8 | S11 | What If Everyone Took Their Money Out at Once? | 6.95 | +0.00 | −0.00 | **6.95** | - |
| 9 | S05 | Japan Owes the Most. So Why Isn't It First to Go Broke? | 7.95 | +0.00 | −1.50 | **6.45** | benzer_aci −1.5 |
| 10 | S10 | The Worst Trades in History, Judged Without Hindsight | 6.20 | +0.00 | −0.00 | **6.20** | - |
| 11 | S04 | What Happens When the Boomers Sell Their Houses? | 7.05 | +0.30 | −1.50 | **5.85** | seri +0.3; benzer_aci −1.5 |
| 12 | S12 | What Happens When Someone Tries to Buy a Whole Market? | 7.35 | +0.00 | −1.50 | **5.85** | benzer_aci −1.5 |
```
Kullanılmayan skill: `youtube-full` transkripti (rakip-ozet §7: yt-dlp altyazı 4/4 bot kontrolü), `dataviz` (kendi CTR/AVD verisi yok, tahmin/gerçek grafiği çizilecek veri yok).
