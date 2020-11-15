import requests
import json

response = requests.get('http://localhost:3000/employees')
# print(response.text)
print(type(response.text))

# deserialize to python object
result = json.loads(response.text)
print(type(result))
print(result[1])
print(result[1]["name"])
