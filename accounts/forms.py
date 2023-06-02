from tkinter import Widget
from django import forms
import re
from django.contrib.auth.forms import UserCreationForm  
from .models import User



class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=20,
        help_text='20 caracteres como máximo. Únicamente letras, números y @/./+/-/_'
    )
    password1 = forms.CharField(
        label="Contraseña",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
        help_text="La contraseña debe tener al menos 8 caracteres y no puede tener similitud a los demas campos."
    )
    password2 = forms.CharField(
        label="Confirmar contraseña",
        strip=False,
        widget=forms.PasswordInput(attrs={'autocomplete': 'new-password', 'class': 'form-control'}),
        help_text="Ingrese la misma contraseña de arriba, para su verificación."
    )

    class Meta:
        model = User
        fields = ["username" ,"name","email","password1","password2"]


