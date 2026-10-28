# kurgu-editoru — hafıza

## Kurallar
- Kurgu katmanı animasyonu sarar (Tam altyazısız → vurgu → altyazı en üstte, ölçeksiz). Vurgu olmayan karede çıktı Tam ile piksel-aynı olmalı (still farkı 0 ile doğrula) → `~/.finansal-arac/parca/<Tam>` parçaları yeni ID dizinine hardlink, yalnız değişen parça render.
- Ses: müzik stem'i olduğu gibi; SFX zamanı görsel olaya (animasyon-efekt-cue.json + kare kontrolü), F6 dosya/kazancı korunur. Son miks Python'da örnek-doğru toplanır, `render-parca.sh --ses` ile verilir.
- Altyazı hizası kapısı: son ses ↔ anlatim.wav çapraz korelasyon (`08-kurgu/ses_kayma.py`) + `tools/ses/hiza-dogrula.py`. Ham Whisper'la doğrudan kıyas cümle başlarında 250–950 ms sahte fark verir (kapı için kullanma).
- Kadans ölçümü `kadans.py` (altyazı bandı hariç, yükselen kenar): sürekli harekette (şerit yağmuru, çizgi çizimi) olay kaçırır → >10 sn çıkan aralığı kontakt sayfasıyla elle doğrula.
- Shorts: kesit başı = altyazı öbeği başı (öbek ilk kelimesi −0,08 sn); sahne parçasını uzatma (sonraki cümle sızar) → sessiz kuyruk + yavaş itme (freezedetect); köprü kartı güvenli alanda (sağ ≤918, alt ≤1536); politika şeritleri kesit dışında kalıyorsa kurgu katmanında ekle.
- Açılış vurgusu (punch-in) 1080p kaynakta ≤1,07 algılanmıyor, büyüğü köşe etiketlerini (Illustration/Source) kırpar → açılışta metin katmanı (vaat şeridi) daha etkili.

## Dersler
- 2026-10-27 (1929-1000-dolar F7): 3 açılış varyantı → B (başlık sorusu "CAN YOU KEEP IT?" 7,9 sn); C (snap punch-in) kırpma + algılanmama ile elendi. İlk render'da şerit köşe göstergesine biniyordu — varyant karşılaştırmasında her zaman tam çözünürlük kare bak.
- render-parca.sh `-shortest` son 4 kareyi kesiyordu (18.945/18.949) → `-t` ile düzeltildi; final 4 dk'da (1/11 parça) çıktı.
- F6 SFX stem'i kelime zamanlıydı, 20+ vuruş görselden kayık; kurguda yeniden zamanlama 43 sn sürdü, WER değişmedi (%0,87 vs %0,93). Bir dahaki sefere F6 öncesi muzik-ses-tasarimcisi'ne animasyon cue'sunu kullan notu ver.
- Shorts ilk render'larında 3 kusur yakalandı (önceki cümle kelimesi 2 kare, kuyrukta sonraki cümle sesi + karartma altyazıyı gizledi, kuyruk donması) → hepsi kontakt sayfası + freezedetect ile; Shorts'ta her render sonrası 2 sn aralıklı kontakt sayfası şart.
- Shorts hook'u tek kadrajsa (3,9 sn) virgül duraklamasında ×1,05 snap → ilk görsel değişim 1,5 sn; ×1,09 alt yazıyı kenara dayadı.
- 2026-10-28 (1929 abone ol animasyonu): ortak `video/src/ortak/AboneOl.tsx` (sessiz bileşen; klik sesi miks betiğinde bas+1,3 sn, `assets/efekt/ozgun-fare-klik.flac` kendi sentez). Yerleşim tablosu tek kaynak (`kurgu_ses.py` ABONE_* → kurgu-veri.ts). Yer seçimi: kelime zamanlarından doruk/açıklama arası boşluk + mevcut finalden kare; Leo'nun karşı tarafına. Dikeyde varsayılan y 1150 S21 grafiğinin veri satırını örttü → `ust` ile 1100'e (her Shorts yerleşiminde still bak). Miks farkı ölçümü (eski/yeni wav fark aralıkları) değişikliğin yalnız klikler olduğunu kanıtladı; yalnız 4/11 parça yeniden render.
- 2026-10-28: yeniden render sonrası tam dosya uzun-form Whisper WER %0,9→%2,1 sıçradı, ses aynıyken (bölge farkı 0,0) cümle atlıyordu → değişiklik kapısı için **eski/yeni aynı pencere transkripti** kullan (±8 sn, değişen noktalarda); tam-dosya WER'i yalnız bilgi. Paralel çalışan ajan `tools/` betiklerini yarım bırakabiliyor → render öncesi `bash -n` + gerekirse `git show HEAD:` kopyasıyla çalış, araca dokunma, uretim-muhendisi'ne not.
