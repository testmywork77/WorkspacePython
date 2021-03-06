import requests
import json

f = open("./demosRequests/user.json", "r").read()
resp = requests.post("https://reqres.in/api/users", json=json.loads(f))
print(resp.status_code)
print(resp.json())
print(resp.headers.get("Content-Type"))
assert resp.json()['job'] == "Tech Lead"

