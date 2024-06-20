from django import forms
from .models import reservation
from datetime import datetime, date, time

class ReserveTableForm(forms.ModelForm):
    
    class Meta:
        model = reservation
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-control', 'id': 'name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control', 'id': 'email'}),
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control', 'id': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control', 'id': 'time'}),
            'no_of_people': forms.NumberInput(attrs={'placeholder': 'number of people', 'class': 'form-control', 'id': 'select1'}),
            'specialRequest': forms.Textarea(attrs={'placeholder': 'Special Request', 'class': 'form-control', 'id': 'message', 'style': 'height: 100px'}),
        }
        
    def clean_date(self):
        selected_date = self.cleaned_data.get('date')
        if selected_date and selected_date < date.today():
            raise forms.ValidationError("The date must be in the future.")
        return selected_date

    def clean_time(self):
        selected_date = self.cleaned_data.get('date')
        selected_time = self.cleaned_data.get('time')
        if selected_date and selected_time:
            reservation_datetime = datetime.combine(selected_date, selected_time)
            if reservation_datetime <= datetime.now():
                raise forms.ValidationError("The time must be in the future.")
        return selected_time