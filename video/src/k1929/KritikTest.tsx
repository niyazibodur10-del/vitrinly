import React from "react";
import { AbsoluteFill, Easing, Img, interpolate, Sequence, useCurrentFrame, useVideoConfig } from "remotion";
import { Audio } from "@remotion/media";
import { PARCALAR } from "./veri";
import { Altyazi, anton, Doku, fredoka, IllustrationEtiketi, k, KapiIsik, kapiMerkezX } from "./ortak";
import { Sunucu, YUZ } from "./Sunucu";
import { Klon } from "./Klon";

// F5 kritik yol testi (1929-1000-dolar): S01 hook başı (0.0–8.0 sn) + S04 klon yürüyüşü ve "Remember that laugh"
// (62.0–73.7 sn). Ses: public/k1929/kritik-ses.wav (iki parçanın birleşimi, 07-animasyon/hazirla.py).
const [P1, P2] = PARCALAR;
export const KRITIK_SURE = P1.sure + P2.sure;
const CL = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;

// Kamera: odak noktası (plaka koordinatı) ekran merkezine, ölçek s
const kamera = (fx: number, fy: number, s: number): React.CSSProperties => ({
  position: "absolute",
  width: 1920,
  height: 1080,
  transformOrigin: "0 0",
  translate: `${960 - fx * s}px ${540 - fy * s}px`,
  scale: String(s),
});

const kelimeAn = (p: typeof P1, w: string, sonra = 0) => p.kelimeler.find((x) => x.t.toLowerCase().startsWith(w.toLowerCase()) && x.s >= sonra)!.s;

// ---------- Parça 1: S01 ----------
const Sokak: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;
  const p = interpolate(t, [0.2, 0.45], [0, 1], { ...CL, easing: Easing.out(Easing.back(1.6)) });
  return (
    <AbsoluteFill style={{ background: "#000" }}>
      <AbsoluteFill style={{ ...kamera(1000, 520, interpolate(t, [0, 2.2], [1.0, 1.07])) }}>
        <Img src={k("C15.jpg")} style={{ width: 1920, height: 1080 }} />
      </AbsoluteFill>
      <AbsoluteFill style={{ justifyContent: "center", alignItems: "center" }}>
        <div
          style={{
            fontFamily: anton,
            fontSize: 190,
            color: "#fff3d6",
            letterSpacing: 8,
            WebkitTextStroke: "10px #1a1208",
            paintOrder: "stroke fill",
            opacity: p,
            scale: String(0.7 + 0.3 * p),
            translate: `0px -60px`,
          }}
        >
          SEPT 1929
        </div>
      </AbsoluteFill>
      <IllustrationEtiketi />
    </AbsoluteFill>
  );
};

const STUDYO_BAS = 2.1; // whoosh kesmesi ("You" 2.20'den hemen önce)

const StudyoKapilar: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps + STUDYO_BAS;
  const s = interpolate(t, [STUDYO_BAS, 8], [1.1, 1.14]);
  const kay = interpolate(frame, [0, 6], [140, 0], { ...CL, easing: Easing.out(Easing.cubic) });
  return (
    <AbsoluteFill style={{ background: "#05070f", overflow: "hidden" }}>
      <div style={{ ...kamera(1047 - kay, 582, s) }}>
        <Img src={k("C01.jpg")} style={{ width: 1920, height: 1080 }} />
        <KapiIsik ad="mavi" an={kelimeAn(P1, "stock") - STUDYO_BAS} />
        <KapiIsik ad="yesil" an={kelimeAn(P1, "bank") - STUDYO_BAS} />
        <KapiIsik ad="kahve" an={kelimeAn(P1, "shoebox") - STUDYO_BAS} />
      </div>
    </AbsoluteFill>
  );
};

// "$1,000": söylendiği an ortada sayaç gibi dolar, sonra köşe göstergesine küçülür (SEPT 1929 ile)
const BinDolar: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps + STUDYO_BAS;
  const an = kelimeAn(P1, "$1");
  const deger = Math.round(interpolate(t, [an, an + 0.5], [0, 1000], { ...CL, easing: Easing.out(Easing.cubic) }));
  const p = interpolate(t, [an - 0.04, an + 0.14], [0, 1], { ...CL, easing: Easing.out(Easing.back(1.8)) });
  const kos = interpolate(t, [3.75, 4.05], [0, 1], { ...CL, easing: Easing.inOut(Easing.cubic) });
  return (
    <div
      style={{
        position: "absolute",
        left: interpolate(kos, [0, 1], [700, 60]),
        top: interpolate(kos, [0, 1], [330, 34]),
        translate: `${interpolate(kos, [0, 1], [-50, 0])}% 0%`,
        fontFamily: anton,
        fontSize: interpolate(kos, [0, 1], [250, 92]),
        color: "#ffd43b",
        WebkitTextStroke: `${interpolate(kos, [0, 1], [16, 8])}px #120c02`,
        paintOrder: "stroke fill",
        opacity: p,
        scale: String(0.6 + 0.4 * p),
        lineHeight: 1,
        whiteSpace: "nowrap",
        display: "flex",
        alignItems: "baseline",
        gap: 24,
      }}
    >
      ${deger.toLocaleString("en-US")}
      <span style={{ fontSize: "0.42em", color: "#fff3d6", opacity: kos }}>SEPT 1929</span>
    </div>
  );
};

const Parca1: React.FC = () => {
  const { fps } = useVideoConfig();
  const ucKapi = kelimeAn(P1, "three"); // "Three doors" → iki elle kapıları sunar (C12)
  const sunucuYer = (s: number): React.CSSProperties => ({
    position: "absolute",
    left: 1640 - YUZ.x * s,
    top: 352 - YUZ.y * s,
    scale: String(s),
    transformOrigin: "0 0",
  });
  return (
    <AbsoluteFill>
      <Sequence durationInFrames={Math.round(STUDYO_BAS * fps)} name="sokak C15">
        <Sokak />
      </Sequence>
      <Sequence from={Math.round(STUDYO_BAS * fps)} name="stüdyo C01 + sunucu">
        <StudyoKapilar />
        <Sequence durationInFrames={Math.round((ucKapi - STUDYO_BAS) * fps)} name="sunucu a" layout="none">
          <div style={sunucuYer(1.0)}>
            <Sunucu cues={P1.agiz} ofs={STUDYO_BAS} poz="a" tohum={3} />
          </div>
        </Sequence>
        <Sequence from={Math.round((ucKapi - STUDYO_BAS) * fps)} name="sunucu C12 (Three doors)" layout="none">
          <div style={sunucuYer(1.0)}>
            <Sunucu cues={P1.agiz} ofs={ucKapi} poz="C12" tohum={5} giris />
          </div>
        </Sequence>
        <BinDolar />
        <Flas />
      </Sequence>
      <Altyazi kelimeler={P1.kelimeler} />
    </AbsoluteFill>
  );
};

const Flas: React.FC = () => {
  const frame = useCurrentFrame();
  return <AbsoluteFill style={{ background: "#fff", opacity: interpolate(frame, [0, 4], [0.85, 0], CL) }} />;
};

// ---------- Parça 2: S04 ----------
const YAKIN_BAS = 10.5; // "Remember that laugh" yakın planı

const HaHa: React.FC<{ an: number }> = ({ an }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;
  const yerler: [number, number, number][] = [
    [470, 250, -9],
    [1420, 210, 7],
    [560, 640, 6],
    [1480, 620, -6],
  ];
  return (
    <>
      {yerler.map(([x, y, r], i) => {
        const a = an + i * 0.32;
        const p = interpolate(t, [a, a + 0.12, YAKIN_BAS - 0.5, YAKIN_BAS - 0.2], [0, 1, 1, 0], CL);
        return (
          <div
            key={i}
            style={{
              position: "absolute",
              left: x,
              top: y,
              fontFamily: fredoka,
              fontWeight: 700,
              fontSize: 78,
              color: "#fff3d6",
              WebkitTextStroke: "11px #0b0b0b",
              paintOrder: "stroke fill",
              rotate: `${r + Math.sin(t * 9 + i) * 3}deg`,
              opacity: p,
              scale: String(0.5 + 0.5 * p),
            }}
          >
            HA!
          </div>
        );
      })}
    </>
  );
};

const KapiSahnesi: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;
  const g = (w: string, sonra = 0) => kelimeAn(P2, w, sonra);
  const kahkaha = g("laughs");
  const punchBas = kahkaha - 0.25;
  const pz = interpolate(t, [punchBas, punchBas + 0.4], [0, 1], { ...CL, easing: Easing.inOut(Easing.cubic) });
  const s = interpolate(t, [0, punchBas], [1.0, 1.035], CL) * (1 - pz) + 1.42 * pz;
  const fx = interpolate(pz, [0, 1], [960, kapiMerkezX("kahve")]);
  const fy = interpolate(pz, [0, 1], [560, 600]);
  const AYAK = 792, BOY = 410, GIRIS = 2060;
  return (
    <AbsoluteFill style={{ background: "#05070f", overflow: "hidden" }}>
      <div style={kamera(fx, fy, s)}>
        <Img src={k("C01.jpg")} style={{ width: 1920, height: 1080 }} />
        <KapiIsik ad="mavi" an={g("blue") + 0.1} yaziHazir />
        <KapiIsik ad="yesil" an={g("green") + 0.1} yaziHazir />
        <KapiIsik ad="kahve" an={g("brown") + 0.1} yaziHazir />
        <Klon
          yurume="C04"
          durus="C02"
          xBas={GIRIS}
          xBit={kapiMerkezX("mavi")}
          bas={0.12}
          bit={3.3}
          ayakY={AYAK}
          boy={BOY}
          rozet={{ etiket: "STOCK", renk: "#4da3ff" }}
          isim={{ metin: "STOCK LEO", an: g("stock"), son: 3.6 }}
          tohum={0.4}
        />
        <Klon
          yurume="C04"
          durus="C02"
          xBas={GIRIS}
          xBit={kapiMerkezX("yesil")}
          bas={1.95}
          bit={4.55}
          ayakY={AYAK}
          boy={BOY}
          rozet={{ etiket: "BANK", renk: "#5fd35f" }}
          isim={{ metin: "BANK LEO", an: g("bank"), son: 4.9 }}
          tohum={1.3}
        />
        <Klon
          yurume="C05"
          durus="C05"
          xBas={GIRIS}
          xBit={kapiMerkezX("kahve")}
          bas={3.95}
          bit={6.6}
          ayakY={AYAK}
          boy={BOY}
          rozet={{ etiket: "BOX", renk: "#e0884a" }}
          isim={{ metin: "BOX LEO", an: g("box"), son: 7.4 }}
          ezil={kahkaha}
          tohum={2.1}
        />
      </div>
      <HaHa an={kahkaha + 0.05} />
    </AbsoluteFill>
  );
};

const YakinPlan: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;
  const s = interpolate(t, [0, P2.sure - YAKIN_BAS], [1.22, 1.27]);
  const laugh = kelimeAn(P2, "laugh.");
  return (
    <AbsoluteFill style={{ background: "#05070f", overflow: "hidden" }}>
      <div style={{ ...kamera(1290, 420, 1.12), filter: "blur(7px) brightness(0.78)" }}>
        <Img src={k("C03.jpg")} style={{ width: 1920, height: 1080 }} />
      </div>
      <div style={{ position: "absolute", left: 1010 - YUZ.x * s, top: 410 - YUZ.y * s, scale: String(s), transformOrigin: "0 0" }}>
        <Sunucu cues={P2.agiz} ofs={YAKIN_BAS} poz="a" tohum={2} wink={[laugh + 0.2, laugh + 0.58]} />
      </div>
    </AbsoluteFill>
  );
};

const Parca2: React.FC = () => {
  const { fps } = useVideoConfig();
  return (
    <AbsoluteFill>
      <Sequence durationInFrames={Math.round(YAKIN_BAS * fps)} name="C01 klonlar kapılara">
        <KapiSahnesi />
      </Sequence>
      <Sequence from={Math.round(YAKIN_BAS * fps)} name="yakın plan: Remember that laugh (wink)">
        <YakinPlan />
      </Sequence>
      <Altyazi kelimeler={P2.kelimeler} />
    </AbsoluteFill>
  );
};

export const KritikTest: React.FC = () => {
  const { fps } = useVideoConfig();
  return (
    <AbsoluteFill style={{ background: "#000" }}>
      <Audio src={k("kritik-ses.wav")} />
      <Sequence durationInFrames={Math.round(P1.sure * fps)} name="S01 hook">
        <Parca1 />
      </Sequence>
      <Sequence from={Math.round(P1.sure * fps)} name="S04 klonlar">
        <Parca2 />
      </Sequence>
      <Doku />
    </AbsoluteFill>
  );
};
