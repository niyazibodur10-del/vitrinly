import React from "react";
import { AbsoluteFill, interpolate, Sequence, useCurrentFrame, useVideoConfig } from "remotion";
import { Audio } from "@remotion/media";
import { ALTYAZI, SAHNELER } from "./veri-tam";
import { Doku, fredoka } from "./ortak";
import { f } from "./kit";
import { S01, S02, S03, S04 } from "./b1";
import { S05, S06, S07, S08, S09, S10 } from "./b2";
import { S11, S12, S13, S14, S15, S16 } from "./b3";
import { S17, S18, S19, S20, S21, S22, S23, S24 } from "./b4";

// Tam video (16:9) ve sahne başına kompozisyonlar. Kurgu-editoru: sahne kompozisyonları (K1929-Sxx) kendi anlatım
// parçasıyla birlikte gelir; K1929Tam hepsini tek anlatımla dizer (parça render: tools/render-parca.sh).
export const SAHNE_BILESEN: Record<string, React.FC> = { S01, S02, S03, S04, S05, S06, S07, S08, S09, S10, S11, S12, S13, S14, S15, S16, S17, S18, S19, S20, S21, S22, S23, S24 };
export const FPS = 30;
export const kare = (s: number) => Math.round(s * FPS);
export const TAM_KARE = kare(SAHNELER[SAHNELER.length - 1].bitis);

// Altyazı: ses-muhendisi parçaları (altyazi-parcalar.json, global zaman); ofs = sahnenin global başlangıcı
export const AltyaziParca: React.FC<{ ofs: number; alt?: number; boyut?: number; genislik?: number }> = ({ ofs, alt = 70, boyut = 74, genislik = 1500 }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps + ofs;
  const i = ALTYAZI.findIndex((c, k) => {
    const bas = c[0].s - 0.08;
    const son = k + 1 < ALTYAZI.length ? Math.min(ALTYAZI[k + 1][0].s - 0.08, c[c.length - 1].e + 0.9) : c[c.length - 1].e + 0.6;
    return t >= bas && t < son;
  });
  if (i < 0) return null;
  return (
    <AbsoluteFill style={{ justifyContent: "flex-end", alignItems: "center", paddingBottom: alt, pointerEvents: "none" }}>
      <div style={{ display: "flex", gap: 18, flexWrap: "wrap", justifyContent: "center", maxWidth: genislik }}>
        {ALTYAZI[i].map((w, k) => {
          const p = interpolate(t, [w.s - 0.06, w.s + 0.05], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
          return (
            <span
              key={k}
              style={{
                fontFamily: fredoka,
                fontWeight: 700,
                fontSize: boyut,
                color: w.renk ?? "#ffffff",
                WebkitTextStroke: `${Math.round(boyut * 0.17)}px #0b0b0b`,
                paintOrder: "stroke fill",
                opacity: p,
                scale: String(0.85 + 0.15 * p),
                translate: `0px ${(1 - p) * 12}px`,
                display: "inline-block",
                textTransform: "uppercase",
              }}
            >
              {w.t.replace(/[,;:]$/, "")}
            </span>
          );
        })}
      </div>
    </AbsoluteFill>
  );
};

// Tek sahne kompozisyonu: sahnenin anlatım parçası + sahne + doku + altyazı
export const SahneComp: React.FC<{ id: string; altyazi?: boolean }> = ({ id, altyazi = true }) => {
  const s = SAHNELER.find((x) => x.id === id)!;
  const B = SAHNE_BILESEN[id];
  return (
    <AbsoluteFill style={{ background: "#000" }}>
      <Audio src={f("anlatim.wav")} trimBefore={kare(s.bas)} />
      <B />
      <Doku />
      {altyazi ? <AltyaziParca ofs={s.bas} /> : null}
    </AbsoluteFill>
  );
};

export const Tam: React.FC<{ altyazi?: boolean }> = ({ altyazi = true }) => (
  <AbsoluteFill style={{ background: "#000" }}>
    <Audio src={f("anlatim.wav")} />
    {SAHNELER.map((s) => {
      const B = SAHNE_BILESEN[s.id];
      return (
        <Sequence key={s.id} from={kare(s.bas)} durationInFrames={kare(s.bitis) - kare(s.bas)} name={s.id} premountFor={30}>
          <B />
        </Sequence>
      );
    })}
    <Doku />
    {altyazi ? <AltyaziParca ofs={0} /> : null}
  </AbsoluteFill>
);
