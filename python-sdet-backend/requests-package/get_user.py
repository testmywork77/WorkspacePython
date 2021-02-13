import requests


p = {"page": 2}
# resp = requests.get("https://reqres.in/api/users?page=2")
resp = requests.get("https://reqres.in/api/users", params=p)
print(resp.url)
statusCode = resp.status_code
assert statusCode == 200, "response code doesn't match"
response_json = resp.json()
print(response_json["total"])
assert response_json["total"] == 12
print(response_json["data"][0]["email"])
assert response_json["data"][0]["email"] == "michael.lawson@reqres.in"
assert (response_json["data"][0]["email"]).endswith("reqres.in")
assert response_json["data"][2]["last_name"]!= None


"""

print(resp)  # print response
print(type(resp))  # print type of resp object
print(dir(resp))  # print metadata of resp object

print(resp.text)  # response in plain string format
print(resp.content)  # response , bytes format
print(resp.json())  # response in json serialized format

print(resp.headers)
print(resp.cookies)
print(resp.encoding)
print(resp.url)

"""

