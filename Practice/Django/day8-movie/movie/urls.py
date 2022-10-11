# URL설정을 app 단위로!
from django.urls import path 
from . import views

app_name = 'movie'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete', views.delete, name='delete'),
]