# Viralite modeli v0

Amaç: senaryoları üretmeden önce viral olma potansiyeline göre sıralamak.
**Durum:** ağırlıklar başlangıç varsayımıdır (tahmin). Rakip outlier verisi (`rakip-analizi.md`) ve kendi videolarımızın
YouTube Studio verisi (CTR, ortalama izlenme süresi, ilk 30 sn tutma) geldikçe kalibre edilir.

## Temel ölçü: outlier skoru (kanıt için)
`outlier = video izlenmesi / kanalın son 20–30 videosunun medyan izlenmesi`. ≥3 güçlü, ≥10 istisnai.
Bir senaryonun konusu/açısı rakiplerde yüksek outlier üretmişse bu kanıt olarak puana yansır.

## Ölçütler (1–10)
| # | Ölçüt | Ağırlık | Soru |
|---|---|---|---|
| 1 | Merak boşluğu | 0.20 | Başlık + thumbnail "ne oldu / ne olacak?" dedirtiyor mu? |
| 2 | Kanıtlı talep | 0.15 | Konu/açı rakiplerde outlier üretti mi, aramada ilgi var mı? |
| 3 | Hook gücü | 0.15 | İlk 15 sn net vaat + gerilim var mı? |
| 4 | Kişisel bağ | 0.15 | İzleyicinin cebine/hayatına dokunuyor mu (TR izleyici)? |
| 5 | Zamanlama | 0.10 | Şu an konuşuluyor mu / tarihsel yıldönümü var mı? |
| 6 | Hikâye gerilimi | 0.10 | Kahraman, kötü adam, dönüm noktası var mı? |
| 7 | Görselleştirilebilirlik | 0.10 | Animasyonla güçlü anlatılabilir mi (metafor, grafik)? |
| 8 | Raf ömrü | 0.05 | 1 yıl sonra da izlenir mi? |

Toplam = Σ puan × ağırlık (max 10). Eleme: 10 → (toplam) ilk 5 → finans doğrulama riski olanlar çıkar → ilk 3 → hakem.
Ceza: rakip videoya fazla benzeyen açı −1.5; doğrulanamayan ana iddia → elenir.
