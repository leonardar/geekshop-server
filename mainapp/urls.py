from django.urls import path
from mainapp.views import products

ap_name = 'mainapp'

urlpatterns = [
    path ('', products, name='index'),
    path ('<int:id>/',products, name='product' )
]
