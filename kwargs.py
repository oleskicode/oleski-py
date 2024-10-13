def print_address(**kwargs):
    for value in kwargs.values():
        print(value)
    print("-----")


print_address(city="Dilly", street="Dally 12")
print_address(street="Happy", house="Clappy 10")

user_address = {"street": "Abbey St.", "city": "Cambridge", "apartment": 10}

print_address(**user_address)  # dict must be unpacked
