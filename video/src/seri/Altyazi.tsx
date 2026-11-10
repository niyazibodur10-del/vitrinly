import React from "react";
import { interpolate, useCurrentFrame, useVideoConfig } from "remotion";
import { BANT, fredoka, GUVENLI, RENK } from "./sabitler";
import type { Satir } from "./tipler";
import { obekler } from "./zaman";

// Kelime kelime altyazı: konuşmacının satırı ≤4 kelimelik öbeklere bölünür; kelime söylendiği an belirir,
// o an söylenen kelime konuşmacı rengiyle dolar ve büyür. Öbeğin üstünde konuşmacı adı (renkli hap).
// Yerleşim: güvenli alanda, alt kenar BANT.altyazi.alt (1420) → platform arayüzünün (alt %25, sağ 190 px) dışında.

const CL = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;
const SOL = GUVENLI.sol + 30;
const SAG = GUVENLI.sag;

export const Altyazi: React.FC<{ satirlar: Satir[] }> = ({ satirlar }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;

  // görünür öbek: başlamış son öbek; satır bittikten 0,35 sn sonra (veya sonraki satır başlayınca) söner
  let bulunan: { s: Satir; ob: ReturnType<typeof obekler>[number] } | null = null;
  for (let i = 0; i < satirlar.length; i++) {
    const s = satirlar[i];
    const sonraki = satirlar[i + 1]?.bas ?? Infinity;
    if (t < s.bas - 0.05 || t >= Math.min(s.bitis + 0.35, sonraki - 0.05)) continue;
    for (const ob of obekler(s)) if (ob[0].bas - 0.05 <= t) bulunan = { s, ob };
  }
  if (!bulunan) return null;
  const { s, ob } = bulunan;
  const r = RENK[s.konusmaci];
  const giris = interpolate(t, [ob[0].bas - 0.05, ob[0].bas + 0.08], [0, 1], CL);

  return (
    <div
      style={{
        position: "absolute", left: SOL, width: SAG - SOL, bottom: 1920 - BANT.altyazi.alt,
        display: "flex", flexDirection: "column", alignItems: "center", gap: 10,
      }}
    >
      <div
        style={{
          fontFamily: fredoka, fontWeight: 700, fontSize: 34, letterSpacing: 3, color: "#fff",
          background: r.ana, padding: "4px 20px", borderRadius: 24, boxShadow: `0 4px 0 ${r.koyu}`,
          opacity: giris, transform: `translateY(${(1 - giris) * 10}px)`,
        }}
      >
        {r.ad}
      </div>
      <div style={{ display: "flex", flexWrap: "wrap", justifyContent: "center", columnGap: 20, rowGap: 0, maxWidth: SAG - SOL }}>
        {ob.map((w, i) => {
          const p = interpolate(t, [w.bas - 0.05, w.bas + 0.05], [0, 1], CL);
          const simdi = t >= w.bas - 0.02 && t < w.bitis + 0.04;
          const pop = simdi ? interpolate(t, [w.bas - 0.02, w.bas + 0.08, w.bas + 0.18], [1, 1.12, 1.06], CL) : 1;
          return (
            <span
              key={i}
              style={{
                fontFamily: fredoka, fontWeight: 700, fontSize: 78, lineHeight: 1.12,
                color: simdi ? r.ana : "#ffffff",
                WebkitTextStroke: "12px #0b0d12", paintOrder: "stroke fill",
                textShadow: "0 6px 0 rgba(0,0,0,0.35)",
                opacity: p, transform: `scale(${(0.85 + 0.15 * p) * pop}) translateY(${(1 - p) * 10}px)`,
                display: "inline-block",
              }}
            >
              {w.k}
            </span>
          );
        })}
      </div>
    </div>
  );
};
