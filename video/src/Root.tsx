import { Composition } from "remotion";
import { Pilot, PILOT_SURE } from "./pilot/Pilot";
import { AgizTest } from "./pilot/AgizTest";
import { DikeyKesit } from "./ortak/DikeyKesit";
import { KritikTest, KRITIK_SURE } from "./k1929/KritikTest";
import { AgizTest1929 } from "./k1929/AgizTest1929";
import { kare, SahneComp, Tam, TAM_KARE } from "./k1929/Tam";
import { SAHNELER, SHORTS_EK } from "./k1929/veri-tam";
import { DEk, DikeySahneComp, DIKEY_SAHNE } from "./k1929/dikey";

const PilotDikey: React.FC = () => (
  <DikeyKesit mod="dolgu">
    <Pilot />
  </DikeyKesit>
);

export const RemotionRoot: React.FC = () => {
  return (
    <>
      <Composition
        id="Pilot"
        component={Pilot}
        durationInFrames={Math.round(PILOT_SURE * 30)}
        fps={30}
        width={1920}
        height={1080}
      />
      {/* 9:16 hat testi: Pilot'un 16:9 karesi dikeye sığdırılmış (gerçek Shorts kurgusu kurgu-editoru'nun) */}
      <Composition
        id="PilotDikey"
        component={PilotDikey}
        durationInFrames={Math.round(PILOT_SURE * 30)}
        fps={30}
        width={1080}
        height={1920}
      />
      {/* 1929-1000-dolar F5 kritik yol testi (animasyon-yonetmeni) */}
      <Composition id="K1929Kritik" component={KritikTest} durationInFrames={Math.round(KRITIK_SURE * 30)} fps={30} width={1920} height={1080} />
      <Composition id="K1929AgizTest" component={AgizTest1929} durationInFrames={1} fps={30} width={1920} height={1080} />
      {/* 1929-1000-dolar F5 tam video: tümü + sahne başına (kurgu-editoru birleştirir) */}
      <Composition id="K1929Tam" component={Tam} durationInFrames={TAM_KARE} fps={30} width={1920} height={1080} />
      {SAHNELER.map((s) => (
        <Composition key={s.id} id={`K1929-${s.id}`} component={SahneComp} defaultProps={{ id: s.id, altyazi: true }} durationInFrames={kare(s.bitis) - kare(s.bas)} fps={30} width={1920} height={1080} />
      ))}
      {/* 9:16 Shorts sahneleri (kurgu-editoru keser) + Shorts ek kayıtları (yeni hook/kapanış, konuşan Leo) */}
      {Object.keys(DIKEY_SAHNE).map((id) => {
        const s = SAHNELER.find((x) => x.id === id)!;
        return <Composition key={`D${id}`} id={`K1929D-${id}`} component={DikeySahneComp} defaultProps={{ id, altyazi: true }} durationInFrames={kare(s.bitis) - kare(s.bas)} fps={30} width={1080} height={1920} />;
      })}
      <Composition id="K1929D-Sh1Ek" component={DEk} defaultProps={{ ek: "sh1" as const }} durationInFrames={Math.ceil(SHORTS_EK.sh1.sure * 30)} fps={30} width={1080} height={1920} />
      <Composition id="K1929D-Sh2Ek" component={DEk} defaultProps={{ ek: "sh2" as const }} durationInFrames={Math.ceil(SHORTS_EK.sh2.sure * 30)} fps={30} width={1080} height={1920} />
      <Composition id="AgizTest" component={AgizTest} durationInFrames={1} fps={30} width={1920} height={1080} />
    </>
  );
};
