user_input_string = input("Input snake_case_string:")
# user_input_string = "snake_case_string_here"

def snake_to_camel_case(input_string):
    print(input_string)
    input_list = list(input_string)  # String to List
    print(input_list)
    output_list = []
    nextCharNeedsToBeCapitalized = False
    for char in input_list:
        if char == "_":
            nextCharNeedsToBeCapitalized = True
        elif nextCharNeedsToBeCapitalized == True:
            # print(char.capitalize())
            output_list.append(char.capitalize())
            nextCharNeedsToBeCapitalized = False
        else:
            output_list.append(char)
            nextCharNeedsToBeCapitalized = False
    print(output_list)
    print("".join(output_list))  # List to String


snake_to_camel_case(user_input_string)
