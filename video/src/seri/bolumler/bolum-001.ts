// Flip By Vote · Bölüm 001 "Every Dollar We Have" — kesme listesi (animasyon-yonetmeni 2026-11-11).
// Metin/çekim sözlüğü: uretim/seri/bolum-001/metin.md · ses kilidi: uretim/seri/bolum-001/ses/kilit.md (78,77 sn, sha 289da660bbd0).
// Zamanlar kilitli satır zamanlarından (bolum-001.satirlar.json) ve Whisper kelimelerinden; kesme = satır başından ~0,1 sn önce.
// Görsel olaylar (SFX'e bağlananlar) ve abone anı: uretim/seri/bolum-001/animasyon-efekt-cue.json (aynı sayılar, kare doğru).
// Ses stem'i (müzik + SFX, şablon efektleri dahil) muzik-ses-tasarimcisi'nin bolum-ses.py'si ile o dosyadan üretilir → sablonSfx:false.
import type { AgizDosyasi, Bolum, Prop, Sahne, ZamanJson } from "../tipler";
import { satirDosyasi, type WhisperKelimeler } from "../zaman";
import agizJson from "./bolum-001.agiz.json";
import kelimelerJson from "./bolum-001.kelimeler.json";
import satirlarJson from "./bolum-001.satirlar.json";
import { MUTFAK_L1 } from "./mekan-l1";

const satirlar = satirDosyasi(satirlarJson as ZamanJson, kelimelerJson as WhisperKelimeler);

// tezgâhtaki banknot (geniş plaka pikseli; tekli çekimde plakayla birlikte 1,25 ölçeklenir)
const BANKNOT_TEZGAH = { x: 545, y: 1470, aci: -7 };
const banknot = (bas: number): Prop => ({ tur: "banknot", bas, ...BANKNOT_TEZGAH });

/** Kesme listesi: [id, bas, bitis, çekim anahtarı, ek]. Çekim anahtarı: genis | yakin:kim | portre:kim:ifade | tahta. */
type Ek = Partial<Pick<Sahne, "kamera" | "proplar" | "vurus" | "sarsinti" | "odak">>;
const K: [string, number, number, string, Ek?][] = [
  // S1 — KANCA (tur 2, Ö2): tezgâh insert'i, kamera kare 0'da hareket halinde (1,45 → 1,22, out eğrisi);
  // büyük banknot 3 karede düşer, kare 3'te (0,1 sn) çarpar (SFX onset) + 2 karelik sarsıntı; BANK pop
  ["s01", 0, 0.6, "genis", {
    kamera: { zoom: [1.45, 1.22], egri: "out", kay: { y: [60, 0] } }, odak: { x: 545, y: 1380 },
    proplar: [{ tur: "banknot", bas: 0, dus: true, yukseklik: 380, ...BANKNOT_TEZGAH, y: 1300, olcek: 1.7 }], sarsinti: [{ t: 0.1, sure: 0.07, guc: 18 }],
  }],
  ["s02", 0.6, 2.55, "yakin:mike", { kamera: { zoom: [1.08, 1.13] } }], // M01 hızlı punch-in
  ["s03", 2.55, 7.1, "yakin:jake", { kamera: { zoom: [1.02, 1.08] }, proplar: [{ tur: "ikon", ad: "hardal", bas: 4.6, bitis: 5.5, x: 205, y: 800, boyut: 170 }] }],
  // S2 — tahta "$100" (SFX 7,206), Mike, Jake, tahta "$1,000,000" sıfırlar tek tek (12,588 … 13,188), "You do" → YOU DECIDE
  ["s04", 7.1, 8.4, "tahta", { kamera: { zoom: [1.14, 1.2] } }],
  ["s05", 8.4, 10.06, "yakin:mike", { kamera: { zoom: [1.03, 1.08] } }],
  ["s06", 10.06, 12.05, "yakin:jake", { kamera: { zoom: [1.04, 1.1] } }],
  ["s07", 12.05, 13.72, "tahta", { kamera: { zoom: [1.12, 1.22] } }],
  ["s08", 13.72, 16.75, "yakin:jake", { kamera: { zoom: [1.02, 1.06] }, vurus: [{ t: 16.04, olcek: 1.1, sure: 0.12 }], proplar: [{ tur: "yazi", metin: "YOU DECIDE", bas: 16.04, bitis: 17.15, y: 860 }] }],
  ["s09", 16.75, 17.15, "portre:jake:gulen", { kamera: { zoom: [1.0, 1.02] }, proplar: [{ tur: "yazi", metin: "YOU DECIDE", bas: 16.04, bitis: 17.15, y: 860 }] }],
  // S3 — telefon alttan (17,303), 3 ilan
  ["s10", 17.15, 20.2, "genis", {
    kamera: { zoom: [1.04, 1.09] },
    proplar: [banknot(0), { tur: "telefon", bas: 17.2, bitis: 20.2, ogeler: [{ ikon: "bisiklet", fiyat: "$60" }, { ikon: "sifonyer", fiyat: "FREE" }, { ikon: "kutu", fiyat: "$40" }] }],
  }],
  ["s11", 20.2, 22.8, "yakin:jake", { kamera: { zoom: [1.03, 1.07] } }],
  ["s12", 22.8, 24.02, "yakin:mike", { kamera: { zoom: [1.06, 1.1] } }],
  ["s13", 24.02, 24.5, "portre:mike:gulen", { kamera: { zoom: [1.0, 1.02] } }], // sırıtma (sessiz)
  // S4 — ilan ROAD BIKE alçak kart (whoosh apex 24,6; yüz açık), "Flat tires" punch, "look at that frame!" sıçrama kesmesi + bisiklet pop
  ["s14", 24.5, 27.62, "yakin:mike", { kamera: { zoom: [1.02, 1.06] }, vurus: [{ t: 26.52, olcek: 1.06, sure: 0.1 }], proplar: [{ tur: "ilan", yer: "alt", bas: 24.5, bitis: 26.75, ikon: "bisiklet", baslik: "ROAD BIKE", fiyat: "$60", not: "flat tires" }] }],
  ["s14b", 27.62, 29.55, "yakin:mike", { kamera: { zoom: [1.16, 1.22] }, proplar: [{ tur: "ikon", ad: "bisiklet", bas: 28.6, bitis: 29.55, x: 220, y: 880, boyut: 190 }] }],
  ["s15", 29.55, 32.48, "yakin:jake", { kamera: { zoom: [1.02, 1.05] }, vurus: [{ t: 31.48, olcek: 1.08, sure: 0.1 }], proplar: [{ tur: "tahtaKose", bas: 29.9, bitis: 32.48, yaz: 30.44, metin: "$100 − $60 = $40", x: 80, y: 870 }] }],
  ["s16", 32.48, 33.92, "genis", { kamera: { zoom: [1.03, 1.06] }, proplar: [banknot(0)] }],
  // "Tires aren't." sert punch-in (33,95), satır sonrası sessiz tutuş; plak cızırtısının ardından Mike'ın yüzü düşer (görsel gag)
  ["s17", 33.92, 35.3, "yakin:jake", { kamera: { zoom: [1.02, 1.03] }, vurus: [{ t: 33.95, olcek: 1.24, sure: 0.08 }] }],
  ["s18", 35.3, 35.7, "portre:mike:endiseli", { kamera: { zoom: [1.0, 1.03] } }],
  // S5 — ilan DRESSER alçak kart (37,5), "We paint it, flip it" sıçrama kesmesi + boya pop; "Free?" = konuşan tabana punch-in (Z3)
  ["s19", 35.7, 39.3, "yakin:jake", { kamera: { zoom: [1.02, 1.07] }, proplar: [{ tur: "ilan", yer: "alt", bas: 37.38, bitis: 39.3, ikon: "sifonyer", baslik: "DRESSER", fiyat: "FREE", not: "must go today" }] }],
  ["s19b", 39.3, 41.38, "yakin:jake", { kamera: { zoom: [1.16, 1.2] }, proplar: [{ tur: "ikon", ad: "boya", bas: 39.64, bitis: 41.38, x: 220, y: 880, boyut: 180 }] }],
  ["s20", 41.38, 43.5, "yakin:mike", { kamera: { zoom: [1.04, 1.06] }, vurus: [{ t: 41.45, olcek: 1.2, sure: 0.08 }], sarsinti: [{ t: 41.45, sure: 0.1, guc: 8 }] }],
  ["s22", 43.5, 47.25, "yakin:jake", { kamera: { zoom: [1.02, 1.05] }, vurus: [{ t: 46.18, olcek: 1.12, sure: 0.1 }], proplar: [{ tur: "ikon", ad: "araba", bas: 46.18, bitis: 47.25, x: 220, y: 880, boyut: 180 }] }],
  ["s23", 47.25, 48.12, "portre:jake:endiseli", {
    kamera: { zoom: [1.0, 1.03] },
    proplar: [{ tur: "ikonSira", bas: 47.25, bitis: 48.12, y: 400, ayrac: "↔", boyut: 200, ogeler: [{ ad: "araba", t: 47.349 }, { ad: "sifonyer", t: 47.699 }] }],
  }],
  ["s24", 48.12, 51.15, "yakin:mike", {
    kamera: { zoom: [1.03, 1.07] },
    proplar: [{ tur: "ikonSira", bas: 48.12, bitis: 51.15, y: 880, boyut: 170, ogeler: [{ ad: "kamyon", t: 48.76 }, { ad: "boya", t: 49.14 }, { ad: "saat", t: 49.58 }] }],
  }],
  ["s25", 51.15, 53.48, "yakin:jake", { kamera: { zoom: [1.03, 1.11] } }], // "Slow. But safe." hafif push-in
  // S6 — Mike kadraja eğilir; ilan GARAGE SALE BOX alçak kart (53,51), kapak titrer (54,7); "Forty bucks" punch; kartuş / çizik diskler
  ["s26", 53.48, 57.62, "yakin:mike", {
    kamera: { zoom: [1.0, 1.14] }, vurus: [{ t: 56.56, olcek: 1.06, sure: 0.1 }],
    proplar: [{ tur: "ilan", yer: "alt", bas: 53.48, bitis: 56.3, ikon: "kutu", baslik: "GARAGE SALE BOX", fiyat: "$40", not: "old games", titre: 54.7 }],
  }],
  ["s27", 57.62, 62.0, "yakin:jake", {
    kamera: { zoom: [1.02, 1.05] }, vurus: [{ t: 60.34, olcek: 1.08, sure: 0.1 }],
    proplar: [{ tur: "ikonSira", bas: 57.62, bitis: 62.0, y: 860, ayrac: "/", boyut: 200, ogeler: [{ ad: "kartus", t: 58.26 }, { ad: "disk", t: 60.674 }] }],
  }],
  // S7 — 1,0 sn sessiz bakışma, banknot ortada, yavaş push-in (gerilim 62,019)
  ["s28", 62.0, 63.08, "genis", { kamera: { zoom: [1.04, 1.1] }, odak: { x: 540, y: 1100 }, proplar: [banknot(0)] }],
  ["s29", 63.08, 65.88, "yakin:mike", { kamera: { zoom: [1.04, 1.12] } }],
  ["s30", 65.88, 70.95, "yakin:jake", { kamera: { zoom: [1.01, 1.05] }, proplar: [banknot(0)] }],
  ["s31", 70.95, 71.4, "portre:jake:dusunceli", { kamera: { zoom: [1.0, 1.02] } }], // iç çekiş (sessiz)
  ["s32", 71.4, 74.45, "yakin:jake", { kamera: { zoom: [1.03, 1.07] }, proplar: [banknot(0)] }],
  // S8 — Mike soruyu sorar (geniş, kamera ortaya); karar kartı "box?"tan sonraki boşlukta (76,0) girer (whoosh kelimeye binmez, Ö1);
  // 78,59 ikisi kameraya: "Ep. 2: YOUR call" + ding; karar kartı 81,0'da çıkar, takip kartı 81,0–83,2 (çakışmasız, kısa kuyruk)
  ["s33", 74.45, 78.59, "genis", { kamera: { zoom: [1.02, 1.08] }, proplar: [banknot(0)] }],
  ["s34", 78.59, 83.2, "ikiPortre", { kamera: { zoom: [1.0, 1.04] } }],
];

const IKI_PORTRE = { sol: { kim: "mike" as const, ifade: "heyecanli" }, sag: { kim: "jake" as const, ifade: "dusunceli" } };

const sahneler: Sahne[] = K.map(([id, bas, bitis, anahtar, ek]) => {
  const [tur, kim, ifade] = anahtar.split(":");
  const cekim =
    tur === "genis" ? ({ tur: "genis" } as const)
      : tur === "tahta" ? ({ tur: "tahta" } as const)
        : tur === "ikiPortre" ? ({ tur: "ikiPortre", ...IKI_PORTRE } as const)
          : tur === "yakin" ? ({ tur: "yakin", kim: kim as "jake" | "mike" } as const)
            : ({ tur: "portre", kim: kim as "jake" | "mike", ifade } as const);
  // tahta yazıları her tahta çekiminde (yazılmış olan kalır)
  const tahta: Prop[] = tur === "tahta"
    ? [{
        tur: "tahtaYazi", bas: 0, satirlar: [
          { metin: "$100", x: 600, y: 300, boyut: 120, t: 7.206, sure: 0.5 },
          { metin: "GOAL:", x: 604, y: 470, boyut: 56, t: 12.05, sure: 0.01, renk: "#b3261e" },
          { metin: "$1,000,000", x: 575, y: 540, boyut: 62, t: 12.138, sure: 0.3, renk: "#b3261e", tik: [12.588, 12.708, 12.828, 12.948, 13.068, 13.188] },
        ],
      }]
    : [];
  return { id, bas, bitis, arka: MUTFAK_L1.genis, cekim, ...ek, proplar: [...tahta, ...(ek?.proplar ?? [])] };
});

export const B001: Bolum = {
  id: "FBV-B001",
  no: 1,
  sure: 83.2,
  satirlar,
  agiz: agizJson as AgizDosyasi,
  agizYolu: "yama",
  mekan: MUTFAK_L1,
  sahneler,
  bank: { baslangic: 100, olaylar: [{ t: 0.1, deger: 100, ses: false }] }, // BANK $100 tüm bölüm; açılışta yalnız pop
  ses: {
    diyalog: "seri/bolum-001/diyalog.wav",
    muzik: { dosya: "seri/bolum-001/muzik-stem.wav", ses: 1 },
    sfx: { dosya: "seri/bolum-001/sfx-stem.wav", ses: 1 },
    sablonSfx: false,
  },
  karar: {
    soru: "Bike, dresser, or mystery box?",
    secenekler: ["ROAD BIKE $60", "FREE DRESSER", "MYSTERY BOX $40"],
    ikonlar: ["bisiklet", "sifonyer", "kutu"],
    bas: 76.0,
    sure: 5,
    kapanis: 78.59,
  },
  abone: { bas: 81.0, ust: 1010, sure: 2.2, klik: 0.9 },
  damga: { ust: 262, olcek: 0.55, sag: true }, // "EP. 1" çipi sağ üst köşe (BANK sol üstte), kancayı örtmez
};
