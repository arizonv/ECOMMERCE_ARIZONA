from email import message
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
import random
from .forms import CustomUserCreationForm

from django.contrib import messages
from django.http import Http404
import json
from django.contrib.auth.decorators import user_passes_test
from decorators import admin_required,client_required


def registro(request):  
    data = {
        'form': CustomUserCreationForm()
    }
    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"],password=formulario.cleaned_data["password1"])
            login (request,user)
            messages.success(request, "Usurio Registrado!")
            return redirect(to='home')
        data ["form"] = formulario
    return render(request, 'registration/registro.html', data )
