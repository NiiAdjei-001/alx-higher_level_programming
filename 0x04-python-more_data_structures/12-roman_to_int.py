#!/usr/bin/python3
def roman_to_int(roman_string):
    rdic = dict(
            [
                ('I', 1),
                ('V', 5),
                ('X', 10),
                ('L', 50),
                ('C', 100),
                ('D', 500),
                ('M', 1000)
            ]
    )
    val = 0
    if len(roman_string) != 1:
        for i in range(0, len(roman_string)):
            if roman_string == "None":
                return 0
            if roman_string[i] not in rdic:
                return 0
            if i == len(roman_string) - 1:
                if rdic[roman_string[i]] <= rdic[roman_string[i - 1]]:
                    val += rdic[roman_string[i]]
                    break
                else:
                    break
            if rdic[roman_string[i]] < rdic[roman_string[i + 1]]:
                val += rdic[roman_string[i + 1]] - rdic[roman_string[i]]
            else:
                val += rdic[roman_string[i]]
    else:
        val += rdic[roman_string[0]]
    return val
