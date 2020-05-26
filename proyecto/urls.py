"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('clientes/', include('clientes.urls')),
                  path('productos/', include('productos.urls')),
                  path('laboratorios/', include('laboratorio.urls')),
                  path('proveedor/', include('proveedor.urls')),
                  path('factura/', include('factura.urls')),
                  path('compras/', include('compras.urls')),
                  path('usuarios/', include('userProfile.urls')),
                  path('accounts/', include('django.contrib.auth.urls')),
                  path('api/v1.0/', include('api.urls')),
                  path('', login_required(TemplateView.as_view(template_name='registration/home.html')), name='index')
              ]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
