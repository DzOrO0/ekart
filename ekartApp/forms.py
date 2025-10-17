from django.contrib.auth.models import User
from django import forms
from ekartApp.models import Kart
from django.contrib.auth.forms import UserCreationForm

class UserRegistartionForm(UserCreationForm):
    email=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=['username','email','password1','password2']

class LoginForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['username','password']


class kartform(forms.ModelForm):
    class Meta:
        model=Kart
        fields=["quantity"]
        widgets={
            'quantity':forms.NumberInput(attrs={'class':'form-control'})
        }
