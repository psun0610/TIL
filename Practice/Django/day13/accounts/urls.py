from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('update/<int:pk>/', views.update, name='update'),
]