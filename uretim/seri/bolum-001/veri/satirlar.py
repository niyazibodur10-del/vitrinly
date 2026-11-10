"""Bölüm 001 replikleri — TEK KAYNAK. metin-kontrol.py bunu okur.
(id, sahne, konuşan, replik, sessiz_vuruş_sn_önce)
konuşan: JAKE / MIKE / BOTH (iki ses aynı anda)."""
SATIRLAR = [
    # S1 KANCA — mutfak tezgâhı. 0.2 sn'de SLAM.
    ("M01", "S1", "MIKE", "That's it. Every dollar we have.", 0.4),
    ("J01", "S1", "JAKE", "Rent's paid. Fridge has mustard. That's everything.", 0.0),
    # S2 SERİ TANITIMI — buzdolabı tahtası, kameraya (≤10 sn)
    ("M02", "S2", "MIKE", "Two best friends. One hundred bucks.", 0.3),
    ("J02", "S2", "JAKE", "One slightly crazy goal.", 0.0),
    ("M03", "S2", "MIKE", "A million dollars.", 0.0),
    ("J03", "S2", "JAKE", "And we don't make the moves. You do.", 0.0),
    # S3 KURULUM — tezgâh, Mike'ın telefonu
    ("M04", "S3", "MIKE", "Okay. Three flips. Hear me out.", 0.3),
    ("J04", "S3", "JAKE", "Every bad idea starts with hear me out.", 0.0),
    ("M05", "S3", "MIKE", "And every good one!", 0.0),
    # S4 SEÇENEK 1 — bisiklet
    ("M06", "S4", "MIKE", "One. A road bike. Eighty bucks. Flat tires, but look at that frame!", 0.2),
    ("J05", "S4", "JAKE", "That's most of our money on a bike that can't roll.", 0.0),
    ("M07", "S4", "MIKE", "Air is free, Jake.", 0.0),
    ("J06", "S4", "JAKE", "Tires aren't.", 0.0),
    # S5 SEÇENEK 2 — bedava şifonyer
    ("J07", "S5", "JAKE", "Two. A solid wood dresser. Free. We paint it, flip it.", 0.3),
    ("M08", "S5", "MIKE", "Free? What's the catch?", 0.0),
    ("J08", "S5", "JAKE", "It has to go today. And we have a tiny car.", 0.0),
    ("M09", "S5", "MIKE", "So we rent a truck, buy paint, and wait. Slow.", 0.8),
    ("J09", "S5", "JAKE", "Slow. But safe.", 0.0),
    # S6 SEÇENEK 3 — kapalı kutu oyunlar
    ("M10", "S6", "MIKE", "Three. A mystery box of old video games. Forty bucks.", 0.3),
    ("J10", "S6", "JAKE", "Could be a gem. Could be forty bucks of scratched discs.", 0.0),
    ("M11", "S6", "MIKE", "That's the fun part!", 0.0),
    ("J11", "S6", "JAKE", "That's the scary part.", 0.0),
    # S7 ÇATIŞMA — ikisi aynı anda banknota uzanır
    ("M12", "S7", "MIKE", "Jake, we don't need more money. We need guts.", 1.0),
    ("J12", "S7", "JAKE", "A price tag is just a number. Value is what somebody actually pays.", 0.0),
    ("J13", "S7", "JAKE", "Fine. We let them decide.", 0.0),
    # S8 SEÇİM ANI — ikisi kameraya döner
    ("B01", "S8", "BOTH", "What should we do? Tell us in the comments.", 0.6),
]
# Sahne sonu sessiz tutuşlar (sn): seçim kartı + "Ep. 2 drops tomorrow"
SON_TUTUS = {"S8": 3.0}
