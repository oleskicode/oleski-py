def common_letters(string1: str, string2: str) -> str:
    result_list = []
    string1 = string1.lower().replace(" ","")
    string2 = string2.lower().replace(" ","")

    if len(string1) >= len(string2):
        longer_list = list(string1)
        shorter_list = list(string2)
    else:
        longer_list = list(string2)
        shorter_list = list(string1)

    print(f"shorter_list: {shorter_list}")
    print(f"longer_list: {longer_list}")
    for char in shorter_list:
        # print(char)
        if char not in result_list:
            if char in longer_list:
                result_list.append(char)
    print(f"Common chars are: {result_list}")

string1 = "apple pie"
string2 = "banana pizza"

common_letters(string1, string2)