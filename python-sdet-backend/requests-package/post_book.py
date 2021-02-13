import requests


payload = {'book_name': 'Python Selenium 18hrs By Rahul Shetty', 'isbn': 'PSRS', 'aisle': '19'}

r = requests.post('http://216.10.245.166/Library/Addbook.php',
                  json=payload,
                  headers={'Content-Type': 'application/json'},)
print(r.json())
