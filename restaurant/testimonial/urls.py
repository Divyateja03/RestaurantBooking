from django.urls import path, re_path
from . import views

app_name = 'testimonial'

urlpatterns = [
    path('', views.testimonial_list, name = 'testimonial_list'),
    
]