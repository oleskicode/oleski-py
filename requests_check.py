import requests

base_url = "https://api.stackexchange.com"
print(base_url)

response = requests.get(
    base_url + "/2.3/questions?order=desc&sort=activity&site=stackoverflow"
)
print(f"Status Code: {response.status_code} \n")

print(f"response.headers ${response.headers} \n")
for key_header, value_header in response.headers.items():
    print(f"{key_header}: {value_header}")

with open("response.json", "w") as file:
    file.write(str(response.json()))

# print(type(response))
# print(type(response.headers))
# print(type(response.json()))
# print(type(response.json()['items']))
# print(type(response.connection))
# print(type(response.status_code))

for item in response.json()["items"]:
    print(item["title"])
    print(item["link"])
