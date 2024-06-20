from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.SpecialRequest, name = 'request_form'),
]


