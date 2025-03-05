# Count how many VOWEL characters are in the string
vowels = ["a", "A", "e", "E", "i", "I", "o", "O", "u", "U"]


def count_vowels(str_input: str) -> int:
    vowels_count = 0
    for char in str_input:
        if char in vowels:
            # print(f"{char} is a vowel")
            vowels_count += 1
    return vowels_count


print(count_vowels("xyz"))
print(count_vowels("abc"))
print(count_vowels("apple"))
