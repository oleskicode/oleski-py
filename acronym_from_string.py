def acronym_generator(str_input: str) -> str:
    if len(str_input) == 0:
        return ""
    str_output = ""
    list1 = str_input.split()
    # print(list1)
    for item in list1:
        str_output += item[0].capitalize()
    return str_output


def acronym_gen(str_input: str) -> str:
    return "".join(word[0].capitalize() for word in str_input.split())


print(acronym_generator("Personal computer"))
print(acronym_generator("air conditioner"))
print(acronym_generator("for     your      info"))
print(acronym_generator(""))

print(acronym_gen("Personal computer"))
print(acronym_gen("air conditioner"))
print(acronym_gen("for     your      info"))
print(acronym_gen(""))
