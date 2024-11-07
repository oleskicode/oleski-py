list1 = [1, 2, 3, 4, "A", "B", "C"]
# string1 = "".join(str(list1)) # incorrect
string1 = "".join(str(item) for item in list1)
print(f"string1 : {string1}")

list2 = ["A", "B", "C"]
string2 = "".join(list2)
print(f"string2 : {string2}")
