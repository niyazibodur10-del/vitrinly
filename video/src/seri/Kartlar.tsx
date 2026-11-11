import React from "react";
import { Easing, Img, interpolate, spring, staticFile, useCurrentFrame, useVideoConfig } from "remotion";
import { ALTIN, anton, BANT, fredoka, GUVENLI, GUVENLI_W, RENK, ZEMIN_KART } from "./sabitler";
import { Ikon } from "./Ikonlar";
import type { KararKarti, KazananYorum } from "./tipler";

// Dizinin kart katmanları: geçici logo, açılış damgası (≤2 sn), kazanan yorum kartı (3–5 sn), karar kartı (5–8 sn).
// Hepsi BANT.kart (y 400–1110) içinde, güvenli alanın yatay sınırlarında (x 60–890). Sesler Bolum.tsx'te yerleşir.

const CL = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;

/** Geçici logo: Jake mavisi / Mike kırmızısı iki yarım para + oy işareti (✓). Gerçek logo gelince Bolum.logo ile değişir. */
export const GeciciLogo: React.FC<{ boyut: number; logo?: string }> = ({ boyut, logo }) => {
  if (logo) return <Img src={staticFile(logo)} style={{ width: boyut, height: boyut, objectFit: "cover", borderRadius: "50%" }} />;
  return (
    <svg width={boyut} height={boyut} viewBox="0 0 100 100">
      <defs>
        <clipPath id="fbv-daire"><circle cx="50" cy="50" r="44" /></clipPath>
      </defs>
      <circle cx="50" cy="50" r="48" fill={ALTIN} />
      <g clipPath="url(#fbv-daire)">
        <polygon points="0,0 100,0 0,100" fill={RENK.jake.ana} />
        <polygon points="100,0 100,100 0,100" fill={RENK.mike.ana} />
      </g>
      <path d="M27,52 L43,68 L74,34" fill="none" stroke="#ffffff" strokeWidth="11" strokeLinecap="round" strokeLinejoin="round" />
    </svg>
  );
};

/** Açılış damgası: "FLIP BY VOTE · EP. N" + logo. Varsayılan 1,8 sn (≤2 sn kuralı). */
export const AcilisDamgasi: React.FC<{ no: number; sure?: number; logo?: string; ust?: number; olcek?: number; sag?: boolean }> = ({ no, sure = 1.8, logo, ust = BANT.kart.ust + 40, olcek = 1, sag = false }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;
  if (t > sure) return null;
  const gir = spring({ frame, fps, config: { damping: 13, stiffness: 170, mass: 0.7 } });
  const cik = interpolate(t, [sure - 0.3, sure], [0, 1], { ...CL, easing: Easing.in(Easing.cubic) });
  const ep = interpolate(t, [0.25, 0.5], [0, 1], { ...CL, easing: Easing.out(Easing.back(2)) });
  return (
    <div
      style={{
        position: "absolute", left: GUVENLI.sol, width: GUVENLI_W, top: ust,
        display: "flex", justifyContent: sag ? "flex-end" : "center", opacity: 1 - cik,
        transformOrigin: sag ? "100% 0" : "50% 0",
        transform: `translateY(${-cik * 40}px) scale(${(0.6 + 0.4 * gir) * olcek})`,
      }}
    >
      <div style={{ display: "flex", alignItems: "center", gap: 22, padding: "20px 34px", borderRadius: 30, background: ZEMIN_KART, border: `3px solid ${ALTIN}`, boxShadow: "0 12px 30px rgba(0,0,0,0.5)" }}>
        <div style={{ rotate: `${(1 - gir) * -180}deg` }}>
          <GeciciLogo boyut={110} logo={logo} />
        </div>
        <div style={{ display: "flex", flexDirection: "column" }}>
          <div style={{ fontFamily: anton, fontSize: 74, lineHeight: 1, letterSpacing: 2, color: "#fff" }}>FLIP BY VOTE</div>
          <div style={{ fontFamily: anton, fontSize: 46, lineHeight: 1.15, letterSpacing: 4, color: ALTIN, opacity: ep, transform: `translateX(${(1 - ep) * -30}px)` }}>
            · EP. {no}
          </div>
        </div>
      </div>
    </div>
  );
};

const kisalt = (n: number) => (n >= 1e6 ? `${(n / 1e6).toFixed(1).replace(/\.0$/, "")}M` : n >= 1e4 ? `${(n / 1e3).toFixed(1).replace(/\.0$/, "")}K` : n.toLocaleString("en-US"));

/** Kazanan yorum kartı: "@kullanici decided:" + yorum + (ops.) beğeni. Bölüm başında 3–5 sn. */
export const KazananYorumKarti: React.FC<{ y: KazananYorum }> = ({ y }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;
  const sure = y.sure ?? 4;
  if (t > sure) return null;
  const gir = spring({ frame, fps, config: { damping: 15, stiffness: 150, mass: 0.8 } });
  const cik = interpolate(t, [sure - 0.3, sure], [0, 1], { ...CL, easing: Easing.in(Easing.cubic) });
  const kalp = interpolate(t, [0.5, 0.65, 0.8], [1, 1.35, 1], CL);
  const ad = y.kullanici.replace(/^@/, "");
  return (
    <div
      style={{
        position: "absolute", left: GUVENLI.sol, width: GUVENLI_W, top: BANT.kart.ust + 40,
        transform: `translateX(${(1 - gir) * -GUVENLI_W - cik * GUVENLI_W}px)`,
      }}
    >
      <div style={{ padding: "26px 30px", borderRadius: 30, background: "rgba(255,255,255,0.97)", boxShadow: `0 0 0 5px ${ALTIN}, 0 14px 34px rgba(0,0,0,0.5)` }}>
        <div style={{ display: "flex", alignItems: "center", gap: 18 }}>
          <div style={{ width: 74, height: 74, borderRadius: 37, background: `linear-gradient(135deg, ${RENK.jake.ana}, ${RENK.mike.ana})`, display: "flex", alignItems: "center", justifyContent: "center", fontFamily: fredoka, fontWeight: 700, fontSize: 40, color: "#fff" }}>
            {ad.slice(0, 1).toUpperCase()}
          </div>
          <div style={{ fontFamily: fredoka, fontWeight: 700, fontSize: 40, color: "#111827", overflow: "hidden", textOverflow: "ellipsis", whiteSpace: "nowrap", maxWidth: 560 }}>
            @{ad} <span style={{ color: "#6b7280" }}>decided:</span>
          </div>
        </div>
        <div style={{ fontFamily: fredoka, fontWeight: 700, fontSize: 50, lineHeight: 1.18, color: "#111827", marginTop: 16 }}>“{y.metin}”</div>
        {y.begeni !== undefined ? (
          <div style={{ display: "flex", alignItems: "center", gap: 10, marginTop: 14, fontFamily: fredoka, fontWeight: 700, fontSize: 36, color: "#e11d48" }}>
            <span style={{ display: "inline-block", scale: String(kalp) }}>♥</span>
            {kisalt(y.begeni)}
          </div>
        ) : null}
      </div>
    </div>
  );
};

const SECENEK_RENK = [RENK.jake.ana, RENK.mike.ana, ALTIN];

/** Karar kartı: soru + 2–3 seçenek (isim + fiyat; harf/numara YOK — incil §5.1) + "Tell us in the comments 👇"
 *  + "Ep. N: YOUR call" (gün sözü yok — incil §5.7). `k.kapanis` verilirse kart o ana kadar kart bandının altına yaslı
 *  durur (üstte konuşan yüzler görünür), kapanışta altyazı bandına iner ve "Ep. N: YOUR call" damgası belirir. */
export const KararKartiKatman: React.FC<{ k: KararKarti; sonrakiNo: number; bas: number }> = ({ k, sonrakiNo, bas }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;
  const kapanis = k.kapanis !== undefined ? k.kapanis - bas : 0;
  const kart = spring({ frame, fps, config: { damping: 16, stiffness: 140, mass: 0.9 } });
  const sec = (i: number) => spring({ frame: frame - Math.round((0.35 + i * 0.18) * fps), fps, config: { damping: 14, stiffness: 160 } });
  const cagri = spring({ frame: frame - Math.round((0.35 + k.secenekler.length * 0.18 + 0.15) * fps), fps, config: { damping: 12, stiffness: 150 } });
  const ep = spring({ frame: frame - Math.round(kapanis * fps), fps, config: { damping: 10, stiffness: 190, mass: 0.7 } });
  const in_ = k.kapanis !== undefined ? spring({ frame: frame - Math.round(kapanis * fps), fps, config: { damping: 18, stiffness: 120 } }) : 1;
  const karart = interpolate(t, [0, 0.3], [0, 0.35], CL) + 0.2 * in_;
  const ok = Math.sin(t * 6) * 6 * cagri;
  const cik = interpolate(t, [(k.sure ?? 7) - 0.25, k.sure ?? 7], [0, 1], { ...CL, easing: Easing.in(Easing.cubic) });
  // alt kenar: kart bandı (1110) → altyazı bandı (1420)
  const ust0 = k.kapanis !== undefined ? BANT.altyazi.ust - 10 : BANT.kart.alt;
  const alt = 1920 - (ust0 + (BANT.altyazi.alt - ust0) * in_);
  return (
    <>
      <div style={{ position: "absolute", inset: 0, background: `linear-gradient(to bottom, rgba(5,8,14,${karart * 0.3}) 0%, rgba(5,8,14,${karart}) 55%)`, opacity: 1 - cik }} />
      <div
        style={{
          position: "absolute", left: GUVENLI.sol, width: GUVENLI_W, bottom: alt,
          transform: `scale(${(0.85 + 0.15 * kart) * (1 - 0.1 * cik)})`, transformOrigin: "50% 100%", opacity: Math.min(1, kart * 1.5) * (1 - cik),
        }}
      >
        <div style={{ padding: "22px 28px 20px", borderRadius: 36, background: ZEMIN_KART, border: `4px solid ${ALTIN}`, boxShadow: "0 18px 44px rgba(0,0,0,0.6)" }}>
          <div style={{ fontFamily: anton, fontSize: 30, letterSpacing: 5, color: ALTIN }}>YOU DECIDE</div>
          <div style={{ fontFamily: fredoka, fontWeight: 700, fontSize: 50, lineHeight: 1.08, color: "#fff", marginTop: 4 }}>{k.soru}</div>
          <div style={{ display: "flex", flexDirection: "column", gap: 10, marginTop: 14 }}>
            {k.secenekler.map((s, i) => {
              const p = sec(i);
              const ikon = k.ikonlar?.[i];
              return (
                <div key={i} style={{ display: "flex", alignItems: "center", gap: 18, padding: "6px 14px", borderRadius: 20, background: "rgba(255,255,255,0.08)", borderLeft: `8px solid ${SECENEK_RENK[i]}`, opacity: Math.min(1, p * 1.4), transform: `translateX(${(1 - p) * 60}px)` }}>
                  {ikon ? <Ikon ad={ikon} boyut={56} hale={false} /> : null}
                  <div style={{ fontFamily: fredoka, fontWeight: 700, fontSize: 40, lineHeight: 1.1, color: "#fff" }}>{s}</div>
                </div>
              );
            })}
          </div>
          <div style={{ marginTop: 14, textAlign: "center", opacity: Math.min(1, cagri * 1.4), transform: `scale(${0.8 + 0.2 * cagri})` }}>
            <div style={{ fontFamily: fredoka, fontWeight: 700, fontSize: 46, color: "#fff" }}>
              Tell us in the comments <span style={{ display: "inline-block", transform: `translateY(${ok}px)` }}>👇</span>
            </div>
          </div>
          {t >= kapanis ? (
            <div style={{ marginTop: 10, textAlign: "center", transform: `scale(${0.5 + 0.5 * ep})`, opacity: Math.min(1, ep * 1.5) }}>
              <span style={{ display: "inline-block", padding: "6px 26px", borderRadius: 18, background: ALTIN, fontFamily: anton, fontSize: 52, letterSpacing: 2, color: "#14110a" }}>
                Ep. {sonrakiNo}: YOUR call
              </span>
            </div>
          ) : null}
        </div>
      </div>
    </>
  );
};
