from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name = 'record'

urlpatterns = [
    path('', views.book, name='book'),
    path('create', views.create, name='create'),
    path('<int:pk>/delete', views.delete, name='delete'),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)