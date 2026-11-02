# F4 görsel kol — rapor · S08 Kitchen Table Budget
**İLERLEME:** biten = prompt paketi dalga 1–2 (G01–G10) + denetim GEÇTİ · sıradaki = koordinatör dalga 1'i (G01–G05) üretir → ben ölçer, mutfak kazananını seçerim (erken karar satırı aşağıda) → dalga 2 · yarım = yok · büyük medya yok.
**Karar:** metinden bağımsız temel varlıklar planlandı; çekirdek 8 + seçmeli 2 üretim, tavan 12 (tekrar payı 2). Leo masada = mevcut rig + masa plakası (yeni oturan taban yok).
**Kapı:** `python3 -I araclar/prompt-kontrol.py canva-promptlari.md` → 10/10 GEÇTİ (çıktı `araclar/prompt-kontrol-cikti.txt`; girdi sha256 47c654a91b14); negatif kontrol (saat sağ bilek, "NOT painterly" silme, banknot yasağı silme, prompt'a "$7,400") → KALDI (exit 1); 2 koşu aynı (çıktı sha256 ce67eaf65211).
**Erken karar satırı (mutfak kazananı G01|G02):** — (dalga 1 dönünce yazılır)

## Plan
| Id | Varlık | Tür | Dalga | Kritik yol |
|---|---|---|---|---|
| G01 / G02 | Mutfak masası orta plan, 2 aday (C01 stil ref / referanssız) | plaka | 1 | evet (H4) |
| G03 | Zarf nesne sayfası (kapalı, açık, yığın, kâğıt) | nesne | 1 | evet (matruşka) |
| G04 / G05 | Leo zarfı açar / zarftan zarf çıkarır (kafa sabit, rig uyumlu) | Leo düzenleme | 1 | evet |
| G06 | Kuşbakışı fatura masası | plaka | 2 | — |
| G07 | Kumbara, kasa, boş kredi kartı, hesap makinesi, işaretsiz para | nesne | 2 | — |
| G08 | Leo hesap makinesi | Leo düzenleme | 2 | — |
| G09 / G10 | Dikey mutfak (Shorts) / buzdolabı boş notlar | plaka seçmeli | 2 | — |

## Yeniden kullanım ve özgünlük
- Yeniden kullanılan yalnız karakter varlıkları (muaf sınıf): paket-v1 a/b, 1929 `rig/` yamaları, 1929 `leo/` jest kesikleri (c, d, e, f, C02, C04, C12, C13, C20, C21). Önceki videodan yeniden kullanılan **sahne görseli: 0**; tüm plakalar bu videoya özgü.
- Rakip ayrışması: Fred - Money Historian maskotu silindir şapka + takım elbise; Leo'da şapka/ceket/kravat yok (kabul listesinde), mekân ev mutfağı.
- Politika (P1): plakalarda bayrak, banknot, parti rengi, yüz yok; rakam/etiket yalnız KOD.

## Değerlendirme yöntemi (dalga dönünce)
Leo'lu: `tools/gorsel/tutarlilik.py` (taban a; kafa kor. ≥0,84) + `araclar/rig-yama.py` kafa bölgesi hizası + 4× yüz incelemesi · plaka/nesne: `araclar/stil-olcum.py` (düzlük ≥%50, doku ≤2,0 hedef), 2× kırpımda yazı taraması (Canny levha yoğunluğu) · kesme: `araclar/kes-m4.py` (saçak + kapalı delik listesi) · kontakt sayfası (sayfa + a + yeni + Leo bindirme).
