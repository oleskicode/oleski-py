# Function to split a string and convert it into an array of words.
# print(string_to_array("Robin Hood"));
# ["Robin", "Hood"]


def string_to_array(input_string: str) -> list[str]:
    # print(type(input_string.split()))
    return input_string.split()


print(string_to_array("Robin Hood"))
