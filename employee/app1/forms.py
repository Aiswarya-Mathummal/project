from django import forms
from . models import employee

class RegisterForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput,max_length=12,min_length=5)
    class Meta():
        model= employee                                    
        fields='__all__'
        