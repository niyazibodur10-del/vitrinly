# F2 — Senaryo kararı (hakem) · 2026-11-02 04:3x UTC

İLERLEME: tamam.
**KAZANAN: S08 — "If America Earned $5,400 a Month, Here's Its Budget"** (The Kitchen Table Budget, Leo = bütçe tutan ev arkadaşı). İki taramada YEŞİL.
**YEDEK: S06 — "The 5% Number That Sets Your Mortgage (It's Not the Fed)"** (The Pipe Under Your House). İki taramada YEŞİL; araştırması tamamen FRED.
**Karar kesindir, Niyazi'ye sorulmaz** (Niyazi kararı 2026-10-26). §4 düzeltmeleri **F3 metin kilidinin ön koşulu**.
**SLOT: Çar 2026-11-04 12:00 ET (17:00 UTC; ABD kış saati 1 Kas'ta başladı) hedeflenir.** Kontrol noktaları §5'te. F9 ONAY Sal 2026-11-03 17:00 UTC'ye yetişmezse S08 **Paz 2026-11-08 12:00 ET**'ye kayar. S08 bayatlamaz (FY2026 rakamları sabit), bu yüzden kayma maliyeti düşük. S09 o durumda stokta kalır.
**Dürüst okuma:** S08 ile S06 puanda eşit (fark 0.01–0.02, eşik 0.30). Kazananı kural belirledi: ilk 15 sn (hook 9 > 8). Ağırlıklar ±0.05 oynatıldığında 30/30 + 30/30 S08 çıkıyor, ama bu sonucu eşitlik bozucu kural veriyor, puan farkı değil.
**Kanıt:** `python3 -I hakem-karar.py` 2 koşu → `diff` aynı (çıktı sha256 6d3b6a9622fc ×2; betik 9bc95353a18e; senaryolar b1e046092c91) · S08 hook 37 kelime ≤40 · hook ve thumbnail rakamları MTS FY2026 ile ±%1 içinde · KIRMIZI seçilmedi (S03/S12 elendi).
Girdi: `senaryolar.md`, `viralite.md` [V], `on-dogrulama.md` [D], `politika-on-tarama.md` [P], `01-arastirma/rakip-ozet.md` [RÖ]. [T] = hakem yargısı, [H] = hesap.

## 1. Gerekçe (3 madde)
1. **Eşit puanda en güçlü ilk 15 sn ve en sağlam rakamlar.** Hook 9 (ilk 3'ün en yükseği [V]). Hook'taki her rakam MTS birincil verisinden: gelir 5.403,3, gider 7.395,8 milyar $ [D §4] → "5,400 / about 7,400" (betik ±%1 OK). S06'nın hook'unda olgu hatası var ("This October… first time"; doğrusu 16 Eyl [D]). S01'de [1K] rakam sayısı en yüksek.
2. **Wednesday slotunu tutturma şansı en yüksek, kayarsa da en az kaybeden aday.** Tek mekân (mutfak masası, zarflar, buzdolabı notları), üretim kolaylığı 9 [T]. Raf ömrü 8 [V]. Hook'ta "just/this week" gibi bir zaman bağı yok, bu yüzden Pazar'a kayarsa yeniden kayıt gerekmez. S06'nın kancası 10 yıllık faizin yayın günü ~%5 civarında olmasına bağlı (29 Eki 4,98 [D]).
3. **Talep kanıtı ve kanal kimliği.** Son 30 günün 2. büyük B kümesi borç/faiz krizi: 3 kanalda 10–11x [RÖ özet 2]. C3 medyanı 323 K [KH]. Leo "bütçe tutan ev arkadaşı" rolünde: genç kitleye en yakın ölçek, danışman değil, kaybeden değil [senaryolar §2]. Eksi tarafı: talep 6, S06'nın 8'inin altında [V]. Bu fark viralite puanında zaten var (7.25 vs 7.50).

## 2. İlk 3: aynı ölçüt tablosu
Bileşik = 0.35 viralite + 0.15 doğrulama + 0.15 politika + 0.10 üretim kolaylığı + 0.15 kanal kimliği + 0.10 özgünlük (1929 kararıyla aynı ağırlıklar). Viralite dışındaki puanlar [T].

| Ölçüt | **S08** Kitchen Table | **S06** Pipe | **S01** Storm Chaser |
|---|---|---|---|
| Viralite [V] (köt.–iyi.) | 7.25 (6.90–7.75) | **7.50** (6.75–7.75) | 7.25 (6.70–7.80) |
| İlk 15 sn (hook) [V] | **9**: ölçek + somut iki rakam + açık döngü | 8: karşıtlık, ama olgu hatası (Ekim → 16 Eyl) | 8: şok rakam + vaat |
| Doğrulama [D] önce/sonra | YEŞİL · 8/9: hepsi MTS/Debt to the Penny [B]; 2 seri sınırı (1966, BEA≠MTS) | YEŞİL · 8/9: tamamı FRED [B]; hook + köprü düzeltmesi | YEŞİL · 7/8: çok sayıda [1K] (F/K 250, Goldman, Unitree); ABD tarafı bilançoyla güncellenecek |
| Politika [P] önce/sonra | YEŞİL · 8/8: seçim haftasında açık konusu; kalan partizan ısı | **YEŞİL · 9/9**: düzeltme yok | YEŞİL · 8/9: skor tablosu hüküm vermesin |
| Üretim kolaylığı [T] | **9**: tek set + 3 MTS/FRED grafiği | 7: musluk→bodrum→şehir→Hazine boru ağı + dünya haritası | 6: Şanghay, Pasifik radarı; STAR 50 serisi lisans/kaynak [doğrulanacak] |
| Kanal kimliği [T] | **8**: gündelik ölçek, genç kitle, Leo ev arkadaşı | 7: güçlü mekanizma; mortgage merceği daha yaşlı ev sahibine dönük | 7: fırtına avcısı iyi; konu hisse/endeks ağırlıklı |
| Özgünlük [T] | 6: "devlet = hane" bilinen eğitici kalıp [V ÖB]; How Money Works komşu | **7**: konu WhiteBoard ile aynı (9,8x), açı farklı; Alt-1 yasak | 6: "China AI bubble burst" çok kanalda (196x/138x haber) |
| **Bileşik önce / sonra** (betik) | **7.64 / 7.79** | 7.62 / 7.78 | 7.04 / 7.34 |
| Karar | **KAZANAN** (eşit, hook) | **YEDEK** | 3. (elendi) |

```
$ python3 -I hakem-karar.py   (2 koşu, diff aynı, sha256 6d3b6a9622fc)
[once] S08 7.64 | S06 7.62 | S01 7.04  → kazanan S08 (eşit (<0.30), hook belirledi)
[sonra] S08 7.79 | S06 7.78 | S01 7.34  → kazanan S08 (eşit (<0.30), hook belirledi)
[once|sonra] ±0.05 ağırlık, 30 durum → S08=30; S06-S08 en büyük |fark| 0.17 / 0.16; S08 dışı kazanan: yok
hook S08: 37 kelime ≤40 OK · gelir 5403 / gider 7396 / açık 1992.5 → '-$2,000/MO' OK · faiz/gelir %19.5 → 'one in five' OK · gider/gelir 1.369 → '$7 for every $5' OK
```
**Uç durum [H]:** S06 iyimser viralitede (7.75), S08 kötümserde (6.90) olsa bile fark 0.20 < 0.30 çıkıyor ve hook yine S08'i seçiyor. S06'yı kazandıracak tek şey kuralın kendisini değiştirmek olurdu.

## 3. Neden kaybedebilir (şeytanın avukatı)
`roast` 5 açısı elle uygulandı (eleştirmen, savunucu, analist, araştırmacı, izleyici). Skill alt ajanda giriş sorusu sorduğu için çağrılmadı.
### S08 (kazanan)
1. **Klişe analoji (eleştirmen).** "Devlet bir aile değildir" iktisatçıların bilinen itirazı. Video kendi analojisine yenilirse güven kaybeder. → H2: "aile değil" bölümü gerçek içerik olacak (kendi parası, dolar borcu, vergi yetkisi), tez cümlesi analojinin sınırını baştan söyleyecek.
2. **Seçim ertesi partizan ısı (izleyici).** 4 Kas, ara seçimin ertesi günü. Açık videosu suçlama yorumlarını çeker. → P1–P3. Seçim sonucu ve parti anılmaz.
3. **Talep en düşük olan (analist).** Rakip outlier'ı 3,0x [V]. Arama tarafı S06'dan zayıf. → Thumbnail "-$2,000/MO" + başlık F8'de Test & Compare'e girer. Borç/faiz kümesi [RÖ] destekliyor ama kanıt dolaylı.
4. **Korku dili (araştırmacı).** "Debt spiral/default" çerçevesi How Money Works'ün açısı. → D6/P2: yalnız "possibility" ve karşı kanıtla.
5. **Ölçek kafa karıştırır (izleyici).** "$1/ay = 1 milyar $/yıl" anlaşılmazsa rakamlar keyfi görünür. → D1: ekranda tek satır ölçek notu, 1. bölümde bir kez sesli.
**Sağ kaldı mı?** Evet. 1, 2, 4 ve 5'in metinle kapanan panzehiri var. 3 viralite riski, F8 testinde ölçülür.
### S06 (yedek)
1. **Ters köşe şu an zayıf:** Fed 16 Eyl'de artırdı, 28 Eki'de 2 üye artış istedi [D]. "It's not the Fed" diyen izleyiciye "ama Fed artırıyor" itirazı hazır. Köprü 2024 vakasına muhtaç.
2. Hook olgu hatası (düzeltilebilir). Yayın günü faiz %5'in belirgin altındaysa kanca ve thumbnail "5%" zayıflar.
3. Aynı konuda WhiteBoard 9,8x: başlık/thumbnail kalıp cezası her an devreye girebilir (Alt-1 −1.5 [V]).
4. Mortgage merceği ABD ev alıcısına daralıyor (kişisel 7–8 [V]).
### S01 (3.)
1. "AI bubble" doymuş (≥2x oranı %11 [RÖ]). Haber kanalları 196x ile önde, biz geç kalmış görünürüz.
2. [1K] rakam yükü + STAR 50 grafik verisi kaynak/lisans belirsiz. F3 yükü en ağır.
3. Bayatlama: 26 Eki verisi 4 Kas'ta 9 günlük olur. Kayma olursa ≤10 gün kuralı sınırda kalır.
4. Hisse/endeks + "Is America next?" = AI maskotun piyasa yönlendirmesi okuması S06/S08'den yüksek.

## 4. Zorunlu F3 düzeltme listesi (S08; senaryo-yazari uygular, finans-dogrulayici ‖ monetizasyon-uyum-uzmani yeniden ölçer, hedef iki taramada YEŞİL)
**Doğrulama [D]:**
- **D1.** Ölçek: hane $/ay = federal milyar $/yıl. Ekranda tek satır not ("$1 a month here = $1 billion a year"), `03-metin/veri/hesap.py`'de türetilir. "FY2026 (Oct 2025–Sep 2026), Monthly Treasury Statement" etiketi her bütçe grafiğinde.
- **D2.** Hook rakamları aynen kalabilir ("five thousand four hundred… about seven thousand four hundred"). Gider için "about" zorunlu (7.395,8).
- **D3.** Faiz: hane faturası **MTS net faiz** 1.051,8 milyar $ (= ~1.050 $/ay, gelirin %19,5'i). BEA `A091RC1Q027SBEA` (1.328,8) aynı ekrana girmez. Tarih grafiği gerekiyorsa seri adıyla ayrı etiketlenir.
- **D4.** Borç/GSYH tarihi: `GFDEGDQ188S` 1966'da başlıyor. "1946 sonrası düşüş" için OMB Historical Table 7.1 kullanılır. Bulunamazsa 1946 örneği çıkar.
- **D5.** Borç: toplam 40,17 T$ (hane ~482 bin $) **veya** halkın elindeki 32,43 T$ (~389 bin $). Biri seçilir, ekranda adıyla yazılır, ikisi karıştırılmaz.
- **D6.** "Eski ucuz borç pahalıyla yenileniyor" [T] mekanizması birincil veriyle desteklenir (Treasury "Average Interest Rates on U.S. Treasury Securities"; 10 yıllık için DGS10 satırları [D §4 S06]). Veri bulunamazsa cümle mekanizma olarak kalır, rakam kullanılmaz. Fed bağlamı gerekirse tek cümle: 28 Eki %3,75–4,00 sabit.
- **D7.** Default/"debt spiral" yalnız olasılık olarak geçer ve karşı kanıt verilir (kendi para birimiyle borçlanma, vade yapısı). Kesin hüküm yok.
**Politika [P]:**
- **P1.** Parti, başkan, aday adı, rengi veya yüzü yok. Açık için suçlama ("who caused it") yok. Ara seçim sonucuna atıf yok (yayın seçimin ertesi günü).
- **P2.** "Debt spiral" korku dili yalnız "possibility" (D7 ile birlikte) [P S08].
- **P3.** Kapanıştaki üç olasılık (büyüme / vergi-harcama / enflasyonla eritme) tarih ve mekanizma olarak sunulur. "Your money / you should / protect yourself" yok. Enflasyon dalı herhangi bir varlık önerisine (altın vb.) bağlanmaz.
- **P4.** Açıklamada yasal not + "Narration voice is AI-generated" satırı. `sentetik_medya` kararını monetizasyon-uyum-uzmani verir (gerçekçi olmayan animasyon).
**Hakem (kimlik / özgünlük / üretim / retention):**
- **H1.** Tez ("A country isn't a family, but the interest bill works the same way") ilk 60 sn'de ve sonda geçer. Bu, analojinin sınırını baştan söyler.
- **H2.** 5:00–9:00 "aile değil" bölümü en az 3 somut fark ve ≥1 birincil veriyle işlenir, dipnot gibi geçilmez. How Money Works'ün "default" çerçevesinden ayrışma budur.
- **H3.** Retention: kanal tanıtımı yok, vaat ilk 15 sn'de (hook ✓), ilk görsel değişim ≤3 sn (Leo masada → 5.400 $ maaş zarfı). Her ≤75 sn'de ↺. Retention haritası metne yazılır.
- **H4.** F5 kritik yol testine **matruşka zarf anı** + Leo'nun masada konuşma sahnesi girer. B planı: zarflar Remotion katmanı olarak tek tek açılır.
- **H5.** S06 ile çakışma: 4. bölümdeki %5 tahvil anlatımı ≤60 sn olur, S06'nın boru/vana metaforunu kullanmaz. S06 yedek ve sonraki B adayı olarak temiz kalır.
- **H6.** Abone ol animasyonu 3–4 kez: ~2:20, ~6:15, kapanış köprüsünden önce. İlk 60 sn'de ve matruşka doruğunun üstünde olmaz.
- **H7.** Kayma güvencesi: metinde "this week/just/today" gibi yayın gününe bağlı zaman sözcüğü yok. Böylece Pazar'a kaymada yeniden TTS gerekmez.
- **H8.** Başlık: çalışma başlığı (50 kr) kalır, Alt-2 "The US Spends $7 for Every $5 It Earns. Then What?" pakette yedek durur. Thumbnail "-$2,000/MO" yanında ölçek kaynağı açıklamada yer alır.

## 5. Slot kararı ve kontrol noktaları
| Seçenek | Getiri | Risk [T] | Karar |
|---|---|---|---|
| A) Çar 11-04 17:00 UTC (B) | Seçim ertesi gün, B rotasyonu korunur, stok boşluğu oluşmaz | 60,5 sa var, F9 ONAY için 36,5 sa (takvim 24 sa kuralı). 1929'da aktif çalışma ~5 sa sürdü, toplamda 25,5 sa (3 oturum limiti boşluğu) [ortak-dersler]. F3–F9 için ~16–20 sa bekleniyor → ~16 sa pay | **SEÇİLDİ** |
| B) Doğrudan Paz 11-08 | Rahat takvim | Çar slotu boş kalır (stok yok), Pazar'ın A'sı (S09) ertelenir | yalnız kaymada |
**Kontrol noktaları (koordinatör izler, `durum.md`):** K1 F3 metin kilidi ≤ 2026-11-02 16:00 UTC · K2 F7 GEÇTİ ≤ 2026-11-03 10:00 UTC · K3 F9 ONAY ≤ 2026-11-03 17:00 UTC. **K3 kaçarsa** S08 Paz 11-08 12:00 ET'ye kayar. Bu takvim §5'teki B kaymasıdır, ama S08'in haber bağı yok ve rakamları FY2026'ya sabit, bu yüzden ≤10 gün kuralı kısıt yaratmaz. S09 sonraki A/C Pazar'ına (11-15) geçer. Kaymayı `durum.md`'ye yazın. Niyazi'nin onayı gecikirse aynı kural uygulanır, otomatik yayın yapılmaz.

## 6. Riskler (karar düzeyi)
| Risk | Olasılık [T] | Etki | Önlem / sahibi |
|---|---|---|---|
| Oturum limiti zinciri K3'ü kaçırır | orta | düşük (S08 kayabilir) | §5 kaymasının maliyeti düşük · koordinatör |
| Seçim ertesi partizan yorum / reklam verenin çekinmesi | orta | orta | P1–P3; yorum moderasyonu F11 sonrası · monetizasyon-uyum-uzmani |
| Talep zayıf, CTR düşük | orta | orta | H8 + F8'de 3 thumbnail ile Test & Compare · thumbnail-tasarimcisi |
| Analoji eleştirisi ("government ≠ household") | orta | düşük-orta | H1, H2 · senaryo-yazari |
| Viralite modeli v0.1, kalibrasyon yok; S06–S08 sırası belirsiz | — | — | F12'de bu çiftin gerçek sonucu kaydedilir · viralite-analisti |

## 7. Karar kaydı (decision log)
- **Karar:** S08 kazanan, S06 yedek, slot Çar 11-04 (K3 kaçarsa Paz 11-08). Karar veren hakem, 2026-11-02. **Geri dönüş tetikleri (yedek S06):** (1) F3'te 2 düzeltme turundan sonra iki taramadan biri YEŞİL değilse; (2) P1–P3 seçim haftasında politika uzmanınca SARI'ya çıkarsa; (3) F5'te mutfak seti ve B planı tutarlılık kapısından kalırsa. S06'ya geçilirse zorunlu düzeltmeler: hook'ta "This fall", köprüde 2024 vakası (Fed indirdi, DGS10 3,65 → 4,79 [D]), "around five percent" + ekranda tarihli değer, Alt-1 başlığı yasak.
- **Seçenekler:** (a) S08 **seçildi** (eşit puan, hook + slot dayanıklılığı); (b) S06 (en yüksek viralite ve politika, ters köşe şu an zayıf, bayatlama orta); (c) S01 (en düşük bileşik, F3 yükü ağır).
- **Varsayımlar:** v0.1 viralite farkları (<0.3) gürültü. MTS FY2026 rakamları revize edilmez. Ara seçim sonucu metni etkilemez.
- **Havuz:** S06 sonraki B adayı (≥1 hafta ara, Ö7), S09 Pazar A stoku, S02/S04/S10 B/C stoku. S03 (çıkar çatışması) ve S12 (KIRMIZI) havuzdan düşer.
