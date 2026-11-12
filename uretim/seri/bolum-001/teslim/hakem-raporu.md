# Hakem raporu (F9): Flip By Vote · Bölüm 001 "Every Dollar We Have"
İLERLEME: tamam (tur 4, yeni sesler: Pocket TTS, Jake george, Mike marius). Bölüm F10 teslime hazır; tek yayın öncesi şart ŞY-1.
**KARAR (tur 4): GEÇTİ + ŞY-1.** Video kapılarının hepsi yeni render'da yeniden ölçüldü ve geçti. Kapak ve paket yeni sha ile tutarlı. ŞY-1: `uretim/seri/lisans-kaydi.md`'de TTS satırı yok. Video dosyası değişmez, ama yayından (17:00Z) önce kapanmalı.
Gerekçe:
1. Ses değişti, ama zamanlama zinciri ölçümle tutuyor: final miks WER %0,6 (1/176, tek hata Whisper'ın p=0,07 güvenle eklediği "Jake"), senkron 0 kare (piksel) ve +1/+1 (Rhubarb), altyazı 25/25 = metin, SFX 15/15 ±2 kare.
2. Görüntü: 74,57 sn, 1080x1920, 30 fps, −14,0 LUFS / TP −2,3, siyah/donma 0. 20 rastgele karede yer tutucu 0, BANK $100 20/20, dikiş 0. Kapanış 1:1 temiz. Takip kartında yeni profil resmi; klik ile buton değişimi aynı karede.
3. Paket: dry-run "0 hata, 0 uyarı". Ses atıf satırı açıklamalarda var (CLAUDE.md 2026-11-11 kararıyla aynı metin). AI satırı var, gün sözü 0. Kapak 72,33 sn karesinden: 1:1 temiz, 108x192'de okunuyor.

## T4. Tur 4 ölçümleri (girdi sha256 **171b2487fb09**; animasyon raporuyla aynı)
| Kapı | Benim ölçümüm | Durum |
|---|---|---|
| Süre / format | ffprobe → 74,567 sn, 2237 kare, 1080x1920, 30/1; aac 48 kHz stereo 74,58 sn | GEÇTİ |
| Ses | `ebur128=peak=true` → I −14,0 LUFS, TP −2,3 dBFS, LRA 5,1 (`tur4/ebur128.txt`) | GEÇTİ |
| Siyah / donmuş | `blackdetect d=0.1 pix_th=0.10` + `freezedetect -60dB d=0.5` → 0 / 0 | GEÇTİ |
| 20 rastgele kare (seed 91141) | `tur4/r20/kontak.jpg`: yer tutucu 0, dikiş 0, altyazı güvenli alanda 20/20, BANK $100 20/20, karar kartı harfsiz + "Ep. 2: YOUR call" | GEÇTİ |
| Altyazı 25/25 | `altyazi-z1-testi.ts` → 25/25. Video tarafındaki `bolum-001.kelimeler.json` ile yeni `ses/kelimeler.json` zamanları birebir aynı (en büyük fark 0,0 sn) | GEÇTİ |
| Ağız senkronu | `agiz-piksel-senkron.py` → 13 yakın çekim, 861 kare, gecikme 0, r 0,522 · `senkron-testi.py` yeni `rhubarb/{JAKE,MIKE}.json` → +1 / +1 (`tur4/senkron.txt`) | GEÇTİ |
| WER (final miks, tam) | `yaziya-dok.py small.en` + `hata-orani.py` → **%0,6** (1/176, 28,88 sn'de p=0,07 güvenle tekrarlanmış "Jake", sesli bir hata değil). Referans = kilitli metin | GEÇTİ |
| SFX + ses çakışması (earshot, 7,3–37,3) | 13/16 cue ±2. Aykırıların stem kontrolü: tahta-hesap 26,53 (0 kare), şifonyer whoosh apex 32,42 (0 kare); 33,98 "G-boya-pop" görsel olay, ses cue'su yok (cue dosyamın hatası). Sonuç **15/15**. Konuşma maskesi: WER %0,6 ve kapanış sorusu doğru | GEÇTİ |
| Kapanış 1:1 | 70,0 / 72,33 sn 600x700 kırpım (`tur4/kapanis-1e1.png`): saç ve kulak kenarı temiz, BANK yüzle kesişmiyor | GEÇTİ |
| Takip kartı + profil resmi | 1 kez, 72,35–74,55. Yeni avatar (Jake + Mike, sarı zemin) 410 px'lik kırpımda okunuyor. Klik stem onset 73,250, FOLLOW→FOLLOWING 73,267 (0 kare) (`tur4/takip-klik.png`) | GEÇTİ |
| Kapak | 72,33 sn karesi (paketleyici commit 860fb54): 1:1 temiz, 108x192 ve 4:5'te "$100 → $1,000,000" okunuyor (`tur4/kapak-kontrol.png`) | GEÇTİ |
| Paket | dry-run 0 hata / 0 uyarı; sha 171b2487fb09 YAYIN.md ve platform-metinleri.md'de; "Voices: Kyutai Pocket TTS (CC BY 4.0); VCTK corpus (CC BY 4.0)." platform-metinleri.md'de 3/3; AI satırı var; gün sözü 0 | GEÇTİ |
| Lisans | `lisans-kontrol.py` → eksik 0, yasak 0 (müzik/SFX). **TTS satırı `lisans-kaydi.md`'de yok** (yalnız `ses/kilit.json`'da ses adı geçiyor) | ŞY-1 |

**ŞY-1 (sahip: ses-yonetmeni, son saat 17:00Z yayından önce).** `uretim/seri/lisans-kaydi.md`'ye TTS bölümü eklenecek. Satırlar: Pocket TTS kodu (MIT) ve ağırlıkları (CC BY 4.0), `george` = VCTK p315 (CC BY 4.0), `marius` (CC0); kaynak URL, erişim tarihi, lisans kanıt kopyası (`assets/lisans-kanit/`), açıklamadaki atıf metni. Video yeniden render edilmez.
Not: politika-format.md §6 "yalnız CC0 + kendi üretim" diyordu. Niyazi'nin 2026-11-11 ses kararı (CLAUDE.md) atıflı CC BY'ye izin veriyor. Atıf satırı paketin üç açıklamasında da var. monetizasyon-uyum-uzmani §6'yı bu karara göre güncellemeli (sonraki bölüm, engel değil).

---
# Tur 3 (arşiv, sha 6d01844629ec)
**KARAR (tur 3): GEÇTİ.** Z3b kapandı: kapanış ikili portresinde (80,5 / 81,0 sn) ve kapakta 1:1 incelemede kopuk saç ucu, tırtık ya da kızıl saçak yok. Ses ve görüntü kapıları tur 3 dosyasında yeniden ölçüldü. Paket yeni sha ile tutarlı.
Gerekçe:
1. Tur 1'de bulunan bütün zorunlu maddeler ölçümle kapandı: Z1 altyazı 25/25 = metin; Z2 kırpma kapağı; Z3 ve Z3b saç kenarı; Z4 BANK–yüz kesişmesi 0.
2. Kapılar: 83,2 sn · 1080x1920 · 30 fps · −14,0 LUFS / TP −2,5 · siyah/donma 0. Senkron 0 ve +1/+1 kare, SFX 21/21 ±2 kare, final miks WER'i 72–79 sn penceresinde doğru. Karar kartında harf ve gün sözü yok. Abone/takip kartı 1 kez, sonda. Ses ve zaman tur 2 ile aynı; tur 3 yalnız portre PNG'lerini değiştirdi (LUFS/TP birebir).
3. Paket: dry-run 0 hata. Kapak 81,0 sn'den yeniden üretildi, kenarı temiz, 108x192'de okunuyor. sha 6d01844629ec YAYIN.md ve platform metinleriyle tutarlı.
Kanca 6/10 (izleyici gözüyle, tur 2 ile aynı). Kalan riskler: R4 göz kapağı ovali, R5 kart girişi, R6 aşağıda.

## T3. Tur 3 fark kontrolü (girdi sha256 **6d01844629ec**)
| Kapı | Benim ölçümüm | Durum |
|---|---|---|
| Format / süre | ffprobe → 1080x1920, 30/1, 2496 kare = 83,20 sn; ses 83,20 | GEÇTİ |
| Ses | `ebur128=peak=true` → I −14,0 LUFS, TP −2,5 dBFS (`tur3/ebur128.txt`) | GEÇTİ |
| Siyah / donmuş | `blackdetect d=0.1 pix_th=0.10` + `freezedetect -60dB d=0.5` → 0 / 0 | GEÇTİ |
| Z3b kapanış kenarı | 80,5 ve 81,0 sn, 1:1 600x700 kırpım (`tur3/kenar-80.5-81.0.png`): Mike'ın sağ saç/kulak kenarı ve Jake'in sol saçı düzgün; kopuk uç 0, kızıl saçak 0 | GEÇTİ |
| Kapak kenarı + okunurluk | `kapak-1080x1920.jpg` 1:1 (`tur3/kapak-kontrol.png`): kenar temiz; 108x192 ve 4:5'te "$100 → $1,000,000" okunuyor; BANK yüzle kesişmiyor | GEÇTİ |
| Diğer portreler (gerileme) | 5 portre çekimi (`bolum-001.ts`: 16,75 / 24,02 / 35,3 / 47,25 / 70,95), `tur3/portreler.png` + 1:1 `tur3/mike-portre-sac-1e1.png`: kopuk parça yok, kızıl saçak yok | GEÇTİ (R6) |
| Paket | `yukle.py --dry-run` → 0 hata, 1 uyarı; sha 6d01844629ec YAYIN.md ve platform-metinleri.md'de; gün sözü 0 | GEÇTİ |

- **R6:** Mike'ın uç yakın portrelerinde (24,02–24,5 "gülen"; 35,3–35,7 "endişeli"; 0,4–0,5 sn, büyütülmüş ve yumuşak) saç ucunun sol üstünde ~40 px'lik açık bir leke var. Kapı değil: kısa süreli ve telefonda ~15 pt [T]. Sonraki bölümde gorsel-varlik-sanatcisi aynı temizliği uç yakın ölçekte de doğrulamalı.

---
# Tur 2 (arşiv, sha 23839dd0b183)
**KARAR (tur 2): KALDI, tek madde (Z3b).** Kapanış ikili portresinde (76,0–83,2 sn) ve kapakta Mike'ın sağ saç/kulak kenarı tırtıklı; kopuk saç parçaları ve kızıl lekeler görünüyor. Jake'in sol saç kenarında da düzensiz koyu saçak var. Hata varlık dosyasından geliyor (`ifade/mike-heyecanli-temiz.png`, yeşil zeminde de görünüyor). Z1, Z2, Z4 ve Ö1–Ö4 kapandı. Diğer bütün kapılar yeniden ölçüldü ve geçti.
Gerekçe:
1. Z3'ün kabul testi "diğer Mike portreleri (heyecanlı, kapanış) de aynı kontrolden geçer" diyordu. 1:1 kırpımda kapanış portresi geçmiyor (`hakem-log/tur2/kapanis-sac-81.png`, `kapak-sac-1e1.png`, `mike-heyecanli-yesil.jpg`). Bu kare videonun son 7 sn'si ve aynı zamanda kapak.
2. Düzeltme ucuz ve yerel: yalnız 2 PNG'nin kenarı + 3,3 dk render + kapak. Ses, altyazı ve zaman değişmez.
3. Seçenekler: (a) ŞARTLI ONAY, çünkü telefonda ~1/2,8 ölçekte kusur ince görünüyor; (b) KALDI. Seçimim (b): kusur, en çok bakılan durağan karede (kapanış + kapak) duruyor ve kapı ölçümle kalıyor. (a)'nın riski, 100 bölümlük dizinin ilk kapağında "yapıştırma" izlenimi bırakmak.
Kanca (tur 2): **6/10** (tur 1'de 5). Tempo 24–58 sn: kabul edilebilir (§T2).
Paket v2: **kontrol edildi, geçti**. Kapak Z3b'den sonra aynı kareden (81,0) yeniden üretilecek.

## T2. Tur 2 fark kontrolü (girdi sha256 **23839dd0b183**; animasyon raporundakiyle aynı)
| Kapı | Benim ölçümüm (komut → sonuç) | Durum |
|---|---|---|
| Format / süre | ffprobe → h264 1080x1920, 30/1, 2496 kare = 83,20 sn; aac 83,20 sn | GEÇTİ |
| Ses | `ebur128=peak=true` → I **−14,0** LUFS, TP **−2,5** dBFS, LRA 2,6 | GEÇTİ |
| Siyah / donmuş | `blackdetect d=0.1 pix_th=0.10` + `freezedetect -60dB d=0.5` → 0 / 0 | GEÇTİ |
| Z1 altyazı | `animasyon/altyazi-z1-testi.ts` (esbuild+node) → 25/25 ekran = metin. `zaman.ts` LCS kodunu okudum: ekrana yalnız `metin` kelimesi yazılıyor. Kareler (`tur2/z1-kareler.png`): 35,85 "Two." · 38,6 "Free." · 48,95 "buy" · 49,95 "Slow." | GEÇTİ |
| Z2 göz kırpma | Kırpma takvimini koddan çıkardım (`kirpmaTakvimi`), 5 kırpmada 2'şer kare (`tur2/z2-kirpma.png`), 1:1 4 kare (`tur2/z2-goz-1e1.png`): düz çizgi 0, tek renk disk 0, kirpik kavisli; Mike yakın çekim ve kancada kırpma kapalı | GEÇTİ (R4) |
| Z3 şaşkın portre | 41,6 / 42,0: konuşan Mike tabanı + punch-in; ağız "Free?" ile oynuyor | GEÇTİ |
| **Z3b kapanış portreleri** | 1:1 kırpım 80,5 / 81,0 + kapak + varlık yeşil zeminde: Mike sağ saç/kulak kenarı tırtıklı, kopuk saç ucu, kızıl saçak; Jake sol saçında koyu saçak. Alfa adası sayısı 1 (`tur2/alfa-adalar.txt`): ada yok, kenar tırtıklı ve renk bulaşığı var | **KALDI** |
| Z4 BANK–yüz | 80,0 / 82,0 / 81,0 ve kapak: rozet Mike'ın saç üstünde, kaşla arasında boşluk var, yüzle kesişme 0 | GEÇTİ |
| Ö1 kapanış sorusu | 72–79 sn final Whisper → "We let them decide. Bike dresser or mystery box? Tell us in the comments." (`tur2/whisper-72-79.txt`) | GEÇTİ |
| Ağız senkronu | piksel 0 kare (r 0,621, 1027 kare) · Rhubarb +1/+1 (`tur2/senkron.txt`) | GEÇTİ |
| SFX ±2 (earshot, 2,3–32,3 + 50,0–80,0) | 18/21. 3 aykırıyı stem'de açtım: tik 12,585 (−0,4 kare, earshot tahta sesine eşledi), disk +0,15, karar-kartı whoosh apex 76,03–76,05 (−0,5…−1) → **21/21** (`tur2/sfx-hiza.txt`) | GEÇTİ |
| Abone/takip kartı | 1 kez, 81,0–83,2. Klik stem onset 81,900; FOLLOW→FOLLOWING değişimi 81,88 (0 kare) (`tur2/abone-klik.png`) | GEÇTİ |
| 30 rastgele kare (seed 91131) | `tur2/rastgele30/kontak.jpg`: yer tutucu 0, BANK $100 30/30, altyazı güvenli alanda 30/30, yeni dikiş 0 (kapanış kenarı yalnız 1:1'de görünüyor) | GEÇTİ |
| Paket v2 | dry-run "0 hata, 1 uyarı"; made for kids=false, sentetik=true; AI satırı 3/3; gün sözü 0; kapak 108x192'de "$100 → $1,000,000" okunuyor (`tur2/kapak-kucuk.png`); sha/süre 23839dd0b183 / 83,2 | GEÇTİ (kapak Z3b'ye bağlı) |

**Z3b düzeltmesi.** Sahip: gorsel-varlik-sanatcisi (`mike-heyecanli-temiz.png`, `jake-dusunceli.png`); ardından animasyon-yonetmeni render alır, youtube-paketleyici kapağı 81,0 sn'den yeniden üretir. Yöntem: alfa üzerinde açma/kapama (3–5 px) ile tırtık ve kopuk uç temizliği, 2–3 px feather, kenardaki kızıl/koyu bulaşık piksellerin saç tonuna çekilmesi (`sac-hale-temizle.py` aynı mantığı yalnız haleye uyguluyordu, tırtığa uygulamıyordu).
**Kabul testi:** yeşil zemin kompoziti + 80,5 / 81,0 sn 1:1 kırpım + kapak 1:1. Kenarda kopuk saç ucu, tırtık ve kızıl saçak olmayacak.

**T2 izleyici gözüyle.**
- **Kanca 6/10.** Kare 0'da büyük banknot havada ve kamera hareketli; çarpma 0,1 sn'de net okunuyor. Marka çipi köşeye alınmış. Eksisi: ilk 0,5 sn'de kadraj gövde üstünde, yüz yok, yani ilk karede duygu yok. Tavsiyem: kadrajın en az bir yüz içermesi; sonraki bölüm için not, kapı değil.
- **Tempo 24–58 sn** (`tur2/tempo-24-58.jpg`, 1 fps): her 1–3 sn'de kesme, punch-in ya da ikon var; ilanlar yüzü kapatmıyor. Tur 1'deki "menü" hissi azaldı.
- 37,4 sn'de şifonyer kartı uçarak girerken 2 kare boyunca altyazının üstünden geçiyor (`tur2/kart-giris-30fps.jpg`). Altyazı üstte kaldığı için okunuyor (R5).

---
# Tur 1 (arşiv, sha 8588a182aeba)
**KARAR: KALDI.** 4 zorunlu düzeltme var: Z1 altyazı yazımı, Z2 göz kırpma kapağı, Z3 Mike portresinin saç kesiği, Z4 kapanışta BANK'ın yüze binmesi. Hepsi tek render turunda (≈3,3 dk) kapanır. Ses, süre, format, senkron, SFX, WER, karar kartı, abone kartı ve paket geçti.
Gerekçe:
1. **Altyazı yazım kapısı kaldı** (`docs/kalite-kapilari.md`: "yazım hatası yok"). 25 satırın 2'sinde ekrandaki yazı ham Whisper çıktısı: "**To** a solid wood dresser." (doğrusu "Two. … Free." — "Free." hiç görünmüyor) ve "So we rent a truck **by** paint and wait." (doğrusu "buy"; "Slow." görünmüyor). Kök neden `video/src/seri/zaman.ts` → `ekranKelimeleri`: kelime sayısı tutmayınca kilitli metne değil Whisper token'ına düşüyor.
2. **Yüzde iki yapay kenar var**, bu yüzden "yüz dikişi 0" kapısı kaldı. Birincisi: göz kırpma kapağı yakın planda düz ten diski ve gözü kesen düz siyah çizgi olarak görünüyor; rastgele 30 karemin 1'inde (k-0309) yakalandı ve kancanın 1,75. saniyesinde Mike'ta da var. İkincisi: Mike'ın "şaşkın" portresinde (41,6–42,1 sn, tam ekran) saç kesiğinde beyaz/açık hale lekeleri görünüyor.
3. **Kapanışta ve kapak görselinde BANK rozeti Mike'ın alnını/kaşını örtüyor** (78,6–85,0 sn, `kapak-1080x1920.jpg`). Videonun izleyicide kalan son karesi ve küçük resmi bu. Kalan kapılar ölçümle geçti (tablo aşağıda).
Kanca puanı (izleyici gözüyle): **5/10**. Gerekçesi §3'te.
Paket: **geldi ve kontrol edildi**. Kapılarını geçti; yalnız kapak, Z4 düzelince yenilenecek.

## 1. Kapı tablosu (girdi `teslim/bolum-001.mp4` sha256 **8588a182aeba**; animasyon raporundaki sha ile aynı)
| Kapı | Benim ölçümüm (komut → sonuç) | Durum |
|---|---|---|
| Süre 60–90 | ffprobe → video 85,000 sn / ses 85,013 sn | GEÇTİ |
| Format | ffprobe → h264 1080x1920, 30/1, 2550 kare; aac 48 kHz stereo | GEÇTİ |
| Ses −14 ±1 LUFS / TP | `ebur128=peak=true` → I **−14,0** LUFS, TP **−2,5** dBFS, LRA 2,6 | GEÇTİ |
| Siyah / donmuş kare | `blackdetect d=0.1 pix_th=0.10` + `freezedetect -60dB d=0.5` (ajanın d=1'inden sıkı) → 0 / 0 | GEÇTİ |
| 30 rastgele kare (seed 91130) | `hakem-log/rastgele30/kontak.jpg`, kareler `kareler.txt` | ↓ |
| · yer tutucu / hata ayıklama yazısı | 0/30 (ayrıca 85 karelik 1 fps BANK şeridi) | GEÇTİ |
| · yüz / ağız / kol dikişi | ağız 0, kol 0. **Yüz: 1/30 göz kapağı yaması (k-0309)** + Mike şaşkın portresinde saç halesi (`portre-saskin.jpg`, `sac-kapanis.jpg`) | **KALDI → Z2, Z3** |
| · altyazı güvenli alanda | 30/30 y≈1300–1420, x≈100–950. IG/YT sağ sütun ve alt bant dışında | GEÇTİ |
| · BANK metinle tutarlı | `hakem-log/bank-1fps.png`: 85/85 saniye "BANK: $100"; tahta "$100 − $60 = $40" (`tahta-hesap.jpg`) = metin R4 | GEÇTİ |
| Altyazı yazımı | `ekranKelimeleri` mantığı satır bazında yeniden koşuldu → **2/25 satır ham Whisper**; karede doğrulandı (`altyazi/altyazi-kontak.png`: "To a", "truck by") | **KALDI → Z1** |
| Ağız senkronu (sha aynı → örneklem yerine ucuz tam koşu) | `agiz-piksel-senkron.py` (15 yakın çekim, 1189 kare) → gecikme **0 kare**, r 0,584 · `senkron-testi.py … rhubarb/{JAKE,MIKE}.json 30 --bant 700-3000` miksli finalde → **+1 / +1 kare** | GEÇTİ (ajanla birebir) |
| WER (final miks, tam) | `yaziya-dok.py small.en` + `hata-orani.py ses/referans.txt` → **%3,4** (6/176). Kuru seste ses-yonetmeni %2,8 ölçmüştü; fark: miksde "bike→like" | GEÇTİ (≤%5), Ö1 |
| SFX ±2 kare (earshot, 2 rastgele pencere) | `tools/earshot timeline --cues hakem-log/cues-hakem.json` 12,0–42,0 + 45,7–75,7 → 23/25. 2 aykırı vuruşu stem'de elle açtım: S2-sifir-1 gerçek tik 12,585 (−0,5 kare; earshot önceki tahta sesine eşlemiş), S6-ikon-disk 60,674 (+0,2) → **25/25** | GEÇTİ |
| Karar kartı | 80,0 sn karesi: "Bike, dresser, or mystery box?", seçenekler ROAD BIKE $60 · FREE DRESSER · MYSTERY BOX $40 (ikon, harf/numara yok), "Ep. 2: YOUR call". `grep tomorrow|drops|friday|tonight` → video/src/seri bölüm 001'de 0, paket 3 dosyada 0 | GEÇTİ |
| Abone/takip kartı | 1 kez, 81,5–85,0 (sonda, karar kartından sonra). Klik sesinin başlangıcı 82,800 = FOLLOW→FOLLOWING kare değişimi (`abone-klik.png`, 0 kare) | GEÇTİ |
| Karakter tutarlılığı | 30 karede ve kanca/kapanış karelerinde Jake ve Mike'ın kıyafeti, saçı ve göz rengi aynı. Mike'ın önden portreleri tabandan daha çizgi filmsi (büyük göz). Aynı kişi okunuyor | GEÇTİ (R2) |
| Lisans | `lisans-kontrol.py` → {"dosya":20,"kayitli":28,"eksik":[],"yasak_lisans":[]}. Görseller: Canva media ID'leri `karakter/rapor.md`'de (J-A, M-A, L1-A/B, T-J, T-M) | GEÇTİ (Ö6) |
| Paket | `yukle.py yayin-paketi.json --dry-run` → hata 0, `selfDeclaredMadeForKids:false`, `containsSyntheticMedia:true`. AI satırı 3 platformda var. Anonimlik satırı var. Kapak 108x192'de "$100 → $1,000,000" okunuyor (`kapak-kucuk.png`) | GEÇTİ (kapak Z4'e bağlı) |

## 2. Düzeltme listesi (ajan bazlı; tek tur, sonra tek render)
| No | Ajan | Ne | Kabul testi |
|---|---|---|---|
| **Z1** | animasyon-yonetmeni (şablon `video/src/seri/zaman.ts`; uretim-muhendisi bilgilendirilsin, diğer bölümler de etkilenir) | `ekranKelimeleri`: sayı uyuşmazlığında **ekrana hiçbir zaman Whisper token'ı yazma**. Metin kelimelerini difflib/LCS ile Whisper zamanlarına eşle; eşleşmeyen kelimelere komşu zamanlardan ara değer ver. Bölüm 001'de etkilenen satırlar: J "Two. A solid wood dresser. Free. We paint it, flip it." ve M "So we rent a truck, buy paint, and wait. Slow." | Betik: 25/25 satırda ekran kelimeleri = `metin.split()`. 36,3 / 38,8 / 49,0 / 50,3 sn karelerinde "Two.", "Free.", "buy", "Slow." görünüyor |
| **Z2** | animasyon-yonetmeni | Göz kırpma kapağı yakın planda düz disk ve düz çizgi olarak görünüyor. Seçenekler: (a) kapak dolgusunu dikey ten gradyanı + 2–3 px yumuşak kenarla boyamak, kirpik çizgisini göz konturuna oturtmak (düz yatay çizgi olmasın); (b) zoom ≥1,15 olan çekimlerde ve kancada (0–3 sn) kırpmayı kapatmak. Ucuz yol (b), kalıcı yol (a) | 1:1 kontakt: 2 yakın + 2 geniş çekimde birer kırpma, her birinde 4 kare. Düz çizgi ya da tek renk disk yok |
| **Z3** | gorsel-varlik-sanatcisi (yama) → animasyon-yonetmeni (yerleşim) | Mike "şaşkın" portresinin saç kenarındaki açık hale lekelerini temizle (saç matlaması / kenar renk çekme). Alternatif: 41,6–42,1'de portre yerine Mike'ın konuşan tabanına punch-in. Bu tabanda ağız da "Free?" ile oynar | 1:1 saç kenarı kırpımı (`sac-saskin.jpg` ile aynı alan): açık piksel halesi yok. Diğer Mike portreleri (heyecanlı, kapanış) de aynı kontrolden geçer |
| **Z4** | animasyon-yonetmeni → youtube-paketleyici (kapak) | 78,6–85,0 ikili portrede BANK rozeti Mike'ın alnını örtüyor. Portreleri ~120 px aşağı al ya da bu çekimde yüzleri rozetin altına yerleştir. Rozetin yeri (incil §4.1 üst-sol) değişmez. Sonra kapak 81,6 sn karesinden yeniden üretilir | 80,0 / 84,0 kareleri ve iki kapak: rozet hiçbir yüzle kesişmiyor (kutu kesişimi 0) |
| Ö1 (öneri, aynı render'a girsin) | muzik-ses-tasarimcisi | `whoosh-kart` 74,50 doğrudan "**Bike**," kelimesinin üstüne düşüyor. Finalde Whisper "Like, dress" duyuyor; kuru seste doğru. Whoosh'u −6 dB indir ya da 1 kHz altını kes | 72–79 sn penceresinde final Whisper: "Bike dresser or mystery box" |
| Ö2 | animasyon-yonetmeni | Kanca: ilk kare statik ikili çekim. Banknot küçük ve alt-orta, "FLIP BY VOTE · EP. 1" çipi 0–2,5 sn ekran ortasında Mike'ın göğsünün üstünde. Banknot ilk karede havada başlasın (yakın + punch-in), çip üste ya da 2,5 sn sonrasına | ilk 2 sn kontakt |
| Ö3 | animasyon-yonetmeni | İlan kartları konuşanın yüzünü kapatıyor (24,6–28,6 Mike; 37,5–41,4 Jake; 53,6–58 Mike). Kartı alt-yarıya kaydır, yüz ve ağız görünsün | 3 kare |
| Ö4 | animasyon-yonetmeni | 47,3–48 sn: araba ikonu Jake'in alnına/kaşına biniyor. Yüz dışına taşı | 1 kare |
| Ö5 | muzik-ses-tasarimcisi | `lisans-kaydi.md` kullanım sütunu bayat: fare-klik 71,87 → gerçek **82,80**; whoosh 53,51 → 53,56; çarpma 0,00 → 0,10 | `ses-cue.mutlak.json` ile birebir |

## 3. İzleyici gözüyle
**Kanca 5/10.** Artısı: "That's it. Every dollar we have." güçlü bir cümle, ses 0,1 sn'de vuruyor ve BANK $100 ilk karede görünüyor. Eksisi: ilk kare iki kişinin durduğu statik bir geniş plan; çarpan banknot küçük, alt-ortada ve 3 karede bitiyor; kaydırırken ilk göze çarpan şey ekranın ortasındaki marka çipi. 1,75. sn'de Mike'ın göz kapağı yaması görünüyor (Z2). "Ne oluyor?" sorusu ancak 6–9 sn'de ("Two best friends. One hundred bucks.") netleşiyor. Ö2 uygulanırsa tahminim 6–7 [T].
Zayıf anlar:
- **Tempo:** 24–58 sn üç ilan arka arkaya ve yapı "ilan kartı → yorum → şaka" diye tekrarlıyor. Menü gibi akıyor, en düşük yer burası. "Air is free / Tires aren't" gag'i çalışıyor. Kutu bölümü (54–62) en zayıf şaka.
- **Ağız / ifade:** göz kırpma yaması (Z2); 41,6'da Mike portresi bulanık, hale var ve "Free?" ağzı oynamayan portrede söyleniyor (Z3). İlan kartları konuşanın ağzını kapatıyor (Ö3).
- **Kapanış:** 81,5–85,0 arasında yalnız takip kartı var, CTA sonrası 3,5 sn ölü kuyruk. Reels döngüsünde bu süre kayıp. Süre payı var ama kartı 2,0 sn'ye indirmek değerlendirilmeli [öneri].
- **Anlaşılmayan şaka:** ölçülebilir bir örnek bulamadım. "Fridge has mustard" görselle (hardal ikonu) destekleniyor.

## 4. Riskler
- R1: Z1'in kök nedeni şablonda. Düzeltilmezse her bölümde Whisper'ın eşsesli hatası (two/to, buy/by) ekrana çıkar. Bu şablon riskidir, tek bölüm sorunu değil.
- R2: Mike'ın önden portreleri tabandan daha çizgi filmsi. Günlük dizide izleyici bunu "farklı çizim" diye fark edebilir [T]. 5 bölümlük denetimde ölçülmeli (`karakter/rapor.md` kor. ölçümüyle).
- R3: Takip kartında "FOLLOW" yazıyor. YouTube'daki karşılığı "Subscribe". Aynı video üç platformda kullanıldığı için kabul edilebilir, ama karar koordinatörde.
- R4 (tur 2): Göz kapağı 1:1'de hâlâ hafif bir oval olarak seçiliyor; sağ gözde kapağın üstünden orijinal kirpik ucu taşıyor. Telefon ölçeğinde 4 karelik kırpmada fark edilmez [T]. Kapı değil, şablon iyileştirmesi.
- R5 (tur 2): İlan kartları uçarak girerken 2 kare altyazının üstünden geçiyor. Altyazı üstte kaldığı için okunuyor. Kapı değil.

## 5. Yeniden ölçüm planı (Z1–Z4 sonrası, fark kontrolü)
sha256 → ffprobe + ebur128 + black/freeze (tam) → Z1 betiği 25/25 → Z2/Z3/Z4 kontakt kareleri → 72–79 sn pencere Whisper (Ö1) → `cmp` ile değişmeyen ses yolunda WER'i yeniden koşmadan geç. Ham çıktılar: `teslim/hakem-log/`.
