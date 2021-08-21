from django.shortcuts import render
from mainapp.models import Product, ProductCategory
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from basketapp.models import Basket
from django.core.cache import cache
from django.conf import settings

def get_links_menu():
   if settings.LOW_CACHE:
       key = 'links_menu'
       links_menu = cache.get(key)
       if links_menu is None:
           links_menu = ProductCategory.objects.all()
           cache.set(key, links_menu)
       return links_menu
   else:
       return ProductCategory.objects.all()

def get_category(pk):
   if settings.LOW_CACHE:
       key = f'category_{pk}'
       category = cache.get(key)
       if category is None:
           category = get_object_or_404(ProductCategory, pk=pk)
           cache.set(key, category)
       return category
   else:
       return get_object_or_404(ProductCategory, pk=pk)

def get_products(category_id):
   if settings.LOW_CACHE:
       key = 'products'
       products = cache.get(key)
       if products is None:
           products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
           cache.set(key, products)
       return products
   else:
       return Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()

def get_product(pk):
   if settings.LOW_CACHE:
       key = f'product_{pk}'
       product = cache.get(key)
       if product is None:
           product = get_object_or_404(Product, pk=pk)
           cache.set(key, product)
       return product
   else:
       return get_object_or_404(Product, pk=pk)

def get_products_orederd_by_price():
   if settings.LOW_CACHE:
       key = 'products_orederd_by_price'
       products = cache.get(key)
       if products is None:
           products = Product.objects.filter(is_active=True, \
                                  category__is_active=True).order_by('price')
           cache.set(key, products)
       return products
   else:
       return Product.objects.filter(is_active=True,\
                                 category__is_active=True).order_by('price')


def get_products_in_category_orederd_by_price(pk):
   if settings.LOW_CACHE:
       key = f'products_in_category_orederd_by_price_{pk}'
       products = cache.get(key)
       if products is None:
           products = Product.objects.filter(category__pk=pk, is_active=True, category__is_active=True).order_by('price')
           cache.set(key, products)
       return products
   else:
       return Product.objects.filter(category__pk=pk, is_active=True,category__is_active=True).order_by('price')


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
        'categories': get_links_menu(),
        'baskets': baskets}
    else:
        context = {'title': 'Geekshop - Каталог',
                'categories': get_links_menu()}

    products = get_products(category_id)
    paginator = Paginator(products, per_page=4)
    try:
        products_paginator = paginator.page(page)
    except PageNotAnInteger:
        products_paginator = paginator.page(1)
    except EmptyPage:
        products_paginator = paginator.page(paginator.num_pages)
    context.update({'products': products_paginator})
    return render(request, 'mainapp/products.html', context)

