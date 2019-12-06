import requests
import json

r_get = requests.get("http://httpbin.org/get")
r_post = requests.post("http://httpbin.org/post")
r_put = requests.put("http://httpbin.org/put")
r_delete = requests.delete("http://httpbin.org/delete")
r_options = requests.options("http://httpbin.org/get")

print(r_get.content)

print(r_get.json())

r_json = r_get.json()

print(r_json["headers"])

print(json.dumps(r_json["headers"], indent=4, sort_keys=True))
print(json.dumps(r_get.json(), indent=4, sort_keys=True))

"""
https://jsonplaceholder.typicode.com/posts
https://jsonplaceholder.typicode.com/users
https://jsonplaceholder.typicode.com/photos
"""


