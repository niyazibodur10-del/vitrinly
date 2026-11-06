# kanal-analisti — hafıza

## Kurallar
- Veri yolu sırası: `YOUTUBE_API_KEY` (Data API v3; `channels`/`playlistItems`/`videos` 1 birim) → WebSearch [AÖ] → 3. taraf (socialblade/playboard/piped 403). `search` ayrı günlük tavanlı, trend-avcisi ile paylaşımlı: başta az ve hedefli (8–10 sorgu sorunsuz geçti 10-28, 11-04). Anahtar repoya/sohbete yazılmaz; teslimde `grep -c AIza`.
- yt-dlp altyazı güvenilmez (10-28 1/5, 11-04 0/4 bot kontrolü) → hook kanıtı için önce Data API `snippet.description` ilk cümleleri [AÇK] + thumbnail [GÖZ]; altyazıyı tek videoya harca.
- support.google.com/youtube ve blog.youtube WebFetch ile açılır → politika [B-Kn]; tek yardım sayfasına güvenme, "Changes to YPP" + resmi blogu da aç.
- Kalıp/süre istatistiği her zaman kanal içi medyana göre ve "kanal medyanı ≥1.000" filtresiyle; kalıbın kaç kanalda görüldüğünü yaz (n büyük ama 3 kanal = kanal etkisi). Hayatta kalan yanlılığını ve pivot etkisini (Fred) her zaman not et.
- Kanal seçmeden önce son yükleme tarihini ve dilini (`defaultAudioLanguage`, Devanagari başlık) API'yle ölç; Hintçe kanallar İngilizce başlıkla sızıyor (THE LOST CHAPTER, Truth Vault).
- Etiket kapısı: `uretim/2026-11-04-miras-sizintilari/01-arastirma/etiket_test.py <md> <tarih> [--bolum A B]` (etiketler API|H|ALT|GÖZ|T|ÖB|AÇK|AÖ); her rakamlı satıra açık etiket, öneri satırları [T: öneri].
- Hazır betikler (kopyala, parametrele): `uretim/2026-11-04-miras-sizintilari/01-arastirma/olcum/` → `delta90.py` (90 g, iki skor: medyan ve izlenme/abone, Shorts sayısı), `desen90.py`/`desen90b.py`, `sirala90.py` (A/B kanal sırası), `kendi.py` (kendi kanal + sabit yorum ayrımı), `haric.txt`. İlk-video kıyası: `uretim/2026-10-26-1929-1000-dolar/10-yayin-sonrasi/olcum/olc.py`.
- Kendi sabit yorumumuz commentCount'u şişirir → `authorChannelId == kanal` ile ayır. Studio CSV'yi 7 g raporundan ÖNCE koordinatörden iste; yoksa CTR/AVD dersleri yazılamaz.

## Dersler
- 2026-10-26: TR'de animasyon/maskot finans kanalı bulunamadı; kanal İngilizce/global, TR boşluğu yalnız not. Politika araştırmasında önce kanalın mevcut halini oku.
- 2026-10-27: Kalıp başlık kanalı açar, tekrarı skoru düşürür ("real reason/true origin" n=119, medyan 0,55). Konu doygunluğu = başlık taraması (n, medyan skor, ≥2x).
- 2026-10-28: maskotlu rakipler (Fred; 11-04'te Marcus Explains) → thumbnail-tasarimcisi'ne ayrışma notu.
- 2026-11-04 (F1, 90 g delta): küçük→büyük kanıtı izlenme/abone sıralamasıyla bulundu (False Profit 7,8 B abone → 777 B). Kanal medyanı tek başına küçük kanalları gizler; iki skoru birlikte ver.
- 2026-11-04: patlayan genç kanallar 0–2 Shorts / 40–79 uzun (90 g); bizim Shorts 341 izlenme → uzun +5. Shorts'u büyüme motoru diye önerme; köprü iddiasını ölçmeden yazma.
- 2026-11-04: API S08'i planlanandan (11-04 17:00Z) önce `public` gösterdi → kendi videolarında her ölçümde `privacyStatus`/`publishAt`'i plana karşı kontrol et, sapmayı koordinatöre ilk satırda bildir.
