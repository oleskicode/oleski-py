def parse_quadratic(input_string: str) -> list:
    """Parse quadratic equation in the form of input string"""
    # normalization
    input_string = input_string.lower()
    input_string = input_string.replace(" ", "")
    input_string = input_string.replace("^", "")
    # input_string = input_string.replace("=0","")

    print(input_string)

    # a
    a = input_string.split("x2")[0]
    if a == "":
        a = 1
    if a == "-":
        a = -1
    a = float(a)
    print(f"a = {a}")

    # b
    b = input_string.split("x2")[1].split("x")[0]
    if b == "+":
        b = 1
    if b == "-":
        b = -1
    b = float(b)
    print(f"b = {b}")

    # c
    c = input_string.split("x")[2].split("=")[0]
    if c == "":
        c = 0
    c = float(c)
    print(f"c = {c}")
    return [a, b, c]


print(parse_quadratic("2 X^2 + 5 X - 1= 0  "))
print(parse_quadratic("-X^2 - X + 9 = 0  "))
print(parse_quadratic("X^2 + X = 0  "))
