# F5 iskelet — animasyon-yonetmeni (2026-11-04, akış 0b, metin v1.0)

İLERLEME: tamam (iskelet). Sıradaki: ses kolu GEÇTİ → `sahne-veri.py` ile gerçek zaman + Rhubarb → `ANLATIM_HAZIR = true` → KMirasKritik testi (senkron ≤2 kare, AgizTest, blackdetect).
**SONUÇ: GEÇTİ (iskelet)** — 31 sahne + 9:16 (5 dikey sahne + 2 tam Shorts) tek zaman kaynağından derleniyor; tsc 0 hata; 123/123 kesme karesi + 14 düzeltme + 16 dikey kare render edildi.
- Kod: `video/src/videolar/miras-sizintilari/` (önek **KMiras**; Root.tsx'e işaretten eklendi). Varlık klasörü `public/kmiras` (boş; anlatim.wav + plakalar buraya).
- Tek kaynak: `zaman.ts` (31 plan, kelime çapası; `yap()` kesme sırası + olay sınır denetimi). 243 görsel olay, 123 kesme, 40 ağız aralığı (234 sn).
- ABONE (tahmini): ABONE-1 S05 sonu k3646 (2:01,5) · ABONE-2 S17 sonu k15056 (8:21,9) · ABONE-3 S30 sonu k26702 (14:50,1). Sağ alt (x>1170, y 660–830) üç anda da boş (kare kanıtı `kareler/kontak-duzeltme.jpg`).
- Efekt cue: `06-muzik/animasyon-efekt-cue.json` (`tahmini: true` — muzik-ses-tasarimcisi ses gelince yeniden üretilmiş sürümü kullanır).
- Rakam: grafikler yalnız `veri-grafik.ts` (G, R-kodlu) — `grafik-veri.py` her değeri rakam-tablosu R satırında assert eder (28 değer, 22 kaynak satırı, kutu 10→6 kutu-hesap-cikti.txt ile eş).

## Kanıt (komut → sonuç; girdi sha256 ilk 12)
| Kapı | Sonuç |
|---|---|
| `python3 -I 07-animasyon/tahmini-veri.py` (metin.md) | 31 sahne, 904,1 sn tahmini (160 kpm + 0,35 sn cümle arası + ABONE nefesi); Shorts 43,9 / 41,4 sn |
| `python3 -I 07-animasyon/grafik-veri.py` | GEÇTİ 28 değer / 22 kaynak / kutu 6 |
| `node 07-animasyon/olay-cikar.mjs` (zaman.ts fb5fd76baaa5, veri-sahne 941a066c4830) | 243 olay, 3 abone, cue cb293e627430 |
| `cd video && npx tsc --noEmit -p .` | EXIT 0 |
| `node scripts/kare-ornek.mjs KMirasTam … $(node 07-animasyon/kare-listesi.mjs 0.9)` | 123/123 kare (her kesme +0,9 sn) → `kareler/kontak-giris-1..4.jpg` |
| ≤1 sn giriş kapısı (kontak taraması) | ilk tur 4 ihlal (S06 kutu yüklemesi, S19 faturalar, S21 G4 başlığı, S17 G3 yalnız başlık) → 3'ü düzeltildi (kesik kutu çerçeveleri, başlıklar t0'da); G3/G5/UK başlıkla girer, değer kelimede |
| 9:16 (`KMirasD-Sh1`, `KMirasD-Sh2`) | 16/16 kare; her grafik cümle başında (−0,15 sn) girer → `kareler/kontak-dikey.jpg` |

## Yapı
- `sahneler.tsx`: `Sahne` = aktif kesmenin çekimi (`CEKIM` anahtarı "ad:param") + ekran yazıları + R-kodlu kaynak satırı. `Tam`, `SahneComp`, `KritikTest` (S01 + S12 bant gag'i başı ≈ 20 sn), `DEk` (Shorts tam okuma; cümle → çekim tablosu `EK_CEKIM`, cümle sayısı değişirse hata fırlatır).
- `grafik.tsx` (kodla çizilen): Kutu/KutuDizisi (10 Okafor kutusu, renk sabit, kayıp sırası LIVING 4,5 → CARE 6 → GIVING 8), Pano (sızıntı çizelgesi / envanter: S07, S11, S12, S14, S16, S18, S22), Selale G6 (envanter şelalesi, 10 → 6 − dilim → ≈3 each), G7 bölünmüş tablo (Cerulli ızgara ‖ Fed DFA ayrı panel, "separate data"), G1 (124 = ~105 + ~18; es/bagis varyantı), G2 (100 ikon 56/22), G3, G4 (aynı doğrusal ölçekte $15M vs ~$410K), G5 (iki ayrı kart, farklı pencere), G19, Fatura, Kapılar, 7'de 1, Banknot, Tabela(lar), Gişe, Saat, Bayrak, Tez, EsTabela, DevKutu (S01 hook: ≤3 sn damla, $18T dilim, 10 kutu), KaynakSatiri (R-kodu → `KAYNAK` metni; ORNEK → "EXAMPLE FAMILY · ILLUSTRATION").
- Donma önleme: tüm grafik zeminleri `Zemin` (%0,35/sn itme + girişte %1,2 punch-in); yer tutucu plaka da kayar + itme. Kutular/pano idle salınımı.
- Leo: **yer tutucu rig** = S08 Leo (`rig.ts` KLASOR "kbutce", `YER_TUTUCU_RIG = true` → karede kırmızı uyarı etiketi). Nakliye yelekli Leo pozları + yamalar gelince `varlik-hazirla.py` rig.ts'in üstüne yazar.
- Ses yok: `ANLATIM_HAZIR = false` (Audio bileşenleri kapalı; render ses dosyası aramaz).

## Ses gelince (yeniden eşleme, ~10 dk)
1. `tools/animasyon/rhubarb-toplu.py` → `tools/animasyon/sahne-veri.py --ses-dizin 04-ses --rhubarb 07-animasyon/rhubarb --cikis video/src/videolar/miras-sizintilari/veri-sahne.ts --ek sh1:shorts-1-ek --ek sh2:shorts-2-ek` (ses-muhendisi'nin `sahne-zamanlari.json` S01–S31 olmalı).
2. `node 07-animasyon/olay-cikar.mjs` — eksik çapa varsa adıyla patlar; düzelt; cue + agiz-gorunur yeniden yazılır.
3. `sahneler.tsx` `ANLATIM_HAZIR = true`; DEk `ekPlan` k değerleri (fifteen/median vb.) Whisper kelime zamanına çevrilir.
4. KMirasKritik render → `test-10sn.mp4`, senkron testi, AgizTest.

## Açık işler / riskler
- **Canva plakaları yok**: 60+ kesme "YER TUTUCU" plakası (kamyon kapısı, harita, yol, ev içi, okul, kavşak…). Plaka adları gorsel-varlik-sanatcisi teslimiyle `yer:<ad>` → `Plaka` eşlenecek; prompt talebi ayrıca hazırlanacak (sahne listesi = `efekt-cue.json` `kesme:` satırları).
- **Kadans**: bazı kesmeler uzun (S26 şelale 27,6 sn, S21 G4 ~23 sn, S06 17 sn) — grafik içi sürekli animasyon var ama referans tempo için plaka gelince punch-in/kesme eklenecek (hedef ≤8 sn).
- Tahmini süre 15:04 (metin §12 13:28 duraklamasız). Gerçek TTS ile değişir; bölüm zamanları kurgu-editoru'nde.
- Dikey grafikler üst yarıda; Shorts altyazısı alt 430 px; Shorts ABONE (sonda, alt orta 1150–1304) için son cümlede (soruKutu) alt orta boş.
- Elenen: (a) S08'deki gibi her sahne için ayrı elle yazılmış bileşen (31 sahnede ~2.000 satır, ses sonrası her kesme iki yerde değişir) → kesme listesinden çekim anahtarlı tek çatı seçildi; (b) Shorts'u uzun anlatım kesitinden kurmak → metin §5 Shorts'u ayrı tam okuma tanımlıyor, DEk cümle zamanıyla kuruldu (dikey sahneler yine var).
