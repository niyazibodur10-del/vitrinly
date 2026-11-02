// TEK KAYNAK zaman planı (animasyon-yonetmeni): sahne kodu, efekt cue'ları (06-muzik/animasyon-efekt-cue.json) ve
// ağzın göründüğü aralıklar (07-animasyon/agiz-gorunur.json) bu fonksiyonlardan üretilir → hiçbiri kayamaz.
// Saf TS (React yok): 07-animasyon/olay-cikar.mjs esbuild ile paketleyip node'da çalıştırır.
// Zamanlar sahne YEREL saniyesi; kelime çapası (an(id)("word", n)) — ses değişince kendini günceller, eksik kelime hata fırlatır.
import { SAHNELER } from "./veri-sahne";

export type Olay = { t: number; olay: string; tur: string; oneri?: string };
export type Kes = [t: number, ad: string, leo?: boolean];
export type Plan = { k: Record<string, number>; olay: Olay[]; agiz: [number, number][]; kes?: Kes[] };

const norm = (w: string) => w.toLowerCase().replace(/[\u2018\u2019]/g, "'").replace(/[^a-z0-9$'-]/g, "");
export const sure = (id: string) => SAHNELER.find((s) => s.id === id)!.sure;
export const an = (id: string) => {
  const s = SAHNELER.find((x) => x.id === id)!;
  // "five|$5": alternatifler (hizalı metin yazıyla, ham Whisper rakamla yazabilir) — ilk bulunan
  return (w: string, n = 1, son = false): number => {
    for (const alt of w.split("|")) {
      const hedef = norm(alt);
      let say = 0;
      for (const k of s.kelimeler) if (norm(k.w) === hedef && ++say === n) return son ? k.e : k.s;
    }
    throw new Error(`${id}: kelime yok: ${w} #${n}`);
  };
};
// Abone anları (metin ABONE-1..3): sahne sonundaki 1,5 sn nefesin başı (son kelime bitişi + 0,15)
export const ABONE_SAHNE = ["S07", "S12", "S26"] as const;
export const aboneAn = (id: string) => {
  const s = SAHNELER.find((x) => x.id === id)!;
  return s.kelimeler[s.kelimeler.length - 1].e + 0.15;
};


// Kesme listesinden plan: ağız aralıkları = Leo'nun konuştuğu kesmeler; her kesme bir SFX olayı
const yap = (id: string, k: Record<string, number>, kes: Kes[], olay: Olay[] = []): Plan => {
  const S = sure(id);
  kes.forEach((c, i) => {
    if (i && c[0] <= kes[i - 1][0] + 0.4) throw new Error(`${id}: kesme sırası/aralığı bozuk: ${kes[i - 1][1]} → ${c[1]} (${kes[i - 1][0].toFixed(2)} → ${c[0].toFixed(2)})`);
  });
  if (kes.length && S - kes[kes.length - 1][0] < 0.4) throw new Error(`${id}: son kesme sahne sonuna çok yakın`);
  const agiz: [number, number][] = [];
  kes.forEach((c, i) => {
    if (c[2]) agiz.push([Math.max(0, c[0]), i + 1 < kes.length ? kes[i + 1][0] : S]);
  });
  const ko: Olay[] = kes.map((c) => ({ t: Math.max(0, c[0]), olay: `kesme: ${c[1]}`, tur: "kesme", oneri: c[0] <= 0.01 ? "sahne geçişi (yumuşak whoosh)" : "kısa whoosh" }));
  return { k, kes, olay: [...ko, ...olay].sort((a, b) => a.t - b.t), agiz };
};

const P: Record<string, () => Plan> = {
  S01: () => {
    const a = an("S01");
    const k = {
      ev: 1.9,
      brings: a("brings"),
      five: a("five|$5"),
      spends: a("spends"),
      seven: a("seven|$7"),
      eksi: a("let's") - 0.9,
      lets: a("let's"),
      gap: a("gap"),
      son: sure("S01"),
    };
    return {
      k,
      olay: [
        { t: 0, olay: "Capitol silüeti tam ekran, küçülmeye başlar", tur: "kart", oneri: "alçalan whoosh" },
        { t: k.ev, olay: "Capitol → masadaki ev maketi (pop) + Leo masaya oturur", tur: "pop", oneri: "tahta tık / sandalye" },
        { t: k.brings + 0.1, olay: "maaş zarfı masaya düşer ($5,400 IN)", tur: "dus", oneri: "kâğıt düşme" },
        { t: k.five, olay: "sayaç 0→5,400 (0,8 sn)", tur: "sayac", oneri: "tıkırtı + ding" },
        { t: k.spends - 0.1, olay: "kesme: buzdolabı yakın plan", tur: "kesme", oneri: "whoosh" },
        { t: k.seven, olay: "not yapışır: $7,400 OUT", tur: "pop", oneri: "yapışkan not tap" },
        { t: k.eksi, olay: "kırmızı −$2,000/MO notu yanıp söner", tur: "vurgu", oneri: "alarm tik ×3" },
        { t: k.lets - 0.1, olay: "kesme: masa, Leo'ya yavaş punch-in", tur: "kesme", oneri: "" },
      ],
      agiz: [
        [k.ev + 0.35, k.spends - 0.1],
        [k.lets - 0.1, k.son],
      ],
    };
  },
  S12: () => {
    const a = an("S12");
    const k = {
      watch: a("watch"),
      open: a("open"),
      inside: a("inside", 1),
      borrowed: a("borrowed", 1),
      heres: a("here's"),
      gap: a("gap"),
      half: a("half"),
      so1: a("so", 1),
      newm: a("new"),
      so2: a("so", 2),
      i2: a("inside", 2),
      i3: a("inside", 3),
      i4: a("inside", 4),
      i5: a("inside", 5),
      son: sure("S12"),
      abone: aboneAn("S12"),
    };
    return {
      k,
      olay: [
        { t: 0.25, olay: "kırmızı INTEREST zarfı masaya kayar", tur: "kay", oneri: "kâğıt kayma" },
        { t: k.watch - 0.05, olay: "punch-in Leo + zarf", tur: "kamera", oneri: "whoosh kısa" },
        { t: k.open, olay: "zarf açılır: içinden mor zarf (Leo G05)", tur: "vurgu", oneri: "zarf yırtma / kâğıt" },
        { t: k.borrowed, olay: "BORROWED etiketi pop", tur: "pop", oneri: "pop" },
        { t: k.heres - 0.05, olay: "kesme: AÇIK çubuğu kartı ($2,000)", tur: "kesme", oneri: "" },
        { t: k.half, olay: "çubuğun kırmızı faiz kısmı dolar: 53% OF THE GAP", tur: "sayac", oneri: "yükselen ton" },
        { t: k.so1 - 0.05, olay: "kesme: Leo zarflar ters renk (mor dış, kırmızı iç)", tur: "kesme", oneri: "" },
        { t: k.so2 - 0.05, olay: "kesme: kuşbakışı masa, matruşka başlar", tur: "kesme", oneri: "whoosh" },
        { t: k.i2, olay: "matruşka 1: mor zarftan kırmızı zarf çıkar + punch-in", tur: "vurgu", oneri: "kâğıt + tık" },
        { t: k.i3, olay: "matruşka 2: kırmızıdan mor zarf + punch-in", tur: "vurgu", oneri: "kâğıt + tık" },
        { t: k.i4, olay: "matruşka 3 + punch-in", tur: "vurgu", oneri: "kâğıt + tık (hızlanan)" },
        { t: k.i5, olay: "matruşka 4 + punch-in", tur: "vurgu", oneri: "kâğıt + tık (hızlanan)" },
        { t: k.abone, olay: "ABONE-2 (sağ alt boş; kule sol-orta)", tur: "abone", oneri: "klik (kurgu-editoru bileşeni)" },
      ],
      agiz: [
        [0, k.heres - 0.05],
        [k.so1 - 0.05, k.so2 - 0.05],
      ],
      kes: [
        [0, "masa orta: kırmızı zarf", true],
        [k.watch - 0.05, "punch-in Leo G05", true],
        [k.heres - 0.05, "açık çubuğu"],
        [k.so1 - 0.05, "Leo G05 ters renk", true],
        [k.so2 - 0.05, "matruşka"],
      ],
    };
  },
  S02: () => {
    const a = an("S02");
    const k = { because: a("because"), starting: a("starting"), car: a("car"), mortgages: a("mortgages"), by: a("by"), fastest: a("fastest"), why: a("why", 2), three: a("three") };
    return yap("S02", k, [[0, "masa orta, Leo", true], [k.because + 0.5, "kamera pencereye kayar (Leo çıkar)"], [k.by - 0.1, "buzdolabı: sorular + A·B·C"]], [
      { t: k.car, olay: "araba ikonu + CAR LOANS", tur: "pop", oneri: "pop" },
      { t: k.mortgages, olay: "ev ikonu + MORTGAGES", tur: "pop", oneri: "pop" },
      { t: k.fastest, olay: "not: FASTEST BILL?", tur: "pop", oneri: "yapışkan not tap" },
      { t: k.why, olay: "not: WHY?", tur: "pop", oneri: "yapışkan not tap" },
      { t: k.three, olay: "üç not A · B · C", tur: "pop", oneri: "tap ×3" },
    ]);
  },
  S03: () => {
    const a = an("S03");
    const k = { one: a("one|$1"), equals: a("equals|="), these: a("these"), and: a("and"), country: a("country"), remember: a("remember"), test: a("test") };
    return yap("S03", k, [[0, "Leo yakın: I'm Leo", true], [k.one - 0.1, "ölçek kartı"], [k.and - 0.1, "masa geniş, Leo", true], [k.country - 0.1, "buzdolabı: kırmızı tez notu"], [k.remember - 0.1, "Leo yakın, ciddi", true]], [
      { t: 0.3, olay: "isim etiketi LEO", tur: "pop", oneri: "hafif pop" },
      { t: k.equals, olay: "= işareti + $1 billion a year", tur: "vurgu", oneri: "ding" },
      { t: k.these, olay: "kaynak satırı FY2026", tur: "pop", oneri: "" },
      { t: k.country + 0.1, olay: "kırmızı tez notu buzdolabına çarpar", tur: "dus", oneri: "tok tap / slap" },
    ]);
  },
  S04: () => {
    const a = an("S04");
    const k = { payday: 0.1, five: a("five|$5"), paychecks: a("paychecks"), company: a("company"), payroll: a("payroll"), thats: a("that's"), spending: a("spending"), envelope: a("envelope"), last: a("last") };
    return yap("S04", k, [[0, "kuşbakışı masa: PAYDAY"], [k.thats - 0.1, "masa orta, Leo zarfları dizer", true]], [
      { t: k.payday, olay: "PAYDAY yazısı", tur: "pop", oneri: "kasa ding" },
      { t: k.five, olay: "maaş zarfı masaya düşer $5,400", tur: "dus", oneri: "kâğıt düşme" },
      { t: k.paychecks, olay: "şerit: PAYCHECK TAXES", tur: "kay", oneri: "kâğıt çekme" },
      { t: k.company, olay: "şerit: COMPANY TAXES", tur: "kay", oneri: "kâğıt çekme" },
      { t: k.payroll, olay: "şerit: PAYROLL TAXES", tur: "kay", oneri: "kâğıt çekme" },
      { t: k.envelope, olay: "6 zarf yelpaze gibi dizilir", tur: "pop", oneri: "kart dağıtma ×6" },
      { t: k.last, olay: "kırmızı zarf kenara çekilir (?)", tur: "vurgu", oneri: "gizem tını" },
    ]);
  },
  S05: () => {
    const a = an("S05");
    const k = { social: a("social"), about1: a("about", 1), env2: a("envelope", 2), medicare: a("medicare"), about2: a("about", 2), env3: a("envelope", 3), health: a("health"), about3: a("about", 3), three: a("three") };
    return yap("S05", k, [[0, "masa orta, Leo + hesap makinesi", true], [k.env2 - 0.1, "grafik G1: gelir çubuğu dolar"], [k.env3 - 0.1, "kuşbakışı: üç zarf yığılır"], [k.three - 0.1, "grafik G1: toplam sayaç"]], [
      { t: k.social, olay: "mavi zarf SOCIAL SECURITY düşer", tur: "dus", oneri: "kalın zarf thud" },
      { t: k.about1, olay: "hesap makinesi $1,667", tur: "sayac", oneri: "tuş tıkırtısı" },
      { t: k.medicare, olay: "yeşil dilim MEDICARE $1,073 + büyük +$1,073", tur: "pop", oneri: "pop" },
      { t: k.health, olay: "açık yeşil zarf HEALTH", tur: "dus", oneri: "zarf thud" },
      { t: k.three - 0.1, olay: "kesme sonrası grafik + büyük +$1,026", tur: "pop", oneri: "pop" },
      { t: k.three + 0.3, olay: "sayaç SPENT $3,765", tur: "sayac", oneri: "tıkırtı + ding" },
    ]);
  },
  S06: () => {
    const a = an("S06");
    const k = { defense: a("defense"), ships: a("ships"), planes: a("planes"), salaries: a("salaries"), bases: a("bases"), nine: a("nine|$965"), now: a("now"), five: a("five"), interest: a("interest"), about: a("about"), that: a("makes") - 0.3, read: a("read"), alone: a("alone") - 0.5, one: a("one"), buys: a("buys") - 0.25, nothing: a("nothing"), road: a("road"), check: a("check"), ship: a("ship") };
    return yap("S06", k, [[0, "kuşbakışı: gri DEFENSE zarfı"], [k.now - 0.1, "masa orta: kırmızı zarf kendiliğinden kayar", true], [k.that - 0.1, "grafik G1b: sıralı çubuk"], [k.read - 0.1, "kuşbakışı: INTEREST > DEFENSE"], [k.alone - 0.1, "grafik: 5 dolardan 1'i"], [k.buys - 0.1, "Leo yakın: BUYS NOTHING", true]], [
      { t: k.defense, olay: "gri DEFENSE zarfı düşer", tur: "dus", oneri: "thud" },
      { t: k.ships, olay: "etiket SHIPS", tur: "pop", oneri: "tik" },
      { t: k.planes, olay: "etiket PLANES", tur: "pop", oneri: "tik" },
      { t: k.salaries, olay: "etiket SALARIES", tur: "pop", oneri: "tik" },
      { t: k.bases, olay: "etiket BASES", tur: "pop", oneri: "tik" },
      { t: k.nine, olay: "$965", tur: "pop", oneri: "pop" },
      { t: k.five - 0.1, olay: "kırmızı zarf masaya kayar (müzik kesilir)", tur: "kay", oneri: "MÜZİK KES + tek tık" },
      { t: k.interest, olay: "INTEREST yazısı", tur: "vurgu", oneri: "tek tık" },
      { t: k.about, olay: "$1,050 / MO", tur: "pop", oneri: "" },
      { t: k.that + 0.2, olay: "çubuklar sırayla dolar, INTEREST 3. sırada parlar", tur: "sayac", oneri: "tıkırtı ×5" },
      { t: k.read + 0.4, olay: "INTEREST > DEFENSE", tur: "vurgu", oneri: "vuruş" },
      { t: k.one, olay: "5 dolardan biri kırmızıya döner", tur: "vurgu", oneri: "ding" },
      { t: k.nothing, olay: "BUYS NOTHING damgası", tur: "vurgu", oneri: "damga thud" },
      { t: k.road, olay: "NO ROAD", tur: "pop", oneri: "tik" },
      { t: k.check, olay: "NO CHECK", tur: "pop", oneri: "tik" },
      { t: k.ship, olay: "NO SHIP", tur: "pop", oneri: "tik" },
    ]);
  },
  S07: () => {
    const a = an("S07");
    const k = { everything: a("everything"), veterans: a("veterans"), roads: a("roads"), food: a("food"), science: a("science"), parks: a("parks"), courts: a("courts"), about1: a("about", 1), now: a("now"), out: a("out"), in: a("in"), short: a("short"), and2: a("and", 2), loan: a("loan"), abone: aboneAn("S07") };
    return yap("S07", k, [[0, "kuşbakışı: EVERYTHING ELSE zarfı"], [k.now - 0.1, "terazi: gider ↔ gelir"], [k.and2 - 0.1, "masa orta: LOAN BOOK", true]], [
      { t: 0.15, olay: "kahve zarf EVERYTHING ELSE düşer", tur: "dus", oneri: "thud" },
      ...(["veterans", "roads", "food", "science", "parks", "courts"] as const).map((w) => ({ t: k[w], olay: `etiket ${w.toUpperCase()}`, tur: "pop", oneri: "tik" })),
      { t: k.about1, olay: "~$1,600", tur: "pop", oneri: "" },
      { t: k.out, olay: "terazi gider tarafına yatar (~$7,400 OUT)", tur: "vurgu", oneri: "ahşap gıcırtı + thud" },
      { t: k.in, olay: "$5,400 IN etiketi", tur: "pop", oneri: "" },
      { t: k.short, olay: "−$2,000 / MO kırmızı", tur: "vurgu", oneri: "alarm tik" },
      { t: k.loan, olay: "LOAN BOOK masaya kayar, +$2,000 satırı", tur: "kay", oneri: "kitap kayma + kalem" },
      { t: k.abone, olay: "ABONE-1 (sağ alt boş; defter solda)", tur: "abone", oneri: "klik (kurgu-editoru bileşeni)" },
    ]);
  },
  S08: () => {
    const a = an("S08");
    const k = { open: a("open"), decades: a("decades"), balance: a("balance"), three: a("three|about", 1), real: a("real"), thirty: a("thirty-two|$32", 1), one: a("one"), average: a("average"), theres: a("there's"), trust: a("trust"), pocket: a("pocket"), another: a("another") };
    return yap("S08", k, [[0, "masa orta: defter açılır", true], [k.balance - 0.1, "grafik G2: bakiye"], [k.one - 0.1, "Leo yakın: pahalı değil", true], [k.theres - 0.1, "kuşbakışı: cepten cebe"]], [
      { t: k.open, olay: "LOAN BOOK açılır", tur: "vurgu", oneri: "kitap açılma" },
      { t: k.decades, olay: "sayfalar masadan yere akar", tur: "parcacik", oneri: "kâğıt yağmuru" },
      { t: k.balance + 0.4, olay: "sayaç ~$389,000", tur: "sayac", oneri: "tıkırtı + ding" },
      { t: k.real, olay: "gerçek ölçek satırı $32.43 TRILLION", tur: "pop", oneri: "" },
      { t: k.average, olay: "not: ≈3–3.5% a year, not card rates", tur: "pop", oneri: "" },
      { t: k.trust, olay: "kumbara + kasa", tur: "pop", oneri: "" },
      { t: k.pocket, olay: "ok: cepten cebe", tur: "kay", oneri: "whoosh kısa" },
    ]);
  },
  S09: () => {
    const a = an("S09");
    const k = { paycheck: a("paycheck"), six: a("six"), nothing: a("nothing"), loan: a("loan"), and: a("and", 1), adding: a("adding") };
    return yap("S09", k, [[0, "Leo yakın: $389,000", true], [k.six - 0.3, "grafik G2b: 6 yıl"], [k.and - 0.1, "masa orta: defter uzar", true]], [
      { t: 0.1, olay: "$389,000 yazısı", tur: "pop", oneri: "" },
      { t: k.six, olay: "6 yıl kutusu sırayla dolar ($64,800 ×6)", tur: "sayac", oneri: "tık ×6" },
      { t: k.nothing, olay: "NO FOOD · NO RENT", tur: "pop", oneri: "" },
      { t: k.adding, olay: "+$2,000 satırı", tur: "pop", oneri: "kalem" },
    ]);
  },
  S10: () => {
    const a = an("S10");
    const k = { americans: a("americans"), pension: a("pension"), banks: a("banks"), foreign: a("foreign"), federal: a("federal"), when: a("when"), promise: a("promise"), treasury: a("treasury"), back: a("back") };
    return yap("S10", k, [[0, "masa orta: WHO HOLDS THE LOAN?", true], [k.americans - 0.1, "ikon kartları: alacaklılar"], [k.when - 0.1, "Leo yakın: IOU", true]], [
      { t: 0.2, olay: "WHO HOLDS THE LOAN?", tur: "pop", oneri: "kapı zili" },
      ...(["americans", "pension", "banks", "foreign", "federal"] as const).map((w) => ({ t: k[w], olay: `alacaklı ikonu (${w})`, tur: "pop", oneri: "kapı zili / pop" })),
      { t: k.promise, olay: "IOU fişi", tur: "pop", oneri: "kâğıt" },
      { t: k.treasury, olay: "TREASURY BOND = A PROMISE", tur: "vurgu", oneri: "" },
    ]);
  },
  S11: () => {
    const a = an("S11");
    const k = { stop: a("stop"), yes: a("yes"), hold: a("hold"), first: a("first"), strange: a("strange") };
    return yap("S11", k, [[0, "iki kredi başvurusu"], [k.hold - 0.1, "buzdolabı: soru notu"], [k.first - 0.1, "masa orta: kırmızı zarfa spot", true]], [
      { t: k.stop, olay: "DENIED damgası (aile)", tur: "vurgu", oneri: "damga thud" },
      { t: k.yes, olay: "APPROVED damgası (hane)", tur: "vurgu", oneri: "damga thud" },
      { t: k.hold + 0.1, olay: "soru notu yapışır", tur: "dus", oneri: "slap" },
      { t: k.strange, olay: "spot ışık kırmızı zarfa", tur: "vurgu", oneri: "gizem tını" },
    ]);
  },
  S13: () => {
    const a = an("S13");
    const k = { part: a("part"), rate0: a("rate"), early: a("early"), sep: a("september"), just: a("just") - 0.3, tripled: a("tripled"), kitchen: a("kitchen"), growing: a("growing") };
    return yap("S13", k, [[0, "masa orta: şişman kırmızı zarf", true], [k.early - 0.2, "grafik G3a: ortalama faiz"], [k.just - 0.1, "grafik G3b: net faiz çubukları FY16–26"]], [
      { t: k.part, olay: "etiket SIZE OF THE LOAN + punch-in", tur: "pop", oneri: "pop" },
      { t: k.rate0, olay: "etiket THE RATE (vurgu)", tur: "vurgu", oneri: "vuruş" },
      { t: k.early + 0.3, olay: "EARLY 2022 ~1.4%", tur: "pop", oneri: "" },
      { t: k.sep + 0.3, olay: "SEP 2026 ~3.5% (termometre yükselir)", tur: "sayac", oneri: "yükselen ton" },
      { t: k.just + 0.2, olay: "11 çubuk sırayla", tur: "sayac", oneri: "tık ×11" },
      { t: k.tripled, olay: "~3× IN 5 YEARS", tur: "vurgu", oneri: "vuruş" },
      { t: k.kitchen, olay: "$352 → $1,052 / mo", tur: "pop", oneri: "" },
      { t: k.growing, olay: "FY2026 çubuğu yanıp söner", tur: "vurgu", oneri: "tik ×2" },
    ]);
  },
  S14: () => {
    const a = an("S14");
    const k = { many: a("many"), weeks: a("weeks"), decades: a("decades"), roll: a("roll"), every: a("every"), replaced: a("replaced"), late: a("late"), short: a("short-term|short") };
    return yap("S14", k, [[0, "Leo yakın", true], [k.many - 0.2, "konveyör: krediler"], [k.late - 0.2, "grafik G4: yeni faizler"]], [
      { t: k.weeks, olay: "kısa şerit WEEKS", tur: "pop", oneri: "" },
      { t: k.decades, olay: "uzun şerit DECADES", tur: "pop", oneri: "" },
      { t: k.roll, olay: "ROLL OVER yazısı", tur: "pop", oneri: "pop" },
      { t: k.every, olay: "OLD LOAN DUE etiketi", tur: "pop", oneri: "tik" },
      { t: k.replaced, olay: "CHEAP 1% düşer → NEW 5%", tur: "vurgu", oneri: "etiket kopma + tık" },
      { t: k.late + 0.2, olay: "NEW 10-YEAR ~5%", tur: "pop", oneri: "" },
      { t: k.short, olay: "SHORT-TERM ~4%", tur: "pop", oneri: "" },
    ]);
  },
  S15: () => {
    const a = an("S15");
    const k = { climbing: a("climbing"), thats: a("that's"), rate: a("rate", 2), skip: a("skip"), and1: a("and", 1), but: a("but"), break: a("break"), three: a("three") };
    return yap("S15", k, [[0, "gösterge: ortalama faiz tırmanır"], [k.thats - 0.1, "buzdolabı: RATE × BALANCE"], [k.and1 - 0.1, "kuşbakışı: CAN'T SKIP"], [k.but - 0.1, "masa orta: FAMILY çatlar", true]], [
      { t: k.climbing, olay: "ibre yükselir", tur: "sayac", oneri: "yükselen ton" },
      { t: k.rate, olay: "RATE × BALANCE notu", tur: "dus", oneri: "slap" },
      { t: k.skip, olay: "CAN'T SKIP damgası", tur: "vurgu", oneri: "damga" },
      { t: k.break, olay: "FAMILY yazısı çatlar", tur: "vurgu", oneri: "cam çatlama" },
    ]);
  },
  S16: () => {
    const a = an("S16");
    const k = { own: a("own"), currency: a("currency"), run: a("run"), thats: a("that's"), answered: a("answered"), but: a("but"), if: a("if"), less: a("less"), inflation: a("inflation"), remember: a("remember") };
    return yap("S16", k, [[0, "kart: 1 · OWN MONEY"], [k.thats - 0.1, "buzdolabı: soru notuna tik"], [k.but - 0.1, "masa orta: But there's a catch", true], [k.if - 0.1, "fotokopi banknot + küçülen sepet"], [k.remember - 0.1, "Leo yakın", true]], [
      { t: 0.15, olay: "1 · IT BORROWS IN ITS OWN MONEY", tur: "pop", oneri: "pop" },
      { t: k.currency, olay: "OWN CURRENCY ✓ damgası", tur: "vurgu", oneri: "damga" },
      { t: k.run, olay: "CAN'T RUN OUT OF DOLLARS", tur: "pop", oneri: "pop" },
      { t: k.answered, olay: "yeşil tik (A5 kapanır)", tur: "vurgu", oneri: "doğru ding" },
      { t: k.answered + 0.8, olay: "alt köşe: LIKE IF THE ENVELOPE TOWER SURPRISED YOU (3 sn, sessiz)", tur: "etkilesim", oneri: "(sessiz)" },
      { t: k.if + 0.4, olay: "banknotlar çoğalır, sepet küçülür", tur: "parcacik", oneri: "fotokopi vınlaması" },
      { t: k.inflation, olay: "INFLATION", tur: "vurgu", oneri: "vuruş" },
    ]);
  },
  S17: () => {
    const a = an("S17");
    const k = { payday: a("payday"), it: a("rolling") - 0.6, rolling: a("rolling"), so: a("so"), back: a("back"), keep2: a("keep", 2) };
    return yap("S17", k, [[0, "kart: 2 · NEVER RETIRES"], [k.it - 0.1, "masa orta: IOU takla", true], [k.so - 0.1, "soru değişir"]], [
      { t: 0.15, olay: "2 · IT NEVER RETIRES", tur: "pop", oneri: "pop" },
      { t: k.payday, olay: "takvim sonsuz çevrilir", tur: "flip", oneri: "kâğıt çevirme" },
      { t: k.rolling, olay: "IOU fişleri takla atar", tur: "flip", oneri: "kâğıt hışırtı" },
      { t: k.back, olay: "PAY IT ALL BACK? üstü çizilir", tur: "vurgu", oneri: "kalem çizme" },
      { t: k.keep2, olay: "KEEP PAYING THE INTEREST?", tur: "pop", oneri: "pop" },
    ]);
  },
  S18: () => {
    const a = an("S18");
    const k = { tax: a("tax"), cut: a("cut"), both: a("both"), roommate: a("roommate") };
    return yap("S18", k, [[0, "kart: 3 · GIVE ITSELF A RAISE"], [k.both - 0.1, "Leo yakın: voters decide", true]], [
      { t: 0.15, olay: "3 · IT CAN GIVE ITSELF A RAISE", tur: "pop", oneri: "pop" },
      { t: k.tax, olay: "maaş zarfına kadran (yukarı/aşağı)", tur: "vurgu", oneri: "kadran tık-tık" },
      { t: k.cut, olay: "makas zarfı keser", tur: "vurgu", oneri: "makas" },
      { t: k.roommate, olay: "Leo gülümser (omuz silker)", tur: "vurgu", oneri: "hafif tını" },
    ]);
  },
  S19: () => {
    const a = an("S19");
    const k = { n46: a("nineteen|1946", 1), bigger: a("bigger", 1), n74: a("by"), quarter: a("quarter"), heres2: a("here's", 2), grew: a("grew", 1), loan: a("loan", 1), paycheck: a("paycheck"), family: a("family") };
    return yap("S19", k, [[0, "masa orta, Leo", true], [k.n46 - 0.2, "grafik G5: borç/GSYH 1946→1974"], [k.heres2 - 0.1, "grafik: borç $ çubuğu"], [k.loan - 0.1, "kuşbakışı: maaş büyür, defter aynı"], [k.family - 0.1, "Leo yakın", true]], [
      { t: k.n46, olay: "çizgi çizilmeye başlar, >100% (1946)", tur: "sayac", oneri: "çizim sesi" },
      { t: k.bigger, olay: "BIGGER THAN THE WHOLE ECONOMY etiketi", tur: "vurgu", oneri: "vuruş" },
      { t: k.quarter, olay: "~23% (1974) etiketi", tur: "pop", oneri: "ding" },
      { t: k.grew, olay: "$242B → $344B çubuğu yükselir", tur: "sayac", oneri: "yükselen ton" },
      { t: k.paycheck, olay: "maaş zarfı büyür", tur: "vurgu", oneri: "şişme" },
    ]);
  },
  S20: () => {
    const a = an("S20");
    const k = { ninety: a("ninety-seven|97%|percent", 1), so: a("so", 1), possibility: a("possibility"), but: a("but"), currency: a("currency"), years: a("years"), safest: a("safest"), brake: a("brake"), time: a("time", 1) };
    return yap("S20", k, [[0, "grafik G5 devam: ~97% (Q2 2026)"], [k.so - 0.1, "sarmal okları"], [k.but - 0.1, "masa orta: frenler var", true], [k.currency - 1.3, "üç fren ikonu"], [k.brake - 0.1, "Leo yakın", true]], [
      { t: k.ninety, olay: "ayrı nokta ~97% (FRED)", tur: "pop", oneri: "ding" },
      { t: k.so + 0.3, olay: "sarmal dönmeye başlar", tur: "parcacik", oneri: "dönen whoosh" },
      { t: k.possibility, olay: "SPIRAL? A POSSIBILITY, NOT A VERDICT", tur: "vurgu", oneri: "" },
      { t: k.currency, olay: "fren 1 OWN CURRENCY", tur: "pop", oneri: "fren tık" },
      { t: k.years, olay: "fren 2 LONG LOANS", tur: "pop", oneri: "fren tık" },
      { t: k.safest, olay: "fren 3 LENDERS' TRUST", tur: "pop", oneri: "fren tık" },
    ]);
  },
  S21: () => {
    const a = an("S21");
    const k = { this2: a("forecast") - 0.6, ill: a("i'll"), A: a("a", 2), B: a("b"), C: a("c") };
    return yap("S21", k, [[0, "masa orta: üç olasılık", true], [k.ill - 0.1, "buzdolabı: A · B · C dolar"]], [
      { t: k.this2, olay: "POSSIBILITIES, NOT A FORECAST şeridi", tur: "pop", oneri: "" },
      { t: k.A, olay: "not A · GROW", tur: "pop", oneri: "tap" },
      { t: k.B, olay: "not B · CHANGE THE ENVELOPES", tur: "pop", oneri: "tap" },
      { t: k.C, olay: "not C · LET PRICES RISE", tur: "pop", oneri: "tap" },
    ]);
  },
  S22: () => {
    const a = an("S22");
    const k = { faster: a("faster"), thats: a("that's"), catch: a("catch"), if2: a("if", 3), wins: a("wins"), fatter: a("fatter") };
    return yap("S22", k, [[0, "yarış: maaş önde"], [k.thats - 0.1, "G5 kısa geri dönüş 1946–74"], [k.catch - 0.3, "Leo yakın: GROWTH vs RATE", true], [k.if2 - 0.1, "yarış: borç öne geçer"]], [
      { t: 0.15, olay: "A · GROW THE PAYCHECK", tur: "pop", oneri: "düdük" },
      { t: k.faster, olay: "maaş öne geçer", tur: "vurgu", oneri: "koşu whoosh" },
      { t: k.catch, olay: "GROWTH vs RATE", tur: "pop", oneri: "hakem düdüğü" },
      { t: k.wins, olay: "borç defteri öne geçer", tur: "vurgu", oneri: "olumsuz vuruş" },
      { t: k.fatter, olay: "kırmızı zarf şişer", tur: "vurgu", oneri: "şişme" },
    ]);
  },
  S23: () => {
    const a = an("S23");
    const k = { raise: a("raise"), cut: a("cut", 1), every: a("every", 1), retirees: a("retirees"), patients: a("patients"), soldiers: a("soldiers"), students: a("students"), every2: a("every", 2), slow: a("slow") };
    return yap("S23", k, [[0, "kuşbakışı: B · CHANGE THE ENVELOPES"], [k.every - 0.1, "zarflardan siluetler"], [k.every2 - 0.1, "masa orta: slow and loud", true]], [
      { t: k.raise, olay: "RAISE TAXES", tur: "pop", oneri: "" },
      { t: k.cut, olay: "CUT SPENDING + makas", tur: "pop", oneri: "makas" },
      ...(["retirees", "patients", "soldiers", "students"] as const).map((w) => ({ t: k[w], olay: `silüet (${w})`, tur: "pop", oneri: "pop" })),
      { t: k.slow, olay: "SLOW AND LOUD", tur: "vurgu", oneri: "" },
    ]);
  },
  S24: () => {
    const a = an("S24");
    const k = { smaller: a("smaller"), n46: a("nineteen|1946"), eighteen: a("eighteen|18%|percent", 1), catch: a("catch"), grocery: a("grocery"), lenders: a("lenders") - 0.5, envelope: a("envelope"), fatter: a("fatter") };
    return yap("S24", k, [[0, "kart: C · LET PRICES RISE"], [k.n46 - 0.2, "1946: PRICES +18%"], [k.catch - 0.3, "masa orta: market fişi uzar", true], [k.lenders - 0.1, "Leo yakın: zarf geri şişer", true]], [
      { t: 0.15, olay: "C · LET PRICES RISE", tur: "pop", oneri: "pop" },
      { t: k.smaller, olay: "banknotlar küçülür", tur: "vurgu", oneri: "büzülme" },
      { t: k.eighteen, olay: "+18% (1946)", tur: "pop", oneri: "ding" },
      { t: k.grocery, olay: "market fişi uzar", tur: "vurgu", oneri: "yazarkasa fişi" },
      { t: k.fatter, olay: "kırmızı zarf şişer + OLD DEBT SHRINKS · NEW RATES RISE", tur: "vurgu", oneri: "şişme" },
    ]);
  },
  S25: () => {
    const a = an("S25");
    const k = { luck: a("luck"), but: a("but"), A: a("a", 2) - 0.1, comments: a("comments") };
    return yap("S25", k, [[0, "buzdolabı: A B C + LUCK"], [k.but - 0.1, "Leo yakın: you can read the bill", true], [k.A - 0.1, "kart: ONE LETTER IN THE COMMENTS"]], [
      { t: k.luck, olay: "+ LUCK notu", tur: "pop", oneri: "tap" },
      { t: k.A + 0.1, olay: "A · B · C → ONE LETTER IN THE COMMENTS", tur: "vurgu", oneri: "pop ×3" },
    ]);
  },
  S26: () => {
    const a = an("S26");
    const k = { money: a("money"), retires: a("retires"), raise: a("raise"), but: a("but"), kitchen: a("kitchen"), military: a("military"), paper: a("paper"), inside: a("inside"), abone: aboneAn("S26") };
    return yap("S26", k, [[0, "buzdolabı: tez notu + 3 tik"], [k.but - 0.1, "Leo yakın: RATE × BALANCE", true], [k.kitchen - 0.4, "masa geniş: lamba kısılır", true]], [
      { t: 0.2, olay: "tez notu büyür", tur: "pop", oneri: "" },
      { t: k.money, olay: "tik 1", tur: "pop", oneri: "tik" },
      { t: k.retires, olay: "tik 2", tur: "pop", oneri: "tik" },
      { t: k.raise, olay: "tik 3", tur: "pop", oneri: "tik" },
      { t: k.military, olay: "$1,050 > DEFENSE $965", tur: "vurgu", oneri: "" },
      { t: k.inside, olay: "kırmızı zarftan iç zarf kenarı görünür", tur: "vurgu", oneri: "kâğıt" },
      { t: k.abone, olay: "ABONE-3 (sağ alt boş; zarf solda)", tur: "abone", oneri: "klik (kurgu-editoru bileşeni)" },
    ]);
  },
  S27: () => {
    const a = an("S27");
    const k = { we: a("we"), five: a("five|5%|percent", 1), where: a("where"), story: a("story") };
    return yap("S27", k, [[0, "masa orta: bir sayı", true], [k.we - 0.1, "buzdolabı: ~5% notu"], [k.where - 0.1, "pencere: not evlerin üstüne uçar"]], [
      { t: k.five, olay: "~5% notuna punch-in", tur: "kamera", oneri: "" },
      { t: k.where + 0.3, olay: "not pencereden uçar", tur: "kay", oneri: "kâğıt uçuşu" },
    ]);
  },
};

export const ZAMAN = P;
export const plan = (id: string): Plan => {
  const f = P[id];
  if (!f) throw new Error(`zaman planı yok: ${id}`);
  return f();
};
