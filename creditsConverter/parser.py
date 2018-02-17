import re
from romans import RomanNumber, RomanLiteral

class ParserResponse(object):
    def __init__(self, ok = False, text = "", value = -1, unit = ""):
        self.ok = ok
        self.text = text
        self.value = value
        self.unit = unit

class Parser(object):
    translate_dictionary = {}
    metals_values = {}

    def __init__(self):
        self.local_dictionary = {
            "I" : RomanLiteral("I", 1, 1, True, True),
            "V" : RomanLiteral("V", 5, 2, False, False),
            "X" : RomanLiteral("X", 10, 2, True, True),
            "L" : RomanLiteral("L", 50, 3, False, False),
            "C" : RomanLiteral("C", 100, 3, True, True),
            "D" : RomanLiteral("D", 500, 4, False, False),
            "M" : RomanLiteral("M", 1000, 4, True, False)
        }

    def parse_instruction(self, text):

        #how many credits
        matchObj = re.match( r'^how many Credits is (.*) \?$', text)
        if matchObj:
            words = matchObj.group(1).split(" ")
            metal = words[-1]
            translated_number = self.translate_intergalactic_to_roman(" ".join(words[:len(words) - 1]))
            total_credits = int(translated_number.convert() * self.metals_values[metal])

            return ParserResponse(True, matchObj.group(1) + " is " + str(total_credits) + " Credits", total_credits, "Credits")

        #sets the metal value
        matchObj = re.match( r'(.*) is (.*) Credits$', text)
        if matchObj:
            words = matchObj.group(1).split(" ")
            metal = words[-1]

            translated_number = self.translate_intergalactic_to_roman(" ".join(words[:len(words) - 1]))
            self.metals_values[metal] = float(matchObj.group(2))/translated_number.convert()
            return ParserResponse(True)
        #ho much is..
        matchObj = re.match( r'^how much is (.*) \?$', text)
        if matchObj:
            translated_number = self.translate_intergalactic_to_roman(matchObj.group(1))
            converted_number = int(translated_number.convert())
            return ParserResponse(True, matchObj.group(1) + " is " + str(converted_number), converted_number)

        #sets the roman translation
        matchObj = re.match( r'(.*) is (.*)', text)
        if matchObj:
            if matchObj.group(2) in self.local_dictionary:
                self.translate_dictionary[matchObj.group(1)] = self.local_dictionary[matchObj.group(2)]
                return ParserResponse(True)
            else:
                raise ValueError("Key is not a roman number")

        return ParserResponse(False, "I have no idea what you are talking about")

    def translate_intergalactic_to_roman(self, text):
        roman_number = RomanNumber()
        intergalactic_splited = text.split(" ")
        for number in intergalactic_splited:
            if number in self.translate_dictionary:
                roman_number.append(self.translate_dictionary[number])
            else:
                raise ValueError(number + " key is not a translatable number")
        return roman_number
