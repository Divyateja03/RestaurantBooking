from django.urls import path
from . import views

app_name = 'about'

urlpatterns = [
    path('', views.team_details, name = 'team_details'),
]