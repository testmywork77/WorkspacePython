import requests

endpoint = "http://localhost:8000/api"
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
}

response = requests.get(endpoint, json={"query": "Hello World!"})
print(response.status_code)
print(response.json())

"""
# response = requests.get(endpoint, headers=headers)
# comes as 'data': '{"query": "Hello World!"}'
response = requests.get(endpoint, json={"query": "Hello World!"}) 
print(response.json())
# 'form': {'query': 'Hello World!'}
response = requests.get(endpoint, data={"query": "Hello World!"}) 
print(response.json())
"""
