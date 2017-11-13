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
from Usuario.views import *
from Inmueble.views import *
from rest_framework import routers, serializers, viewsets
router = routers.DefaultRouter()
router.register(r'usuario', UsuarioViewSet, r'usuario')
router.register(r'inmueble', InmuebleViewSet, r'inmueble')
urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'api/', include(router.urls, namespace='api')),
    url(r'^$', index_view, {}, name="index"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

