import requests


c = {'visit-month': 'February'}
response = requests.get('https://rahulshettyacademy.com', cookies=c)
print(response.history)
print(response.status_code)

# allow_redirects set to false
response = requests.get('https://rahulshettyacademy.com', allow_redirects=False, cookies=c, timeout=1)
print(response.history)
print(response.status_code)
