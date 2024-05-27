from django import forms
from .models import User
from django.contrib.auth.forms import UserCreationForm

class UserCreationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'nom', 'prenom', 'mot_de_passe']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'nom': forms.TextInput(attrs={'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control'}),
            'mot_de_passe': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

