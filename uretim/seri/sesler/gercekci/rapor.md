# Gerçekçi karakter sesleri — 6 kör aday (ses-yonetmeni, 2026-11-11)

İLERLEME: tamam (örnekler hazır; Niyazi'nin seçimi bekleniyor → `tools/ses/bolum-ses.sh` tek komut)
**Sonuç:** 6 dosyanın hepsi **Kyutai Pocket TTS** (100M parametre, yerel CPU, ücretsiz; kod MIT, ağırlık CC BY 4.0). Supertonic-2 hızlı ama bölümde kelime yuttuğu için elendi. Chatterbox, Dia, Orpheus, Kyutai 1.6B ve Qwen3-TTS diske sığmadı (boş alan 1,4 GB).
**Kapılar:** 6 örnekte WER %0 (A3: %2,9, tek kelime "A→The") · −13,9…−14,4 LUFS · TP ≤ −1,5 · süre 10,3–15,8 sn.
**Hız (Bölüm 1, 25 replik, gerçek ölçüm):** Pocket ile üretim 48–56 sn; transkript, Rhubarb ve kilit dahil toplam **78–90 sn** (sınır 10 dk).
**Ölçüme göre önerim:** Jake = A1 (95 Hz, sakin ±1,9 yarım ton, Amerikan) + Mike = A3 (150 Hz, enerjik, 196 kpm). Perde farkı 7,9 yarım ton. Bölüm 1 tam testi: 70–72 sn, WER %0–1,7, kapıların hepsi geçti. Karar Niyazi'nin kulağında.
**Risk:** (1) A2, A3, A4 ve A6'da aksan kaydı yok; Amerikan aksanı dinleyerek doğrulanmalı (A1 ve A5 VCTK'da "American" olarak kayıtlı). (2) Pocket örnekleme yapıyor (temp 0.3): her üretim biraz farklı çıkıyor, bölüm bir kez üretilip sha ile kilitleniyor. (3) CC BY 4.0 atıf yükümlülüğü var (aşağıda).

## Ölçüm tablosu (son dosyalar, `olc.py` → `olcum-A.json`; Whisper small.en, 34 kelime)
| Dosya | WER | Whisper güveni | F0 | Perde değişkenliği | kpm | Duraklama ≥150 ms | Değerlendirme |
|---|---|---|---|---|---|---|---|
| A1 | 0 | 0,920 | 95 Hz | 1,9 yt | 180 | 2 | düz ve sakin, temkinli Jake'e uyuyor; az duraklama, cümleleri bağlıyor |
| A2 | 0 | 0,955 | 98 Hz | 4,6 yt | 166 | 6 | koyu ama canlı tonlama, cümle sonu düşüşleri doğal; anlatıcı tınısı |
| A3 | 2,9 | 0,941 | 150 Hz | 3,8 yt | 196 | 5 | genç, hızlı, enerjik; Mike'ın aceleciliğine uyuyor. "A price" iki üretimde de "The" duyuldu |
| A4 | 0 | 0,972 | 82 Hz | 0,5 yt | 137 | 6 | çok koyu, yavaş, en net; perde ölçümü çok düz, monotonluk riski var (kulakla kontrol) |
| A5 | 0 | 0,961 | 115 Hz | 2,4 yt | 203 | 6 | orta perde, en hızlı konuşan; hem Mike hem Jake olabilir |
| A6 | 0 | 0,965 | 122 Hz | 5,6 yt | 148 | 6 | en dalgalı tonlama, en "oyunculu" ses; Mike'a uyuyor |

Doğallık ölçütü: perde değişkenliği (monotonluk), cümle arası doğal duraklama ve nefes, Whisper güveni. Kulakla dinleme yapılmadı (ajan dinleyemez); son karar Niyazi'nin kör dinlemesinde.

## Lisans doğrulaması (2026-11-11, HF API + model kartları)
- **Pocket TTS:** `kyutai/pocket-tts-without-voice-cloning` (kapısız; `license: cc-by-4.0`), kod MIT (pip `pocket-tts` 4.0.1). Model kartı yasakları: izinsiz ses taklidi ya da klonlama yok, üretilen sesi gerçek kayıt gibi sunmak yok. Bizde ses klonlama yok, yalnız hazır katalog sesleri kullanılıyor; açıklamadaki AI beyanı sürüyor.
- **Seslerin kaynakları** (huggingface.co/kyutai/tts-voices README + `pocket_tts/utils/utils.py`):
  - VCTK (CC BY 4.0): michael = p360, george = p315
  - Gönüllü bağış (CC0): marius, javert
  - voice-zero / LibriVox (CC0): peter_yearsley, stuart_bell, bill_boerst
  - **Yasak (NC):** jean (EARS), cosette (Expresso). `tools/ses/gercekci_tts.py` yalnız izinli listeyi kabul ediyor.
- **Atıf (CC BY 4.0, youtube-paketleyici'ye):** açıklamaya şu satır eklenmeli: "Voices: Kyutai Pocket TTS (CC BY 4.0); VCTK corpus (CC BY 4.0)" (VCTK yalnız A1 ya da A5 seçilirse).
- **Supertonic-2:** OpenRAIL-M; ticari kullanım serbest, ama içeriğin makine üretimi olduğu açıkça belirtilmeli. Kod MIT. Lisansı uygun ama kalite nedeniyle elendi.

## Elenenler (tek satır)
- **Supertonic-2** M1–M5: en hızlısı (80 sn'lik bölüm ≈ 8 sn), ama kelime yutuyor. Örnekte M1, M3, M5 ("A price", "Jake", "Hold on"); Bölüm 1'de M2 WER %8,5 ("make", "Slow"), M4 %4,5 ("A million", "is free", "and wait"). Tek başına çözülen satırlarda da tekrarladı → gerçek model hatası.
- **Pocket `bill_boerst`:** 12 saniyede hiç duraklama yok (cümleleri yapıştırıyor), güveni en düşük (0,915).
- **Chatterbox / Chatterbox-Turbo (MIT):** ağırlık 3–4 GB, boş alan 1,4 GB.
- **Dia 1.6B** (6,4 GB), **Orpheus 3B** (≥6 GB; Llama tabanlı, CPU'da yavaş), **Kyutai TTS 1.6B** (4 GB), **Qwen3-TTS 0.6B** (2,5 GB), **VibeVoice-Realtime 0.5B** (2 GB): disk. NeuTTS Air: codec 0,8–1,2 GB ve kapılı.
- **StyleTTS2-LibriTTS** (0,77 GB): kurulumu ağır (repo kodu + phonemizer), 13:00Z son tarihine yetişmezdi; yedek olarak duruyor.
- **XTTS-v2 (CPML), F5-TTS (NC), Pocket jean/cosette, Expresso/EARS kaynaklı sesler:** ticari kullanıma kapalı.
- Pocket 24 katmanlı İngilizce modeli (1,3 GB, daha yüksek kalite) disk yüzünden denenmedi. Disk açılırsa sıradaki iyileştirme bu.

## Üretim hattı (seçim gelince tek komut)
```
tools/ses/bolum-ses.sh uretim/seri/bolum-001 --ses JAKE=pocket:michael --ses MIKE=pocket:marius
```
- `tools/ses/gercekci_tts.py`: motorlar `pocket:<ses>`, `supertonic:<M1..M5>[:hız]`, `kokoro:<am_x>:hız`. Gerçekçi motorlar satırı tek parça üretir, böylece cümleler arası prozodi doğal kalır.
- `tools/ses/diyalog.py`: motor seçimli. Satır arası boşluk kuralları aynı. Tepe sınırı nedeniyle −14,5'in altında kalırsa 4 kat aşırı örneklemeli sınırlayıcıyla ikinci geçiş yapar (Pocket'te gerekli oldu: −14,6 → −14,2).
- `tools/ses/bolum-ses.sh` çıktıları (formatlar Kokoro kilidiyle aynı, `<dizin>/ses/` altında):
  - `bolum-001.wav` ve `.m4a`
  - `.zaman.json`
  - `-JAKE` / `-MIKE` `.wav` + `.txt`
  - `referans.txt`, `kelimeler.json` (small.en)
  - `rhubarb/JAKE.json`, `rhubarb/MIKE.json`
  - `kilit.json` (sha256, süre, WER, LUFS, TP, sesler, süreler)
- Kapılar: 60–90 sn, WER ≤ %5, LUFS −14 ±0,5, Rhubarb her satırda. Kalırsa çıkış kodu 2 döner; Pocket örnekleme yaptığı için yeniden koşmak yeterli.
- Ortam: `~/.finansal-arac/gercekci-venv` (python3.12; torch kokoro-venv'den `.pth` ile paylaşılıyor, ek ~60 MB). Kurulum: `pip install pocket-tts onnxruntime`. Supertonic modeli `~/.finansal-arac/modeller/supertonic-2`. Pocket ağırlıkları ilk çalıştırmada HF önbelleğine iner (~220 MB). `tools/kurulum.sh`'ye eklenmesi gerekiyor → uretim-muhendisi.
- Bölüm 1 hat testleri (karalama dizini, kilitli Kokoro dosyalarına dokunulmadı):
  - michael + marius: 72,3 sn / WER %0 ve 70,8 sn / %1,7
  - george + Supertonic M4: %4,5 (yukarıda)
  - Supertonic M2 + stuart_bell: %8,5 (yukarıda)
  - Rhubarb her koşuda 13/13 ve 12/12 satır

## Yeniden üretim
`~/.finansal-arac/gercekci-venv/bin/python tools/ses/gercekci_tts.py pocket:<ses> "<metin>" out.wav` → `tts-son.sh` → `diyalog.lufs_duzelt` → m4a (aynı iki replik, 0,5 sn ara). Ölçüm: `~/.finansal-arac/venv/bin/python olc.py A?.m4a`.
