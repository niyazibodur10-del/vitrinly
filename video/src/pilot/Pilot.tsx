import React from "react";
import { AbsoluteFill, interpolate, Sequence, staticFile, useCurrentFrame, useVideoConfig } from "remotion";
import { Audio } from "@remotion/media";
import { Karakter } from "./Karakter";
import { BirikimSahne, SabahArka, Yil1923 } from "./Sahneler";
import { Altyazi } from "./Altyazi";

// Pilot v2 sesi: Kokoro am_fenrir 0.9 anlatım + CC0 müzik/efekt miksi (1.0 sn müzik girişi, 2.0 sn çıkış).
// Zamanlar uretim/ses-testi/pilot/v2/anlatim-v2-kelimeler.json (+1.0 sn ofset) ve agiz-zamanlari.json'dan.
export const PILOT_SURE = 14.1; // sn, public/pilot-ses.wav (14.10 sn)

// Sahne sınırları (sn, ses zamanına göre)
const S = {
  sabah: [0, 2.8], // "Imagine waking up one morning" (konuşma 1.00–2.80)
  birikim: [2.8, 6.5], // "and your savings ... coffee" (2.80–5.92)
  sasirma: [6.5, 8.0], // "Sounds impossible?" (6.76–7.58)
  yil: [8.0, 10.3], // "In 1923, in Germany," (8.24–10.14)
  final: [10.3, PILOT_SURE], // "that's exactly what happened." (10.48–11.88) + müzik çıkışı
} as const;

// Kelime tetikli animasyonlar (Whisper kelime başlangıcı, ses zamanı)
const KELIME = { cup: 5.1, Germany: 9.68 } as const;

// Sequence içindeki karakter, ses zamanını sahne başlangıcı + yerel kareden hesaplar
const KarakterPlan: React.FC<{
  bas: number;
  x: number;
  y: number;
  olcek: number;
  zoomBitis?: number;
  sallanma?: boolean;
  tohum?: number;
}> = ({ bas, x, y, olcek, zoomBitis, sallanma, tohum }) => {
  const frame = useCurrentFrame();
  const { fps, durationInFrames } = useVideoConfig();
  const z = zoomBitis ? interpolate(frame, [0, durationInFrames], [olcek, zoomBitis]) : olcek;
  const titreme = sallanma ? interpolate(frame, [0, 6, 12], [14, -8, 0], { extrapolateRight: "clamp" }) : 0;
  return (
    <AbsoluteFill style={{ transform: `translate(${x + titreme}px, ${y}px) scale(${z})`, transformOrigin: "0 0" }}>
      <Karakter zaman={bas + frame / fps} kirpmaTohum={tohum} />
    </AbsoluteFill>
  );
};

export const Pilot: React.FC = () => {
  const { fps } = useVideoConfig();
  const f = (s: number) => Math.round(s * fps);
  const seq = (a: readonly [number, number]) => ({ from: f(a[0]), durationInFrames: f(a[1]) - f(a[0]) });
  return (
    <AbsoluteFill style={{ background: "#0d1a33" }}>
      <Audio src={staticFile("pilot-ses.wav")} />

      {/* 1: "Imagine waking up one morning" — sabah odası, yavaş yaklaşma */}
      <Sequence {...seq(S.sabah)}>
        <SabahArka />
        <KarakterPlan bas={S.sabah[0]} x={760} y={60} olcek={0.92} zoomBitis={0.98} tohum={20} />
      </Sequence>

      {/* 2: "and your savings are worth less than a cup of coffee" — grafik + köşede konuşan karakter */}
      <Sequence {...seq(S.birikim)}>
        <BirikimSahne sure={S.birikim[1] - S.birikim[0]} fincanAn={KELIME.cup - S.birikim[0]} />
        <KarakterPlan bas={S.birikim[0]} x={1420} y={640} olcek={0.42} tohum={5} />
      </Sequence>

      {/* 3: "Sounds impossible?" — yüze ani yakınlaşma */}
      <Sequence {...seq(S.sasirma)}>
        <SabahArka karartma={0.25} />
        <KarakterPlan bas={S.sasirma[0]} x={60} y={-420} olcek={1.55} zoomBitis={1.62} sallanma tohum={40} />
      </Sequence>

      {/* 4: "In 1923, in Germany" — eski kâğıt, yıl ve mühür */}
      <Sequence {...seq(S.yil)}>
        <Yil1923 muhurAn={KELIME.Germany - S.yil[0]} />
      </Sequence>

      {/* 5: "that's exactly what happened" — ciddi ton, soğuk ışık */}
      <Sequence {...seq(S.final)}>
        <SabahArka karartma={0.55} />
        <KarakterPlan bas={S.final[0]} x={520} y={20} olcek={0.98} zoomBitis={1.08} tohum={11} />
      </Sequence>

      <Altyazi />
    </AbsoluteFill>
  );
};
