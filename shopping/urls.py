from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from shopping import views

app_name = 'shopping'

urlpatterns = [
    path('caja/', TemplateView.as_view(template_name='compra.html'), name='caja'),
    path('agregar/<int:producto_id>/', views.agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', views.eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', views.restar_producto, name="Sub"),
    path('limpiar/', views.limpiar_carrito, name="Cls"),
    path('compra/', views.procesar_compra, name="procesar_compra"),
]
