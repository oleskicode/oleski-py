user_input_string = input("Input snake_case_string:")
# user_input_string = "snake_case_string_here"


def snake_to_camel_case(input_string: str) -> str:
    print(input_string)
    input_list = list(input_string)  # String to List
    print(input_list)
    output_list = []
    capitalize_next_char = False
    for char in input_list:
        if char == "_":
            capitalize_next_char = True
        elif capitalize_next_char:
            # print(char.capitalize())
            output_list.append(char.capitalize())
            capitalize_next_char = False
        else:
            output_list.append(char)
            capitalize_next_char = False
    print(output_list)
    # print("".join(output_list))  # List to String
    return "".join(output_list)


print(snake_to_camel_case(user_input_string))
