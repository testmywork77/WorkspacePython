# Inline user dictionary
import requests


user_dict = {
    "name": "venkata",
    "job": "leader"
}
resp = requests.post("https://reqres.in/api/users", data=user_dict)
print(resp.status_code)
print(resp.json())
assert resp.json()['job'] == "leader"

