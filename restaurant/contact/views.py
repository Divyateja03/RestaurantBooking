from django.shortcuts import render
from .models import specialRequest
from .forms import requestForm
# Create your views here.




def SpecialRequest(request):
    request_form = requestForm()
    
    if request.method == 'POST':
        request_form = requestForm(request.POST)
        
        if request_form.is_valid():
            request_form.save()
            
    request_form = requestForm()
    
    context = {
        'request_form' : request_form,
    }
    return render(request, 'contact/contact.html', context)

        
    