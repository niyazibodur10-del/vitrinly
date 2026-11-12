# Bölüm 002 — fiyat doğrulaması (finans-dogrulayici, 2026-11-12)

İLERLEME: tamam.
**KARAR: GEÇTİ.** N5–N7 gerçekçi; BANK zinciri 100 → 40 → 24 doğru, eksi yok. Metinde değişiklik gerekmez. Tek koşul: §7'deki etiketler aşağıdaki gibi güncellenir.
- Girdi: `bolum-002/metin.md` sha256 9c4435c57b0b · `bolum.txt` replikleri (sixty, eight, sixteen, hundred and forty, seventy-six, sixty-four, ninety, fourteen, hundred and fifteen) → hepsi tabloda, `[RAKAM?]` kalmadı.
- Hesap: `python3 -c` → maliyet 60+16=76; net 140→64, 90→14, 115→39, 100→24, 120–140→44–64; BANK 24+satış = 114 / 124 / 144–164. Hepsi §4.5 (net ≤ maliyet 76) içinde.
- Etiketler: [K] sayfası okundu · [AÖ] arama özeti, ≥2 kaynak · [T] tahmin/hesap.

## Rakam tablosu
| # | İddia | Değer | Kaynak | Durum | §7 etiketi |
|---|---|---|---|---|---|
| N1–N2 | BANK $100, alış $60 → $40 | | B001 dogrulama D1-A; fiyat-referans | doğru | doğru |
| N3 | İç lastik $8 × 2 = $16 → BANK $24 | $8/adet | [AÖ] favoritebikes, leoguarbikes: $5–12/adet | doğru | [AÖ] |
| N4 | Maliyet $76 | | aritmetik | doğru | doğru |
| N5 | İlan $140 (istenen fiyat), kâr $64 "If she sells" | ilan | [K] underpriced: ucuz bisiklet "$50–100 profits" → $76 maliyetle satış $126–176. [AÖ] BikeForums/Craigslist eski çelik yol bisikleti istenen fiyatları $150–600, bir kısmı haftalarca satılmıyor; satılmış kayıt bulunamadı | doğru (ilan fiyatı olarak) | [AÖ] ilan fiyatı; satış değil |
| N6 | Teklif $90, kâr $14 | ilanın %64'ü | Marketplace'te düşük teklif anlatısı yaygın [T] | gerçekçi | [T] |
| N7 | Karşı teklif $115, kâr $39 | ortalama | [T] | gerçekçi | [T] |
| Z1 | Zarf COUNTER → $100 satış, BANK $124 | | [T] | tutarlı | [T] |
| Z2 | Zarf TAKE → BANK $114 | | aritmetik | doğru | doğru |
| Z3 | Zarf HOLD → 1–3 hafta, $120–140, BANK $144–164 | | [K] underpriced: satış 7–21 gün; fiyat [T] | tutarlı | süre [K], fiyat [T] |

## Risk taraması
- Tavsiye dili 0; "Trust the vibe" karakter repliği, Jake hemen sorguluyor → YEŞİL.
- Zarf TAKE "gündüz, kalabalık yer, nakit" rutin olarak gösteriliyor → YEŞİL. Bölüm 1 notu hâlâ açık: satış/alışta seri numarası (çalıntı kontrolü) rutin olarak bir kez gösterilebilir (isteğe bağlı).
- Kâr ifadesi: "sixty-four profit" brüt (zaman/yağ hariç); Jake "If she sells" dediği için vaat değil → YEŞİL.
- Zincir yağı masrafsız ("evdeki yağ") kabul; yazılırsa BANK $24'ten düşülmeli.

## Kaynaklar
underpriced.app/blog/bicycles-flipping-guide [K] · m.bikeforums.net/showthread.php?p=23217920 · bikeforums.net/classic-vintage/1291768 (Part 3 ilanları) · favoritebikes.com (lastik maliyeti) · leoguarbikes.com/blogs/news/how-to-replace-bicycle-tire-2025
