# Filter list to include names which have "a"


def filter_list_with_symbol(input_list: list, symbol: str) -> list:
    def check_symbol_in_string(string1: str):
        return symbol.lower() in string1.lower()

    return list(filter(check_symbol_in_string, input_list))


print(filter_list_with_symbol(["Anne", "Bob", "Carol", "Danny"], "a"))
print(filter_list_with_symbol(["Anne", "Bob", "Carol", "Danny"], "b"))
print(filter_list_with_symbol(["Anne", "Bob", "Carol", "Danny"], "c"))
