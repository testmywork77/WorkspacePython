# External user dictionary
import requests
from payloads.payload import *


# Passing external dictionary to data attribute
resp = requests.post("https://reqres.in/api/users", data=userPayload())
print(resp.status_code)
print(resp.json())
assert resp.json()['job'] == "developer"

# Passing external dictionary to json attribute directly, it will encode automatically
resp = requests.post("https://reqres.in/api/users", json=userPayload())
print(resp.status_code)
print(resp.json())
assert resp.json()['job'] == "developer"
