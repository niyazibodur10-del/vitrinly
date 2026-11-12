# Flip By Vote · karakter sayfaları değerlendirmesi (2026-11-10, gorsel-varlik-sanatcisi)
İLERLEME: J-A, M-A, L1-A, L1-B, T-J, T-M KABUL; kesim + yerleşim + ifade varlıkları `video/public/seri/bolum-001/` (VARLIKLAR.md). AG-J + AG-M KABUL, ağız yamaları teslim. Kota 8/12 (4 yedek).
- **J-A KABUL** (Jake, `MAHajKKbhbM`): kontrol listesi 8/8, sayfa içi yüz kor. ort 0,76 (nötr 0,91; gülen 0,67 / heyecanlı 0,60 → ten açık-pembe kaymış, yüz yapısı aynı).
- **M-A KABUL** (Mike, `MAHajPZXWbU`): kontrol listesi 8/8, sayfa içi yüz kor. ort 0,93 (0,90–0,95). Saç hedef taslaktan koyu (kestane, ΔE 24,6) → kumral tanımına uyuyor; sayfa kanonik kabul edildi.
- Çözünürlük: ikisi 1920x1080 (doğal 1680x944 export). Yazı/logo/ekstra kişi: yok (1:1 göz incelemesi).
- Kota: 2/12 kullanıldı; her istek 1 görsel döndürdü.
- Kontakt: `kontak-sayfa.jpg` (üst: iki sayfa; alt: ön görünüm yüzü + 6 ifade yüzü, Jake üst sıra, Mike alt sıra).

## Ölçüm
Komut: `~/.finansal-arac/venv/bin/python -I araclar/sayfa-olcum.py canva-ham <kontak>` · girdi sha256 J-A `9f8401f215ca`, M-A `a885aca23e36` (`sha256sum canva-ham/*.png`).
| | J-A | M-A |
|---|---|---|
| Ön yüz ↔ ifade HSV kor. | nötr 0,91 · gülen 0,67 · şaşkın 0,75 · endişeli 0,76 · heyecanlı 0,60 · düşünceli 0,84 | 0,91 · 0,90 · 0,94 · 0,95 · 0,93 · 0,95 |
| Renk medyanı (ΔE taslak hedefe) | hoodie #293347 (6,8) · chino #BCAB91 (7,9) · saç #452E20 (4,3) · ayakkabı #E3DEDB (6,8) | flanel kırmızı #901B18 (11,2) · tişört #E9E5E2 (4,5) · jean #2A3445 (7,4) · saç #6B3F23 (24,6) · bot #4C2E1F (6,9) |
Taslak hedef hex'ler prompt öncesi tahmindi. Kabulden sonra hedef = sayfanın ölçülen medyanı (`canva-promptlari.md` §2).

## Kontrol listesi (✔ = geçti)
- Jake: ✔ kısa koyu kahve saç, üstü sağa · ✔ düz koyu kaş · ✔ kahverengi göz · ✔ kısa hafif sakal+bıyık (dolgun değil) · ✔ lacivert hoodie, kapüşon arkada, gri bağcık, baskı yok · ✔ bej chino + beyaz spor ayakkabı · ✔ oval yüz, ince yapı · ✔ gözlük/şapka/saat yok. Not: önden kanguru cebi belirsiz (önemsiz).
- Mike: ✔ dağınık saç alna düşen · ✔ kestane-kumral · ✔ mavi göz · ✔ sakalsız · ✔ büyük kareli kırmızı-siyah flanel, açık, kol dirsek altı kıvrık, beyaz tişört · ✔ koyu jean + kahverengi bot · ✔ yanak kızarıklığı, atletik · ✔ aksesuar yok. Not: ilk portrenin sol alt köşesinde küçük beyaz leke (x≈900, y≈510); taban olarak kullanılmayacağı için önemsiz.
- Ön, yan, arka ve 6 ifade iki sayfada da aynı kişi; yan görünüm sağa bakıyor; ifadelerin 6'sı da ayırt edilebiliyor.

## Kullanım kuralları
- Kimlik çapası = sayfanın **nötr portresi** (sağ üst ilk kare; ön görünüme kor. 0,91). Türev pozların ölçümü bu kareye göre yapılır.
- Jake'in gülen/heyecanlı portreleri doğrudan varlık olarak kullanılacaksa önce ten Lab eşleme (`uretim/2026-10-28-yeni-video/05-gorsel/araclar/ten-esle.py`) gerekir.
- 6 ifade portresi kameraya bakıyor. Dördüncü duvar anlarında (S2, S8) ve tepki yakın planlarında kullanılabilir; konuşmaz, ağız yaması yok.
- Lisans/kaynak: Canva AI (`generate-image`), Niyazi'nin Canva aboneliği, 2026-11-10. Prompt metni `canva-promptlari.md` J-A / M-A, ham kayıt `canva-ham/uretim-kaydi.md`.

## Not (koordinatöre)
- Araba: seri incili L2'ye göre Jake'in arabası, brief'e göre Mike'ın. Prompt nötr ("the friends' car"), karar senaryo-yazari'nda.
- Bölüm 1 metni 23 poz istiyor; 10 hakla bu mümkün değil. Plan için `canva-promptlari.md` §1'e bak (animasyon-yonetmeni'ne iletilecek).

## Tur 2 (2026-11-10): L1-A, L1-B, T-J, T-M
Girdi sha256: T-J `c3bb924da25b`, T-M `b78bbd97b630`, L1-A `de4cc07a70ce`, L1-B `798280488f68`. Kontakt: `kontak-v2.jpg`.
- **L1-A KABUL** (MAHajNE3GRU): kişi yok; 2× kırpımda yazı/logo yok (raftaki kitap sırtları dahil); tezgâh arka kenarı y=1186 (sütun taraması 1179–1191). İstenen ön kenar %68–72 yerine arka kenar %62; bel üstü kesik yine tezgâh arkasına oturuyor.
- **L1-B KABUL** (MAHajDYp1b8): tahta boş ve düz (y 12–37 %), mıknatıs + kalem var. Tabanlar burada kullanılamaz (kesik kollar buzdolabı önünde açıkta kalır) → L1-B = tahta insert'i.
- **T-J KABUL** (MAHajBqI-Qs): kontrol listesi 8/8. Sayfa nötr portresine yüz kor. 0,78, ten ΔE 9,7, hoodie 4,9, saç 5,1. Kafa 20° dönük olduğu için kor. aynı açıdaki düzenleme eşiğinin (0,84) altında; kimlik göz incelemesinde aynı kişi. Bakış istenenin TERSİ (kadraj solu).
- **T-M KABUL** (MAHajIzpXBs): 8/8, kor. 0,83, ten ΔE 5,3, flanel 7,6, tişört 1,6, saç 5,2. Bakış kadraj solu → **Mike aynalandı** (aynalama yasağı Leo'nun saati içindi; Mike'ta asimetrik kimlik öğesi yok, Jake'in saç yönü aynalanmaz). İkilide Mike solda, Jake sağda.
- **Kesim:** M4 (`kes-m4.py`) T-J'de lacivert omzu yedi (kenar artığı 0,174; ışıklı omuz zemine ΔE 7,6) → ELENDİ. Yeni `araclar/kes-gc.py`: Lab tohumlu GrabCut, gövdede σ7 kontur yumuşatma, T-J'de dışbükey zarf, zemin cebi temizliği (Mike 9.412 px), saç saçağının rengini saç tonuna çekme. Yeşil önizleme temiz. İki koşu birebir aynı (`cmp`).
- **Yerleşim** (`araclar/yerlesim.py`): tezgâh ön katmanında dikdörtgenle başlatılan GrabCut blok verdi → elle çizilmiş bölge ve tohumla yeniden yapıldı. İlk ikilide Mike 0,50'de Jake'ten kısa göründü → 0,55'e çıktı, Jake 0,58 önde; açıkta kalan kesik pikseli 0.
- **İfade portreleri** (`araclar/ifade-hazirla.py`): sayfa kartı → Lanczos 1080 + keskinleştirme → kes-gc → ten Lab eşleme (Jake ΔE 2,7–5,1 → ≤1,4; Mike 5,3–9,9 → ≤2,3). Tezgâh arkasına baş-omuz olarak yerleştirince dev kafa ve gri hale çıktı → RED. Düzeltme: alfa 2 px içeri, Mike aynalı, kullanım yalnız ekstrem yakın plan. Boyunda ton basamağı (ten maskesi satırdan kesilmişti) → tüm ten maskesine geçildi, giderildi. ESRGAN x4, başka ajanların ağır CPU işiyle çakıştığı için durduruldu. Yeniden üretim: `tools/karakter/buyut.py <kart> <çıkış> tam` (kart başına ~1–3 dk), sonra `ifade-hazirla.py`.
- **Ağız aracı** (`araclar/agiz-yama.py`): Leo a/b çiftiyle sınandı. Hiza: bölge dışı fark %0,22, dikiş %0,57. Yarı açık = DIS optik akış t=0,5 ara karesi; ilk sürümde akış yönleri ters eşlenmişti (çift ağız gölgesi) → düzeltildi, tek ağız, temiz. Deterministik (`cmp`).

## Tur 3 (2026-11-11): AG-J, AG-M
Girdi sha256: AG-J `c0df33b400eb`, AG-M `0974fc910889`.
- **AG-J KABUL** (MAHajI3OgKw): tabana tüm kare ham fark %0,56, fark kutusu yalnız ağız-çene (x 517–660, y 614–765). Kafa yerinde, kimlik aynı.
- **AG-M KABUL** (MAHajG_s9zc): tüm kare fark %0,56, ama saçta ve flanelde de küçük oynamalar var (%0,1–0,7). Yama yalnız ağız bölgesini aldığı için bunlar tabana taşınmaz.
- `agiz-yama.py`: bölge dışı fark Jake %0,03 / Mike %0,24 (kabul ≤%1), dikiş %0. Açık/yarı çene taban silüeti dışına taşmıyor (0 px). Yeni `--siluet` seçeneği: Mike'ın yama kutusundaki 1.916 ham zemin pikseli saydam yapıldı (Remotion'da mavi boyamasın). Mike yamaları aynalı. İki koşu birebir aynı (`cmp`).
- Göz incelemesi (3 durum, 1,5×): tek ağız, gölgesiz, dikiş yok; açıkta üst dişler görünüyor, gülümseme yok.

## Z3b (2026-11-11): ifade portresi kenar temizliği → GEÇTİ (kendi testim; hakem fark kontrolü bekleniyor)
- **Kök neden:** `kes-gc.py` saç saçağı adımı zemine karışmış tellerin renk tonunu saç tonuna çekip açıklığını bırakmıştı → Mike'ta kızıl, Jake'te bordo/koyu lekeler. Üstüne ikili GrabCut maskesi 4,3× büyütülmüş kartta tırtık ve kopuk uç bırakmıştı. Önceki `sac-hale-temizle.py` yalnız gri haleyi silmişti.
- **Düzeltme:** 12 portre kaynak kırpımdan `IFADE_SAC_PX=0 ifade-hazirla.py` ile yeniden üretildi (saç renk adımı kapalı) ve sonuna yeni `araclar/ifade-kenar.py` eklendi. Kenar aracının adımları:
  - kenar bandında yabancı piksel silme (gri halede s<0,22; saçta soluk tel s<0,33 & v<0,80; parlak gri s<0,18);
  - alfa kapama + açma (r=4), en büyük bileşen, delik doldurma;
  - kontur Gauss σ5 (saç) / σ3 (yüz-gövde), sonra σ2 yumuşak kenar;
  - kenardan 8 px'e kadar renk = en yakın temiz iç pikselin rengi (temiz iç: 14 px içeride ve kafada s>0,30), 8–14 px arası geçiş.
- **Ara elemeler** (göz kontrolü, 1:1):
  - v1 (renk bandı 4–8 px): tel uçlarında gri kaldı.
  - v2 (14 px): kaynak pikselin kendisi soluk olduğu için gri kaldı.
  - v3: soluk-tel kuralı boyun gölgesini yedi, boyunda çentik oluştu → kural saç yüksekliğine (üst %40) sınırlandı.
  - v4: saç konturunda ~10 px basamak → saçta σ5.
- **Ölçüm (12/12):** alfa adası 1; kafa kenar bandında gri piksel (s<0,18, kenara ≤6 px) 0; yüz içi (kenardan >30 px) eski varlığa ortalama fark 0,2–0,9 (yüz değişmedi). Boyut ve konum aynı, `yerlesim.json` / `mekan-l1.ts` değişmeden çalışır. İki koşu birebir aynı (`cmp`, 12 dosya).
- **Teslim:** `video/public/seri/bolum-001/ifade/` aynı adlar. Mike'ın `-temiz.png` dosyaları (gulen, saskin, endiseli, heyecanli) yeni sürümün kopyası. sha256: mike-heyecanli-temiz `77f705048e50`, jake-dusunceli `74ee5a42fee6`.
- **Kanıt:** `kontak-z3b.jpg` (üst: önce/sonra 1:1 yeşil zemin, Mike sağ saç-kulak ve Jake sol saç; alt: 12 portre yeşil zeminde).

## Bölüm 2 (2026-11-12): B2-G1 bisiklet + L3-A garaj yolu → KABUL. Kota 10/12.
Girdi sha256: B2-G1 `1fd7b5f4b449`, L3-A `5990fc1c22f8`. Kanıt: `kontak-b2.jpg`.
- **B2-G1 KABUL** (MAHarTobDG0): yan görünüm, bordo çelik gövde, iki lastik basık; 2× kırpımda yazı/çıkartma/logo yok.
- **L3-A KABUL** (MAHarbC_Rog): kişi yok; posta kutusunda numara yok, plakalar okunmuyor; orta şerit boş.
- **Kesim:** yeni `araclar/kes-yesil.py`. Yumuşak Lab anahtarı, yeşil sızıntı giderme, delik doldurma yok (teller arası boşluk zemin kalır). Sonuç: 1 ada, 655 px gürültü silindi. Temas gölgesi nötr koyuya çevrildi. İki koşu birebir aynı (`cmp`).
- **Şişik sürüm** (`araclar/bisiklet-lastik.py`): teker alt bölgesi temiz yan sektörün radyal lastik profiliyle boyandı. Teker alt bölgesi dışında değişen piksel 0.
  - Elenen ara sürümler (göz kontrolü 1:1):
    - aynalama: üstteki fren kaliperi alta taşındı;
    - üst kenar ölçümü ön tekerde gidona takıldı;
    - basık kalıntısı ve iç jant yayı kaldı → doygunluk + yapı tensörüyle silindi;
    - silme kutusu aynakolu yedi → yalnız taban satırlarıyla sınırlandı;
    - boyanan halka aynakol dişlerini kesti → yalnız alt bölge + geçiş bandında yalnız boş pikseller;
    - daire modeli arka tekeri 68 px kaçırdı → eksen hizalı elips, aykırı ayıklama (arka teker: 49 nokta, sapma 2,0 px); ön tekerde nokta az → daire yedeği.
  - Bilinen kalıntı: 1:1'de zincirin alt kolunda küçük bir basamak var → şişik sürüm ≤0,45 ölçek kuralı.
- **Yerleşim** (`araclar/yerlesim-b2.py`): ayrıntı ve kurallar `video/public/seri/bolum-002/VARLIKLAR.md` ve `yerlesim.json`'da. Önizlemeler kontağın alt satırında.
- **Brenda:** yeni karakter değil, bisikletin adı; görsel gerekmez.
