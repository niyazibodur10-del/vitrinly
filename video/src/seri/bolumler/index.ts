import type { Bolum } from "../tipler";
import { B001 } from "./bolum-001";
import { B002 } from "./bolum-002";
import { DEMO, DEMO90 } from "./demo";

// Bölüm kaydı: yeni bölüm = bolum-XXX.ts + buraya bir satır (README.md "Yeni bölüm").
// Kompozisyon kimliği Bolum.id (ör. "FBV-B001"); Root.tsx bu listeyi otomatik kaydeder.
export const BOLUMLER: Bolum[] = [
  DEMO,
  DEMO90,
  B001,
  B002,
  // yeni bölümler: import { B00N } from "./bolum-00N"; → B00N,
];

export const bolumBul = (id: string) => BOLUMLER.find((b) => b.id === id);
