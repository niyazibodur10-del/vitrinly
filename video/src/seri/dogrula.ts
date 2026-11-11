import type { Bolum } from "./tipler";

// Veri kapısı. calculateMetadata içinde çalışır: hata varsa render HİÇ başlamaz.
// taslak=false (varsayılan, yayın): yer tutucu, kılavuz çizgisi ve süre/kart kuralı ihlali → hata.
// taslak=true: yalnız yapısal hatalar (zaman sırası, eksik veri) hata; yer tutucu serbest.

const yerTutuculariBul = (o: unknown, yol: string, out: string[]) => {
  if (o && typeof o === "object") {
    if ("yerTutucu" in (o as object)) out.push(yol);
    for (const [k, v] of Object.entries(o as object)) if (k !== "yerTutucu") yerTutuculariBul(v, `${yol}.${k}`, out);
  }
};

export const yerTutucular = (b: Bolum): string[] => {
  const out: string[] = [];
  // Geçici logo (b.logo yok) yer tutucu sayılmaz: temiz, yayınlanabilir geçici sürüm (README).
  yerTutuculariBul(b.sahneler, "sahneler", out);
  return out;
};

export const dogrula = (b: Bolum, o: { taslak: boolean; kilavuz: boolean }): string[] => {
  const h: string[] = [];
  const S = b.sure;
  const sat = b.satirlar.satirlar;
  if (!sat.length) h.push("satır yok");
  sat.forEach((s, i) => {
    if (!(s.bitis > s.bas)) h.push(`satır ${i}: bitis <= bas`);
    if (i && s.bas < sat[i - 1].bitis - 0.02) h.push(`satır ${i}: önceki satırla çakışıyor`);
    if (s.bitis > S) h.push(`satır ${i}: bölüm süresini aşıyor (${s.bitis} > ${S})`);
    if (s.konusmaci !== "jake" && s.konusmaci !== "mike") h.push(`satır ${i}: bilinmeyen konuşmacı ${s.konusmaci}`);
  });
  // sahneler bölümü boşluksuz kaplamalı
  const sh = [...b.sahneler].sort((a, c) => a.bas - c.bas);
  if (!sh.length || sh[0].bas !== 0) h.push("ilk sahne 0'da başlamalı");
  sh.forEach((s, i) => {
    if (!(s.bitis > s.bas)) h.push(`sahne ${s.id}: bitis <= bas`);
    if (i && Math.abs(s.bas - sh[i - 1].bitis) > 1e-6) h.push(`sahne ${s.id}: önceki sahneyle boşluk/çakışma`);
    const yol = s.agizYolu ?? b.agizYolu;
    if (yol === "yama" && !s.cekim) {
      if (!b.agiz) h.push(`sahne ${s.id}: yama yolu agiz.json ister`);
      if (!s.karakterler?.some((k) => k.agiz)) h.push(`sahne ${s.id}: yama yolu en az bir karakterde agiz kutusu ister`);
    }
    if (s.cekim) {
      if (!b.mekan) h.push(`sahne ${s.id}: çekim çatısı bolum.mekan ister`);
      else if (s.cekim.tur === "portre" && !b.mekan.karakterler[s.cekim.kim].portreler[s.cekim.ifade]) h.push(`sahne ${s.id}: portre yok (${s.cekim.kim}:${s.cekim.ifade})`);
    } else {
      if (yol === "ifade" && !s.karakterler?.some((k) => k.ifadeler)) h.push(`sahne ${s.id}: ifade yolu karakter ifadeleri ister`);
    }
  });
  if (sh.length && Math.abs(sh[sh.length - 1].bitis - S) > 1e-6) h.push("son sahne bölüm sonunda bitmeli");
  const kSure = b.karar.sure ?? 7;
  if (kSure < 5 || kSure > 8) h.push(`karar kartı süresi 5–8 sn olmalı (${kSure})`);
  if (b.karar.secenekler.length < 2 || b.karar.secenekler.length > 3) h.push("karar kartı 2–3 seçenek ister");
  if (b.kazananYorum) {
    const ys = b.kazananYorum.sure ?? 4;
    if (ys < 3 || ys > 5) h.push(`kazanan yorum kartı 3–5 sn olmalı (${ys})`);
    if (!b.kazananYorum.kullanici.trim()) h.push("kazanan yorum: kullanıcı adı boş");
  }
  if (b.karar.bas !== undefined && b.karar.bas + kSure > S + 1e-6) h.push("karar kartı bölüm sonunu aşıyor");
  if (b.abone && b.abone.bas !== undefined && b.abone.bas + 3.5 > S + 1e-6) h.push("abone kartı bölüm sonunu aşıyor");
  for (const e of b.bank.olaylar ?? []) if (e.t < 0 || e.t > S) h.push(`BANK olayı bölüm dışında (${e.t})`);
  if (!o.taslak) {
    if (S < 60 || S > 90) h.push(`yayın süresi 60–90 sn olmalı (${S})`);
    const yt = yerTutucular(b);
    if (yt.length) h.push(`yer tutucu görsel var (${yt.length}): ${yt.slice(0, 4).join(", ")}${yt.length > 4 ? " …" : ""}`);
    if (o.kilavuz) h.push("kılavuz çizgileri yalnız taslakta");
  }
  return h;
};
