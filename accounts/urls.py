from xml.dom.minidom import Document
from django.urls import path , include

from django.conf import settings
from django.conf.urls.static import static
from accounts import views


app_name = 'accounts'

urlpatterns = [
    path('registro/', views.registro, name='registro'),  
]
  