# Function to extract a specified number of characters from a string from first element.
# print(truncate_string("Robin Hood", 4)) # Output: "Robi"

def truncate_string(input_string :str, length :int) -> str:
    return input_string[:length]

print(truncate_string("Robin Hood", 4))
print(truncate_string("Hi", length=1))