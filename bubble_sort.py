numbers = [77, 5, 4, 200, 15, 7, 0, 3, 2, 99]


def bubble_sort(numbers_input):
    input_length = len(numbers_input)
    for l in range(input_length - 1):
        for i in range(input_length - 1):
            if numbers_input[i] > numbers_input[i + 1]:
                numbers_input[i], numbers_input[i + 1] = (
                    numbers_input[i + 1],
                    numbers_input[i],
                )
    print(numbers_input)


bubble_sort(numbers)
