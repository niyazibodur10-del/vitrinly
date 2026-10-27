#!/usr/bin/env python3
"""viralite-analisti: duyarlılık testi (model v0.1, tools/viralite.py hesabını kullanır, ağırlıkları kalıcı değiştirmez).

1) Ağırlık testi: her ölçüt çiftinde 0.05 bir ölçütten alınıp diğerine verilir (toplam 1.00 korunur; 8x7 = 56 durum).
   Her durumda ilk 3 (küme ve sıra) temel sonuçla karşılaştırılır.
2) Puan aralığı testi: girdideki `aralik_kotumser_iyimser` ile her senaryonun kötümser / iyimser nihai puanı.
3) Tek senaryo kötümser, diğerleri iyimser (en sert çapraz test): ilk 3 kümesi değişiyor mu?

Kullanım: python3 viralite-duyarlilik.py viralite-girdi.json
"""
import json
import os
import sys
from decimal import Decimal

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "..", "tools"))
import viralite as v  # noqa: E402

ADIM = Decimal("0.05")
ESIK = Decimal("0.3")


def sirala(senaryolar):
    return [r for r in v.sirala([v.puanla(s) for s in senaryolar]) if not r["elendi"]]


def ilk3(senaryolar):
    return [r["id"] for r in sirala(senaryolar)[:3]]


def main(yol):
    senaryolar = v.oku(yol)
    temel_sira = sirala(senaryolar)
    temel = [r["id"] for r in temel_sira[:3]]
    print(f"Temel ilk 3: {temel}  (model {v.MODEL_SURUMU}, ağırlık toplamı {sum(v.AGIRLIK.values())})")
    puan = {r["id"]: r["nihai"] for r in temel_sira}
    fark = [(temel_sira[i]["id"], temel_sira[i + 1]["id"], temel_sira[i]["nihai"] - temel_sira[i + 1]["nihai"]) for i in range(4)]
    for a, b, f in fark:
        print(f"  {a} − {b} = {f}  {'(anlamlı değil, <0.3)' if f < ESIK else ''}")

    # 1) ağırlık testi
    orijinal = dict(v.AGIRLIK)
    anahtarlar = list(orijinal)
    kume_degisen, sira_degisen, toplam = [], 0, 0
    for a in anahtarlar:
        for b in anahtarlar:
            if a == b:
                continue
            v.AGIRLIK.update(orijinal)
            v.AGIRLIK[a] = orijinal[a] - ADIM
            v.AGIRLIK[b] = orijinal[b] + ADIM
            assert sum(v.AGIRLIK.values()) == Decimal("1.00")
            sonuc = ilk3(senaryolar)
            toplam += 1
            if set(sonuc) != set(temel):
                kume_degisen.append((a, b, sonuc))
            elif sonuc != temel:
                sira_degisen += 1
    v.AGIRLIK.update(orijinal)
    assert sum(v.AGIRLIK.values()) == Decimal("1.00")
    print(f"\n1) Ağırlık ±{ADIM} testi: {toplam} durum | ilk 3 KÜMESİ değişen: {len(kume_degisen)} | yalnız sırası değişen: {sira_degisen}")
    for a, b, s in kume_degisen:
        print(f"  {a} −{ADIM} → {b} +{ADIM}: ilk 3 = {s}")

    # 2) aralık testi
    def varyant(s, uc):
        d = dict(s)
        for k, (lo, hi) in s.get("aralik_kotumser_iyimser", {}).items():
            d[k] = lo if uc == "kotumser" else hi
        return d

    print("\n2) Puan aralığı (kötümser / temel / iyimser nihai):")
    kot = {r["id"]: r["nihai"] for r in sirala([varyant(s, "kotumser") for s in senaryolar])}
    iyi = {r["id"]: r["nihai"] for r in sirala([varyant(s, "iyimser") for s in senaryolar])}
    for r in temel_sira:
        i = r["id"]
        print(f"  {i}: {kot[i]} / {puan[i]} / {iyi[i]}")

    # 3) çapraz test: bir senaryo kötümser, diğerleri iyimser
    print("\n3) Çapraz test (hedef kötümser, diğer hepsi iyimser) — ilk 3'teki her senaryo için:")
    for hedef in temel:
        karisik = [varyant(s, "kotumser" if s["id"] == hedef else "iyimser") for s in senaryolar]
        s3 = ilk3(karisik)
        print(f"  {hedef} kötümser → ilk 3 = {s3}  {'(KÜME DEĞİŞTİ)' if set(s3) != set(temel) else '(küme aynı)'}")

    kirilgan = bool(kume_degisen)
    print(f"\nSONUÇ: ağırlık testine göre sıralama {'KIRILGAN' if kirilgan else 'SAĞLAM'} "
          f"(kural: ±0.05 ağırlıkta ilk 3 kümesi değişirse kırılgan).")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1]))
