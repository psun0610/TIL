from django.urls import path
from . import views

app_name = 'record'

urlpatterns = [
    path('', views.book, name='book'),
    path('create', views.create, name='create'),
    path('<int:pk>/delete', views.delete, name='delete'),
]