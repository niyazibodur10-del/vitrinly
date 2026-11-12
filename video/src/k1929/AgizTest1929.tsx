import React from "react";
import { AbsoluteFill } from "remotion";
import { Sunucu, YUZ } from "./Sunucu";
import { fredoka } from "./ortak";

// Kalite kapısı karesi: 9 Rhubarb şekli (X, A–H) Leo'nun kendi yüzünde (rig yamaları), 3x3.
const SEKILLER = ["X", "A", "B", "C", "D", "E", "F", "G", "H"];
const ESLEME: Record<string, string> = { X: "taban a", A: "taban a", B: "C07", C: "C08", D: "b", E: "C09", F: "C10", G: "C07", H: "C08" };
export const AgizTest1929: React.FC = () => {
  const S = 1.5;
  return (
    <AbsoluteFill style={{ background: "#1b2333", display: "flex", flexDirection: "row", flexWrap: "wrap" }}>
      {SEKILLER.map((s) => (
        <div key={s} style={{ width: 640, height: 360, position: "relative", overflow: "hidden", outline: "2px solid #0b0f18" }}>
          <div style={{ position: "absolute", left: 320 - YUZ.x * S, top: 200 - YUZ.y * S, scale: String(S), transformOrigin: "0 0" }}>
            <Sunucu cues={[]} ofs={0} zorlaSekil={s} />
          </div>
          <div style={{ position: "absolute", left: 14, top: 6, color: "#fff", fontSize: 44, fontFamily: fredoka, fontWeight: 700, WebkitTextStroke: "6px #000", paintOrder: "stroke fill" }}>
            {s} <span style={{ fontSize: 26 }}>{ESLEME[s]}</span>
          </div>
        </div>
      ))}
    </AbsoluteFill>
  );
};
