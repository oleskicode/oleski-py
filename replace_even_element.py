def replace_even_element(string1):
    list1 = list(string1)
    print(list1)
    list2 = []
    for item in list1:
        # print(list1.index(item))
        if list1.index(item) % 2 == 0:
            list2.append(item)
        else:
            list2.append("*")
    print(list2)

replace_even_element("12345678")
