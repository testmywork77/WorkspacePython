import requests
from utilities.configurations import *
from utilities.resources import *


p = {"page": 2}
# resp = requests.get("https://reqres.in/api/users?page=2")

# Use params parameter for query string/parameters as dictionary object
# resp = requests.get("https://reqres.in/api/users", params=p)

# Read baseURI from properties.ini file
# config = ConfigParser()
# config.read(r'..\utilities\properties.ini')
# config.read('../utilities/properties.ini')

config = getConfig()
print(config['api']['base_uri'])
url = config['api']['base_uri'] + ApiResources.getUser
headers = {"Content-Type": "application/json"}
resp = requests.get(url, params=p, headers = headers)
print(resp.url)
statusCode = resp.status_code
assert statusCode == 200, "response code doesn't match"
response_json = resp.json()
print(response_json["total"])
assert response_json["total"] == 12
print(response_json["data"][0]["email"])
assert response_json["data"][0]["email"] == "michael.lawson@reqres.in"
assert (response_json["data"][0]["email"]).endswith("reqres.in")
assert response_json["data"][2]["last_name"]!= None


"""

print(resp)  # print response
print(type(resp))  # print type of resp object
print(dir(resp))  # print metadata of resp object

print(resp.text)  # response in plain string format
print(resp.content)  # response , bytes format
print(resp.json())  # response in json serialized format

print(resp.headers)
print(resp.cookies)
print(resp.encoding)
print(resp.url)

"""

