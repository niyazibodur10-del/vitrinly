# hakem — hafıza

## Kurallar

## Dersler
- 2026-10-26: Yeni görev — her ajan teslimatını `docs/ajan-karnesi.md`'ye 1–10 puanla (kalite, test kanıtı, protokol uyumu, hız). Rakip analizi v1 ve viralite modeli v0.1 henüz puanlanmadı ("—").
- 2026-10-27 (F2 secim, S03 kazanan / S01 yedek): Bileşik puanı **iki durumda** hesapla: taramaların bugünkü rengi ve zorunlu düzeltmeler sonrası kalan risk. Bu turda düzeltme öncesinde S01 0.22 öndeydi (eşik altı), düzeltme sonrasında S03 30/30 kazandı. Bu yüzden karar "şartlı kazanan + ölçülebilir yedek tetikleri" diye yazıldı. Tek durumla hesap yanıltır.
- 2026-10-27: Eşitlik bozucuyu (ilk 15 sn = viralite hook puanı) betiğe göm (`hakem-karar.py`) ve ±0.05 ağırlık duyarlılığını her iki durum için çalıştır. Kazananı değiştiren oynatmaları listele, "çoğu" gibi yazma (bu turda "çoğu" yazmıştım, liste "tamamı" gösterdi, düzelttim).
- 2026-10-27: Yedek seçiminde ölçüt "aynı slotu kim kurtarır": aynı konu + YEŞİL/YEŞİL olan, F3'e sıfırdan araştırmayla dönen farklı konudan iyidir. Farklı konu yalnız ana konu taramada çökerse tercih edilir.
- 2026-10-27: Karne puanında ajanın kendi işaretlediği eksiği (ör. viralite tur 2'yi doğrulamasız yapması) daha hafif, başka ajanın yakaladığı hatayı (KH-A12, son-20 medyanı) daha ağır say.
- 2026-10-27: `roast` skill'i alt ajanda giriş soruları sorduğu için çağrılamıyor; 5 açıyı (eleştirmen, savunucu, analist, araştırmacı, izleyici) elle uygula ve bunu dosyada belirt.
- 2026-10-27 (F9 1929-1000-dolar, ONAY + ŞY-1): Senkron kapısını **miksli finalde** yeniden koş (F5 müziksiz kaynakta ölçmüştü). Komut: `senkron-testi.py final.mp4 07-animasyon/rhubarb/tum-kapili.json 30 --araliklar <agiz-gorunur.json>` (+ `--bant formant`). Sonuç değişmedi (+1), ama kapının gerçek dosyada geçtiği ancak böyle kanıtlanır.
- 2026-10-27: Whisper (faster-whisper small.en, int8) deterministik. Kendi JSON'um kurgu-editoru'nunkiyle bayt bayt aynı çıktı. Sonraki sefer `cmp` ile hızlı bağımsız kanıt al: 10 dk ses ≈2 dk 10 sn (4 çekirdek). Kalan küçük fark yalnız zaman ondalığında olur.
- 2026-10-27: "Açık risk" listesini kendi karelerimle ölç (4 fps kontakt): S18 "~1 sn" dediği an gerçekte ~1,5–1,75 sn çıktı. Ajanın verdiği süreyi değil kendi ölçtüğümü yaz. Kapıyı bozmayan ama ölçülebilen risk RED gerekçesi değildir. RED ancak bir kapı ölçümle kalınca verilir; aksi zevke dayanır.
- 2026-10-27: Ö1–Ö12'de "kısmi" kalan ve video dosyası dışında (kanal metni) olan madde için RED yerine adlandırılmış, sahibi belli bir yayın öncesi şart (ŞY-n) yaz. Dosya değişmez, slot korunur.
- 2026-10-27: Teslim paketindeki yayin-paketi*.json'ları değiştirmeden kopyala (yollar `../08-kurgu` → `teslim/` kardeş klasör olduğu için çözülür). mp4'leri sembolik bağla ver ve dry-run'ı `teslim/` içinden koş.
