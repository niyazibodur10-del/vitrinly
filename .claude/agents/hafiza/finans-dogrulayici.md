# finans-dogrulayici — hafıza

## Kurallar
- Rakamın **ne olduğunu** da doğrula: kapanış mı gün içi mi, fiks mi vadeli mi, posted price mı piyasa mı, nominal mi reel mi, fiyat mı toplam getiri mi. Çelişkilerin çoğu farklı ölçülerden çıkıyor (Hunt: 49,45 $ Londra fiksi / 50,35 $ COMEX gün içi / 48,70 $ önceki gün kapanışı).
- Almanca/İngiliz uzun ölçek tuzağı: Almanca "Billion" = 10^12 = İngilizce trillion. PBS bile Rentenmark'ı "one billion" diye yanlış çevirmiş. İç tutarlılık hesabıyla sına (1 $ = 4,2 RM).
- Fed History (FRH), FRED, Fiscal Data hızlı birincil kaynak; WebFetch "verbatim quote" istemi iyi çalışır. Japan Times ücretli → Reuters/resmi veri.
- Etiket sayısı risk ölçüsü değildir: hiç `[doğrulanacak]` olmayan senaryoda da hesap hatası çıkabilir. Her kaldıraç/yüzde iddiasını betikle tekrar hesapla (30:1'de %3 = sermayenin %93'ü, %100 değil).

- Kaynağın kelimesini oku, F2 yorumunu değil: Cerulli "54 T$ spouses before eventually transferring to heirs" der, "124'ün içinde" demez → durak/gecikme diye yaz. Oranı betikle sına ("more than 50%" = 62/124 = tam %50).

## Dersler
- 2026-10-27: Hook rakamı ≥2 bağımsız kaynak; aykırıysa (ABA "%69 silver" vs ~1/3) sayısız yeniden yazım öner.
- 2026-10-27: "X yıl sonra toparlandı" (1929→1954, Nikkei 34 yıl, Cisco 25 yıl) iddialarının hepsi nominal fiyat endeksi. Metinde "price" kelimesi veya ekranda not şart, yoksa yanıltıcı oluyor.
- 2026-10-27: Haziran 2026 sonrası güncel rakamlar (TÜFE, Fed, Brent, altın) mutlaka aranır; ikincil kaynak aramayla çelişebilir.
- 2026-10-27 (F3 1929-1000-dolar, 6 DÜZELT): Birincil kaynak da yanılabilir. FRH "typically 10 percent" marjin dedi; akademik derleme (Borowiecki 2022, Smiley-Keehn, Rappoport-White) 1929 ortasında 40–50 % diyor. Fed essay'i bile tek kaynak sayılır; tarihsel "tipik" oranlarda akademik literatürü ara. F2 önerim ("as little as") metne geçmemişti → F3'te F2 düzeltmelerini tek tek grep'le.
- 2026-10-27: Alıntının bağlamını oku: FRH-BP'deki "one-third reopened" Sekizinci Bölge cümlesinin devamıydı, ulusal oran değil. WebFetch'e "önceki cümleyi de ver" de.
- 2026-10-27: Rakamlar doğru olup karşılaştırma yanıltıcı olabilir: "kutu kazandı" anlatısı, hayatta kalan bankadaki paranın da (mevduatın ≈%78'i) deflasyondan aynı kazancı aldığını söylemiyordu. Her "kazanan/kaybeden" kurgusunda karşı kapının iyi senaryosunu hesapla. "Most people…" genellemeleri (Shorts hook) kaynaksızsa düşür.
- 2026-10-27: İkincil kaynaklı analizleri (Hulbert) birincil veriyle yeniden üret: Shiller ie_data.xls (xlrd scratchpad'e pip --target) reel toplam getiri başa başını Kas 1936 verdi. BEA DBnomics yansısı → BEA'nın kendi NipaDataA.txt toplu dosyasıyla pay/payda teyidi işe yaradı. Yazıyla yazılmış sayılar için `dogrulama-kontrol.py` (sayı-kelime ayrıştırıcı + GÖRSEL eşleme) tekrar kullanılabilir.
- 2026-10-27: Sayısız anlatı cümleleri de (olay sırası: Kara Pazartesi öncesi düşüş zaten %22) tabloya girer.
- 2026-10-27 (F3 RED-1): düzeltme turunda grep sayısını satır numarasıyla oku (eski ifade değişiklik tablosunda kalır); Shorts kesimi tarih bağlamını siler → 9:16 tarih etiketi iste.
- 2026-11-02 (F2 12 senaryo): FRED fredgraph.csv?id=…, Fiscal Data API (`curl -g`, MTS Table 1/9, debt_to_penny), federalreserve.gov basın bülteni ve Shiller xls açık → güncel rakamı ikincil haber yerine birincil veriden betikle üret. Arama özetinden önce bunları dene.
- 2026-11-02: Senaryo hook'larında "ilk kez X ayında", "%X düştü" gibi zaman/yön ifadeleri seriyle çelişebiliyor (10y ilk %5 Eylül'de, rupi %5 değil %6 değil). Pencereyi de sına: "21/23 midterm" 3 aylık pencere. FRED seri başlangıçlarını kontrol et (HY OAS 2023+, GFDEGDQ 1966+, SP500 10 yıl).
- 2026-11-02 (F3 rakam tablosu S08): Aynı kavramın birden çok ölçüsü var: net faiz MTS 1,05 T$ / BEA 1,33 / brüt ~1,4; YoY MTS %8 / CBO %11. Tabloda birini seç, diğerlerini "metne girmez" satırına yaz. Analoji rakamı bozabilir: borç "kredi kartı" denirse ima faiz %3 vs kart %20+ → analoji sınırını tabloya yaz.
- 2026-11-02: OMB T7.1 = govinfo BUDGET-<yıl>-TAB-8-1.xlsx; MTS T9 30 Eyl kaydı FY2016+.
- 2026-11-02 (F3 S08 doğrulama, DÜZELT 6 küçük): Rakam tablosu önceden kilitlenince 120 sayının hepsi eşleşti; hatalar ifadeye kaydı: iki sahnede aynı kavrama farklı rakam (%3 / %3,5), "every/first/even if" gibi mutlak sözcükler, grafikte OMB tahmin yılları. Metinde kesinlik sözcüklerini ve grafik serilerinin bitiş yılını tara.
- 2026-11-04 (F2 12 senaryo): "Sıralama/evrim" tezini (bigger heists, money ↑) sıraladığın rakamlarla sına: kronolojik dizi monoton değilse başlık ve grafik yanlış. Paradoks hook'unda karşı tarafın da aynı yönde hareket edip etmediğine bak (Fransa faizi ↑ ama JGB de 30 yılın zirvesi) → karşıtlığı seviyeyle kur.
- 2026-11-04: Manşet rakamın asıl sahibini bul (124 T$ = Cerulli, BofA aktarıyor) ve neyi içerdiğini sına: eş/bağış payı rakamın içindeyse "sızıntı" çift sayımdır. Haber rakamı "etkilenen varlık" mı "çalınan" mı ayır (Binance 6,3). Wikipedia tarihini birincil raporla (SEC OIG) değiştir.
- 2026-11-04 (F3 rakam tablosu S03): cdc.gov ve ssa.gov curl'e kapalı (≈400 B yanıt); ASPE govinfo PDF, medicare.gov, IRS newsroom, Genworth IR, Fed DFA CSV (`releases/z1/dataviz/download/dfa-*.csv`) ve SCF pdf açık. Aynı kavramın iki ölçüsü (65'te ömür 19,7 dönem / 20,5 kohort; LTC %56 / %70) → yuvarlak ortak yazım + seçileni etiketle.
- 2026-11-04 (F3 S03 doğrulama, DÜZELT 6): rakamlar %100 tablodaydı, hatalar çerçevedeydi. Üç tür: kaynağın yöntemi hakkında iddia ("forecast counts money before it's lived on"), dar kavramın geniş adla anılması ("taxes" = yalnız emlak vergisi; IRA gelir vergisi yok), Shorts'ta alt küme ima eden "of it". Her seferinde tara.
