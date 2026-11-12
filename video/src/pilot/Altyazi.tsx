import React from "react";
import { AbsoluteFill, interpolate, useCurrentFrame, useVideoConfig } from "remotion";
import { captionChunks } from "./data";
import { fredoka } from "./Sahneler";

// Referans videodaki gibi: 1–5 kelimelik parça, kelimeler söylendikçe belirir, anahtar kelime sarı.
export const Altyazi: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;
  const idx = captionChunks.findIndex((c, i) => {
    const bas = c[0].s - 0.08;
    const son = i + 1 < captionChunks.length ? captionChunks[i + 1][0].s - 0.08 : c[c.length - 1].e + 0.6;
    return t >= bas && t < son;
  });
  if (idx < 0) return null;
  const parca = captionChunks[idx];
  return (
    <AbsoluteFill style={{ justifyContent: "flex-end", alignItems: "center", paddingBottom: 90 }}>
      <div style={{ display: "flex", gap: 22, flexWrap: "wrap", justifyContent: "center", maxWidth: 1500 }}>
        {parca.map((w, i) => {
          const p = interpolate(t, [w.s - 0.06, w.s + 0.06], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
          return (
            <span
              key={i}
              style={{
                fontFamily: fredoka,
                fontWeight: 700,
                fontSize: 84,
                color: w.hl ? "#ffd43b" : "#ffffff",
                WebkitTextStroke: "14px #111111",
                paintOrder: "stroke fill",
                opacity: p,
                transform: `scale(${0.85 + 0.15 * p}) translateY(${(1 - p) * 12}px)`,
                display: "inline-block",
              }}
            >
              {w.t}
            </span>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};
