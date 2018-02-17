import sys
sys.path.append('../')

import unittest
from creditsConverter.parser import Parser
from creditsConverter.romans import RomanNumber, RomanLiteral

class TestParseLineMethods(unittest.TestCase):
    def test_creates_local_dictionary(self):
        p = Parser()
        self.assertTrue(p.local_dictionary["I"].value == 1)
        self.assertTrue(p.local_dictionary["V"].value == 5)
        self.assertTrue(p.local_dictionary["X"].value == 10)
        self.assertTrue(p.local_dictionary["L"].value == 50)
        self.assertTrue(p.local_dictionary["C"].value == 100)
        self.assertTrue(p.local_dictionary["D"].value == 500)
        self.assertTrue(p.local_dictionary["M"].value == 1000)

    def test_parse_instruction_roman_assignation(self):
        p = Parser()
        p.parse_instruction("glob is I")
        p.parse_instruction("prok is V")
        p.parse_instruction("pish is X")
        p.parse_instruction("tegj is L")
        self.assertTrue(p.translate_dictionary["glob"].value == 1)
        self.assertTrue(p.translate_dictionary["prok"].value == 5)
        self.assertTrue(p.translate_dictionary["pish"].value == 10)
        self.assertTrue(p.translate_dictionary["tegj"].value == 50)
        #try to assig wrong roman numbers
        with self.assertRaises(ValueError):
            p.parse_instruction("bleh is 0")
            p.parse_instruction("rome is D")

    def test_parse_instructions_how_mush(self):
        p = Parser()
        p.parse_instruction("glob is I")
        p.parse_instruction("prok is V")
        p.parse_instruction("pish is X")
        p.parse_instruction("tegj is L")
        response = p.parse_instruction("how much is pish tegj glob glob ?")
        self.assertEqual(response.value, 42)

    def test_parse_instruction_metal_value(self):
        p = Parser()
        p.parse_instruction("glob is I")
        p.parse_instruction("prok is V")
        p.parse_instruction("pish is X")
        p.parse_instruction("tegj is L")
        p.parse_instruction("glob glob Silver is 34 Credits")
        self.assertTrue("Silver" in p.metals_values)
        self.assertEqual(p.metals_values["Silver"], 17)
        p.parse_instruction("glob prok Gold is 57800 Credits")
        self.assertTrue("Gold" in p.metals_values)
        self.assertEqual(p.metals_values["Gold"], 14450)
        p.parse_instruction("pish pish Iron is 3910 Credits")
        self.assertTrue("Iron" in p.metals_values)
        self.assertEqual(p.metals_values["Iron"], 195.5)

    def test_parse_intructions_how_many_credits(self):
        p = Parser()
        p.parse_instruction("glob is I")
        p.parse_instruction("prok is V")
        p.parse_instruction("pish is X")
        p.parse_instruction("tegj is L")
        p.parse_instruction("glob glob Silver is 34 Credits")
        p.parse_instruction("glob prok Gold is 57800 Credits")
        p.parse_instruction("pish pish Iron is 3910 Credits")
        response = p.parse_instruction("how many Credits is glob prok Silver ?")
        self.assertEqual(response.value, 68)
        response = p.parse_instruction("how many Credits is glob prok Gold ?")
        self.assertEqual(response.value, 57800)
        response = p.parse_instruction("how many Credits is glob prok Iron ?")
        self.assertEqual(response.value, 782)

    def test_parse_instructions_confusing_question(self):
        p = Parser()
        p.parse_instruction("glob is I")
        p.parse_instruction("prok is V")
        p.parse_instruction("pish is X")
        p.parse_instruction("tegj is L")
        p.parse_instruction("glob glob Silver is 34 Credits")
        p.parse_instruction("glob prok Gold is 57800 Credits")
        p.parse_instruction("pish pish Iron is 3910 Credits")

        response = p.parse_instruction("how much wood could a woodchuck chuck if a woodchuck could chuck wood ?")
        self.assertFalse(response.ok)

    def test_roman_convert_rules(self):
        r = RomanNumber()

        roman_i = RomanLiteral("I", 1, 1, True, True)
        roman_v = RomanLiteral("V", 5, 2, False, False)
        roman_x = RomanLiteral("X", 10, 2, False, False)
        roman_l = RomanLiteral("L", 50, 3, False, False)

        #Wrong cases
        #you can have only 3 repetitions
        r.append(roman_i)
        r.append(roman_i)
        r.append(roman_i)
        r.append(roman_i)
        with self.assertRaises(ValueError):
            r.convert()

        #you can rest only numers of a level before
        r = RomanNumber()
        r.append(roman_i)
        r.append(roman_l)
        with self.assertRaises(ValueError):
            r.convert()

        r = RomanNumber()
        #you can rest almost one level at a time
        r.append(roman_i)
        r.append(roman_v)
        r.append(roman_x)
        with self.assertRaises(ValueError):
            r.convert()

        #XXIXIX
        r = RomanNumber()
        r.append(roman_x)
        r.append(roman_i)
        r.append(roman_x)
        r.append(roman_i)
        r.append(roman_x)
        with self.assertRaises(ValueError):
            r.convert()

        #you can rest only one time
        r = RomanNumber()
        r.append(roman_x)
        r.append(roman_x)
        r.append(roman_i)
        r.append(roman_x)
        r.append(roman_x)
        with self.assertRaises(ValueError):
            r.convert()








if __name__ == '__main__':
    unittest.main()
