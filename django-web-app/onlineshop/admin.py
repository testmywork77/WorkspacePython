from django.contrib import admin
from .models import Product, Category, Order

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','category_name', 'description', 'created_at', 'updated_at']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','product_name','description','price','image', 'category', 'created_at', 'updated_at']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','customer_name', 'email', 'product', 'quantity', 'created_at', 'updated_at']
