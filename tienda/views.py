from email import message
from django.forms import PasswordInput
from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponse
import random
from tienda.models import Categorias, Marca, Producto
from .forms import ContactoForm,ProductoForm
from django.contrib import messages
from django.http import Http404
import json

from .serializers import productoSerializer
from rest_framework import viewsets
from django.db.models import Q
from django.contrib.auth.decorators import user_passes_test
from decorators import admin_required,client_required

from shopping.carrito import Carrito


class ProductoViewSet(viewsets.ModelViewSet):
    queryset =Producto.objects.all()
    serializer_class = productoSerializer


def home(request):
    return render(request, 'home.html', {'name': 'gvrrido'})


def store(request):
    carrito = Carrito(request)
    busqueda = request.POST.get("buscador")
    print(f"Valor de búsqueda: {busqueda}")  # Impresión para depuración
    productos = Producto.objects.order_by('nombre')
    if busqueda:
        productos = Producto.objects.filter(
            Q(nombre__startswith=busqueda) |
            Q(precio__icontains=busqueda)
        ).order_by('nombre').distinct()
    data = {
        'entity': productos,
        'title': 'LISTADO DE PRODUCTOS',
        'total_productos_carrito': carrito.cantidad_total()
    }
    return render(request, 'store.html', data)



def contacto(request):
    with open('resource/regiones-comunas.json', encoding='utf-8') as f:
        try:
            rc = json.load(f)
            print(rc)
        except ValueError:
            print("El archivo JSON está mal formateado")
    regiones = [(r['name']) for r in rc['regions']]
    comunas = {r['name']: r['communes'] for r in rc['regions']}
    form = ContactoForm()
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            print("mensaje exitoso")
            form = ContactoForm()  # Crear una nueva instancia del formulario vacío
        else:
            form = formulario  # Asignar el formulario no válido a la variable 'form'     
    return render(request, 'contacto.html', {'form': form, 'regiones': regiones, 'comunas': comunas})


def detalleProducto(request,id):
    producto = get_object_or_404(Producto,id=id)
    context = {
        'producto': producto
    }
    return render(request, 'producto/detalle.html', context )


def addProducto(request):
    data = {
        'form' : ProductoForm()
    }

    if request.method == 'POST':
        formulario = ProductoForm(data=request.POST, files=request.FILES)

        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Registro agregado correctamente")
            return redirect(to="/listar")
        else:
            data["form"] = formulario   
    return render(request, 'producto/agregar.html', data)


def listarProductos(request):
    busqueda = request.POST.get("buscador")
    lista_productos = Producto.objects.order_by('nombre')
    if busqueda:
        lista_productos = Producto.objects.filter(
            Q(nombre__startswith=busqueda) |
            Q(precio__icontains=busqueda)
        ).order_by('nombre').distinct()
    try:
        lista_productos = lista_productos
    except:
        raise Http404

    data = {'entity': lista_productos,
            'title': 'LISTADO DE PRODUCTOS',
            }
    return render(request, 'producto/listar.html', data)




def modificar(request, product_id):
    producto = get_object_or_404(Producto, id=product_id)

    if request.method == 'POST':
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'producto/modificar.html', {'form': form})




def eliminar_producto(request, product_id):
    producto = get_object_or_404(Producto, id=product_id)
    producto.delete()
    return redirect('tienda:listar')



