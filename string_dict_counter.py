def str_to_dict_count(s: str) -> dict:
    """Count characters in a string"""
    result_dict = {}
    for char in s:
        if char in result_dict:
            result_dict[char] += 1
        else:
            result_dict[char] = 1
    return result_dict


print(str_to_dict_count.__doc__)
print(str_to_dict_count("apple"))
print(str_to_dict_count("banana"))
print(str_to_dict_count("coconut"))
