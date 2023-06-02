from xml.dom.minidom import Document
from django.urls import path , include
from tienda import views
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.db import router 
from django.views.generic import TemplateView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include('tienda.urls')),
    path('shop/', include('shopping.urls')),
    path('auth/', include('accounts.urls')),
    path('accounts/' , include('django.contrib.auth.urls') , name = 'login'),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


