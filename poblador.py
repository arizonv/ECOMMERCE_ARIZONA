import os
from django.conf import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


import django
django.setup()

from django.db import models
from django.db.models.fields.files import ImageField
from tienda.models import Categorias, Marca, Producto, contacto
import random

# Generar datos ficticios para la tabla categorias
def generar_categorias(n):
    categorias = ['Electrónica', 'Informática', 'Audio y sonido', 'Telecomunicaciones', 'Videojuegos', 'Fotografía', 'Oficina', 'Hogar', 'Entretenimiento', 'Deportes']
    for i in range(n):
        categoria = Categorias(nombre=random.choice(categorias))
        categoria.save()

# Generar datos ficticios para la tabla marca
def generar_marcas(n):
    marcas = ['Samsung', 'Apple', 'Sony', 'LG', 'HP', 'Dell', 'Lenovo', 'Asus', 'Acer', 'Microsoft']
    for i in range(n):
        marca = Marca(nombre=random.choice(marcas))
        marca.save()

# Generar datos ficticios para la tabla producto
def generar_productos(n):
    productos = ['Smartphone', 'Laptop', 'Televisor', 'Tablet', 'Cámara', 'Reproductor de audio', 'Consola de videojuegos', 'Auriculares', 'Altavoz inteligente', 'Impresora']
    categorias = Categorias.objects.all()
    marcas = Marca.objects.all()
    for i in range(1, n+1):
        producto = Producto(
            nombre=random.choice(productos),
            precio=random.randint(1000, 5000),
            descripcion=f"Descripcion del producto {i}",
            marca=random.choice(marcas),
            categoria=random.choice(categorias),
            stock=random.randint(0, 100),
            oferta = random.choice([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50]),
            nuevo=random.choice([True, False]),
            imagen = r"static/resources/audifonos.jpg"
        )
        producto.save()

# Generar datos ficticios para la tabla contacto
def generar_contactos(n):
    regiones = ['Región de Arica y Parinacota', 'Región de Tarapacá', 'Región de Antofagasta', 'Región de Atacama', 
                'Región de Coquimbo', 'Región de Valparaíso', 'Región Metropolitana de Santiago', 'Región del Libertador General Bernardo O’Higgins',
                'Región del Maule', 'Región del Ñuble', 'Región del Biobío', 'Región de La Araucanía', 'Región de Los Ríos', 'Región de Los Lagos',
                'Región de Aysén del General Carlos Ibáñez del Campo', 'Región de Magallanes y de la Antártica Chilena']
    comunas = ['Santiago', 'Providencia', 'Las Condes', 'La Florida', 'Ñuñoa', 'Vitacura', 'Lo Barnechea', 'Maipú', 'La Reina', 'Estación Central']
    for i in range(n):
        C = contacto(
            nombre=f"Persona {i}",
            apellido=f"Apellido {i}",
            email=f"email{i}@correo.com",
            numero=f"+569{random.randint(10000000, 99999999)}",
            descripcion=f"Descripcion del contacto {i}",
            region=random.choice(regiones),
            comuna=random.choice(comunas)
        )
        C.save()

# Llamar a las funciones para poblar la base de datos
generar_categorias(5)
generar_marcas(3)
generar_productos(10)
generar_contactos(5)



















       