// TEK KAYNAK zaman planı (animasyon-yonetmeni) — S03 "The Biggest Inheritance Ever" (2026-11-04-miras-sizintilari).
// Sahne kodu, efekt cue'ları (06-muzik/animasyon-efekt-cue.json) ve ağzın göründüğü aralıklar (07-animasyon/agiz-gorunur.json)
// bu fonksiyonlardan üretilir → hiçbiri kayamaz. Saf TS (React yok): 07-animasyon/olay-cikar.mjs esbuild ile çalıştırır.
// Zamanlar sahne YEREL saniyesi; kelime çapası (an(id)("word", n)) — ses gelince kendini günceller, eksik kelime hata fırlatır.
// Kaynak desen: video/src/videolar/yeni-video/zaman.ts (S08 KButce).
import { SAHNELER } from "./veri-sahne";

export type Olay = { t: number; olay: string; tur: string; oneri?: string };
// Kesme: [t, açıklama, Leo konuşuyor mu, çekim anahtarı (sahneler.tsx CEKIM; "ad:param"), yoksa yer tutucu plaka]
export type Kes = [t: number, ad: string, leo?: boolean, cekim?: string];
// Ekran yazısı (üst bant, ekran uzayı): [t, metin, son?, renk?]
export type Ekran = [t: number, metin: string, son?: number, renk?: string];
export type Plan = { k: Record<string, number>; olay: Olay[]; agiz: [number, number][]; kes: Kes[]; ekran: Ekran[]; kaynak: [number, string][] };

const norm = (w: string) => w.toLowerCase().replace(/[‘’]/g, "'").replace(/[^a-z0-9$'-]/g, "");
const sv = (id: string) => {
  const s = SAHNELER.find((x) => x.id === id);
  if (!s) throw new Error(`sahne yok: ${id}`);
  return s;
};
export const sure = (id: string) => sv(id).sure;
export const an = (id: string) => {
  const s = sv(id);
  // "fifteen|$15M": alternatifler (hizalı metin yazıyla, ham Whisper rakamla yazabilir) — ilk bulunan
  return (w: string, n = 1, son = false): number => {
    for (const alt of w.split("|")) {
      const hedef = norm(alt);
      let say = 0;
      for (const k of s.kelimeler) if (norm(k.w) === hedef && ++say === n) return son ? k.e : k.s;
    }
    throw new Error(`${id}: kelime yok: ${w} #${n}`);
  };
};
// Abone anları (metin §3 ABONE-1..3): sahne sonundaki 1,5 sn nefesin başı (son kelime bitişi + 0,15); çapa = sonraki sahnenin ilk cümlesi
export const ABONE_SAHNE = ["S05", "S17", "S30"] as const;
export const aboneAn = (id: string) => {
  const s = sv(id);
  return s.kelimeler[s.kelimeler.length - 1].e + 0.15;
};
const abone = (id: string, n: number, not: string): Olay => ({ t: aboneAn(id), olay: `ABONE-${n} (${not})`, tur: "abone", oneri: "klik (kurgu-editoru ortak bileşeni)" });

// Kesme listesinden plan: ağız aralıkları = Leo'nun konuştuğu kesmeler; her kesme ve ekran yazısı bir görsel olay
const yap = (id: string, k: Record<string, number>, kes: Kes[], olay: Olay[] = [], ekran: Ekran[] = [], kaynak: [number, string][] = []): Plan => {
  const S = sure(id);
  kes.forEach((c, i) => {
    if (i && c[0] <= kes[i - 1][0] + 0.4) throw new Error(`${id}: kesme sırası/aralığı bozuk: ${kes[i - 1][1]} → ${c[1]} (${kes[i - 1][0].toFixed(2)} → ${c[0].toFixed(2)})`);
  });
  if (kes.length && S - kes[kes.length - 1][0] < 0.4) throw new Error(`${id}: son kesme sahne sonuna çok yakın`);
  for (const o of olay) if (!(o.t >= 0 && o.t < S)) throw new Error(`${id}: olay sahne dışında: ${o.olay} @${o.t.toFixed(2)}`);
  const agiz: [number, number][] = [];
  kes.forEach((c, i) => {
    if (c[2]) agiz.push([Math.max(0, c[0]), i + 1 < kes.length ? kes[i + 1][0] : S]);
  });
  const ko: Olay[] = kes.map((c) => ({ t: Math.max(0, c[0]), olay: `kesme: ${c[1]}`, tur: "kesme", oneri: c[0] <= 0.01 ? "sahne geçişi (yumuşak whoosh)" : "kısa whoosh" }));
  const eo: Olay[] = ekran.map((e) => ({ t: e[0], olay: `ekran yazısı: ${e[1]}`, tur: "yazi", oneri: "hafif pop" }));
  return { k, kes, ekran, kaynak, olay: [...ko, ...eo, ...olay].sort((a, b) => a.t - b.t), agiz };
};

const P: Record<string, () => Plan> = {
  // ---------- Bölüm 1 — The Number on the Truck ----------
  S01: () => {
    const a = an("S01");
    const k = { son: sure("S01"), kapi: 0.1, damla: 1.6, but: a("but"), charity: a("charity"), fifty: a("fifty-four"), spouse: a("spouse"), so: a("so"), one2: a("one", 2), family: a("family") };
    return yap(
      "S01",
      k,
      [
        [0, "kamyon arka kapısı: dev kutu $124T", false, "devKutu"],
        [k.fifty - 0.1, "kamyon yan şeride sinyal: sarı tabela", false, "esTabela:s01"],
        [k.so - 0.1, "Leo kamyon yanında pano kaldırır", true, "leo:kapi"],
        [k.one2 - 0.1, "dev kutu 10 küçük kutuya bölünür", false, "devKutu"],
      ],
      [
        { t: k.kapi, olay: "kamyon arka kapısı açılır, dev kutu $124T", tur: "kart", oneri: "metal kapı + sürgü" },
        { t: k.damla, olay: "kutunun köşesinden banknot damlar (≤3 sn görsel değişim)", tur: "damla", oneri: "damla / kâğıt" },
        { t: k.charity, olay: "dilim kayar: $18T → CHARITY", tur: "kay", oneri: "kâğıt kayma" },
        { t: k.spouse, olay: "sinyal + SPOUSE FIRST tabelası", tur: "vurgu", oneri: "sinyal tık-tık" },
        { t: k.one2 + 0.15, olay: "dev kutu 10 kutuya bölünür", tur: "pop", oneri: "karton pop ×10" },
      ],
      [],
      [[0, "R01"], [k.charity, "R03"], [k.fifty, "R04"]],
    );
  },
  S02: () => {
    const a = an("S02");
    const k = { often: a("often"), but: a("but"), maybe1: a("maybe", 1), maybe2: a("maybe", 2), either: a("either"), so: a("so"), less: a("less"), later: a("later"), which: a("which") };
    return yap(
      "S02",
      k,
      [
        [0, "ABD haritası, küçük kamyonlar", false, "yer:harita"],
        [k.maybe1 - 0.1, "kamera tek sokağa, tek eve iner: kapıda kutu", false, "yer:ev"],
        [k.maybe2 - 0.1, "kapıdan çıkan kutular, içeri giren genç siluet", false, "yer:ev"],
        [k.so - 0.1, "Leo kamyon kapısında", true, "leo:kapi"],
        [k.which - 0.1, "soru işaretli kutu BIGGEST LEAK = ?", false, "soruKutu"],
      ],
      [{ t: k.which + 0.2, olay: "soru işaretli kutu sallanır", tur: "vurgu", oneri: "gizem tını" }],
      [
        [0.3, "OFTEN CALLED THE BIGGEST INHERITANCE IN HISTORY", k.maybe1 - 0.2],
        [k.either, "HEIR? HOME BUYER? BOTH?", k.so - 0.2],
        [k.less, "LESS? LATER?", k.which - 0.2],
      ],
    );
  },
  S03: () => {
    const a = an("S03");
    const k = { cartoon: a("cartoon"), load: a("load"), before: a("before"), an: a("an"), its: a("it's") };
    return yap(
      "S03",
      k,
      [
        [0, "Leo kamyon kapısında (yelek, pano, bant)", true, "leo:kapi"],
        [k.before - 0.1, "Leo yakın, ciddi", true, "leo:yakin"],
        [k.an - 0.1, "tez kamyonun yan yüzüne boyanır", false, "tez"],
      ],
      [
        { t: 0.3, olay: "isim etiketi LEO · MOVING CREW BOSS", tur: "pop", oneri: "hafif pop" },
        { t: k.cartoon, olay: "Leo göz kırpar", tur: "vurgu", oneri: "tık" },
        { t: k.an, olay: "tez yazısı boyanır", tur: "vurgu", oneri: "fırça / sprey" },
        { t: sure("S03") - 0.6, olay: "kontak: motor çalışır", tur: "vurgu", oneri: "motor SFX" },
      ],
    );
  },
  S04: () => {
    const a = an("S04");
    const k = { first: a("first"), forecast: a("forecast"), nearly: a("nearly"), about1: a("about", 1), about2: a("about", 2), and: a("and", 2), fifty: a("fifty-four"), stop: a("stop", 1), money: a("money", 2), so: a("so"), detour: a("detour"), remember: a("remember") };
    return yap(
      "S04",
      k,
      [
        [0, "Leo büyüteçle dev kutunun etiketini okur", true, "leo:kapi"],
        [k.forecast - 0.1, "etiket yakın: FORECAST · CERULLI · DEC 2024", false, "etiket"],
        [k.nearly - 0.1, "grafik G1: tek çubuk $124T", false, "g1"],
        [k.and - 0.1, "Leo: here's the twist", true, "leo:yakin"],
        [k.fifty - 0.1, "G1 üstünden geçen yol + sarı durak tabelası", false, "g1:es"],
        [k.so - 0.1, "Leo kamyonu yan şeride çevirir: DETOUR ≠ LEAK", true, "leo:kapi"],
      ],
      [
        { t: k.nearly + 0.2, olay: "not: ~$100T from Boomers and older (81%)", tur: "pop", oneri: "" },
        { t: k.about1, olay: "çubuk dolar: ~$105T HEIRS (lacivert)", tur: "sayac", oneri: "yükselen tık" },
        { t: k.about2, olay: "~$18T CHARITY (yeşil) dilimi", tur: "pop", oneri: "pop" },
        { t: k.fifty + 0.3, olay: "sarı tabela SPOUSE FIRST · ~$54T STOP", tur: "pop", oneri: "tabela tok" },
        { t: k.money + 0.2, olay: "ok çubuğa geri döner", tur: "kay", oneri: "whoosh kısa" },
        { t: k.detour, olay: "pano: DETOUR ≠ LEAK", tur: "vurgu", oneri: "keçeli kalem" },
      ],
      [[k.detour, "DETOUR ≠ LEAK", undefined, "#ffd43b"]],
      [[k.forecast, "R01"], [k.nearly, "R06"], [k.about1, "R02"], [k.fifty, "R04"]],
    );
  },
  S05: () => {
    const a = an("S05");
    const k = { hides: a("hides"), to: a("to"), we: a("we"), one3: a("one", 3), abone: aboneAn("S05") };
    return yap(
      "S05",
      k,
      [
        [0, "harita → kamera tek eve iner", false, "yer:ev"],
        [k.to - 0.1, "kapıda 4 siluet + kamyon (sağ alt boş)", false, "aileKapi"],
      ],
      [abone("S05", 1, "sağ alt boş; aile + kamyon sol-orta")],
      [[k.we, "ONE FAMILY. ONE TRUCK."]],
    );
  },
  // ---------- Bölüm 2 — Loading the Okafors ----------
  S06: () => {
    const a = an("S06");
    const k = { meet: a("meet"), two: a("two"), ten: a("ten"), four1: a("four", 1), four2: a("four", 2), two3: a("two", 3), each: a("each"), there: a("there"), on: a("on", 2), to: a("to", 1), moving1: a("moving", 1), moving2: a("moving", 2), well: a("we'll") };
    return yap(
      "S06",
      k,
      [
        [0, "kapı eşiğinde 4 düz siluet + EXAMPLE FAMILY etiketi", false, "aileKapi"],
        [k.ten - 0.1, "10 kutu yüklenir (4 HOUSE · 4 RETIREMENT · 2 BANK)", false, "kutular:0"],
        [k.on - 0.1, "Leo her kutuya TO: THE KIDS yazar", true, "leo:kapi"],
        [k.moving1 - 0.1, "kutular yakın: etiketler", false, "kutular:0"],
        [k.well - 0.1, "Leo kameraya: we'll see", true, "leo:yakin"],
      ],
      [
        { t: k.four1, olay: "4 kiremit HOUSE kutusu yerine oturur", tur: "pop", oneri: "karton tok ×4" },
        { t: k.four2, olay: "4 lacivert RETIREMENT kutusu", tur: "pop", oneri: "karton tok ×4" },
        { t: k.two3, olay: "2 yeşil BANK kutusu", tur: "pop", oneri: "karton tok ×2" },
        { t: k.to + 0.1, olay: "keçeli: TO: THE KIDS", tur: "vurgu", oneri: "keçeli kalem" },
      ],
      [[k.each, "10 BOXES = ALL THEIR WEALTH", k.on - 0.2], [k.there + 0.4, "ILLUSTRATION, NOT AN AVERAGE", k.on - 0.2], [k.moving1, "RULE 1: LABEL EVERYTHING", k.moving2 - 0.1], [k.moving2, "RULE 2: CHECK THE BOTTOM"]],
      [[0, "ORNEK"]],
    );
  },
  S07: () => {
    const a = an("S07");
    const k = { six: a("six"), some: a("some"), one: a("one"), and: a("and"), lets: a("let's") };
    return yap(
      "S07",
      k,
      [
        [0, "Leo panoyu gösterir", true, "leo:kapi"],
        [k.six - 0.1, "pano: 6 durak (sızıntı çizelgesi)", false, "pano:S07"],
        [k.and - 0.1, "6 durak tabelası yol boyunca", false, "tabelalar"],
        [k.lets - 0.1, "kamyon yola çıkar", false, "yer:yol"],
      ],
      [
        { t: k.six + 0.2, olay: "pano satırları sırayla yazılır ×6", tur: "pop", oneri: "kalem tık ×6" },
        { t: k.lets + 0.3, olay: "kamyon kalkar", tur: "vurgu", oneri: "motor + korna" },
      ],
    );
  },
  // ---------- Bölüm 3 — Living and Care ----------
  S08: () => {
    const a = an("S08");
    const k = { stop: a("stop"), in: a("in"), about: a("about"), thats: a("that's", 1), and2: a("and", 2), so: a("so"), label: a("label"), is: a("is", 2), but: a("but"), a2: a("headline"), and3: a("honestly") - 0.2 };
    return yap(
      "S08",
      k,
      [
        [0, "durak tabelası LIVING", false, "tabela:LIVING"],
        [k.in - 0.1, "zaman şeridi AGE 65 → ~20 MORE YEARS", false, "omur"],
        [k.thats - 0.1, "iki lacivert kutu açılır: market, fatura, tren bileti", false, "yer:kutuIci"],
        [k.so - 0.1, "kutular: 2 kutuya SPENT ON LIVING damgası", false, "kutular:0"],
        [k.is - 0.1, "Leo: is that a leak?", true, "leo:yakin"],
        [k.a2 - 0.1, "ekran: ONE COUNTRY-WIDE TOTAL ≠ ONE FAMILY'S BOXES (D-1)", false, "soz:ONE COUNTRY-WIDE TOTAL ≠ ONE FAMILY'S BOXES"],
        [k.and3, "Leo gülümser", true, "leo:kapi"],
      ],
      [
        { t: k.about + 0.1, olay: "zaman şeridi uzar: ~20 MORE YEARS", tur: "sayac", oneri: "yükselen tık" },
        { t: k.label, olay: "SPENT ON LIVING damgası ×2", tur: "damga", oneri: "damga thud ×2" },
      ],
      [],
      [[k.in, "R14"]],
    );
  },
  S09: () => {
    const a = an("S09");
    const k = { and: a("and"), tape: a("tape") };
    return yap("S09", k, [[0, "sisli yoldan CARE tabelası belirir", false, "tabela:CARE"], [k.and - 0.1, "Leo bant rulosunu sallar", true, "leo:yakin"]], [{ t: 0.5, olay: "CARE tabelası sisten çıkar", tur: "vurgu", oneri: "rüzgâr / sis" }]);
  },
  S10: () => {
    const a = an("S10");
    const k = { stop: a("stop"), getting: a("getting"), cooking: a("cooking"), taking: a("taking"), us: a("u.s.|us", 1), more: a("more", 1), about: a("about", 1), sometimes1: a("sometimes", 1), and: a("bill") - 0.4, median: a("median") };
    return yap(
      "S10",
      k,
      [
        [0, "Leo: stop two is care", true, "leo:kapi"],
        [k.getting - 0.1, "ev içi siluet kareleri: düğme, ocak, ilaç", false, "yer:evIci"],
        [k.us - 0.1, "grafik G2: 100 insan ikonu", false, "g2"],
        [k.sometimes1 - 0.1, "evde aile / huzurevi siluetleri", false, "yer:huzurevi"],
        [k.and, "fatura kartı $129,575 / YEAR", false, "fatura"],
      ],
      [
        { t: k.more, olay: "56 ikon renklenir: 56%", tur: "sayac", oneri: "tıkırtı" },
        { t: k.about, olay: "22 ikon koyulaşır: >5 YEARS 22%", tur: "vurgu", oneri: "tık" },
        { t: k.median, olay: "fatura kartı sayacı $129,575", tur: "sayac", oneri: "yazar kasa" },
      ],
      [],
      [[k.us, "R16"], [k.and, "R13"]],
    );
  },
  S11: () => {
    const a = an("S11");
    const k = { why: a("why"), because: a("because"), that: a("that"), and: a("and", 1), states: a("states"), the: a("same") - 0.15, about: a("about"), for: a("okafors") - 0.3, label: a("label"), in: a("different") - 0.2 };
    return yap(
      "S11",
      k,
      [
        [0, "Leo: why does this one leak so much?", true, "leo:yakin"],
        [k.because - 0.1, "iki kapı: MEDICARE / MEDICAID", false, "kapilar"],
        [k.the - 0.1, "grafik: 7 ikondan 1'i kırmızı", false, "yedide1"],
        [k.for, "pano CARE −1", false, "pano:S11"],
        [k.in, "iki hayalet kamyon: 0 kutu / 4 kutu", false, "hayalet"],
      ],
      [
        { t: k.because + 0.3, olay: "levha: LONG-TERM CUSTODIAL CARE: GENERALLY NOT COVERED", tur: "pop", oneri: "levha tok" },
        { t: k.states, olay: "el ESTATE RECOVERY etiketi yapıştırır", tur: "vurgu", oneri: "etiket yapışma" },
        { t: k.about + 0.2, olay: "7'de 1 ikon kırmızı: $100K+", tur: "vurgu", oneri: "ding" },
        { t: k.label, olay: "CARE −1 kalem çizgisi", tur: "vurgu", oneri: "keçeli çizgi" },
      ],
      [],
      [[k.because, "R25"], [k.the, "R17"], [k.for, "ORNEK"]],
    );
  },
  S12: () => {
    const a = an("S12");
    const k = { the: a("the"), i: a("i", 1), i1: a("tape", 1), then: a("then"), so: a("so"), okay: a("okay"), two: a("two", 1), and: a("and", 2), nobody: a("nobody") };
    return yap(
      "S12",
      k,
      [
        [0, "kasa içi: Leo (M09)", true, "leo:kasa"],
        [k.i - 0.1, "kutu yakın: Leo bantlar (M05 el), başka köşeden damla, 2. bant", false, "bantEl"],
        [k.okay - 0.1, "Leo kameraya: two-tape stop", true, "leo:kasaYakin"],
        [k.and - 0.1, "pano −3", false, "pano:S12"],
        [k.nobody - 0.1, "Leo yakın, sakin", true, "leo:kasaYakin"],
      ],
      [
        { t: k.i1, olay: "bant 1 çekilir", tur: "vurgu", oneri: "koli bandı çekme" },
        { t: k.then + 0.4, olay: "başka köşeden damla", tur: "damla", oneri: "damla" },
        { t: k.so + 0.3, olay: "bant 2 çekilir", tur: "vurgu", oneri: "koli bandı çekme" },
      ],
      [[k.okay, "TAPE USED: 2", k.and - 0.2, "#ffd43b"]],
      [[k.and, "ORNEK"]],
    );
  },
  // ---------- Bölüm 4 — The Detour and the Gift ----------
  S13: () => {
    const a = an("S13");
    const k = { when: a("when"), it: a("turns") - 0.2, cerulli: a("cerulli"), nearly: a("nearly"), for: a("example") - 0.3, but: a("but") };
    return yap(
      "S13",
      k,
      [
        [0, "kavşak, sinyal: SPOUSE FIRST tabelası", false, "tabela:SPOUSE FIRST"],
        [k.when - 0.1, "eşikte iki siluet; biri yumuşakça solar (ışık kalır)", false, "solma"],
        [k.it, "kamyon karşı kaldırıma yanaşır", false, "yer:karsiKaldirim"],
        [k.cerulli - 0.1, "sarı durak tabelası ~$54T · ~$40T", false, "esTabela:s13"],
        [k.for - 0.1, "Leo kutulardaki isimleri gösterir", true, "leo:kapi"],
      ],
      [
        { t: 0.3, olay: "sinyal", tur: "vurgu", oneri: "sinyal tık-tık" },
        { t: k.when + 1.2, olay: "siluet solar, sıcak ışık kalır", tur: "vurgu", oneri: "yumuşak pad (vuruş yok)" },
        { t: k.nearly, olay: "~$40T OF IT TO WIDOWED WOMEN satırı", tur: "pop", oneri: "" },
      ],
      [],
      [[k.cerulli, "R04"], [k.nearly, "R05"]],
    );
  },
  S14: () => {
    const a = an("S14");
    const k = { now: a("now"), zero: a("zero"), but: a("but", 1), while: a("while", 1), more: a("more", 1), to: a("to"), detour: a("detour"), think: a("think"), baton: a("baton"), kids: a("kids", 2) };
    return yap(
      "S14",
      k,
      [
        [0, "pano: SPOUSE −0 + kum saati +YEARS", false, "pano:S14"],
        [k.but - 0.1, "Leo yakın: the part the headline hides", true, "leo:yakin"],
        [k.while - 0.1, "park hâlinde kamyon, takvim yaprakları; LIVING/CARE ikinci kez", false, "yer:park"],
        [k.to - 0.1, "kutu büyür, sonra açılıp küçülür", false, "buyuyenKutu"],
        [k.detour - 0.1, "Leo: more time", true, "leo:kapi"],
        [k.think - 0.1, "bayrak yarışı pisti", false, "bayrak"],
      ],
      [
        { t: k.zero, olay: "SPOUSE −0 yazılır", tur: "vurgu", oneri: "kalem tık" },
        { t: k.zero + 0.6, olay: "kum saati +YEARS döner", tur: "vurgu", oneri: "kum saati" },
        { t: k.more + 0.2, olay: "LIVING / CARE tabelaları ikinci kez geçer", tur: "kay", oneri: "whoosh ×2" },
        { t: k.baton, olay: "bayrak eşe geçer", tur: "vurgu", oneri: "bayrak devri" },
        { t: k.kids, olay: "pist ucunda bekleyen iki siluet", tur: "pop", oneri: "" },
      ],
      [[k.zero, "BOXES LOST: 0", k.but - 0.2, "#ffd43b"]],
    );
  },
  S15: () => {
    const a = an("S15");
    const k = { and: a("and") };
    return yap("S15", k, [[0, "GIVING tabelası, küçük kalp", false, "tabela:GIVING"], [k.and - 0.1, "Leo: on purpose", true, "leo:yakin"]], [{ t: 0.5, olay: "kalp parlar", tur: "vurgu", oneri: "sıcak tını" }]);
  },
  S16: () => {
    const a = an("S16");
    const k = { cerulli: a("cerulli"), schools: a("schools"), hospitals: a("hospitals"), churches: a("churches"), research: a("research"), this: a("this"), in: a("in"), i: a("i"), label: a("label"), its: a("it's", 2) };
    return yap(
      "S16",
      k,
      [
        [0, "Leo: stop four is giving", true, "leo:kapi"],
        [k.cerulli - 0.1, "S04 çubuğunda ~$18T CHARITY parlar", false, "g1:bagis"],
        [k.schools - 0.1, "okul / hastane / ibadethane ikonları (eşit boy)", false, "ikonlar"],
        [k.in - 0.1, "kamyon okulun önünde, yeşil kutu kapıya", false, "yer:okul"],
        [k.i - 0.1, "pano GIVING −1", false, "pano:S16"],
        [k.its - 0.1, "Leo gülümser", true, "leo:yakin"],
      ],
      [
        ...(["schools", "hospitals", "churches", "research"] as const).map((w) => ({ t: k[w], olay: `ikon ${w.toUpperCase()}`, tur: "pop", oneri: "tik" })),
        { t: k.label, olay: "GIVEN etiketi", tur: "vurgu", oneri: "keçeli kalem" },
      ],
      [],
      [[k.cerulli, "R03"], [k.in, "ORNEK"]],
    );
  },
  S17: () => {
    const a = an("S17");
    const k = { in: a("in"), forty: a("forty-seven"), in2: a("in", 2), fifty: a("fifty-five"), fewer: a("fewer"), abone: aboneAn("S17") };
    return yap(
      "S17",
      k,
      [
        [0, "grafik G3: iki çubuk (sol-orta)", false, "g3"],
        [k.fewer - 0.1, "Leo kutuyu iki siluet arasında tutar (sol)", false, "kararsiz"],
      ],
      [
        { t: k.forty, olay: "çubuk 2026: 47%", tur: "sayac", oneri: "tık" },
        { t: k.fifty, olay: "çubuk 2024: 55% (geri bakış)", tur: "sayac", oneri: "tık" },
        abone("S17", 2, "sağ alt boş; grafik/Leo sol-orta"),
      ],
      [],
      [[0, "R09"]],
    );
  },
  // ---------- Bölüm 5 — The Heaviest Box ----------
  S18: () => {
    const a = an("S18");
    const k = { living: a("living"), care: a("care"), detour: a("detour"), giving: a("giving"), six: a("six"), and: a("and") };
    return yap(
      "S18",
      k,
      [
        [0, "pano ara özet (envanter)", false, "pano:S18"],
        [k.six - 0.1, "kamyonun içi: 6 kutu, 4 kiremit dipte", false, "kutular:4"],
      ],
      (["living", "care", "detour", "giving"] as const).map((w) => ({ t: k[w], olay: `pano satırı ${w.toUpperCase()} tik`, tur: "tik", oneri: "tik" })),
      [],
      [[0, "ORNEK"]],
    );
  },
  S19: () => {
    const a = an("S19");
    const k = { for: a("for"), and: a("and", 1), fed: a("fed"), but: a("but"), two: a("two", 1), one: a("one", 1), if: a("if"), and2: a("selling") - 0.15, agent: a("agent"), repairs: a("repairs"), property: a("property"), sometimes: a("sometimes") };
    return yap(
      "S19",
      k,
      [
        [0, "4 kiremit kutu yapışık: tek parça ev maketi", false, "kutular:4"],
        [k.fed - 0.1, "tek çubuk BOOMERS ~41% OF US HOUSEHOLD REAL ESTATE", false, "g19"],
        [k.but - 0.1, "Leo: you can't cut it in half", true, "leo:yakin"],
        [k.two - 0.1, "iki genç siluet maketi çeker (bölünmez)", false, "yer:cekisme"],
        [k.if - 0.1, "tek SOLD kartı", false, "sold"],
        [k.and2, "fatura kartları uçar", false, "faturalar"],
        [k.sometimes - 0.1, "sepya geri dönüş: ev CARE durağında satılır", false, "yer:sepya"],
      ],
      [
        { t: k.fed + 0.3, olay: "çubuk dolar ~41%", tur: "sayac", oneri: "yükselen tık" },
        { t: k.if + 0.6, olay: "SOLD kartı çakılır", tur: "damga", oneri: "tabela tok" },
        ...(["agent", "repairs", "property"] as const).map((w) => ({ t: k[w], olay: `fatura kartı ${w.toUpperCase()}`, tur: "pop", oneri: "kâğıt" })),
      ],
      [],
      [[k.fed, "R23"]],
    );
  },
  S20: () => {
    const a = an("S20");
    const k = { it: a("it"), and: a("and", 1), maybe: a("maybe"), oh: a("oh"), more: a("more") };
    return yap(
      "S20",
      k,
      [
        [0, "kiremit kutudan ince dilim: −A SLICE", false, "dilim"],
        [k.and - 0.1, "kapıdan genç siluet anahtarla girer", false, "yer:anahtar"],
        [k.oh - 0.1, "Leo üçüncü köşeyi bantlar", true, "leo:kapi"],
      ],
      [
        { t: k.it + 0.1, olay: "dilim kesilir", tur: "vurgu", oneri: "maket bıçağı" },
        { t: k.maybe, olay: "anahtar şıngırtısı", tur: "vurgu", oneri: "anahtar" },
        { t: k.more, olay: "bant 3", tur: "vurgu", oneri: "koli bandı (incelmiş rulo)" },
      ],
      [[k.more, "TAPE USED: 3", undefined, "#ffd43b"]],
    );
  },
  // ---------- Bölüm 6 — The Leak Everyone Fears ----------
  S21: () => {
    const a = an("S21");
    const k = { taxes: a("taxes"), so: a("so", 1), as: a("as", 1), fifteen: a("fifteen|$15M"), now: a("now"), for: a("for", 2), median: a("median"), the: a("line") - 0.3, so2: a("so", 2), the2: a("drive") - 0.6, but: a("but"), money: a("money"), income: a("income"), some: a("some", 2), and: a("other") - 0.2, in: a("u.k.|uk") - 0.25, three: a("three") };
    return yap(
      "S21",
      k,
      [
        [0, "ürkütücü gişe TAX (gölgeli)", false, "gise"],
        [k.so - 0.1, "Leo tabelayı okur", true, "leo:yakin"],
        [k.as - 0.1, "grafik G4: eşik çizgisi $15M", false, "g4"],
        [k.so2 - 0.1, "bariyer kalkar, kamyon geçer", false, "gise:acik"],
        [k.but - 0.1, "kart: ESTATE TAX ≠ THE ONLY TAX (R28, rakamsız)", false, "gelirVergisi"],
        [k.some - 0.1, "not: some states have their own taxes", false, "g4:eyalet"],
        [k.in - 0.1, "UK kartı £325,000", false, "uk"],
      ],
      [
        { t: 0.2, olay: "gök gürültüsü", tur: "vurgu", oneri: "gök gürültüsü" },
        { t: k.so + 0.2, olay: "gürültü kesilir", tur: "vurgu", oneri: "MÜZİK KES" },
        { t: k.fifteen, olay: "eşik çizgisi iner: $15M PER PERSON", tur: "pop", oneri: "tok vuruş" },
        { t: k.median, olay: "küçük çubuk ~$410K belirir", tur: "pop", oneri: "küçük tık" },
        { t: k.the, olay: "aradaki boşluk oku: DOZENS OF TIMES HIGHER", tur: "vurgu", oneri: "yükselen whoosh" },
        { t: k.the2 + 0.3, olay: "bariyer kalkar", tur: "vurgu", oneri: "bariyer + motor" },
        { t: k.money, olay: "emeklilik kutusu: TAXED AS INCOME etiketi", tur: "pop", oneri: "etiket tap" },
        { t: k.three, olay: "UK kartı: £325,000", tur: "pop", oneri: "pop" },
      ],
      [],
      [[k.as, "R18"], [k.median, "R19"], [k.but, "R28"], [k.some, "R20"], [k.in, "R26"]],
    );
  },
  S22: () => {
    const a = an("S22");
    const k = { the: a("the", 2), for: a("for"), living: a("living"), care: a("care"), time: a("time"), quick: a("quick"), tell: a("tell") };
    return yap(
      "S22",
      k,
      [
        [0, "Leo: the surprise of this whole road", true, "leo:kapi"],
        [k.for - 0.1, "pano: TAX −0; LIVING ve CARE altı çizilir", false, "pano:S22"],
        [k.quick - 0.1, "Leo yakın: yorum sorusu", true, "leo:yakin"],
      ],
      [
        { t: k.living, olay: "LIVING altı çizilir", tur: "vurgu", oneri: "keçeli çizgi" },
        { t: k.care, olay: "CARE altı çizilir", tur: "vurgu", oneri: "keçeli çizgi" },
        { t: k.time, olay: "TIME altı çizilir", tur: "vurgu", oneri: "keçeli çizgi" },
      ],
      [[k.the, "THE LOUD LEAK IS SMALL.", k.quick - 0.2], [k.for, "THE QUIET LEAKS ARE BIG.", k.quick - 0.2, "#ffd43b"], [k.tell, "WHICH LEAK DID YOU PICK? ↓ COMMENTS"]],
    );
  },
  S23: () => {
    const a = an("S23");
    const k = { it: a("it"), clock: a("clock") };
    return yap("S23", k, [[0, "gişenin arkasında dev yol saati", false, "saat"], [k.it - 0.1, "saat yakın", false, "saat:yakin"]], [{ t: k.clock, olay: "saat tik-tak başlar", tur: "vurgu", oneri: "saat tik" }]);
  },
  S24: () => {
    const a = an("S24");
    const k = { the: a("the", 3), you: a("you"), in: a("in", 1), but: a("but"), a: a("lot") - 0.2, and: a("waiting") - 0.2, even: a("even"), money1: a("money", 2), money2: a("money", 3), same: a("same") };
    return yap(
      "S24",
      k,
      [
        [0, "Leo: boxes arrive late", true, "leo:kapi"],
        [k.the - 0.1, "TO: THE KIDS etiketindeki siluetlerin saçı griye döner", false, "griSac"],
        [k.you - 0.1, "grafik G5: kuşak payları", false, "g5"],
        [k.a - 0.1, "Leo: middle of their lives", true, "leo:yakin"],
        [k.even - 0.1, "1 $ banknot solar: $1 → ~$0.67", false, "banknot"],
        [k.money1 - 0.1, "iki yol işareti: STARTING OUT / LATER", false, "yolIsareti"],
        [k.same - 0.1, "Leo yakın: same boxes, different job", true, "leo:yakin"],
      ],
      [
        { t: k.the + 0.6, olay: "saçlar griye döner", tur: "vurgu", oneri: "zaman atlaması" },
        { t: k.in, olay: "GEN X ~$14T (first 10 years) çubuğu", tur: "sayac", oneri: "tık" },
        { t: k.but, olay: "MILLENNIALS ~$46T (through 2048) çubuğu", tur: "sayac", oneri: "yükselen tık" },
        { t: k.even + 0.4, olay: "banknot solar, sayaç $1.00 → $0.67", tur: "sayac", oneri: "inen ton" },
        { t: k.money2, olay: "ikinci yol işareti LATER", tur: "pop", oneri: "" },
      ],
      [],
      [[k.you, "R08"], [k.even, "R21"]],
    );
  },
  S25: () => yap("S25", {}, [[0, "son viraj; ufukta TO: THE KIDS evi", false, "yer:viraj"]], [{ t: 0.3, olay: "kamyon viraja girer", tur: "kay", oneri: "lastik + motor" }]),
  // ---------- Bölüm 7 — Arrival ----------
  S26: () => {
    const a = an("S26");
    const k = { i: a("i", 1), loaded: a("loaded"), s1: a("stop", 1), s2: a("stop", 2), s3: a("stop", 3), s4: a("stop", 4), s5: a("stop", 5), s6: a("stop", 6), income: a("income"), delivered: a("delivered"), split: a("split") };
    return yap(
      "S26",
      k,
      [
        [0, "kapılar açılır, Leo panoyu okur", true, "leo:kapi"],
        [k.loaded - 0.1, "grafik G6: Okafor şelalesi (envanter)", false, "selale"],
      ],
      [
        { t: 0.2, olay: "kamyon kapıları açılır", tur: "vurgu", oneri: "metal kapı" },
        { t: k.loaded, olay: "LOADED: 10 sütunu", tur: "pop", oneri: "tok" },
        ...([1, 2, 3, 4, 5, 6] as const).map((n) => ({ t: k[`s${n}`], olay: `şelale adımı ${n}`, tur: "sayac", oneri: n === 3 || n === 6 ? "tık (kayıp yok)" : "inen tık" })),
        { t: k.income, olay: "INCOME TAX: −SLIVER (ince taralı dilim)", tur: "sayac", oneri: "ince tık" },
        { t: k.delivered, olay: "DELIVERED: 6 − SLICE − SLIVER, LATER", tur: "vurgu", oneri: "vuruş" },
        { t: k.split, olay: "ikiye bölünür: ≈3 EACH", tur: "pop", oneri: "pop ×2" },
      ],
      [],
      [[k.loaded, "ORNEK"]],
    );
  },
  S27: () => {
    const a = an("S27");
    const k = { look: a("look"), thats: a("that's"), and: a("and", 1), a2: a("smaller") - 0.4, the: a("point") - 0.15 };
    return yap(
      "S27",
      k,
      [
        [0, "iki genç siluet kutuları içeri taşır", false, "yer:varis"],
        [k.look - 0.1, "Leo panoya bakar", true, "leo:kapi"],
        [k.and - 0.1, "üç hayalet kamyon yan yana", false, "hayalet:uc"],
        [k.the - 0.1, "Leo yakın: where the boxes went", true, "leo:yakin"],
      ],
      [{ t: k.a2, olay: "boş kasa → Okafor (6) → konvoy", tur: "pop", oneri: "pop ×3" }],
      [[k.thats, "USED, NOT LOST", k.and - 0.2, "#ffd43b"]],
    );
  },
  S28: () => {
    const a = an("S28");
    const k = { now: a("now"), cerulli: a("cerulli"), and: a("and", 1), the: a("top") - 0.15, bottom: a("bottom"), so: a("so"), for: a("for", 1), thats: a("that's") };
    return yap(
      "S28",
      k,
      [
        [0, "kamera Okafor evinden yükselir, haritaya", false, "yer:harita"],
        [k.cerulli - 0.1, "grafik G7: bölünmüş tablo kartı", false, "g7"],
        [k.so - 0.1, "Leo: real, just lumpy", true, "leo:yakin"],
        [k.for - 0.1, "haritada birkaç konvoy, çok sayıda küçük kamyon", false, "yer:konvoy"],
        [k.thats - 0.1, "Leo: both be right", true, "leo:kapi"],
      ],
      [
        { t: k.cerulli + 0.5, olay: "100 haneden 2'si turuncu", tur: "vurgu", oneri: "tık ×2" },
        { t: k.and + 0.3, olay: "ayrı panel DFA: TOP 10% ≈ 69%", tur: "sayac", oneri: "yükselen tık" },
        { t: k.bottom, olay: "BOTTOM 50% ≈ 2%", tur: "pop", oneri: "küçük tık" },
      ],
      [[k.so, "THE HEADLINE IS REAL. IT'S JUST LUMPY.", k.for - 0.2]],
      [[k.cerulli, "R07"], [k.and, "R24"]],
    );
  },
  S29: () => {
    const a = an("S29");
    const k = { if1: a("if", 1), if2: a("if", 2), this: a("this", 2) };
    return yap(
      "S29",
      k,
      [
        [0, "yol haritası (tek yol)", false, "yolHaritasi"],
        [k.this - 0.1, "Leo yakın: not a forecast", true, "leo:yakin"],
      ],
      [
        { t: k.if1 + 0.4, olay: "CARE tabelası kesik çizgiyle büyür", tur: "vurgu", oneri: "" },
        { t: k.if2 + 0.4, olay: "TAX tabelası kesik çizgiyle kayar", tur: "vurgu", oneri: "" },
      ],
      [[k.this + 0.2, "NOT A FORECAST. NOT A PLAN. A MAP."]],
    );
  },
  S30: () => {
    const a = an("S30");
    const k = { picture: a("picture"), an: a("an"), and: a("and"), tape: a("tape"), abone: aboneAn("S30") };
    return yap(
      "S30",
      k,
      [
        [0, "Leo kamyon yanında: $124T", true, "leo:kapi"],
        [k.an - 0.1, "tez yazısı yakın plan", false, "tez"],
        [k.and - 0.1, "Leo boş kutuyu bırakır, ince ruloyu omzuna atar (sol-orta)", true, "leo:kapi"],
      ],
      [
        { t: k.picture, olay: "kamyon görünür", tur: "pop", oneri: "" },
        { t: k.tape, olay: "rulo omza (karakter anı)", tur: "vurgu", oneri: "kısa müzik vurgusu" },
        abone("S30", 3, "sağ alt boş; Leo sol-orta"),
      ],
      [],
      [[0, "R01"]],
    );
  },
  S31: () => {
    const a = an("S31");
    const k = { the: a("the", 1), what: a("what") };
    return yap(
      "S31",
      k,
      [
        [0, "kiremit kutu kamyonda tek başına parlar", false, "kutular:yalniz"],
        [k.what - 0.1, "kamera yola döner, ufukta ışıklı mahalle", false, "yer:mahalle"],
      ],
      [{ t: k.the, olay: "kiremit kutu parlar", tur: "vurgu", oneri: "sıcak tını" }],
    );
  },
};

export const ZAMAN = P;
export const plan = (id: string): Plan => {
  const f = P[id];
  if (!f) throw new Error(`zaman planı yok: ${id}`);
  return f();
};
export { SAHNELER };
