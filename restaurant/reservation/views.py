from django.shortcuts import render, redirect
from .models import reservation
from .forms import ReserveTableForm

def reserve_table(request):
    reserve_form = ReserveTableForm()
    
    if request.method == 'POST':
        reserve_form = ReserveTableForm(request.POST)
        
        if reserve_form.is_valid():
            reserve_form.save()
            
    reserve_form = ReserveTableForm()
            
            
    context = {'reserve_form' : reserve_form,}
    return render(request, 'reservation/reservation.html', context)
