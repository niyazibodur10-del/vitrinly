# Flip By Vote · karakter sayfaları değerlendirmesi (2026-11-10, gorsel-varlik-sanatcisi)
İLERLEME: J-A + M-A değerlendirildi → ikisi de KABUL. Sıradaki: L1-A (bkz. `canva-promptlari.md` sıra listesi).
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
