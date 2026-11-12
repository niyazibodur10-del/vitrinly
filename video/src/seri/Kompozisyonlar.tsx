import React from "react";
import { Composition, Folder } from "remotion";
import { BolumKompozisyon, bolumMetadata } from "./Bolum";
import { BOLUMLER } from "./bolumler";
import { FPS } from "./sabitler";
import type { BolumProps } from "./tipler";

// Her bölüm bir kompozisyon. Varsayılan props = YAYIN modu (taslak=false): yer tutucu varsa calculateMetadata
// render'ı durdurur. Taslak/kanıt render'ı: --props='{"taslak":true}' (tools/seri-render.sh --taslak).
export const SeriKompozisyonlar: React.FC = () => (
  <Folder name="FlipByVote">
    {BOLUMLER.map((b) => (
      <Composition
        key={b.id}
        id={b.id}
        component={BolumKompozisyon}
        calculateMetadata={bolumMetadata}
        defaultProps={{ bolumId: b.id, taslak: false, kilavuz: false } satisfies BolumProps}
        durationInFrames={Math.round(b.sure * FPS)}
        fps={FPS}
        width={1080}
        height={1920}
      />
    ))}
  </Folder>
);
