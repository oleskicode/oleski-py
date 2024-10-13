try:
    x = float(input("Enter x = "))
    y = float(input("Enter y = "))
    result = x / y
except ValueError as e:
    print(e)
    print("Not a numer")
except ZeroDivisionError as e:
    print(e)
    print("Error - Division by zero")
else:
    print(f"x / y = {result}")
finally:
    print("--- Finally part is always executed. ---")
