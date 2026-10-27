// animasyon-yonetmeni 2026-10-27. Kullanım: cd video && [BUNDLE=<bundle_dizini>] node scripts/kare-ornek.mjs <CompId> <cikis_dizini> <kare1,kare2,...> [olcek]
// Kare örnekleri: tek bundle + tek tarayıcı ile çok sayıda still (CLI'de her still ~6 sn tarayıcı açılışı).
// Kullanım (video/ içinden): node <bu> <CompId> <cikis_dizini> <kare1,kare2,...> [olcek=0.5]

import { renderStill, selectComposition, openBrowser } from "@remotion/renderer";
import path from "node:path";
import fs from "node:fs";
const [id, out, kareler, olcek = "0.5"] = process.argv.slice(2);
fs.mkdirSync(out, { recursive: true });
const b = fs.readdirSync("/opt/pw-browsers").find((d) => d.startsWith("chromium_headless_shell"));
const browserExecutable = `/opt/pw-browsers/${b}/chrome-headless-shell-linux64/chrome-headless-shell`;
const serveUrl = process.env.BUNDLE || (await (await import("@remotion/bundler")).bundle({ entryPoint: path.resolve("src/index.ts") }));
const browser = await openBrowser("chrome", { browserExecutable });
const composition = await selectComposition({ serveUrl, id, puppeteerInstance: browser });
for (const k of kareler.split(",").map(Number)) {
  const o = path.join(out, `${id}-${String(k).padStart(5, "0")}.jpg`);
  try {
    await renderStill({ composition, serveUrl, output: o, frame: k, imageFormat: "jpeg", jpegQuality: 80, scale: Number(olcek), puppeteerInstance: browser });
    console.log("ok", k);
  } catch (e) {
    console.log("HATA", k, String(e.message).split("\n")[0]);
  }
}
await browser.close({ silent: true });
