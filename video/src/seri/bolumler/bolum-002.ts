// Flip By Vote · Bölüm 002 "Meet Brenda" — kesme listesi (animasyon-yonetmeni 2026-11-12).
// Metin/çekim sözlüğü: uretim/seri/bolum-002/metin.md · ses kilidi: uretim/seri/bolum-002/ses/kilit.json (Pocket TTS, 85,07 sn, sha a28f95e61c03).
// Zamanlar kilitli satır + Whisper kelime zamanlarından (bolum-002.satirlar.json / .kelimeler.json); kesme = satır başından ~0,1 sn önce.
// Görsel olaylar → uretim/seri/bolum-002/animasyon-efekt-cue.json → bolum-ses.py cevir --gorsel (stem) · sablonSfx:false.
// Bölüm 1 dersleri: Z1 altyazı kilitli metinden · Z2 kırpma kapısı · Z4 rozet yüzden uzak · kanca kare 0'da hareket · 2–3 kesme/ilan.
import type { AgizDosyasi, Bolum, MekanSeti, Prop, Sahne, ZamanJson } from "../tipler";
import { satirDosyasi, type WhisperKelimeler } from "../zaman";
import agizJson from "./bolum-002.agiz.json";
import kelimelerJson from "./bolum-002.kelimeler.json";
import satirlarJson from "./bolum-002.satirlar.json";
import { MUTFAK_L1 } from "./mekan-l1";
import { GARAJ_YOLU_L3 } from "./mekan-l3";

const satirlar = satirDosyasi(satirlarJson as ZamanJson, kelimelerJson as WhisperKelimeler);

// Brenda (bisiklet): 1600x917, zemin satırı basık 859 / şişik 883; teker daireleri bisiklet.json
const BB = "seri/bolum-002/nesne/bisiklet-basik.png", BS = "seri/bolum-002/nesne/bisiklet-sisik.png";
const TEKER = [{ cx: 357, cy: 563, r: 328 }, { cx: 1272, cy: 572, r: 311 }];
const bisiklet = (o: Partial<Extract<Prop, { tur: "nesne" }>> & { bas: number; x0: number; zeminY: number; olcek: number }): Prop =>
  ({ tur: "nesne", dosya: BB, w: 1600, h: 917, zemin: 859, ...o });
const brendaL3: Prop = { tur: "nesne", bas: 0, dosya: BS, w: 1600, h: 917, zemin: 883, olcek: 0.33, x0: 276, zeminY: 1250, uzay: "sahne" };

const MSJ_UCUZ = { metin: "sorry, found one cheaper", t: 53.45 };
const MSJ_90 = { metin: "$90 cash, today?", t: 58.45 };

type Ek = Partial<Pick<Sahne, "kamera" | "proplar" | "vurus" | "sarsinti" | "odak">> & { mekan?: MekanSeti };
const L3 = GARAJ_YOLU_L3;
const K: [string, number, number, string, Ek?][] = [
  // S1 — KANCA K1: kare 0'da Mike'ın yüzü + Brenda sağdan yuvarlanır (kamera hareket halinde); üst bant 0–3 sn önceki seçim (BIKE ✓) + ilerleme şeridi
  ["s01", 0, 3.37, "yakin:mike", {
    kamera: { zoom: [1.14, 1.06], egri: "out" },
    proplar: [
      bisiklet({ bas: 0, x0: 860, x1: 430, hareketSure: 1.2, zeminY: 1945, olcek: 0.7, ziplama: 8, etiket: { metin: "BRENDA", t: 2.5, x: 420, y: -380 } }),
      { tur: "oncekiSecim", bas: 0, bitis: 3.0, secenekler: ["BIKE", "DRESSER", "BOX"], secilen: 0, tikT: 0.86 },
      { tur: "cip", bas: 0, bitis: 3.0, y: 338, boyut: 26, metinler: [{ metin: "EP. 2 · BANK $100 → $1,000,000", t: 0 }] },
    ],
  }],
  // S2 — "flat tires": tekerlere kırmızı halka; "Please" sonrası kameraya bakış (nötr portre, sessiz)
  ["s02", 3.37, 6.25, "yakin:jake", { kamera: { zoom: [1.02, 1.07] }, proplar: [bisiklet({ bas: 0, x0: -170, zeminY: 1640, olcek: 0.5, halkalar: TEKER, halkaT: 5.26 })] }],
  ["s03", 6.25, 7.7, "yakin:mike", { kamera: { zoom: [1.04, 1.11] }, proplar: [bisiklet({ bas: 0, x0: 380, zeminY: 1700, olcek: 0.6 })] }],
  ["s04", 7.7, 9.9, "yakin:jake", { kamera: { zoom: [1.02, 1.06] } }],
  ["s05", 9.9, 10.5, "portre:jake:notr", { kamera: { zoom: [1.0, 1.02] } }],
  // S3 — "Sixty" BANK −$60 → $40 + köşe tahta; "Day 2" çipi; "So, no." sert punch-in; seri no kontrolü
  ["s06", 10.5, 12.7, "genis", {
    kamera: { zoom: [1.03, 1.07] },
    proplar: [
      { tur: "tahtaKose", bas: 10.6, bitis: 12.7, yaz: 10.74, metin: "$100 − $60 = $40", x: 80, y: 870 },
      { tur: "cip", bas: 10.6, bitis: 12.6, y: 338, boyut: 30, metinler: [{ metin: "DAY 2", t: 10.6 }] },
    ],
  }],
  ["s07", 12.7, 13.85, "yakin:mike", { kamera: { zoom: [1.05, 1.08] } }],
  ["s08", 13.85, 17.7, "yakin:jake", {
    kamera: { zoom: [1.02, 1.04] }, vurus: [{ t: 14.04, olcek: 1.18, sure: 0.08 }],
    proplar: [{ tur: "mesaj", bas: 15.6, bitis: 17.7, baslik: "Serial check", mesajlar: [{ metin: "SERIAL CHECK ✓", t: 15.84, onay: true }, { metin: "not reported stolen", t: 16.38 }] }],
  }],
  ["s09", 17.7, 20.05, "yakin:mike", { kamera: { zoom: [1.03, 1.08] }, proplar: [bisiklet({ bas: 0, x0: 400, zeminY: 1720, olcek: 0.55 })] }],
  // S4 — pompa ×3, PAT (ikinci kanca: şaşkın portre + sarsıntı + iç lastik), "$8 × 2" ve BANK −$16 → $24, donut
  ["s10", 20.05, 23.98, "genis", {
    kamera: { zoom: [1.03, 1.09] },
    proplar: [
      bisiklet({ bas: 0, x0: 250, zeminY: 1640, olcek: 0.5 }),
      { tur: "ikon", ad: "pompa", bas: 20.44, bitis: 21.1, x: 240, y: 1080, boyut: 170 },
      { tur: "ikon", ad: "pompa", bas: 21.4, bitis: 22.0, x: 240, y: 1080, boyut: 185 },
      { tur: "ikon", ad: "pompa", bas: 22.3, bitis: 23.98, x: 240, y: 1080, boyut: 200 },
    ],
  }],
  ["s11", 23.98, 25.3, "portre:mike:saskin", {
    kamera: { zoom: [1.0, 1.04] }, sarsinti: [{ t: 24.0, sure: 0.07, guc: 18 }],
    proplar: [{ tur: "ikon", ad: "iclastik", bas: 24.05, bitis: 25.3, x: 300, y: 300 + 600, boyut: 210 }],
  }],
  ["s12", 25.3, 27.6, "yakin:jake", { kamera: { zoom: [1.02, 1.06] } }],
  ["s13", 27.6, 31.0, "yakin:jake", {
    kamera: { zoom: [1.13, 1.15] },
    proplar: [{ tur: "ikonSira", bas: 27.6, bitis: 31.0, y: 860, boyut: 170, ayrac: "+", ogeler: [{ ad: "iclastik", t: 28.42 }, { ad: "iclastik", t: 28.62, etiket: "$8 × 2" }] }],
  }],
  ["s14", 31.0, 33.1, "yakin:mike", {
    kamera: { zoom: [1.03, 1.09] },
    proplar: [{ tur: "ikonSira", bas: 31.0, bitis: 33.1, y: 860, boyut: 170, ogeler: [{ ad: "donut", t: 32.22 }, { ad: "donut", t: 32.36 }] }],
  }],
  ["s15", 33.1, 35.2, "yakin:jake", { kamera: { zoom: [1.02, 1.06] } }],
  ["s16", 35.2, 35.7, "portre:jake:gulen", { kamera: { zoom: [1.0, 1.02] } }], // küçük zafer (sessiz)
  // S5 — ilan $140 (şişik Brenda), tahta hesabı, "On my way!"
  ["s17", 35.7, 38.75, "yakin:mike", {
    kamera: { zoom: [1.02, 1.07] },
    proplar: [{ tur: "ilan", yer: "alt", bas: 37.1, bitis: 38.75, ikon: "bisiklet", gorsel: BS, baslik: "ROAD BIKE", fiyat: "$140", not: "rides great" }],
  }],
  ["s18", 38.75, 43.35, "tahta", {
    kamera: { zoom: [1.12, 1.2] },
    proplar: [{
      tur: "tahtaYazi", bas: 0, satirlar: [
        { metin: "$60 + $16", x: 585, y: 290, boyut: 66, t: 38.98, sure: 0.4 },
        { metin: "= $76", x: 625, y: 372, boyut: 66, t: 39.42, sure: 0.3 },
        { metin: "$140 − $76", x: 585, y: 480, boyut: 62, t: 40.46, sure: 0.45, renk: "#1f3f8f" },
        { metin: "= $64?", x: 625, y: 560, boyut: 70, t: 41.24, sure: 0.3, renk: "#b3261e" },
      ],
    }],
  }],
  ["s19", 43.35, 47.95, "yakin:mike", {
    kamera: { zoom: [1.02, 1.08] },
    proplar: [{ tur: "mesaj", bas: 46.7, bitis: 47.95, mesajlar: [{ metin: "On my way!", t: 46.98 }] }],
  }],
  // S6 — mekân değişimi L3 (üçüncü kanca serisi): saat 2:00 → 2:45 PM, gelmeyen alıcı, "sorry, found one cheaper"
  ["s20", 47.95, 49.3, "bos", {
    mekan: L3, kamera: { zoom: [1.0, 1.07] },
    proplar: [brendaL3, { tur: "cip", ortala: true, bas: 47.95, bitis: 49.3, y: 470, boyut: 80, metinler: [{ metin: "2:00 PM", t: 47.95 }, { metin: "2:15 PM", t: 48.4 }, { metin: "2:30 PM", t: 48.7 }, { metin: "2:45 PM", t: 48.95 }] }],
  }],
  ["s21", 49.3, 50.5, "yakin:jake", { mekan: L3, kamera: { zoom: [1.03, 1.06] } }],
  ["s22", 50.5, 51.7, "yakin:mike", { mekan: L3, kamera: { zoom: [1.04, 1.07] } }],
  ["s23", 51.7, 53.4, "yakin:jake", { mekan: L3, kamera: { zoom: [1.02, 1.04] }, vurus: [{ t: 51.84, olcek: 1.08, sure: 0.1 }] }],
  ["s24", 53.4, 54.1, "portre:mike:endiseli", { mekan: L3, kamera: { zoom: [1.0, 1.03] }, proplar: [{ tur: "mesaj", bas: 53.4, bitis: 55.3, mesajlar: [MSJ_UCUZ] }] }],
  ["s25", 54.1, 58.4, "yakin:mike", { mekan: L3, kamera: { zoom: [1.02, 1.12] }, proplar: [{ tur: "mesaj", bas: 53.4, bitis: 55.3, mesajlar: [MSJ_UCUZ] }] }],
  // S7 — yeni mesaj "$90 cash, today?" (ding), hesaplar köşe tahtada, "yazıyor…"
  ["s26", 58.4, 59.4, "bos", { mekan: L3, kamera: { zoom: [1.04, 1.1] }, proplar: [brendaL3, { tur: "mesaj", bas: 58.4, bitis: 60.6, mesajlar: [MSJ_UCUZ, MSJ_90] }] }],
  ["s27", 59.4, 62.5, "yakin:mike", { mekan: L3, kamera: { zoom: [1.03, 1.08] }, proplar: [{ tur: "mesaj", bas: 58.4, bitis: 60.6, mesajlar: [MSJ_UCUZ, MSJ_90] }] }],
  ["s28", 62.5, 66.8, "yakin:jake", { mekan: L3, kamera: { zoom: [1.02, 1.07] }, proplar: [{ tur: "tahtaKose", bas: 62.8, bitis: 66.8, yaz: 63.3, metin: "$90 − $76 = $14", x: 80, y: 870 }] }],
  ["s29", 66.8, 72.5, "yakin:mike", { mekan: L3, kamera: { zoom: [1.0, 1.12] }, vurus: [{ t: 71.54, olcek: 1.06, sure: 0.1 }] }],
  ["s30", 72.5, 74.45, "yakin:jake", { mekan: L3, kamera: { zoom: [1.02, 1.06] }, proplar: [{ tur: "ikon", ad: "saat", bas: 73.68, bitis: 74.45, x: 220, y: 880, boyut: 180 }] }],
  ["s31", 74.45, 77.75, "yakin:mike", { mekan: L3, kamera: { zoom: [1.03, 1.08] }, proplar: [{ tur: "tahtaKose", bas: 76.3, bitis: 77.75, yaz: 76.48, metin: "$115?", x: 80, y: 870 }] }],
  ["s32", 77.75, 80.5, "yakin:jake", { mekan: L3, kamera: { zoom: [1.02, 1.07] }, proplar: [{ tur: "mesaj", bas: 78.25, bitis: 81.0, mesajlar: [{ ...MSJ_90, t: 0 }], yaziyor: 78.4 }] }],
  ["s33", 80.5, 81.0, "portre:jake:dusunceli", { mekan: L3, kamera: { zoom: [1.0, 1.02] }, proplar: [{ tur: "mesaj", bas: 78.25, bitis: 81.0, mesajlar: [{ ...MSJ_90, t: 0 }], yaziyor: 78.4 }] }],
  // S8 — mutfak geniş; karar kartı "Take" öncesi boşlukta (81,0) girer; 84,9 ikisi kameraya + "Ep. 3: YOUR call"; takip kartı 86,05–88,25
  ["s34", 81.0, 84.9, "genis", { kamera: { zoom: [1.02, 1.08] } }],
  ["s35", 84.9, 88.25, "ikiPortre", { kamera: { zoom: [1.0, 1.04] } }],
];

const IKI_PORTRE = { sol: { kim: "mike" as const, ifade: "heyecanli" }, sag: { kim: "jake" as const, ifade: "dusunceli" } };

const sahneler: Sahne[] = K.map(([id, bas, bitis, anahtar, ek]) => {
  const [tur, kim, ifade] = anahtar.split(":");
  const cekim =
    tur === "genis" ? ({ tur: "genis" } as const)
      : tur === "tahta" ? ({ tur: "tahta" } as const)
        : tur === "bos" ? ({ tur: "bos" } as const)
          : tur === "ikiPortre" ? ({ tur: "ikiPortre", ...IKI_PORTRE } as const)
            : tur === "yakin" ? ({ tur: "yakin", kim: kim as "jake" | "mike" } as const)
              : ({ tur: "portre", kim: kim as "jake" | "mike", ifade } as const);
  const mk = ek?.mekan ?? MUTFAK_L1;
  return { id, bas, bitis, arka: mk.genis, cekim, ...ek, mekan: mk, proplar: ek?.proplar ?? [] };
});

export const B002: Bolum = {
  id: "FBV-B002",
  no: 2,
  sure: 88.25,
  satirlar,
  agiz: agizJson as AgizDosyasi,
  agizYolu: "yama",
  mekan: MUTFAK_L1,
  sahneler,
  bank: { baslangic: 100, olaylar: [{ t: 10.74, deger: 40 }, { t: 30.22, deger: 24 }] }, // "Sixty" −$60 · "each" −$16 (incil §4.1)
  ses: {
    diyalog: "seri/bolum-002/diyalog.wav",
    muzik: { dosya: "seri/bolum-002/muzik-stem.wav", ses: 1 },
    sfx: { dosya: "seri/bolum-002/sfx-stem.wav", ses: 1 },
    sablonSfx: false,
  },
  karar: {
    soru: "Take the ninety, hold out, or counter?",
    secenekler: ["TAKE $90", "HOLD OUT $140", "COUNTER $115"],
    bas: 81.0,
    sure: 5,
    kapanis: 84.9,
  },
  abone: { bas: 86.05, ust: 1010, sure: 2.2, klik: 0.9 },
  logo: "seri/ortak/flipbyvote-profil.png",
  damga: false, // bölüm 2+: tanıtım = önceki seçim kartı + ilerleme şeridi (incil §8)
};
