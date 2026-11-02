import React from "react";
import { AbsoluteFill, interpolate, Sequence, useCurrentFrame, useVideoConfig } from "remotion";
import { Audio } from "@remotion/media";
import { ALTYAZI, SAHNELER } from "./veri-sahne";
import { Doku, fredoka } from "./ortak";
import { f } from "./kit";
import { S01, S12 } from "./sahne1";
import { plan } from "./zaman";

// Tam video (16:9) + sahne başına kompozisyonlar + kritik yol testi (animasyon-yonetmeni). Kaynak desen: video/src/k1929/Tam.tsx
export const SAHNE_BILESEN: Record<string, React.FC> = { S01, S12 };
export const FPS = 30;
export const kare = (s: number) => Math.round(s * FPS);
export const TAM_KARE = kare(SAHNELER[SAHNELER.length - 1].bitis);
const sh = (id: string) => SAHNELER.find((x) => x.id === id)!;

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
  const s = sh(id);
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
    {SAHNELER.filter((s) => SAHNE_BILESEN[s.id]).map((s) => {
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

// Kritik yol testi (H4): S01 tamamı (Leo masada konuşur) + S12 başı → matruşka açılışı ("borrowed" + 0,6 sn)
export const kritikParcalar = () => {
  const k12 = plan("S12").k;
  return [
    { id: "S01", bas: 0, sure: sh("S01").sure },
    { id: "S12", bas: 0, sure: k12.borrowed + 0.9 },
  ];
};
export const KRITIK_KARE = kritikParcalar().reduce((a, p) => a + kare(p.sure), 0);
export const KritikTest: React.FC = () => {
  let from = 0;
  return (
    <AbsoluteFill style={{ background: "#000" }}>
      {kritikParcalar().map((p) => {
        const s = sh(p.id);
        const B = SAHNE_BILESEN[p.id];
        const el = (
          <Sequence key={p.id} from={from} durationInFrames={kare(p.sure)} name={p.id}>
            <Audio src={f("anlatim.wav")} trimBefore={kare(s.bas + p.bas)} trimAfter={kare(s.bas + p.bas + p.sure)} />
            <B />
            <Doku />
            <AltyaziParca ofs={s.bas} />
          </Sequence>
        );
        from += kare(p.sure);
        return el;
      })}
    </AbsoluteFill>
  );
};
