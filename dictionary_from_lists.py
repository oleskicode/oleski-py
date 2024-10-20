word_keys = ["Apple", "Banana", "Pine"]
definitions_values = ["Red fruit", "Yellow fruit", "Tree"]

words_definitions = {}

number_of_items = len(word_keys)
print(f"Words = ", word_keys)
print(f"Definitions = ", definitions_values)
print(f"number_of_items = ", number_of_items)

for index in range(number_of_items):
    words_definitions[word_keys[index]] = definitions_values[index]

print(words_definitions)
