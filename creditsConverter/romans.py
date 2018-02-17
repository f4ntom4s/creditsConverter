import sys

class RomanLiteral( object ):
    value = 0
    name = ''
    level = 0

    def __init__(self, name, value, level = 0, repeatable = False, restable = False):
        self.value = value
        self.name = name
        self.level = level
        self.repeatable = repeatable
        self.restable = restable

    def __lt__(self, other):
        return self.value < other.value
    def __le__(self, other):
        return self.value <= other.value
    def __gt__(self, other):
        return self.value > other.value
    def __ge__(self, other):
        return self.value >= other.value
    def __eq__(self, other):
        return self.value == other.value


class RomanNumber(object):
    roman_number = []
    translation = ""
    def __init__(self):
        self.roman_number = []
        self.translation = ""

    def append(self, number):
        self.roman_number.append(number)
        self.translation += number.name
    def to_string(self):
        return self.translation

    def convert(self):
        previous = RomanLiteral("None", 0)
        previous_count = 0
        result = 0
        rests_in_current_level = False
        current_level = self.roman_number[-1].level

        #start to read the roman number backwards or throws exception
        for roman in reversed(self.roman_number):
            #check if the literal is repeatable
            if previous == roman:
                if not roman.repeatable:
                    raise ValueError("Wrong roman number format")
                previous_count += 1
            else:
                if roman < previous and previous_count > 0:
                    raise ValueError("Wrong roman number format"    )
                previous_count = 0
            #if it repeatable check the count of repeats
            if previous_count >= 3:
                raise ValueError("Wrong roman number format")
            #if it equal or more than the current number and in the same level, it can be summed
            if roman >= previous:
                if current_level < roman.level:
                    rests_in_current_level = False
                current_level = roman.level
                result += roman.value
            else:
                #else it is rested but with some conditions, must not be more rests in
                #the current level and mus be of the same level
                if current_level - roman.level == 1 and not rests_in_current_level:
                    result -= roman.value
                    rests_in_current_level = True
                else:
                    raise ValueError("Wrong roman number format")
            previous = roman
        return result
