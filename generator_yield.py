def my_generator():
    print("First part")
    yield 1
    print("After first yield")
    yield 2
    print("After second yield")
    yield 3


gen = my_generator()

print(next(gen))  # Outputs 1, prints "First part"
print(next(gen))  # Outputs 2, prints "After first yield"
print(next(gen))  # Outputs 3, prints "After second yield"
