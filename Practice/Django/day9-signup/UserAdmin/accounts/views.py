from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model

# Create your views here.
def index(request):
    return render(request, 'accounts/index.html')


def userlist(request):
    users = get_user_model().objects.all()
    context = {
        'users': users,
    }
    return render(request, 'accounts/userlist.html', context)


def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:userlist')
    else:
        form = CustomUserCreationForm()
    context = { 
        'form': form
    }
    return render(request, 'accounts/signup.html', context)