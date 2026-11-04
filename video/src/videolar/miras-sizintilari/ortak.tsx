import React from "react";
import { AbsoluteFill, staticFile, useCurrentFrame, useVideoConfig } from "remotion";
import { loadFont } from "@remotion/fonts";

// Yerel yazı tipleri (render tarayıcısı Google Fonts'a erişemiyor). Kaynak: video/src/k1929/ortak.tsx
export const anton = "Anton";
export const fredoka = "Fredoka";
loadFont({ family: anton, url: staticFile("fonts/Anton-400.woff2"), weight: "400" });
loadFont({ family: fredoka, url: staticFile("fonts/Fredoka-700.woff2"), weight: "700" });

// Ortak birleştirici doku: kâğıt greni + vinyet. Gren tohumu 2 karede bir değişir.
export const Doku: React.FC<{ gren?: number; vinyet?: number }> = ({ gren = 0.05, vinyet = 0.4 }) => {
  const frame = useCurrentFrame();
  const { width, height } = useVideoConfig();
  const tohum = Math.floor(frame / 2) % 50;
  return (
    <AbsoluteFill style={{ pointerEvents: "none" }}>
      <AbsoluteFill style={{ background: `radial-gradient(ellipse at 50% 50%, rgba(0,0,0,0) 55%, rgba(0,0,0,${vinyet}) 100%)` }} />
      <svg width={width} height={height} style={{ position: "absolute", opacity: gren, mixBlendMode: "overlay" }}>
        <filter id={`gren-${tohum}`}>
          <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves={2} seed={tohum} stitchTiles="stitch" />
          <feColorMatrix type="saturate" values="0" />
        </filter>
        <rect width="100%" height="100%" filter={`url(#gren-${tohum})`} />
      </svg>
    </AbsoluteFill>
  );
};
