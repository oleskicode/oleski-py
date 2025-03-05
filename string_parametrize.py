# Function to parametrize a string.
# Test Data : print(string_parametrize("Robin Hood from England."));
# "robin-hood-from-england"


def string_parametrize(input_string: str) -> str:
    input_split = input_string.lower().split(" ")
    print(input_split)
    return "-".join(input_split)


print(string_parametrize("Robin Hood from England"))
