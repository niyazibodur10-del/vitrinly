// animasyon-yonetmeni 2026-11-11: tek bundle'ı diske yaz (kare-ornek.mjs BUNDLE=<dizin> ile yeniden kullanılır). Kullanım: [PUBLIC_DIR=<yalnız gereken varlıkların symlink dizini>] node scripts/bundle-kaydet.mjs <dizin> (disk darken bundle ~600 MB → ~170 MB)
import { bundle } from "@remotion/bundler"; import path from "node:path";
const out = await bundle({ entryPoint: path.resolve("src/index.ts"), outDir: process.argv[2], ...(process.env.PUBLIC_DIR ? { publicDir: process.env.PUBLIC_DIR } : {}) });
console.log(out);
