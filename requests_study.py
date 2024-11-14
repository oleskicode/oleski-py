import requests

site_url = "https://jsonplaceholder.typicode.com/posts"

#GET
response_get = requests.get(site_url+"/1")
print(response_get.text)
print(response_get.json)
print(f'response_get.json()["title"] : {response_get.json()["title"]}')
print(response_get.headers)
for header, value in response_get.headers.items(): #iteration using .items
    print(f"header: {header}    value: {value}")

#POST
headers_post = {
    "Content-Type":"application/json; charset=utf-8"
}
body_post = {
    "userId": 182,
    "title":"TitleTom",
    "body":"DeBody"
}
response_post = requests.post(url=site_url, json=body_post, headers=headers_post)
print(response_post.status_code, response_post.reason)
print(response_post.text)

#PUT
data_put = {
    "title":"test_put"
}
response_put = requests.put(url=site_url + "/1", data = data_put)
print(response_put.status_code, response_put.reason)
print(response_put.text)

#PATCH
data_patch = {
    "title" : "test_patch"
}
response_patch = requests.patch(url=site_url + "/1", data = data_patch)
print(response_patch.status_code, response_patch.reason)
print(response_patch.text)
response_get = requests.get(site_url+"/1")
print(response_get.text)

#DELETE
response_delete = requests.delete(url=site_url + "/1")
print(response_delete.status_code, response_delete.reason)
print(response_delete.text)
