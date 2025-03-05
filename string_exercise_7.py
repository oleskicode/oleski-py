# Write function to return a new string by pairing up the characters in the corresponding locations in both sub-strings. 
# The string will always split evenly with the asterisk in the center. 
# Input: "123*abc"
# Output: 1a2b3c

def string_asterisk_task(input_str: str) -> str: 
    outputstring = ""
    input_list = input_str.split("*")
    print(input_list)
    assert(len(input_list[0])==len(input_list[1]))

    for i in range(len(input_list[0])):
        outputstring += input_list[0][i] + input_list[1][i]
    return outputstring
    
print(string_asterisk_task("aaa*bbb")) # ababab
print(string_asterisk_task(input_str="123*abc")) # 1a2b3c
