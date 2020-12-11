from django.contrib import admin

from .models import Customer,Product,ShippingAddress,Order,OrderItem

admin.site.register(Customer)
admin.site.register(ShippingAddress)
admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Product)
