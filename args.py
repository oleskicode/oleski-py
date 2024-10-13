def add_numbers(*args):
    sum = 0
    for number in args:
        sum += number
    print(sum)


add_numbers()
add_numbers(1)
add_numbers(1, 2)
add_numbers(1, 2, 3)
add_numbers(1, 2, 3, 4)
