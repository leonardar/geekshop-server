from django.urls import path
from authapp.views import login, register

ap_name = 'authapp'

urlpatterns = [
    path ('login/', login, name='login'),
    path ('register/', register, name='register'),
]

