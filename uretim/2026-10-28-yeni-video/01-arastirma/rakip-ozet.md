# F1 rakip özeti (DELTA): son 30 günde B (güncel haber) ve C (gelecek senaryosu) outlier'ları

Hazırlayan: kanal-analisti · **Ölçüm tarihi: 2026-10-28**, pencere 2026-09-28 → 2026-10-28 [API]. İLERLEME: tamam.
Taban: `uretim/2026-10-26-1929-1000-dolar/01-arastirma/rakip-ozet.md` (12 aylık A sütunu analizi) ve `docs/rakip-analizi.md` (v1, 2026-10-26). Burada yalnız fark var.
Ham veri: `uretim/2026-10-28-yeni-video/01-arastirma/olcum/delta-veri-2026-10-28.json` (sha256 ba4f87c23718). Betikler: `olcum/delta30.py`, `olcum/desen30.py`.

**Özet (karar için 5 satır) [API][H]:**
1. Son 30 günün en güçlü B kümesi **enerji/dizel/petrol krizi**: 3 kanalda 9 video ≥3x. Çoğu Fred - Money Historian'ın (bir maskot kanalı) [API][H].
2. İkinci küme **Fransa'nın borç/faiz krizi**: 3 kanalda 10–11x (Econoclasts, Chill Financial Historian, Market Maker) [API][H].
3. C sütununun tek büyük outlier'ı **"What Happens If Trump Loses The Midterms?"** (3,53 M izlenme, 35,9x). Tek örnek, yani zayıf kanıt [API][H].
4. "AI bubble" doymuş: nişte 61 video, medyan skor 1,00, ≥2x oranı %11 (geri kalan videolarda %21) [H]. Tek başına açı değil.
5. Süre: 30–60 dk bandı biraz önde (medyan skor 1,17). 10–15 dk bandı nötr (1,01) [H]. Bizim 10–14 dk hedefimiz cezalı görünmüyor.

## 0. Kaynak, yöntem, etiketler
- **Etiketler:** [API] Data API v3, 2026-10-28 · [H] API sayılarından hesap · [ALT] yt-dlp otomatik altyazı, 2026-10-28 · [GÖZ] i.ytimg.com mqdefault thumbnail incelemesi, 2026-10-28 · [T] tahmin.
- **Örneklem [API]:** önceki 51 kanal + 8 hedefli `search` sorgusu (son 30 gün, uzun video, izlenmeye göre; 8×100 = 800 birim). Toplam 134 kanal; 104'ü son 30 günde aktif ve ≥5 taban videosu var; 1.768 video. **Niş alt kümesi:** 28 İngilizce anlatımlı finans/ekonomi kanalı, 393 video (≥3 günlük). Podcast/klip, Hintçe/Kannada ve konu dışı kanallar çıkarıldı (liste `olcum/desen30.py` içinde) [API][H].
- **Skor [H]:** izlenme ÷ kanalın 2026-10-21 öncesi son 20 uzun (≥4 dk) videosunun medyanı. Videolar 3–30 günlük; yaşlılar avantajlı. Sütun etiketi başlıktan regex'le atanıyor (`desen30.py`), kaba bir sınıflama.
- **Erişim engeli (2026-10-28):** yt-dlp altyazı ilk istekten itibaren "Sign in to confirm you're not a bot" + 429 verdi, 5 videodan 1'i indi [ALT]. Hook analizi bu yüzden n=1 ve **zayıf kanıt**. Data API `search` 8 sorguda takılmadı [API].

## 1. Son 30 günün B/C outlier'ları (niş, ≥3x ve ≥20 bin izlenme) [API][H]

| Sütun | Video (id) | Kanal (abone) | Süre | Yaş | İzlenme | Kanal medyanı | Skor |
|---|---|---|---|---|---|---|---|
| C | What Happens If Trump Loses The Midterms? (AyMHJBLc_tA) | Finance Bureau (130 B) | 19,1 dk | 11 g | 3.529.205 | 98.350 | 35,9x |
| C | Why The U.S. Diesel Crisis Is Only Getting Started (RwZrPUh924M) | Fred - Money Historian (13 B) | 41,4 dk | 13 g | 59.172 | 2.303 | 25,7x |
| B | October Diesel Supply Crisis Deepens (3i9pmZuLvPo) | Fred - Money Historian | 40,9 dk | 8 g | 56.978 | 2.303 | 24,7x |
| B | $100 Oil, Record Debt: What's Really Happening to Saudi Arabia's Money (c_nSo7Rl74A) | Fred - Money Historian | 40,2 dk | 11 g | 43.896 | 2.303 | 19,1x |
| B | France cannot save itself (TgW81-Yi4F8) | Econoclasts (70 B) | 22,3 dk | 11 g | 471.097 | 41.254 | 11,4x |
| B | Why France's Economy is Facing a Massive Shift (jyqvmguz1go) | Chill Financial Historian (137 B) | 43,3 dk | 9 g | 74.898 | 7.438 | 10,1x |
| C | Canada's $44 Billion Oil Shift Could Cost America Billions (IWOaTrkOXVU) | America Prime (3 B) | 24,0 dk | 8 g | 26.523 | 3.233 | 8,2x |
| B | America Is Entering a Second Great Depression And Nobody Is Ready (xRrVFXNE-Tk) | Finance Economist (92 B) | 46,7 dk | 16 g | 35.743 | 5.532 | 6,5x |
| B | The (Overdue) Collapse Of The AI Bubble (XEMvG2vulKg) | Damon Cassidy (339 B) | 23,6 dk | 21 g | 2.186.511 | 373.873 | 5,9x |
| B | Global Panic Spreads (_HtlkHuC2RQ) | Joe Blogs (485 B) | 22,6 dk | 12 g | 330.157 | 79.228 | 4,2x |
| C | Diesel Prices Are Out of Control SOMETHING BIG IS COMING (B2tqxDBCXi0) | Finance Economist | 46,0 dk | 21 g | 21.959 | 5.532 | 4,0x |
| B | Gas Stations Just Sent a TERRIFYING Warning About the Economy (oGsOAQORT1E) | Eurodollar University (235 B) | 21,9 dk | 9 g | 500.259 | 139.586 | 3,6x |

Bölgesel küme, bizim için dışarıda [API]: Jack McAllister (6 B), Kanada otomotiv/Çin arabaları, 45,8x ve 11,7x. Niş dışı ama ölçülen: Market Maker Podcast "Is France About to Fail?" 11,2x [API].
Büyük kanalların son 30 günü sakin [API]: How Money Works, Economics Explained, Moon ve Patrick Boyle'un bu pencerede ≥3x videosu yok.

## 2. Delta desenleri (her biri ≥2 örnekli; tek örnekli "zayıf kanıt")

**D1. Somut kriz + "henüz bitmedi" çerçevesi (B→C köprüsü).** Örnekler: "Only Getting Started" 25,7x · "Crisis Deepens" 24,7x · "SOMETHING BIG IS COMING" 4,0x · "Facing a Massive Shift" 10,1x [API][H]. Haber geçmiş zamanda anlatılmıyor; başlık **gidişatı** satıyor. Kalıp kategorisi olarak "Collapse/Crisis/Bubble/Crash" n=76, medyan 1,21. Geri kalan 317 videonun medyanı 0,98 [H]. Etki küçük ama pozitif.

**D2. Ülke/kurum öznesi + kesin hüküm.** Örnekler: "France cannot save itself" 11,4x · "Saudi Arabia's Money" 19,1x · "Russia Stops Paying" 3,5x [API][H]. Ülke öznesi tek başına etkisiz: n=135, medyan 0,98 [H]. İşi gören **hüküm cümlesi**, ülke adı değil.

**D3. "What Happens If <yakın tarihli olay>" (C).** Tek örnek, 35,9x: zayıf kanıt [API][H]. Nişte bu kalıpla son 30 günde 1 video var, yani arz boş. 12 aylık veride de aynı video 34x olarak görünüyordu (önceki rapor §1) [API].

**D4. "Here's Why / What Happened" eki.** n=4, medyan 5,71, 3'ü ≥2x [H]. Küçük n, kanıt orta. "Nobody/No One" n=9, medyan 0,80 [H]: aşınmış, kullanma.

**D5. Thumbnail [GÖZ] (6 outlier incelendi).** 3 tip öne çıkıyor:
- (a) Tek büyük yüz + yanan sembol, metin yok: Trump/ABD haritası, AyMHJBLc_tA.
- (b) Maskot + tek obje + 1–2 kelimelik büyük metin: "2 WEEKS." (RwZrPUh924M) ve "SAUDI IS OVER?" (c_nSo7Rl74A) [GÖZ].
- (c) İllüstrasyon metaforu + 3–4 kelime: terazi, "WHERE FRANCE'S MONEY GOES" (jyqvmguz1go). Ayrıca logolar + "THEY'RE DONE" (XEMvG2vulKg) [GÖZ].
Metin ≤4 kelime: 5/6 [GÖZ].

**D6. Hook [ALT], n=1, zayıf kanıt.** jyqvmguz1go 0–30 sn: tarih + kişi + mikrofon sahnesi ("On Monday the 21st of September, 2026, France's Economy Minister…"). Ardından tek şok sayı (2027'de 91 milyar € faiz). Hemen karşılaştırma geliyor: eğitim 63 milyar, savunma 53 milyar. Sonra yeniden çerçeve: "That's not paying the debt back. That's just the interest." Diğer 4 videonun hook'u: YAPILAMADI (bot kontrolü).

## 3. Önemli uyarı: maskotlu doğrudan rakip
**Fred - Money Historian** (13 B abone) çizgi maskotla anlatıyor: silindir şapkalı, takım elbiseli adam [GÖZ]. Kanal 12 aylık veride tarih anlatıyordu ("2008 Crisis Explained Like You're 5", 4,9x) [API]. Son 30 günde enerji/dizel haberine geçti ve 14 videonun 11'i ≥2x oldu [API][H]. **Skor şişkin:** taban medyan (2.303) eski tarih videolarından geliyor, yani skorun bir kısmı pivot etkisi [H]. Süreleri 38–41 dk [API].
- Kopyalamama: Leo'nun silüeti, renkleri ve aksesuarı Fred'in maskotundan ayrışmalı (şapka/takım yok) [GÖZ]. Thumbnail'de "maskot + tek obje + 1–2 kelime" desenini kendi renk dilimizle kullanırız. Kıyas için thumbnail-tasarimcisi'ne `i.ytimg.com/vi/RwZrPUh924M/mqdefault.jpg` örneği verilsin.

## 4. Senaryo / paket için delta önerileri (karar senaryo-yazari, viralite ve hakemde)
- **B adayı:** enerji/dizel/petrol krizi ya da Fransa'nın faiz yükü. Talep kanıtlı (≥3 kanalda outlier) [API][H]. Ama arz da hızla doluyor: Fred, Finance Economist ve America Prime haftada çok video çıkarıyor [API]. Bizim açımız: rakiplerin 40 dk'lık monoloğu yerine 10–14 dk'lık sinematik açıklama. Fred'in yanından geçerken açıyı da farklı tutmalıyız [T].
- **C adayı:** "What Happens If <takvimdeki somut olay>" (seçim, faiz kararı, borç tavanı). Kanıt zayıf (n=1) ama arz boş [API][H]. Yatırım tavsiyesi olmadan "senaryo" çerçevesiyle anlatılmalı.
- **Başlık:** somut özne + gidişat fiili ("is only getting started", "cannot…") ya da "What happens if…". "Nobody is ready / No one is talking about" kullanılmasın (medyan 0,80) [H]. "AI bubble" tek başına kullanılmasın (%11 ≥2x) [H].
- **Hook:** tarih + kişi + tek şok sayı + iki tanıdık kalemle kıyas + "bu bile değil" yeniden çerçevesi, ilk 20 sn içinde (n=1, zayıf kanıt) [ALT].

## 5. Kendi kanal
BVJwZ1C9R1U henüz yayında değil (planlı yayın 2026-10-28 16:00 UTC). Dokunulmadı, ölçülmedi. 48 saat raporu 2026-10-30 16:00 UTC'den sonra [T: takvim].

## 6. YPP ilerlemesi
Ölçülecek herkese açık uzun video yok. Abone ve 12 aylık saat bir sonraki raporda [API: kanal durumu önceki raporda 0 herkese açık video].

## 7. Test
- `python3 etiket_test.py rakip-ozet.md` → rakamlı satırların etiketli olduğunu ve ölçüm tarihinin başlıkta yazdığını sayar.
- Google API anahtarı önekiyle `grep -c` (olcum/*.json, olcum/*.py) → 0 (anahtar sızıntısı yok).
