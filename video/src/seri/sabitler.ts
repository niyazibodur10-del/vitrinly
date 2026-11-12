import { loadFont } from "@remotion/fonts";
import { staticFile } from "remotion";
import type { AgizSekli, Konusmaci } from "./tipler";

export const FPS = 30;
export const GEN = 1080;
export const YUK = 1920;

// Dikey güvenli alan (1080x1920). Kaynak ve karar: README.md "Güvenli alan".
// Üst 250 (IG/TikTok başlık sekmeleri, Shorts arama), alt 480 (= %25; kullanıcı adı, açıklama, müzik şeridi; TikTok ölçümü 480,
// IG organik ~%20), sol 60, sağ 190 (beğeni/yorum/paylaş sütunu; Shorts 192). Tüm metin ve kart bu kutunun içindedir.
export const GUVENLI = { sol: 60, ust: 250, sag: 1080 - 190, alt: 1920 - 480 } as const;
export const GUVENLI_W = GUVENLI.sag - GUVENLI.sol; // 830
export const GUVENLI_H = GUVENLI.alt - GUVENLI.ust; // 1190

// Dikey yerleşim bantları (güvenli alan içinde, birbirine binmez):
export const BANT = {
  bank: { ust: 270 }, // sol üst hap
  kart: { ust: 400, alt: 1110 }, // açılış damgası, kazanan yorum, abone kartı, karar kartı
  altyazi: { ust: 1150, alt: 1420 }, // altyazı öbeği (alt kenara yaslı)
} as const;

export const RENK: Record<Konusmaci, { ana: string; koyu: string; ad: string }> = {
  jake: { ana: "#4DA8FF", koyu: "#0B3A73", ad: "JAKE" },
  mike: { ana: "#FF5A4E", koyu: "#7A140D", ad: "MIKE" },
};
export const ALTIN = "#FFC93C";
export const ZEMIN_KART = "rgba(12,16,26,0.92)";

export const fredoka = "Fredoka";
export const anton = "Anton";
loadFont({ family: fredoka, url: staticFile("fonts/Fredoka-700.woff2"), weight: "700" });
loadFont({ family: anton, url: staticFile("fonts/Anton-400.woff2"), weight: "400" });

// Şablon efektleri (assets/efekt kaynaklı, lisans: assets/efekt kaydı; kopya video/public/seri/ortak/sfx)
export const SFX = {
  bankArti: "seri/ortak/sfx/ka-ching.flac",
  bankEksi: "seri/ortak/sfx/coin-drop.flac",
  klik: "seri/ortak/sfx/fare-klik.flac",
  kart: "seri/ortak/sfx/whoosh-kisa.flac",
  damga: "seri/ortak/sfx/pop-pluck.flac",
};

// Rhubarb eşlemesi: eksik yama şekli → en yakın temel şekil
export const AGIZ_YEDEK: Record<AgizSekli, AgizSekli[]> = {
  A: ["A", "X"], B: ["B", "C"], C: ["C", "B"], D: ["D", "C"], E: ["E", "C"],
  F: ["F", "E"], G: ["G", "F", "A"], H: ["H", "C", "B"], X: ["X", "A"],
};
