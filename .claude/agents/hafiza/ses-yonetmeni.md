# ses-yonetmeni — hafıza

## Kurallar
- Telaffuz hatası = tam dosya Whisper'ı + cümle tek başına (`cumle-whisper.py`) iki yerde tekrarlanan hata; düzeltme misaki `[kelime](/IPA/)` (`+2` vurgu çoğu kez işe yaramaz), kilitli metin değişmez (1929 + yeni-video).
- Tek cümle düzeltmesi tam yeniden üretim (~6 dk + Whisper 3 dk) yerine `uretim/2026-10-28-yeni-video/04-ses/ekle-cumle.py` ile ham wav'a eklenir, sonra tts-son + Whisper.

## Dersler
- 2026-10-26: Niyazi ücretsiz yapay zekâ anlatıcı sesi istiyor → TTS bu ajana bağlandı (ik-direktoru). Kokoro-82M Apache-2.0 (PyPI `kokoro` 0.9.4, HF erişilebilir) doğrulandı; VOICES.md'de erkek ABD sesleri (am_michael, am_fenrir, am_puck) "C+", af_bella "A-" notlu — karar yine ölçüm + kör dinlemeyle.
- 2026-10-26: Niyazi'nin kendi kaydında Whisper hata oranı %10 (temiz) — TTS için kıyas çizgisi.
- 2026-10-26: Niyazi kör testte (A/B/C) ajan seçimi am_michael yerine **am_fenrir 0.9**'u (daha genç, enerjik; perde 153 Hz, değişkenlik 4.4 yarım ton) seçti. Ders: ölçüm 'sakin/güvenli'yi öne çıkardı, Niyazi 'enerjik'i tercih ediyor; enerjiyi ölçütte daha ağır tart, son kararı her zaman kör dinlemeyle Niyazi'ye bırak.
- 2026-10-27 (1929-1000-dolar F4): Tam metin (1.701 kelime) am_fenrir 0.9 → **10:31.6, 161.6 kpm** (metin 143 kpm varsaymıştı → −82 sn). Pilottaki kpm uzun metne genellenmez (paragraf duraklama oranı farklı). Bir dahaki sefere: metin kilidinden ÖNCE senaryo-yazari'ya 160 kpm hesabını söyle; ≥10 dk kuralı için pay gerekirse hız değil duraklama (`--cumle/--paragraf`) artır.
- 2026-10-27: `tts.py` "U.S. " sonrasında cümleyi bölüyor (cümle ortası 0,3 sn sessizlik) → kısaltmaları `[U.S.](/jˌuˈɛs/)` fonetik işaretiyle ver. misaki işaretleri çalışıyor: `[kelime](/IPA/)` ve `[kelime](+2)` vurgu; `ʰ` dahil.
- 2026-10-27: Tam dosya Whisper'ı bağlam yanlılığı (is→was, looks→looked) ve sessizlikte uydurma ("Yes." p 0,12) üretir → hatayı **cümle tek başına** (`04-ses/cumle-whisper.py`) yeniden çöz; ancak orada da tekrarlanan hata gerçek telaffuz hatasıdır. Bu videoda 4 gerçek hata (this→the, "And Box"→"Inbox", "Leo is"→"Lia was", looked→looks) fonetik işaretle düzeldi. Kokoro deterministik → tohum yok; varyant = işaret/yazım.
- 2026-10-27: "Toonomy" espeak'te doğru (tˈunəmi, "TOO-nuh-mee") ama Whisper "Toonami" yazar (ASR yanlılığı). Kanal adı geçen metinde kapıyı Whisper `initial_prompt`/hotword ile ya da fonem kıyasıyla ölç; düz WER'e güvenme.
- 2026-10-27: `hata-orani.py` WER'inin çoğu normalizasyon artığı (sıra sayıları, "$1,000") — 45 hatanın 41'i. Gerçek değeri raporda sınıflandırarak ver.
- 2026-11-02 (yeni-video S08 F4): 1.878 kelime → 11:18, **166 kpm** (1929'da 161,6; kısa cümle oranı yüksek). Süre tahmininde 160–166 kpm bandı ver. Cümle başı "A, B, or C" Kokoro'da artikel /ə/ → harf için `[A](/ˈA/)`. "borrows"→"barfs": `/bˈɔɹˌOz/`.
- 2026-11-02: Whisper uzun dosyada bütün bir cümleyi atlayabilir (cümle 93) → hizala.py 'ara' ile tahmin eder; WER'de "delete" uzun dizi görünce tek başına çöz, ses hatası sanma. Yazıyla uzun sayılar SRT'de >25 kr/sn → kurgu-editoru'na rakam notu.
