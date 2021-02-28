import requests


payload = {
    "job": "web testing"
}
resp = requests.patch("https://reqres.in/api/users/2", data=payload)
print(resp)
print(resp.json())
assert resp.json()['job'] == 'web testing'
