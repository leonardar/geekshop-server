from django.urls import path
from authapp.views import UserLoginView, register,logout,profile,verify,send_verify_email

ap_name = 'authapp'

urlpatterns = [
    path ('login/', UserLoginView.as_view(), name='login'),
    path ('register/', register, name='register'),
    path ('logout/', logout, name='logout'),
    path ('profile/', profile, name='profile'),
    path ('verify/<str:email>/<str:activation_key>/', verify, name='verify'),
    path ('send_verify_email/', send_verify_email, name='send_verify_email'),
]

