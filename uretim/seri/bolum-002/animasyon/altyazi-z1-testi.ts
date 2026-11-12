import { satirDosyasi, ekranKelimeleri, obekler } from "../../../../video/src/seri/zaman";
import sj from "../../../../video/src/seri/bolumler/bolum-002.satirlar.json";
import kj from "../../../../video/src/seri/bolumler/bolum-002.kelimeler.json";
const d = satirDosyasi(sj as any, kj as any);
let ok = 0; const sat: string[] = [];
for (const s of d.satirlar) {
  const ek = ekranKelimeleri(s).map((w) => w.k).join(" ");
  const ob = obekler(s).flat().map((w) => w.k).join(" ");
  const ayni = ek === s.metin.split(/\s+/).join(" ") && ob === ek;
  const sirali = ekranKelimeleri(s).every((w, i, a) => w.bitis >= w.bas && (i === 0 || w.bas >= a[i - 1].bas - 1e-6) && w.bas >= s.bas - 1e-6 && w.bitis <= s.bitis + 1e-6);
  if (ayni && sirali) ok++; else sat.push(`KALDI: ${s.metin} | ${ek}`);
}
for (const s of d.satirlar.filter((x) => /solid wood|rent a truck/.test(x.metin))) console.log(ekranKelimeleri(s).map((w) => `${w.k}@${w.bas.toFixed(2)}`).join(" "));
console.log(`Z1: ${ok}/${d.satirlar.length} satır ekran = metin (sıra+aralık dahil)`); sat.forEach((x) => console.log(x));
