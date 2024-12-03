def add_num(a, b):
    return a + b


def minus_num(a, b):
    return a - b


a = float(input("a = "))
b = float(input("b = "))
operator = input("Operator:")

dict1 = {"+": add_num, "-": minus_num}

if operator in dict1:
    # print(f"valid operator {operator}")
    result = dict1[operator](a, b)
    print(result)
else:
    print(f"Valid operators are: {" ".join(dict1.keys())}")
