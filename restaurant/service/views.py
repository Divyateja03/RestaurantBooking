from django.shortcuts import render
from .models import Services

# Create your views here.

def services(request):
    services = Services.objects.all()
    context = {
        'services' : services,
    }
    return render(request, 'service/service.html', context)