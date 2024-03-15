from django.shortcuts import render

from .models import Order, Category, Product
from .serializers import OrderSerializer, CategorySerializer

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response

# Create your views here.
class OrderView(APIView):
    
    # Get all orders
    def get(self, request):
        try:
            orders = Order.objects.all()
            serializer = OrderSerializer(orders, many=True)

            return Response({
                'data': serializer.data,
                'message': "Orders Data fetched Successfully"
            }, status= status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response({
                'data': {},
                'message': "Something went wrong while fetching the data"
            }, status= status.HTTP_400_BAD_REQUEST)


    # Create a new order
    def post(self, request):
        try:
            data = request.data
            serializer = OrderSerializer(data=data)  

            if not serializer.is_valid():
                return Response({
                'data': serializer.errors,
                'message': "Something went wrong"
            }, status= status.HTTP_400_BAD_REQUEST)

            # subject = "New Order is Placed" 
            # message = "Dear Customer" + " " + data['customer_name'] + " Your order is placed now. Thanks for your order"
            # email = data['customer_email']
            # recipient_list = [email]
            # send_mail(subject, message, EMAIL_HOST_USER, recipient_list, fail_silently=True) 
            serializer.save()

            return Response({
                'data': serializer.data,
                'message': "New order is created or Placed"
            }, status= status.HTTP_201_CREATED)

        except:
            return Response({
                'data': {},
                'message': "Something went wrong in creation of Order"
            }, status= status.HTTP_400_BAD_REQUEST)

    # Update an existing order
    def patch(self, request):
        try:
            data = request.data
            order1 = Order.objects.filter(id=data.get('id'))

            if not order1.exists():
              return Response({
                'data': {},
                'message': "Order is not Found with this ID"
            }, status= status.HTTP_404_NOT_FOUND)

            serializer = OrderSerializer(order1[0], data= data, partial=True)

            if not serializer.is_valid():
                return Response({
                  'data': serializer.errors,
                  'message': "Something went wrong"
                }, status= status.HTTP_500_BAD_REQUEST)

            serializer.save()

            return Response({
                'data': serializer.data,
                'message': "Order is Updated successfully"
             }, status= status.HTTP_200_OK)

        except:     
            return Response({
                'data': {},
                'message': "Something went wrong in creation of Order"
            }, status= status.HTTP_400_BAD_REQUEST)

    # Delete an existing order
    def delete(self, request):
        try:
            data =request.data
            order = Order.objects.filter(id =data.get('id'))
            
            if not order.exists():
               return Response({
                'data': {},
                'message': "Order is not Found with this ID"
            }, status= status.HTTP_404_NOT_FOUND)

            order[0].delete() 
            return Response({
                'data': {},
                'message': "Order is Deleted"
             }, status= status.HTTP_200_OK)

        except:  
              return Response({
                'data': {},
                'message': "Something went wrong in deleting the Order"
            }, status= status.HTTP_400_BAD_REQUEST)

class CategoryView(APIView):
    
    # Get all orders
    def get(self, request):
        try:
            category = Category.objects.all()
            serializer = CategorySerializer(category, many=True)

            return Response({
                'data': serializer.data,
                'message': "category Data fetched Successfully"
            }, status= status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response({
                'data': {},
                'message': "Something went wrong while fetching the data"
            }, status= status.HTTP_400_BAD_REQUEST)