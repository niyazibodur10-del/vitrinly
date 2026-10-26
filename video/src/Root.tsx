import { Composition } from "remotion";
import { Pilot, PILOT_SURE } from "./pilot/Pilot";
import { AgizTest } from "./pilot/AgizTest";
import { DikeyKesit } from "./ortak/DikeyKesit";

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
      <Composition id="AgizTest" component={AgizTest} durationInFrames={1} fps={30} width={1920} height={1080} />
    </>
  );
};
