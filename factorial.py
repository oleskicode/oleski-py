def factorial(input_num: int) -> int:
    """Function to calculate factorial."""
    # print(f"input_num = {input_num}")
    if input_num < 0:
        raise ValueError("Factorial function input must not be negative")
    if input_num == 0:
        return 1
    return input_num * factorial(input_num - 1)


print(factorial.__doc__)
# print(factorial(-5))
print(factorial(0))
print(factorial(1))
print(factorial(2))
print(factorial(3))
print(factorial(4))
print(factorial(5))
