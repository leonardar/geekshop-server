from django.contrib import admin

# Register your models here.
from mainapp.models import ProductCategory, Product
from authapp.models import User

admin.site.register(ProductCategory)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'price',
        'quantity',
    ]