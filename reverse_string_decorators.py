user_input_string = input("String to reverse:")
# user_input_string = "abCdEz"

def print_decorator(func):
    def wrapper(*args, **kwargs):
        print(f"\nFunction is: {func}")
        func(*args, **kwargs)
        print(f"End of function {func} \n")
    return wrapper

@print_decorator
def pro_reverse_string(input_string):
    print(input_string[::-1])
    return(input_string[::-1])

@print_decorator
def noob_reverse_string(input_string):
    list_of_chars = list(input_string) #string to list
    reversed_list = []
    for char in list_of_chars[::-1]:
        # print(char, end='')
        reversed_list.append(char)
    reversed_string = "".join(reversed_list) #list to string
    print(reversed_string)
    return(reversed_string)

print(pro_reverse_string(user_input_string))
print(noob_reverse_string(user_input_string))
