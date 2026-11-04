# F2 — Senaryo kararı (hakem) · 2026-11-04

İLERLEME: tamam.
**KAZANAN: S03 — "The Biggest Inheritance Ever, and Why Heirs Might Miss It"** (The Leaky Moving Truck; sütun C; Leo = nakliye ekibi şefi). Doğrulama SARI → §4 düzeltmeleriyle YEŞİL beklenir · politika YEŞİL.
**YEDEK: S01 — "History's Biggest Heists, Ranked by How Little They Needed"** (Alt-1; çalışma başlığı "Bigger Heists…" veriyle çeliştiği için yasak). Sütun A.
**Karar kesindir, Niyazi'ye sorulmaz** (Niyazi kararı 2026-10-26). §4 düzeltmeleri **F3 metin kilidinin ön koşulu**.
**SLOT: Paz 2026-11-08 12:00 ET (17:00 UTC).** K3 = F9 ONAY ≤ 2026-11-07 17:00 UTC. Kaçarsa S03 **Çar 2026-11-11 12:00 ET**'ye B yerine kayar (takvim §3 stok kuralı: A/C, Çarşamba slotunu doldurabilir). S03'ün zaman bağı yok, bu yüzden kayma maliyeti düşük (§5).
**Dürüst okuma:** Bu sefer eşitlik yok. S03 iki durumda da 0.68 önde (7.58 / 7.98). ±0.05 ağırlık oynatmasında 30/30 + 30/30 S03 çıkıyor. Uç durumda (S03 kötümser, rakipler iyimser viralite) de 0.39 önde. S01'in kazanması için viralite ağırlığının ≥0.79 olması gerekir. O noktada fark eşiğin altına düşer ve S01'i hook kuralı (9 > 7) kazandırır, puan değil. Kazananın en zayıf ölçütü **hook 7**. Bu yüzden H1 zorunlu.
**Kanıt:** `python3 -I hakem-karar.py` 2 koşu → `diff` aynı (çıktı sha256 774a24280878 ×2; betik 3a61f716ca8d; senaryolar 389c943ccdc2) → `log/hakem-karar-cikti.txt` · 3 hook adayı 34–38 kelime ≤40 · Cerulli 105+18 = 123 ≈ 124 (%0,8) → eş payı toplamın içinde · S01 rekor serisi monoton artmıyor (1.000 > 473 > 101 < 6.300 M$) → doğrulayıcının bulgusu betikle teyit edildi · KIRMIZI seçilmedi (havuzda 0).
Girdi: `senaryolar.md`, `viralite.md` [V], `on-dogrulama.md` [D], `politika-on-tarama.md` [P], `01-arastirma/kanal-ozet.md` [KÖ]. [T] = hakem yargısı, [H] = hesap.

## 1. Gerekçe (3 madde)
1. **En yüksek viralite ile en düşük düzeltilmiş risk aynı senaryoda.** Viralite 8.10, ilk 3'ün tepesi [V]. Komşu outlier'lar: AJ Osborne 953x (4,9 B abone) ve Philosophase 137x [V §2]. Politika YEŞİL, düzeltme yok [P]. Doğrulama SARI, ama iki düzeltmeyle kapanıyor: atıf Cerulli olacak ve çift sayım kaldırılacak [D]. Asıl kazanç şu: çift sayım bulgusu hook'a ters köşe olarak giriyor (§4 H1). S01'in sorunu ise tezin kendisinde, aynı ölçüde düzeltilemiyor (§3).
2. **Kanalın şu anki durumuna en uygun aday.** 1929 videosu 7. günde 208 izlenmede durdu. Önerilen akış videoyu almıyor [KÖ 1]. 3 aboneli bir kanalda ilk izlenme aramadan ve kalıcı merak sorgusundan gelir. "What happens when boomers are gone" sorgusu kalıcı. S03 ayrıca 4 ülkede kişisel konu (mirasçı ya da ev alıcısı) ve raf ömrü 8 [V]. Haber dalgasına bağlı değil. Rotasyona da uyuyor: son A/C videosu 1929 (A) idi, sıradaki C olmalı (takvim §2).
3. **Slot dayanıklılığı ve üretilebilirlik.** Hook'ta zaman bağı yok. K3 kaçarsa Çarşamba'ya kayması yeniden kayıt gerektirmez. S01'in Binance kancası 11-11'de 12 günlük olur (Gloam 1,90 M ile zaten aldı). Tek metafor (kamyon + kutular + bant) gerekiyor, tek rig karakter Leo. S01 dört ayrı tarihsel set istiyor (Bağdat savaş bağlamı kısıtlı, Tokyo, Dakka, borsa).

## 2. İlk 3: aynı ölçüt tablosu
Bileşik = 0.35 viralite + 0.15 doğrulama + 0.15 politika + 0.10 üretim kolaylığı + 0.15 kanal kimliği + 0.10 özgünlük (1929 ve S08 kararlarıyla aynı ağırlıklar). Viralite dışındaki puanlar [T].
S06 (7.50) ve S08 (7.50) ilk 3'e alınmadı. Politika uzmanı ikisini de bu slotta önermiyor [P]: S06 yayımlanmış S08 videosunun tezini tekrarlıyor, S08'de çıkar çatışması ve "üçüncü piyasa düşüşü" çizgisi var. Yerlerine bir sonraki aday S05 alındı, Alt-2 başlıkla 7.70 [V].

| Ölçüt | **S03** Leaky Truck | **S01** Heist Museum | **S05** Pressure Chamber (Alt-2) |
|---|---|---|---|
| Viralite [V] (köt.–iyi.) | **8.10** (7.60–8.40) | 8.00 (7.40–8.35) | 7.70 (Alt-2; cezasız 7.95) |
| İlk 15 sn (hook) [V] | 7 (7–8): tek rakam + vaat; ters köşe yok (H1 ile 8 hedef) | **9**: kamyon ↔ dizüstü karşıtlığı | **9**: paradoks; ama karşıtlık bozuk (JGB de 30 yılın zirvesinde [D]) |
| Doğrulama [D] önce/sonra | SARI · 6/8: atıf (Cerulli) + çift sayım; sızıntı rakamlarının çoğu [doğrulanacak] | SARI · 5/7: **tez/başlık veriyle çelişiyor**, Binance canlı soruşturma, Mt. Gox hukuk riski, "five hours" tek kaynak | SARI · 6/8: hook karşıtlığı seviyeye çevrilmeli, +130 bp tek kaynak |
| Politika [P] önce/sonra | **YEŞİL · 9/9** | SARI · 7/8: 4 madde (soruşturma, yöntem, savaş, yüceltme) | YEŞİL koşullu · 8/8: S08 satır 119 tekrarı, "your money" repliği |
| Üretim kolaylığı [T] | 7: kamyon/kutu metaforu, şelale grafiği; kurgusal aile ek karakter riski (H4) | 6: dört tarihsel set + müze; savaş görseli yasak | 7: basınç odası + ülke kartları |
| Kanal kimliği [T] | **8**: genç mirasçı/ev alıcısı, 4 ülke, Leo bant gag'i | 7: suç teması kanalda yeni; "rekor müzesi" yüceltme tonu riski | 6: S08 bütçe videosundan hemen sonra ikinci kamu borcu videosu |
| Özgünlük [T] önce/sonra | 6/7: "boomers gone" rakip açısı yaygın; "sızıntı" çerçevesi yok; kapanış değişince 7 | 6/6: Gloam Binance'i 310x ile aldı; "biggest heists" listeleri yaygın | 5/6: OBF 8,64 M / Broke Economy kopya dalgası |
| **Bileşik önce / sonra** (betik) | **7.58 / 7.98** | 6.85 / 7.30 | 6.90 / 7.30 |
| Karar | **KAZANAN** (açık fark 0.68) | **YEDEK** | 3. (elendi) |

```
$ python3 -I hakem-karar.py   (2 koşu, diff aynı, sha256 774a24280878)
[once] S03 7.58 | S05 6.90 | S01 6.85 → S03 (açık fark 0.68) · [sonra] S03 7.98 | S01 7.30 | S05 7.30 → S03 (0.68)
±0.05 ağırlık, 30+30 durum → S03=30/30; S03−S01 en küçük fark 0.64 · uç durum → S03 (0.39) · S01 için viralite ağırlığı ≥0.79
```
**Yedek seçimi (S01 ↔ S05 'sonra' durumunda 7.30 = 7.30, hook 9 = 9):** S01 seçildi. Gerekçeler: viralite daha yüksek (8.00 > 7.70), havuzun en büyük kalıcı talebi (sorgu medyanı 2,05 M [V]), kanalda yeni bir tema. S05'in iki zayıflığı var: S08'den hemen sonra ikinci kamu borcu videosu olur [P "repetitive"] ve kopya dalgasının içinde kalır. S01 slota uyuyor (A/C). Ancak §4-Y'deki tez değişikliği olmadan devreye giremez.

## 3. Neden kaybedebilir (şeytanın avukatı)
`roast` 5 açısı elle uygulandı (eleştirmen, savunucu, analist, araştırmacı, izleyici). Skill alt ajanda giriş sorusu sorduğu için çağrılmadı (hafıza 2026-10-27).
### S03 (kazanan)
1. **Hook ilk 3'ün en zayıfı (eleştirmen).** "124 trilyon el değiştiriyor" finans medyasının klişe rakamı ("Great Wealth Transfer"). İlk 15 sn'de bir sürpriz yok. → H1: bu rakamın içinden çıkan ters köşe (18 T$ bağışa gidiyor, 54 T$ önce eşte duruyor) ilk 15 sn'ye girer. Hook F8'de yeniden puanlanır.
2. **Talep genel açıda, bizim açımızda değil (analist).** 953x outlier "boomers gone" genel sorusu, "sızıntı" değil [V talep kötümser 8]. → Başlık/thumbnail F8'de Test & Compare'e girer. Alt-1 ("Where Will the Boomers' Money Actually Go?") talebe en yakın yedek başlık.
3. **F3 rakam yükü (araştırmacı).** Bakım maliyeti, emlak vergisi eşiği, yaşam süresi, %47/%55 ve Dunham alıntısının hepsi [doğrulanacak]. → D4–D6: birincil kaynak yoksa sızıntı niteliksel kalır, rakamsız anlatılır. Düzeltilmiş tez bunu taşır ("whatever is left at the end of a long road").
4. **Genç izleyici ilgisiz kalabilir, ölüm konusu ağır gelebilir (izleyici).** "Benim mirasım yok" tepkisi. → 15–30 sn köprüsü "heir, home buyer, or both" ile kişisel bağ kurar. Ölüm soyut kalır, kurgusal aile "example" etiketi taşır [P].
5. **Tavsiye algısı (araştırmacı/politika).** Miras, vergi ve bakım konuları "planlama tavsiyesi" bölgesine yakın [K1 1311392]. → P1: yalnız mekanizma anlatılır, "you should / set up / gift now" yok.
6. **Savunucu:** zaman bağı yok, politika temiz, C rotasyonuna uyuyor, Leo'nun bant gag'i akılda kalan bir an, kayma maliyeti en düşük aday.
**Sağ kaldı mı?** Evet. 1, 3, 4 ve 5 metinle kapanıyor. 2 viralite riski, F8 testinde ölçülür. Kalan en büyük risk hook'un etkisi; ölçülmeden bilinemez.
### S01 (yedek)
1. **Tez veriyle çelişiyor.** "Bigger heists" ve "para ↑, gereken ↓" grafiği çizilemiyor: 1.000 > 473 > 101 < 6.300 M$ (betik). Çalışma başlığı, Alt-2 ve H2 yanlış. Yalnız "ne gerekti" ölçütü tutuyor.
2. **Haber kancası soğuyor.** Binance 11-08'de 10 günlük, 11-11'de 12 günlük olur. Gloam aynı olayla 1,90 M aldı. Rakam soruşturmada değişiyor (5,7–6,3).
3. **Politika SARI, 4 madde** (canlı soruşturma, "nasıl yapılır" sınırı, Bağdat savaş bağlamı, yüceltme tonu) ve Mt. Gox'ta Karpelès'e "hırsız" denemez [D].
4. Üretimi en ağır aday: dört tarihsel set, savaş görseli yasak.
### S05 (3.)
1. Hook karşıtlığı bozuk: Japonya'nın faizi de 1996'dan beri zirvede [D]. Paradoks yalnız seviye üzerinden kurulabiliyor ve bu daha zayıf.
2. Kopya dalgası: OBF 8,64 M, Broke Economy 14x. Çalışma başlığı −1.5 cezalı, yalnız Alt-2 ile seçilebilir [V].
3. S08 bütçe videosundan hemen sonra ikinci kamu maliyesi videosu ve satır 119'un tekrarı [P]. Kanalda "aynı konu" deseni oluşur.

## 4. Zorunlu F3 düzeltme listesi (S03; senaryo-yazari uygular, finans-dogrulayici ‖ monetizasyon-uyum-uzmani yeniden ölçer, hedef iki taramada YEŞİL)
**Tez düzeltmeleri / doğrulama [D]:**
- **D1. Atıf.** "Bank of America says" yasak. Doğrusu: "Cerulli Associates estimates, through twenty forty-eight" (gerekirse "cited by Bank of America"). Kaynak Cerulli basın bülteni (Ara 2024). Dönem (2048) ekranda ve metinde geçer. Vaat cümlesindeki "BofA'nın rakamı" da düzeltilir.
- **D2. Çift sayım yasağı (tezin çekirdeği).** 105 T$ mirasçılara, 18 T$ bağışa gidiyor. Toplam 123 ≈ 124 (betik %0,8). 54 T$'lık eş payı **bu toplamın içinde** ve bir **gecikme**, kayıp değil: para önce eşe, sonra çocuklara gider. Sızıntı 3 "detour/delay" olarak anlatılır. "124 − 54 − 18 = 52" gibi bir çıkarma metne, grafiğe ve Shorts'a girmez. Bağış (18) ise başlık rakamının mirasçıya gitmeyen kısmıdır ve böyle söylenebilir. Okafor şelalesi 124'ten değil, ailenin kendi örnek servetinden başlar. Kontrol `03-metin/veri/hesap.py`'de assert ile yapılır.
- **D3. "Biggest handover of money ever"** → "often called the biggest…" (yorum [T]). Başlıktaki "Ever" için F8'de paketleyici yedek başlık hazırlar (risk §6).
- **D4.** %47 / %55 (BofA Study of Wealthy Americans): yayın tarihi ve örneklem birincil kaynaktan teyit edilir. Teyit edilemezse Shorts 2 kancası ve 4. bölümdeki çubuk grafik çıkar.
- **D5.** Sızıntı rakamları (bakım maliyeti, emlak vergisi eşiği, yaşam süresi) yalnız birincil kaynakla girer; kaynak yoksa sızıntı rakamsız anlatılır. Vergi eşiği "as of 2026" etiketi taşır. ABD rakamı olduğu söylenir. İngiltere/Kanada/Avustralya cümlesi ancak kaynakla girer, yoksa çıkar.
- **D6.** Dunham "mirage" alıntısı birincil kaynakla teyit edilir, edilemezse düşer.
**Politika [P]:**
- **P1.** Planlama tavsiyesi yok: "you should / set up a trust / gift it now / buy" yok. Vergi, bakım ve ev yalnız mekanizma olarak anlatılır. Vergi yasası değişikliği anılırsa parti ve politikacı adı geçmez.
- **P2.** Kuşak suçlaması yok (Leo iki kuşağın kutusunu da taşır). Ölüm soyut kalır. Kurgusal aile her sahnede "example / illustration" etiketi taşır.
- **P3.** Açıklamaya yasal not + "Narration voice is AI-generated" satırı eklenir. Notta "not … legal or tax advice" vurgulanır. `sentetik_medya` kararını monetizasyon-uyum-uzmani verir.
**Kapanış biçimi değişikliği (kanal düzeyi, [P §3]):**
- **K1.** "Üç olasılık" kapanışı **yasak**: "Possibility A/B/C", "three ways this could go", "scenario one/two/three" kalıplarından hiçbiri ve üç dallı yapı yok. Yerine **varış sahnesi + envanter listesi** gelir. Kamyon varır, Leo listedeki çizik kalemleri tek tek okur. Okafor payı başlangıçtan varışa tek şelalede gösterilir (illustration). Ardından tek bir "bölünmüş tablo" kartı gelir: başlık rakamı birkaç aile için gerçek, çoğu aile için daha küçük ve daha geç. Dağılım verisi gerekiyorsa birincil kaynakla (Fed DFA vb.), yoksa kart niteliksel kalır. Gelecek yalnız cümle içinde "could / may / if" ile anlatılır, dallanma yok. Kapanış tez + bant gag'i ile biter. Kontrol: senaryo-yazari kapanış bölümünde bu kalıpları grep'ler (0 eşleşme), politika uzmanı F3'te yeniden ölçer.
**Hakem (hook / kimlik / üretim / retention):**
- **H1. Hook 3 aday (F3'te test edilir, seçim senaryo-yazari'nda, rakamlar finans-dogrulayici'de).** Hakem eğilimi **H1b**: ters köşe ilk 15 sn'de.
  - H1b (38 kelime): "About one hundred twenty-four trillion dollars is set to pass down in America by twenty forty-eight, Cerulli estimates. But eighteen trillion goes to charity, and fifty-four trillion stops at a spouse first. So what really reaches the kids?"
  - H1c (34 kelime): "One hundred twenty-four trillion dollars. That's the number everyone quotes for the boomers' money. But it's a forecast out to twenty forty-eight, and it leaks. Let's follow one family's share and count what's left."
  - H1a: eski hook, yalnız D1 + D3 düzeltmesiyle (en zayıf).
  - H1b'nin cevabı videoda D2'ye uygun verilir: "54 T$ kayboluyor" değil, "geç geliyor" denir.
- **H2.** Tez ("An inheritance isn't a number. It's whatever is left at the end of a long road.") ilk 60 sn'de ve sonda geçer.
- **H3. Retention.** Kanal tanıtımı yok. Vaat ilk 15 sn'de. İlk görsel değişim ≤3 sn (kamyon → kutudan damlayan para). Her ≤75 sn'de bir yeniden kanca (↺). Retention haritası metne yazılır. Süre 13–14 dk (≥10).
- **H4. Üretim.** Okafor ailesi rig'li karakter olmaz: etiketli kutular + siluet/ikon kullanılır. Tek tekrar eden karakter Leo (tutarlılık kapısı). F5 kritik yol testine **bant gag'i** ("I'm going to need more tape") + kutudan damlama girer. B planı: damlama Remotion parçacık katmanı.
- **H5. Abone ol animasyonu 3–4 kez:** ~3:00, ~7:30 ve kapanış köprüsünden önce. İlk 60 sn'de, sızıntı 3 ters köşesinin ve kamyon varış/şelale anının üstünde olmaz.
- **H6.** Yayın gününe bağlı sözcük yok ("this week / today / just"). Böylece 11-11 kaymasında yeniden TTS gerekmez.
- **H7. S04 ile örtüşme.** Sızıntı 5 (ev) ≤90 sn tutulur. S04'ün "satılık tabelalar sokağı" görseli kullanılmaz. S04 seri devamı olarak temiz kalır.
- **H8. Başlık.** Çalışma başlığı kalır. Alt-1 F8'de Test & Compare adayı olur. Thumbnail "WHO GETS IT?" + küçük "$124T" etiketi. Thumbnail'da "Bank of America" yazmaz.
**Yedek S01'e geçilirse zorunlu (Y):** (Y1) başlık Alt-1. Çalışma başlığı, Alt-2 ve "each one moved more" yasak. Tez "Thieves didn't get smarter. Money got lighter." yalnız "ne gerekti" ekseniyle kalır, para ekseninde "artan" grafik çizilmez. (Y2) Güvenli hook [D S01 #1] aynen kullanılır, "over five hours" düşer. (Y3) Politika (a)–(d) [P] uygulanır. Mt. Gox'ta "hackers drained it over years" denir. (Y4) Kapanışta da K1 geçerlidir. (Y5) S02 ve S07 bundan sonra en az 2 video ara verilerek planlanır.

## 5. Slot ve kontrol noktaları (koordinatör izler, `durum.md`)
| Nokta | Son saat (UTC) | Kaçarsa |
|---|---|---|
| K1 F3 metin kilidi (iki tarama YEŞİL) | 2026-11-05 16:00 | 2 düzeltme turu sonrası hâlâ YEŞİL değilse yedek S01 (§7 tetik 1) |
| K2 F7 GEÇTİ | 2026-11-07 06:00 | F9a'yı F8b ile paralel başlat (hakem kuralı) |
| **K3 F9 ONAY** | **2026-11-07 17:00** (slot −24 sa) | S03 **Çar 2026-11-11 12:00 ET**'ye B yerine kayar (takvim §3, §5). Paz 11-08 boş kalır, stok yok. Rotasyon yeniden dizilir: sonraki Pazar 11-15 A. Kayma `durum.md`'ye yazılır. Niyazi onayı gecikirse de aynı kural geçerli, otomatik yayın yok. |

## 6. Riskler (karar düzeyi)
| Risk | Olasılık [T] | Etki | Önlem / sahibi |
|---|---|---|---|
| Hook 7 → düşük ilk 30 sn tutma | orta | yüksek | H1 3 aday + F8 son viralite · senaryo-yazari, viralite-analisti |
| Çift sayım metne veya grafiğe sızar | orta | yüksek (güven) | D2 assert (`hesap.py`) + F3 grep · finans-dogrulayici |
| F3 rakam yükü K1'i kaçırır | orta | orta | D5: kaynaksız sızıntı rakamsız anlatılır · senaryo-yazari |
| "Biggest … Ever" başlığı yanıltıcı okunur | düşük | orta | D3 + F8 yedek başlık · youtube-paketleyici |
| Tavsiye algısı (miras/vergi) | düşük | orta | P1, P3 · monetizasyon-uyum-uzmani |
| Milyon hedefi: taban oranı 0/186, model güveni düşük [V] | — | — | Beklenti yönetimi: "milyon" tahmini %1–3 [T]. F12'de bu kararın sonucu kalibrasyona girer · viralite-analisti |

## 7. Karar kaydı (decision log)
- **Karar:** S03 kazanan, S01 yedek (Alt-1 + Y1–Y5), slot Paz 11-08 (K3 kaçarsa Çar 11-11). Karar veren hakem, 2026-11-04.
- **Yedeğe geçiş tetikleri:** (1) F3'te 2 düzeltme turundan sonra iki taramadan biri YEŞİL değilse; (2) D2 çözülemezse, yani Cerulli kırılımı birincil kaynakta 105/18/54 ile tutarsız çıkar ve tez kurulamazsa; (3) F5'te bant/damlama kritik yolu ve B planı tutarlılık kapısından kalırsa.
- **Seçenekler:** (a) S03 **seçildi**: en yüksek viralite, temiz politika, düzeltilebilir doğrulama, slot dayanıklılığı. (b) S01: en yüksek hook ve talep, ama tez çelişkili, politika SARI, haber soğuyor. (c) S05: kopya dalgası ve kamu borcu tekrarı.
- **Varsayımlar:** v0.2 viralite farkları <0.3 gürültü. Bu kararda fark 0.68 ve viralitenin dışından geliyor (doğrulama, politika, kimlik). Cerulli kırılımı [A] F3'te birincil kaynakla teyit edilecek.
- **Havuz:** S01 sonraki A adayı (Binance kancası olmadan da çalışır: Alt-1 + Bybit rekoru). S06 ≥4 hafta sonra (S08'e atıfla). S05 yalnız Alt-2 ile C stoku. S04 S03'ün seri devamı. S02/S07 suç ara kuralı. S08 AI çıkar çatışması nedeniyle bekler.
