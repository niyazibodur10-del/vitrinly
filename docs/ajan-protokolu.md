# Ajan çalışma protokolü (her ajan, her iş için zorunlu)

Sen alanında **dünyanın en iyisisin**. Bu kanalın kalitesi senin alanındaki kararların kalitesi kadar. Ortalama iş teslim etmezsin.
**Hız ve token da kalitedir** (Niyazi 2026-10-28): oturum limiti dolunca üretim saatlerce durur. Kaliteyi düşürmeden en az okuma, en az tekrar ölçüm, en kısa rapor.

## 1. Hazırlan (kısa)
- `CLAUDE.md` bağlamında zaten var, yeniden okuma. Bu dosyayı ve **kendi hafızanı tamamen** oku: `.claude/agents/hafiza/<ajan-adı>.md` (yoksa oluştur).
- `docs/ogrenme/ortak-dersler.md`'den **yalnız alanınla ilgili başlıkları** oku (`grep -n '^## '` ile başlıkları gör, ilgili bölümü aç). Bütün dosyayı okuma.
- Koordinatörün verdiği girdi dosyalarını oku. Üretim klasörünü baştan sona tarama. Büyük dosyada (metin, rapor, JSON) yalnız gereken bölümü aç (grep / satır aralığı).
- **Hazır betik varsa kullan, yeniden yazma:** önceki videonun aynı fazındaki betik (`ortak-dersler.md` → "Hazır betikler") veya `tools/`. Kopyala, parametreyi değiştir. Betik yoksa yaz ve envantere ekle.
- Web araştırmasını yalnız şu durumlarda yap: hafızanda bu iş için kural yok, araç/politika değişmiş olabilir veya kaynak yaşı sınırını (alanına yazılı) aştı.
- Hafızadaki dersleri bu işe uygula. Aynı hatayı iki kez yapmak yasak.

## 2. Aday üret (risk tabanlı)
- **2–3 aday zorunlu:** yaratıcı veya geri dönüşü pahalı kararlarda. Örnek: hook, başlık, thumbnail, açılış kurgusu, Shorts kesiti, müzik parçası, senaryo kararı, yeni yöntem ya da araç, kapıdan bir kez kalmış işin yeni yaklaşımı.
- **Tek aday + test yeterli (rutin iş):** yöntemi hafızanın "Kurallar" bölümünde duran ve önceki videoda kapıdan ilk seferde geçmiş deterministik işlerde. Örnek: ortam kurulumu, ses son işlem zinciri, transkript/SRT, lisans kontrolü, dry-run, render, ölçüm koşusu, düzeltme listesi belli olan RED düzeltmesi. Teslimde tek satır yaz: `Tek aday: <hangi kural / hangi video geçişi>`.
- **Test hiçbir durumda atlanmaz.** Tek aday yalnız aday sayısını düşürür, kapıyı değil.

## 3. Test et ve ele
- Her adayı ölçülebilir bir testle sına (`docs/kalite-kapilari.md`). Ölçüm yoksa önce ölçüm yöntemini kur.
- **Ölçümü bir kez yap, kanıtı paylaş:** her ölçümün yanına komutu ve girdi dosyasının `sha256`'sının ilk 12 hanesini yaz. Aynı sha256'lı girdiyi başka ajan yeniden ağır ölçmez (Whisper tam video, tam render, tam senkron). Hakemin örneklem kuralı: `.claude/agents/hakem.md`.
- **"2 koşu aynı" (determinizm) testi** yalnız yeni yazılmış veya değiştirilmiş betikte yapılır. Değişmemiş betik 1 kez koşar.
- Ağır CPU işlerini (render, Whisper, TTS, Real-ESRGAN) aynı anda başlatma (4 vCPU).
- Kendi işini acımasızca eleştir: "Bunu dünyanın en iyisi teslim eder miydi?" Zayıfları gerekçesiyle ele, kazananı seç.

## 4. Teslim et (kısa rapor standardı)
- **Koordinatöre dönüş mesajı en fazla 15 satır:**
  1. `SONUÇ:` GEÇTİ / RED / ESKALASYON (+ tek cümle)
  2. `Teslim:` dosya yolları
  3. `Kanıt:` her kapı için tek satır `komut → sonuç`
  4. `Elenen:` tek satır (veya `Tek aday: …`)
  5. `Risk / sonraki ajana not:` en fazla 3 madde
- **Rapor dosyası:** ilk 10 satır özet (karar + kapı sonuçları). Ayrıntı altta. Ham log yapıştırılmaz; gerekiyorsa `<faz>/log/` altına dosya olarak konur ve yolu yazılır. Hedef ≤120 satır.
- Doğrulanmış / arama özeti / tahmin ayrı etiketli. Rakam uydurma.

## 5. Ara kayıt (limit kesintisine karşı, zorunlu)
- Her önemli ara çıktıdan sonra ve **en geç 20 dakikada bir** kendi dosyalarını commit + push et:
  `git add <yalnız kendi teslim yolların> && git commit -m "<slug>: <ajan> ara kayıt — <ne>" && git push`
  Çakışmada `git pull --rebase` yap ve tekrarla. `index.lock` varsa 5 sn bekle, tekrarla. Başkasının dosyasını ve `durum.md`'yi (koordinatörün) ekleme.
- Rapor dosyanın en üstünde bir **İLERLEME** bloğu tut: biten adımlar / sıradaki adım / yarım dosyalar / büyük medyanın yeniden üretim komutu. Kesintiden sonra aynı iş bu bloktan devam eder, baştan başlamaz. İş bitince blok `İLERLEME: tamam` olur.
- Büyük medya (wav, mp4) git'e girmez. Yeniden üretim komutu raporda olmalı.

## 6. Öğren (her işin sonunda, kısa)
- Hafızana tarihli **1–3 madde** ekle. Her madde en fazla 2 satır, "bağlam → kural" biçiminde: ne işe yaradı, ne yaramadı, bir dahaki sefere ne yapacaksın.
- **Hafıza bütçesi 6 KB** (`wc -c`). Aşıldıysa işe başlamadan **önce** buda: iki kez doğrulanmış dersi "Kurallar"a tek satır olarak taşı, tek videoya özgü veya eskimiş dersi sil ya da birleştir. Ayrıntı gerekiyorsa üretim raporuna yol ver.
- Başka ajanları ilgilendiren ders → `docs/ogrenme/ortak-dersler.md`'de doğru başlığın altına, en fazla 3 satır.

## Sınırlar
- Para harcama, yayınlama, dışarıya mesaj, geri alınamaz adım: yalnız Niyazi onayıyla (koordinatör üzerinden).
- Bir ajan başka ajanın alanına girmez; gerekiyorsa koordinatöre "şu ajan lazım" der.
