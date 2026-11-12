import React from "react";
import { AbsoluteFill, Composition, Easing, interpolate, Sequence, useCurrentFrame, useVideoConfig } from "remotion";
import { Audio } from "@remotion/media";
import { AltyaziParca, DEk, kare, SahneComp, Tam, TAM_KARE } from "./sahneler";
import { f } from "./kit";
import { anton, fredoka } from "./ortak";
import { ABONE_ANA, KURGU_SHORTS } from "./kurgu-veri";
import { AboneOl } from "../../ortak/AboneOl";
import { SAHNELER } from "./veri-sahne";
import { plan } from "./zaman";

// F7 kurgu katmanı (kurgu-editoru) — S03 The Great Wealth Transfer Has a Leak. Kaynak desen: videolar/yeni-video/kurgu.tsx.
// KMirasTam'ı altyazısız sarar → kurgu vurguları + abone → altyazı en üstte. Vurgusuz karelerde KMirasTam ile piksel-aynı.

const CL = { extrapolateLeft: "clamp", extrapolateRight: "clamp" } as const;
const SARI = "#ffd43b", KIRMIZI = "#ff5a4f";
const SAHNE_BAS: Record<string, number> = Object.fromEntries(SAHNELER.map((s) => [s.id, s.bas]));

const Serit: React.FC<{ bas: number; son: number; x: number; y: number; hiza?: "left" | "right"; boyut?: number; children: React.ReactNode }> = ({ bas, son, x, y, hiza = "left", boyut = 64, children }) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();
  const t = frame / fps;
  if (t < bas || t >= son) return null;
  const p = interpolate(t, [bas, bas + 0.25], [0, 1], { ...CL, easing: Easing.out(Easing.back(1.6)) });
  return (
    <div style={{ position: "absolute", [hiza]: x, top: y, textAlign: hiza, opacity: Math.min(1, p * 1.4), scale: String(0.7 + 0.3 * p), transformOrigin: hiza === "left" ? "0% 50%" : "100% 50%", fontFamily: anton, fontSize: boyut, lineHeight: 1.05, color: "#ffffff", textShadow: "0 3px 0 #000, 0 0 16px rgba(0,0,0,0.85)", letterSpacing: 1 }}>
      {children}
    </div>
  );
};

// ---------- Açılış varyantları (ilk 30 sn): A animasyon · B + vaat şeridi (2,0 başlık / 6,9 vaat) · C = B + kamyona yavaş itme ----------
export const VARYANT: Record<string, { vaat: boolean; itme: boolean }> = { A: { vaat: false, itme: false }, B: { vaat: true, itme: false }, C: { vaat: true, itme: true } };
export const KURGU_VARYANT = "B"; // kazanan (kurgu-rapor.md §1)

const VaatSeridi: React.FC = () => {
  const frame = useCurrentFrame();
  const t = frame / 30;
  if (t >= 9.45) return null;
  return (
    <>
      <Serit bas={2.0} son={9.45} x={90} y={120} hiza="right">THE GREAT WEALTH TRANSFER</Serit>
      {t >= 6.9 ? (
        <Serit bas={6.9} son={9.45} x={90} y={192} hiza="right">
          <span style={{ color: KIRMIZI }}>HAS A LEAK.</span> <span style={{ color: SARI }}>HOW BIG?</span>
        </Serit>
      ) : null}
    </>
  );
};
// C: kamyon planında (0–9,45) sol-alt sabit yavaş itme (kaynak satırı sol altta kalır)
const Itme: React.FC<{ acik: boolean; children: React.ReactNode }> = ({ acik, children }) => {
  const frame = useCurrentFrame();
  const t = frame / 30;
  if (!acik || t >= 9.45) return <>{children}</>;
  const s = interpolate(t, [0, 9.45], [1, 1.07], CL);
  return <AbsoluteFill style={{ transform: `scale(${s})`, transformOrigin: "0% 100%" }}>{children}</AbsoluteFill>;
};

// ---------- S21 vurgusu (16:9 ve dikey): 507–520 sn'de ekranda yalnız başlık + vergi çizgisi → yeni rakam yok ----------
// sahne-YEREL zaman (S21 başı = 0). "typical family" etiketi → zeminden vergi çizgisine uzayan ölçü oku → medyan çubuğuna halka.
type S21Yer = { etiket: number; okUst: number; cizgi: number; taban: number; ok: number; cip: [number, number]; halka: [number, number]; boy: number };
const S21_YATAY: S21Yer = { etiket: 330, okUst: 310, cizgi: 116, taban: 975, ok: 1050, cip: [250, 680], halka: [900, 978], boy: 1 };
const S21_DIKEY: S21Yer = { etiket: 530, okUst: 380, cizgi: 380, taban: 1500, ok: 930, cip: [80, 1150], halka: [490, 1500], boy: 0.85 };
const S21Vurgu: React.FC<{ y: S21Yer }> = ({ y }) => {
  const frame = useCurrentFrame();
  const g = frame / 30 + SAHNE_BAS.S21; // global sn
  if (g < 506.95 || g >= 519.85) return null;
  const cip = interpolate(g, [506.95, 507.2], [0, 1], { ...CL, easing: Easing.out(Easing.back(1.6)) });
  const ok = interpolate(g, [509.3, 512.3], [0, 1], { ...CL, easing: Easing.inOut(Easing.cubic) });
  const ust = interpolate(g, [512.3, 512.55], [0, 1], { ...CL, easing: Easing.out(Easing.back(2)) });
  const halka = interpolate(g, [515.0, 515.3, 516.6], [0, 1, 0.75], CL);
  const boyOk = (y.taban - y.okUst) * ok; // 16:9: başlık çizginin altında (G4) → ok başlığın altında biter, yazıya binmez
  return (
    <AbsoluteFill style={{ pointerEvents: "none" }}>
      <div style={{ position: "absolute", left: y.cip[0], top: y.cip[1], opacity: cip, scale: String(0.8 + 0.2 * cip), transformOrigin: "0% 50%", padding: "8px 18px", borderRadius: 10, background: "rgba(10,14,26,0.85)", border: `4px solid ${SARI}`, fontFamily: anton, fontSize: 46 * y.boy, color: SARI, letterSpacing: 1 }}>A TYPICAL FAMILY ↓</div>
      {ok > 0 ? (
        <>
          <div style={{ position: "absolute", left: y.ok - 4, top: y.taban - boyOk, width: 8, height: boyOk, background: `repeating-linear-gradient(to top, ${SARI} 0 22px, transparent 22px 36px)` }} />
          <div style={{ position: "absolute", left: y.ok - 22, top: y.taban - boyOk - 30, fontFamily: anton, fontSize: 44, color: SARI, textShadow: "0 2px 0 #000" }}>▲</div>
        </>
      ) : null}
      {ust > 0 ? <div style={{ position: "absolute", left: y.ok - 330, top: y.etiket, opacity: ust, scale: String(0.8 + 0.2 * ust), fontFamily: anton, fontSize: 40 * y.boy, color: KIRMIZI, textShadow: "0 2px 0 #000" }}>THE TAX LINE</div> : null}
      {halka > 0 ? <div style={{ position: "absolute", left: y.halka[0] - 150, top: y.halka[1] - 60, width: 300, height: 120, borderRadius: "50%", border: `7px solid ${SARI}`, opacity: halka, scale: String(0.7 + 0.3 * Math.min(1, halka * 1.3)), boxShadow: "0 0 26px rgba(255,212,59,0.5)" }} /> : null}
    </AbsoluteFill>
  );
};

export const Final: React.FC<{ varyant?: string }> = ({ varyant = KURGU_VARYANT }) => {
  const v = VARYANT[varyant];
  return (
    <AbsoluteFill style={{ background: "#000" }}>
      <Itme acik={v.itme}>
        <Tam altyazi={false} />
      </Itme>
      {v.vaat ? <VaatSeridi /> : null}
      <Sequence from={kare(SAHNE_BAS.S21)} durationInFrames={kare(SAHNE_BAS.S22) - kare(SAHNE_BAS.S21)} name="S21Vurgu" layout="none">
        <S21Vurgu y={S21_YATAY} />
      </Sequence>
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
// Kanca snap'i: ek kaydının ilk planı 3–4 sn durağan → 1,5 sn'de ×1,06 snap (ilk 2 sn görsel değişim), kesmede biter
const Snap: React.FC<{ an: number; s: number; oy: string; children: React.ReactNode }> = ({ an, s, oy, children }) => {
  const frame = useCurrentFrame();
  const t = frame / 30;
  const k = interpolate(t, [an, an + 4 / 30], [1, s], { ...CL, easing: Easing.out(Easing.cubic) });
  return <AbsoluteFill style={{ transform: `scale(${k})`, transformOrigin: `50% ${oy}` }}>{children}</AbsoluteFill>;
};

// Köprü kartı (son 2 sn): cevap yalnız uzun videoda → alttaki "ilgili video" bağlantısını işaret eder; kuyrukta altyazı yok → "BIGGEST LEAK = ?" yazısının (≈1170) altında, güvenli alan ≤1536
const KopruKarti: React.FC<{ ust: string; alt: string }> = ({ ust, alt }) => {
  const frame = useCurrentFrame();
  const t = frame / 30;
  const p = interpolate(t, [0, 0.25], [0, 1], { ...CL, easing: Easing.out(Easing.back(1.4)) });
  const ok = Math.sin(t * Math.PI * 3) * 10;
  return (
    <AbsoluteFill>
      <div style={{ position: "absolute", left: 70, top: 1220, width: 760, padding: "24px 28px", borderRadius: 22, background: SARI, border: "6px solid #0b0b0b", boxShadow: "0 10px 0 #0b0b0b", textAlign: "center", opacity: p, scale: String(0.8 + 0.2 * p) }}>
        <div style={{ fontFamily: anton, fontSize: 56, color: "#0b0b0b", lineHeight: 1.05 }}>{ust}</div>
        <div style={{ fontFamily: fredoka, fontWeight: 700, fontSize: 34, color: "#0b0b0b", marginTop: 8 }}>{alt}</div>
      </div>
      <div style={{ position: "absolute", left: 418, top: 1400 + ok, fontFamily: anton, fontSize: 90, color: SARI, textShadow: "0 4px 0 #000", opacity: p }}>↓</div>
    </AbsoluteFill>
  );
};
const KOPRU = { ust: "THE ANSWER IS IN THE FULL VIDEO", alt: "The Great Wealth Transfer Has a Leak" };

// Shorts 2 politika satırı (metin §5, Z2): sabit. Ek planlarında üstte (y 196); S21 kesitinde punch-in'li başlık oraya taştığı için
// kırmızı vergi çizgisinin hemen altında (y 400). Altta altyazı (iki satır) ve zemin çizgisi var → alta konmaz.
const G4_KES = plan("S21").kes.find((c) => c[3] === "g4")![0]; // S21 yerel sn: G4 grafiğine kesme
const FederalSatir: React.FC = () => {
  const frame = useCurrentFrame();
  const p = KURGU_SHORTS.sh2.parcalar.find((x) => x.tur === "sahne")!;
  // S21 kesitinde G4 planı: başlık punch-in'den önce y 310–420, sonra ~230–330; kırmızı çizgi 440 → ~375 → şerit çizginin ALTINDA (460).
  // R2 (hakem F9): y 400'de punch-in öncesi başlığın 2. satırına biniyordu. Leo planında (G4'ten önce) ve ek planlarında üstte (196).
  const g4 = frame >= p.yer && frame < p.yer + p.sure && p.kareBas + (frame - p.yer) >= kare(SAHNE_BAS.S21 + G4_KES);
  return (
    <div style={{ position: "absolute", left: 60, width: 840, top: g4 ? 460 : 196, textAlign: "center", padding: "6px 0", borderRadius: 10, background: "rgba(0,0,0,0.55)", fontFamily: fredoka, fontWeight: 700, fontSize: 28, color: "#e8ecf4", letterSpacing: 0.5 }}>
      US FEDERAL ONLY · STATE &amp; OTHER COUNTRIES DIFFER
    </div>
  );
};

// Kuyruk: ek kaydın son planı sessiz, altyazısız; yavaş itme (donma kapısı)
const Kuyruk: React.FC<{ ek: "sh1" | "sh2"; kareBas: number; sure: number }> = ({ ek, kareBas, sure }) => {
  const frame = useCurrentFrame();
  const s = interpolate(frame, [kareBas, kareBas + sure], [1, 1.07], CL);
  return (
    <AbsoluteFill style={{ transform: `scale(${s})`, transformOrigin: "50% 40%" }}>
      <DEk ek={ek} altyazi={false} />
    </AbsoluteFill>
  );
};

export const KurguShorts: React.FC<{ ad: "sh1" | "sh2" }> = ({ ad }) => {
  const v = KURGU_SHORTS[ad];
  return (
    <AbsoluteFill style={{ background: "#000" }}>
      <Audio src={f(`${ad}-yatak.wav`)} />
      {v.parcalar.map((p, i) => (
        <Sequence key={i} from={p.yer} durationInFrames={p.sure} name={`${p.tur}-${p.kaynak}-${p.bas}`}>
          {p.tur === "sahne" ? (
            <Sequence from={-(p.kareBas - kare(SAHNE_BAS[p.kaynak]))}>
              <SahneComp id={p.kaynak} />
              {p.kaynak === "S21" ? <S21Vurgu y={S21_DIKEY} /> : null}
            </Sequence>
          ) : (
            <Sequence from={-p.kareBas}>
              {p.tur === "kuyruk" ? (
                <Kuyruk ek={p.kaynak as "sh1" | "sh2"} kareBas={p.kareBas} sure={p.sure} />
              ) : i === 0 ? (
                <Snap an={1.5} s={1.06} oy={ad === "sh1" ? "45%" : "30%"}>
                  <DEk ek={p.kaynak as "sh1" | "sh2"} />
                </Snap>
              ) : (
                <DEk ek={p.kaynak as "sh1" | "sh2"} />
              )}
            </Sequence>
          )}
        </Sequence>
      ))}
      {ad === "sh2" ? <FederalSatir /> : null}
      {/* Shorts 2 kancası: TAX tabelası 0–3,75 durağan, ×1,06 snap koyu planda algılanmadı (kadans ilk olay 4,75) → 1,45 sn metin pop'u */}
      {ad === "sh2" ? (
        <AbsoluteFill style={{ alignItems: "center" }}>
          <Serit bas={1.45} son={3.75} x={0} y={830} boyut={92}>
            <div style={{ width: 1080, textAlign: "center" }}>
              THE <span style={{ color: KIRMIZI }}>SCARIEST</span> LEAK?
            </div>
          </Serit>
        </AbsoluteFill>
      ) : null}
      <Sequence from={v.abone.kare} durationInFrames={v.abone.sure} name="AboneOl" layout="none">
        <AboneOl duzen="dikey" sure={v.abone.sure / 30} ust={v.abone.ust ?? undefined} />
      </Sequence>
      <Sequence from={v.kopruBas} name="Kopru">
        <KopruKarti {...KOPRU} />
      </Sequence>
    </AbsoluteFill>
  );
};

export const KMirasKurgu: React.FC = () => (
  <>
    <Composition id="KMirasFinal" component={Final} durationInFrames={TAM_KARE} fps={30} width={1920} height={1080} />
    {(["A", "B", "C"] as const).map((x) => (
      <Composition key={x} id={`KMirasIlk30-${x}`} component={Final} defaultProps={{ varyant: x }} durationInFrames={900} fps={30} width={1920} height={1080} />
    ))}
    <Composition id="KMirasShorts1" component={KurguShorts} defaultProps={{ ad: "sh1" as const }} durationInFrames={KURGU_SHORTS.sh1.toplam} fps={30} width={1080} height={1920} />
    <Composition id="KMirasShorts2" component={KurguShorts} defaultProps={{ ad: "sh2" as const }} durationInFrames={KURGU_SHORTS.sh2.toplam} fps={30} width={1080} height={1920} />
  </>
);
