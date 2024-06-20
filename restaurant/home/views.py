from django.shortcuts import render
from booking.models import Menu, Category
from service.models import Services
from team.models import Team
from testimonial.models import Testimonial
from reservation.models import reservation
from reservation.forms import ReserveTableForm

# Create your views here.

def home_view(request):
    menu_list = Menu.objects.all()
    categories = Category.objects.all()
    services = Services.objects.all()
    team_members = Team.objects.all()
    testimonial_list = Testimonial.objects.all()
    reserve_form = ReserveTableForm()
    
    if request.method == 'POST':
        reserve_form = ReserveTableForm(request.POST)
        
        if reserve_form.is_valid():
            reserve_form.save()
            
    reserve_form = ReserveTableForm()
    
    context = {
        'menu_list' : menu_list,
        'categories' : categories,
        'services' : services,
        'team_members' : team_members,
        'testimonial_list' : testimonial_list,
        'reserve_form' : reserve_form,
    }
    
    return render(request, 'home/home.html', context)
