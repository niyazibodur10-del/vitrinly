# Dış kaynaklı ses varlıkları — lisans kaydı

Kural: yalnız **CC0** veya **CC-BY** (atıf metniyle). CC-BY-NC / CC-BY-SA / "kişisel kullanım" / kaynağı belirsiz dosya repoya girmez.
Her satır: dosya · kaynak URL · lisans · yazar · erişim tarihi · atıf metni. Lisans sayfasının o günkü kopyası `assets/lisans-kanit/` altında
(itiraz/Content ID anlaşmazlığında kanıt). Seviye ayarı (tepe −3 dBFS) ve biçim dönüşümü dışında içerik değiştirilmedi.

## Müzik (`assets/muzik/`)

| Dosya | Kaynak | Lisans | Yazar | Erişim | Not |
|---|---|---|---|---|---|
| `merak-unsolved-investigation-isaiah658.ogg` (48 sn, kesintisiz döngü, orijinal dosya) | https://opengameart.org/content/unsolved-investigation | CC0 1.0 | isaiah658 | 2026-10-26 | Ana alt müzik (merak/gizem) |
| `gerilim-80s-mysterywave-desertdev.ogg` (4:58, MP3'ten Vorbis q3'e dönüştürüldü, 4.3 MB) | https://opengameart.org/content/80s-mysterywave-music | CC0 1.0 | DesertDev | 2026-10-26 | Gerilim/kriz bölümleri, uzun yatak |
| `enerji-down-to-business-zane-little.mp3` (45 sn, orijinal dosya) | https://opengameart.org/content/down-to-business-day-25 | CC0 1.0 | Zane Little Music | 2026-10-26 | Giriş/kapanış, "iş/para" enerjisi |

CC0 atıf istemez; yine de açıklamaya gönüllü teşekkür önerilir (Content ID itirazında kaynağı göstermek kolaylaşır):
> Music: "Unsolved Investigation" by isaiah658, "80s Mysterywave" by DesertDev, "Down to Business" by Zane Little Music — all CC0 (OpenGameArt.org).

## Efekt (`assets/efekt/`, 48 kHz FLAC)

| Dosya | Kaynak | Lisans | Yazar | Erişim |
|---|---|---|---|---|
| `whoosh-kisa.flac`, `whoosh-uzun.flac`, `riser.flac` | Kendi üretimimiz: `tools/ses/efekt-uret.py` (sentez, sabit tohum) | Bizim | Financial Rise | 2026-10-26 |
| `pop-pluck.flac` (← `pluck_001.ogg`), `pop-drop.flac` (← `drop_002.ogg`), `tik-select.flac` (← `select_001.ogg`), `tik-click.flac` (← `click_001.ogg`) | https://kenney.nl/assets/interface-sounds | CC0 1.0 | Kenney (kenney.nl) | 2026-10-26 |
| `muhur-impact-punch.flac` (← `impactPunch_heavy_000.ogg`), `muhur-impact-plate.flac` (← `impactPlate_heavy_000.ogg`) | https://kenney.nl/assets/impact-sounds | CC0 1.0 | Kenney (kenney.nl) | 2026-10-26 |
| `yazi-klavye.flac` (← `Human Typing/human_vel-004.wav`) | https://opengameart.org/content/keyboard-soundpack-1-typing-and-single-keystrokes | CC0 1.0 | unicaegames | 2026-10-26 |
| `yazi-daktilo.flac` (← `typewriter2.wav`) | https://opengameart.org/content/typewriter-sounds | CC0 1.0 | Cassie-OrbitGames | 2026-10-26 |
| `para-coin-drop.flac` (← `coin_drop.ogg`) | https://opengameart.org/content/coin-drop | CC0 1.0 | Vinrax | 2026-10-26 |

Gönüllü atıf: "Sound effects: Kenney (kenney.nl), unicaegames, Cassie-OrbitGames, Vinrax — CC0."

## Anlatıcı sesi (TTS)

| Bileşen | Lisans | Kaynak | Not |
|---|---|---|---|
| Kokoro-82M model ağırlıkları + ses paketleri (`am_michael` vb.) | Apache-2.0 | https://huggingface.co/hexgrad/Kokoro-82M | Ticari kullanım serbest; üretilen ses bizim. Lisans metni model kartında (`license: apache-2.0`). |
| `kokoro` / `misaki` Python paketleri | Apache-2.0 | PyPI | Yalnız araç. |
| (Elenen aday) Piper `en_US-joe-medium` | Veri seti CC0 | https://huggingface.co/rhasspy/piper-voices | Elendi (kalite); kullanılmıyor. |
| (Elenen) Piper `en_US-ryan-high` | Veri seti **CC BY-NC-SA 4.0** | aynı | Ticari değil → baştan elendi. |

## Değerlendirilip alınmayanlar
- "The Y Files" (TAD, CC0): bilinen bir dizi temasının parodisi → melodik benzerlik/Content ID riski, alınmadı.
- "Investigation" (wipics, CC0): enerjinin %31'i konuşma bandında (1–4 kHz) → anlatımı maskeler.
- "Tension" (Komiku/Loyalty Freak Music, CC0): uygun ama yedek; dosyaya alınmadı (gerekirse https://opengameart.org/content/tension).
- `whoosh2_0.wav` (Air whoosh, CC0): 5 sn döngü, gürültü tabanı yüksek (SNR 19.6 dB) → yerine kendi sentezimiz.
- "Swishes Sound Pack" (CC0): 0.1–0.2 sn kılıç sesi, video geçişi için fazla kısa.
