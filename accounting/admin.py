from django.contrib import admin
from .models import Customer, Supplier, Product, Sale, Purchase

admin.site.register(Customer)
admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(Purchase)
