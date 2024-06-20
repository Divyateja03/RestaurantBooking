from django import forms
from .models import specialRequest

class requestForm(forms.ModelForm):
    
    
    class Meta:
        model = specialRequest
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name', 'class': 'form-control', 'id': 'name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email', 'class': 'form-control', 'id': 'email'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Subject', 'class': 'form-control', 'id': 'subject'}),
            'message': forms.Textarea(attrs={'placeholder': 'Leave a message here', 'class': 'form-control', 'id': 'message', 'style': 'height: 150px'}),
        }