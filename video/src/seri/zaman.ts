import type { AgizCue, AgizSekli, Kelime, Konusmaci, Satir } from "./tipler";

/** t anında konuşan satır (yoksa null). */
export const aktifSatir = (satirlar: Satir[], t: number): Satir | null =>
  satirlar.find((s) => t >= s.bas && t < s.bitis) ?? null;

/** t'den önce başlamış son satır (satır arası boşlukta kamera son konuşmacıda kalsın diye). */
export const sonSatir = (satirlar: Satir[], t: number): Satir | null => {
  let son: Satir | null = null;
  for (const s of satirlar) if (s.bas <= t) son = s;
  return son;
};

/** Satırın kelimeleri; ses-yonetmeni kelime zamanı vermediyse harf sayısına göre orantılı dağıtılır. */
export const kelimeler = (s: Satir): Kelime[] => {
  if (s.kelimeler && s.kelimeler.length) return s.kelimeler;
  const parca = s.metin.split(/\s+/).filter(Boolean);
  const top = parca.reduce((a, p) => a + p.length + 1, 0);
  let t = s.bas;
  return parca.map((p) => {
    const d = ((p.length + 1) / top) * (s.bitis - s.bas);
    const k = { k: p, bas: t, bitis: t + d };
    t += d;
    return k;
  });
};

/** Altyazı için kelimeyi satır metnindeki yazımla eşle (Kokoro/Whisper token'ı noktalamasız olabilir). */
export const ekranKelimeleri = (s: Satir): Kelime[] => {
  const ks = kelimeler(s);
  const metin = s.metin.split(/\s+/).filter(Boolean);
  if (metin.length === ks.length) return ks.map((k, i) => ({ ...k, k: metin[i] }));
  return ks;
};

/** Altyazı öbekleri: satır içinde en fazla `max` kelime veya noktalama sonunda bölünür. */
export const obekler = (s: Satir, max = 4): Kelime[][] => {
  const out: Kelime[][] = [];
  let cur: Kelime[] = [];
  for (const k of ekranKelimeleri(s)) {
    cur.push(k);
    if (cur.length >= max || /[.!?,;:]$/.test(k.k)) {
      out.push(cur);
      cur = [];
    }
  }
  if (cur.length) out.push(cur);
  return out;
};

export const agizSekli = (cues: AgizCue[] | undefined, t: number): AgizSekli => {
  if (!cues) return "X";
  const c = cues.find((x) => t >= x.bas && t < x.bitis);
  return ((c?.sekil as AgizSekli) ?? "X") as AgizSekli;
};

export const konusuyor = (satirlar: Satir[], kim: Konusmaci, t: number) =>
  satirlar.some((s) => s.konusmaci === kim && t >= s.bas && t < s.bitis);

export const kare = (sn: number, fps: number) => Math.round(sn * fps);
