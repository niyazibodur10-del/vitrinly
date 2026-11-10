// ŞABLON DEMOSU (test/kanıt): yer tutucu görseller + Kokoro demo diyaloğu. Yayın kapısı bunu REDDEDER (yer tutucu, süre).
// Ses (ses-yonetmeni aracı, Jake am_onyx 0.95 / Mike am_fenrir 1.05):
//   kokoro-venv/bin/python tools/ses/diyalog.py uretim/seri/sablon-demo/demo-diyalog.txt video/public/seri/demo/diyalog.wav
//   → diyalog.zaman.json buraya demo.satirlar.json olarak kopyalanır (biçim olduğu gibi; satirDosyasi() çevirir)
// Ağız: python3 -I tools/seri/agiz-cue.py video/public/seri/demo/diyalog.wav video/src/seri/bolumler/demo.satirlar.json video/src/seri/bolumler/demo.agiz.json
// Üç ağız yolu tek bölümde sınanır: S1 yama, S2 ifade, S3 kamera.
import type { AgizDosyasi, Bolum, KarakterSahne, ZamanJson } from "../tipler";
import { satirDosyasi } from "../zaman";
import satirlarJson from "./demo.satirlar.json";
import agizJson from "./demo.agiz.json";

const satirlar = satirDosyasi(satirlarJson as ZamanJson);
const agiz = agizJson as AgizDosyasi;

const ARKA = { yerTutucu: "blok", renk: "#3a4658", renk2: "#262c37" } as const;
const ARKA2 = { yerTutucu: "blok", renk: "#4a3f52", renk2: "#2c2633" } as const;
const JAKE_N = { yerTutucu: "figur", renk: "#7f8fa3", renk2: "#5f6d80" } as const;
const JAKE_K = { yerTutucu: "figur", renk: "#a9bdd6", renk2: "#7f93ad" } as const;
const MIKE_N = { yerTutucu: "figur", renk: "#a38f7f", renk2: "#806d5f" } as const;
const MIKE_K = { yerTutucu: "figur", renk: "#d6bda9", renk2: "#ad937f" } as const;
const AGIZ = { yerTutucu: "agiz", renk: "#1b1f27" } as const;

// figür kutusu 380x860; baş merkezi kutunun (190, 134) noktası, ağız (190, 190)
const jake = (ek: Partial<KarakterSahne> = {}): KarakterSahne => ({
  kim: "jake", gorsel: JAKE_N, x: 110, y: 700, w: 380, h: 860, odak: { x: 300, y: 840 }, ...ek,
});
const mike = (ek: Partial<KarakterSahne> = {}): KarakterSahne => ({
  kim: "mike", gorsel: MIKE_N, x: 590, y: 700, w: 380, h: 860, odak: { x: 780, y: 840 }, ...ek,
});

export const DEMO: Bolum = {
  id: "FBV-Demo",
  no: 2,
  sure: 20,
  satirlar,
  agiz,
  agizYolu: "yama",
  sahneler: [
    {
      id: "s1-yama", bas: 0, bitis: 4.65, arka: ARKA, agizYolu: "yama",
      karakterler: [
        jake({ agiz: { x: 255, y: 868, w: 90, h: 52, sekiller: AGIZ } }),
        mike({ agiz: { x: 735, y: 868, w: 90, h: 52, sekiller: AGIZ } }),
      ],
    },
    {
      id: "s2-ifade", bas: 4.65, bitis: 9.35, arka: ARKA2, agizYolu: "ifade", kamera: { zoom: [1.04, 1.1] },
      karakterler: [
        jake({ ifadeler: { notr: JAKE_N, konusur: JAKE_K } }),
        mike({ ifadeler: { notr: MIKE_N, konusur: MIKE_K } }),
      ],
    },
    {
      id: "s3-kamera", bas: 9.35, bitis: 20, arka: ARKA, agizYolu: "kamera", kamera: { zoom: [1, 1.04] },
      karakterler: [jake(), mike()],
    },
  ],
  bank: { baslangic: 100, olaylar: [{ t: 8.7, deger: 85 }] },
  ses: { diyalog: "seri/demo/diyalog.wav" },
  kazananYorum: { kullanici: "@sarah_flips", metin: "Buy the cheapest thing at a garage sale and flip it!", begeni: 1243, sure: 3.5 },
  karar: {
    soru: "What should they do with the camera?",
    secenekler: ["Sell it online tonight", "Fix it and flip it for more", "Trade it for something bigger"],
    sure: 6,
  },
};

// Render süresi ölçümü için 90 sn varyant: 17 sn'lik blok 5 kez döner (yalnız ölçüm; içerik anlamsız).
// Ses: public/seri/demo/diyalog90.wav = diyalog.wav 17 sn'ye doldurulup 5 kez (README "Demo").
export const DEMO90: Bolum = {
  ...DEMO,
  id: "FBV-Demo90",
  sure: 90,
  satirlar: {
    satirlar: Array.from({ length: 5 }, (_, i) =>
      satirlar.satirlar.map((s) => ({
        ...s, bas: s.bas + i * 17, bitis: s.bitis + i * 17,
        kelimeler: s.kelimeler?.map((w) => ({ ...w, bas: w.bas + i * 17, bitis: w.bitis + i * 17 })),
      })),
    ).flat(),
  },
  agiz: {
    jake: Array.from({ length: 5 }, (_, i) => (agiz.jake ?? []).map((c) => ({ ...c, bas: c.bas + i * 17, bitis: c.bitis + i * 17 }))).flat(),
    mike: Array.from({ length: 5 }, (_, i) => (agiz.mike ?? []).map((c) => ({ ...c, bas: c.bas + i * 17, bitis: c.bitis + i * 17 }))).flat(),
  },
  sahneler: Array.from({ length: 5 }, (_, i) =>
    DEMO.sahneler.map((s, j) => ({
      ...s, id: `${s.id}-${i}`, bas: i * 17 + s.bas, bitis: j === 2 ? (i === 4 ? 90 : (i + 1) * 17) : i * 17 + s.bitis,
    })),
  ).flat(),
  bank: { baslangic: 100, olaylar: Array.from({ length: 5 }, (_, i) => ({ t: 8.7 + i * 17, deger: 100 - 15 * (i + 1) + 40 * i })) },
  ses: { diyalog: "seri/demo/diyalog90.wav" },
  karar: { ...DEMO.karar, sure: 7 },
};
