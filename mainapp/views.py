from django.shortcuts import render
from django.views.generic import ListView

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


# def products(request, category_id=None,page=1):
#     if request.user.is_authenticated:
#         baskets = Basket.objects.filter(user=request.user)
#         context = {
#         'title': 'Geekshop - Каталог',
#         'categories': ProductCategory.objects.all(),
#         'baskets': baskets}
#     else:
#         context = {'title': 'Geekshop - Каталог',
#                 'categories': ProductCategory.objects.all()}
#
#     products = Product.objects.filter(category_id=category_id) if category_id else Product.objects.all()
#     paginator = Paginator(products, per_page=3)
#     try:
#         products_paginator = paginator.page(page)
#     except PageNotAnInteger:
#         products_paginator = paginator.page(1)
#     except EmptyPage:
#         products_paginator = paginator.page(paginator.num_pages)
#     context.update({'products': products_paginator})
#     return render(request, 'mainapp/products.html', context)

class ProductView(ListView):
    model = Product
    template_name = 'mainapp/products.html'
    # paginator = Paginator
    # paginate_by = 4

    def get_queryset(self):
        category_id = self.kwargs.get('category_id')
        if category_id == None:
            products = Product.objects.all()
        else:
            products = Product.objects.filter(category_id=category_id)
        categories = ProductCategory.objects.all()
        queryset = {'products': products, 'categories': categories }
        return queryset

    def get_context_data(self, **kwargs):
        context = super(ProductView, self).get_context_data(**kwargs)
        # category_id = kwargs.get('category_id', None)
        # page = kwargs.get('page', None)

        # paginator = self.paginator(products, per_page=3)
        # try:
        #     products_paginator = paginator.page(page)
        # except PageNotAnInteger:
        #     products_paginator = paginator.page(1)
        # except EmptyPage:
        #     products_paginator = paginator.page(paginator.num_pages)
        # products = paginator.page(page)
        context.update({'title': 'Geekshop - Каталог', 'categories': self.get_queryset()['categories'] ,'products': self.get_queryset()['products']})
        return context


class ProductCategoryView(ListView):
    model = ProductCategory
    template_name = 'mainapp/products.html'

    def get_context_data(self, **kwargs):
        context = super(ProductCategoryView, self).get_context_data(**kwargs)
        context.update({'title': 'Geekshop - Каталог', 'categories': ProductCategory.objects.all()})
        return context

