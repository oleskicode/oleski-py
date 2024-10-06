user_input_string = input("String to reverse:")
# user_input_string = "abCdEz"


def pro_reverse_string(input_string):
    return input_string[::-1]


def noob_reverse_string(input_string):
    list_of_chars = list(input_string)  # string to list
    reversed_list = []
    for char in list_of_chars[::-1]:
        # print(char, end='')
        reversed_list.append(char)
    reversed_string = "".join(reversed_list)  # list to string
    return reversed_string


print(pro_reverse_string(user_input_string))
print(noob_reverse_string(user_input_string))
