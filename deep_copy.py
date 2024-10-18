from copy import deepcopy


def is_equal_is(list_1, list_2):
    print(f"List A: {list_1}")
    print(f"List B: {list_2}")
    print(f"A == B: {list_1 == list_2}")
    print(f"A is B: {list_1 is list_2}")


original_list = [[1, 1], [2, 2], [3, 3]]

shallow_copy_list = original_list  # Shallow copy
deep_copy_list = deepcopy(original_list)  # Deep copy

is_equal_is(original_list, shallow_copy_list)
is_equal_is(original_list, deep_copy_list)
