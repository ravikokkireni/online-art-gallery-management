from django.contrib import admin

# Register your models here.
# shop/admin.py

from django.contrib import admin
from .models import Product, Order, Exhibition

admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Exhibition)

# admin.site.register(OrderItem)
