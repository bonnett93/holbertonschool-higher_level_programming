#!/usr/bin/python3
def roman_to_int(roman_string):
    integer = 0
    if type(roman_string) == str:
        one = ['V', 'X']
        ten = ['L', 'C']
        hun = ['D', 'M']
        romans = {"I": 1, "V": 5, "X": 10, "L": 50,
                  "C": 100, "D": 500, "M": 1000}
        for i in range(len(roman_string) - 1):
            if roman_string[i] == 'I':
                if roman_string[i + 1] in one:
                    integer -= 1
                else:
                    integer += 1
            elif roman_string[i] == 'X':
                if roman_string[i + 1] in ten:
                    integer -= 10
                else:
                    integer += 10
            elif roman_string[i] == 'C':
                if roman_string[i + 1] in hun:
                    integer -= 100
                else:
                    integer += 100
            else:
                integer += romans[roman_string[i]]
        integer += romans[roman_string[-1]]
        return integer
