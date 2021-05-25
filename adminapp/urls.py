from django.urls import path
from adminapp.views import index

ap_name = 'adminapp'

urlpatterns = [
    path ('', index, name='index'),

]

