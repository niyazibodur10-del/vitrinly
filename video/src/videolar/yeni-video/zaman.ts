// TEK KAYNAK zaman planı (animasyon-yonetmeni): sahne kodu, efekt cue'ları (06-muzik/animasyon-efekt-cue.json) ve
// ağzın göründüğü aralıklar (07-animasyon/agiz-gorunur.json) bu fonksiyonlardan üretilir → hiçbiri kayamaz.
// Saf TS (React yok): 07-animasyon/olay-cikar.mjs esbuild ile paketleyip node'da çalıştırır.
// Zamanlar sahne YEREL saniyesi; kelime çapası (an(id)("word", n)) — ses değişince kendini günceller, eksik kelime hata fırlatır.
import { SAHNELER } from "./veri-sahne";

export type Olay = { t: number; olay: string; tur: string; oneri?: string };
export type Plan = { k: Record<string, number>; olay: Olay[]; agiz: [number, number][] };

const norm = (w: string) => w.toLowerCase().replace(/[^a-z0-9$'-]/g, "");
export const sure = (id: string) => SAHNELER.find((s) => s.id === id)!.sure;
export const an = (id: string) => {
  const s = SAHNELER.find((x) => x.id === id)!;
  return (w: string, n = 1, son = false): number => {
    const hedef = norm(w);
    let say = 0;
    for (const k of s.kelimeler) if (norm(k.w) === hedef && ++say === n) return son ? k.e : k.s;
    throw new Error(`${id}: kelime yok: ${w} #${n}`);
  };
};
// Abone anları (metin ABONE-1..3): sahne sonundaki 1,5 sn nefesin başı (son kelime bitişi + 0,15)
export const ABONE_SAHNE = ["S07", "S12", "S26"] as const;
export const aboneAn = (id: string) => {
  const s = SAHNELER.find((x) => x.id === id)!;
  return s.kelimeler[s.kelimeler.length - 1].e + 0.15;
};

const P: Record<string, () => Plan> = {
  S01: () => {
    const a = an("S01");
    const k = {
      ev: 1.9,
      brings: a("brings"),
      five: a("five"),
      spends: a("spends"),
      seven: a("seven"),
      eksi: a("hundred", 2, true),
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
    };
  },
};

export const ZAMAN = P;
export const plan = (id: string): Plan => {
  const f = P[id];
  if (!f) throw new Error(`zaman planı yok: ${id}`);
  return f();
};
