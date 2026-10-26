# Canva'da üretilen görseli tam çözünürlükte repoya indirme

Doğrulandı: 2026-10-26 (gorsel-varlik-sanatcisi). Sonuç: `uretim/canva-testi/test2-mutfak-tam.png` = **1920x1080 PNG** (2,5 MB).

## Neden dolaylı yol?
- `generate-image` / `get-generate-image-job` yalnız **media id** döndürür (tasarım yok); önizleme 199x112.
- `get-assets` gerçek boyutu söyler (Canva üretimleri: **1680x944**, 16:9) ama thumbnail URL'si imzalı:
  `width/height` parametresini değiştirmek → **403 "Signature invalid"** (denendi).
- Tek resmi çıkış yolu `export-design` → görselin bir **tasarım sayfasında** olması gerekir.

## Kalıcı çalışma tuvali
Canva tasarımı **`DAHZHv3mU9w`** — "FR export tuvali 1920x1080" (custom 1920x1080, Niyazi'nin hesabında).
Oluşturma: `resize-design` (Niyazi'nin tek sayfalık eski bir tasarımından `custom 1920x1080`; orijinal değişmez,
yeni tasarım döner). Yapay zekâ hakkı harcamaz. Sayfalar: 1 = mutfak testi, 2–7 = paket-v1 a–f, 8–9 = adaylar.

## Adımlar (her yeni görsel için)
1. `get-assets [media_id]` → boyutu kontrol et (16:9 değilse sayfa boyutunu görsel oranına göre seç).
2. `read-design DAHZHv3mU9w open_transaction=true` → `transaction_id`.
3. `edit-design` (keep_open): `add_page {width:1920,height:1080,title:"<ad>"}` (birden fazla olabilir).
4. `read-design` (aynı transaction_id, `design_content`, `page_indices:[yeni]`) → yeni sayfa id'leri
   (not: `page_metadata` kaydedilmemiş sayfaları göstermez; `design_content` gösterir).
5. `edit-design` (keep_open): her sayfa için `insert_fill {page_id, asset_type:"image", asset_id:<media_id>, top:0,left:0,width:1920,height:1080}`.
   Tek çağrıda birden çok sayfaya eklenebilir. 1680x944 görsel "cover" ile yerleşir: yanlardan ~2 px kırpılır.
6. `edit-design finalize="commit"` (export kaydedilmiş sürümü okur).
7. `export-design {type:"png", width:1920, height:1080, lossless:true, pages:[...]}` → sayfa başına imzalı S3 URL'si.
8. `curl -sS -o <hedef>.png "<url>"` (URL saatler içinde düşer; hemen indir) → `file <hedef>.png` ile 1920x1080 doğrula.

## Sınırlar / notlar
- Doğal çözünürlük **1680x944**; 1920x1080 export Canva'nın ×1,14 yeniden örneklemesidir (yeni detay yok).
  ≥2048 px karakter gerekiyorsa: export'u 1920x1080 al, sonra `tools/karakter/buyut.py` (Real-ESRGAN x4).
  Export'ta `width:3840` da verilebilir ama bu da yalnız yeniden örnekleme.
- `create-design` (brief'ten üretim) kullanma: üretken araçtır, yapay zekâ hakkı harcayabilir ve sayfayı doldurur.
- `edit-design commit` geri alınamaz; yalnız bu çalışma tuvalinde yapılır, Niyazi'nin tasarımlarında yapılmaz.
- 9:16 için aynı yol: ayrı sayfa `add_page {width:1080,height:1920}` + görseli 9:16 üretip yerleştir.
