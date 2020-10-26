# GetAllStudents.py
	import requests

	url = "http://localhost:8080/student/list"

	payload = {}
	headers= {}

	response = requests.request("GET", url, headers=headers, data = payload)

	print(response.text.encode('utf8'))

# GetStudentById.py
	import requests

	url = "http://localhost:8080/student/1"

	payload = {}
	headers= {}

	response = requests.request("GET", url, headers=headers, data = payload)

	print(response.text.encode('utf8'))

# GetStudentByQueryString.py:
	import requests

	url = "http://localhost:8080/student/list?programme=Computer Science&limit=2"

	payload = {}
	headers= {}

	response = requests.request("GET", url, headers=headers, data = payload)

	print(response.text.encode('utf8'))

# GetStudentsByPaging.py:
	import requests

	url = "http://localhost:8080/student/list?limit=10"

	payload = {}
	headers= {}

	response = requests.request("GET", url, headers=headers, data = payload)

	print(response.text.encode('utf8'))
	
# PostStudent.py:
	import requests

	url = "http://localhost:8080/student"

	payload = "{\n    \"firstName\": \"FName1\",\n    \"lastName\": \"LName1\",\n    \"email\": \"Name1@gmail.com\",\n    \"programme\": \"Computer Science\",\n    \"courses\": [\n        \"Java\",\n        \"C#\"\n    ]\n}"
	headers = {
	  'Content-Type': 'application/json',
	  'Accept': ''
	}

	response = requests.request("POST", url, headers=headers, data = payload)

	print(response.text.encode('utf8'))
	
# PutStudent.py/UpdateStudent.py:
	import requests

	url = "http://localhost:8080/student/101"

	payload = "{\n    \"firstName\": \"FName3\",\n    \"lastName\": \"LName3\",\n    \"email\": \"Name3@gmail.com\",\n    \"programme\": \"Computer Science\",\n    \"courses\": [\n        \"Java\",\n        \"C#\"\n    ]\n}"
	headers = {
	  'Content-Type': 'application/json'
	}

	response = requests.request("PUT", url, headers=headers, data = payload)

	print(response.text.encode('utf8'))


# PatchStudent.py/PartialUpdateStudent.py:
	import requests

	url = "http://localhost:8080/student/102"

	payload = " {\n      \"email\": \"test1234@gmail.com\"\n    }"
	headers = {
	  'Content-Type': 'application/json'
	}

	response = requests.request("PATCH", url, headers=headers, data = payload)

	print(response.text.encode('utf8'))
	
# DeleteStudent.py:
	import requests

	url = "http://localhost:8080/student/102"

	payload = {}
	headers= {}

	response = requests.request("DELETE", url, headers=headers, data = payload)

	print(response.text.encode('utf8'))