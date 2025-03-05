# Convert string camelCase format to snake_case: getRandomColor > get_random_color

def convert_to_snake_case(input_string):
    # print(input_string)
    input_list = list(input_string)
    output_list = []
    for char in input_list:
        if char.isupper():
            output_list.append("_")
            output_list.append(char.lower())
        else:
            output_list.append(char)
    return "".join(output_list)

print(convert_to_snake_case("getRandomColor"))
print(convert_to_snake_case("getSomeRandomNumber"))
