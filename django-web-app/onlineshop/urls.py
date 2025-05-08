from django.urls import path
from onlineshop.views import OrderView, CategoryView

urlpatterns = [
    path('order/', OrderView.as_view(), name='order'),
    path('category/', CategoryView.as_view(), name='category'),
]