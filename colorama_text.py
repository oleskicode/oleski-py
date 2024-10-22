from colorama import Fore, Back

with open("colorama_text.txt") as f:
    readfile = f.read()
    print(readfile)

readfile = readfile.split()
print(readfile)

for array_item in readfile:
    print(array_item, end="")

# Text to Colored Text Transformer
print("\nColored string:")
for array_item in readfile:
    if array_item == "G":
        print(Back.GREEN + Fore.YELLOW + "T ", end="")
    if array_item == "B":
        print(Back.BLUE + Fore.YELLOW + "3 ", end="")
    if array_item == "Y":
        print(Back.LIGHTYELLOW_EX + Fore.CYAN + "s ", end="")
    if array_item == "R":
        print(Back.RED + Fore.CYAN + "s ", end="")
    if array_item == "\n":
        print("EOL")
