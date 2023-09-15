from django.contrib import admin
from .models import Client, Order, Product
# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_filter = ["name"]

class OrderAdmin(admin.ModelAdmin):
    pass

class ProductAdmin(admin.ModelAdmin):
    list_filter = ["name"]

admin.site.register(Client, ClientAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)


