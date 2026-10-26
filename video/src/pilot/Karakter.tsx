import React from "react";
import { Img, staticFile, useCurrentFrame, useVideoConfig } from "remotion";
import { Cue, mouthCues } from "./data";

// portre.png: 1196x1110 (kaynak 2D sayfa x4, arka planı temizlenmiş).
// Ağız ve göz konumları bu görselin piksel koordinatlarıdır.
export const PORTRE = { w: 1196, h: 1110 };
const AGIZ = { x: 612, y: 786, aci: 15 };
const GOZLER = [
  { x: 545, y: 539, w: 128, h: 58, aci: 10 },
  { x: 771, y: 580, w: 108, h: 52, aci: 14 },
];

const RENK = {
  ic: "#561f17",
  dil: "#c9574b",
  dis: "#fff7ef",
  dudak: "#e48f62",
  cizgi: "#2b130b",
  ten: "#f6a46d",
};

const sekilBul = (cues: Cue[], t: number): string => {
  for (const c of cues) {
    if (t >= c.start && t < c.end) return c.value;
  }
  return "X";
};

// Ağız şekilleri (Rhubarb A–H, X). A ve X: görseldeki kapalı ağız kalır.
const Agiz: React.FC<{ sekil: string }> = ({ sekil }) => {
  const olcu: Record<string, { w: number; h: number; yuvarlak?: boolean }> = {
    B: { w: 188, h: 20 },
    C: { w: 196, h: 32 },
    D: { w: 200, h: 54 },
    E: { w: 140, h: 46, yuvarlak: true },
    F: { w: 92, h: 32, yuvarlak: true },
    G: { w: 188, h: 24 },
    H: { w: 194, h: 42 },
  };
  const o = olcu[sekil];
  if (!o) return null;
  const { w, h } = o;
  const x0 = -w / 2;
  const x1 = w / 2;
  // üst kenar hafif kavisli, alt kenar daha derin: konuşan, hafif gülümseyen ağız
  const ust = o.yuvarlak
    ? `M ${x0} 0 C ${x0} ${-h * 0.55}, ${x1} ${-h * 0.55}, ${x1} 0`
    : `M ${x0} 0 C ${x0 * 0.5} ${-h * 0.32}, ${x1 * 0.5} ${-h * 0.32}, ${x1} 0`;
  const alt = o.yuvarlak
    ? `C ${x1} ${h * 0.75}, ${x0} ${h * 0.75}, ${x0} 0 Z`
    : `C ${x1 * 0.6} ${h * 1.05}, ${x0 * 0.6} ${h * 1.05}, ${x0} 0 Z`;
  const yol = `${ust} ${alt}`;
  const disGoster = sekil === "B" || sekil === "C" || sekil === "D" || sekil === "G" || sekil === "H";
  return (
    <g>
      {/* alt dudak */}
      <path d={`M ${x0 + 6} 2 C ${x0 * 0.5} ${h * 1.05 + 16}, ${x1 * 0.5} ${h * 1.05 + 16}, ${x1 - 6} 2 Z`} fill={RENK.dudak} />
      <clipPath id={`agiz-${sekil}`}>
        <path d={yol} />
      </clipPath>
      <path d={yol} fill={RENK.ic} />
      <g clipPath={`url(#agiz-${sekil})`}>
        {(sekil === "D" || sekil === "H") && (
          <ellipse cx={0} cy={sekil === "H" ? h * 0.45 : h * 0.75} rx={w * 0.3} ry={h * 0.35} fill={RENK.dil} />
        )}
        {disGoster && <rect x={x0} y={-h} width={w} height={h * (sekil === "B" ? 1.25 : 1.12)} fill={RENK.dis} />}
        {sekil === "B" && <rect x={x0} y={h * 0.55} width={w} height={h} fill={RENK.dis} />}
        {sekil === "G" && <rect x={x0} y={h * 0.6} width={w} height={h} fill={RENK.dudak} />}
      </g>
      <path d={yol} fill="none" stroke={RENK.cizgi} strokeWidth={4.5} strokeLinejoin="round" />
    </g>
  );
};

// Göz kırpma: ~3–4 sn'de bir, 5 karelik (kapan-açıl) kırpma
const kirpmaOrani = (frame: number, fps: number, tohum: number): number => {
  const aralik = Math.round(fps * 3.4);
  const yerel = (frame + tohum) % aralik;
  const egri = [0, 0.6, 1, 1, 0.5];
  return yerel < egri.length ? egri[yerel] : 0;
};

export const Karakter: React.FC<{
  zaman: number; // ses dosyasındaki zaman (sn)
  kirpmaTohum?: number;
  zorlaSekil?: string; // test için: belirli ağız şeklini göster
  style?: React.CSSProperties;
}> = ({ zaman, kirpmaTohum = 0, zorlaSekil, style }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const sekil = zorlaSekil ?? sekilBul(mouthCues, zaman);
  const kapanma = kirpmaOrani(frame, fps, kirpmaTohum);
  // konuşurken baş hafif sallanır, nefes alır
  const konusuyor = sekil !== "X" && sekil !== "A";
  const nefes = Math.sin(frame / (fps * 0.9)) * 0.006;
  const bas = Math.sin(frame / (fps * 0.55)) * (konusuyor ? 1.1 : 0.4);
  return (
    <div
      style={{
        position: "absolute",
        width: PORTRE.w,
        height: PORTRE.h,
        transformOrigin: "50% 100%",
        transform: `rotate(${bas * 0.6}deg) scale(${1 + nefes})`,
        ...style,
      }}
    >
      <Img src={staticFile("pilot/portre.png")} style={{ width: PORTRE.w, height: PORTRE.h }} />
      <svg width={PORTRE.w} height={PORTRE.h} style={{ position: "absolute", left: 0, top: 0 }}>
        <g transform={`translate(${AGIZ.x} ${AGIZ.y}) rotate(${AGIZ.aci})`}>
          <Agiz sekil={sekil} />
        </g>
        {kapanma > 0 &&
          GOZLER.map((g, i) => (
            <g key={i} transform={`translate(${g.x} ${g.y}) rotate(${g.aci})`}>
              <clipPath id={`goz-${i}`}>
                <ellipse cx={0} cy={0} rx={g.w / 2 + 6} ry={g.h / 2 + 6} />
              </clipPath>
              <g clipPath={`url(#goz-${i})`}>
                <rect x={-g.w} y={-g.h / 2 - 8} width={g.w * 2} height={(g.h + 16) * kapanma} fill={RENK.ten} />
                <line
                  x1={-g.w / 2}
                  x2={g.w / 2}
                  y1={-g.h / 2 - 8 + (g.h + 16) * kapanma}
                  y2={-g.h / 2 - 8 + (g.h + 16) * kapanma}
                  stroke={RENK.cizgi}
                  strokeWidth={7}
                  strokeLinecap="round"
                />
              </g>
            </g>
          ))}
      </svg>
    </div>
  );
};
