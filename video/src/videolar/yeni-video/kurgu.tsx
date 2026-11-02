import React from "react";
import { AbsoluteFill, Composition, Easing, interpolate, Sequence, useCurrentFrame, useVideoConfig } from "remotion";
import { Audio } from "@remotion/media";
import { AltyaziParca, kare, Tam, TAM_KARE } from "./Tam";
import { DEk, DikeySahneComp } from "./dikey";
import { f } from "./kit";
import { anton, fredoka } from "./ortak";
import { ABONE_ANA, KURGU_SHORTS } from "./kurgu-veri";
import { AboneOl } from "../../ortak/AboneOl";
import { SAHNELER } from "./veri-sahne";

// F7 kurgu katmanı (kurgu-editoru) — S08 Kitchen Table Budget. Kaynak desen: video/src/k1929/kurgu.tsx.
// Animasyona dokunmaz: KButceTam'ı altyazısız sarar → kurgu vurguları (vaat şeridi, başlık yankısı) + abone → altyazı en üstte.
// Vurgu olmayan karelerde çıktı KButceTam ile piksel-aynı (aynı katman sırası) → render-parca önbelleği (--kaynak KButceTam).

const CL = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;

// Açılış varyantları (ilk 30 sn): A = animasyon olduğu gibi · B = A + vaat şeridi · C = B + başlık yankısı (Capitol planında)
export const VARYANT: Record<string, { vaat: boolean; baslik: boolean }> = {
  A: { vaat: false, baslik: false },
  B: { vaat: true, baslik: false },
  C: { vaat: true, baslik: true },
};
export const KURGU_VARYANT = "B"; // kazanan (kurgu-rapor.md §1)

const Serit: React.FC<{ bas: number; son: number; x: number; y: number; hiza?: "left" | "right"; children: React.ReactNode }> = ({ bas, son, x, y, hiza = "left", children }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;
  if (t < bas || t >= son) return null;
  const p = interpolate(t, [bas, bas + 0.25], [0, 1], { ...CL, easing: Easing.out(Easing.back(1.6)) });
  return (
    <div style={{ position: "absolute", [hiza]: x, top: y, textAlign: hiza, opacity: Math.min(1, p * 1.4), scale: String(0.7 + 0.3 * p), transformOrigin: hiza === "left" ? "0% 50%" : "100% 50%", fontFamily: anton, fontSize: 64, lineHeight: 1.05, color: "#ffffff", textShadow: "0 3px 0 #000, 0 0 16px rgba(0,0,0,0.85)", letterSpacing: 1 }}>
      {children}
    </div>
  );
};

// B: vaat (videonun sözü: açığın nereye gittiği) — −$2,000 notu yandıktan sonra, Leo'ya punch-in planında (9,32–13,06), pencere üstü sol
const VaatSeridi: React.FC = () => (
  <Serit bas={9.4} son={13.06} x={70} y={110}>
    WHERE DOES THE
    <br />
    <span style={{ color: "#ff5a4f" }}>−$2,000</span> A MONTH GO?
  </Serit>
);
// C ek: başlık yankısı (tıklanan vaat) — Capitol planında sağ üst (0,2–1,9; 1,9'da kesme)
const BaslikYankisi: React.FC = () => (
  <Serit bas={0.2} son={1.9} x={90} y={130} hiza="right">
    IF AMERICA EARNED
    <br />
    <span style={{ color: "#ffd43b" }}>$5,400 A MONTH…</span>
  </Serit>
);

// ↺14 (524,7 "And time is what the three possibilities are about"): animasyonda Leo yakın planı 521,09–527,85 olaysız
// → kurgu vurgusu: pencere üstü solda kısa şerit, sonraki kesmede (A·B·C notları 527,85/529,08) biter
const Kanca14: React.FC = () => (
  <Serit bas={524.62} son={527.85} x={70} y={110}>
    TIME = <span style={{ color: "#ffd43b" }}>A · B · C</span>
  </Serit>
);

// S05 G1 grafiği 101,7–112,06 arası durağan (kadans: 11,25 sn boşluk) → kurgu vurgusu, yeni rakam yok:
// 106,62 "Three envelopes" → üç dolu çubuğun üstünde köşeli parantez + "3 ENVELOPES"; 109,10 "three thousand seven hundred" → $3,765 çerçevesi
const S05Vurgu: React.FC = () => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;
  if (t < 106.62 || t >= 112.06) return null;
  const p = interpolate(t, [106.62, 106.9], [0, 1], { ...CL, easing: Easing.out(Easing.cubic) });
  const q = interpolate(t, [109.1, 109.35], [0, 1], { ...CL, easing: Easing.out(Easing.back(1.8)) });
  const sari = "#ffd43b";
  return (
    <AbsoluteFill>
      <div style={{ position: "absolute", left: 232, top: 262, width: 984 * p, height: 14, borderTop: `6px solid ${sari}`, borderLeft: `6px solid ${sari}`, borderRight: p > 0.98 ? `6px solid ${sari}` : undefined, filter: "drop-shadow(0 2px 0 #000)" }} />
      <div style={{ position: "absolute", right: 1920 - 1216, top: 200, opacity: p, fontFamily: anton, fontSize: 48, color: sari, textShadow: "0 3px 0 #000" }}>3 ENVELOPES</div>
      {t >= 109.1 ? <div style={{ position: "absolute", left: 212, top: 570, width: 660, height: 140, border: `7px solid ${sari}`, borderRadius: 18, opacity: Math.min(1, q * 1.4), scale: String(0.85 + 0.15 * q), boxShadow: "0 0 24px rgba(255,212,59,0.45)" }} /> : null}
    </AbsoluteFill>
  );
};

export const Final: React.FC<{ varyant?: string }> = ({ varyant = KURGU_VARYANT }) => {
  const v = VARYANT[varyant];
  return (
    <AbsoluteFill style={{ background: "#000" }}>
      <Tam altyazi={false} />
      {v.baslik ? <BaslikYankisi /> : null}
      {v.vaat ? <VaatSeridi /> : null}
      <Kanca14 />
      <S05Vurgu />
      {ABONE_ANA.map((a) => (
        <Sequence key={a.kare} from={a.kare} durationInFrames={a.sure} name={`AboneOl-${a.kare}`} layout="none">
          <AboneOl duzen="yatay" taraf={a.taraf} sure={a.sure / 30} ust={a.ust ?? undefined} />
        </Sequence>
      ))}
      <AltyaziParca ofs={0} />
    </AbsoluteFill>
  );
};

// ---------------- Shorts (9:16) ----------------
// Uzun videoya köprü kartı (son ~1–2,5 sn): güvenli alanda (x 70–810, y 960–1130; ok ≤1300 → altyazı ≈1340 üstü; ilk render'da ok altyazıya biniyordu), alttaki "ilgili video" bağlantısını işaret eder
const KopruKarti: React.FC<{ ust: string; alt: string }> = ({ ust, alt }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;
  const p = interpolate(t, [0, 0.25], [0, 1], { ...CL, easing: Easing.out(Easing.back(1.4)) });
  const ok = Math.sin(t * Math.PI * 3) * 10;
  return (
    <AbsoluteFill>
      <div style={{ position: "absolute", left: 70, top: 960, width: 740, padding: "24px 30px", borderRadius: 22, background: "#ffd43b", border: "6px solid #0b0b0b", boxShadow: "0 10px 0 #0b0b0b", textAlign: "center", opacity: p, scale: String(0.8 + 0.2 * p) }}>
        <div style={{ fontFamily: anton, fontSize: 56, color: "#0b0b0b", lineHeight: 1.05 }}>{ust}</div>
        <div style={{ fontFamily: fredoka, fontWeight: 700, fontSize: 36, color: "#0b0b0b", marginTop: 8 }}>{alt}</div>
      </div>
      <div style={{ position: "absolute", left: 418, top: 1190 + ok, fontFamily: anton, fontSize: 90, color: "#ffd43b", textShadow: "0 4px 0 #000", opacity: p }}>↓</div>
    </AbsoluteFill>
  );
};

const KOPRU: Record<string, { ust: string; alt: string }> = {
  sh1: { ust: "ALL FIVE ENVELOPES", alt: "Full video: America's $5,400 budget" },
  sh2: { ust: "WHERE IT STANDS TODAY", alt: "Full video: America's $5,400 budget" },
};

const SAHNE_BAS: Record<string, number> = Object.fromEntries(SAHNELER.map((s) => [s.id, s.bas]));

export const KurguShorts: React.FC<{ ad: "sh1" | "sh2" }> = ({ ad }) => {
  const v = KURGU_SHORTS[ad];
  return (
    <AbsoluteFill style={{ background: "#000" }}>
      <Audio src={f(`${ad}-yatak.wav`)} />
      {v.parcalar.map((p, i) => (
        <Sequence key={i} from={p.yer} durationInFrames={p.sure} name={`${p.tur}-${p.kaynak}-${p.bas}`}>
          {p.tur === "ek" ? (
            <Sequence from={-p.kareBas}>
              <DEk ek={p.kaynak as "sh1" | "sh2"} />
            </Sequence>
          ) : (
            <Sequence from={-(p.kareBas - kare(SAHNE_BAS[p.kaynak]))}>
              <DikeySahneComp id={p.kaynak} />
            </Sequence>
          )}
        </Sequence>
      ))}
      <Sequence from={v.abone.kare} durationInFrames={v.abone.sure} name="AboneOl" layout="none">
        <AboneOl duzen="dikey" sure={v.abone.sure / 30} ust={v.abone.ust ?? undefined} />
      </Sequence>
      <Sequence from={v.kopruBas} name="Kopru">
        <KopruKarti {...KOPRU[ad]} />
      </Sequence>
    </AbsoluteFill>
  );
};

export const KButceKurgu: React.FC = () => (
  <>
    <Composition id="KButceFinal" component={Final} durationInFrames={TAM_KARE} fps={30} width={1920} height={1080} />
    {(["A", "B", "C"] as const).map((v) => (
      <Composition key={v} id={`KButceIlk30-${v}`} component={Final} defaultProps={{ varyant: v }} durationInFrames={900} fps={30} width={1920} height={1080} />
    ))}
    <Composition id="KButceShorts1" component={KurguShorts} defaultProps={{ ad: "sh1" as const }} durationInFrames={KURGU_SHORTS.sh1.toplam} fps={30} width={1080} height={1920} />
    <Composition id="KButceShorts2" component={KurguShorts} defaultProps={{ ad: "sh2" as const }} durationInFrames={KURGU_SHORTS.sh2.toplam} fps={30} width={1080} height={1920} />
  </>
);
