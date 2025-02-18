# Camelize String function to convert a string into camel case.
# print(camelize("some Exercises"));
# print(camelize("some more exercise"));


def camelize(string: str) -> str:
    splitted = string.split(" ")
    # print(splitted)
    splitted[0] = splitted[0].lower()
    for i in range(1, len(splitted)):
        splitted[i] = splitted[i].capitalize()
    return "".join(splitted)

print(camelize("some Exercise"))
print(camelize("some more Exercise"))
