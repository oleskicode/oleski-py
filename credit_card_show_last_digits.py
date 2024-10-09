card_number1 = "0123 1234 1234 5678"
card_number2 = "0123 1234 1234 9291"

def show_only_last_four_noob(card_number):
    print(card_number)
    input_string_length = len(card_number)
    # print(input_string_length)
    output_string = ""
    for x in range(input_string_length - 4):
        if x % 5 == 4:
            output_string += " "
        else:
            output_string += "*"
    for i in range(4,0,-1):
        output_string += card_number[input_string_length-i]
    print(output_string)

def show_only_last_four_pro(card_number):
    print(card_number)
    last_four_numbers = card_number[-4::]  # Slicing the last 4 characters
    print("**** **** **** " + last_four_numbers)

show_only_last_four_noob(card_number1)
show_only_last_four_noob(card_number2)

show_only_last_four_pro(card_number1)
show_only_last_four_pro(card_number2)