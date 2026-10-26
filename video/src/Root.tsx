import { Composition } from "remotion";
import { Pilot, PILOT_SURE } from "./pilot/Pilot";
import { AgizTest } from "./pilot/AgizTest";

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
      <Composition id="AgizTest" component={AgizTest} durationInFrames={1} fps={30} width={1920} height={1080} />
    </>
  );
};
