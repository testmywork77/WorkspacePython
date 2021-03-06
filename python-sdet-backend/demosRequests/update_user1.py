import requests


payload = {
    "name": "morpheus",
    "job": "api testing"
}
resp = requests.put("https://reqres.in/api/users/2", data=payload)
print(resp)
print(resp.json())
