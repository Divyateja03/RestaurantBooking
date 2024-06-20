from django.urls import path, re_path
from . import views

app_name = 'booking'

urlpatterns = [
    path('', views.menu_list, name = 'menu_list'),
    path('<slug:slug>', views.meal_details, name = 'meal_details'),
]