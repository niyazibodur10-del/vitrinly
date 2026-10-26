import React from "react";
import { AbsoluteFill } from "remotion";
import { Karakter } from "./Karakter";

// Test: tüm ağız şekillerini yüz üzerinde yan yana gösterir (kalite kapısı için).
const SEKILLER = ["X", "A", "B", "C", "D", "E", "F", "G", "H"];
export const AgizTest: React.FC = () => (
  <AbsoluteFill style={{ background: "#222", display: "flex", flexDirection: "row", flexWrap: "wrap" }}>
    {SEKILLER.map((s) => (
      <div key={s} style={{ width: 640, height: 360, position: "relative", overflow: "hidden" }}>
        <div style={{ position: "absolute", left: -1340, top: -1900, transform: "scale(2.6)", transformOrigin: "0 0" }}>
          <Karakter zaman={0} zorlaSekil={s} kirpmaTohum={1} />
        </div>
        <div style={{ position: "absolute", left: 16, top: 8, color: "#fff", fontSize: 48, fontFamily: "sans-serif" }}>{s}</div>
      </div>
    ))}
  </AbsoluteFill>
);
