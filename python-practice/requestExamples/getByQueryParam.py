import requests

# Arrange
url = 'http://localhost:3000/students'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
params = {'name': 'name1', 'programme': 'FrontEnd'}

# Act
response = requests.get(url, params=params, headers=headers)

# Assert
json_response = response.json()
print(json_response)
print(type(json_response))  # list
print(json_response[0])
# Assertions
assert response.status_code == 200
assert response.headers["content-type"] == 'application/json; charset=utf-8'
