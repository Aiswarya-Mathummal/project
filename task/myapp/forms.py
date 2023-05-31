from django import forms
from . models import user_register,Galleryy

class RegisterForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput,max_length=12,min_length=5)
    class Meta():
        model= user_register                                       
        fields='__all__'
        
class LoginForm(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput,max_length=12,min_length=2)
    class Meta():
        model= user_register                                       
        fields=('email','password')
        
class UpdateForm(forms.ModelForm):
    class Meta():
        model=user_register
        fields=('username','email','address','phone','photo')

class changePswdForm(forms.Form):
    OldPassword=forms.CharField(widget=forms.PasswordInput,max_length=12,min_length=2)
    NewPassword=forms.CharField(widget=forms.PasswordInput,max_length=12,min_length=2)
    ConfirmPassword=forms.CharField(widget=forms.PasswordInput,max_length=12,min_length=2)
    
    
# ---------------------------------GALLERY-------------------------------------------

# class getimagesForm(forms.Form):
#     class Meta():
#         model=Galleryy
#         fields=('name','img')