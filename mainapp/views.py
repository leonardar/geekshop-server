from django.shortcuts import render
from mainapp.models import Product, ProductCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from basketapp.models import Basket


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        baskets = Basket.objects.filter(user=request.user)
        context = {
        'title': 'index',
        'baskets': baskets}
    else:
        context = {'title': 'index'}

    return render(request, 'mainapp/index.html', context)


def products(request, category_id=None,page=1):
    if request.user.is_authenticated:
        baskets = Basket.objects.filter(user=request.user)
        context = {
        'title': 'Geekshop - Каталог',
        'categories': ProductCategory.objects.all(),
        'baskets': baskets}
    else:
        context = {'title': 'Geekshop - Каталог',
                'categories': ProductCategory.objects.all()}

    products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
    paginator = Paginator(products, per_page=3)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context.update({'products': products_paginator})
    return render(request, 'mainapp/products.html', context)

