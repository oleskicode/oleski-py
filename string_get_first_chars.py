def truncate_string(input_string: str, length: int) -> str:
    """Extract a specified number of characters from first element."""
    return input_string[:length]


print(truncate_string("Robin Hood", 4))  # "Robi"
print(truncate_string("Hi", length=1))
