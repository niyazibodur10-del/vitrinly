// L1 THE KITCHEN mekân seti + Jake/Mike rig'i (animasyon-yonetmeni 2026-11-11). Her bölüm yeniden kullanır (incil §2).
// Kaynak: video/public/seri/bolum-001/yerlesim.json + VARLIKLAR.md (gorsel-varlik-sanatcisi) ve goz-kapak.json
// (göz elipsleri: uretim/seri/bolum-001/animasyon/goz-kapak-olc.py). Değerler oradan kopyalandı; değişirse burası güncellenir.
// Mike portreleri (şaşkın, gülen, endişeli, heyecanlı): saç halesi koddan temizlenmiş *-temiz.png (animasyon/sac-hale-temizle.py, hakem Z3).
// Mike tabanının ten rengi yanaktan elle düzeltildi (#f8b89c, #e49a80): göz altı örneği kapakta turuncu kalıyordu.
import type { GozElips, MekanSeti } from "../tipler";

const P = "seri/bolum-001/";
const GOZ: Record<string, GozElips[]> = {"jake-taban": [{"cx": 485, "cy": 450, "rx": 47, "ry": 27, "aci": 0, "ten": "#eca57b"}, {"cx": 654.5, "cy": 437.5, "rx": 39, "ry": 25, "aci": -5, "ten": "#f5ad82"}], "mike-taban": [{"cx": 550, "cy": 412.5, "rx": 40, "ry": 22, "aci": 5, "ten": "#f8b89c"}, {"cx": 698.5, "cy": 404, "rx": 32, "ry": 20, "aci": -5, "ten": "#e49a80"}], "jake-dusunceli": [{"cx": 423, "cy": 596, "rx": 64, "ry": 38, "aci": 10, "ten": "#df9871"}, {"cx": 686, "cy": 565, "rx": 60, "ry": 42, "aci": 10, "ten": "#ecaa84"}], "mike-heyecanli": [{"cx": 424, "cy": 571.2, "rx": 55, "ry": 37, "aci": 3, "ten": "#ffbd95"}, {"cx": 662.9, "cy": 571.9, "rx": 55, "ry": 36, "aci": -5, "ten": "#f8a47f"}]};

export const MUTFAK_L1: MekanSeti = {
  genis: P + "plaka/L1-A.png",
  on: P + "plaka/L1-A-tezgah-on.png",
  tahta: P + "plaka/L1-B.png",
  tahtaAlan: { x: 560, y: 250, w: 475, h: 505 },
  ikili: { mike: { olcek: 0.55, xy: [0, 141] }, jake: { olcek: 0.58, xy: [454, 141] } },
  onde: "jake",
  tekli: { jake: { plakaOlcek: 1.25, capa: [760, 1186] }, mike: { plakaOlcek: 1.25, capa: [320, 1186] } },
  portreArka: { olcek: 1.6, capa: [540, 900], bulanik: 6 },
  karakterler: {
    jake: {
      taban: P + "karakter/jake-taban.png", w: 1080, h: 1920,
      agiz: { x: 479, y: 594, w: 208, h: 186, kapali: P + "agiz/jake-agiz-kapali.png", yari: P + "agiz/jake-agiz-yari.png", acik: P + "agiz/jake-agiz-acik.png" },
      gozler: GOZ["jake-taban"],
      yuz: { x: 570, y: 560 },
      portreler: {
      notr: { dosya: "seri/bolum-001/ifade/jake-notr.png", w: 1080, h: 1564, xy: [-162, 372], olcek: 1.3 },
      gulen: { dosya: "seri/bolum-001/ifade/jake-gulen.png", w: 1080, h: 1564, xy: [-162, 367], olcek: 1.3 },
      saskin: { dosya: "seri/bolum-001/ifade/jake-saskin.png", w: 1080, h: 1564, xy: [-162, 370], olcek: 1.3 },
      endiseli: { dosya: "seri/bolum-001/ifade/jake-endiseli.png", w: 1080, h: 1564, xy: [-162, 381], olcek: 1.3 },
      heyecanli: { dosya: "seri/bolum-001/ifade/jake-heyecanli.png", w: 1080, h: 1564, xy: [-162, 383], olcek: 1.3 },
      dusunceli: { dosya: "seri/bolum-001/ifade/jake-dusunceli.png", w: 1080, h: 1564, xy: [-162, 435], olcek: 1.3, gozler: GOZ["jake-dusunceli"] },
      },
    },
    mike: {
      taban: P + "karakter/mike-taban.png", w: 1080, h: 1920,
      agiz: { x: 555, y: 496, w: 204, h: 208, kapali: P + "agiz/mike-agiz-kapali.png", yari: P + "agiz/mike-agiz-yari.png", acik: P + "agiz/mike-agiz-acik.png" },
      gozler: GOZ["mike-taban"],
      yuz: { x: 610, y: 500 },
      portreler: {
      notr: { dosya: "seri/bolum-001/ifade/mike-notr.png", w: 1080, h: 1602, xy: [-162, 423], olcek: 1.3 },
      gulen: { dosya: "seri/bolum-001/ifade/mike-gulen-temiz.png", w: 1080, h: 1602, xy: [-162, 407], olcek: 1.3 },
      saskin: { dosya: "seri/bolum-001/ifade/mike-saskin-temiz.png", w: 1080, h: 1602, xy: [-162, 419], olcek: 1.3 },
      endiseli: { dosya: "seri/bolum-001/ifade/mike-endiseli-temiz.png", w: 1080, h: 1602, xy: [-162, 429], olcek: 1.3 },
      heyecanli: { dosya: "seri/bolum-001/ifade/mike-heyecanli-temiz.png", w: 1080, h: 1602, xy: [-162, 419], olcek: 1.3, gozler: GOZ["mike-heyecanli"] },
      dusunceli: { dosya: "seri/bolum-001/ifade/mike-dusunceli.png", w: 1080, h: 1602, xy: [-162, 537], olcek: 1.3 },
      },
    },
  },
};
