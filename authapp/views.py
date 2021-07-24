from django.shortcuts import render, HttpResponseRedirect
from authapp.forms import UserLoginForm, UserRegisterForm, UserProfileForm
from django.contrib import auth, messages
from django.urls import reverse
from basketapp.models import Basket
from django.contrib.auth.decorators import login_required
from authapp.models import User
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
import logging
from django.utils.http import is_safe_url
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout as auth_logout
from django.utils.decorators import method_decorator
from django.views.decorators.cache import never_cache
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.debug import sensitive_post_parameters
from django.views.generic import FormView, RedirectView
from geekshop import settings
from django.core.mail import send_mail

# Create your views here.

class UserLoginView(FormView):

    model = User
    template_name = 'authapp/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('index')


    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(self.success_url)
        return render (request, 'authapp/login.html', self.get_context_data())

    def get_context_data(self, **kwargs):
        context = super(UserLoginView, self).get_context_data(**kwargs)
        context.update({'title': 'Geekshop - Авторизация'})
        return context

# def login(request):
#     if request.method == 'POST':
#         form = UserLoginForm(data=request.POST)
#         if form.is_valid():
#             username = request.POST['username']
#             password = request.POST['password']
#             user = auth.authenticate(username=username, password=password)
#             if user and user.is_active:
#                 auth.login(request, user)
#                 return HttpResponseRedirect(reverse('index'))
#     else:
#         form = UserLoginForm()
#     context = {'titles': 'Geekshop - Авторизация', 'form': form}
#     return render(request, 'authapp/login.html', context)

def send_verify_email(user):

    verify_link = reverse('users:verify', args=[user.email, user.activation_key])
    title = f'Активация на сайте пользователя {user.username}'
    message = f'Для активации вашей учётной записи {user.email} на портале {settings.DOMAIN_NAME}' \
            f'перейдите по ссылке : \n{settings.DOMAIN_NAME}{verify_link}'

    return send_mail(title, message, settings.EMAIL_HOST, [user.email], fail_silently=False)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            if send_verify_email(user):
                messages.success(request, 'Вы успешно зарегистрированы!')
                return HttpResponseRedirect(reverse('users:login'))
            else:
                messages.error(request, 'Не удалось отправить сообщение!')
                return HttpResponseRedirect(reverse('users:login'))

    else:
        form = UserRegisterForm()
    context = {'title': 'Geekshop - Регистрация', 'form': form}
    return render(request, 'authapp/register.html', context)


def verify(request, email, activation_key):
    try:
        user = User.objects.get(email=email)
        if user.activation_key == activation_key and not user.activation_key_is_expired():
            user.is_active = True
            user.save()
            auth.login(request, user)
            return render(request, 'authapp/verification.html')
    except Exception as err:
        print(f'error activation user: {err.args}')
        return HttpResponseRedirect(reverse ('index'))


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def profile(request):
    if request.method == 'POST':
        form = UserProfileForm(data=request.POST, files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = UserProfileForm(instance=request.user)

    # total_quantity = 0
    # total_sum = 0
    # for basket in baskets:
    #     total_quantity += basket.quantity
    #     total_sum += basket.sum()

    # total_quantity = sum(basket.quantity for basket in baskets)
    # total_sum = sum(basket.sum() for basket in baskets)

    context = {'title': 'Geekshop - Личный Кабинет', 'form': form,
               'baskets': Basket.objects.filter(user=request.user), }

    return render(request, 'authapp/profile.html', context)
