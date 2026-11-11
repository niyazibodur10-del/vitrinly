# hakem — hafıza

## Kurallar
- F2: bileşik puanı iki durumda hesapla (bugünkü renk + zorunlu düzeltme sonrası); eşitlik bozucuyu ve ±0.05 duyarlılığı `hakem-karar.py`'de koş, kazananı değiştiren oynatmaları tek tek listele. Fark eşik altıysa "puan değil kural" diye yaz.
- F2 yedek: aynı slotu kurtaran (aynı konu, YEŞİL/YEŞİL) adayı seç. Politika "önerme" dediği aday ilk 3'e girmez. `roast` alt ajanda çalışmıyor, 5 açıyı elle uygula.
- Karne: ajanın kendi işaretlediği eksik hafif sayılır, başkasının yakaladığı hata ağır sayılır. RED yalnız ölçümle kalan kapıya verilir; kanal metni eksiği ŞY-n olarak yazılır.
- Senkron ve WER her zaman **miksli finalde** ölçülür. Whisper small.en deterministik → `cmp` ile kanıt yeterli. ffmpeg döngülerinde her zaman `-nostdin` kullan.
- Abone/klik: kör ses dedektörü kullanma. Doğru yöntem: kart kutusunda kırmızı→gri dönüşü + SFX stem'inde onset. earshot cue'sunu yalnız SFX olaylarından kur (kesmeleri katma).
- SFX ±2 dışında kalan her vuruşu stem'de elle aç: earshot çoğu zaman bir önceki sesi eşliyor (3 videoda 3 sahte aykırı).

## Dersler
- 2026-10-27: "Açık risk" sürelerini kendi kontakt karemle ölç; ajanın verdiği süreyi değil kendi ölçtüğünü yaz.
- 2026-10-27: Teslimdeki yayin-paketi*.json'ları değiştirmeden kopyala, dry-run'ı `teslim/` içinden koş.
- 2026-11-02: Uç ekran başlangıcını son abone kartının bitişiyle karşılaştır (ŞY).
- 2026-11-10 (miras): her grafiğin 9:16 kesitini 0,5 sn kontaktla aç; dikeyde metin üstüne binme oluyor.
- 2026-11-11 (FBV B001, KALDI): Altyazı **yazımını** satır bazında betikle denetle (ekran kelimeleri = `metin.split()`). Şablon, kelime sayısı tutmayınca ham Whisper'a düşüyordu ("To a", "truck by"). Ajanların 20 karelik denetimi yalnız güvenli alana bakıyor.
- 2026-11-11: Rastgele karelere ek olarak 1:1 yüz kırpımları aç: göz kırpma anını (4 kare), tam ekran portrelerin saç kenarını ve son karede rozet/yüz kesişimini. Küçük kontaktta bu üçü görünmüyor.
- 2026-11-11: Kapanış sorusunu 7 sn'lik pencerede final ile kuru ses karşılaştırarak dinlet. WER geçse bile SFX anahtar kelimeyi bozabilir ("Bike" → "Like").
- 2026-11-11 (B001 tur 2): Kenar kusuru için PNG'yi yeşil zemine bindirip incele; alfa ada sayısı 1 çıksa bile tırtık ve renk bulaşığı kalabilir. Kabul testinde "diğer kullanımlar"ı (kapanış/kapak) adıyla yaz, ajan yalnız adı geçen kareyi düzeltiyor. Tesseract renkli/konturlu altyazıda işe yaramıyor, kare aç.
