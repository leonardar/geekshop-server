from django.shortcuts import render

# Create your views here.

def login(request):
    context = {'titles':'Geekshop - Авторизация'}
    return render(request, 'authapp/login.html',context)