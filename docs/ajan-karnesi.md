# Ajan karnesi

Her teslimattan sonra `hakem` puan verir (1–10): kalite, test kanıtı, protokole uyum, hız.
`ik-direktoru` bu tabloya bakarak eğitir, yeniler veya değiştirir.
Kurallar: son 3 işin ortalaması < 6 → uyarı + yeniden yazım; ardışık 2 iş < 5 veya Niyazi "beğenmedim" → işten çıkar (arşiv) + yenisini al.

| Tarih | Ajan | İş | Puan | Not |
|---|---|---|---|---|
| 2026-10-26 | kanal-analisti | rakip analizi v1 | — | veri erişimi kısıtlı; puanlama hakem tarafından yapılacak |
| 2026-10-26 | viralite-analisti | model v0.1 | — | betik + test teslim etti |
| 2026-10-26 | ses-muhendisi | TTS + müzik/efekt + miks | 8 | koordinatör ön puanı: kapsamlı test, lisans kanıtı; Niyazi yedek sesi seçti (ölçüt enerjiyi az tarttı) |
| 2026-10-26 | gorsel-varlik-sanatcisi | Canva karakter paketi v1 | 9 | koordinatör ön puanı: 7/7 tutarlılık, tam çözünürlük yolu; Niyazi onayı bekleniyor |
| 2026-10-27 | uretim-muhendisi | F0 ortam (secim) | 9 | 9 komutluk test tablosu; 2 gerçek arıza bulup düzeltti (render-son.sh -inf LUFS, Whisper hata mesajı), 3 aday + eleme, regresyon −14,0 LUFS; hafıza dersi var; 10 dk |
| 2026-10-27 | trend-avcisi | F1 konu havuzu | 8 | 23 konu, kaynak-kontrol.py 23/23, ilgi ölçümü kaynaklı; eksi: KH-A12 gümüş zirvesi 48,70 $ yanlış etiketli (doğrulayıcı yakaladı); hafıza dersi var |
| 2026-10-27 | kanal-analisti | F1 rakip özeti | 8 | 39 kanal/1.123 video [API], 81/81 etiketli, desenler ≥2 örnekli, kopyalamama tablosu; eksi: son-20 medyanı büyüyen kanalda skoru düşürdü (MotP 4,4x→yerel 7,6x, viralite-analisti düzeltti); search 429 dürüstçe raporlandı |
| 2026-10-27 | senaryo-yazari | F2 11 senaryo | 8 | 11 senaryo/11 açı, her hook 3 aday + eleme, betik 2 koşu aynı, çelişkileri kendisi işaretledi; eksi: tavsiye dili sızdı (S03 "picked wrong", S06 "what I believe now"), S05/S08 başlıkları rakibe çok yakın (−1.5 ceza) |
| 2026-10-27 | viralite-analisti | F2 viralite sıralaması | 9 | betik 2 koşu sha256 aynı, 56 durumluk duyarlılık + çapraz test, kırılgan 3. sırayı açıkça bildirdi, yerel medyanla rakip-özeti düzeltti; eksi: tur 2 risk filtresi doğrulama raporu gelmeden yapıldı (kendisi belirtti) |
| 2026-10-27 | finans-dogrulayici | F2 ön doğrulama | 9 | 2 çelişkiyi birincil kaynakla çözdü (49,45 $; 1 RM = 10¹² M), hesaplar [H], her SARI için 3 güvenli yazım; eksi: bazı satırlar [AÖ] düzeyinde kaldı (Cisco, gümüş payı) |
| 2026-10-27 | monetizasyon-uyum-uzmani | F2 politika ön taraması | 9 | 3 politika sayfası bugün yeniden okundu, birebir alıntılar, her SARI'da 2–3 seçenek + viralite maliyeti, betik 2 koşu aynı, kanal düzeyi kimlik notu; hafıza dersi var |
| 2026-10-27 | hakem | F2 senaryo kararı | — | kendini puanlamaz; ik-direktoru puanlar |
| 2026-10-27 | senaryo-yazari | F3 tam metin (1929-1000-dolar) | 7 | 1.701 kelime, retention haritası, Shorts kancaları, betik 2 koşu aynı. Eksi: doğrulayıcı RED-1 ile 6 zorunlu düzeltme buldu. 143 kpm varsayımı gerçekte 161,6 kpm çıktı (−82 sn, ≥10 dk payı daraldı). Hafıza dersi var |
| 2026-10-27 | finans-dogrulayici | F3 metin doğrulama | 9 | RED-1: 6 düzeltme kesin metinle, yeniden doğrulamada eşlenmeyen rakam 0, 48/42 ay pencere etiketi önerisi finalde işe yaradı; betik 2 koşu aynı |
| 2026-10-27 | monetizasyon-uyum-uzmani | F3 metin politikası + F8 politika raporu | 9 | Birebir politika alıntıları, Ö1–Ö12 tablosu, sahne tekrarı betikle %0,0, Z1 yol hatasını yakaladı, negatif test var. Ölçümlerim raporla çelişmedi. Eksi: Ö9'u "kısmi" bıraktı, kapatacak sahip/tarih atamadı (hakem ŞY-1 olarak kapattırdı) |
| 2026-10-27 | ses-yonetmeni | F4 TTS anlatım | 8 | 4 gerçek telaffuz hatası fonetik işaretle düzeldi, cümle-Whisper yöntemi, final WER %0,9. Eksi: kpm uyuşmazlığını metin kilidinden sonra fark etti |
| 2026-10-27 | ses-muhendisi | F4 son işlem + hizalı transkript + SRT | 9 | −14,2 LUFS / TP −1,5, 4 aday, akustik hiza p95 7 ms. SRT 228 blok finalde değişmeden geçti (benim taramam: çakışma 0, satır ihlali 0) |
| 2026-10-27 | gorsel-varlik-sanatcisi | F4 Canva dalga 1–3 | 9 | 23 üretimin 23'ünde media ID + tarih, tutarlılık ölçümleri (kafa kor. 0,84–0,96), C11'i 2 kez gerekçeli RED; hafıza dersi var |
| 2026-10-27 | muzik-ses-tasarimcisi | F4 adaylar + F6 miks | 8 | Lisans kontrolü exit 0 (benim koşum da), WER farkı −0,35, konuşma altı 21,7 dB. Eksi: SFX vuruşları görselden 0,4–3 sn kayıktı (20+), kurgu-editoru yeniden zamanladı |
| 2026-10-27 | thumbnail-tasarimcisi | F8 3 finalist | 8 | 9 aday → 3, 168x94 OCR + rakip benzerlik testi, 2 koşu sha256 aynı. Benim küçültmemde 3/3 okunur. Eksi: yol/ad paketle uyuşmadı (Z1, paketleyici tarafında kapandı) |
| 2026-10-27 | animasyon-yonetmeni | F5 kritik yol + tüm sahneler + 9:16 | 8 | Senkron +1 kare (miksli finalde de +1), blackdetect hatasını kendi buldu ve düzeltti, 2×210 kare denetimi. Eksi: S18'de ~1,5 sn boş an ve Sh1 S10'da grafiğin geç girmesi kaçtı (kurgu-editoru raporladı) |
| 2026-10-27 | kurgu-editoru | F7 final + SRT + 2 Shorts | 9 | 3 açılış varyantı ve 4 Shorts adayı → 2. render-parca -shortest kök nedenini buldu, SFX'i görsele yeniden hizaladı. Ölçümlerim raporla birebir (18.949 kare, −14,0/−2,2, WER 15/1726, sha256 3/3). Açık riskleri kendisi yazdı |
| 2026-10-27 | youtube-paketleyici | F8 paket + YAYIN.md | 9 | Dry-run 3/3 0 hata (benim koşum da, teslim/ içinden de), bölümler sahne başına ≤1 sn. Eksi: ilk sürümde thumbnail yolu yanlıştı (Z1, politika uzmanı yakaladı) |
| 2026-10-27 | viralite-analisti | F8 son viralite | 8 | 2 koşu aynı, belirsizlik dürüstçe yazıldı (A2–D1 farkı 0,2 < 0,3 eşik → seçim Test & Compare'e bırakıldı), başlık kalıbı API ile ölçüldü. Model v0.1, kalibrasyon verisi yok |
| 2026-10-28 | kurgu-editoru | F7b abone ol animasyonu + yeniden render | 9 | Sayım 4/1/1, hakem dedektörü aynı sonucu buldu. Klik maskeleme ölçüldü. WER artışını pencerelerle kendisi açıkladı, hakem örneklemi doğruladı. Yalnız 4/11 parça yeniden render. Arızalı aracı yamamadı, HEAD sürümüyle çalıştı. Eksi: Sh2 kartı grafik bandını kısmen örtüyor |
