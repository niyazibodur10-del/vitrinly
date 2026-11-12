// L3 THE DRIVEWAY mekân seti (animasyon-yonetmeni 2026-11-12). Karakter rig'i L1 ile aynı (bölüm 1 varlıkları);
// yerleşim video/public/seri/bolum-002/yerlesim.json: yakın = plaka 1,3× (540,600) σ4, taban ölçek 1 (0,0), ön katman yok;
// portre = plaka 1,6× (540,700) σ6. İkili çekim yok (L3'te karakterler tekli/portre; geniş = "bos" + nesne).
import type { MekanSeti } from "../tipler";
import { MUTFAK_L1 } from "./mekan-l1";

export const GARAJ_YOLU_L3: MekanSeti = {
  ...MUTFAK_L1,
  genis: "seri/bolum-002/plaka/L3-A.png",
  on: undefined,
  tekli: { jake: { plakaOlcek: 1.3, capa: [540, 600] }, mike: { plakaOlcek: 1.3, capa: [540, 600] } },
  tekliBulanik: 4,
  portreArka: { olcek: 1.6, capa: [540, 700], bulanik: 6 },
};
