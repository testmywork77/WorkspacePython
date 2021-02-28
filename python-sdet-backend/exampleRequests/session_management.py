import requests


s = requests.session()
s.auth = auth = ('testmywork77@gmail.com', 'abctestmywork2020$')
# Can use session object for all the consecutive requests

# /testmywork77
url1 = "https://api.github.com/users/testmywork77"

# response1 = requests.get(url, verify=false, auth=('username', 'pwd') )
response1 = requests.get(url1, auth=('username', 'pwd'))
print(response1.status_code)
print(response1.text)

# url2 = "https://api.github.com/users/testmywork77/repos"
# response2 = requests.get(url2)
# print(response2.status_code)
# print(response2.text)

# url3 = "https://api.github.com/users/testmywork77/repos"
