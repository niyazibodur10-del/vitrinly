import React from "react";
import { Img, staticFile } from "remotion";
import type { AgizSekli, Gorsel } from "./tipler";

// Görsel katmanı: dosya (public/) veya yer tutucu. Yer tutucular YAZI İÇERMEZ (ekranda hata ayıklama yazısı yok);
// yalnız veri dosyasında `yerTutucu` alanıyla işaretlidir ve yayın kapısı (dogrula.ts) onları reddeder.

const AGIZ_ACIKLIK: Record<AgizSekli, [number, number]> = {
  // [genişlik oranı, yükseklik oranı] — Rhubarb şekillerinin kaba karşılığı
  A: [0.55, 0.06], B: [0.7, 0.22], C: [0.75, 0.42], D: [0.85, 0.7], E: [0.55, 0.45],
  F: [0.35, 0.3], G: [0.65, 0.18], H: [0.7, 0.35], X: [0.5, 0.05],
};

const Figur: React.FC<{ renk: string; renk2?: string }> = ({ renk, renk2 }) => {
  const id = "fg" + React.useId().replace(/[^a-zA-Z0-9_-]/g, "");
  return (
  <svg viewBox="0 0 400 900" width="100%" height="100%" preserveAspectRatio="none">
    <defs>
      <linearGradient id={id} x1="0" x2="1">
        <stop offset="0" stopColor={renk} />
        <stop offset="1" stopColor={renk2 ?? renk} />
      </linearGradient>
    </defs>
    <ellipse cx="200" cy="140" rx="105" ry="125" fill={`url(#${id})`} />
    <rect x="40" y="290" width="320" height="610" rx="150" fill={`url(#${id})`} />
  </svg>
  );
};

export const YerTutucuAgiz: React.FC<{ sekil: AgizSekli; renk: string }> = ({ sekil, renk }) => {
  const [w, h] = AGIZ_ACIKLIK[sekil] ?? AGIZ_ACIKLIK.X;
  return (
    <svg viewBox="0 0 100 100" width="100%" height="100%">
      <ellipse cx="50" cy="50" rx={50 * w} ry={Math.max(3, 50 * h)} fill={renk} />
    </svg>
  );
};

export const GorselKatman: React.FC<{ g: Gorsel; style?: React.CSSProperties; sekil?: AgizSekli }> = ({ g, style, sekil }) => {
  const kutu: React.CSSProperties = { position: "absolute", inset: 0, width: "100%", height: "100%", ...style };
  if (typeof g === "string") return <Img src={staticFile(g)} style={{ objectFit: "cover", ...kutu }} />;
  if (g.yerTutucu === "figur")
    return (
      <div style={kutu}>
        <Figur renk={g.renk} renk2={g.renk2} />
      </div>
    );
  if (g.yerTutucu === "agiz")
    return (
      <div style={kutu}>
        <YerTutucuAgiz sekil={sekil ?? "X"} renk={g.renk} />
      </div>
    );
  // blok: nötr arka plan — iki tonlu degrade + zemin çizgisi (derinlik hissi için)
  return (
    <div style={{ ...kutu, background: `linear-gradient(180deg, ${g.renk} 0%, ${g.renk} 62%, ${g.renk2 ?? g.renk} 62%, ${g.renk2 ?? g.renk} 100%)` }} />
  );
};
