some_string = "abc"
print(id(some_string)) # someid1
some_string = some_string + "d"
print(id(some_string)) # DIFFERENT value
