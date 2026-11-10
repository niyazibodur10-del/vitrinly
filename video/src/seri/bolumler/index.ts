import type { Bolum } from "../tipler";
import { DEMO, DEMO90 } from "./demo";

// Bölüm kaydı: yeni bölüm = bolum-XXX.ts + buraya bir satır (README.md "Yeni bölüm").
// Kompozisyon kimliği Bolum.id (ör. "FBV-B001"); Root.tsx bu listeyi otomatik kaydeder.
export const BOLUMLER: Bolum[] = [
  DEMO,
  DEMO90,
  // yeni bölümler: import { B001 } from "./bolum-001"; → B001,
];

export const bolumBul = (id: string) => BOLUMLER.find((b) => b.id === id);
