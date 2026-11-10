import React from "react";
import { Audio } from "@remotion/media";
import { AbsoluteFill, CalculateMetadataFunction, Sequence, staticFile, useVideoConfig } from "remotion";
import { AboneOl, ABONE_KLIK_SN, ABONE_SURE_SN } from "../ortak/AboneOl";
import { Altyazi } from "./Altyazi";
import { BankSayaci } from "./BankSayaci";
import { bolumBul } from "./bolumler";
import { dogrula } from "./dogrula";
import { AcilisDamgasi, GeciciLogo, KararKartiKatman, KazananYorumKarti } from "./Kartlar";
import { BANT, FPS, GUVENLI, SFX } from "./sabitler";
import { SahneKarti } from "./SahneKarti";
import type { Bolum, BolumProps } from "./tipler";

// Flip By Vote bölüm kompozisyonu: veri (bolumler/bolum-XXX.ts) → 1080x1920 30 fps video.
// Katman sırası (alttan üste): sahne kartları (sert kesme) → altyazı → BANK → açılış damgası → kazanan yorum
// → abone/takip kartı → karar kartı (karartma + kart). Ses: diyalog + müzik + SFX stem'i + şablon efektleri.
// Veri kapısı calculateMetadata'da: yayın modunda (taslak=false, varsayılan) yer tutucu / kural ihlali render'ı durdurur.

export const DAMGA_SN = 1.8;

export const zamanlar = (b: Bolum) => {
  const kararSure = b.karar.sure ?? 7;
  const kararBas = b.sure - kararSure;
  const yorumBas = b.kazananYorum ? b.kazananYorum.bas ?? DAMGA_SN : 0;
  const aboneBas = b.abone === false ? null : b.abone?.bas ?? kararBas - 0.4 - ABONE_SURE_SN;
  return { kararSure, kararBas, yorumBas, aboneBas };
};

export const bolumMetadata: CalculateMetadataFunction<BolumProps> = ({ props }) => {
  const b = bolumBul(props.bolumId);
  if (!b) throw new Error(`[seri] bölüm yok: ${props.bolumId}`);
  const hatalar = dogrula(b, { taslak: props.taslak, kilavuz: props.kilavuz });
  if (hatalar.length) throw new Error(`[seri kapı] ${b.id} ${props.taslak ? "(taslak)" : "(yayın)"}:\n- ${hatalar.join("\n- ")}`);
  return { durationInFrames: Math.round(b.sure * FPS), fps: FPS, width: 1080, height: 1920 };
};

const Kilavuz: React.FC = () => (
  // Yalnız taslakta (kapı yayında reddeder): güvenli alan ve bantlar. Yazı içermez.
  <AbsoluteFill style={{ pointerEvents: "none" }}>
    <div style={{ position: "absolute", left: 0, right: 0, top: 0, height: GUVENLI.ust, background: "rgba(255,0,80,0.28)" }} />
    <div style={{ position: "absolute", left: 0, right: 0, top: GUVENLI.alt, bottom: 0, background: "rgba(255,0,80,0.28)" }} />
    <div style={{ position: "absolute", left: GUVENLI.sag, width: 1080 - GUVENLI.sag, top: GUVENLI.ust, height: GUVENLI.alt - GUVENLI.ust, background: "rgba(255,0,80,0.28)" }} />
    <div style={{ position: "absolute", left: 0, width: GUVENLI.sol, top: GUVENLI.ust, height: GUVENLI.alt - GUVENLI.ust, background: "rgba(255,0,80,0.18)" }} />
    <div style={{ position: "absolute", left: GUVENLI.sol, top: GUVENLI.ust, width: GUVENLI.sag - GUVENLI.sol, height: GUVENLI.alt - GUVENLI.ust, outline: "4px dashed #00ff88" }} />
    {[BANT.kart.ust, BANT.kart.alt, BANT.altyazi.ust, BANT.altyazi.alt].map((y) => (
      <div key={y} style={{ position: "absolute", left: GUVENLI.sol, width: GUVENLI.sag - GUVENLI.sol, top: y, height: 0, borderTop: "3px dotted #ffe600" }} />
    ))}
  </AbsoluteFill>
);

export const BolumKompozisyon: React.FC<BolumProps> = ({ bolumId, kilavuz }) => {
  const { fps } = useVideoConfig();
  const b = bolumBul(bolumId)!;
  const k = (sn: number) => Math.round(sn * fps);
  const { kararSure, kararBas, yorumBas, aboneBas } = zamanlar(b);
  const sablonSfx = b.ses.sablonSfx !== false;
  const satirlar = b.satirlar.satirlar;

  return (
    <AbsoluteFill style={{ backgroundColor: "#000" }}>
      {b.sahneler.map((s) => (
        <Sequence key={s.id} from={k(s.bas)} durationInFrames={k(s.bitis) - k(s.bas)} name={`sahne ${s.id}`}>
          <SahneKarti sahne={s} satirlar={satirlar} agiz={b.agiz} agizYolu={b.agizYolu} />
        </Sequence>
      ))}
      <Altyazi satirlar={satirlar} />
      <BankSayaci baslangic={b.bank.baslangic} olaylar={b.bank.olaylar ?? []} sesAcik={sablonSfx} />
      <Sequence durationInFrames={k(DAMGA_SN)} name="açılış damgası">
        <AcilisDamgasi no={b.no} sure={DAMGA_SN} logo={b.logo} />
      </Sequence>
      {b.kazananYorum ? (
        <Sequence from={k(yorumBas)} durationInFrames={k(b.kazananYorum.sure ?? 4)} name="kazanan yorum">
          <KazananYorumKarti y={b.kazananYorum} />
        </Sequence>
      ) : null}
      {aboneBas !== null ? (
        <Sequence from={k(aboneBas)} durationInFrames={k(ABONE_SURE_SN)} name="takip">
          <AboneOl
            duzen="dikey" ust={BANT.kart.ust + 60} ad="Flip By Vote" tutamac="@flipbyvote" adBoyut={30}
            dugme="FOLLOW" dugmeSonra="✓ FOLLOWING" profil={<GeciciLogo boyut={96} logo={b.logo} />}
          />
        </Sequence>
      ) : null}
      <Sequence from={k(kararBas)} durationInFrames={k(kararSure)} name="karar kartı">
        <KararKartiKatman k={b.karar} sonrakiNo={b.no + 1} />
      </Sequence>
      {kilavuz ? <Kilavuz /> : null}

      {/* ses katmanları */}
      <Audio src={staticFile(b.ses.diyalog)} />
      {b.ses.muzik ? <Audio src={staticFile(b.ses.muzik.dosya)} volume={b.ses.muzik.ses ?? 0.18} /> : null}
      {b.ses.sfx ? <Audio src={staticFile(b.ses.sfx.dosya)} volume={b.ses.sfx.ses ?? 1} /> : null}
      {sablonSfx ? (
        <>
          <Sequence from={0} durationInFrames={k(1)} layout="none"><Audio src={staticFile(SFX.damga)} volume={0.6} /></Sequence>
          {b.kazananYorum ? <Sequence from={k(yorumBas)} durationInFrames={k(1)} layout="none"><Audio src={staticFile(SFX.kart)} volume={0.5} /></Sequence> : null}
          {aboneBas !== null ? <Sequence from={k(aboneBas + ABONE_KLIK_SN)} durationInFrames={k(1)} layout="none"><Audio src={staticFile(SFX.klik)} volume={0.9} /></Sequence> : null}
          <Sequence from={k(kararBas)} durationInFrames={k(1)} layout="none"><Audio src={staticFile(SFX.kart)} volume={0.6} /></Sequence>
        </>
      ) : null}
    </AbsoluteFill>
  );
};
