---
name: earshot
description: Sesi ajan için kanıta çevirir — vuruş (SFX/kesme/cue) senkron ölçümü, dinleme transkripti, LUFS/true peak ölçümü ve koddan deterministik SFX üretimi (252 sesli banka, apex'i kareye hedefleme). F6b SFX stem'i, F7 kurgu SFX hizası ve F9 hakem örneklemesi için. Yerel CPU, ücretsiz, anahtar istemez.
---

# earshot (Toonomy uyarlaması)

Kaynak: https://github.com/Leonxlnx/earshot — Leon Lin, **MIT lisansı**, sabit sürüm `0.4.0` (commit `591fa3e`, 2026-10-22).
Banka sesleri kodla sentez; `fit/*` sesleri CC0 Freesound kayıtlarının ölçülmüş yapısı (örnek içermez, `docs/CREDITS_FIT.md`).
Lisans kaydına satır: `earshot sfx <id> — kendi üretim (MIT kod, Leon Lin; CC0 türev) — atıf gerekmez`.

## Kurulum (repo dışı, ~1,4 GB; sahibi uretim-muhendisi)
```bash
E=~/.finansal-arac/earshot-venv
uv venv -q --seed --python python3 $E
uv pip install -q --python $E/bin/python --index-url https://download.pytorch.org/whl/cpu "torch==2.14.1+cpu"
uv pip install -q --python $E/bin/python "git+https://github.com/Leonxlnx/earshot.git@591fa3e"
$E/bin/earshot doctor --fetch      # CLAP + AST modelleri bir kez (HF, sabit revizyon, safetensors); sonra:
export EARSHOT_OFFLINE=1           # çalışırken asla indirme yapmaz
```

## Güvenlik (ik-direktoru denetimi 2026-11-02)
- Ağ: yalnız `doctor --fetch` (Hugging Face, sabit commit, safetensors). Pickle yüklemez.
- `earshot llm` (Gemini) **KULLANILMAZ**: ücretli/anahtar ister ve sesi dışarı yükler. `--yes-upload` yasak.
- MCP sunucusu (`earshot mcp`) kurulmadı: ayar değişikliği gerektirir, CLI yeterli.

## Kim, nerede, ne için
| Faz | Sahip | Komut | Çıktı / kapı |
|---|---|---|---|
| F6b | muzik-ses-tasarimcisi | `earshot sfx list`, `earshot sfx render <id> --apex <sn> [--dur] [--pitch] [--seed] -o x.wav` | Vuruşun tepe anı görsel olay karesine hedeflenir (ölçülen apex raporda, `checks: clean`). Aynı seed = aynı bayt (deterministik). `--apex` yalnız whoosh/swish/swipe ailesinde; riser'da `--dur` + bitiş hizası. |
| F6b | muzik-ses-tasarimcisi | `earshot timeline <miks.wav> --cues cues.json --detail low` | Kendi kontrolü: her cue'da onset ±1 kare / ±100 ms, `NO HIT` sayısı 0. |
| F7 | kurgu-editoru | `earshot timeline <dilim.mp4> --cues cues.json --detail low --out sync.json` | SFX hizası kapısı (±2 kare) için ikinci ölçüm: video kesimleri + cue'lar, `NO HIT`/`CHECK` satırları `kurgu-rapor.md`'ye. |
| F9 | hakem | aynı `timeline` komutu, 2 rastgele 30 sn pencere | Örneklem: kurgu-editoru'nun sonucuyla çelişirse karneye. |
| her yerde | ses-muhendisi, muzik-ses-tasarimcisi | `earshot measure <dosya>` (model yüklemez, ~15 sn) | LUFS, true peak, LRA, gürültü tabanı; ebur128'e ikinci görüş. |

## Cue dosyası (animasyon-efekt-cue.json → earshot)
earshot `{fps, events:[{f, kind, id}]}` bekler; dilim başlangıcı `T0` ise:
```python
ev=[{'f':round((o['t']-T0)*30),'kind':o['tur'],'id':o.get('oneri','')} for o in d['olaylar'] if T0<=o['t']<T0+SURE]
```

## Okuma kuralları
- `NO HIT` = cue'nun ±100 ms içinde onset yok. Whoosh'ta tepe kesmeden **sonra** gelebilir (tasarım gereği); `strong sound at +N ms` değeri >67 ms (2 kare) ise sahibine CHECK olarak döner, otomatik RED değil — `earshot sheet` PNG'sine bakıp karar verilir.
- Etiketler (CLAP) ipucudur, kanıt değil; senkron ve ölçüm sayıları kanıttır.
- Her CLI çağrısı modelleri 20–40 sn yükler: çok pencere varsa tek Python betiği (`from earshot import api`). Ağır CPU işleriyle aynı anda koşma (`nice`, `--threads 2`).
- `critique` puan kartı ürün tanıtım filmi profiline göredir (Toonomy anlatımlı uzun video değil): karar ölçütü yapma.

## Test kanıtı (2026-11-02, S08 Kitchen Table Budget, final 176,1–206,1 sn)
`timeline dilim.mp4 --cues cues.json --detail low` → 29,8 sn; 9 cue'nun %78'i ±100 ms, 2 `NO HIT` (194,33 ve 201,87 sn "kesme kısa whoosh", güçlü ses +163/+133 ms).
`measure` → −14,2 LUFS, TP −3,7 dBTP. `sfx render whoosh_fast/crisp --apex 0.25` → ölçülen apex +0 ms, 2 koşu sha256 `ee71d0224684` aynı.
