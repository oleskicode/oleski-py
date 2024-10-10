sample_dictionary = {"Oleski":1, "Code":2.0, "Dict":"Three"}

print(sample_dictionary)
print(sample_dictionary.keys())
print(sample_dictionary.values())

for key in sample_dictionary.keys(): #.keys
    print(key)

for value in sample_dictionary.values(): #.values
    print(value)

for key, value in sample_dictionary.items(): #.items = .keys + .values
    print(f"key:{key} -- value:{value}")
