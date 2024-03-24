from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.api_home, name='api_home') # localhost:8000/api/
]
