#!/usr/bin/env python3
"""Flip By Vote Bölüm 002 paketi — TEK KAYNAK (kalıp: bolum-001/paket/paket-uret.py). Metinler burada; çıktılar betikle.
Çıktı: teslim/yayin-paketi.json (yukle.py şeması), teslim/platform-metinleri.md
Kapılar (çıkış 1 = hata): politika + anonim + ses atfı satırları birebir ve yerinde, yasak kalıplar, sınırlar, soru bolum.txt'de,
video sha/süre (VIDEO_SHA12 None iken BEKL: render yok). Kullanım: python3 paket-uret.py [--final]  (--final: BEKL = hata)"""
import hashlib, json, os, re, subprocess, sys
BOL = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
KOK = os.path.abspath(os.path.join(BOL, "../../.."))
TESLIM = os.path.join(BOL, "teslim")
sys.path.insert(0, os.path.join(KOK, "tools/yayin"))

EP = 2
VIDEO = "bolum-002.mp4"  # seri-render çıktı adı (B001 kalıbı); render gelince ls ile teyit
VIDEO_SHA12, VIDEO_SURE = None, None  # render gelince yazılır
KAPAK_SN = None  # animasyon-yonetmeni önerisi gelince
YAYIN_ZAMANI = "2026-11-12T17:00:00Z"  # 20:00 TSİ (CLAUDE.md yayın saati)
ONAY = {"niyazi_onayi": False, "tarih": None}  # onayı paketleyici vermez

POLITIKA = "Fiction. Not financial advice. Voices and visuals are AI-generated."
SES_ATIF = ("Voices: Kyutai Pocket TTS; Jake's voice synthesized from the VCTK corpus (CSTR, University of Edinburgh). "
            "CC BY 4.0: creativecommons.org/licenses/by/4.0")  # politika Z2
SES_KAYNAK = "Sources: huggingface.co/kyutai/pocket-tts-without-voice-cloning · datashare.ed.ac.uk/handle/10283/3443"  # yalnız YouTube
ANONIM = "We may show winning comments on screen with your username. Prefer to stay anonymous? Just say so in your comment."
SORU_VIDEO = ("Take the ninety, hold out, or counter?", "Tell us in the comments.")  # B01 + B02, bolum.txt'de aranır
SORU = "Take $90, hold out for $140, or counter at $115?"  # rakamlar dogrulama.md N5–N7

YT_BASLIK = "Take $90, Hold Out, or Counter? You Pick · Ep. 2"
YT_ACIKLAMA = "\n".join([
    "Nobody commented last time, so Mike picked the bike. Two torn tubes and one no-show buyer later, Brenda finally has an offer: $90 cash, today.",
    SORU + " Tell us in the comments.",
    "Jake & Mike started with $100. The goal: $1,000,000. You decide the moves.",
    "", ANONIM, "", POLITIKA, SES_ATIF, SES_KAYNAK, "", "#Shorts #flipbyvote #flipping #bikeflip"])
YT_ETIKET = ["Flip By Vote", "flipbyvote", "animated series", "interactive story", "you decide", "bike flip", "road bike",
             "flipping", "reselling", "side hustle", "haggling", "lowball offer", "Jake and Mike", "animation", "cartoon"]
YT_KATEGORI = "24"
PIN_YORUM = ("Jake wants the sure $90. Mike swears Brenda is worth $140. Would you take the deal, wait, or counter? "
             "Got a smarter move? Tell us that too.\n\n" + ANONIM)

IG_ACIKLAMA = "\n".join([
    SORU + " You pick · Ep. 2",
    "Nobody commented last time, so Mike picked the bike. Then the tubes tore and the buyer never showed.",
    "Jake & Mike: $100 to $1,000,000, one choice at a time. Tell us in the comments.",
    "", ANONIM, "", POLITIKA, SES_ATIF, "", "#flipbyvote #flipping #animatedseries #bikeflip"])
TT_ACIKLAMA = "\n".join([
    SORU + " Ep. 2 of $100 → $1,000,000. Nobody commented last time, so Mike picked. Tell us in the comments.",
    "", ANONIM, "", POLITIKA, SES_ATIF, "", "#flipbyvote #flipping #animatedseries #bikeflip"])

YASAK = re.compile(r"\b(tomorrow|daily|every ?day|drops?|comment (?:[a-c1-3])\b|like if|tag a friend|share|win|winner|giveaway|prize|"
                   r"subscribe|follow|you should|invest|guarantee|vote for|you ignored|kids)\b", re.I)


def kontrol(final=False):
    h, bekl = [], []
    for ad, m in {"YT açıklama": YT_ACIKLAMA, "IG açıklama": IG_ACIKLAMA, "TikTok açıklama": TT_ACIKLAMA}.items():
        st = m.split("\n")
        if POLITIKA not in st: h.append(f"{ad}: politika satırı birebir yok"); continue
        if ANONIM not in st: h.append(f"{ad}: anonim satırı birebir yok")
        i = st.index(POLITIKA)
        if i + 1 >= len(st) or st[i + 1] != SES_ATIF: h.append(f"{ad}: ses atfı AI satırının hemen altında birebir yok")
        if m.count("#") > 5: h.append(f"{ad}: hashtag > 5")
    st = YT_ACIKLAMA.split("\n")
    if SES_ATIF in st and (st.index(SES_ATIF) + 1 >= len(st) or st[st.index(SES_ATIF) + 1] != SES_KAYNAK):
        h.append("YT açıklama: kaynak satırı ses atfının hemen altında yok")
    for ad, m in {"YT": YT_ACIKLAMA, "IG": IG_ACIKLAMA, "TT": TT_ACIKLAMA, "pin": PIN_YORUM, "başlık": YT_BASLIK}.items():
        for y in YASAK.findall(m): h.append(f"{ad}: yasak kalıp '{y}'")
    if len(YT_BASLIK) > 60: h.append(f"YT başlık {len(YT_BASLIK)} > 60")
    if not YT_BASLIK.startswith("Take $90, Hold Out, or Counter?"): h.append("A4: başlık seçim sorusuyla başlamıyor")
    if not IG_ACIKLAMA.startswith(SORU): h.append("A4: IG ilk satırı seçim sorusu değil")
    for t in (IG_ACIKLAMA, TT_ACIKLAMA):
        if len(t) > 2200: h.append("IG/TT açıklama > 2200")
    bt = open(os.path.join(BOL, "bolum.txt"), encoding="utf-8").read()
    for parca in SORU_VIDEO:
        if parca not in bt: h.append(f"soru videoda yok: {parca}")
    for rakam in ("ninety", "hundred and forty", "hundred and fifteen"):
        if rakam not in bt: h.append(f"açıklamadaki rakam videoda yok: {rakam}")
    vy = os.path.join(TESLIM, VIDEO)
    if VIDEO_SHA12 is None or not os.path.isfile(vy): bekl.append("video/sha/süre: render bekleniyor")
    else:
        sha = hashlib.sha256(open(vy, "rb").read()).hexdigest()[:12]
        if sha != VIDEO_SHA12: h.append(f"video sha {sha} ≠ {VIDEO_SHA12}")
        sure = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", vy],
                                    capture_output=True, text=True).stdout)
        if abs(sure - VIDEO_SURE) > 0.05: h.append(f"video süresi {sure:.2f} ≠ {VIDEO_SURE}")
        if KAPAK_SN is None or not 0 < KAPAK_SN < sure: bekl.append("kapak karesi yok / video dışında")
    for k in ("kapak-1080x1920.jpg", "kapak-1080x1350.jpg"):
        if not os.path.isfile(os.path.join(TESLIM, k)): bekl.append(f"{k} yok")
    if final: h += [f"BEKL→hata: {b}" for b in bekl]; bekl = []
    return h, bekl


def main():
    h, bekl = kontrol("--final" in sys.argv)
    yp = {"sema": "yayin-paketi/1", "tur": "shorts",
          "dosyalar": {"video": VIDEO, "altyazilar": []},
          "metadata": {"baslik": YT_BASLIK, "aciklama": YT_ACIKLAMA, "etiketler": YT_ETIKET, "bolumler": [],
                       "kategori_id": YT_KATEGORI, "varsayilan_dil": "en", "ses_dili": "en"},
          "durum": {"gizlilik": "private", "yayin_zamani": YAYIN_ZAMANI, "cocuklara_ozel": False, "sentetik_medya": True,
                    "lisans": "youtube", "gomulebilir": True},
          "oynatma_listesi_id": None, "onay": ONAY,
          "_not": (f"Bölüm {EP}. yayin_zamani 17:00Z = 20:00 TSİ. sentetik_medya=true (politika-format §3), cocuklara_ozel=false. "
                   f"Video {VIDEO_SURE} sn, sha256 {VIDEO_SHA12}. #Shorts yalnız YouTube'da: yukle.py kapısı ister (A4 'gerekmiyor'). "
                   "Kaynak: paket/paket-uret.py; elle düzenleme yok.")}
    json.dump(yp, open(os.path.join(TESLIM, "yayin-paketi.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
    kap = f"kaynak kare {KAPAK_SN:.2f} sn = kare {round(KAPAK_SN * 30)}" if KAPAK_SN else "kaynak kare: render bekleniyor"
    md = [f"# Bölüm {EP:03d} · platform metinleri (betik çıktısı: paket/paket-uret.py — elle düzenleme yok)", "",
          f"Video: `{VIDEO}` · {VIDEO_SURE} sn · 1080x1920 · sha256 {VIDEO_SHA12} · yayın 20:00 TSİ (17:00Z), üç platform aynı anda", "",
          f"## YouTube Shorts\nBaşlık ({len(YT_BASLIK)} krk):\n```\n{YT_BASLIK}\n```\nAçıklama ({len(YT_ACIKLAMA)} krk):\n```\n{YT_ACIKLAMA}\n```",
          f"Etiketler: `{', '.join(YT_ETIKET)}` · Kategori 24 Entertainment · made for kids: No · altered/synthetic: Yes · dil en",
          f"\nSabit yorum (üç platformda aynı; yayından sonra):\n```\n{PIN_YORUM}\n```",
          f"\n## Instagram Reels\nAçıklama ({len(IG_ACIKLAMA)}/2200 krk):\n```\n{IG_ACIKLAMA}\n```",
          f"Kapak: `kapak-1080x1920.jpg` ({kap}); profil ızgarası: `kapak-1080x1350.jpg`. AI label: AÇIK. Platform müziği yok.",
          f"\n## TikTok\nAçıklama ({len(TT_ACIKLAMA)} krk):\n```\n{TT_ACIKLAMA}\n```",
          "Kapak: `kapak-1080x1920.jpg`. AI-generated: AÇIK. Otomatik yorum yanıtı YOK (politika §5).", ""]
    open(os.path.join(TESLIM, "platform-metinleri.md"), "w", encoding="utf-8").write("\n".join(md))
    for x in h: print("HATA:", x)
    for x in bekl: print("BEKL:", x)
    print(f"kapı: {len(h)} hata, {len(bekl)} bekleyen · YT başlık {len(YT_BASLIK)}")
    return 1 if h else 0


if __name__ == "__main__":
    sys.exit(main())
