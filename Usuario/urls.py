from Usuario.views import *
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'usuario', UsuarioViewSet, r'usuario')

urlpatterns = router.urls