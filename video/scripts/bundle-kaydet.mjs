// animasyon-yonetmeni 2026-11-11: tek bundle'ı diske yaz (kare-ornek.mjs BUNDLE=<dizin> ile yeniden kullanılır). Kullanım: node scripts/bundle-kaydet.mjs <dizin>
import { bundle } from "@remotion/bundler"; import path from "node:path";
const out = await bundle({ entryPoint: path.resolve("src/index.ts"), outDir: process.argv[2] });
console.log(out);
