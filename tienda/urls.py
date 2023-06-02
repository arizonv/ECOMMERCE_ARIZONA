from xml.dom.minidom import Document
from django.urls import path , include

from django.conf import settings
from django.conf.urls.static import static
from django.db import router
from tienda import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register("producto", views.ProductoViewSet)

app_name = 'tienda'

urlpatterns = [
    path('store', views.store, name='store'),
    path('Contacto', views.contacto, name='contacto'),
    path('api/', include(router.urls)),
    path('detalle/<id>', views.detalleProducto, name='detalle'),
    path('listar/', views.listarProductos, name='listar'),
    path('addproducto/', views.addProducto, name='addproducto'),
    path('producto/<int:product_id>/modificar/', views.modificar, name='modificar'),
    path('eliminar/<int:product_id>/', views.eliminar_producto, name='eliminar'),
]
  