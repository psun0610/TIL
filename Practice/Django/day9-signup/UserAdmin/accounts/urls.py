from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.userlist, name='userlist'),
    path('signup', views.signup, name='signup'),
]