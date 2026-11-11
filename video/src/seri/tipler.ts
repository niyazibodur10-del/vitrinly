// Flip By Vote — dizi şablonu veri tipleri. Bir bölüm = tek bir `Bolum` nesnesi (bolumler/bolum-XXX.ts).
// Zamanlar SANİYE (bölüm başına göre); konumlar 1080x1920 kare pikseli (kamera dönüşümünden ÖNCEKİ sahne uzayı).

export type Konusmaci = "jake" | "mike";
export type AgizSekli = "A" | "B" | "C" | "D" | "E" | "F" | "G" | "H" | "X";

/** Yer tutucu görsel: yalnız taslak render'da kabul edilir (yayın render'ı `dogrula` kapısında durur). */
export type YerTutucu = { yerTutucu: "blok" | "figur" | "agiz"; renk: string; renk2?: string };
/** `public/` altındaki dosya yolu (ör. "seri/bolum-001/s1-arka.png") veya yer tutucu. */
export type Gorsel = string | YerTutucu;

/** Ağız yolu (görsel-varlik-sanatcisi önerir, bölüm/sahne verisinde seçilir):
 *  yama   = konuşmacının ağız bölgesine Rhubarb A–H/X yama karesi (agiz.json gerekir)
 *  ifade  = yalnız ifade görseli değişir (konuşurken "konusur", dinlerken "notr" veya satırın ifadesi)
 *  kamera = ağız hareketi yok; kamera konuşan karaktere kayar/yaklaşır */
export type AgizYolu = "yama" | "ifade" | "kamera";

export type Kelime = { k: string; bas: number; bitis: number };
/** Şablonun iç satır biçimi (konuşmacı küçük harf). kelimeler opsiyonel; yoksa harf sayısına göre dağıtılır. */
export type Satir = { konusmaci: Konusmaci; bas: number; bitis: number; metin: string; kelimeler?: Kelime[] };
export type SatirDosyasi = { ses?: string; sure?: number; satirlar: Satir[] };
/** ses-yonetmeni çıktısı olduğu gibi: tools/ses/diyalog.py → <ad>.zaman.json
 *  {"sesler":{JAKE:"am_onyx:0.95",...}, "sure", "satirlar":[{"no","konusmaci":"JAKE","bas","bitis","metin", "kelimeler"?}]}
 *  zaman.ts satirDosyasi() ile şablon biçimine çevrilir (konuşmacı küçük harfe, bilinmeyen konuşmacı → hata). */
export type ZamanJson = {
  sesler?: Record<string, string>; sure?: number;
  satirlar: { no?: number; konusmaci: string; bas: number; bitis: number; metin: string; kelimeler?: Kelime[] }[];
};
export type AgizCue = { bas: number; bitis: number; sekil: AgizSekli | string };
export type AgizDosyasi = Partial<Record<Konusmaci, AgizCue[]>> & { kaynak?: unknown };

export type AgizYamasi = {
  /** yamanın sahne uzayındaki kutusu (px) */
  x: number; y: number; w: number; h: number;
  /** şekil → görsel; eksik şekil Rhubarb eşlemesiyle en yakın şekle düşer (G→F, H→C, X→A) */
  sekiller: Partial<Record<AgizSekli, Gorsel>> | YerTutucu;
};

export type KarakterSahne = {
  kim: Konusmaci;
  /** karakter katmanı; yoksa karakter arka plan görseline gömülüdür (yalnız odak/ağız konumu kullanılır) */
  gorsel?: Gorsel;
  /** katman kutusu (px): x,y sol üst; w,h boyut. Gömülü karakterde odak hesabı için yine verilir. */
  x: number; y: number; w: number; h: number;
  /** "ifade" yolu: ifade adı → görsel ("notr" ve "konusur" önerilir) */
  ifadeler?: Record<string, Gorsel>;
  /** "yama" yolu */
  agiz?: AgizYamasi;
  /** kamera odak noktası (yüz merkezi); varsayılan kutunun üst %22'si */
  odak?: { x: number; y: number };
};

export type Kamera = {
  /** yavaş hareket: başlangıç/bitiş ölçeği ve kayma (px). Varsayılan 1 → 1.06, kayma yok. */
  zoom?: [number, number];
  kay?: { x?: [number, number]; y?: [number, number] };
  /** konuşmacıya punch-in ölçeği (yama/ifade yolunda hafif, kamera yolunda güçlü). 1 = kapalı. */
  punch?: number;
  /** zoom eğrisi: "inOut" (varsayılan) veya "out" (kare 0'da hareket halinde başlar — kanca) */
  egri?: "inOut" | "out";
  /** konuşmacı değişiminde geçiş süresi (sn); 0 = kesme (sert punch-in) */
  gecis?: number;
};

// ---- Çekim çatısı (animasyon-yonetmeni 2026-11-11, bölüm 001+) ----
// Sahne `cekim` alanı varsa Cekim.tsx çizer (mekân plakası + rig + kod-prop + kamera); yoksa eski SahneKarti.
/** Göz kapağı (kodla kırpma): görsel pikselinde göz elipsi + ten rengi. */
export type GozElips = { cx: number; cy: number; rx: number; ry: number; aci: number; ten: string };
/** Bir karakterin rig varlıkları: taban görseli + ağız yaması (3 durum) + gözler; ifade portreleri ayrı. */
export type RigKarakter = {
  taban: string; w: number; h: number;
  agiz: { x: number; y: number; w: number; h: number; kapali: string; yari: string; acik: string };
  gozler: GozElips[];
  /** yüz merkezi (taban pikseli): kamera odağı */
  yuz: { x: number; y: number };
  /** ifade portreleri: ad → {dosya, xy, gozler?} (yerlesim.json ifade_tekli) */
  portreler: Record<string, { dosya: string; w: number; h: number; xy: [number, number]; olcek: number; gozler?: GozElips[] }>;
};
/** Mekân seti (L1 mutfak): plakalar + karakterlerin geniş/tekli yerleşimi (yerlesim.json). */
export type MekanSeti = {
  genis: string; on?: string; tahta: string;
  /** tahta plakasında yazı alanı (px) */
  tahtaAlan: { x: number; y: number; w: number; h: number };
  ikili: Record<Konusmaci, { olcek: number; xy: [number, number] }>;
  /** ikili çekimde önde olan */
  onde: Konusmaci;
  tekli: Record<Konusmaci, { plakaOlcek: number; capa: [number, number] }>;
  portreArka: { olcek: number; capa: [number, number]; bulanik: number };
  karakterler: Record<Konusmaci, RigKarakter>;
};

export type Cekim =
  | { tur: "genis" }
  | { tur: "yakin"; kim: Konusmaci }
  | { tur: "portre"; kim: Konusmaci; ifade: string }
  | { tur: "ikiPortre"; sol: { kim: Konusmaci; ifade: string }; sag: { kim: Konusmaci; ifade: string } }
  | { tur: "tahta" };

export type IkonAdi = "hardal" | "kamyon" | "boya" | "saat" | "kartus" | "disk" | "araba" | "sifonyer" | "bisiklet" | "kutu";

/** Kod-prop. Zamanlar bölüm saniyesi. uzay "ekran" = kamera dışı (güvenli alan), "sahne" = plaka pikseli (kamerayla oynar). */
export type Prop =
  | { tur: "banknot"; bas: number; bitis?: number; x: number; y: number; aci?: number; olcek?: number; dus?: boolean; /** düşüş mesafesi (px) */ yukseklik?: number }
  | { tur: "ikon"; ad: IkonAdi; bas: number; bitis: number; x: number; y: number; boyut?: number; parla?: boolean; uzay?: "ekran" | "sahne" }
  | { tur: "ikonSira"; bas: number; bitis: number; y: number; ogeler: { ad: IkonAdi; t: number; etiket?: string }[]; ayrac?: string; boyut?: number }
  | { tur: "ilan"; bas: number; bitis: number; ikon: IkonAdi; baslik: string; fiyat: string; not: string; titre?: number; /** "alt" = yüzü kapatmayan alçak, yatay kart */ yer?: "ust" | "alt" }
  | { tur: "telefon"; bas: number; bitis: number; ogeler: { ikon: IkonAdi; fiyat: string }[] }
  | { tur: "tahtaYazi"; bas: number; satirlar: { metin: string; x: number; y: number; boyut: number; t: number; sure?: number; renk?: string; tik?: number[] }[] }
  | { tur: "tahtaKose"; bas: number; bitis: number; metin: string; yaz: number; x: number; y: number }
  | { tur: "yazi"; bas: number; bitis: number; metin: string; y: number; renk?: string; boyut?: number };

export type Sahne = {
  id: string;
  bas: number; bitis: number;
  arka: Gorsel;
  karakterler?: KarakterSahne[];
  agizYolu?: AgizYolu; // sahne düzeyinde; yoksa bölümün varsayılanı
  kamera?: Kamera;
  /** çekim çatısı (varsa Cekim.tsx); kamera.zoom/kay bu çekimde de geçerli */
  cekim?: Cekim;
  proplar?: Prop[];
  /** hızlı punch-in vuruşları (bölüm saniyesi): olcek'e `sure` içinde atlar ve kalır; sarsıntı: kısa titreme */
  vurus?: { t: number; olcek: number; sure?: number }[];
  sarsinti?: { t: number; sure?: number; guc?: number }[];
  /** kamera odağı (sahne pikseli); yoksa çekim türünün varsayılanı */
  odak?: { x: number; y: number };
  /** satır aralığına ifade ataması ("ifade" yolu): bu aralıkta kim hangi ifadede */
  ifadeler?: { bas: number; bitis: number; kim: Konusmaci; ifade: string }[];
};

export type BankOlayi = { t: number; deger: number; /** public/ yolu; false = sessiz; yoksa varsayılan */ ses?: string | false };

export type KazananYorum = { kullanici: string; metin: string; begeni?: number; bas?: number; sure?: number };

export type KararKarti = {
  soru: string;
  secenekler: string[]; // 2–3 seçenek; harfler A/B/C otomatik
  sure?: number; // 5–8 sn, bölüm sonuna yaslanır
  /** başlangıç (bölüm sn); yoksa sure − kararSure */
  bas?: number;
  /** kapanış anı (bölüm sn): "Ep. N: YOUR call" belirir, kart alta (altyazı bandına) iner. Yoksa baştan görünür. */
  kapanis?: number;
  /** seçenek önündeki renkli ikonlar (harf yok — incil §5.1) */
  ikonlar?: IkonAdi[];
};

export type SesKatmanlari = {
  diyalog: string; // public/ yolu (wav)
  muzik?: { dosya: string; ses?: number };
  sfx?: { dosya: string; ses?: number };
  /** şablonun kendi efektleri (BANK, abone klik, kart girişleri). Stem'de varsa false. */
  sablonSfx?: boolean;
};

export type Bolum = {
  /** kompozisyon kimliği, ör. "FBV-B001" */
  id: string;
  no: number;
  /** toplam süre (sn). Yayın kapısı: 60–90. */
  sure: number;
  satirlar: SatirDosyasi;
  agiz?: AgizDosyasi;
  agizYolu: AgizYolu;
  sahneler: Sahne[];
  bank: { baslangic: number; olaylar?: BankOlayi[] };
  ses: SesKatmanlari;
  kazananYorum?: KazananYorum;
  karar: KararKarti;
  /** abone/takip kartı; varsayılan karar kartından 0,4 sn önce biter. false = yok */
  abone?: { bas?: number; ust?: number; sure?: number; klik?: number } | false;
  /** açılış damgası yerleşimi: üst kenar (px), ölçek, sağa yaslı çip. Yoksa kart bandında, ortada, tam boy. */
  damga?: { ust?: number; olcek?: number; sag?: boolean };
  /** çekim çatısı mekân + rig seti (sahne.cekim kullanılıyorsa zorunlu) */
  mekan?: MekanSeti;
  /** logo dosyası (public/); yoksa şablonun geçici logosu */
  logo?: string;
};

export type BolumProps = { bolumId: string; taslak: boolean; kilavuz: boolean };
