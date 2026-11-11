import React from "react";
import type { IkonAdi } from "./tipler";

// Kodla çizilen prop ikonları (logosuz, marka yok). 100x100 viewBox, "çıkartma" dili: kalın koyu kontur + beyaz kenar
// (Ikon bileşeni dışına beyaz hale ve gölge verir). Dizi boyunca tekrar kullanılır.

const K = "#1d1b22"; // kontur
const s = { stroke: K, strokeWidth: 4, strokeLinejoin: "round" as const, strokeLinecap: "round" as const };

const CIZIM: Record<IkonAdi, React.ReactNode> = {
  hardal: (
    <g {...s}>
      <path d="M42 8 h16 v10 h-16z" fill="#d23b2f" />
      <path d="M45 18 h10 l4 10 h-18z" fill="#f4c21b" />
      <path d="M36 28 h28 c4 0 6 3 6 7 v52 c0 4-3 7-7 7 h-26 c-4 0-7-3-7-7 v-52 c0-4 2-7 6-7z" fill="#f4c21b" />
      <path d="M34 50 h32 v22 h-32z" fill="#fff6d6" />
      <path d="M40 61 h20" stroke="#d23b2f" strokeWidth={5} />
    </g>
  ),
  kamyon: (
    <g {...s}>
      <path d="M6 30 h52 v40 h-52z" fill="#e8eef6" />
      <path d="M58 42 h20 l14 14 v14 h-34z" fill="#3a8be0" />
      <path d="M64 46 h12 l9 9 h-21z" fill="#bfe0ff" />
      <circle cx="24" cy="74" r="9" fill="#2a2d36" />
      <circle cx="76" cy="74" r="9" fill="#2a2d36" />
      <circle cx="24" cy="74" r="3" fill="#cfd5df" />
      <circle cx="76" cy="74" r="3" fill="#cfd5df" />
    </g>
  ),
  boya: (
    <g {...s}>
      <path d="M22 30 c0-6 56-6 56 0 v50 c0 8-56 8-56 0z" fill="#c9d1db" />
      <ellipse cx="50" cy="30" rx="28" ry="7" fill="#7cc3a0" />
      <path d="M22 44 c0 6 56 6 56 0 v20 c0 6-56 6-56 0z" fill="#2fae6a" />
      <path d="M26 30 c0-22 48-22 48 0" fill="none" />
      <path d="M62 31 c2 10 -2 18 2 26" stroke="#2fae6a" strokeWidth={6} fill="none" />
    </g>
  ),
  saat: (
    <g {...s}>
      <circle cx="50" cy="54" r="36" fill="#fffaf0" />
      <path d="M30 14 l-12 12 M70 14 l12 12" strokeWidth={8} />
      <path d="M50 54 V32 M50 54 l14 10" strokeWidth={6} />
      <circle cx="50" cy="54" r="4" fill={K} />
    </g>
  ),
  kartus: (
    <g {...s}>
      <path d="M22 14 h56 v60 l-8 10 h-40 l-8-10z" fill="#7b5cd6" />
      <path d="M30 22 h40 v30 h-40z" fill="#ffd34d" />
      <path d="M36 30 l8 14 l8-10 l6 8" stroke="#e05a2e" fill="none" />
      <path d="M34 76 v8 M42 76 v8 M50 76 v8 M58 76 v8 M66 76 v8" stroke="#f2c14e" strokeWidth={4} />
    </g>
  ),
  disk: (
    <g {...s}>
      <circle cx="40" cy="58" r="30" fill="#d9dde4" />
      <circle cx="40" cy="58" r="8" fill="#ffffff" />
      <circle cx="62" cy="44" r="30" fill="#e7eaef" />
      <circle cx="62" cy="44" r="8" fill="#ffffff" />
      <path d="M46 26 l26 30 M70 22 l-10 18 M44 52 l30 6" stroke="#8a8f99" strokeWidth={3} fill="none" />
    </g>
  ),
  araba: (
    <g {...s}>
      <path d="M8 62 c0-10 6-14 14-16 l14-14 c4-3 8-4 14-4 h18 c6 0 10 3 14 10 l6 10 c6 2 4 6 4 14 v6 h-84z" fill="#e2564a" />
      <path d="M38 36 h14 v14 h-26z M56 36 h12 c3 0 5 2 7 5 l4 9 h-23z" fill="#bfe0ff" />
      <circle cx="28" cy="72" r="10" fill="#2a2d36" />
      <circle cx="74" cy="72" r="10" fill="#2a2d36" />
    </g>
  ),
  sifonyer: (
    <g {...s}>
      <path d="M14 10 h72 v74 h-72z" fill="#b8793f" />
      <path d="M20 18 h60 v18 h-60z M20 42 h60 v18 h-60z M20 66 h60 v12 h-60z" fill="#d39858" />
      <path d="M44 27 h12 M44 51 h12 M44 72 h12" strokeWidth={5} />
      <path d="M18 84 v8 M82 84 v8" strokeWidth={6} />
    </g>
  ),
  bisiklet: (
    <g {...s} fill="none">
      <circle cx="24" cy="64" r="18" strokeWidth={6} />
      <circle cx="76" cy="64" r="18" strokeWidth={6} />
      <path d="M24 64 l18-28 h30 l4 28 M42 36 l12 28 h22 M54 64 l18-28 M38 28 h12 M70 30 l4-8 h8" stroke="#e2564a" strokeWidth={6} />
      <path d="M8 78 q8 6 20 2" stroke="#8a8f99" strokeWidth={4} />
    </g>
  ),
  kutu: (
    <g {...s}>
      <path d="M12 40 l38-14 l38 14 v40 l-38 14 l-38-14z" fill="#c8945a" />
      <path d="M12 40 l38 14 l38-14 M50 54 v40" fill="none" />
      <path d="M12 40 l-6-12 l38-14 l6 12z M88 40 l6-12 l-38-14 l-6 12z" fill="#ddb07a" />
      <text x="50" y="80" textAnchor="middle" fontFamily="Anton" fontSize="22" fill={K} stroke="none">?</text>
    </g>
  ),
};

export const Ikon: React.FC<{ ad: IkonAdi; boyut: number; parla?: number; hale?: boolean }> = ({ ad, boyut, parla = 0, hale = true }) => (
  <div style={{ width: boyut, height: boyut, position: "relative" }}>
    {parla > 0 ? (
      <div style={{ position: "absolute", inset: -boyut * 0.35, borderRadius: "50%", background: `radial-gradient(circle, rgba(255,214,77,${0.75 * parla}) 0%, rgba(255,214,77,0) 65%)` }} />
    ) : null}
    <svg viewBox="-6 -6 112 112" width={boyut} height={boyut} style={{ position: "relative", filter: hale ? "drop-shadow(0 0 0 #fff) drop-shadow(3px 0 0 #fff) drop-shadow(-3px 0 0 #fff) drop-shadow(0 3px 0 #fff) drop-shadow(0 -3px 0 #fff) drop-shadow(0 8px 10px rgba(0,0,0,0.45))" : undefined }}>
      {CIZIM[ad]}
    </svg>
  </div>
);
