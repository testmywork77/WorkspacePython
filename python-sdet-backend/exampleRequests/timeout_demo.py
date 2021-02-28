import requests


resp = requests.get("https://httpbin.org/delay/5", timeout=3)
print(resp.status_code)
