import requests

url = 'http://localhost:3000/employees'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
response = requests.get(url, headers=headers)
json_response = response.json()
print(json_response)
print(type(json_response))  # list
print(json_response[0])
# print(json_response[0]["name"])
# print(response.status_code)
assert response.status_code == 200
# print(response.headers)
assert response.headers["content-type"] == 'application/json; charset=utf-8'

