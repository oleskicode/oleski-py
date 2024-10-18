class DictFromLists:
    dict = {}

    def __init__(self, keys, values):
        self.dict = dict(zip(keys, values))

    def __str__(self):
        return str(self.dict)


list1 = ["one", "two", "three", "four"]
list2 = [1, 2, 3, 4]

dicti1 = DictFromLists(list1, list2)
print(dicti1)
