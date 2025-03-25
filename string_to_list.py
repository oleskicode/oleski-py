def string_to_array(input_string: str) -> list[str]:
    """Function to split a string and convert it into an array of words."""
    # print(type(input_string.split()))
    return input_string.split()


print(string_to_array.__doc__)
print(string_to_array("I am Robin Hood"))
