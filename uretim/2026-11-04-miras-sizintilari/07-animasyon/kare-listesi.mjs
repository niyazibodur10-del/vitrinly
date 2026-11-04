// Kare denetimi listesi: her kesmenin başı + 0,9 sn (≤1 sn giriş kapısı) ve +3 sn (global kare, KMirasTam). Kullanım: node <bu> [ofset_sn ...]
import { build } from "../../../video/node_modules/esbuild/lib/main.js";
import fs from "node:fs"; import path from "node:path"; import { fileURLToPath } from "node:url";
const A = path.dirname(fileURLToPath(import.meta.url)); const KOK = path.resolve(A, "../../..");
const out = path.join(A, ".zaman-paket2.mjs");
await build({ entryPoints: [path.join(KOK, "video/src/videolar/miras-sizintilari/zaman.ts")], bundle: true, format: "esm", platform: "node", outfile: out, logLevel: "error" });
const { ZAMAN, SAHNELER } = await import(out); fs.unlinkSync(out);
const ofs = process.argv.slice(2).map(Number); const kareler = [];
for (const s of SAHNELER) { const p = ZAMAN[s.id](); p.kes.forEach((c, i) => { const son = i + 1 < p.kes.length ? p.kes[i + 1][0] : s.sure; for (const o of ofs) if (c[0] + o < son) kareler.push(Math.round((s.bas + c[0] + o) * 30)); }); }
console.log(kareler.join(","));
