# Hakem raporu (F9): Flip By Vote · Bölüm 002 "Meet Brenda"
İLERLEME: tamam (tur 1).
**KARAR: GEÇTİ.** Bölüm 1'in tur 1–4 kapı setindeki her kapıyı bu dosyada yeniden ölçtüm; kalan kapı yok. İkame SFX'lerden "PAT" iç lastik patlaması olarak okunmuyor (Ö1). Kapak Bölüm 1'inkiyle neredeyse aynı (Ö2). İkisi de kapı değil, öneri.
Gerekçe:
1. Süre 88,27 sn (90 sınırına 1,73 sn pay). Ses −14,0 LUFS / TP −2,6. Siyah/donma 0/0.
2. Senkron ve altyazı: piksel senkron 0 kare, Rhubarb +1/+1, altyazı 29/29 = kilitli metin, final miks WER %3,6 (≤5). SFX 22/22 ±2 kare (2 pencere).
3. Görüntü ve paket: 30 rastgele karede dikiş 0, BANK metinle tutarlı ($100 → $40 → $24). Kapanış 1:1 temiz. Takip kartı 1 kez, sonda. Karar kartında harf ve gün sözü yok. Paket dry-run 0 hata, Z2 atıf satırı 3/3 platformda.
Kanca **6/10**, tempo iyi (§3).

## 1. Kapı tablosu (girdi sha256 **8ba870ac5b0e**, animasyon raporundakiyle aynı)
| Kapı | Benim ölçümüm | Durum |
|---|---|---|
| Süre / format | ffprobe → 88,267 sn (2648 kare), ses 88,277; 1080x1920, 30/1 | GEÇTİ (pay 1,73 sn) |
| Ses | `ebur128=peak=true` → I −14,0 LUFS, TP −2,6 dBFS, LRA 4,3 (`hakem-log/ebur128.txt`) | GEÇTİ |
| Siyah / donmuş | `blackdetect d=0.1 pix_th=0.10` + `freezedetect -60dB d=0.5` → 0 / 0 | GEÇTİ |
| 30 rastgele kare (seed 92002) | `hakem-log/r30/kontak.jpg`: yer tutucu 0, dikiş 0, altyazı güvenli alanda 30/30. BANK $100 → $40 (DAY 2 sayaç geçişi) → $24, tahta "$60 + $16 = $76", "$90 − $76 = $14" metinle aynı | GEÇTİ |
| Altyazı 29/29 | `altyazi-z1-testi.ts` → 29/29. Videodaki `bolum-002.kelimeler.json` = `ses/kelimeler.json` (zaman farkı 0,0) | GEÇTİ |
| Ağız senkronu | `agiz-piksel-senkron.py` → 14 yakın çekim, 930 kare, gecikme 0, r 0,568 · `senkron-testi.py` → +1 / +1 (`hakem-log/senkron.txt`) | GEÇTİ |
| WER (final miks, tam) | `yaziya-dok.py small.en` + `hata-orani.py` → **%3,6** (7/194). Tam dosyada "counter → count her" ×2 çıktı. Pencerede yeniden ölçtüm: final 74,0–78 "Then we counter, meet him at 115", 81,5–86 "or counter? Tell us in the comments." → segmentasyon artefaktı, miks maskelemesi değil (`hakem-log/counter-pencere.txt`) | GEÇTİ |
| SFX ±2 (earshot; cue = `ses-cue.mutlak.json` sfx) | 0–30 + 42,2–72,2 → 16/22. 6 aykırıyı stem'de açtım: pop/ding onset −0,5 / −0,3 / +0,2 kare; whoosh'lar apex hizalı, tepe 21,40 / 22,30 / 47,95 = 0 kare → **22/22** (`hakem-log/sfx-hiza.txt`) | GEÇTİ |
| Kapanış 1:1 | 85,33 / 87,4 sn 600x700 (`hakem-log/kapanis-1e1.png`): saç ve kulak kenarı temiz, BANK yüzle kesişmiyor | GEÇTİ |
| Takip kartı | 1 kez, 86,05–88,25; yeni profil resmi. Klik stem onset 86,950; FOLLOW→FOLLOWING 86,967 (0–1 kare) (`hakem-log/takip-klik.png`) | GEÇTİ |
| Karar kartı | "Take the ninety, hold out, or counter?" · TAKE $90 · HOLD OUT $140 · COUNTER $115 · "Ep. 3: YOUR call": harf/numara 0, gün sözü 0 (`hakem-log/detay.png`) | GEÇTİ |
| Paket | dry-run "0 hata, 1 uyarı"; sha 8ba870ac5b0e YAYIN.md + platform-metinleri.md; Z2 satırı ("CC BY 4.0: creativecommons.org/…" + Sources) 3/3 platform + YT açıklaması; AI satırı; MFK=false, sentetik=true; gün sözü 0 | GEÇTİ |
| Lisans | `lisans-kontrol.py` → eksik 0, yasak 0; TTS satırları `lisans-kaydi.md` 50–52'de (Bölüm 1 ŞY-1 kapanmış) | GEÇTİ |
| Kapak | 86,0 sn karesi: 1:1 temiz, 108x192'de "$100 → $1,000,000" okunuyor (`hakem-log/kapak-kontrol.png`) | GEÇTİ (Ö2) |

## 2. İkame SFX: earshot ile dinledim (`earshot match`, stem kesitleri)
| Olay | Kullanılan | Ölçüm | Hüküm |
|---|---|---|---|
| S1 "flap" (0,1 sn, Brenda yuvarlanıyor) | kutu-tikirti | "flat bicycle tire… flapping" → eşleşme yok (z +0,8). En yakın: "snare roll", "playful and quirky" | Lastik değil, çizgi film tıkırtısı gibi duruluyor. Kancada kabul edilebilir |
| S4 pompa ×3 | whoosh-kisa | "bicycle hand pump hiss of air" → **strong** (z +3,8) | Doğal duruyor |
| S4 "PAT" (24,0 sn, ikinci kanca) | tezgah-carpma + plak-cizik | "inner tube bursting, loud pop" → eşleşme yok (z +1,1). En yakın: "snare roll" (+4,6), "record scratch" (+3,8) | **Tuhaf:** patlama yerine trampet + plak cızırtısı duyuluyor. Görsel gag (portre + sarsıntı) çalışıyor, ama ses "patladı" demiyor → Ö1 |

## 3. İzleyici gözüyle
- **Kanca 6/10.** Kare 0'da Mike'ın yüzü var, bisiklet kadraja yuvarlanıyor, önceki seçim şeridinde "BIKE ✓". 2,5 sn'deki "BRENDA" etiketi iyi bir isim şakası. Eksi: ilk cümle "No comments, so I picked." Yeni gelen izleyiciye "bu dizi izlenmiyor" sinyali veriyor (sosyal kanıt eksi) [T]. Koordinatörün Z1 kararı bu; esprili ton riski yumuşatıyor.
- **Tempo:** 34 kesme, 24,0'da PAT, 47,95'te mekân değişimi (L3) + saat, 58,45 "$90 cash", 78,4 "yazıyor…". 10–15 sn'de bir yeniden kanca var; Bölüm 1'den daha diri. 33–37 sn'de tahta hesabı arka arkaya 3 karede kalıyor, en yavaş yer orası.
- **Zayıf anlar:** 16,3 sn'de "SERIAL CHECK ✓" kartı Jake'in ağzını kapatıyor ("though" sırasında). 62,3 sn'de mesaj kartı Mike'ın alnına biniyor. İkisi de kısa.

## 4. Öneriler ve riskler (kapı değil)
- **Ö1 (muzik-ses-tasarimcisi, Bölüm 3'e kadar):** `earshot forge` ile "inner tube pop" ve "flat tire flap" üret, kütüphaneye ekle; kabul ölçütü `match` "strong". Bu bölüm için yeniden render şart değil.
- **Ö2 (youtube-paketleyici):** Kapak Bölüm 1'inkiyle aynı şablon ve aynı ikili portre; değişen yalnız "EP. 2" ve BANK. Günlük dizide ızgara aynı görünür; politika §2.5 (görsel tekrar) ve tıklama açısından zayıf. Bölüme özgü kanca öğesi ekle (Brenda + "$90 cash?").
- **R1:** Kapanıştaki ikili portre her bölümde aynı. Politika §2.5 "sabit kartlar hariç" diyor; 5 bölümlük denetimde monetizasyon-uyum-uzmani ölçmeli.
- **R2:** Süre 88,27 sn, sınıra yakın. Bölüm 3 metninde kelime bütçesi ≤195 tutulmalı (Pocket TTS ölçülen hız).
