# F2 viralite — 12 senaryo (viralite-analisti) · 2026-11-02 · model v0.1

İLERLEME: tamam. Yeniden üretim: `python3 tools/viralite.py 02-senaryo/viralite-girdi.json` (girdi sha256 ce90cd6d7bd9).
**Karar (ilk 3, B slotu Çar 2026-11-04):** **S06 7.50** (5 % tahvil → mortgage) · **S01 7.25** (Çin AI hisseleri → ABD) · **S08 7.25** (ABD bütçesi = bir hane). Puanlar **TAHMİN [T]**, model güveni DÜŞÜK.
**Farklar anlamsız:** S06−S01 0.25, S01−S08 0.00 (<0.3) → sıralamayı hakem risk raporlarıyla verir; benim eğilimim S06 (aynı konuda 9,8x yerel outlier + karşı-sezgisel başlık + Fed'den bağımsız tez).
**Kapılar:** 2 koşu aynı (sha256 dab7ffb8050d ×2) ✓ · ağırlık toplamı 1.00 ✓ (`--dokuman` tutarlı) · duyarlılık: B havuzunda 56 ağırlık durumundan 1'inde 3. sıra değişiyor (S08→S12) → **3. sıra kırılgan**, 1–2 sağlam küme.
**Elenen:** S09 slot dışı (A, Paz 11-08 stoku için en iyi A: 7.15); S12, S07 risk turunda; 6 senaryo puanla (aşağıda tek cümle).
**Hakeme 3 not:** (1) S06'da Alt-1 başlığı kullanılırsa WhiteBoard Finance kalıbı → −1.5 (6.00); çalışma başlığı kalmalı. (2) Veri 2026-10-28 tarihli: S06 faiz seviyesi ve S01 Çin rakamları F3'te tazelenmeli. (3) S05 tavansız 7.05 olurdu (S08'den 0.20 aşağı, anlamsız) — seçim ertesi zamanlaması tek gücü, üretim + siyaset riski yüksek.

## 1. Kanıt: en yakın rakip outlier'ı (yerel medyan, API 2026-11-02) [API][H]
`viralite-outlier.py` (önceki videodan kopya, yalnız HEDEFLER değişti; videos/channels/playlistItems, search yok) → `viralite-outlier.json` (sha256 3d26548c96bb). Skor = izlenme ÷ çevredeki ≤10 uzun (≥4 dk) yüklemenin medyanı.

| ID | En yakın outlier (kanal) | Skor | Diğer komşular | Talep puanı (çapa) |
|---|---|---|---|---|
| S01 | China's AI Bubble Has Burst (India Global Review, haber) · Reuters | 196x · 138x | Damon Cassidy AI collapse 4,1x; Infographics "AI bubble bursts" 7,2x | 8 (haber kanalı, 6 günlük, niş dışı → bir kademe düşük; "AI bubble" nişte doymuş [RÖ]) |
| S02 | CoreWeave Is Imploding (Prof G) | 2,6x | Tilbury 1,2x · Eisman 1,1x | 4 (outlier yok, ilgi var) |
| S03 | Anthropic S-1 (Prof G) | 1,2x | Breaking Points 0,6x · Carlson 0,9x | 4 (HN 1.697 puan; YT outlier yok) |
| S04 | What the Supreme Court Tariff Ruling Says (Washington Gun Law, Şubat) | 7,4x | CNN n=0 (ölçülemedi) | 6 (≥3x ama açı "karar", "iade" değil) |
| S05 | What Happens If Trump Loses The Midterms? (Finance Bureau) | **50,6x** | ClearValue 2,1x · BWB 0,35x | 8 (≥10x tek kanal) |
| S06 | The 10-Year Treasury Just Hit 5% (WhiteBoard Finance) | **9,8x** | CNBC 0,38x | 8 (≥3x tek kanal; arama medyanı 4,6 K düşük ama aynı konu outlier) |
| S07 | America's Housing Market Just Took a Very Strange Turn (MHFIN) | **42,9x** | Graham Stephan 3,8x · Damon Cassidy 2,6x | 8 (≥10x tek kanal + ≥3x ikinci; doygunluk yüksek) |
| S08 | Why A National Debt Default Now Looks Genuinely Possible (How Money Works) | 3,0x (2,97) | Infographics 0,77x | 6 (eşikte; iyimser 7) |
| S09 | The VOLCKER Shock (Sleeping Economist, 4,6 B abone, 2.184 izlenme) | 6,0x | FINAiUS 0,28x | 5 (küçük kanal, zayıf) |
| S10 | — ölçülmedi (sezon öncesi) | — | — | 3 ([ÖB] tavanı) |
| S11 | What happens if dollar hits ₹100? (The News Minute) | 2,2x | Gaurav Thakur 2,0x · FinnovationZ 0,56x | 4 |
| S12 | Why The U.S. Diesel Crisis Is Only Getting Started (Fred, maskot rakip) | 8,7x | Fred Suudi 5,6x · Eurodollar Univ. 4,5x | 8 (≥3x üç videoda) |

## 2. Puan tablosu (temel; aralık = kötümser–iyimser) [T]
| ID | Merak | Talep | Hook | Kişisel | Zaman | Hikâye | Görsel | Raf | Nihai (köt./tem./iyi.) |
|---|---|---|---|---|---|---|---|---|---|
| S06 | 8 (7–8) | 8 (7–8) | 8 | 8 (7–8) | 7 (6–8) | 5 (4–6) | 9 | 7 | 6.75 / **7.50** / 7.75 |
| S01 | 8 | 8 (7–9) | 8 | 6 (5–7) | 8 (7–9) | 6 (5–7) | 8 | 5 | 6.70 / **7.25** / 7.80 |
| S08 | 8 (7–9) | 6 (6–7) | 9 | 7 (6–8) | 6 | 6 | 9 | 8 | 6.90 / **7.25** / 7.75 |
| S09 | 8 | 5 (4–5) | 8 | 6 | 5 | 9 | 8 | 9 | 7.00 / **7.15** / 7.15 |
| S12 | 7 | 8 (7–8) | 7 | 8 | 7 (4–8) | 5 | 8 | 5 | 6.55 / **7.00** / 7.10 |
| S07 | 7 (6–8) | 8 (8–9) | 7 | 8 | 6 | 5 | 7 | 5 | 6.60 / **6.80** / 7.15 |
| S04 | 8 | 6 (5–7) | 7 (6–8) | 6 (5–7) | 6 | 7 | 8 | 5 | 6.40 / **6.80** / 7.20 |
| S05 | 8→**6** tavan | 8 (7–9) | 7 (6–8) | 7 (6–8) | 10 | 5 | 6 | 3 | 6.25 / **6.65** / 7.05 |
| S03 | 8 | 4 | 8 | 4 (3–5) | 8 (7–8) | 6 | 7 | 4 | 5.95 / **6.20** / 6.35 |
| S11 | 8 | 4 | 8 | 5 (4–7) | 6 | 5 | 7 | 6 | 5.95 / **6.10** / 6.40 |
| S02 | 6 (tavan: "AI Boom" somut özne değil) | 4 (4–5) | 8 | 5 (4–6) | 7 | 6 | 7 | 5 | 5.75 / **5.90** / 6.20 |
| S10 | 6 ("Not What It Seems" boş vaat) | 3 | 7 | 8 | 6 (5–7) | 4 | 8 | 4 | 5.65 / **5.75** / 5.85 |

Belirsiz ölçüt gerekçeleri (iyimser / temel / kötümser):
- **S06 hikâye 6/5/4:** tesisatçı Leo + "Fed değil" ters köşesi gerilim kurar / mekanizma anlatısı, kötü adam yok / boru dersi gibi kuru kalabilir. **Zamanlama 8/7/6:** %5 hâlâ manşette / 1 Ekim'de geçildi, seviye oynak / 4 Kas'ta %5 altındaysa kanca zayıflar.
- **S01 kişisel 7/6/5:** emeklilik fonu = herkesin cebi / dolaylı / "hisse sahibi değilim" diyen genç izleyiciye uzak. **Talep 9/8/7:** 196x+138x tam sayılır / haber kanalı bir kademe düşük / nişte "AI bubble" doymuş (%11 ≥2x [RÖ]).
- **S08 merak 9/8/7:** "$5,400" somut ve şaşırtıcı / temel / "devlet = hane" bilinen bir eğitici kalıp [ÖB] (ölçülen rakip başlığı yok, ceza yok).
- **S12 zamanlama 8/7/4:** saldırılar sürüyor / temel / 4 Kas'ta barış veya fiyat düşüşü → bayat (varyantla 6.70).
Merak ölçütü gerekçesi (marketing-psychology): bilgi boşluğu en güçlü olduğunda başlık bilinen bir inancı kırar (S06 "Not the Fed", S01 "Is America next?"); "Not What It Seems" gibi boşluğu adlandırmayan vaat zayıftır.

## 3. Eleme turları (12 → 3)
**Tur 1 — slot / sert eleme:** sert eleme yok (finans-dogrulayici paralel; `ana_iddia_dogrulandi` geçici true).
- S09: A sütunu, Çar B slotuna uymaz; Paz 11-08 / Kasım A stoku için en güçlü aday (hikâye 9, raf 9).
**Tur 2 — puan (B havuzu, ilk 5: S06, S01, S08, S12, S07; S07↔S04 eşitliği talep 8>6 ile S07'ye):**
- S04 (6.80): iade sorusu evrensel ama ABD-merkezli ve kaynak ikincil; aynı açıda (iade) taze outlier yok.
- S05 (6.65): zamanlama 10 tek gücü; başlıkta somut özne yok (tavan), raf 3, sonuç F7'de 4 Kas sabahı eklenecek.
- S03 (6.20): YT'de outlier yok (≤1,2x) ve çıkar çatışması (metni Anthropic modeli yazıyor) kanal güvenini riske atar.
- S11 (6.10): kişisel bağ Hindistan dışında zayıf; outlier yok (≤2,2x).
- S02 (5.90): talep 2,6x'te kalıyor, başlık somut özne taşımıyor; S01'in 5. belirtisi olarak zaten içeride.
- S10 (5.75): talep ölçülmedi ve 4 Kas için erken; Kasım sonu stoku.
**Tur 3 — risk (5 → 3):**
- S12 (7.00): saldırı/ölüm hassasiyeti + jeopolitik bayatlama (kötümser 6.70) + Fred maskot rakibinin enerji kümesi.
- S07 (6.80): talep güçlü ama 3. sıranın 0.45 altında ve nişin en doymuş konusu (MHFIN, Graham, Damon).
**İlk 3:** S06, S01, S08 → hakem (risk raporlarıyla).

## 4. Hesap betiği çıktısı (test kapısı)
```
$ python3 tools/viralite.py 02-senaryo/viralite-girdi.json   (2 koşu; diff → fark yok; çıktı sha256 dab7ffb8050d ×2)
| 1 | S06 | The 5% Number That Sets Your Mortgage (It's Not the Fed) | 7.50 | +0.00 | −0.00 | **7.50** | - |
| 2 | S01 | China's AI Stocks Lost $480 Billion. Is America Next? | 7.25 | +0.00 | −0.00 | **7.25** | - |
| 3 | S08 | If America Earned $5,400 a Month, Here's Its Budget | 7.25 | +0.00 | −0.00 | **7.25** | - |
| 4 | S09 | The Fed Chief Who Pushed Rates to 20%: Hero or Villain? | 7.15 | +0.00 | −0.00 | **7.15** | - |
| 5 | S12 | $115 Oil: Follow One Barrel From the Gulf to Your Gas Pump | 7.00 | +0.00 | −0.00 | **7.00** | - |
| 6 | S07 | Record Home Prices, Fewer Buyers: How Are Both True? | 6.80 | +0.00 | −0.00 | **6.80** | - |
| 7 | S04 | $130 Billion in Tariff Refunds. Where Is the Money Going? | 6.80 | +0.00 | −0.00 | **6.80** | - |
| 8 | S05 | The Midterms Are Over. What Happens to Your Money Now? | 6.65 | +0.00 | −0.00 | **6.65** | merak 8→6 (somut özne yok) |
| 9 | S03 | An $80 Billion Loss? Reading Anthropic's IPO Paperwork | 6.20 | +0.00 | −0.00 | **6.20** | - |
| 10 | S11 | What Happens If the Rupee Hits 100 Per Dollar? | 6.10 | +0.00 | −0.00 | **6.10** | - |
| 11 | S02 | Who Is Lending Money to the AI Boom? | 5.90 | +0.00 | −0.00 | **5.90** | - |
| 12 | S10 | The First $1 Trillion Holiday Season Is Not What It Seems | 5.75 | +0.00 | −0.00 | **5.75** | - |
$ python3 tools/viralite.py --dokuman docs/viralite-modeli.md → Doküman tutarlı: 8 ağırlık betikle aynı, toplam 1.00
```
**Yargı varyantları** (`viralite-girdi-varyant.json`, sha256 fb4292e4d0f7): S01 talep 9 → 7.40 · S08 talep 7 → 7.40 · S05 tavansız → 7.05 · S12 zamanlama 4 → 6.70 · S06 Alt-1 başlığı (benzer_aci) → 6.00. Hiçbiri ilk 3 kümesini değiştirmiyor; yalnız S06 başlık seçimi kritik.
**Duyarlılık** (`viralite-duyarlilik.py`, değişmemiş betik, 1 koşu): tam havuzda 56 durumun 21'inde S09 ilk 3'e giriyor (slot dışı olduğu için geçersiz). B havuzunda (`viralite-girdi-bslot.json`, sha256 b398562e7fbe) yalnız `raf −0.05 → talep +0.05` 3. sırayı S08→S12 yapıyor; 23 durumda yalnız sıra değişiyor. Çapraz test (hedef kötümser, diğerleri iyimser): her üçünde S04 3. sıraya giriyor → **"sıralama kırılgan" (3. sıra)**, hakeme bildirildi.

## 5. Kalibrasyon durumu
Kendi kanal: 1929 videosu 2026-10-28'de yayında; `yayin-sonrasi/` raporu ve `yt-analytics.readonly` kapsamı henüz yok → kalibrasyon yapılmadı, model v0.1 kalır. Tetik: ≥5 video tahmin/gerçek sıralaması; ≥10 videoda ağırlık ayarı.
