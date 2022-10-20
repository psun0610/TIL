from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from .forms import MyUserCreationForm
from django.contrib.auth import login as mylogin
from django.contrib.auth import logout as mylogout
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def signup(request):
    if request.method == 'POST':
        creationform = MyUserCreationForm(request.POST)
        if creationform.is_valid():
            user = creationform.save()
            mylogin(request, user)
            return redirect('articles:index')
    else:
        creationform = MyUserCreationForm()
    context = {
        'creationform': creationform,
    }
    return render(request, 'accounts/signup.html', context)

def login(request):
    if request.method == 'POST':
        loginform = AuthenticationForm(request, data=request.POST)
        if loginform.is_valid():
            mylogin(request, loginform.get_user())
            return redirect(request.GET.get(next) or 'articles:index')
    else:
        loginform = AuthenticationForm()
    return render(request, 'accounts/login.html', {'loginform': loginform})

def logout(request):
    mylogout(request)
    return redirect('articles:index')

def profile(request):
    return render(request, 'accounts/profile.html')