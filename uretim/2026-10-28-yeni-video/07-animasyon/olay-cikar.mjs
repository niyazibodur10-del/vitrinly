// Tek kaynak → (1) 06-muzik/animasyon-efekt-cue.json (+07-animasyon/efekt-cue.json), (2) 07-animasyon/agiz-gorunur.json
// zaman.ts'i esbuild ile paketler, tüm sahne planlarını çalıştırır (eksik kelime çapası burada patlar).
// Kullanım (repo kökü): node uretim/2026-10-28-yeni-video/07-animasyon/olay-cikar.mjs
import { build } from "../../../video/node_modules/esbuild/lib/main.js";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";
const A = path.dirname(fileURLToPath(import.meta.url));
const U = path.resolve(A, "..");
const KOK = path.resolve(U, "../..");
const out = path.join(A, ".zaman-paket.mjs");
await build({ entryPoints: [path.join(KOK, "video/src/videolar/yeni-video/zaman.ts")], bundle: true, format: "esm", platform: "node", outfile: out, logLevel: "error" });
const { ZAMAN, ABONE_SAHNE } = await import(out + "?" + Date.now());
const { SAHNELER } = await import(out + "?v");
fs.unlinkSync(out);
const veri = fs.readFileSync(path.join(KOK, "video/src/videolar/yeni-video/veri-sahne.ts"), "utf8");
const sahneler = JSON.parse(veri.match(/export const SAHNELER: SahneVeri\[\] = (.*);\n/)[1]);
const tahmini = veri.startsWith("// TAHMİNİ");
const olaylar = [], agiz = [], hata = [];
for (const s of sahneler) {
  const f = ZAMAN[s.id];
  if (!f) { hata.push(`${s.id}: plan yok`); continue; }
  let p;
  try { p = f(); } catch (e) { hata.push(String(e.message)); continue; }
  for (const o of p.olay) {
    const g = +(s.bas + o.t).toFixed(3);
    olaylar.push({ sahne: s.id, t: g, kare: Math.round(g * 30), olay: o.olay, tur: o.tur, oneri: o.oneri ?? "" });
  }
  for (const [a, b] of p.agiz) agiz.push({ sahne: s.id, bas: +(s.bas + a).toFixed(2), bitis: +(s.bas + Math.min(b, s.sure)).toFixed(2) });
}
if (hata.length) { console.error("HATA:\n" + hata.join("\n")); process.exit(1); }
olaylar.sort((a, b) => a.t - b.t);
const cue = { kaynak: "video/src/videolar/yeni-video/zaman.ts (tek kaynak; 07-animasyon/olay-cikar.mjs)", eksen: "04-ses/anlatim.wav (0 = anlatım başı)", fps: 30, tahmini, olaylar };
fs.writeFileSync(path.join(A, "efekt-cue.json"), JSON.stringify(cue, null, 1));
fs.writeFileSync(path.join(U, "06-muzik/animasyon-efekt-cue.json"), JSON.stringify(cue, null, 1));
fs.writeFileSync(path.join(A, "agiz-gorunur.json"), JSON.stringify(agiz, null, 1));
const say = {}; for (const o of olaylar) say[o.tur] = (say[o.tur] ?? 0) + 1;
console.log(JSON.stringify({ olay: olaylar.length, tur: say, abone: olaylar.filter((o) => o.tur === "abone").map((o) => `${o.sahne}@${o.t}s/k${o.kare}`), agiz_aralik: agiz.length, agiz_sn: +agiz.reduce((a, x) => a + x.bitis - x.bas, 0).toFixed(1), tahmini }));
console.log("ARALIKLAR " + agiz.map((x) => `${x.bas}-${x.bitis}`).join(","));
