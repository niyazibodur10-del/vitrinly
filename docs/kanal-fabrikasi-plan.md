# Kanal fabrikası (şablon) — plan (Niyazi 2026-11-02)

**Ne zaman:** S08 yüklendikten sonra (2026-11-03). Tetik: Niyazi "üretim fabrikasını kuralım" der → koordinatör bu planla yönlendirir.
**Hedef:** başka bir Claude Code hesabında 1. mesajda sistemi yükle, 2. mesajda `/kurulum` sihirbazı her şeyi sorup kursun; sonra "Bugünün videosu gelsin" çalışsın.

## 1. mesaj — yükleme
- Bu repodan kanala özel veriden arındırılmış şablon repo (`kanal-fabrikasi`, GitHub "Use this template"). Yer: yeni repo (Niyazi açar + erişim) veya bu repoda ayrı dal — yarın Niyazi'ye sorulacak.
- SessionStart kancası + `tools/kurulum.sh` (Remotion, Rhubarb, Whisper, Kokoro).

## 2. mesaj — `/kurulum` sihirbazı (sırayla)
1. **Niş → alt niş → isim (Niyazi şartı):** kullanıcı bir niş verir → ajanlar o nişin alt nişlerini/açılarını önerir (talep, rekabet, RPM, YPP riski, özgünlük; kaynaklı) → kullanıcı seçer → **kanal adı önerileri** (çakışma/@handle kontrolü, global okunurluk).
2. **Kadro otomatik (Niyazi şartı):** `ik-direktoru` seçilen nişe göre kadroyu otomatik kurar — nişe uymayan ajanları **işten çıkarır**, eksikleri **işe alır** (ör. finans-dogrulayici → nişin doğrulayıcısı), değişiklikleri `docs/kadro-degisiklikleri.md`'ye yazar; çekirdek üretim ajanları kalır.
3. Karakter: referans yükleme veya Canva ile üretim → karakter kartı + rig.
4. Ses: 3 ücretsiz TTS kör testi.
5. Kanal kimliği: açıklama, banner, profil, oynatma listeleri, takvim.
6. Bağlantılar (adım adım yönlendirme): Google Cloud proje + YouTube Data API + OAuth istemcisi; secret'lar ortam ayarına (sohbete asla); `yukle.py --yetki-al` + "Publish app"; claude.ai → Connectors → Canva.
7. `kanal.json` + yeni CLAUDE.md yazılır → 10 sn deneme videosu → hazır.

## Taşınır / sıfırlanır
- Taşınır: ajanlar, komutlar, kalite kapıları, tools/, Remotion bileşenleri (AboneOl dahil), ortak-dersler.
- Sıfırlanır: uretim/, kanal-kimligi, assets/karakter, rakip analizi, viralite kalibrasyonu, ajan hafızalarının kanala özel kısmı.

## Yapacaklar
`uretim-muhendisi` (şablon, kancalar, kanal.json parametreleri) ‖ `ik-direktoru` (otomatik kadro mantığı, sihirbaz komutu) → boş oturumda uçtan uca test → hakem.
