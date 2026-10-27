# F4 ses — anlatım raporu (ses-yonetmeni, 2026-10-27)

Etiketler: **[ölçüm]** bu çalışmada ölçüldü · **[tahmin]** yorum veya çıkarım.
Ses: Kokoro-82M `am_fenrir`, hız 0.9, cümle cümle (`tools/ses/tts.py`, duraklamalar: cümle 0.30 / soru 0.40 / sahne sonu 0.65 sn) → `tools/ses/tts-son.sh`. Lisans Apache-2.0 (karar ve aday tablosu `uretim/ses-testi/tts/rapor.md`).

## 1. Sonuç ve kapılar [ölçüm]
| Kapı | Ölçüm | Hedef | Sonuç |
|---|---|---|---|
| WER (Whisper small.en, `hata-orani.py`, tüm dosya) | **%2.5** (45/1789) | ≤ %10 | GEÇTİ |
| WER sahne başına toplam (`olc.py`, sahne sınırında kelime kayması dahil) | %4.6 (82/1789) | ≤ %10 | GEÇTİ |
| Kanal adı | Anlatımda "Toonomy" **geçmiyor** (kilitli metin; tanıtım kuralı). Ayrıca test edildi, §2 | doğru | GEÇTİ (bkz. not) |
| "Leo" | her geçişte iki heceli lˈiO; Whisper "Leo" yazıyor ("Stock Leo" bazen "Stockleo" diye bitişik — normalizasyon artığı) | doğru | GEÇTİ |
| Ses yüksekliği `anlatim.wav` | **−14.2 LUFS**, true peak **−1.5 dBTP**, LRA 2.0 | −14 ±1, ≤ −1 | GEÇTİ |
| `anlatim.m4a` (AAC 192k) | −14.2 LUFS, TP −1.3 dBTP | aynı | GEÇTİ |
| Biçim | 48 kHz mono 24-bit WAV, **631.6 sn (10:31.6)** | 48 kHz mono | GEÇTİ |
| Uzun metin tutarlılığı (dakika dakika perde / değişkenlik / parlaklık) | 151–154 Hz, 4.3–4.9 yarım ton, 1976–2054 Hz (dk 0–9); son 31 sn 142 Hz (kapanış tonlaması) | kayma yok | GEÇTİ |
| Shorts ek kayıtları | `shorts-1-ek.wav` 9.5 sn WER %0 · `shorts-2-ek.wav` 6.5 sn WER %0; −14.2 / −14.1 LUFS, TP −1.5 | ≤ %10 | GEÇTİ |

## 2. Telaffuz adayları ve eleme (kısa test, am_fenrir 0.9, cümle tek başına Whisper) [ölçüm]
Dosyalar: `telaffuz-testi/varyant-1.txt`, `varyant-2.txt`; ölçüm aracı `cumle-whisper.py` (her cümleyi ayrı çözer → bağlam etkisi yok).

| Kelime | Aday A | Aday B | Aday C | Kazanan |
|---|---|---|---|---|
| FDIC | "FDIC" (misaki harf harf: ɛf-di-aɪ-si) → FDIC 1.00 / FDIC's 0.98 | "F D I C" → 0.99 / 0.98 | "F-D-I-C" → 1.00 / 0.98 | **A** (metin aynen; fark yok) |
| U.S. | "US" → U.S. 0.63/1.00 | `[U.S.](/jˌuˈɛs/)` → aynı | "U.S." düz | **B** — düz yazım `tts.py`'de "U.S. " sonrası cümleyi bölüp cümle ortasına 0.3 sn sessizlik koyuyordu; B hem okunuşu hem bütünlüğü koruyor |
| Roosevelt | düz (espeak: ɹˈOzəvˌɛlt) → 1.00 | `[Roosevelt](/ɹˈOzəvˌɛlt/)` → 1.00 | — | **A** |
| Toonomy | düz (espeak: tˈunəmi = "TOO-nuh-mee", kanal-adi.md ile aynı) → Whisper "Toonami" 0.63 | `/tˈunəmi/` → "Toonami" 0.64 | `/tunˈɑmi/` → "Toonami" 0.71 | **A** (okunuş doğru; Whisper bilinen "Toonami" kelimesine kayıyor — ses hatası değil, ASR sözlük yanlılığı) |
| Dow, yıllar, ondalıklar | "the Dow" 0.76–0.86; "381.17", "41.22", "3.7 %", "1929", "2025" hepsi doğru | — | — | metin aynen |

v1 tam üretimdeki 4 gerçek telaffuz hatası (cümle tek başına da tekrarlandı) → 2 aday, kazanan `okuma-hazirla.py` TELAFFUZ listesine yazıldı, tam anlatım yeniden üretildi (v2):

| Cümle | v1 Whisper | Aday 1 (`+2` vurgu) | Aday 2 (fonetik) | Kazanan → v2 sonucu |
|---|---|---|---|---|
| S02 "nobody in **this** studio" | "the" (0.79) | this 0.98 | `/ðˈɪs/` this 0.98 | fonetik → this 0.98 |
| S04 "**And** Box Leo takes…" | "Inbox Leo" | And 0.65 / box 0.52 | `/ˈænd/` And 0.61 / box 0.62 | fonetik → And 0.66 / box 0.48 |
| S08 "Bank Leo **is** fine" | "Banklia was" | Leo 0.57 is 0.97 | `/ˈɪz/` Leo 0.55 is 0.98 (`[Leo](/lˈiˌO/)` elendi: "Banklio") | `/ˈɪz/` → Bank Leo is 0.97 |
| S23 "the door that **looked** smart" | "looks" (0.60) | "looks" 0.55 (elendi) | `/lˈʊktʰ/` looked 0.95 | fonetik → looked 0.86 |
Hepsi yalnız telaffuz işareti; görünen kelime ve anlam aynı (kilitli metin değişmedi; `referans-metni.txt` = kilitli metin).

## 3. Kalan farklar (v2, `wer-cikti.txt`) — sınıflandırma [ölçüm + yorum]
- **Normalizasyon artığı (ses doğru):** sıra sayıları (third→"3rd", eighth→"8th", eleventh, fourth, first), Whisper'ın "$1,000" / "$500" yazması (fazladan "one"/"dollars"), "thirteen and a half"→"13.5", "twelve hundred seventy"→"1,270", "thirties"→"30s", "Stock Leo"→"Stockleo". Bunlar 45 düzenleme hatasının 41’i (geri kalan 4: aşağıdaki 2 uydurma + 2 bağlam yanlılığı).
- **Whisper uydurması (sessizlikte):** 9:07.9 "Yes." (p 0.12) ve 10:00.3 "up." (p 0.22) — cümleyi takip eden sessizlikle birlikte tek başına çözünce yok.
- **Bağlam yanlılığı (yalnız tam dosya çözümünde):** S08 "is"→"was", S13 "looks"→"looked"; tek başına çözünce doğru (0.97 / 0.90).
- **Hafif:** S23 "laughed at came" tek başına "laughed, it came" (bağlamda doğru). Yeniden üretim gerekmedi.
- Yeniden üretilebilir içerik hatası: **0**.

## 4. Süre: gerçek vs tahmin [ölçüm]
- **Gerçek 10:31.6 (631.6 sn), tahmin 11:54 (714 sn) → −82 sn (−%11.5).** Ortalama 161.6 kelime/dk (duraklamalar dahil); metin 143 kpm varsaydı (pilotta paragraf duraklaması oranı daha yüksekti). Sahne başına konuşma hızı 141–189 kpm.
- **Risk:** kanal kuralı ≥10 dk; anlatım 10:31 ile geçiyor ama pay 31 sn [ölçüm]. Kurgu sahne geçişlerine/ilk karta görsel nefes eklerse uzar; daha fazla pay gerekirse ses değişmeden duraklama artırılabilir: `--cumle 0.40 --paragraf 0.9` ≈ +23 sn (168 cümle × 0.1 + 23 sahne × 0.25) [tahmin, hesap]. Hız 0.9 Niyazi kararı, değiştirilmedi.
- Sahne tablosu (başlangıç/bitiş, tahmin farkı, kpm, sahne WER): `olc-cikti.txt`; makine okunur: `sahne-zamanlari.json`.

### YouTube bölümleri (gerçek ses; montajda baş boşluk eklenirse kaydırılır)
```
0:00 The game: $1,000 and three doors
1:19 Door 1: The stock market
2:46 Door 2: The bank
4:46 Door 3: The shoebox
6:12 The bottom: July 1932
7:33 March 1933: every door locked
8:42 The twist: the same door in 2026
9:52 What the game really tests
```
### Yeniden kancalar (cümle başı zamanı)
Hook 0:00 · ↺1 0:28 · ↺2 1:14 · ↺3 1:54 · ↺4 2:44 · ↺5 3:33 · ↺6 3:52 · ↺7 4:44 · ↺8 5:38 · ↺9 6:07 · ↺10 6:37 · ↺11 7:31 · ↺12 8:40 · ↺13 9:53 · köprü 10:18. **En uzun aralık 73 sn** (↺12→↺13; kapı ≤90 GEÇTİ). Abone cümlesi (S11) 4:29, ilk büyük ödülden (S10 bitiş 4:29.35) sonra ✓.

## 5. Shorts
Ana anlatımda birebir olmayan cümleler (`okuma-hazirla.py` otomatik buldu) ayrı üretildi:
- `shorts-1-ek.wav` (9.5 sn): hook "In nineteen twenty-nine, the smartest-looking door was the worst one." **0.00–3.81** · kapanış "The brown door won… full video." **4.46–9.48** (zamanlar `shorts-1-ek-ham.zaman.json`).
- `shorts-2-ek.wav` (6.5 sn): hook iki cümle **0.00–3.04** + **3.34–6.52**.
- Diğer cümleler ana anlatımdan kesilir (cümle başları `anlatim-ham.zaman.json`). Tahmini konuşma süresi (cümleler + 0.3 sn aralık): **Shorts 1 ≈ 48.4 sn, Shorts 2 ≈ 53.4 sn** (≤60 ✓) [ölçüm, cümle süreleri toplamı].
- Not (kurgu-editoru): Shorts 1 hook'u 3.8 sn, Shorts 2 hook'u 6.5 sn (iki cümle) — "ilk 2 sn" testinde ilk 2 sn = "In nineteen twenty-nine, the smartest…" / "A shoebox of cash gained power…".

## 6. Dosyalar
| Dosya | Git | İçerik |
|---|---|---|
| `okuma-metni.txt` | ✓ | Kokoro'ya verilen metin, sahne başına 1 satır (S01…S24 sırası; eşleme `sahne-esleme.json`) |
| `referans-metni.txt` | ✓ | WER referansı = kilitli metin |
| `sahne-esleme.json` | ✓ | sahne → cümle aralığı + kelime |
| `sahne-zamanlari.json` | ✓ | sahne → bas/bitis (kesme noktası) + konusma_bitis, sn |
| `anlatim-ham.zaman.json` | ✓ | 192 cümlenin başlangıç/bitişi (anlatim.wav ile aynı zaman ekseni: tts-son.sh zamanı kaydırmaz) |
| `kelimeler.json` | ✓ | Whisper small.en kelime zamanları (1613 kelime, ort. güven 0.957; sayılar rakamla yazılı, ör. "1929") |
| `anlatim.wav` | ✗ (`*.wav` git dışı) | yayın seviyesi anlatım |
| `anlatim.m4a` | ✓ | AAC 192k kopya (15 MB); wav bundan yeniden üretilebilir ya da `okuma-hazirla.py` + `tts.py` + `tts-son.sh` ile birebir (Kokoro deterministik) |
| `shorts-{1,2}-ek.{wav,m4a,txt}`, `shorts-*-ham.zaman.json` | m4a/txt/json ✓ | Shorts ek kayıtları |
| `olc.py`, `olc-cikti.txt`, `wer-cikti.txt`, `whisper.txt` | ✓ | ölçüm aracı ve çıktıları |
| `okuma-hazirla.py`, `cumle-whisper.py`, `telaffuz-testi/` | ✓ | hazırlık + telaffuz testi |

Yeniden üretim (04-ses içinde):
```
python3 -I okuma-hazirla.py
~/.finansal-arac/kokoro-venv/bin/python ../../../tools/ses/tts.py okuma-metni.txt anlatim-ham.wav --ses am_fenrir --hiz 0.9   # ≈4 dk, 4 çekirdek
bash ../../../tools/ses/tts-son.sh anlatim-ham.wav anlatim.wav anlatim.m4a
~/.finansal-arac/venv/bin/python ../../../tools/ses/yaziya-dok.py anlatim.wav kelimeler.json small.en                       # ≈2.5 dk
python3 ../../../tools/ses/hata-orani.py referans-metni.txt kelimeler.json && python3 -I olc.py
```

## 7. Sonraki ajanlara notlar
- **ses-muhendisi:** `kelimeler.json` hazır (Whisper small.en). Altyazıda Whisper'ın rakam yazımı ("1929", "$1,000") ve 9:07.9 "Yes." / 10:00.3 "up." uydurmaları **silinmeli** (sesde yok). Rhubarb için düz metin: `referans-metni.txt`.
- **kurgu-editoru / youtube-paketleyici:** bölüm zamanları §4 (montajda ses önüne boşluk eklenirse aynı miktar kaydır). Video uzunluğu payı 31 sn.
- **uretim-muhendisi (öneri):** `hata-orani.py` sıra sayılarını (third/3rd) ve "$1,000"→"one thousand dollars" farkını hâlâ hata sayıyor (45 hatanın 41’i); normalizasyona eklenirse WER gerçek değere iner. `cumle-whisper.py` (cümle tek başına çözüm) `tools/ses/`'e alınabilir.
