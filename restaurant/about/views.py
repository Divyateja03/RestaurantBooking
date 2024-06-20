from django.shortcuts import render
from team.models import Team
# Create your views here.

def team_details(request):
    team_details = Team.objects.all
    context = {
        'team_details' : team_details,
    }
    return render(request, 'about/about.html', context)

