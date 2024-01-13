from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import views as auth_views
from .forms import UserRegisterForm

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account Has Been Created!')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def logout(request):
    if request.method == 'POST':
        auth_views.logout(request)
    return render(request, 'users/logout.html')

