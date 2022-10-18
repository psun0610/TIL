from django.shortcuts import render, redirect
from accounts.models import User
from .forms import CustomerUserCreationForm, CustomUserChangeForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = CustomerUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user) 
            return redirect("articles:index")
    else:
        form = CustomerUserCreationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('articles:index')

def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {
        'user': user
    }
    return render(request, 'accounts/detail.html', context)

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:detail', request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form' : form
    }
    return render(request, 'accounts/update.html', context)
