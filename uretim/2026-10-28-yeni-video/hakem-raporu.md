# F9 Hakem raporu — S08 "If America Earned $5,400 a Month, Here's Its Budget" + 2 Shorts · 2026-11-02 ~18:00 UTC

**KARAR: ONAY.** Her kapıyı kendim yeniden ölçtüm; tablodaki 19/19 satır geçti. Video dosyalarına dokunulmayacak. Yayından önce render gerektirmeyen tek bir Studio şartı var (ŞY-1). K3 (≤ 2026-11-03 17:00 UTC) tutuldu, slot Çar 2026-11-04 12:00 ET.
**ŞY-1 (koordinatör/youtube-paketleyici, Studio):** Uç ekran 11:03'te değil, **11:07'de** başlasın (11 sn, sınır ≥5 sn). Abone-3 kartı 662,6–666,1 sn'de ekranda (kare 19878 + 105). YAYIN.md'deki 11:03–11:18 aralığı kartla 3 sn çakışıyor.
**Gerekçe:**
1. **Teknik kapılar ajan ölçümleriyle birebir.** Final sha256 403ee6df0af2 (teslim/ ile aynı). 1920x1080, 30 fps, 678,2 sn. −14,0 LUFS / TP −3,3. Siyah ve donma 0. Senkron miksli finalde 1 kare. SRT 240 blok, sorun 0, hizalama sapması 0 ms. Ham hata %0,6 (normalizasyon hariç).
2. **YPP kapısını final dosyada kendim koştum.** `politika-f8.py --video final` sonucu hata 0. Yeniden kullanılan sahne %3,1. Eşleşen 6 kareyi açıp baktım: hepsi koyu bulanık arka planlı yeni grafik, gerçek tekrar 0. AI satırı 3/3, `sentetik_medya: true` 3/3. Lisans 31/31 ve exit 0. Tavsiye kalıbı SRT'de 0.
3. **Retention ve abone kapıları kendi dedektörümle doğrulandı.** İlk görsel değişim <1 sn, intro/logo yok, vaat 9,4 sn'de yazılı. Abone sayısı 4/1/1, hepsi kırmızı→gri dönüşüyle tespit edildi. Klik sesi görsel tıkla 0,0 ms hizalı.
**Kanıt (ham çıktılar):** `09-paket/hakem-log/` (dosya adları tabloda). Teslim dry-run'ı `teslim/` içinden 3/3 0 hata.

## Kapı tablosu (her satır benim ölçümüm)
| Kapı | Komut → sonuç | Log |
|---|---|---|
| Bütünlük | sha256 final 403ee6df0af2 · sh1 1ec621210e9f · sh2 c0b2aec801fc · srt 479cc079982c = kurgu kaydı = teslim/ | — |
| Kurgu (ffprobe) | 1920x1080 / 1080x1920 ×2, 30 fps, H.264 + AAC 48 kHz st · 678,20 / 57,39 / 41,92 sn (≥10 dk ✓, Shorts ≤60 ✓) | ffprobe.txt |
| Ses | ebur128: final −14,0 LUFS / TP −3,3 · sh1 −14,0 / −3,2 · sh2 −13,9 / −3,6 (±1, ≤−1 ✓) | olcum-*.txt |
| Siyah / donma | blackdetect d0,5 + freezedetect d2: 0 / 0 / 0 | olcum-*.txt |
| Dudak senkronu | `senkron-testi.py final… tum-kapili.json 30 --araliklar <40 aralık, 236,5 sn> --bant 700-3000` → 1 kare GEÇTİ. Tek sapma S01 9,32–13,06 −4 (3,7 sn pencere); tam sahne 2,25–16,03 → 1 kare | senkron-final.txt |
| Altyazı biçim | 240 blok: numara/biçim/çakışma/boş 0 · ≤2 satır · maks 42 kr · maks 21,8 kr/sn · <0,7 sn 0 | srt-tarama.txt |
| Altyazı yazım | SRT'deki 1.895 kelimenin kilitli metinde olmayanı 0. WER örneklemi (sha aynı → 2 rastgele 60 sn + S05 en uzun ağız aralığı): 350 kelimede ham 24 hata, 22'si rakam yazımı → gerçek 2 (%0,6). Kurgu 26, benim↔kurgu fark 4 kelime | wer-orneklem.txt |
| Altyazı hiza | Blok başı − akustik hizalama 240/240, maks 0 ms. Anlatım stem'inde 3 blok başında ses başlangıcı 0–50 ms (Whisper'ın ±0,5 sn sapması Whisper gürültüsü) | srt-tarama.txt |
| İlk 30 sn | 0,5 sn Capitol küçülür, 1,0 sn mutfak, 2,0 sn Leo · intro/logo yok · vaat şeridi 9,4–13,1 sn · hook ilk 15 sn'de | ilk3sn.jpg, ilk30-sahne.txt |
| Retention haritası | `03-metin/metin.md` §3: 14 kanca, ABONE-1..3 · kurgu ↺14 boşluğunu şeritle kapattı (kare kontrolü ✓) | vurgu-kontakt.jpg |
| Kurgu vurgu katmanları (3) | Vaat şeridi 9,6/12,8 sn · "3 ENVELOPES" köşeli parantezi + "$3,765 SPENT" çerçevesi 106,8/110 sn · "TIME = A·B·C" 525/527,6 sn → altyazı, Leo ve grafikle çakışma yok, yeni rakam yok | vurgu-kontakt.jpg |
| Abone (sayı / yer) | Düğme kutusu dedektörü, kırmızı→gri, 4 fps: uzun **4** (175,5 · 305,1 sağ/sol · 449,6 · 662,6) · sh1 **1** (52,7 / 57,4, sonda) · sh2 **1** (38,2 / 41,9, sonda). İlk 60 sn'de yok. #4 S19 doruğundan (454,9) 1,8 sn önce bitiyor | abone-say.txt |
| Abone (klik hizası) | Uzun: final sesi ↔ klikli miks çapraz ilinti 0,0 ms (5 nokta). Klik penceresinde final, klikli miksle kliksizden 2,4–2,9 dB daha iyi eşleşiyor → klik var, başı görsel dönüş karesinde (kare +39) → **0 kare 4/4**. Shorts: anlatımsız yatakta klik şablonu +0,04 / +0,00 kare, yatak ↔ final 0,0 ms → **0 kare 2/2** | klik-hiza.txt |
| SFX hizası | 5 rastgele vuruş (tohum 20261102). Stem çapraz ilinti ±0,5 sn → 5/5 cue'da (0 kare). Görsel başlangıç farkları 0 / +2 / +2 / +2 / +4 kare. +4 (438,64) dedektör hatası: önceki sahne kesmesini yakaladı. Karede kart 438,667'de giriyor → +0,7 kare. **5/5 ±2** | sfx-orneklem.txt, sfx-438-kontakt.jpg |
| Thumbnail | 3/3 1280x720, 98–111 KB · 168x94'te üçü de okunur · ≤4 kelime · gerçek kişi/logo yok · "INTEREST > MILITARY" = net faiz 1.051,8 > savunma 965,2 (MTS) | thumb-168x94-x2.png |
| Başlık–thumbnail–hook | Başlık "$5,400 a Month" · A1 "−$2,000 EVERY MONTH" · hook "5,400 in / about 7,400 out … where the gap goes" · vaat şeridi "−$2,000 A MONTH" → tutarlı (politika-f8 [3] 12/12 VAR) | politika-f8-final.txt |
| Paket | `paket-kontrol.py --final` → 66 OK, 0 hata, exit 0 · `yukle.py <3 paket> --dry-run` → 10/7/7 kontrol, 0 hata (09-paket ve teslim/) · başlık 51/51/59 kr · bölüm 7, sahne başına ≤1 sn (04:31 = S12 zarf kayması 271,75) · açıklama: "Not financial advice" + "Narration voice is AI-generated" + "fictional" + CC0 atıf 3/3 · gizlilik private, çocuk false, niyazi_onayi false | paket-kontrol-final.txt, dry-run*.txt, aciklama-kontrol.txt, bolum-kontrol.txt |
| YPP politika (video) | `politika-f8.py --video 08-kurgu/final-16x9.mp4` → hata 0 · tekrar %3,1 (≤20). 6 eşleşen kareyi elle açtım: gerçek tekrar 0. Dış klip 0 · lisans 31, kayıtsız/NC/ND/SA 0 · AI beyanı 3/3 · SRT'de tavsiye kalıbı 0 · Leo "fictional cartoon character, not a financial adviser" | politika-f8-final.txt, tekrar-kontakt.jpg |
| Lisans + Canva kaydı | `06-muzik/lisans-kontrol.py` → 31 dosya, exit 0 · kullanılan Canva üretimleri (G01, G03, G05, G06, G07, G09, G10) `canva-ham/uretim-kaydi.md`'de media ID + tarih ile; rig/jestler 1929 kaydında; thumbnail'da yeni üretim yok | lisans-kontrol.txt |

## Riskler (RED gerekçesi değil, ölçülebilir)
1. **Klik sesi kısık.** Klik −17 dB kazançla giriyor (1929 ile aynı). İlk 5 ms'de 1,9 kHz bandında yatağa göre #1 −1,1 dB, #2 +2,9 dB, #3 −7,2 dB, #4 −8,6 dB. #3 ve #4 müzik altında zor duyulabilir. Kapı "klik sesi var + hizalı" diyor, iki koşul da sağlanıyor. Sonraki video için kurgu-editoru'na: kazançta +4–6 dB dene ve kulak testiyle karar ver.
2. **Grafikte yuvarlama farkı.** "$3,765 SPENT" doğru (1.667,1 + 1.072,6 + 1.025,6 = 3.765,3), ama yuvarlanmış etiketlerin toplamı 3.766. Dikkatli bir izleyici yorumda yakalayabilir. Önceden hazır yanıt `yorum-yanitlari.md`'ye eklenebilir.
3. **SRT'de rakamlar yazıyla.** "twenty twenty-six", "one thousand fifty dollars" gibi. Okunurluk tercihi, hata değil. Sonraki videoda `final.en.srt`'de rakam kullanımı düşünülebilir.
4. Viralite 7,25 [T], model v0.1, kalibrasyon yok. Varsayılan thumbnail A1; A1/C1 farkı ayırt edilemez, Test & Compare karar verecek.

## Seçenekler
(a) **ONAY + ŞY-1.** Seçildi: hiçbir kapı ölçümle kalmadı. (b) RED (klik kazancı). Reddedildi: kapı ölçütü sağlanıyor, risk zevk düzeyinde. RED bir render turu ve K3'ü kaçırma riski getirirdi.
