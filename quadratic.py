# parse quadratic equation in the form of input string
# assume input is always valid
# solve it

def parse_quadratic_eq(input_str):
    print(input_str)
    input_str = input_str.replace(" ", "").replace("=0", "")

    a_string = input_str.split("x2")[0]
    # print(f"a_string = {a_string}")
    if a_string == "" or a_string == "1" or a_string == "+1":
        a = 1
    elif a_string == "-" or a_string == "-1":
        a = -1
    else:
        a = float(a_string)
    print(f"a = {a}")

    b_string = input_str.split("x2")[1]
    if 'x' in b_string:
        # print("b is present")
        if b_string.split("x")[0] == "-":
            b = -1
        elif b_string.split("x")[0] == "+":
            b = +1
        else:
            b = float(b_string.split("x")[0])
    else:
        # print("b is absent")
        b = 0
    print(f"b = {b}")

    c_string = input_str.split("x2")[1]
    if 'x' in c_string:
        c_string = c_string.split("x")[1]
    # print(f"c_string = {c_string}")
    if c_string == "" or c_string == "0":
        # print("c is absent")
        c = 0
    else:
        c = float(c_string)
    print(f"c = {c}")

    discriminant = b**2 - 4*a*c
    # print("D = ", discriminant)
    if discriminant < 0:
        print("D < 0. No solution.")
        return None
    if discriminant == 0:
        x = -b / (2 * a)
        print("1 solution:")
        print("x = ", x)
        return x

    x1 = (-b - discriminant**0.5) / (2 * a)
    x2 = (-b + discriminant**0.5) / (2 * a)

    print("x1 = ", x1)
    print("x2 = ", x2)
    return x1, x2


# parse_quadratic_eq("-x2=0")
# parse_quadratic_eq("x2-2x=0")
# parse_quadratic_eq("11x2-22x+33=0")
# parse_quadratic_eq("9x2-12x+4=0")
# parse_quadratic_eq("4x2+4x+1=0")
# parse_quadratic_eq("x2-5x+6=0")
parse_quadratic_eq("2x2-7x+3=0")
# parse_quadratic_eq("-x2+12x+9=0")
