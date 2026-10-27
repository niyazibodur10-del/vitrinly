# F9 Hakem raporu — "You Have $1,000 in 1929. Can You Keep It?" + 2 Shorts

**Hakem:** hakem (bağımsız) · **Tarih:** 2026-10-27 · **Girdi:** `08-kurgu/final-16x9.mp4`, `shorts-1.mp4`, `shorts-2.mp4`, `final.en.srt`, `09-paket/*`, `07-animasyon/senkron-rapor.md`, `04-ses/ses-rapor.md`, `06-muzik/lisans-kaydi.md`, `05-gorsel/canva-promptlari.md` §5.
Her satır **benim yeniden ölçümüm**. Ajan raporuna yalnız kendi ölçümümle karşılaştırmak için baktım.

## KARAR: ONAY (GEÇTİ), yayın öncesi 1 idari şart

**Şart (ŞY-1, koordinatör, render gerekmez):** Ö9'un kanal düzeyi yarısı açık. Kanal Hakkında metninde videoların insan ekip tarafından hazırlandığı yazmıyor (`uretim/kanal-kimligi/kanal-paketi.json`). F11 yüklemesinden önce Hakkında'ya şu satır eklenmeli: *"Researched, written and produced by the Toonomy team."* Kanal ayarlarını Niyazi koordinatöre bıraktı. Bu yüzden video RED almaz, Niyazi'den ek bir şey istenmez.

**Gerekçe (3 madde)**
1. **Teknik kapıların hepsi geçti ve ajan raporlarıyla birebir tutuyor.** Süre 10:31,6. Ses −14,0 LUFS / TP −2,2. Siyah kare ve donma yok. Dudak senkronu +1 kare (ağzın göründüğü 13 aralığın hepsi ≤2 kare). WER %0,9 (15/1726). Shorts 49,6 / 56,0 sn. sha256 değerleri 3/3 eşleşiyor.
2. **YPP politika kapısı geçti.** `sentetik_medya=true` 3/3 pakette. AI satırı, "Not financial advice" ve "fictional cartoon character, not a financial adviser" satırları 3/3 açıklamada. Lisans kontrolü exit 0 (55 dosya, kayıtsız 0, NC/ND 0). TTS Apache-2.0. Canva için 23 üretimin hepsinde media ID var. Sahne tekrarı %0,0. Ö1–Ö12'de tek kısmi madde Ö9 (kanal düzeyi, ŞY-1).
3. **Retention kapısı geçti.** Kanal tanıtımı ve logo yok, ilk kare SEPT 1929 + anlatım. İlk görsel değişim 2,0 sn'de (≤3). Vaat sesle 0:09'da ("one door is a disaster…"), ekranda 7,9 sn'de ("CAN YOU KEEP IT?"), yani ilk 15 sn içinde. Retention haritası `03-metin/metin.md` §13'te. Gerçek sesle 13 yeniden kanca var, en uzun aralık 71,7 sn (≤90).

## Kapı tablosu (kendi ölçümüm)

| Kapı | Ölçüt | Benim ölçümüm (komut) | Ajan raporu | Sonuç |
|---|---|---|---|---|
| Dosya bütünlüğü | sha256 = sha256.txt | `sha256sum -c 08-kurgu/sha256.txt` → final OK · shorts-1 OK · shorts-2 OK | aynı | ✓ |
| Format/süre | 1080p+, doğru fps, ≥10 dk | ffprobe: 1920x1080, 30/1, h264+aac 48 kHz 2 kanal, **631,633 sn, 18.949 kare** | aynı | ✓ |
| Ses (son dosya) | −14 ±1 LUFS, TP ≤ −1 | ebur128 peak=true: final **−14,0 / −2,2 dBTP / LRA 2,0** · Sh1 −14,0 / −3,4 · Sh2 −14,0 / −3,6 | aynı | ✓ |
| Siyah kare / donma | 0 | blackdetect d=0.1 pix=0.10 + freezedetect n=0.003 d=2: final 0/0, Sh1 0/0, Sh2 0/0 | aynı | ✓ |
| Dudak senkronu | ≤2 kare (ağız görünür) | `tools/senkron-testi.py final-16x9.mp4 07-animasyon/rhubarb/tum-kapili.json 30 --araliklar <13 aralık, agiz-gorunur.json>`: geniş bant **+1 kare** (kor. 0,38) · formant **+1** (0,53), aralık başına 1–2 kare. Not: F5 ölçümü müziksiz kaynakta yapılmıştı, ben miksli finalde ölçtüm, sonuç değişmedi | +1 / +1 | ✓ |
| Anlaşılırlık (WER) | miks anlatımı bozmuyor | `yaziya-dok.py small.en` + `hata-orani.py 04-ses/referans-metni.txt` → **1726 kelime, 15 hata, %0,9**. Benim Whisper JSON'um kurgu-editoru'nunkiyle bayt bayt aynı (deterministik) | %0,87 | ✓ |
| Shorts transkripti | onaylı okuma metni | Sh1 ve Sh2 metinleri okundu, kapanışlar "prices were falling" / "arithmetic, not a plan" var. Sh1 JSON bayt aynı, Sh2 yalnız zaman ondalığında farklı | aynı | ✓ |
| Altyazı | yazım 0, ±150 ms, ≤42 karakter, ≤2 satır | kendi SRT tarayıcım: 228 blok, çakışma 0, satır ihlali 0. **>21 kr/sn olan 16 blok, en yüksek 24,1, >25 olan 0.** Hiza: ses ↔ anlatim.wav ofseti 0 (Whisper JSON eşleşmesi + kurgu 12 pencere) | 16 blok bilgi notu | ✓ (risk R3) |
| Bölümler | gerçek sahne başına denk | 8 bölüm ↔ `04-ses/sahne-zamanlari.json`: fark 0,0 / 0,7 / 0,5 / 0,5 / 0,7 / 1,0 / 0,9 / 0,9 sn (hepsi sahne başından ≤1 sn önce) | ±1 sn | ✓ |
| Paket | başlık ≤60, dry-run 0 hata | `yukle.py --dry-run` 3/3: **0 hata 0 uyarı**. Uzun: başlık 41, açıklama 3370/5000 bayt, etiket 373/500, thumbnail 1280x720 131 KB, SRT 228 blok, yayın 2026-11-01T17:00Z. Sh1 başlık 42, Sh2 başlık 47 | aynı | ✓ |
| Yasal not | "Not financial advice" + "Narration voice is AI-generated" + atıflar | `tam_aciklama()` çıktısında 3/3 pakette her ikisi + "fictional cartoon character" var. Müzik/SFX CC0 atıfları açıklamada | aynı | ✓ |
| Telif/lisans | her dosya kayıtlı, NC/ND yok | `06-muzik/lisans-kontrol.py` → dosya 55, kayıtsız 0, yasak lisans [], cue kayıtsız [] (exit 0). TTS Kokoro Apache-2.0 (`ses-rapor.md`). Canva 23 üretim, 23 media ID + tarih (`canva-promptlari.md` §5). Thumbnail kaynak media ID'leri `thumb-rapor.md`'de | aynı | ✓ |
| Thumbnail | 168x94'te okunur, ≤4 kelime, içerikle tutarlı | Lanczos 168x94 küçültme (kendi yan yana sayfam): A2 "ONE IS A DISASTER", B1 "THE SURPRISE DOOR", D1 "EVERY DOOR LOCKED" okunuyor. 3 kelime ≤4. Gerçek kişi/logo yok. Üçü de videoda geçiyor (0:09 disaster, 10:00 SURPRISE, S17 kilitler) | aynı | ✓ |
| Başlık–thumbnail–hook | tek vaat | T1 "Can You Keep It?" ↔ ekranda 7,9 sn "CAN YOU KEEP IT?" ↔ A2 kapılar + "disaster" ↔ hook "one door is a disaster, one is a gamble, one is a surprise" | aynı | ✓ |
| Retention (ilk 30 sn) | intro yok, vaat ≤15 sn, ilk değişim ≤3 sn | 16 karelik kendi kontakt sayfam (0–15 sn, 1 fps): intro/logo yok, 2. sn'de sokaktan stüdyoya kesme, 8. sn'den itibaren "CAN YOU KEEP IT?" şeridi, 10–13 sn DISASTER?/GAMBLE?/SURPRISE? | aynı | ✓ |
| Shorts | 1080x1920, ≤60 sn, ilk 2 sn kendi kancası, −14 ±1 | 1080x1920, 49,58 / 56,04 sn. İlk kare yazılı kanca + Leo (Sh1 "the smartest-looking door was the worst one", Sh2 "A shoebox of cash gained power in 1932"). −14,0 / −14,0 | aynı | ✓ (risk R2) |
| YPP: AI beyanı | `sentetik_medya` pakette + satır | 3/3 `true`. Dry-run gövdesinde `containsSyntheticMedia: true` | aynı | ✓ |
| YPP: maskot tavsiye vermiyor | 0 tavsiye | 3 transkripti okudum: emir yok, kişiye özel yönlendirme yok. Bugüne dönük tek cümle "That's arithmetic, not a plan." (tavsiyeyi reddeden çerçeve) | 0 | ✓ |
| YPP: reused/dış görüntü | 0 | 3 videonun kontakt sayfalarında dış klip yok. Tüm görseller Canva kaydında ya da kod. Sahne tekrarı %0,0 (politika-f8.py, 632 kare; betiği yeniden koşmadım, girdisi olan final sha256'sı eşleşiyor) | %0,0 | ✓ |
| YPP: Ö1–Ö12 | 12/12 | 11 ✓ + **Ö9 kısmi**: açıklamada "animated by our team" var, Hakkında'da insan ekip satırı yok | Ö9 kısmi | **ŞY-1** |

## Açık riskler, değerlendirmem

| # | Risk | Kendi ölçümüm | Karar |
|---|---|---|---|
| R1 | S18'de boş lacivert an | 486,5–490,5 sn arası 4 fps kare: **487,5–489,0 sn (~1,5–1,75 sn)** ekranda yalnız altyazı ("WHEN THE HOLIDAY ENDS / ABOUT FOUR") ve kaynak etiketi var. ~489,25'te "~4,000 BANKS NEVER REOPENED" geliyor. Anlatım sürüyor, siyah kare değil, kadans kuralı (5–10 sn'de değişim) bozulmuyor | Kabul. Kapı ihlali değil. Düzeltmek için parça render + yeniden miks + bütün kapıların yeniden ölçümü gerekir (≈40–60 dk), kazancı 1,5 sn. F12'de bu noktada tutma düşüşü varsa ders olur. animasyon-yonetmeni'ne not |
| R2 | Shorts 1 S10 kesiti | 13–18 sn arası kareler: ~4 sn yalnız "DOOR 2: THE SCORE" başlığı ve altyazı, grafik ~17. sn'de giriyor. En zayıf an | Kabul (Shorts kapısını geçiyor). Hook ve kapanış güçlü. Sonraki dikey kesitte grafik ≤1 sn'de girmeli |
| R3 | 16 SRT bloğu >21 kr/sn | en yüksek 24,1, >25 olan 0. Kaynak TTS hızı 161,6 kpm | Kabul. Bloğu bölmek zamanlamayı değiştirmez, CC'de okunabilirlik sınırında. Sonraki metinde 160 kpm hesabı (ses-yonetmeni dersi) |
| R4 | Shorts 2: grafikte 48 ay, anlatımda 12 ay | 30–55 sn kareleri: önce "12 MONTHS TO SEPT 2026 / +3.7% / $964" kartı anlatımla eşleşiyor. Ardından ayna grafik "SEPT 2022 → SEPT 2026, 48 MONTHS" etiketli ve anlatım "In 2026, prices are rising" diyor (rakam söylemiyor). Açıklama iki pencereyi açıkça yazıyor | Kabul. Etiketli, yanıltıcı rakam eşleşmesi yok. Bir dahaki seferde Shorts'ta tek pencere kullanılmalı |
| R5 | "Tension" (Komiku) Content ID | CC0 kanıtı var, Content ID garantisi yok | Yükleme sonrası Telif sekmesi kontrolü (YAYIN.md §2.8) |
| R6 | Leo yarı gerçekçi görünüm (P8) | açıklama + Hakkında maskot satırı var | ŞY-1 bunu da güçlendiriyor |

## Belirsiz karar: 2 seçenek
- **A) ONAY + ŞY-1 (SEÇİLDİ).** Riski düşük: Ö9 açığı kanal metninde, video dosyasında değil. Koordinatörün yetkisiyle 1 API çağrısıyla kapanır. Slot (01.11 12:00 ET) korunur.
- **B) RED → S18 boşluğu + Sh1 S10 düzeltmesi + Ö9.** Kazanç ~1,5 sn ölü an ve 4 sn zayıf Shorts anı. Maliyeti ≥1 render turu, kapıların yeniden ölçümü ve 2 düzeltme turu sınırına bir tur yaklaşmak. Ölçülen hiçbir kapı kalmadığı için RED'in gerekçesi ölçüme değil zevke dayanırdı → elendi.

## Teslim (`teslim/`)
`final-16x9.mp4`, `shorts-1.mp4`, `shorts-2.mp4` → `../08-kurgu/` dosyalarına sembolik bağ (git dışı, sha256 yukarıda). Thumbnail'lar A2/B1/D1 ve `final.en.srt` kopya. `yayin-paketi*.json` değiştirilmeden kopyalandı: yollar `../08-kurgu/` ve `../09-paket/` olduğu için `teslim/`den de çözülüyor, `teslim/` içinden dry-run 3/3 0 hata. Ayrıca `YAYIN.md`, `politika-raporu.md`, bu rapor.
