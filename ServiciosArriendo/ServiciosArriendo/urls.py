"""ServiciosArriendo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url, include
from django.contrib import admin
# from Usuario.views import *
from Inmueble.views import *
from Codeudor.views import *
from Archivo.views import *
from Arrendatario.views import *
from Arrendador.views import *
from Administrador.views import *
from ContratoLey.views import *
from Contrato.views import *
from Habitacion.views import *
from Ley.views import *
from Pago.views import *
from django.views.generic import TemplateView

from rest_framework import routers, serializers, viewsets
router = routers.DefaultRouter()
# router.register(r'usuario', UsuarioViewSet, r'usuario')
router.register(r'arrendatario', ArrendatarioViewSet, r'arrendatario')
router.register(r'arrendador', ArrendadorViewSet, r'arrendador')
router.register(r'administrador', AdministradorViewSet, r'administrador')
router.register(r'inmueble', InmuebleViewSet, r'inmueble')
router.register(r'codeudor', CodeudorViewSet, r'codeudor')
router.register(r'archivo', ArchivoViewSet, r'archivo')
router.register(r'contrato', ContratoViewSet, r'contrato')
router.register(r'contratoley', ContratoLeyViewSet, r'contratoley')
router.register(r'habitacion', HabitacionViewSet, r'habitacion')
router.register(r'ley', LeyViewSet, r'ley')
router.register(r'pago', PagoViewSet, r'pago')

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home/', TemplateView.as_view(template_name='index.html')),
    url(r'^vermas/', TemplateView.as_view(template_name='vermas.html')),
    url(r'^usuarios/', TemplateView.as_view(template_name='verusuarios.html')),
    url(r'^administrador/', TemplateView.as_view(template_name='veradministrador.html')),
    url(r'^arrendador/', TemplateView.as_view(template_name='verarrendador.html')),
    url(r'^administrador/', include('Administrador.urls')),
    url(r'^apiusuario/', include('Usuario.urls')),
    url(r'api/', include(router.urls, namespace='api')),
    # url(r'^$', index_view, {}, name="index"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


