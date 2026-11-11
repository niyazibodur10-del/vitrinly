# Hakem raporu (F9): Flip By Vote · Bölüm 001 "Every Dollar We Have"
İLERLEME: tamam (tur 1). Sıradaki adım: Z1–Z4 düzeltmeleri, yeniden render, ardından hakemin fark kontrolü.
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

## 5. Yeniden ölçüm planı (Z1–Z4 sonrası, fark kontrolü)
sha256 → ffprobe + ebur128 + black/freeze (tam) → Z1 betiği 25/25 → Z2/Z3/Z4 kontakt kareleri → 72–79 sn pencere Whisper (Ö1) → `cmp` ile değişmeyen ses yolunda WER'i yeniden koşmadan geç. Ham çıktılar: `teslim/hakem-log/`.
