import React from "react";
import { Audio } from "@remotion/media";
import { Easing, interpolate, Sequence, staticFile, useCurrentFrame, useVideoConfig } from "remotion";
import { anton, BANT, GUVENLI, SFX } from "./sabitler";
import type { BankOlayi } from "./tipler";

// "BANK: $100" sayacı (sol üst, güvenli alan içinde). Değer değişince: 0,9 sn sayma (easeOut), hap sekmesi,
// artışta yeşil / düşüşte kırmızı parlama, yükselen "+$85" etiketi ve efekt sesi (artış ka-ching, düşüş bozuk para).
// Sesler olay karesine kare-doğru yerleşir (Sequence from = round(t*fps)).

const CL = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;
const SAY = 0.9;
export const para = (v: number) => "$" + Math.round(v).toLocaleString("en-US");

export const BankSayaci: React.FC<{ baslangic: number; olaylar: BankOlayi[]; sesAcik: boolean }> = ({ baslangic, olaylar, sesAcik }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;
  const sirali = [...olaylar].sort((a, b) => a.t - b.t);

  let onceki = baslangic, deger = baslangic;
  let son: BankOlayi | null = null, sonOnceki = baslangic;
  for (const e of sirali) {
    if (e.t <= t) {
      sonOnceki = onceki; son = e; onceki = e.deger;
    }
  }
  if (son) {
    const p = interpolate(t - son.t, [0, SAY], [0, 1], { ...CL, easing: Easing.out(Easing.cubic) });
    deger = sonOnceki + (son.deger - sonOnceki) * p;
  }
  const dt = son ? t - son.t : 99;
  const artis = son ? son.deger >= sonOnceki : true;
  const vurgu = interpolate(dt, [0, 0.12, SAY + 0.5], [0, 1, 0], CL);
  const pop = interpolate(dt, [0, 0.1, 0.25, 0.4], [1, 1.16, 0.97, 1], CL);
  const fark = son ? son.deger - sonOnceki : 0;
  // aynı değer olayı = yalnız "pop" (giriş vurgusu, altın), etiket yok
  const renk = fark === 0 ? "255,201,60" : artis ? "61,220,132" : "255,77,77";
  const etiket = interpolate(dt, [0, 0.15, 1.2, 1.6], [0, 1, 1, 0], CL);

  return (
    <>
      <div
        style={{
          position: "absolute", left: GUVENLI.sol, top: BANT.bank.ust, transformOrigin: "0 50%", scale: String(pop),
          display: "flex", alignItems: "baseline", gap: 14, padding: "10px 26px 12px", borderRadius: 22,
          background: "rgba(10,14,22,0.88)", border: `3px solid rgba(${renk},${0.25 + 0.75 * vurgu})`,
          boxShadow: `0 6px 18px rgba(0,0,0,0.45), 0 0 ${28 * vurgu}px rgba(${renk},${0.8 * vurgu})`,
        }}
      >
        <span style={{ fontFamily: anton, fontSize: 38, letterSpacing: 3, color: "#FFC93C" }}>BANK:</span>
        <span style={{ fontFamily: anton, fontSize: 60, letterSpacing: 1, color: vurgu > 0.05 ? `rgb(${renk})` : "#ffffff", fontVariantNumeric: "tabular-nums" }}>
          {para(deger)}
        </span>
      </div>
      {son && etiket > 0 && fark !== 0 ? (
        <div
          style={{
            position: "absolute", left: GUVENLI.sol + 24, top: BANT.bank.ust + 96 - 30 * Math.min(1, dt / 1.2), opacity: etiket,
            fontFamily: anton, fontSize: 46, color: `rgb(${renk})`, WebkitTextStroke: "8px #0b0d12", paintOrder: "stroke fill",
          }}
        >
          {(fark >= 0 ? "+" : "−") + para(Math.abs(fark))}
        </div>
      ) : null}
      {sesAcik
        ? sirali.map((e, i) => {
            const prev = i ? sirali[i - 1].deger : baslangic;
            const dosya = e.ses === false ? null : e.ses ?? (e.deger >= prev ? SFX.bankArti : SFX.bankEksi);
            return dosya ? (
              <Sequence key={i} from={Math.round(e.t * fps)} layout="none">
                <Audio src={staticFile(dosya)} volume={0.8} />
              </Sequence>
            ) : null;
          })
        : null}
    </>
  );
};
