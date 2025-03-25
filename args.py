def add_numbers(*args) -> float:
    sum_args: float = 0
    for number in args:
        sum_args += number
    print(sum_args)
    return sum_args


add_numbers()
add_numbers(1)
add_numbers(1, 2)
add_numbers(1, 2, 3)
add_numbers(1, 2, 3, 4)
