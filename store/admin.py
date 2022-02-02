from django.contrib import admin

# Register your models here.
from .models import Item, OrderItems, Order


admin.site.register(Item)
admin.site.register(OrderItems)
admin.site.register(Order)
