"""Bölüm 002 replikleri — TEK KAYNAK. metin-kontrol.py bunu okur.
(id, sahne, konuşan, replik, sessiz_vuruş_sn_önce)
konuşan: JAKE / MIKE. sessiz = diyalog.py otomatik boşluğuna EK sessizlik (SFX, grafik, tutuş)."""
SATIRLAR = [
    # S1 KANCA + PREVIOUSLY (≤3 sn) — YAKIN-M, kare 0'da bisiklet (G1) sağdan yuvarlanıyor, "flap-flap" 0.1 sn;
    # üstte önceki seçim kartı BIKE ✓ · DRESSER · BOX (rozet yok, Z1) + ilerleme şeridi "Ep. 2 · BANK $100 → $1,000,000"
    ("M01", "S1", "MIKE", "No comments, so I picked. Meet Brenda!", 0.15),
    # S2 AÇIK DÖNGÜ + ZERO-OY KABULÜ — "Was he right?" bölüm sonuna kadar açık kalır
    ("J01", "S2", "JAKE", "Was he right? Brenda has two flat tires.", 0.0),
    ("M02", "S2", "MIKE", "Brenda couldn't wait!", 0.0),
    ("J03", "S2", "JAKE", "Next time, you decide. Please.", 0.0),
    # S3 BEDEL — BANK 100 → 40, seri numarası rutini
    ("J04", "S3", "JAKE", "Sixty dollars. Did you haggle?", 0.3),
    ("M03", "S3", "MIKE", "He seemed nice.", 0.0),
    ("J05", "S3", "JAKE", "So, no.", 0.0),
    ("J06", "S3", "JAKE", "I checked the serial number, though. Not stolen.", 0.0),
    ("M04", "S3", "MIKE", "See? Brenda's innocent.", 0.0),
    # S4 HATA — pompa, patlama; BANK 40 → 24
    ("M05", "S4", "MIKE", "Now we pump her up. Air is free. Easy money!", 0.3),
    ("J07", "S4", "JAKE", "Air is free. Tubes are not.", 1.0),
    ("J08", "S4", "JAKE", "Both tubes are torn. New ones are eight bucks each.", 0.0),
    ("M06", "S4", "MIKE", "Sixteen dollars for rubber donuts?", 0.0),
    ("J09", "S4", "JAKE", "Tires aren't free. I did say that.", 0.0),
    # S5 İLAN — tahta hesabı
    ("M07", "S5", "MIKE", "Okay, Brenda rides! I'm listing her for a hundred and forty.", 0.4),
    ("J10", "S5", "JAKE", "She cost us seventy-six. So, sixty-four profit. If she sells.", 0.0),
    ("M08", "S5", "MIKE", "Oh, she sells. A guy already wrote back. On my way!", 0.0),
    # S6 GELMEYEN ALICI — L3 garaj yolu (G2), saat kartı 2:00 PM → 2:45 PM
    ("J11", "S6", "JAKE", "He's not on his way.", 1.0),
    ("M09", "S6", "MIKE", "Maybe traffic?", 0.0),
    ("J12", "S6", "JAKE", "Forty-five minutes of traffic?", 0.0),
    ("M10", "S6", "MIKE", "He says, sorry, found one cheaper. Brenda deserved better.", 0.6),
    # S7 YENİ İKİLEM — telefon "ding", yeni teklif
    ("M11", "S7", "MIKE", "Wait. New message. Ninety bucks, cash, today.", 0.6),
    ("J13", "S7", "JAKE", "Ninety is still fourteen profit. Fast. And safe.", 0.0),
    ("M12", "S7", "MIKE", "Fourteen? She's worth a hundred and forty! We wait. Trust the vibe.", 0.0),
    ("J14", "S7", "JAKE", "And if the next guy doesn't show either?", 0.0),
    ("M13", "S7", "MIKE", "Then we counter. Meet him at a hundred and fifteen.", 0.0),
    ("J15", "S7", "JAKE", "And maybe he walks. Then Brenda lives here.", 0.0),
    # S8 SEÇİM ANI — ikisi kameraya; soruyu Mike sorar, Jake bitirir
    ("B01", "S8", "MIKE", "Take the ninety, hold out, or counter?", 0.8),
    ("B02", "S8", "JAKE", "Tell us in the comments.", 0.0),
]
# Sahne sonu sessiz tutuşlar (sn): seçim kartı + "Ep. 3: YOUR call" kartı
SON_TUTUS = {"S8": 3.0}
# BANK zinciri (gösterilen her işlem): (satır id, tutar)
BANK_BAS = 100
ISLEMLER = [("J04", -60), ("J08", -16)]
BANK_SON = 24
