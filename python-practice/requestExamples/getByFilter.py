import requests

# Arrange
expectedStudent = {
        "id": 4,
        "name": "name4",
        "email": "name4@gmail.com",
        "programme": "Cloud",
        "languages": [
            "AWS",
            "Azure",
            "GCP"
        ]
    }
url = 'http://localhost:3000/students'
headers = {'Content-Type': 'application/json', 'Accept': 'application/json'}


# Act
response = requests.get(url, headers=headers)
json_response = response.json()

# Assert
# Retrieve the student details with programme as 'Cloud'
for student in json_response:
    if student['programme'] == 'Cloud':
        # print(student)
        actualStudent = student
        break

assert actualStudent == expectedStudent
