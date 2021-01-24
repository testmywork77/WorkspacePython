# Post request by json as Payload
import requests

url = 'http://localhost:3000/students'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}

response = requests.post(url, json={
    "id": 5,
    "name": "name5",
    "email": "name5@gmail.com",
    "programme": "programme5",
    "languages": [
        "lang1",
        "lang2"
    ]
}, headers=headers)

if response.status_code == 201:
    assert response.status_code == 201
    print("Student added")
    print(response.json())
elif response.status_code == 500:
    assert response.status_code == 500
    print("Error: Insert failed, duplicate id")


