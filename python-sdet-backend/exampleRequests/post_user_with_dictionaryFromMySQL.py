# External user dictionary
import requests
from payload1 import *

query = "SELECT * FROM User"
payload = buildPayloadFromMySQL(query)
print(type(payload))

# Passing external dictionary to data attribute
# resp = requests.post("https://reqres.in/api/users", data=payload)
# print(resp.status_code)
# print(resp.json())


# Passing external dictionary to json attribute directly, it will encode automatically
resp = requests.post("https://reqres.in/api/users", json=payload)
print(resp.status_code)
print(resp.json())
