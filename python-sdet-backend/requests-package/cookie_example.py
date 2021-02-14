import requests


c = {'visit-month': 'Apr'}
response = requests.get('https://httpbin.org/cookies', cookies=c)
print(response.status_code)
print(response.text)


# Cookie with Session object
s = requests.session()
s.cookies.update({'visit-year': '2020'})
response = s.get('https://httpbin.org/cookies', cookies=c)
print(response.status_code)
print(response.text)


