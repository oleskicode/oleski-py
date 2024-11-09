def calc_add(a, b):
    return a+b

def calc_multiply(a,b):
    return a*b

def calc_average(*args):
    print(f"args: {args}")
    args_sum = 0
    count = len(args)
    print(f"args count: {count}")
    for arg in args:
        args_sum += arg
    print(f"Average: {args_sum/count}")
    return args_sum/count

def find_max(*args):
    print(f"args: {args}")
    print(f"max value: {max(args)}")
    return max(args)
