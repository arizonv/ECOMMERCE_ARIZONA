from django.contrib import admin
from .models import Marca,Producto,contacto,Categorias
# Register your models here.


class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio", "categoria","stock","oferta","nuevo"]
    list_editable = ["precio","oferta","nuevo"]
    search_fields = ["nombre","stock"]
    list_filter = ["categoria"]
    list_per_page = 10

admin.site.register(Marca)
admin.site.register(Categorias)
admin.site.register(Producto,ProductoAdmin)
admin.site.register(contacto)
