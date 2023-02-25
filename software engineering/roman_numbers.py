import roman

# Conversion from decimal to Roman numerals
num = 1234
roman_num = roman.toRoman(num)
print(f"{num} in Roman numerals is {roman_num}")

# Conversion from Roman numerals to decimal
roman_num = 'MCCXXXIV'
decimal_num = roman.fromRoman(roman_num)
print(f"{roman_num} in decimal is {decimal_num}")
