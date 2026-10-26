# ses-muhendisi — hafıza

## Kurallar
- Temizleme zinciri `tools/ses/temizle.sh` (highpass 80 → RNNoise arnndn → afftdn → de-ess → EQ → kompresör → 2 geçişli loudnorm → baş/son kırpma). Ajan tanımındaki eski "DeepFilterNet" ifadesi gerçek zincir değildi; zincir değişirse betik + bu dosya birlikte güncellenir.
- Son yayın LUFS'u son stereo dosyada ölçülür (mono→stereo ~+3 LU fark); normalizasyon `tools/render-son.sh`'de.
- Whisper (medium.en) aynı sese ±2 kelime oynar: tek WER sayısına değil, ölçümler arasında tekrar eden hatalara bak.
- Yama birleştirme: sessiz noktadan (−50 dB altı enerji) kes, 12 ms fade, sonra TEK loudnorm geçişi (`tools/ses/birlestir.py`).

## Dersler
- 2026-10-26 (ses testi v1, iPhone Sesli Notlar AAC 48 kHz mono): ham −15.3 LUFS / tepe +0.7 dBFS / gürültü −37 dB → temiz −14.1 LUFS / −1.0 dBFS / −58.3 dB (−21 dB iyileşme). Whisper hata oranı ham %11.7 → temiz %10.0: temizlik anlaşılırlığı bozmadı.
- 2026-10-26 (v2 yama): kanal adı "Financial Rise" 3 okumanın en iyisiyle (güven 0.997) kalıcı düzeldi. Daha kötü çıkan yama okumaları (R2, R3) kullanılmadı → yamayı kelime bazında değerlendir, toplam kazanç yoksa eskiyi koru.
- 2026-10-26: Kalıcı hatalı kelimeler (crashes, bold, scenarios, charts, complicated) ses işleme ile değil metin tarafında (senaryo-yazari eşanlamlı) çözülür.
- 2026-10-26: `tools/ses/temizle.sh` başlık yorumunda eski yol (`tools/ses-temizle.sh`) yazıyor; doğru yol `tools/ses/temizle.sh`.
- 2026-10-26 (TTS anlatıcı seçimi): Kokoro-82M (Apache-2.0) 11 erkek ses + Piper (CC0/PD) 4 ses denendi; WER hepsinde %0–1.7 → anlaşılırlık ayırt etmez. Ayırt eden ölçümler: kelime/dk, perde ortalaması/değişkenliği (YIN, `tools/ses/ses-olc.py`), Whisper kelime güveni, Kokoro'nun kendi not tablosu (VOICES.md). Kazanan am_michael hız 0.95 (yedek am_fenrir 0.9).
- 2026-10-26: Kokoro tek parça üretimde ~205–230 kelime/dk konuşur; çözüm hızı kısmak değil cümle bazlı üretim + duraklama (cümle 0.30 / soru 0.40 / "..." 0.55 / paragraf 0.65 sn, `tools/ses/tts.py`). Hız arttıkça kanal adı güveni düşüyor (0.9: 0.89 → 1.0: 0.72 → 1.1: 0.45) → kanal adı gibi kritik kelimeleri hız taramasıyla ayrıca ölç.
- 2026-10-26: Cümle kırpmada 5 ms ön pay "No boring charts" başındaki /n/'yi yedi (Whisper "news/videos" duydu, 3 varyantta tekrar) → ön pay 30 ms, son pay 50 ms. Tekrarlayan tek kelime hatası = kesme/işleme hatası şüphesi.
- 2026-10-26: Kokoro çıktısının tepe/ortalama oranı ~23 dB → doğrusal loudnorm −14.9'da kalır; önce hafif kompresör + kazanç + sınırlayıcı, sonra loudnorm (`tools/ses/tts-son.sh`). AAC kodlaması tepeyi ~0.1–0.3 dB yükseltir → TP hedefi −1.5.
- 2026-10-26: Müzik-konuşma farkı K-ağırlıklı anlık LUFS ile ölçülür (ebur128 M); 100 Hz üstü ağırlıksız RMS bas ağırlıklı müzikte farkı ~10 dB fazla gösterdi. Miks doğrulaması: son miks dosyasında Whisper WER (müzik maskelemiyor mu?).
- 2026-10-26: Kör testte Niyazi yedek sesi (am_fenrir 0.9) seçti; varsayılan anlatıcı artık o. Uzun metinde tını/tempo tutarlılığını bu sesle ölç.
- 2026-10-26 (pilot v2): Pilot v1 Niyazi'nin okumasıyla render edilmişti; karar am_fenrir 0.9 idi. **Pilot/üretim sesi her zaman karar verilen anlatıcıyla yapılır; render öncesi ses kaynağını kontrol et** (`.zaman.json` içindeki `ses`/`hiz` + perde ölçümü: fenrir ~153 Hz, Niyazi ~106 Hz + video sesi ile anlatım stem'i korelasyonu).
- 2026-10-26: Kokoro Python 3.13'te kurulamıyor → ayrı venv `~/.finansal-arac/kokoro-venv` (python3.12, torch CPU index + `pip install kokoro soundfile`); Whisper/numpy işleri eski venv'de kalır.
- 2026-10-26: miks.py yalnız AAC yazar; Remotion için m4a → WAV açıldığında hizalama kaybı yok (çapraz korelasyon 0 ms). Müzik adayı seçimi: aynı ayarla (−6/6) Unsolved Investigation 22.6 dB (bantta), Mysterywave 25.3 dB (fazla kısık).
