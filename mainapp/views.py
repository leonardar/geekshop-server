from django.shortcuts import render
from mainapp.models import Product, ProductCategory


# Create your views here.
def index(request):
    context = {
        'title': 'index',
    }
    return render(request, 'mainapp/index.html', context)


def products(request):
    context = {
        'title': 'products',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),
    }
    return render(request, 'mainapp/products.html', context)
