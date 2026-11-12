# Bölüm 002 görsel varlıkları (gorsel-varlik-sanatcisi, 2026-11-12)
Kaynak: Canva AI (Niyazi aboneliği). Ham dosyalar ve prompt'lar `uretim/seri/karakter/` altında (B2-G1, L3-A). Sayısal yerleşim `yerlesim.json` içinde. Kanıt: `uretim/seri/karakter/kontak-b2.jpg`.

| Dosya | Ne | Kaynak |
|---|---|---|
| plaka/L3-A.png | Garaj yolu, gündüz, 1080x1920, kişi/yazı yok | MAHarbC_Rog |
| nesne/bisiklet-basik.png | "Brenda": 1980'ler çelik yol bisikleti, lastikler basık, RGBA, 1600x917 | MAHarTobDG0 |
| nesne/bisiklet-sisik.png | Aynı bisiklet, lastikler şişik (kodla). Aynı tuval ve hizada, temas gölgesi pişmiş. | basık sürümden türetildi |
| nesne/bisiklet.json | Teker merkezleri, yarıçaplar, zemin satırı (basık 859, şişik 883) | — |
| Mutfak, karakter, ağız, ifade | Bölüm 1'den referansla: `../bolum-001/plaka/`, `karakter/`, `agiz/`, `ifade/` (kurallar `../bolum-001/VARLIKLAR.md`) | — |

## Yerleşim
- **Geniş L3 (S6):**
  - Bisiklet ölçek 0,33, ortada, zemin y=1250. Basık için xy (276,967), şişik için (276,959); takasta yalnız y değişir.
  - Ölçek garaj yolu genişliğinden geliyor: y≈1260'ta ~1060 px ≈ 3,2 m, yani ~330 px/m; bisiklet ≈1,7 m.
  - Derz çizgisi y=1408, ufuk/garaj tabanı y≈600.
- **Yakın L3 (S6 replikleri):**
  - Plaka L3-A 1,3× yakınlaştırılır (çapa 540,600) ve σ4 bulanıklaştırılır.
  - Taban ölçek 1, (0,0). Kesik kollar kadraj kenarında, alt kenar kadraj altında; ön katman gerekmez.
  - Ağız yamaları bölüm 1'deki konumlarda.
- **Portre (L3):** plaka 1,6× (540,700) + σ6; konumlar `../bolum-001/yerlesim.json` → `ifade_tekli`.
- **S1 mutfak girişi:**
  - Bölüm 1 tekli Mike düzeni.
  - Bisiklet ölçek 0,7, zemin y=1945, x 1080→430 kayar, ±8 px zıplama.
  - Katman: `tezgah-on` ÜSTÜNDE (kameraya en yakın).
- **Şişik sürüm** en çok 0,45 ölçekte kullanılır (geniş plan, ilan kartı). 1:1'de zincirin alt kolunda küçük bir basamak var. Yakın planda basık sürüm kullanılır.
- **Işık:** bisiklet nötr stüdyo ışığında, L3 sıcak öğleden sonra güneşinde. Gerekirse bisiklete hafif sıcak ton verilebilir (animasyon kararı).
