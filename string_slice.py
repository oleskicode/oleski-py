"""
Slice strings from the char (excluding) to the end:
slice_string("apple", "a") >> "pple"
slice_string("carrot", "a") >> "rrot"
slice_string("abcdefg", "c") >> "defg"
"sunday".index("a") == 4
"""


def slice_string(input_string, char):
    print(f"Slice {input_string} from {char}:")
    slice_index = input_string.index(char)
    print(input_string[slice_index + 1 :])


def slice_string2(input_string, char):
    print(f"Slice {input_string} from {char}:")
    print(input_string[input_string.index(char) + 1 : :])


slice_string("apple", "a")
slice_string("banana", "a")
slice_string("coconut", "c")

slice_string2("apple", "a")
slice_string2("banana", "a")
slice_string2("coconut", "c")
