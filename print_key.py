# Check whether dict item has field key "city" and print its value
person1 = {"name": "John", "age": 30, "city": "New York"}
person2 = {"name": "Bob", "age": 20}
person3 = {"city": "Paris"}
person4 = "this is a string"


def get_city_key(person: dict):
    if type(person) != dict:
        print("Incorrect input type")
        return
    if "city" in person:
        return person["city"]


print(get_city_key(person1))
print(get_city_key(person2))
print(get_city_key(person3))
print(get_city_key(person4))


def get_city_key2(person: dict):
    if type(person) != dict:
        print("Incorrect input type")
        return
    return person.get("city")


print(get_city_key2(person1))
print(get_city_key2(person2))
print(get_city_key2(person3))
print(get_city_key2(person4))
