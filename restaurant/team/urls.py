from django.urls import path, re_path
from . import views

app_name = 'team'

urlpatterns = [
    path('', views.team_members, name = 'team_members'),
]