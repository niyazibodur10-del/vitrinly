#!/usr/bin/env python3
# hata-orani.py normalizasyon testleri: eşdeğer biçimler aynı kelimelere iner, farklı değerler farklı kalır
# (kapı aracı "her şeyi eşit sayarak" hatayı gizlememeli). Kullanım: python3 tools/ses/test_hata_orani.py
import importlib.util
import os
import unittest

_s = importlib.util.spec_from_file_location("ho", os.path.join(os.path.dirname(os.path.abspath(__file__)), "hata-orani.py"))
ho = importlib.util.module_from_spec(_s); _s.loader.exec_module(ho)


class Esdeger(unittest.TestCase):
    ESIT = [
        ("September 3rd", "September third"),
        ("October 28th", "October twenty-eighth"),
        ("December 11th, 1930", "December eleventh, nineteen thirty"),
        ("on January 1, 1934", "on January first, nineteen thirty four"),
        ("March 4th", "March fourth"),
        ("the 21st century", "the twenty first century"),
        ("the 2nd door", "the second door"),
        ("$1,000", "one thousand dollars"),
        ("$1,000", "1000 dollars"),
        ("$1,000", "a thousand dollars"),
        ("this $1,000 is", "this thousand dollars is"),
        ("about $500.", "about five hundred."),
        ("like $1,270.", "like twelve hundred seventy."),
        ("$1500", "1500 dollars"),
        ("$1500", "fifteen hundred dollars"),
        ("$2.5 billion", "two point five billion dollars"),
        ("about 13.5%", "about thirteen and a half percent"),
        ("in the early 1930s", "in the early nineteen thirties"),
        ("the '30s", "the thirties"),
        ("Leo's money", "Leos money"),
        ("one hundred and fifty", "150"),
        ("It's September 1929.", "it's september nineteen twenty-nine"),
    ]
    FARKLI = [
        ("third", "thirty"),
        ("$1,000", "$100"),
        ("in 1929", "in 1930"),
        ("1500 dollars", "1600 dollars"),
        ("13.5%", "13%"),
        ("March 4th", "March 14th"),
        ("the 1930s", "the 1940s"),
        ("$1,270", "$1,027"),
        ("five hundred", "five thousand"),
    ]

    def test_esit(self):
        for a, b in self.ESIT:
            with self.subTest(a=a, b=b):
                self.assertEqual(ho.norm(a), ho.norm(b))

    def test_farkli(self):
        for a, b in self.FARKLI:
            with self.subTest(a=a, b=b):
                self.assertNotEqual(ho.norm(a), ho.norm(b))

    def test_yil_bozulmadi(self):
        self.assertEqual(ho.norm("In 1929"), ["in", "nineteen", "twenty", "nine"])
        self.assertEqual(ho.norm("By 2008"), ["by", "two", "thousand", "eight"])

    def test_alt_kelime_kelime_kelime(self):
        # hizalayıcılar kelime kelime çağırır: bağlam kuralı yok, sıra sayısı var
        self.assertEqual(ho.norm_alt("$1,000"), ["one", "thousand", "dollars"])
        self.assertEqual(ho.norm_alt("3rd"), ["third"])
        self.assertEqual(ho.norm_alt("dollars."), ["dollars"])


if __name__ == "__main__":
    unittest.main(verbosity=1, warnings="ignore")
