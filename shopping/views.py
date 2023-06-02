from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse
from tienda.models import Categorias, Marca, Producto
from django.contrib import messages
from .carrito import Carrito


def compra(request):
    return render(request, 'compra.html')

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    return carrito.procesar_operacion(request, producto_id, 'agregar')

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    return carrito.procesar_operacion(request, producto_id, 'eliminar')

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    return carrito.procesar_operacion(request, producto_id, 'restar')



def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect(reverse("tienda:store"))


def procesar_compra(request):
    carrito = Carrito(request)
    for item in carrito.carrito.values():
        producto_id = item["producto_id"]
        cantidad = item["cantidad"]
        producto = Producto.objects.get(id=producto_id)
        producto.stock = max(producto.stock - cantidad, 0)
        producto.save()
    carrito.limpiar()
    return redirect(reverse("tienda:store"))
