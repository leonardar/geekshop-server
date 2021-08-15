from django.contrib import admin
from authapp.models import User,UserProfile
from django.contrib.auth.admin import UserAdmin

# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)