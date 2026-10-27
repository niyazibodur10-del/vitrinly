import React from "react";
import { Img, interpolate, staticFile, useCurrentFrame, useVideoConfig } from "remotion";
import { AGIZ_YAMA, Cue, Kutu, SUNUCU, YAMA } from "./veri";

// Konuşan Leo rig'i (cut-out): bel üstü poz (a / C12; aynı kadraj) + Rhubarb ağız yamaları + göz kırpma + tek göz kırpma.
// Yamalar 05-gorsel/rig/rig-yamalar.json konumlarında (SUNUCU kırpım kutusuna göre). Eşleme: A,X = taban · B,G = C07 ·
// C,H = C08 · D = b (yalnız a pozunda piksel hizalı; C12'de C08) · E = C09 · F = C10.
// Kafa yüz merkezi (kırpım koordinatı) — kamera/punch-in odakları için dışarı verilir.
export type Rig = { klasor: string; kutu: Kutu; yama: Record<string, Kutu> };
export const RIG_KRITIK: Rig = { klasor: "k1929", kutu: SUNUCU, yama: YAMA };
export const yuzRig = (r: Rig) => ({ x: 940 - r.kutu.x, y: 330 - r.kutu.y });
export const YUZ = yuzRig(RIG_KRITIK);

// Rig uyumlu pozlar (kafa a ile hizalı → ağız yamaları çalışır); diğerleri ifade pozu (ağız/göz sabit)
export type SunucuPoz = "a" | "C12" | "C13" | "C14" | "C21" | "balt" | "c" | "d" | "e" | "f" | "C20";
const AGIZ_UYUMLU = new Set(["a", "C12", "C13", "C14", "C21", "balt"]);
const GOZ_UYUMLU = new Set(["a", "C12", "C13", "C14", "C21"]);

const sekilBul = (cues: Cue[], t: number): string => {
  for (const c of cues) if (t >= c.start && t < c.end) return c.value;
  return "X";
};

// Göz kırpma: 2.6–4.4 sn aralıklarla (tohumlu sözde rastgele), 3 kare kapalı
const kirpiyor = (t: number, tohum: number): boolean => {
  let bas = 0.8 + (tohum % 7) * 0.13;
  let i = 0;
  while (bas < t + 1) {
    if (t >= bas && t < bas + 0.1) return true;
    i++;
    bas += 2.6 + (((tohum * 31 + i * 17) % 19) / 19) * 1.8;
  }
  return false;
};

const Yama: React.FC<{ ad: string; rig: Rig }> = ({ ad, rig }) => {
  const y = rig.yama[ad];
  return <Img src={staticFile(`${rig.klasor}/${ad}.png`)} style={{ position: "absolute", left: y.x, top: y.y, width: y.w, height: y.h }} />;
};

export const Sunucu: React.FC<{
  cues: Cue[];
  ofs: number; // Sequence yerel zamanı → parça (Rhubarb) zamanı farkı (sn)
  poz?: SunucuPoz;
  tohum?: number;
  wink?: [number, number]; // parça zamanında tek göz kırpma aralığı
  giris?: boolean; // poz değişiminde 5 karelik oturma (pose-to-pose pop)
  zorlaSekil?: string; // AgizTest için
  style?: React.CSSProperties;
  rig?: Rig;
  konusmaz?: boolean; // dış ses sırasında ağız kapalı
}> = ({ cues, ofs, poz = "a", tohum = 1, wink, giris = false, zorlaSekil, style, rig = RIG_KRITIK, konusmaz = false }) => {
  const SUNUCU = rig.kutu;
  const YUZ = yuzRig(rig);
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps + ofs;
  const sekil = zorlaSekil ?? (konusmaz || !AGIZ_UYUMLU.has(poz) ? "X" : sekilBul(cues, t));
  const konusuyor = sekil !== "X" && sekil !== "A";
  const winkVar = wink && t >= wink[0] && t < wink[1];
  const winkYakin = wink && t > wink[0] - 0.7 && t < wink[1] + 0.4; // tek göz kırpma çevresinde normal kırpma yok
  const kirp = !winkYakin && !zorlaSekil && GOZ_UYUMLU.has(poz) && kirpiyor(t, tohum);
  // Nefes (3.4 sn) + hafif gövde salınımı; konuşurken küçük baş-gövde vurgusu
  const nefes = Math.sin((t / 3.4) * Math.PI * 2) * 0.005;
  const salinim = Math.sin((t / 4.3) * Math.PI * 2) * 0.35 + (konusuyor ? Math.sin(t * Math.PI * 2 * 1.6) * 0.25 : 0);
  const otur = giris ? interpolate(frame, [0, 2, 5], [0.965, 1.012, 1], { extrapolateRight: "clamp" }) : 1;
  const tabanD = sekil === "D" && poz === "a";
  const yamaAd = sekil === "D" && poz !== "a" ? "agiz-C-C08" : AGIZ_YAMA[sekil];
  return (
    <div
      style={{
        position: "absolute",
        width: SUNUCU.w,
        height: SUNUCU.h,
        transformOrigin: `${YUZ.x}px ${SUNUCU.h}px`,
        rotate: `${salinim}deg`,
        scale: String((1 + nefes) * otur),
        ...style,
      }}
    >
      <Img src={staticFile(`${rig.klasor}/leo-${tabanD ? "b" : poz}.png`)} style={{ position: "absolute", left: 0, top: 0, width: SUNUCU.w, height: SUNUCU.h }} />
      {!tabanD && yamaAd ? <Yama ad={yamaAd} rig={rig} /> : null}
      {kirp ? <Yama ad="goz-kapali-C06" rig={rig} /> : null}
      {winkVar ? <Yama ad="goz-tek-C06" rig={rig} /> : null}
    </div>
  );
};
