# Kör dinleme anahtarı — gerçekçi sesler (Niyazi dinlemeden önce açmasın)
Her dosya aynı iki repliği okur (önce Mike repliği, 0,5 sn ara, sonra Jake repliği). −14 LUFS (±0,5), TP ≤ −1,5.

| Dosya | Motor | Ses (kaynak kaydın lisansı) | Uygun karakter | sha256 (12) |
|---|---|---|---|---|
| A1 | Kyutai Pocket TTS 100M | `michael` — VCTK p360, Amerikan erkek (CC BY 4.0) | Jake | 43432a475bb0 |
| A2 | Kyutai Pocket TTS 100M | `peter_yearsley` — LibriVox/voice-zero (CC0); aksan kaydı yok | Jake | 53157744d055 |
| A3 | Kyutai Pocket TTS 100M | `marius` — Kyutai gönüllü ses bağışı (CC0); aksan kaydı yok | Mike | bd1d2e80d223 |
| A4 | Kyutai Pocket TTS 100M | `javert` — Kyutai gönüllü ses bağışı (CC0); aksan kaydı yok | Jake | aebee30b4dfe |
| A5 | Kyutai Pocket TTS 100M | `george` — VCTK p315, Amerikan erkek (CC BY 4.0) | Mike (hızlı) / Jake | 6661ef804e46 |
| A6 | Kyutai Pocket TTS 100M | `stuart_bell` — LibriVox/voice-zero (CC0); aksan kaydı yok | Mike | 9b9f88a50ef5 |

Seçim sonrası üretim: `tools/ses/bolum-ses.sh uretim/seri/bolum-001 --ses JAKE=pocket:<ses> --ses MIKE=pocket:<ses>`
