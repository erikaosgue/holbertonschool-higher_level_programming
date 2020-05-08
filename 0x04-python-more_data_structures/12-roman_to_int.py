#!/usr/bin/python3
roman_number_map = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000,
    'IV': 4,
    'IX': 9,
    'XL': 40,
    'XC': 90,
    'CD': 400,
    'CM': 900,
}


def roman_to_int(roman_string):

    if not isinstance(roman_string, str):
        return 0

    str_len = len(roman_string)

    if str_len == 1:
        return roman_number_map[roman_string[0]]

    value = 0
    i = 0
    while i < str_len:
        # If there's at least 2 chars left
        if i < (str_len - 1):
            numerals = roman_string[i:i+2]
            if numerals in roman_number_map:
                value += roman_number_map[numerals]
                i += 2
            else:
                value += roman_number_map[roman_string[i]]
                i += 1
        else:
            value += roman_number_map[roman_string[i]]
            i += 1
    return value
