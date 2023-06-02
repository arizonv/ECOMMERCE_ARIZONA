from distutils.command import upload
from pyexpat import model
from django.db import models


class Categorias(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre
    

class Marca(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre

class Producto(models.Model):

    OFERTA_CHOICES = [
        ('0', 'Sin oferta'),
        ('5', '5% de descuento'),
        ('10', '10% de descuento'),
        ('15', '15% de descuento'),
        ('20', '20% de descuento'),
        ('25', '25% de descuento'),
        ('30', '30% de descuento'),
        ('35', '35% de descuento'),
        ('40', '40% de descuento'),
        ('45', '45% de descuento'),
        ('50', '50% de descuento'),
    ]

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    precio = models.IntegerField()
    descripcion = models.TextField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    categoria = models.ForeignKey(Categorias, on_delete=models.PROTECT)
    stock = models.IntegerField(null=True, default=0)
    oferta = models.CharField(max_length=2, choices=OFERTA_CHOICES, default='0')
    nuevo = models.BooleanField()
    imagen = models.ImageField(upload_to='media/%Y/%m/%d', blank=True)
    
    @property
    def precio_descuento(self):
        descuento = int(self.oferta) # Convertir la cadena a entero
        precio_descuento = self.precio - ((descuento / 100) * self.precio) # Calcular el descuento
        return precio_descuento

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'productos'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['id']


class contacto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    numero = models.CharField(max_length=12)
    descripcion = models.TextField(max_length=150)
    region = models.CharField(max_length=50)
    comuna = models.CharField(max_length=50)
    
    def __str__(self):
        return self.nombre




    






