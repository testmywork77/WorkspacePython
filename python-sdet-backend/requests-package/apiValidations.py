import requests
import configparser

params_dict = {
    "AuthorName": "Rahul Shetty2"
}

# Get request with QueryString in in-line url
# response = requests.get('http://216.10.245.166/Library/GetBook.php?AuthorName=RahulShetty2')

# Pass QueryString as params
# response = requests.get('http://216.10.245.166/Library/GetBook.php', params=params_dict)

# Get Base_URI from config
config = configparser.ConfigParser()
config.read('/utilities/properties.ini')
print(config['api']['base_url'])
response = requests.get(config['api']['base_url']+'/Library/GetBook.php', params=params_dict)

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
