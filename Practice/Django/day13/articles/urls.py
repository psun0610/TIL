from django.urls import path 
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/comments/', views.comment_create, name='comment_create'),
    path('<int:pk>/comments/<int:comment_pk>', views.comment_delete, name='comment_delete'),
    path('<int:pk>/delete', views.delete, name='delete'),
]