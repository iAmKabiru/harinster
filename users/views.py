from django.shortcuts import render
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404 
from django.views import generic
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required

class SignUp(generic.CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'


@login_required
def profile(request):
    args = {'user': request.user}
    return render(request, 'registration/profile.html')


@login_required
def edit_profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance = request.user)

        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserChangeForm(instance = request.user)
        args = {'form':form}
        return render(request, 'registration/edit_profile.html', args)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data =request.POST, user = request.user)

        if form.is_valid():
            update_session_auth_hash(request, form.user)
            form.save()
            return redirect('login')
        else:
            return redirect('change_password')
    else:
        form = PasswordChangeForm(user = request.user)
        args = {'form':form}
        return render(request, 'registration/password_change_form.html', args)