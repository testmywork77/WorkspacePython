import requests


payload = {
    "name": "venkata",
    "job": "leader"
}
resp = requests.post("https://reqres.in/api/users", data=payload)
print(resp.status_code)
print(resp.json())
assert resp.json()['job'] == "leader"

