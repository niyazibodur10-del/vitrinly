import React from "react";
import { Composition } from "remotion";
import { AgizTest } from "./AgizTest";
import { DEk, DIKEY_SAHNE, kare, KRITIK_KARE, KritikTest, SahneComp, Tam, TAM_KARE } from "./sahneler";
import { SAHNELER, SHORTS_EK } from "./veri-sahne";

// S03 "The Biggest Inheritance Ever" (2026-11-04-miras-sizintilari) — önek KMiras (animasyon-yonetmeni).
// İskelet: 160 kpm tahmini zaman (veri-sahne.ts TAHMİNİ); ses gelince sahne-veri.py üstüne yazar, kompozisyon süreleri kendiliğinden güncellenir.
export const KMirasKompozisyonlar: React.FC = () => (
  <>
    <Composition id="KMirasKritik" component={KritikTest} durationInFrames={KRITIK_KARE} fps={30} width={1920} height={1080} />
    <Composition id="KMirasAgizTest" component={AgizTest} defaultProps={{ poz: "a" as const }} durationInFrames={1} fps={30} width={1920} height={1080} />
    <Composition id="KMirasTam" component={Tam} durationInFrames={TAM_KARE} fps={30} width={1920} height={1080} />
    {SAHNELER.map((s) => (
      <Composition key={s.id} id={`KMiras-${s.id}`} component={SahneComp} defaultProps={{ id: s.id, altyazi: true }} durationInFrames={kare(s.bitis) - kare(s.bas)} fps={30} width={1920} height={1080} />
    ))}
    {/* 9:16: uzun anlatımdan dikey sahneler + Shorts tam okumaları (kurgu-editoru keser, ABONE'yi koyar) */}
    {DIKEY_SAHNE.map((id) => {
      const s = SAHNELER.find((x) => x.id === id)!;
      return <Composition key={`D${id}`} id={`KMirasD-${id}`} component={SahneComp} defaultProps={{ id, altyazi: true }} durationInFrames={kare(s.bitis) - kare(s.bas)} fps={30} width={1080} height={1920} />;
    })}
    <Composition id="KMirasD-Sh1" component={DEk} defaultProps={{ ek: "sh1" as const, altyazi: true }} durationInFrames={Math.ceil(SHORTS_EK.sh1.sure * 30)} fps={30} width={1080} height={1920} />
    <Composition id="KMirasD-Sh2" component={DEk} defaultProps={{ ek: "sh2" as const, altyazi: true }} durationInFrames={Math.ceil(SHORTS_EK.sh2.sure * 30)} fps={30} width={1080} height={1920} />
  </>
);
