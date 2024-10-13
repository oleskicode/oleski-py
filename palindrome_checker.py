user_string = input("Type text to check if it is a palindrome:")
# user_string = "12345"
user_string2 = "A man a plan a canal Panama"
user_string3 = "234_432"


def is_palindrome_noob(input_string):
    input_string = input_string.replace(" ", "")  # remove spaces
    input_list = list(input_string.lower())  # string to list
    print(input_list)
    # print(len(input_list))
    string_middle = int(len(input_string) / 2)
    # print(string_middle)
    for i in range(string_middle):
        if input_list[i] != input_list[len(input_list) - 1 - i]:
            print(f"{input_list[i]} != {input_list[len(input_list) - 1 - i]}")
            print("Not a palindrome")
            return
    print("Is a palindrome")


def is_palindrome_pro(input_string):
    input_string = input_string.lower().replace(" ", "")
    print(input_string)
    reversed_string = input_string[::-1]
    if input_string == reversed_string:
        print("Is a palindrome")
    else:
        print("Not a palindrome")


is_palindrome_noob(user_string)
is_palindrome_noob(user_string2)
is_palindrome_noob(user_string3)

is_palindrome_pro(user_string)
is_palindrome_pro(user_string2)
is_palindrome_pro(user_string3)
