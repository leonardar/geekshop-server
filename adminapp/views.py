from django.shortcuts import render, HttpResponseRedirect
from authapp.models import User
from django.urls import reverse
from adminapp.forms import UserAdminRegisterForm

def index(request):
    return render(request, 'adminapp/admin.html')


# CRUD Create Read Update Delete
def admin_users_read(request):
    context = {'users': User.objects.all()}
    return render(request, 'adminapp/admin-users-read.html', context)

def admin_users_create(request):
    if request.method == 'POST':
        form = UserAdminRegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_users_read'))
    else:
        form = UserAdminRegisterForm()
    context = {'form': form}
    return render(request, 'adminapp/admin-users-create.html',context)