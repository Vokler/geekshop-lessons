from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test

from authapp.models import User
from adminapp.forms import UserAdminRegisterForm, UserAdminProfileForm

from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView
from django.urls import reverse_lazy


@user_passes_test(lambda u: u.is_superuser)
def index(request):
    return render(request, 'adminapp/index.html')


class UsersListView(ListView):
    model = User
    template_name = 'adminapp/admin-users-read.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)


class UsersCreateView(CreateView):
    model = User
    template_name = 'adminapp/admin-users-create.html'
    success_url = reverse_lazy('admin_staff:admin_users')
    form_class = UserAdminRegisterForm


@user_passes_test(lambda u: u.is_superuser)
def admin_users_update(request, user_id):
    # U - Update
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = UserAdminProfileForm(data=request.POST, files=request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('admin_staff:admin_users'))
    else:
        form = UserAdminProfileForm(instance=user)

    context = {'form': form, 'user': user}
    return render(request, 'adminapp/admin-users-update-delete.html', context)


@user_passes_test(lambda u: u.is_superuser)
def admin_users_remove(request, user_id):
    user = User.objects.get(id=user_id)
    # user.delete()
    user.is_active = False
    user.save()
    return HttpResponseRedirect(reverse('admin_staff:admin_users'))
