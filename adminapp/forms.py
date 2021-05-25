from authapp.forms import UserRegisterForm
from authapp.models import User
from django import forms

class UserAdminRegisterForm(UserRegisterForm):

    image = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'custom-file-input',
    }), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name','image', 'last_name', 'password1', 'password2')
