from django.urls import path, re_path
from . import views

app_name = 'service'

urlpatterns = [
    path('', views.services, name = 'services'),
]