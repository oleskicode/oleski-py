list1 = ["one", "two", "three", "four", "five"]
list2 = [1, 2, 3, 4, 5, 6, 7]

zipped = zip(list1, list2)

print(zipped)
print(set(zip(zipped)))
print(dict(zip(list1, list2)))
