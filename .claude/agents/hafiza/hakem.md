# hakem — hafıza

## Kurallar

## Dersler
- 2026-10-26: Yeni görev — her ajan teslimatını `docs/ajan-karnesi.md`'ye 1–10 puanla (kalite, test kanıtı, protokol uyumu, hız). Rakip analizi v1 ve viralite modeli v0.1 henüz puanlanmadı ("—").
- 2026-10-27 (F2 secim, S03 kazanan / S01 yedek): Bileşik puanı **iki durumda** hesapla: taramaların bugünkü rengi ve zorunlu düzeltmeler sonrası kalan risk. Bu turda düzeltme öncesinde S01 0.22 öndeydi (eşik altı), düzeltme sonrasında S03 30/30 kazandı. Bu yüzden karar "şartlı kazanan + ölçülebilir yedek tetikleri" diye yazıldı. Tek durumla hesap yanıltır.
- 2026-10-27: Eşitlik bozucuyu (ilk 15 sn = viralite hook puanı) betiğe göm (`hakem-karar.py`) ve ±0.05 ağırlık duyarlılığını her iki durum için çalıştır. Kazananı değiştiren oynatmaları listele, "çoğu" gibi yazma (bu turda "çoğu" yazmıştım, liste "tamamı" gösterdi, düzelttim).
- 2026-10-27: Yedek seçiminde ölçüt "aynı slotu kim kurtarır": aynı konu + YEŞİL/YEŞİL olan, F3'e sıfırdan araştırmayla dönen farklı konudan iyidir. Farklı konu yalnız ana konu taramada çökerse tercih edilir.
- 2026-10-27: Karne puanında ajanın kendi işaretlediği eksiği (ör. viralite tur 2'yi doğrulamasız yapması) daha hafif, başka ajanın yakaladığı hatayı (KH-A12, son-20 medyanı) daha ağır say.
- 2026-10-27: `roast` skill'i alt ajanda giriş soruları sorduğu için çağrılamıyor; 5 açıyı (eleştirmen, savunucu, analist, araştırmacı, izleyici) elle uygula ve bunu dosyada belirt.
