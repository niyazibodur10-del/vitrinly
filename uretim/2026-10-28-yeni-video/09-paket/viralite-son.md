# F8 son viralite puanı · S08 "If America Earned $5,400 a Month, Here's Its Budget" · 2026-11-02 · model v0.1

İLERLEME: tamam. Yeniden üretim: `python3 tools/viralite.py uretim/2026-10-28-yeni-video/09-paket/viralite-son-girdi.json` (girdi d2b82e1413a9, betik 4b71c5ada1a7).
**Son puan: 7.25 [T]** (aralık 7.15–7.40); F2 puanıyla aynı (7.25). Bitmiş ürün F2 tahminlerini doğruladı; artış ya da düşüş yok.
**Thumbnail:** A1 7.25 = C1 7.25 > B1 7.05. Fark 0.20, yani 0.3'ün altında: model ayıramıyor. Sıra Test & Compare'e kalır, varsayılan **A1** (başlık, thumbnail ve ilk 15 sn aynı vaadi veriyor). thumbnail-tasarimcisi'nin A1 → C1 → B1 sırası korunur.
**Kapılar:** ağırlık toplamı 1.00 ✓ (`--dokuman` tutarlı) · betik ve ağırlıklar değişmedi, 1 koşu (protokol: "2 koşu aynı" yalnız betik değişince).
**F8b kuralı:** başlık, thumbnail ve ilk 15 sn değişmezse yeniden hesap yok, "F8a ile aynı" yazılır. Girdi sha256: video `07-animasyon/tam-16x9.mp4` 380b3ba073b0 · A1 f8148925a6df · C1 ad63f8d5b1f8 · B1 a5fc459fa14a · `yayin-paketi.json` 5e323f769f36 (paket commit b172cbb).

## Ölçülen ürün özellikleri [Ö] → puan
| Ölçüt | F2 | F8 | Kanıt |
|---|---|---|---|
| Merak | 8 | 8 (B1 7) | Başlık T1 değişmedi ve somut özne var. A1'de şaşkın yüz + "−$2,000 EVERY MONTH" (2 kelime + sayı). C1 "INTEREST > MILITARY" ayrı bir boşluk açıyor, aynı güçte. B1'de yüz düşünceli ve sayı bağlamsız → 7 |
| Hook | 9 | 9 (köt. 8) | `kelimeler-hizali.json`: ilk 15 sn 43 kelime, **172 kpm** (rakip bandı 175–225'in hemen altında); ilk 30 sn 177 kpm (bantta). Vaat 0:13'te tamam ("see where the gap goes"), 15–30 sn köprüsü sonu vaat ediyor. Kareler: 0:00 Capitol → 0:03 zarf "$0 IN" → 0:07 buzdolabında "$5,400 IN" → 0:11 Leo masada; kelime kelime altyazı var |
| Kişisel | 7 | 7 (iyi. 8) | Köprüde "car loans and mortgages" bağı açıkça söyleniyor |
| Görsel | 9 | 9 | Mutfak ve zarf metaforu her karede; sıcak lamba, soğuk gece arka planı (stil kararına uygun) |
| Talep 6 · Zamanlama 6 · Hikâye 6 · Raf 8 | — | aynı | Talep: How Money Works 2,97x (F2 ölçümü, yeniden ölçülmedi). Yayın seçim ertesi; FY2026 rakamları sabit, bayatlama yok |

## Betik çıktısı
```
| 1 | S08-A1-iyi | A1, kişisel iyimser (köprüde araba kredisi/mortgage) | 7.40 | +0.00 | −0.00 | **7.40** | - |
| 2 | S08-A1 | T1 + A1 '-$2,000 EVERY MONTH' (varsayılan) | 7.25 | +0.00 | −0.00 | **7.25** | - |
| 3 | S08-C1 | T1 + C1 'INTEREST > MILITARY' | 7.25 | +0.00 | −0.00 | **7.25** | - |
| 4 | S08-A1-kot | A1, hook kötümser (ilk 15 sn 172 kpm < 175) | 7.15 | +0.00 | −0.00 | **7.15** | - |
| 5 | S08-B1 | T1 + B1 hesap makinesi '-2,000' | 7.05 | +0.00 | −0.00 | **7.05** | - |
$ python3 tools/viralite.py --dokuman docs/viralite-modeli.md → Doküman tutarlı: 8 ağırlık betikle aynı, toplam 1.00
```

## Kalibrasyon notu
Tahmin kaydı: S08 = 7.25 (A1). Yayından sonra kanal-analisti'nin 48 sa / 7 g raporundaki CTR (merak + thumbnail), AVD ve 30 sn tutma (hook) bu satırla karşılaştırılır. 1929 videosu ile birlikte n=2; ağırlık ayarı ≥10 videoda yapılır. `yt-analytics.readonly` kapsamı hâlâ gerekli. Başlık ve thumbnail ayrı, ardışık Test & Compare testlerinde ölçülmeli; aynı anda değiştirilirse kalibrasyon verisi karışır.
