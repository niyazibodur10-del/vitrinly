// Flip By Vote · Bölüm 001 "Every Dollar We Have" — kesme listesi (animasyon-yonetmeni 2026-11-11).
// Metin/çekim sözlüğü: uretim/seri/bolum-001/metin.md · ses kilidi: uretim/seri/bolum-001/ses/kilit.json (Pocket TTS, 69,32 sn, sha 1d0d8235acd4).
// Satır içi yorumlardaki saniyeler ESKİ sese (78,8 sn) aittir; geçerli değer tablodaki sayıdır.
// 2026-11-11 ses değişimi: tüm zamanlar uretim/seri/bolum-001/animasyon/zaman-esle.py ile (eski→yeni kelime çapaları, LCS) taşındı.
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
  ["s01", 0, 0.455, "genis", {
    kamera: { zoom: [1.45, 1.22], egri: "out", kay: { y: [60, 0] } }, odak: { x: 545, y: 1380 },
    proplar: [{ tur: "banknot", bas: 0, dus: true, yukseklik: 380, ...BANKNOT_TEZGAH, y: 1300, olcek: 1.7 }], sarsinti: [{ t: 0.1, sure: 0.07, guc: 18 }],
  }],
  ["s02", 0.455, 1.961, "yakin:mike", { kamera: { zoom: [1.08, 1.13] } }], // M01 hızlı punch-in
  ["s03", 1.961, 5.115, "yakin:jake", { kamera: { zoom: [1.02, 1.08] }, proplar: [{ tur: "ikon", ad: "hardal", bas: 3.42, bitis: 4.016, x: 205, y: 800, boyut: 170 }] }],
  // S2 — tahta "$100" (SFX 7,206), Mike, Jake, tahta "$1,000,000" sıfırlar tek tek (12,588 … 13,188), "You do" → YOU DECIDE
  ["s04", 5.115, 6.095, "tahta", { kamera: { zoom: [1.14, 1.2] } }],
  ["s05", 6.095, 7.333, "yakin:mike", { kamera: { zoom: [1.03, 1.08] } }],
  ["s06", 7.333, 8.672, "yakin:jake", { kamera: { zoom: [1.04, 1.1] } }],
  ["s07", 8.672, 10.344, "tahta", { kamera: { zoom: [1.12, 1.22] } }],
  ["s08", 10.344, 12.315, "yakin:jake", { kamera: { zoom: [1.02, 1.06] }, vurus: [{ t: 11.92, olcek: 1.1, sure: 0.12 }], proplar: [{ tur: "yazi", metin: "YOU DECIDE", bas: 11.92, bitis: 12.715, y: 860 }] }],
  ["s09", 12.315, 12.715, "portre:jake:gulen", { kamera: { zoom: [1.0, 1.02] }, proplar: [{ tur: "yazi", metin: "YOU DECIDE", bas: 11.92, bitis: 12.715, y: 860 }] }],
  // S3 — telefon alttan (17,303), 3 ilan
  ["s10", 12.715, 15.69, "genis", {
    kamera: { zoom: [1.04, 1.09] },
    proplar: [banknot(0), { tur: "telefon", bas: 12.765, bitis: 15.69, ogeler: [{ ikon: "bisiklet", fiyat: "$60" }, { ikon: "sifonyer", fiyat: "FREE" }, { ikon: "kutu", fiyat: "$40" }] }],
  }],
  ["s11", 15.69, 17.869, "yakin:jake", { kamera: { zoom: [1.03, 1.07] } }],
  ["s12", 17.869, 18.967, "yakin:mike", { kamera: { zoom: [1.06, 1.1] } }],
  ["s13", 18.967, 19.447, "portre:mike:gulen", { kamera: { zoom: [1.0, 1.02] } }], // sırıtma (sessiz)
  // S4 — ilan ROAD BIKE alçak kart (whoosh apex 24,6; yüz açık), "Flat tires" punch, "look at that frame!" sıçrama kesmesi + bisiklet pop
  ["s14", 19.447, 23.903, "yakin:mike", { kamera: { zoom: [1.02, 1.06] }, vurus: [{ t: 20.9, olcek: 1.06, sure: 0.1 }], proplar: [{ tur: "ilan", yer: "alt", bas: 19.447, bitis: 22.214, ikon: "bisiklet", baslik: "ROAD BIKE", fiyat: "$60", not: "flat tires" }] }],
  ["s14b", 23.903, 25.738, "yakin:mike", { kamera: { zoom: [1.16, 1.22] }, proplar: [{ tur: "ikon", ad: "bisiklet", bas: 24.915, bitis: 25.738, x: 220, y: 880, boyut: 190 }] }],
  ["s15", 25.738, 28.037, "yakin:jake", { kamera: { zoom: [1.02, 1.05] }, vurus: [{ t: 27.38, olcek: 1.08, sure: 0.1 }], proplar: [{ tur: "tahtaKose", bas: 26.022, bitis: 28.037, yaz: 26.54, metin: "$100 − $60 = $40", x: 80, y: 870 }] }],
  ["s16", 28.037, 29.365, "genis", { kamera: { zoom: [1.03, 1.06] }, proplar: [banknot(0)] }],
  // "Tires aren't." sert punch-in (33,95), satır sonrası sessiz tutuş; plak cızırtısının ardından Mike'ın yüzü düşer (görsel gag)
  ["s17", 29.365, 30.535, "yakin:jake", { kamera: { zoom: [1.02, 1.03] }, vurus: [{ t: 29.395, olcek: 1.24, sure: 0.08 }] }],
  ["s18", 30.535, 30.935, "portre:mike:endiseli", { kamera: { zoom: [1.0, 1.03] } }],
  // S5 — ilan DRESSER alçak kart (37,5), "We paint it, flip it" sıçrama kesmesi + boya pop; "Free?" = konuşan tabana punch-in (Z3)
  ["s19", 30.935, 33.401, "yakin:jake", { kamera: { zoom: [1.02, 1.07] }, proplar: [{ tur: "ilan", yer: "alt", bas: 32.355, bitis: 33.401, ikon: "sifonyer", baslik: "DRESSER", fiyat: "FREE", not: "must go today" }] }],
  ["s19b", 33.401, 35.055, "yakin:jake", { kamera: { zoom: [1.16, 1.2] }, proplar: [{ tur: "ikon", ad: "boya", bas: 33.98, bitis: 35.055, x: 220, y: 880, boyut: 180 }] }],
  ["s20", 35.055, 36.934, "yakin:mike", { kamera: { zoom: [1.04, 1.06] }, vurus: [{ t: 35.125, olcek: 1.2, sure: 0.08 }], sarsinti: [{ t: 35.125, sure: 0.1, guc: 8 }] }],
  ["s22", 36.934, 39.485, "yakin:jake", { kamera: { zoom: [1.02, 1.05] }, vurus: [{ t: 38.84, olcek: 1.12, sure: 0.1 }], proplar: [{ tur: "ikon", ad: "araba", bas: 38.84, bitis: 39.485, x: 220, y: 880, boyut: 180 }] }],
  ["s23", 39.485, 40.355, "portre:jake:endiseli", {
    kamera: { zoom: [1.0, 1.03] },
    proplar: [{ tur: "ikonSira", bas: 39.485, bitis: 40.355, y: 400, ayrac: "↔", boyut: 200, ogeler: [{ ad: "araba", t: 39.584 }, { ad: "sifonyer", t: 39.934 }] }],
  }],
  ["s24", 40.355, 44.393, "yakin:mike", {
    kamera: { zoom: [1.03, 1.07] },
    proplar: [{ tur: "ikonSira", bas: 40.355, bitis: 44.393, y: 880, boyut: 170, ogeler: [{ ad: "kamyon", t: 40.98 }, { ad: "boya", t: 41.52 }, { ad: "saat", t: 42.02 }] }],
  }],
  ["s25", 44.393, 46.371, "yakin:jake", { kamera: { zoom: [1.03, 1.11] } }], // "Slow. But safe." hafif push-in
  // S6 — Mike kadraja eğilir; ilan GARAGE SALE BOX alçak kart (53,51), kapak titrer (54,7); "Forty bucks" punch; kartuş / çizik diskler
  ["s26", 46.371, 52.037, "yakin:mike", {
    kamera: { zoom: [1.0, 1.14] }, vurus: [{ t: 49.44, olcek: 1.06, sure: 0.1 }],
    proplar: [{ tur: "ilan", yer: "alt", bas: 46.371, bitis: 49.44, ikon: "kutu", baslik: "GARAGE SALE BOX", fiyat: "$40", not: "old games", titre: 48.28 }],
  }],
  ["s27", 52.037, 55.273, "yakin:jake", {
    kamera: { zoom: [1.02, 1.05] }, vurus: [{ t: 54.22, olcek: 1.08, sure: 0.1 }],
    proplar: [{ tur: "ikonSira", bas: 52.037, bitis: 55.273, y: 860, ayrac: "/", boyut: 200, ogeler: [{ ad: "kartus", t: 52.5 }, { ad: "disk", t: 54.471 }] }],
  }],
  // S7 — 1,0 sn sessiz bakışma, banknot ortada, yavaş push-in (gerilim 62,019)
  ["s28", 55.273, 56.353, "genis", { kamera: { zoom: [1.04, 1.1] }, odak: { x: 540, y: 1100 }, proplar: [banknot(0)] }],
  ["s29", 56.353, 58.649, "yakin:mike", { kamera: { zoom: [1.04, 1.12] } }],
  ["s30", 58.649, 62.828, "yakin:jake", { kamera: { zoom: [1.01, 1.05] }, proplar: [banknot(0)] }],
  ["s31", 62.828, 63.269, "portre:jake:dusunceli", { kamera: { zoom: [1.0, 1.02] } }], // iç çekiş (sessiz)
  ["s32", 63.269, 65.546, "yakin:jake", { kamera: { zoom: [1.03, 1.07] }, proplar: [banknot(0)] }],
  // S8 — Mike soruyu sorar (geniş, kamera ortaya); karar kartı "box?"tan sonraki boşlukta (67,33) girer (whoosh kelimeye binmez, Ö1);
  // 69,14 ikisi kameraya: "Ep. 2: YOUR call" + ding; karar kartı 72,33'te çıkar, takip kartı 72,35–74,55 (çakışmasız, kısa kuyruk)
  ["s33", 65.546, 69.136, "genis", { kamera: { zoom: [1.02, 1.08] }, proplar: [banknot(0)] }],
  ["s34", 69.136, 74.55, "ikiPortre", { kamera: { zoom: [1.0, 1.04] } }],
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
          { metin: "$100", x: 600, y: 300, boyut: 120, t: 5.221, sure: 0.5 },
          { metin: "GOAL:", x: 604, y: 470, boyut: 56, t: 8.672, sure: 0.01, renk: "#b3261e" },
          { metin: "$1,000,000", x: 575, y: 540, boyut: 62, t: 8.73, sure: 0.3, renk: "#b3261e", tik: [9.247, 9.407, 9.522, 9.637, 9.752, 9.866] },
        ],
      }]
    : [];
  return { id, bas, bitis, arka: MUTFAK_L1.genis, cekim, ...ek, proplar: [...tahta, ...(ek?.proplar ?? [])] };
});

export const B001: Bolum = {
  id: "FBV-B001",
  no: 1,
  sure: 74.55,
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
    bas: 67.333,
    sure: 5,
    kapanis: 69.136,
  },
  abone: { bas: 72.35, ust: 1010, sure: 2.2, klik: 0.9 },
  logo: "seri/ortak/flipbyvote-profil.png", // kanal profil resmi (takip kartı + açılış çipi)
  damga: { ust: 262, olcek: 0.55, sag: true }, // "EP. 1" çipi sağ üst köşe (BANK sol üstte), kancayı örtmez
};
