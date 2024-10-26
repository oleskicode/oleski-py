list1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

def fizzbuzz_using_print(input_list):
    for number in input_list:
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
            continue
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)

def fizzbuzz_using_yield(input_list) -> str:
    for number in input_list:
        if number % 3 ==0 and number % 5 == 0:
            yield "FizzBuzz"
        elif number % 3 ==0:
            yield "Fizz"
        elif number % 5 == 0:
            yield "Buzz"
        else:
            yield number

fizzbuzz_using_print(list1)

for number in fizzbuzz_using_yield(list1):
    print(number)
