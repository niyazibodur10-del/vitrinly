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
