from dataclasses import fields
from django import forms
from .models import Producto
from rest_framework import serializers


class productoSerializer (serializers.ModelSerializer):
    class Meta:
        model = Producto
        #fields = ["nombre" ,"correo" ,"telefono" ,"nombreFundacion" ,"monto"]
        fields = '__all__'

