from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from .forms import MyUserCreationForm
from django.contrib.auth import login as mylogin
from django.contrib.auth import logout as mylogout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.http import Http404
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

@login_required
def logout(request):
    mylogout(request)
    return redirect('articles:index')

@login_required
def profile(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {
        'user': user,
    }
    return render(request, 'accounts/profile.html', context)

@login_required
def follow(request, pk):
    user = get_object_or_404(get_user_model(), pk=pk)
    # user = get_user_model().objects.get(pk=pk)
    if request.user == user:
        raise Http404("Access is not vaild")
    if request.user in user.follower.all():
        user.follower.remove(request.user)
    else:
        user.follower.add(request.user)
    return redirect('accounts:profile', pk)