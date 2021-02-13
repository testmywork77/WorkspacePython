import requests

validCredentials = ("admin", "admin")
inValidCredentials = ("admin1", "admin1")
resp = requests.get("https://the-internet.herokuapp.com/basic_auth", auth=inValidCredentials)
print(resp.status_code)

validCredentials = ("admin", "admin")
resp = requests.get("https://the-internet.herokuapp.com/basic_auth", auth=validCredentials)
print(resp.status_code)
