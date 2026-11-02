import React from "react";
import { Composition } from "remotion";
import { AgizTest } from "./AgizTest";
import { kare, KRITIK_KARE, KritikTest, SAHNE_BILESEN, SahneComp, Tam, TAM_KARE } from "./Tam";
import { SAHNELER } from "./veri-sahne";

// S08 Kitchen Table Budget (2026-10-28-yeni-video) — önek KButce (animasyon-yonetmeni)
export const KButceKompozisyonlar: React.FC = () => (
  <>
    <Composition id="KButceKritik" component={KritikTest} durationInFrames={KRITIK_KARE} fps={30} width={1920} height={1080} />
    <Composition id="KButceAgizTest" component={AgizTest} defaultProps={{ poz: "a" as const }} durationInFrames={1} fps={30} width={1920} height={1080} />
    <Composition id="KButceAgizTestG05" component={AgizTest} defaultProps={{ poz: "G05k" as const }} durationInFrames={1} fps={30} width={1920} height={1080} />
    <Composition id="KButceTam" component={Tam} durationInFrames={TAM_KARE} fps={30} width={1920} height={1080} />
    {SAHNELER.filter((s) => SAHNE_BILESEN[s.id]).map((s) => (
      <Composition key={s.id} id={`KButce-${s.id}`} component={SahneComp} defaultProps={{ id: s.id, altyazi: true }} durationInFrames={kare(s.bitis) - kare(s.bas)} fps={30} width={1920} height={1080} />
    ))}
  </>
);
