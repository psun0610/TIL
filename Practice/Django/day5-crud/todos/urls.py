from django.urls import path
from . import views

app_name = 'todos'

urlpatterns = [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('delete/<int:pk>', views.delete, name='delete'),
    path('edit/<int:pk>', views.edit, name='edit'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('detail_edit/<int:pk>', views.detail_edit, name='detail_edit'),
]