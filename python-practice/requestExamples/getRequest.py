import requests
import json


url = 'http://localhost:3000/students'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
response = requests.get(url, headers=headers)
print(type(response.text))
print(response.text)
# deserialize to python object
result = json.loads(response.text)
print(type(result))
print(result[1])
print(result[1]["name"])
