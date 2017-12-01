from Administrador.views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'administrador', AdministradorViewSet, r'administrador')

urlpatterns = router.urls