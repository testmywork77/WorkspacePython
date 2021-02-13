import requests


resp = requests.delete("https://reqres.in/api/user/2")
print(resp)
assert resp.status_code == 204, "User deletion failed"
