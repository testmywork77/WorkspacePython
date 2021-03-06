# Inline user dictionary
"""
For Linux/Mac
export PYTHONPATH="${PYTHONPATH}:/path/to/your/project/"
For Windows
set PYTHONPATH=%PYTHONPATH%;C:\path\to\your\project\
set PYTHONPATH=%PYTHONPATH%;C:\WorkspacePython\python-sdet-backend
"""

import requests
from utilities.configurations import *
from utilities.resources import *


payload = {
    "name": "venkata",
    "job": "leader"
}

url = getUserBaseURI() + ApiResources.postUser
resp = requests.post(url=url, data=payload)
print(resp.status_code)
print(resp.request.url)
print(resp.json())
assert resp.json()['job'] == "leader"

