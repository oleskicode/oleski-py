fruits = ["apple", "banana", "coconut", "donut"]


def capitalize_each_word_in_list(input_list: list) -> list:
    capitalized_list = [item.capitalize() for item in input_list]
    return capitalized_list


print(capitalize_each_word_in_list(fruits))
