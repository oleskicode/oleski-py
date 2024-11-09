ogre = {"age": 35, "name": "Shrek", "location": "swamp"}
print(ogre)

ogre["location"] = "castle"  # change value
ogre["color"] = "green"  # add new key-value

for key, value in ogre.items():  # dict is iterated using .items
    print(f"{key} -- {value}")
