# Create a dictionary that contains information about countries and their capitals.
# Ask the user for the name of a country and output the capital of that country (if item exists in the dictionary).

country_capitals = {"Italy": "Rome", "Ukraine": "Kyiv", "France": "Paris"}

print(country_capitals)

country = input("Country name:")
country = country.capitalize()
# print(country)

if country in country_capitals.keys():
    print(country_capitals[str(country)])
