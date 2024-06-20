from django.shortcuts import render
from .models import Testimonial
# Create your views here.


def testimonial_list(request):
    testimonial_list = Testimonial.objects.all()
    context = {
        'testimonial_list' : testimonial_list,
    }
    return render(request, 'testimonial/testimonial.html', context)
    