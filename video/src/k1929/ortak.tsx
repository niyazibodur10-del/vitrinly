import React from "react";
import { AbsoluteFill, interpolate, staticFile, useCurrentFrame, useVideoConfig } from "remotion";
import { loadFont } from "@remotion/fonts";
import { Kelime } from "./veri";

// Yerel yazı tipleri (render tarayıcısı Google Fonts'a erişemiyor)
export const anton = "Anton";
export const fredoka = "Fredoka";
loadFont({ family: anton, url: staticFile("fonts/Anton-400.woff2"), weight: "400" });
loadFont({ family: fredoka, url: staticFile("fonts/Fredoka-700.woff2"), weight: "700" });

export const k = (ad: string) => staticFile(`k1929/${ad}`);

// C01 kapı ölçümleri (05-gorsel/kapilar/C01-kapi-koordinatlari.json, 1920x1080 plaka koordinatı)
export const KAPI = {
  mavi: { kasa: [480, 307, 763, 751], panel: [524, 344, 197, 404], levha: [523, 241, 719, 290], renk: "#4da3ff", etiket: "STOCKS" },
  yesil: { kasa: [822, 318, 1073, 750], panel: [851, 345, 195, 402], levha: [850, 241, 1046, 290], renk: "#5fd35f", etiket: "BANK" },
  kahve: { kasa: [1130, 299, 1415, 750], panel: [1175, 344, 196, 403], levha: [1175, 241, 1371, 291], renk: "#e0884a", etiket: "SHOEBOX" },
} as const;
export type KapiAd = keyof typeof KAPI;
export const kapiMerkezX = (ad: KapiAd) => (KAPI[ad].kasa[0] + KAPI[ad].kasa[2]) / 2;

const CL = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;

// Kapı levhası yazısı + kapı ışığı (plaka koordinatında; kamera katmanının içinde kullanılır)
export const KapiIsik: React.FC<{ ad: KapiAd; an: number; parlama?: number; yaziHazir?: boolean }> = ({ ad, an, parlama = 1, yaziHazir = false }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;
  const d = KAPI[ad];
  const p = yaziHazir ? 1 : interpolate(t, [an - 0.05, an + 0.12], [0, 1], CL);
  const tepe = interpolate(t, [an, an + 0.15, an + 0.9], [0, 1, 0.35], CL) * parlama;
  const [lx0, ly0, lx1, ly1] = d.levha;
  const [px, py, pw, ph] = d.panel;
  return (
    <>
      <div
        style={{
          position: "absolute",
          left: px - 60,
          top: py - 40,
          width: pw + 120,
          height: ph + 80,
          background: `radial-gradient(ellipse at 50% 55%, ${d.renk} 0%, ${d.renk}00 70%)`,
          mixBlendMode: "screen",
          opacity: tepe * 0.75,
        }}
      />
      <div
        style={{
          position: "absolute",
          left: lx0,
          top: ly0,
          width: lx1 - lx0,
          height: ly1 - ly0,
          display: "flex",
          alignItems: "center",
          justifyContent: "center",
          fontFamily: anton,
          fontSize: 36,
          letterSpacing: 3,
          color: "#fff6dc",
          textShadow: `0 0 ${6 + 14 * tepe}px ${d.renk}, 0 2px 0 #000`,
          opacity: p,
          scale: String(0.6 + 0.4 * p + 0.08 * tepe),
        }}
      >
        {d.etiket}
      </div>
    </>
  );
};

// Kelime kelime altyazı: 1–3 kelimelik parça, noktalama parçayı bitirir; anahtar kelime kendi renginde.
const parcala = (k: Kelime[]): Kelime[][] => {
  const out: Kelime[][] = [];
  let cur: Kelime[] = [];
  for (const w of k) {
    cur.push(w);
    if (cur.length >= 3 || /[.,?!]$/.test(w.t)) {
      out.push(cur);
      cur = [];
    }
  }
  if (cur.length) out.push(cur);
  return out;
};

export const Altyazi: React.FC<{ kelimeler: Kelime[]; ofs?: number; alt?: number; boyut?: number }> = ({
  kelimeler,
  ofs = 0,
  alt = 70,
  boyut = 76,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps + ofs;
  const parcalar = parcala(kelimeler);
  const idx = parcalar.findIndex((c, i) => {
    const bas = c[0].s - 0.08;
    const son = i + 1 < parcalar.length ? parcalar[i + 1][0].s - 0.08 : c[c.length - 1].e + 0.45;
    return t >= bas && t < son;
  });
  if (idx < 0) return null;
  return (
    <AbsoluteFill style={{ justifyContent: "flex-end", alignItems: "center", paddingBottom: alt, pointerEvents: "none" }}>
      <div style={{ display: "flex", gap: 20, flexWrap: "wrap", justifyContent: "center", maxWidth: 1500 }}>
        {parcalar[idx].map((w, i) => {
          const p = interpolate(t, [w.s - 0.06, w.s + 0.05], [0, 1], CL);
          return (
            <span
              key={i}
              style={{
                fontFamily: fredoka,
                fontWeight: 700,
                fontSize: boyut,
                color: w.renk ?? "#ffffff",
                WebkitTextStroke: "13px #0b0b0b",
                paintOrder: "stroke fill",
                opacity: p,
                scale: String(0.85 + 0.15 * p),
                translate: `0px ${(1 - p) * 12}px`,
                display: "inline-block",
                textTransform: "uppercase",
              }}
            >
              {w.t.replace(/[,]$/, "")}
            </span>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};

// Ortak birleştirici doku: kâğıt greni + vinyet (gorsel-varlik-sanatcisi önerisi). Gren tohumu 2 karede bir değişir.
export const Doku: React.FC<{ gren?: number; vinyet?: number }> = ({ gren = 0.06, vinyet = 0.45 }) => {
  const frame = useCurrentFrame();
  const tohum = Math.floor(frame / 2) % 50;
  return (
    <AbsoluteFill style={{ pointerEvents: "none" }}>
      <AbsoluteFill style={{ background: `radial-gradient(ellipse at 50% 50%, rgba(0,0,0,0) 55%, rgba(0,0,0,${vinyet}) 100%)` }} />
      <svg width={1920} height={1080} style={{ position: "absolute", opacity: gren, mixBlendMode: "overlay" }}>
        <filter id={`gren-${tohum}`}>
          <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves={2} seed={tohum} stitchTiles="stitch" />
          <feColorMatrix type="saturate" values="0" />
        </filter>
        <rect width="100%" height="100%" filter={`url(#gren-${tohum})`} />
      </svg>
    </AbsoluteFill>
  );
};

// "Illustration" etiketi (politika B2/P5: dönem plakaları görünürken zorunlu)
export const IllustrationEtiketi: React.FC = () => (
  <div
    style={{
      position: "absolute",
      left: 36,
      bottom: 32,
      padding: "6px 14px",
      borderRadius: 8,
      background: "rgba(0,0,0,0.45)",
      color: "rgba(255,255,255,0.85)",
      fontFamily: fredoka,
      fontWeight: 700,
      fontSize: 24,
      letterSpacing: 1,
    }}
  >
    Illustration
  </div>
);
