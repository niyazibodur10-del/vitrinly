import React from "react";
import { AbsoluteFill, Easing, interpolate, Sequence, useCurrentFrame, useVideoConfig } from "remotion";
import { Audio } from "@remotion/media";
import { AltyaziParca, Tam } from "./Tam";
import { DEk, DikeySahneComp, DIKEY_SAHNE } from "./dikey";
import { f, Kart, RENK } from "./kit";
import { Doku, fredoka } from "./ortak";
import { KURGU_SHORTS } from "./kurgu-veri";
import { SAHNELER } from "./veri-tam";

// F7 kurgu katmanı (kurgu-editoru). Animasyonun kendisine dokunmaz: K1929Tam'ı altyazısız sarar, kurgu vurgularını
// (snap punch-in, vaat şeridi) sahne katmanına uygular, altyazıyı ölçeksiz en üste koyar. Vurgu olmayan karelerde çıktı
// K1929Tam ile aynıdır (aynı katman sırası: sahneler → Doku → altyazı) → render-parca önbelleği yeniden kullanılabilir.

type Vurgu = { bas: number; son: number; s: number; ox: string; oy: string };
// Açılış varyantları (ilk 30 sn): A = animasyon olduğu gibi · B = A + vaat şeridi · C = B + 2 snap punch-in
export const VARYANT: Record<string, { vaat: boolean; vurgular: Vurgu[] }> = {
  A: { vaat: false, vurgular: [] },
  B: { vaat: true, vurgular: [] },
  C: {
    vaat: true,
    vurgular: [
      // 8.0: kapılar yandıktan sonra "By 1933…" — üst-sol sabit (köşe göstergesi korunur), kesme sahne sonunda (15.59) gizlenir
      { bas: 8.0, son: 15.591, s: 1.07, ox: "0%", oy: "0%" },
      // 20.3: takvim 1929→2026 çevrilirken ekrana doğru; S02'nin kendi punch-in'i (25.54) üstüne biner, sahne sonunda (34.83) biter
      { bas: 20.3, son: 34.832, s: 1.06, ox: "70%", oy: "25%" },
    ],
  },
};
export const KURGU_VARYANT = "B"; // kazanan (kurgu-rapor.md §1)

const SnapOlcek: React.FC<{ vurgular: Vurgu[]; children: React.ReactNode }> = ({ vurgular, children }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;
  const v = vurgular.find((x) => t >= x.bas && t < x.son);
  if (!v) return <>{children}</>;
  // 4 karelik hızlı oturma (snap), sahne kesmesinde biter → geri zoom görünmez
  const s = interpolate(t, [v.bas, v.bas + 4 / fps], [1, v.s], { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.out(Easing.cubic) });
  return <AbsoluteFill style={{ transform: `scale(${s})`, transformOrigin: `${v.ox} ${v.oy}` }}>{children}</AbsoluteFill>;
};

// Vaat şeridi: başlıktaki soru ("Can you keep it?") 8,0 sn'de köşe göstergesinin altında; S01 sonuna kadar
const VaatSeridi: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;
  if (t < 7.9 || t >= 15.591) return null;
  const p = interpolate(t, [7.9, 8.15], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.out(Easing.back(1.6)) });
  return (
    <div style={{ position: "absolute", left: 58, top: 178, opacity: Math.min(1, p * 1.4), scale: String(0.7 + 0.3 * p), transformOrigin: "0% 50%", fontFamily: "Anton", fontSize: 58, lineHeight: 1.05, color: "#ffffff", textShadow: "0 3px 0 #000, 0 0 14px rgba(0,0,0,0.8)", letterSpacing: 1 }}>
      CAN YOU
      <br />
      <span style={{ color: "#ffd23f" }}>KEEP IT?</span>
    </div>
  );
};

export const Final: React.FC<{ varyant?: string }> = ({ varyant = KURGU_VARYANT }) => {
  const v = VARYANT[varyant];
  return (
    <AbsoluteFill style={{ background: "#000" }}>
      <SnapOlcek vurgular={v.vurgular}>
        <Tam altyazi={false} />
      </SnapOlcek>
      {v.vaat ? <VaatSeridi /> : null}
      <AltyaziParca ofs={0} />
    </AbsoluteFill>
  );
};

// ---------------- Shorts (9:16) ----------------
const Etiket: React.FC<{ metin: string }> = ({ metin }) => (
  <div style={{ position: "absolute", left: 40, top: 205, padding: "5px 13px", borderRadius: 8, background: "rgba(0,0,0,0.45)", color: "rgba(255,255,255,0.85)", fontFamily: fredoka, fontWeight: 700, fontSize: 24 }}>{metin}</div>
);

// Uzun videoya köprü kartı (son 1,4–2,6 sn): güvenli alanda (y 1180–1420, x ≤ 900), alttaki "ilgili video" bağlantısını işaret eder
const KopruKarti: React.FC<{ ust: string; alt: string }> = ({ ust, alt }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;
  const p = interpolate(t, [0, 0.25], [0, 1], { extrapolateLeft: "clamp", extrapolateRight: "clamp", easing: Easing.out(Easing.back(1.4)) });
  const ok = Math.sin(t * Math.PI * 3) * 10;
  return (
    <AbsoluteFill>
      <div style={{ position: "absolute", left: 70, top: 1130, width: 740, padding: "26px 30px", borderRadius: 22, background: "#ffd23f", border: "6px solid #0b0b0b", boxShadow: "0 10px 0 #0b0b0b", textAlign: "center", opacity: p, scale: String(0.8 + 0.2 * p) }}>
        <div style={{ fontFamily: "Anton", fontSize: 58, color: "#0b0b0b", lineHeight: 1.05 }}>{ust}</div>
        <div style={{ fontFamily: fredoka, fontWeight: 700, fontSize: 38, color: "#0b0b0b", marginTop: 8 }}>{alt}</div>
      </div>
      <div style={{ position: "absolute", left: 418, top: 1390 + ok, fontFamily: "Anton", fontSize: 90, color: "#ffd23f", textShadow: "0 4px 0 #000", opacity: p }}>↓</div>
    </AbsoluteFill>
  );
};

const KOPRU: Record<string, { ust: string; alt: string }> = {
  sh1: { ust: "WHY IT FLIPS TODAY", alt: "Full game: $1,000 in 1929" },
  sh2: { ust: "WHO WON 1929?", alt: "Full game: $1,000 in 1929" },
};

export const KurguShorts: React.FC<{ ad: "sh1" | "sh2" }> = ({ ad }) => {
  const v = KURGU_SHORTS[ad];
  return (
    <AbsoluteFill style={{ background: "#000" }}>
      <Audio src={f(`${ad}-yatak.wav`)} />
      {v.parcalar.map((p, i) => (
        <Sequence key={i} from={p.yer} durationInFrames={p.sure} name={`${p.tur}-${p.kaynak}-${p.bas}`}>
          {p.tur === "kuyruk" ? (
            <Sequence from={-(p.kareBas - Math.round(SAHNE_BAS[p.kaynak] * 30))}>
              <SessizSahne id={p.kaynak} kareBas={p.kareBas - Math.round(SAHNE_BAS[p.kaynak] * 30)} sure={p.sure} />
            </Sequence>
          ) : p.tur === "ek" ? (
            <Sequence from={-p.kareBas}>
              {ad === "sh1" && p.kareBas === 0 ? (
                // Shorts 1 hook tek kadraj 3,96 sn → virgül duraklamasında (1,40 sn) snap punch-in; ilk görsel değişim ≤2 sn, kesmede biter
                <SnapOlcek vurgular={[{ bas: 1.4, son: 99, s: 1.05, ox: "42.6%", oy: "30%" }]}>
                  <DEk ek="sh1" />
                </SnapOlcek>
              ) : (
                <DEk ek={p.kaynak as "sh1" | "sh2"} />
              )}
            </Sequence>
          ) : (
            <Sequence from={-(p.kareBas - Math.round(SAHNE_BAS[p.kaynak] * 30))}>
              <DikeySahneComp id={p.kaynak} />
            </Sequence>
          )}
          {/* S06 dikey: C16 borsa plakası (bulanık) — politika notu: plaka görünen her karede "Illustration" */}
          {p.kaynak === "S06" ? <Etiket metin="Illustration" /> : null}
          {/* S16 kesiti "decade." (441.0) öncesinde biter → niteleyici şerit BOX satırıyla (434.31) birlikte kurgu katmanında gelir (politika B1) */}
          {p.kaynak === "S16" ? (
            <Sequence from={-(p.kareBas - Math.round(SAHNE_BAS.S16 * 30))}>
              <Kart an={434.31 - SAHNE_BAS.S16} x={60} y={1210} w={860} h={100} arka={RENK.sari} cerceve="#101010">
                <div style={{ height: "100%", display: "flex", alignItems: "center", justifyContent: "center", fontFamily: "Anton", fontSize: 46, color: "#101010", letterSpacing: 2 }}>IN A DECADE OF FALLING PRICES</div>
              </Kart>
            </Sequence>
          ) : null}
        </Sequence>
      ))}
      <Sequence from={v.kopruBas}>
        <KopruKarti {...KOPRU[ad]} />
      </Sequence>
    </AbsoluteFill>
  );
};

// Köprü kuyruğu: sahne görüntüsü sürer, anlatım ve altyazı yok
// (S21 sonu durağan → ilk render'da freezedetect 53,6 sn'de donma buldu; kuyrukta yavaş itme ile hareket korunur)
const SessizSahne: React.FC<{ id: string; kareBas: number; sure: number }> = ({ id, kareBas, sure }) => {
  const B = DIKEY_SAHNE[id];
  const frame = useCurrentFrame();
  const s = interpolate(frame, [kareBas, kareBas + sure], [1, 1.08], { extrapolateLeft: "clamp", extrapolateRight: "clamp" });
  return (
    <AbsoluteFill style={{ background: "#000" }}>
      <AbsoluteFill style={{ transform: `scale(${s})`, transformOrigin: "50% 35%" }}>
        <B />
      </AbsoluteFill>
      <Doku />
    </AbsoluteFill>
  );
};

const SAHNE_BAS: Record<string, number> = Object.fromEntries(SAHNELER.map((s) => [s.id, s.bas]));
