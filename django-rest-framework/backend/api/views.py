import json
from django.http import JsonResponse

# Create your views here.
def api_home(request, *args, **kwargs):
    body = request.body # byte string of JSON data    
    data = {}
    try:
        data = json.loads(body)
    except:
        pass

    print(data)
    return JsonResponse({"message": "Django API response"})