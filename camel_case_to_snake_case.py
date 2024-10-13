# Convert string in camelCase format to snake_case: getRandomColor > get_random_color

# input_string = input()
input_string = "getRandomColor"
# input_string = "getSomeRandomNumberX"


def convert_to_snake_case(input_string):
    print(input_string)
    input_list = list(input_string)
    print(input_list)
    outputlist = []
    for char in input_list:
        if char.isupper():
            outputlist.append("_")
            outputlist.append(char.lower())
        else:
            outputlist.append(char)
    print(outputlist)
    print("".join(outputlist))


convert_to_snake_case(input_string)
