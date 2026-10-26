# Kalite referansı 01 — analiz

Kaynak: Niyazi'nin ekran kaydı (Instagram reel, hesap "yaasonra.yt", "Zombi İstilası Part 5"), 2026-10-26.
Dosya: 828x1792 dikey ekran kaydı, 20.2 sn (videonun kendisi ~18 sn). Kareler: `assets/referans/referans-01-*.jpg`.
Not: karakter ve çizimler başkasına ait; **stil seviyesi** referans alınır, karakter/kompozisyon kopyalanmaz.

## Ölçülenler (ffmpeg)
- Sahne kesmesi (scene>0.2): 1.34, 2.26, 3.71, 5.18, 6.58, 7.55, 8.61, 9.91, 12.28, 13.28, 14.78, 17.45 sn
  → ~18 sn'de 12 kesme, **ortalama ~1.4 sn'de bir yeni görsel**.
- Ses: ortalama −17.9 dB, tepe 0.0 dB (ekran kaydı üzerinden; kaynağın gerçek miksajını göstermez).

## Gözlenenler (kare inceleme)
- **Teknik aslında "hareketli illüstrasyon":** her sahne tek, çok detaylı bir çizim. Kare kare animasyon yok;
  su dökme sahnesinde 6 fps örneklemede su ve eller sabit. Hareket = kamera (yavaş zoom/pan, ani "punch-in" yakınlaştırma) + kesme.
- **Tutarlı karakter:** her sahnede aynı tasarım (beyaz yuvarlak kafa, tek tutam saç, beyaz eldivenli eller, kırmızı örgü kazak, gri pantolon).
  Duygu yüz ifadesi ve vücut pozuyla veriliyor (kızgın kaşlar + "dur" eli, şaşkın göz, uyuyan pozu).
- **Çizim kalitesi:** kalın siyah kontur, cel-shading gölge, detaylı ve yaşanmış mekânlar (Türk evi: banyo, çaydanlık, damacana),
  soğuk mavi-gri arka plan + sıcak kırmızı karakter = karakter her karede öne çıkıyor.
- **Altyazı:** ekranın altında 1–4 kelimelik parçalar, beyaz kalın yazı + **anahtar kelime sarı/yeşil vurgulu**, kelime kelime ilerliyor.
- **Bilgi grafiği:** sayılar ekrana büyük yazı olarak giriyor ("88 LİTRE", "22 gün"), basit ikonlar (yasak işareti).
- **Anlatım:** ikinci tekil şahıs ("küveti de dolduruyorsun", "sonra kendine soruyorsun"), problem → çözüm → yeni problem zinciri ("3. problem: yemek").
  Seri formatı ("Part 5") → izleyiciyi geri getiriyor.

## Bizim için sonuç
1. Referans kalitesine ulaşmanın yolu **tam animasyon değil, sahne başına üst düzey tutarlı illüstrasyon + sinematik kamera + hızlı kesme + vurgulu altyazı**.
   Bu hem kanıtlanmış bir format hem de uzun videoda üretilebilir.
2. Niyazi'nin istediği **ağız/el/ayak senkronu** bunun üstüne eklenir (hibrit):
   - Karakterin konuştuğu "anlatıcı" sahneleri: katmanlı rig + Rhubarb dudak senkronu + göz kırpma + el jestleri.
   - Önemli anlar (sahne başına birkaç saniye): AI image-to-video ile gerçek vücut hareketi (yürüme, dökme, düşme) — kör testle model seçimi.
   - Kalan sahneler: referanstaki gibi tek illüstrasyon + kamera hareketi.
3. Uzun video için tempo: referans 1.4 sn/kesme (kısa video). Uzun videoda hedef ilk 60 sn ~1.5–2 sn, sonra 3–6 sn (tahmin; rakip analizinden kalibre edilecek).
   Görsel sayısı hesabı: 12 dk video ≈ 720 sn; ortalama 4 sn/sahne → ~180 illüstrasyon (kamera ile aynı görsel 2–3 kez farklı kadrajda kullanılabilir).
4. Altyazı stili ve sayı grafikleri kodla (Remotion) üretilir; Türkçe yazıyı AI görsel modeline yazdırmayız.
5. Uzun video yatay 16:9 olacak; aynı sahnelerden 9:16 Shorts kesitleri ayrıca çıkar (referans formatı zaten Shorts/Reels).
