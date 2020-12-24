import requests

url = 'http://localhost:3000/students/id'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}
params = {'id': 7}
response = requests.delete(url, params=params)
print(response.status_code)
