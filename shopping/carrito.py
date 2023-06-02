from django.contrib import messages
from django.shortcuts import render, HttpResponse, redirect
from django.urls import reverse

from tienda.models import Producto

class Carrito:
    LIMITE_PRODUCTOS = 4

    def __init__(self, request):
        self.request = request
        self.session = request.session
        self.carrito = self.session.get("carrito", {})

    def obtener_producto(self, producto_id):
        return Producto.objects.get(id=producto_id)

    def procesar_operacion(self, request, producto_id, operacion):
        producto = self.obtener_producto(producto_id)
        if operacion == 'agregar':
            cantidad = int(request.POST.get('cantidad', 1))
            if cantidad > producto.stock:
                mensaje = 'La cantidad ingresada supera el stock disponible.'
                messages.warning(request, mensaje)
                return redirect(reverse("tienda:store"))
            self.agregar(producto, cantidad)
        elif operacion == 'eliminar':
            self.eliminar(producto)
        elif operacion == 'restar':
            self.restar(producto)
        return redirect(reverse("tienda:store"))

    def agregar(self, producto, cantidad):
        id = str(producto.id)
        if id not in self.carrito:
            # Producto no existe en el carrito
            cantidad_nueva = min(cantidad, producto.stock)
            self.carrito[id] = {
                "producto_id": producto.id,
                "nombre": producto.nombre,
                "precio_uni": producto.precio,
                "oferta": producto.oferta,
                "acumulado": self.calcular_acumulado(producto, cantidad_nueva),
                "cantidad": cantidad_nueva,
                "stock": producto.stock - cantidad_nueva,
            }
        else:
            # Producto ya existe en el carrito
            cantidad_actual = self.carrito[id]["cantidad"]
            cantidad_total = cantidad_actual + cantidad

            if cantidad_total > self.LIMITE_PRODUCTOS:
                cantidad_nueva = self.LIMITE_PRODUCTOS - cantidad_actual
                mensaje = f"Solo se pueden agregar {self.LIMITE_PRODUCTOS} unidades del producto '{producto.nombre}' al carrito."
                messages.info(self.request, mensaje)
            else:
                cantidad_nueva = min(cantidad_total, producto.stock) - cantidad_actual
                self.carrito[id]["cantidad"] += cantidad_nueva
                self.carrito[id]["acumulado"] += self.calcular_acumulado(producto, cantidad_nueva)
                self.carrito[id]["stock"] = max(producto.stock - self.carrito[id]["cantidad"], 0)
        self.guardar_carrito()

    def calcular_acumulado(self, producto, cantidad):
        if producto.oferta != '0':
            return producto.precio_descuento * cantidad
        else:
            return producto.precio * cantidad

    def guardar_carrito(self):
        self.session["carrito"] = self.carrito
        self.session.modified = True

    def eliminar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            del self.carrito[id]
            self.guardar_carrito()

    def restar(self, producto):
        id = str(producto.id)
        if id in self.carrito:
            self.carrito[id]["cantidad"] -= 1
            if producto.oferta != '0':
                self.carrito[id]["acumulado"] -= producto.precio_descuento
            else:
                self.carrito[id]["acumulado"] -= producto.precio
            if self.carrito[id]["cantidad"] <= 0:
                self.eliminar(producto)
            self.guardar_carrito()

    def cantidad_total(self):
        total = 0
        for item in self.carrito.values():
            total += item['cantidad']
        return total

    def limpiar(self):
        self.session["carrito"] = {}
        self.session.modified = True
