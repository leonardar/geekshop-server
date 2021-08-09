from django.urls import path
from ordersapp.views import OrdersList, OrderCreate, order_forming_complete, OrderRead, OrderUpdate, OrderDelete, get_product_price

ap_name = 'ordersapp'

urlpatterns = [
    path('', OrdersList.as_view(), name='order_list'),
    path('forming/complete/<int:pk>/', order_forming_complete, name='order_forming_complete'),
    path('create/', OrderCreate.as_view(), name='order_create'),
    path('read/<int:pk>/', OrderRead.as_view(), name='order_read'),
    path('update/<int:pk>/', OrderUpdate.as_view(), name='order_update'),
    path('delete/<int:pk>/', OrderDelete.as_view(), name='order_delete'),
    path('product/<int:pk>/price/', get_product_price)
]
