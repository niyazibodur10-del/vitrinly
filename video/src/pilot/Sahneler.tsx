import React from "react";
import { AbsoluteFill, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig } from "remotion";
import { loadFont } from "@remotion/fonts";

// Yazı tipleri yerelde (public/fonts, OFL lisanslı): render tarayıcısı Google Fonts'a erişemiyor.
export const anton = "Anton";
export const fredoka = "Fredoka";
loadFont({ family: anton, url: staticFile("fonts/Anton-400.woff2"), weight: "400" });
loadFont({ family: fredoka, url: staticFile("fonts/Fredoka-700.woff2"), weight: "700" });

// Sabah: güneşin doğduğu pencere, sıcak duvar. Karakterin arkasında.
export const SabahArka: React.FC<{ karartma?: number }> = ({ karartma = 0 }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const gunes = interpolate(frame, [0, fps * 6], [430, 330], { extrapolateRight: "clamp" });
  return (
    <AbsoluteFill style={{ background: "linear-gradient(180deg, #f2c48f 0%, #e7a06a 100%)" }}>
      <svg width={1920} height={1080} style={{ position: "absolute" }}>
        <defs>
          <linearGradient id="gok" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0" stopColor="#7fb7e0" />
            <stop offset="0.55" stopColor="#ffd6a0" />
            <stop offset="1" stopColor="#ff9f6e" />
          </linearGradient>
          <radialGradient id="isik" cx="0.5" cy="0.5" r="0.5">
            <stop offset="0" stopColor="#fff4d6" stopOpacity="0.9" />
            <stop offset="1" stopColor="#fff4d6" stopOpacity="0" />
          </radialGradient>
        </defs>
        {/* pencere */}
        <rect x={150} y={120} width={760} height={620} fill="url(#gok)" />
        <circle cx={520} cy={gunes} r={150} fill="url(#isik)" />
        <circle cx={520} cy={gunes} r={62} fill="#fff1c9" />
        {/* şehir silueti */}
        {[
          [150, 560, 90, 180], [240, 500, 70, 240], [310, 590, 110, 150], [420, 470, 80, 270],
          [500, 540, 120, 200], [620, 450, 70, 290], [690, 560, 100, 180], [790, 520, 120, 220],
        ].map(([x, y, w, h], i) => (
          <rect key={i} x={x} y={y} width={w} height={h} fill={i % 2 ? "#6b4552" : "#5a3846"} />
        ))}
        {/* pencere çerçevesi */}
        <rect x={150} y={120} width={760} height={620} fill="none" stroke="#2b1a14" strokeWidth={14} />
        <line x1={530} y1={120} x2={530} y2={740} stroke="#2b1a14" strokeWidth={12} />
        <line x1={150} y1={420} x2={910} y2={420} stroke="#2b1a14" strokeWidth={12} />
        <rect x={120} y={740} width={820} height={34} fill="#8a5a3c" stroke="#2b1a14" strokeWidth={8} />
        {/* odaya düşen ışık */}
        <polygon points="150,740 910,740 1500,1080 420,1080" fill="#fff0c8" opacity={0.18} />
      </svg>
      <AbsoluteFill style={{ background: "#0b1530", opacity: karartma }} />
    </AbsoluteFill>
  );
};

// Birikim -> bir fincan kahve
export const BirikimSahne: React.FC<{ sure: number; fincanAn: number }> = ({ fincanAn }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;
  const erime = interpolate(t, [0.6, fincanAn], [1, 0.06], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  const fincan = spring({ frame: frame - Math.round(fincanAn * fps), fps, config: { damping: 12 } });
  const deste = 14;
  const gorunen = Math.max(1, Math.round(deste * erime));
  return (
    <AbsoluteFill style={{ background: "radial-gradient(circle at 40% 45%, #1d3461 0%, #0d1a33 75%)" }}>
      <svg width={1920} height={1080} style={{ position: "absolute" }}>
        {Array.from({ length: 24 }).map((_, i) => (
          <line key={i} x1={i * 80} y1={0} x2={i * 80} y2={1080} stroke="#ffffff" opacity={0.04} />
        ))}
        {/* banknot destesi */}
        <g transform="translate(520 760)">
          {Array.from({ length: gorunen }).map((_, i) => (
            <g key={i} transform={`translate(${(i % 2) * 6} ${-i * 34})`}>
              <rect x={-190} y={-30} width={380} height={60} rx={6} fill="#5fae6a" stroke="#1d3b22" strokeWidth={6} />
              <rect x={-170} y={-18} width={340} height={36} rx={4} fill="none" stroke="#2f6b39" strokeWidth={3} />
              <circle cx={0} cy={0} r={18} fill="#8fd09a" stroke="#2f6b39" strokeWidth={3} />
            </g>
          ))}
        </g>
        <text x={520} y={850} textAnchor="middle" fill="#ffffff" style={{ fontFamily: fredoka, fontWeight: 700, fontSize: 54, letterSpacing: 4 }}>
          YOUR SAVINGS
        </text>
        {/* eşittir ve kahve */}
        <g opacity={fincan}>
          <text x={940} y={560} textAnchor="middle" fill="#ffd43b" style={{ fontFamily: anton, fontSize: 160 }}>
            =
          </text>
        </g>
        <g transform={`translate(1290 600) scale(${fincan})`}>
          <path d="M -140 -110 L 140 -110 L 115 120 Q 110 150 80 150 L -80 150 Q -110 150 -115 120 Z" fill="#f4efe6" stroke="#20120c" strokeWidth={10} />
          <path d="M 138 -60 C 230 -60, 230 70, 125 70" fill="none" stroke="#20120c" strokeWidth={26} />
          <path d="M 138 -60 C 210 -60, 210 70, 125 70" fill="none" stroke="#f4efe6" strokeWidth={12} />
          <ellipse cx={0} cy={-110} rx={140} ry={26} fill="#6b3b22" stroke="#20120c" strokeWidth={10} />
          {[-50, 0, 50].map((x, i) => (
            <path
              key={i}
              d={`M ${x} -160 C ${x - 25} -200, ${x + 25} -230, ${x} -270`}
              fill="none"
              stroke="#ffffff"
              strokeWidth={9}
              strokeLinecap="round"
              opacity={0.35 + 0.25 * Math.sin(frame / 6 + i)}
            />
          ))}
          <ellipse cx={0} cy={175} rx={210} ry={26} fill="#e9e2d6" stroke="#20120c" strokeWidth={8} />
        </g>
      </svg>
    </AbsoluteFill>
  );
};

// 1923 / Germany: eski kâğıt, büyük yıl, kırmızı mühür
export const Yil1923: React.FC<{ muhurAn: number }> = ({ muhurAn }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const yil = spring({ frame: frame - 4, fps, config: { damping: 14, mass: 0.8 } });
  const muhur = spring({ frame: frame - Math.round(muhurAn * fps), fps, config: { damping: 9, stiffness: 180 } });
  const zoom = interpolate(frame, [0, fps * 5], [1, 1.06]);
  return (
    <AbsoluteFill style={{ background: "#e8d9b8", transform: `scale(${zoom})` }}>
      <svg width={1920} height={1080} style={{ position: "absolute" }}>
        <defs>
          <filter id="kagit">
            <feTurbulence type="fractalNoise" baseFrequency="0.9" numOctaves="2" seed={frame % 4} />
            <feColorMatrix values="0 0 0 0 0.35  0 0 0 0 0.25  0 0 0 0 0.12  0 0 0 0.22 0" />
          </filter>
          <radialGradient id="vinyet" cx="0.5" cy="0.5" r="0.75">
            <stop offset="0.55" stopColor="#3a2410" stopOpacity="0" />
            <stop offset="1" stopColor="#3a2410" stopOpacity="0.65" />
          </radialGradient>
        </defs>
        <rect width={1920} height={1080} filter="url(#kagit)" />
        <text
          x={960}
          y={640}
          textAnchor="middle"
          fill="#3b2414"
          opacity={yil}
          style={{ fontFamily: anton, fontSize: 420, letterSpacing: 20 }}
          transform={`translate(960 540) scale(${0.6 + 0.4 * yil}) translate(-960 -540)`}
        >
          1923
        </text>
        <g opacity={muhur > 0.01 ? 1 : 0} transform={`translate(1240 760) rotate(-9) scale(${2.2 - 1.2 * muhur})`}>
          <rect x={-330} y={-80} width={660} height={160} rx={14} fill="none" stroke="#b3261e" strokeWidth={14} />
          <text x={0} y={52} textAnchor="middle" fill="#b3261e" style={{ fontFamily: anton, fontSize: 140, letterSpacing: 18 }}>
            GERMANY
          </text>
        </g>
        <rect width={1920} height={1080} fill="url(#vinyet)" />
      </svg>
    </AbsoluteFill>
  );
};
