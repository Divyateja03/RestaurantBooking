from django.shortcuts import render
from .models import Team
# Create your views here.

def team_members(request):
    team_members = Team.objects.all()
    context = {
        'team_members' : team_members,
    }
    return render(request, 'teams/team.html', context)
