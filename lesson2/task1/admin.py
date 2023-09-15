from django.contrib import admin
from models import Client, Order, Product
# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    pass
class OrderAdmin(admin.ModelAdmin):
    pass
class ProductAdmin(admin.ModelAdmin):
    pass

admin.site.register(Client, ClientAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Product, ProductAdmin)


