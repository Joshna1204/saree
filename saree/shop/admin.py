from django.contrib import admin
from shop.models import Category,Product
# Register your models here.

admin.site.register(Product)
admin.site.register(Category)