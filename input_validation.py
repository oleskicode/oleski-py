while True:
    try:
        a = input("Input number a = ")
        a = float(a)
        break
    except ValueError:
        print("Not a number")

while True:
    try:
        b = input("Input number b = ")
        b = float(b)
        break
    except ValueError:
        print("Not a number")

print(f"a + b = {a + b}")

# a little bit better way
def input_number(prompt):
    while True:
        try:
            num = float(input(prompt))
            return num
        except ValueError:
            print("Not a number")

c = input_number("c = ")
d = input_number("d = ")
print(f"c + d = {c + d}")
