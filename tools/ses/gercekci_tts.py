#!/usr/bin/env python3
"""Gerçekçi (insan benzeri) TTS motorları — tools/ses/diyalog.py bunları "motor:ses:hiz" biçimiyle çağırır.

Motorlar (hepsi yerel, ücretsiz, ticari kullanıma açık; ayrıntı uretim/seri/sesler/gercekci/rapor.md):
  pocket:<ses>[:hiz]       Kyutai Pocket TTS 100M (pip pocket-tts; kod MIT, ağırlık CC BY 4.0). Ses kataloğu yalnız
                           ticari lisanslı olanlar: michael, george (VCTK, CC BY 4.0), marius, javert (gönüllü bağış, CC0),
                           bill_boerst, stuart_bell, peter_yearsley (LibriVox voice-zero, CC0). jean/cosette (EARS/Expresso
                           NC) YASAK. hiz != 1 ise zaman uzatma yok → hız yalnız 1.0 desteklenir.
  supertonic:<M1..M5>[:hiz] Supertone Supertonic-2 ONNX (kod MIT, ağırlık OpenRAIL-M: makine üretimi beyanı şart).
                           Model: ~/.finansal-arac/modeller/supertonic-2 (onnx/ + voice_styles/).
  kokoro:<am_x>[:hiz]      Kokoro-82M (eski yol).
Çalıştırma ortamı: ~/.finansal-arac/gercekci-venv/bin/python (kokoro-venv'in torch'unu .pth ile paylaşır).

API: Motor(spec) → .uret(metin) -> np.float32 dizi @ 24 kHz (diyalog.py SR'si).
Yazan: ses-yonetmeni 2026-11-11.
"""
import os, sys
import numpy as np

SR = 24000
ST_DIZIN = os.path.expanduser("~/.finansal-arac/modeller/supertonic-2")
POCKET_IZINLI = {"michael", "george", "marius", "javert", "bill_boerst", "stuart_bell", "peter_yearsley",
                 "charles", "paul"}
_ONBELLEK = {}


def _yeniden_ornekle(y, sr):
    if sr == SR:
        return y.astype(np.float32)
    from scipy.signal import resample_poly
    from math import gcd
    g = gcd(sr, SR)
    return resample_poly(y, SR // g, sr // g).astype(np.float32)


class Motor:
    def __init__(self, spec):
        p = spec.split(":")
        if p[0] not in ("pocket", "supertonic", "kokoro"):
            p = ["kokoro"] + p  # geriye uyum: "am_onyx:0.95"
        self.motor, self.ses = p[0], p[1]
        self.hiz = float(p[2]) if len(p) > 2 else 1.0
        self.spec = spec
        getattr(self, "_yukle_" + self.motor)()

    # --- Pocket TTS
    def _yukle_pocket(self):
        if self.ses not in POCKET_IZINLI:
            sys.exit(f"pocket sesi '{self.ses}' lisans listesinde yok (izinli: {sorted(POCKET_IZINLI)})")
        if "pocket" not in _ONBELLEK:
            from pocket_tts import TTSModel
            _ONBELLEK["pocket"] = TTSModel.load_model()
        self.m = _ONBELLEK["pocket"]
        self.durum = self.m.get_state_for_audio_prompt(self.ses)

    def _uret_pocket(self, metin):
        y = self.m.generate_audio(self.durum, metin).numpy().astype(np.float32)
        return _yeniden_ornekle(y, self.m.sample_rate)

    # --- Supertonic-2
    def _yukle_supertonic(self):
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        import supertonic_helper as sh
        if "supertonic" not in _ONBELLEK:
            _ONBELLEK["supertonic"] = sh.load_text_to_speech(os.path.join(ST_DIZIN, "onnx"))
        self.m = _ONBELLEK["supertonic"]
        self.stil = sh.load_voice_style([os.path.join(ST_DIZIN, "voice_styles", self.ses + ".json")])

    def _uret_supertonic(self, metin):
        wav, dur = self.m(metin, "en", self.stil, total_step=10, speed=self.hiz)
        y = wav[0, : int(self.m.sample_rate * float(np.ravel(dur)[0]))]
        return _yeniden_ornekle(y, self.m.sample_rate)

    # --- Kokoro
    def _yukle_kokoro(self):
        if "kokoro" not in _ONBELLEK:
            from kokoro import KPipeline
            _ONBELLEK["kokoro"] = KPipeline(lang_code="a", repo_id="hexgrad/Kokoro-82M")
        self.m = _ONBELLEK["kokoro"]
        self.ses = self.ses.replace("+", ",")

    def _uret_kokoro(self, metin):
        return np.concatenate([x.numpy() for _, _, x in self.m(metin, voice=self.ses, speed=self.hiz,
                                                               split_pattern=None)]).astype(np.float32)

    def uret(self, metin):
        return getattr(self, "_uret_" + self.motor)(metin)

    @property
    def satir_butun(self):
        """Gerçekçi motorlar satırı tek parça üretir (cümleler arası doğal prozodi); Kokoro cümle cümle."""
        return self.motor != "kokoro"


if __name__ == "__main__":  # hızlı deneme: gercekci_tts.py <spec> <metin> <cikis.wav>
    import soundfile as sf, time
    t = time.time(); mo = Motor(sys.argv[1]); t1 = time.time(); y = mo.uret(sys.argv[2])
    sf.write(sys.argv[3], y, SR)
    print(f"{sys.argv[1]}: yükleme {t1 - t:.1f} sn, üretim {time.time() - t1:.1f} sn, ses {len(y) / SR:.1f} sn")
