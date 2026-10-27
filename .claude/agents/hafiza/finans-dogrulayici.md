# finans-dogrulayici — hafıza

## Kurallar
- Rakamın **ne olduğunu** da doğrula: kapanış mı gün içi mi, fiks mi vadeli mi, posted price mı piyasa mı, nominal mi reel mi, fiyat mı toplam getiri mi. Çelişkilerin çoğu farklı ölçülerden çıkıyor (Hunt: 49,45 $ Londra fiksi / 50,35 $ COMEX gün içi / 48,70 $ önceki gün kapanışı).
- Almanca/İngiliz uzun ölçek tuzağı: Almanca "Billion" = 10^12 = İngilizce trillion. PBS bile Rentenmark'ı "one billion" diye yanlış çevirmiş. İç tutarlılık hesabıyla sına (1 $ = 4,2 RM).
- Etiket sayısı risk ölçüsü değildir: hiç `[doğrulanacak]` olmayan senaryoda da hesap hatası çıkabilir. Her kaldıraç/yüzde iddiasını betikle tekrar hesapla (30:1'de %3 = sermayenin %93'ü, %100 değil).

## Dersler
- 2026-10-27 (F2 ön doğrulama, 11 senaryo): Fed History essay'leri FRH sayfaları hızlı ve güvenilir birincil kaynak. WebFetch'e "verbatim quote" istemi çoğu iddiayı tek çağrıda çözdü. Paralel 5 fetch iyi çalıştı.
- 2026-10-27: Tek kaynaklı "aykırı" rakam (ABA "%69 of world silver") hook'a girmişti. Yaygın tahmin ~1/3. Hook'taki her rakam için en az 2 bağımsız kaynak ara, aykırıysa sayısız yeniden yazım öner.
- 2026-10-27: "X yıl sonra toparlandı" (1929→1954, Nikkei 34 yıl, Cisco 25 yıl) iddialarının hepsi nominal fiyat endeksi. Metinde "price" kelimesi veya ekranda not şart, yoksa yanıltıcı oluyor.
- 2026-10-27: Bilgi kesimimden (Haziran 2026) sonraki güncel rakamlar (TÜFE, Fed, Brent, altın, JGB) mutlaka aranmalı. Fed ve BLS doğrulandı. Brent 16 Ekim (109,86 $) ve altın rekoru (5.318 $) ikincil kaynakta kaldı ve aramayla çelişti.
- 2026-10-27: Japan Times ücretli duvarda (402). Bloomberg/Reuters aktarımı + resmi veri (Nikkei Inc., FRED) kullan.
