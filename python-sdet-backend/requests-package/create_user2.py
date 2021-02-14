# External user dictionary
import requests
from payload import *


# resp = requests.post("https://reqres.in/api/users", data=addUserPayload())
resp = requests.post("https://reqres.in/api/users", json=addUserPayload())
print(resp.status_code)
print(resp.json())
assert resp.json()['job'] == "developer"

