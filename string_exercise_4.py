# Capitalize Each Word. Function to capitalize the first letter of each word in a string.
def capitalize_words(string: str) -> str:
    list1 = string.split()
    capitalized_list = [item.capitalize() for item in list1 ]
    return " ".join(capitalized_list)


print(capitalize_words('lets Capitalize Every word'))