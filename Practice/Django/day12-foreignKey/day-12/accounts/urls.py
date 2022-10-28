from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('<int:pk>/profile/', views.profile, name='profile'),
    path('<int:pk>/follow/', views.follow, name='follow'),
]