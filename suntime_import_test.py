from colorama import Fore, Back
from suntime import Sun, SunTimeException  # pip3 install suntime

city_name = "Lviv"
city_lat = 49.83
city_lon = 23.98

sun = Sun(city_lat, city_lon)

# Get today's sunrise and sunset in UTC
today_sr = sun.get_sunrise_time()
today_ss = sun.get_sunset_time()
print(f"Today in {city_name}:")
print(Fore.YELLOW + Back.BLACK + f"sunrise time: {today_sr} UTC")
print(Fore.BLUE + Back.BLACK + f"sunset  time: {today_ss} UTC")
