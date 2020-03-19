from django.contrib import admin
from django.contrib.auth.models import User
from .models import Category, Food, Order, Price, Topping, OrderItem

# Register your models here.
admin.site.register(Category)
admin.site.register(Food)
admin.site.register(Topping)
admin.site.register(Price)
admin.site.register(Order)
admin.site.register(OrderItem)
