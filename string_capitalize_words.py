# Capitalize Each Word. Function to capitalize the first letter of each word in a string.

def capitalize_words(string: str) -> str:
    list1 = string.split()
    capitalized_list = [item.capitalize() for item in list1 ]
    return " ".join(capitalized_list)

def capitalize_words2(input_string: str) -> str:
    input_list = input_string.split()
    for i in range(len(input_list)):
        input_list[i] = input_list[i].capitalize()
    return " ".join(input_list)


print(capitalize_words('lets Capitalize Every word'))
print(capitalize_words2('hey how are You?'))
