# F4 görsel kol — rapor · S03 The Leaky Moving Truck
**İLERLEME:** tamam — dalga 1a + 1b + 2 değerlendirildi; varlıklar `video/public/kmiras/`.
**Karar:** 19 üretimden **18 KABUL**, 1 RED (M09 → M19 ile kapandı). **S01 hook = M10 (B)**; A elendi. Thumbnail K1/K3/K4 Leo'ları 0 ek üretimle hazır. Canva 19/20, son hak kullanılmadı.
**Kapılar:** Leo tutarlılık 4/4 ≥0,87 (eşik 0,80) · kafa hizası ≤1,4 px (M07 +4,9 px → ofset) · yazı 0 (2–3× kırpım) · kesme artığı ≤0,001 (lacivert kutular 0,017–0,019, önizlemede temiz) · stil: plaka/nesne düzlük ≥%50 (M09 41 → RED) · prompt kapısı 19/19.
Kanıt komutları (girdi sha256 ilk 12: M01 a4e6d95d5475 · M02 9b1bc7cc21b8 · M03 10e945f0d732 · M04 ce6b7659e113 · M05 6dd3f20686df · M06 3495beaf137c · M07 f6b80f773523 · M08 7e362caf4081 · M09 5c5693a15da6):
- `venv/python -I tools/gorsel/tutarlilik.py <M04–M07 + a> --ref a-konusma-kapali.png` → TÜMÜ GEÇTİ
- `araclar/kafa-hiza.py a.png M04..M07` (yeni; faz korelasyonu kafa x800–1120 y40–360) · `araclar/stil-olcum.py` · `araclar/nesne-bol.py` (yeni) + `araclar/kes-m4.py` · `araclar/kafa-degis.py` (yeni) · `araclar/prompt-kontrol.py canva-promptlari.md` → GEÇTİ
Kontakt: `kontakt/kontakt-dalga1a.jpg` (karakter sayfası + a + M01–M09 + S01 aday A) · `kontakt/thumb-kafa.jpg` · `kontakt/S01-aday-A.jpg`.

## Dalga 1a ölçümleri
| Id | Karar | Ölçüm |
|---|---|---|
| M01 kamyon | KABUL | düzlük 81,9 / doku 0,47 / kontur 2,11; plaka boş, logo yok; kesik yan / arka-açık / arka-kapalı artık ≤0,001, saçak 0 |
| M02 kutular | KABUL | ΔE hex'e kiremit 5,1 · lacivert 7,7 · yeşil 11,6; yarık köşe görünür ama ince (KOD damlama kaynağı); açık kutu kapağı zemin rengine yakın → kapalı delik doldurma (15.774 px) |
| M03 küçük nesneler | KABUL | bant dolu/ince, pano (boş), kalem + kapak, büyüteç; artık ≤0,0002 |
| M04 pano | KABUL | kor. 0,87, ΔE ten/saç/gömlek 2,4/1,5/3,5, kafa (0,3; 1,4) px; yüz bölgesi farkı 12,3 (b ağzı 8,9) → 2× yakın planda aynı yüz |
| M05 bant gag'i | KABUL | kor. 0,92, kayma (0,1; 0,6); kutu M02 yeşiline ΔE 5,7 (hex'e 15,5 → kanonik renk = M02 ölçülen) |
| M06 yarık kutu | KABUL | kor. 0,92, kayma (0,6; −0,4); kiremit ΔE 3,4 |
| M07 ince bant | KABUL (ofsetli) | kor. 0,87, ölçek %6,6, kafa **dy +4,9 px** → bu pozda rig ağız/göz yamaları +5 px aşağı |
| M08 akşam yolu | KABUL | düzlük 73,9 / doku 0,70 / kontur 0,10 (konturu az: arka plan resmi gibi; Leo kalın konturlu önde, tolere) |
| M09 kasa içi | **RED** | düzlük 41,0 / doku 1,84 / kontur 0,06 → resimsi ahşap damarı, set içinde tek stil kuralını bozar. Düzeltme **M19**: M01 referanslı, "flat panels, bold outlines, no wood grain" |

## S01 hook — ilk karar (dalga 1a, A yedek)
A (M08 + M01 arka-açık kesiği + M04): kurulabilir ama kamyon gündüz ışığında çizilmiş, gece yolunda yapıştırılmış gibi duruyor; ayrıca yol kıvrımlı, kamyon düz arka görünüşte. **Karar: A yedek.** Ana aday B (M10 entegre plaka, ref M01). M10 kabul kapısından kalırsa A ana olur, şu KOD şartlarıyla: kamyon katmanı ×0,62 + mavi ton (kasa içi hariç), kasa içinden yola sıcak ışık (radyal), alt temas gölgesi, kamyon düz şeritte x≈700–1100.

## Thumbnail kafa değişimleri (thumbnail-tasarimcisi'ne) — `thumb-leo/`
| Konsept | Dosya | Karar |
|---|---|---|
| K1 | **K1-M06-saskin.png** (M06 + d-saskin) · yedek K1b-M06-notr | seçildi; boyun eki 40 px rampa (satır sıçraması 6,0) |
| K3 | **K3b-M04-notr.png** (M04 + a) | K3-M04-dusunen **ELENDİ**: e-dusunen'in çenedeki eli kolsuz kalıyor |
| K4 | **K4-M05-saskin.png** · alternatif K4b-M05-gulumser (bezgin-mizah tonu için) | ikisi de geçerli (sıçrama 7,3); seçim thumb-test'te |
| K2 | — | koşan Leo kafa-sabit düzenlemeyle üretilemez → K4 |
Kesikler RGBA 1920x1080, a ile aynı kadraj. Kırpım 1,3×'te bile ≥1280 px (büyütme yok). Banknot, zemin ve metin KOD.

## animasyon-yonetmeni'ne teslim
- Leo: `leo/M04.png` (pano), `leo/M05.png` (bant, yeşil kutu; S20 için KOD ton yeşil → kiremit), `leo/M06.png` (yarık kutu), `leo/M07.png` (ince bant, **rig dy +5**). Rig = paket-v1 a + 1929 `rig/` yamaları.
- Nesne: `nesne/M01-{yan,arka-acik,arka-kapali}.png`, `nesne/M02-{kiremit,lacivert,yesil,kiremit-yarik,lacivert-acik}.png`, `nesne/M03-{bant-dolu,bant-ince,pano,kalem,kalem-kapak,buyutec}.png`.
- Plaka: `canva-ham/M08.png` (yol). Kasa içi M19 gelene kadar S12 testi için geçici: M08 + M01 arka-açık kesiği (Leo önde).

## Dalga 1b / 2 (kesin)
`canva-promptlari.md` (sha256 ea20dabc350d): 1b = M10 (ref MAHZ9uk7YSQ), M11, M12, M13, M19 (ref MAHZ9uk7YSQ) · 2 = M14, M15, M16 + seçmeli M17, M18 (ref MAHZ9lpnUVY). Metin v1.1 (22ba68b7750c) farkı yalnız KOD katmanında; dalga 2 prompt'larında değişiklik gerekmedi.

## Yeniden kullanım ve özgünlük
Önceki videodan yeniden kullanılan sahne görseli: **0**. Yeniden kullanılan yalnız karakter varlıkları (muaf sınıf): paket-v1 a/b, 1929 `rig/` ve `leo/` ifade kafaları (d-saskin, b-alt; thumbnail kafa değişimi).

## Dalga 1b + 2 değerlendirme (2026-11-05) — kontakt `kontakt/kontakt-dalga1b-2.jpg`
| Id | Karar | Ölçüm |
|---|---|---|
| M10 hook B | **KABUL, S01 ANA** | düzlük 69,2 / doku 0,80 / kontur 0,37; kamyon M01'e ΔE 9,0 (gece parlaklığı; ton aynı); plaka boş |
| M11 ev | KABUL (tolere) | düzlük 43,3 / doku 2,16 — yaprak dokusu; boyamsı eşiğe (26–38 / 2,6–5,2) inmiyor, kontur var (0,66). Son hak kritik değil diye harcanmadı |
| M12 gişe | KABUL | düzlük 70,5; tabela paneli ve bariyer yazısız (3×) |
| M13 nesneler | KABUL | 5 kesik; ilaç kutusu lila bölmeler zemine yakın → dikdörtgen dolgu + ΔE<12 temizlik (önizleme temiz); kum saati camı saydam |
| M14 koridor | KABUL | levhalar boş (3×), amblem yok |
| M15 okul | KABUL (tolere) | düzlük 47,4 / doku 2,22 (yapraklar); ad/bayrak yok |
| M16 nesneler 2 | KABUL | 4 kesik; saat rakamsız |
| M17 Leo büyüteç | KABUL | kor. 0,91, kafa (−1,9; +1,7) px |
| M18 dikey yol | KABUL | 1080x1920, M08 paleti |
| M19 kasa içi | KABUL | kontur 3,17 / düzlük 71,8 / doku 0,67 (M09: 0,06 / 41 / 1,84); ray delikleri düzenli, harf yok |

**S01 hook kesin karar: B (M10).** Gece ışığı tek görselde (kasadan yola sıcak ışık). A'da kamyon gündüz ışıklı, yapıştırma gibi duruyor. M10'da kamyon solda (x≈230–690): 16:9'da kamyona punch-in en çok 1,3× (doğal 1680 px); 9:16 penceresi x 156–764. Dev kutu ve "$124T" KOD olarak kasa içine (x≈330–600, y≈260–560).

## animasyon-yonetmeni'ne (video/public/kmiras/)
- Plakalar: `M08, M10, M11, M12, M14, M15, M19.jpg` (1920x1080), `M18.jpg` (1080x1920). **`M09.jpg` RED, kullanılmaz** (yerine M19). S01 kodu şu an M08 + kamyon kesiği (A) kullanıyor → M10'a geçilmeli.
- Leo pozları (doğrulanmış M4): `poz-M04` pano, `poz-M05` bant (S20 için yeşil → kiremit KOD ton), `poz-M06` yarık kutu, `poz-M07` ince bant (**rig dy +5 px**), `poz-M17` büyüteç. `ham-leo-*` yerine bunlar önerilir (saçak 0, delik listesi `05-gorsel/leo/*-kesme.json`).
- Nesneler `n-M01-*` (kamyon ×3), `n-M02-*` (kutu ×5), `n-M03-*` (×6), `n-M13-*` (poşet, fatura, bilet, ilaç, kum saati), `n-M16-*` (kutu-ev, yol saati, takvim, çerçeve).
