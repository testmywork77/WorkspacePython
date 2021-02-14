import requests


# File Attachments
url = "https://petstore.swagger.io/v2/pet/9843217/uploadImage"
files = {'file': open(r'C:\MyAttachment\ra.png', 'rb')}
r = requests.post(url, files=files)
print(r.status_code)
print(r.text)
