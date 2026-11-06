import React from "react";
import { Easing, Img, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig } from "remotion";
import { loadFont } from "@remotion/fonts";

// Ortak "Abone ol" animasyonu (kurgu-editoru, Niyazi kararı 2026-10-28 — her videoda; CLAUDE.md).
// Kanal kartı (profil resmi + "Toonomy" + @toonomy) kayarak girer → fare imleci gelip kırmızı SUBSCRIBE düğmesine tıklar
// (tıklama karesinde düğme griye "SUBSCRIBED" döner, basılma + dalga, zil sallanır) → kart çıkar.
// Kullanım: <Sequence from={kare(bas)} durationInFrames={kare(sure)}><AboneOl duzen="yatay" taraf="sol" /></Sequence>
// Ses: bileşen sessizdir; klik sesi (assets/efekt/ozgun-fare-klik.flac) miks betiğinde bas + klik saniyesine konur
// (bileşen sesi taşırsa render-parca --ses yolu bozulur). Varsayılan klik = ABONE_KLIK_SN.
// Yerleşim: yatay (1920x1080) alt üçte bir, y 682–810 → iki satırlık altyazının (üst ≈ 830) üstünde; sol/sağ 56 px.
//           dikey (1080x1920) ×1,2, x 70–876, y 1150–1304 → Shorts güvenli alanı (sağ ≤ 918) ve altyazı (üst ≈ 1340) dışında.
export const ABONE_SURE_SN = 3.5;
export const ABONE_KLIK_SN = 1.3;

loadFont({ family: "Fredoka", url: staticFile("fonts/Fredoka-700.woff2"), weight: "700" });

const W = 672, H = 128;
const BTN = { x: 342, y: 31, w: 250, h: 66 };
const BTN_MERKEZ = { x: BTN.x + BTN.w * 0.55, y: BTN.y + BTN.h * 0.6 };
const CL = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;

const Imlec: React.FC<{ basili: number }> = ({ basili }) => (
  <svg width={46} height={58} viewBox="0 0 46 58" style={{ scale: String(1 - 0.18 * basili), transformOrigin: "4px 4px", filter: "drop-shadow(0 3px 3px rgba(0,0,0,0.55))" }}>
    <path d="M4,4 L4,46 L15,36 L23,54 L31,50 L23,33 L38,33 Z" fill="#ffffff" stroke="#0b0b0b" strokeWidth={3.5} strokeLinejoin="round" />
  </svg>
);

const Zil: React.FC<{ aci: number }> = ({ aci }) => (
  <svg width={50} height={50} viewBox="0 0 50 50" style={{ rotate: `${aci}deg`, transformOrigin: "25px 6px" }}>
    <path d="M25,6 C16,6 12,13 12,22 L12,31 L7,37 L43,37 L38,31 L38,22 C38,13 34,6 25,6 Z" fill="#f1f1f1" stroke="#0b0b0b" strokeWidth={2.5} />
    <circle cx={25} cy={42} r={4.5} fill="#f1f1f1" stroke="#0b0b0b" strokeWidth={2.5} />
  </svg>
);

export const AboneOl: React.FC<{
  duzen?: "yatay" | "dikey";
  taraf?: "sol" | "sag";
  sure?: number; // sn (kart görünür süre)
  klik?: number; // sn (tıklama anı, Sequence başına göre)
  ad?: string;
  tutamac?: string;
  resim?: string; // public/ altındaki yol
  ust?: number; // kartın üst kenarı (px) — varsayılan yerleşimi sahne içeriğine göre kaydırmak için
}> = ({ ust: ustVerilen, duzen = "yatay", taraf = "sol", sure = ABONE_SURE_SN, klik = ABONE_KLIK_SN, ad = "Toonomy", tutamac = "@toonomy", resim = "ortak/toonomy-profil.png" }) => {
  const frame = useCurrentFrame();
  const { fps, width } = useVideoConfig();
  const t = frame / fps;
  if (t < 0 || t > sure) return null;

  const olcek = duzen === "dikey" ? 1.2 : 1;
  const sol = duzen === "dikey" ? 70 : taraf === "sol" ? 56 : width - 56 - W;
  const ust = ustVerilen ?? (duzen === "dikey" ? 1150 : 682);
  const yon = taraf === "sol" || duzen === "dikey" ? -1 : 1;

  // giriş (yaylı kayma) / çıkış (hızlanan kayma)
  const gir = spring({ frame, fps, config: { damping: 15, stiffness: 140, mass: 0.8 } });
  const cik = interpolate(t, [sure - 0.38, sure], [0, 1], { ...CL, easing: Easing.in(Easing.cubic) });
  const kay = (1 - gir) * (W + 120) * yon + cik * (W + 120) * yon;
  const opak = Math.min(1, gir * 1.6) * (1 - cik);

  // imleç: kart oturunca sağ alttan gelir, klikte basılır, sonra hafifçe çekilip söner
  const imlecP = interpolate(t, [0.45, klik - 0.1], [0, 1], { ...CL, easing: Easing.inOut(Easing.cubic) });
  const imlecGor = interpolate(t, [0.4, 0.55, klik + 0.55, klik + 0.85], [0, 1, 1, 0], CL);
  const geri = interpolate(t, [klik + 0.25, klik + 0.85], [0, 1], { ...CL, easing: Easing.out(Easing.quad) });
  const ix = interpolate(imlecP, [0, 1], [BTN_MERKEZ.x + 210, BTN_MERKEZ.x]) + geri * 40;
  const iy = interpolate(imlecP, [0, 1], [BTN_MERKEZ.y + 150, BTN_MERKEZ.y]) + geri * 30;
  const basili = interpolate(t, [klik - 0.04, klik, klik + 0.1], [0, 1, 0], CL);

  // düğme: basılma (0,9) → hafif sekme → 1; renk tıklama karesinde döner
  const abone = t >= klik;
  const dugme = interpolate(t, [klik - 0.03, klik + 0.05, klik + 0.17, klik + 0.28], [1, 0.9, 1.05, 1], CL);
  const dalga = interpolate(t, [klik, klik + 0.4], [0, 1], CL);
  const zilGor = interpolate(t, [klik + 0.12, klik + 0.3], [0, 1], { ...CL, easing: Easing.out(Easing.back(2)) });
  const zilAci = t > klik + 0.2 ? Math.sin((t - klik - 0.2) * 26) * 18 * interpolate(t, [klik + 0.2, klik + 1.1], [1, 0], CL) : 0;

  return (
    <div style={{ position: "absolute", left: sol, top: ust, width: W, height: H, scale: String(olcek), transformOrigin: "0 0", translate: `${kay}px 0px`, opacity: opak, pointerEvents: "none" }}>
      <div style={{ position: "absolute", inset: 0, borderRadius: 64, background: "rgba(14,16,24,0.9)", border: "3px solid rgba(255,255,255,0.16)", boxShadow: "0 10px 26px rgba(0,0,0,0.55)" }} />
      <div style={{ position: "absolute", left: 16, top: 16, width: 96, height: 96, borderRadius: 48, overflow: "hidden", boxShadow: "0 0 0 4px #ffffff" }}>
        <Img src={staticFile(resim)} style={{ width: 96, height: 96 }} />
      </div>
      <div style={{ position: "absolute", left: 132, top: 22, width: 200, fontFamily: "Fredoka", fontWeight: 700 }}>
        <div style={{ fontSize: 42, lineHeight: 1.1, color: "#ffffff" }}>{ad}</div>
        <div style={{ fontSize: 24, color: "#aeb6c4", marginTop: 4 }}>{tutamac}</div>
      </div>
      <div
        style={{
          position: "absolute", left: BTN.x, top: BTN.y, width: BTN.w, height: BTN.h, borderRadius: BTN.h / 2, scale: String(dugme),
          background: abone ? "#3a3a3d" : "#e3202a", boxShadow: abone ? "none" : "0 4px 0 #8e0f15",
          display: "flex", alignItems: "center", justifyContent: "center", gap: 8,
          fontFamily: "Fredoka", fontWeight: 700, fontSize: abone ? 28 : 31, letterSpacing: 1, color: abone ? "#e4e4e4" : "#ffffff", overflow: "hidden",
        }}
      >
        {abone ? "✓ SUBSCRIBED" : "SUBSCRIBE"}
        {dalga > 0 && dalga < 1 ? (
          <div style={{ position: "absolute", left: BTN_MERKEZ.x - BTN.x - 90 * dalga, top: BTN_MERKEZ.y - BTN.y - 90 * dalga, width: 180 * dalga, height: 180 * dalga, borderRadius: "50%", background: `rgba(255,255,255,${0.45 * (1 - dalga)})` }} />
        ) : null}
      </div>
      <div style={{ position: "absolute", left: 604, top: 38, opacity: zilGor, scale: String(0.5 + 0.5 * zilGor) }}>
        <Zil aci={zilAci} />
      </div>
      {imlecGor > 0 ? (
        <div style={{ position: "absolute", left: ix - 4, top: iy - 4, opacity: imlecGor }}>
          <Imlec basili={basili} />
        </div>
      ) : null}
    </div>
  );
};
