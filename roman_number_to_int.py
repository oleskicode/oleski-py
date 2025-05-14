def roman_to_int(s: str) -> int:
    converted_number = 0

    roman_dict = {
        "I":1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
    }
    s = s.upper()  # normalization
    # print(s)
    number_list = [roman_dict[char] for char in s]

    for i in range(len(number_list)-1):
        if number_list[i] < number_list[i+1]:
            number_list[i+1] = number_list[i+1] - number_list[i]
            number_list[i] = 0

    return sum(number_list)


print(roman_to_int(s="i"))
print(roman_to_int(s="II"))
print(roman_to_int(s="III"))
print(roman_to_int(s="IV"))
print(roman_to_int(s="V"))
print(roman_to_int(s="VI"))
print(roman_to_int(s="VII"))
print(roman_to_int("MCMXciv"))  # Output: 1994
