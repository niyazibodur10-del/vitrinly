# viralite-analisti — hafıza

## Kurallar
- Hesap yalnız `tools/viralite.py` ile; ağırlıklar betikte tek yerde (`OLCUTLER`), doküman tablosu onunla aynı olmalı; ağırlık toplamı 1.00 assert.
- Model v0.1'in tüm ağırlıkları TAHMİN [T]; güven DÜŞÜK, ±0.05 belirsizlik; 0.3 puandan küçük sıralama farkı anlamsız.
- "Somut özne yoksa merak ≤6" tavanı ağırlıklandırmadan önce uygulanır.

## Dersler
- 2026-10-26 (v0 → v0.1): kalibrasyon verisi rakip-analizi v1 (5 global kanal, ≈6 outlier, üçüncü taraf/arama özeti). Kanıtlı talep ağırlığı 0.15 korundu, ölçüm yerel medyan tabanına alındı.
- 2026-10-26: Yeniden kalibrasyon tetikleri: (1) YouTube API ile rakip verisi → outlier'ların ölçüt puanlarıyla korelasyonu; (2) kendi kanalımızda ≥5 video → tahmin/gerçek sıralama karşılaştırması, ≥10 videoda ağırlık ayarı; her kalibrasyon sürüm artırır (v0.2…).
- 2026-10-27 (F2, ilk gerçek puanlama, 11 senaryo): Rakip kanıtını "son-20 medyanı" yerine API ile **yerel medyan** ölçerek kur (`02-senaryo/viralite-outlier.py`: yalnız videos/channels/playlistItems, search kotasına dokunma). Büyüyen kanalda fark büyük çıktı: Markets of the Past Great Depression 4,4x (son-20) → 7,6x (yerel). Yerel medyan yöntemi doğrulandı; her F2'de yeniden kullan.
- 2026-10-27: Yeni yüklenmiş videoyu (≤7 gün) karşı kanıt sayma (Black Monday 5 günde 0,48x); komşu sayısı <10 olan skoru (Fred n=5) bir kademe zayıf say.
- 2026-10-27: Benzerlik cezası başlıkla sınırlı değil, **tez kurgusu** da taşınabilir (S02 = MotP "crash was a symptom"). Cezalı/bonuslu her yargıyı `viralite-girdi-varyant.json` ile "yargı olmasaydı" satırı olarak göster; ilk 3'ü değiştiren yargıyı hakeme açıkça yaz. Konunun tek outlier'ının başlık çekirdeğini taşıyan çalışma başlığı (S08 "all the world's silver") ceza alır, alternatif başlıkla tekrar puanla.
- 2026-10-27: Duyarlılık betiği (`viralite-duyarlilik.py`: 56 çift ±0.05 + kötümser/iyimser aralık + çapraz test) işe yaradı: kırılganlığın yalnız 3. sırada (S06↔S04) olduğunu gösterdi. "Kırılgan" etiketini sıra bazında ver, tüm listeye değil.
- 2026-10-27: Model v0.1 metni Türkçe döneme göre yazılmış (ceza = "TR'ye taşıma/çeviri"); kanal İngilizce → v0.2'de ceza tanımı "İngilizce rakip başlık kalıbı/kurgusu" olarak yeniden yazılacak. Seri bonusu format serisini (S03 "aynı oyun başka yılda") kapsamıyor; v0.2'de ayrı ele al. Kalibrasyon için `yt-analytics.readonly` kapsamı şart (CTR/AVD/30 sn tutma).
- 2026-10-27 (F8, S03 son puan): Bitmiş paket F2 ile aynı çıktı (8.40); F8'in değeri puan değil güven: hook/görsel/tek vaat zinciri ölçülmüş ürün özelliği oldu. Paket kombinasyonlarını yalnız **merak** ölçütünde ayır (thumbnail hook/hikâyeyi değiştirmez); model thumbnail'ları ayıramıyor (fark 0.20 < 0.3) → kararı Test & Compare'e bırak, modelle zorlama.
- 2026-10-27: Başlık iskeletini puanlamadan önce rakip havuzunda kalıp ölçümü yap (`09-paket/viralite-baslik-kalip.py`, yalnız playlistItems+videos, ~100 birim): 2.394 videoda soru/you/$N/yıl tek başına nötr (0.85–0.95 vs 0.98), T1 iskeleti n=0. Niş dışı kanallar (film kanalı) havuzu kirletiyor → sonraki ölçümde kanal filtresi ekle.
- 2026-10-27: Test & Compare kuralı (support 16391400): belirsiz sonuçta **ilk yüklenen varyant kalıcı** → yeni kanalda (az gösterim) sıra = en iyi ön tahmin ilk. Planlı/gizli videoda test kurulamaz, API yok (Studio masaüstü, gelişmiş özellikler şart). Başlık ve thumbnail'ı ayrı ardışık testlerde ölç (kalibrasyon verisi temiz kalsın).
- 2026-10-27: Hook için konuşma hızını ölç (kelimeler-hizali.json, 'words' anahtarı, s/e): S03 ilk 30 sn 168 kelime/dk < rakip bandı 175–225 → hook kötümser 8. ses-yonetmeni ile paylaşılacak ders.
