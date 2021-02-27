import requests
from utilities.configurations import *
from utilities.resources import *

params_dict = {
    "AuthorName": "Rahul Shetty2"
}

# Get request with QueryString in in-line url
# response = requests.get('http://216.10.245.166/Library/GetBook.php?AuthorName=RahulShetty2')

# Pass QueryString as params
# response = requests.get('http://216.10.245.166/Library/GetBook.php', params=params_dict)

# Get Base_URI from config
# config = ConfigParser()
# config.read(r'..\utilities\properties.ini')
# config.read('../utilities/properties.ini')

config = getConfig()
print(config['API']['book_uri'])
url = config['API']['book_uri'] + ApiResources.getBook
headers = {"Content-Type": "application/json"}
response = requests.get(url, params=params_dict, headers = headers)
json_response = response.json()
assert response.status_code == 200
# print(type(json_response))
print(response.json())
# print(response.headers)
assert response.headers['Content-Type'].__contains__('application/json'), 'Not exists'
assert response.headers['Content-Type'] == 'application/json;charset=UTF-8'
# Retrieve the book details with isbn as 'PSRS'
expectedBook = {
    'book_name': 'Python Selenium 18hrs By Rahul Shetty',
    'isbn': 'PSRS',
    'aisle': '19'
}
for actualBook in json_response:
    if actualBook['isbn'] == "PSRS":
        print(actualBook)
        break

assert actualBook == expectedBook
