from tkinter import Widget
from django import forms
from .models import contacto,Producto
import re
from django.contrib.auth.forms import UserCreationForm  
from accounts.models import User


class ContactoForm(forms.ModelForm):
    class Meta:
        model = contacto
        fields = ["nombre", "apellido", "email", "numero", "descripcion", "region", "comuna"]
        widgets = {
            "descripcion": forms.Textarea(attrs={"cols": 37, "rows": 5}),
            "region": forms.Select(attrs={"id": "region"}),
            "comuna": forms.Select(attrs={"id": "comuna"}),
        }



class ProductoForm(forms.ModelForm):
    class Meta:

        model = Producto
        widgets = {
            'descripcion': forms.Textarea(attrs={'cols': 37, 'rows': 5 }),
        }
        fields = '__all__'




