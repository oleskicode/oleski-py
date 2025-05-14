def dict_merge(list1: list, list2: list) -> dict:
    """Merge two lists into dict"""
    return dict(zip(list1, list2))


print(dict_merge.__doc__)
print(dict_merge([1, 2, 3], ["a", "b", "c"]))


def dict_concatenate(dict1: dict, dict2: dict) -> dict:
    """Add/concatenate two dicts"""
    return dict1 | dict2


print(dict_concatenate.__doc__)
print(
    dict_concatenate(
        dict_merge([1, 2, 3], ["a", "b", "c"]), dict_merge([4, 5], ["d", "e"])
    )
)
