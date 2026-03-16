from rest_framework import routers
from .api import UsuarioViewSet, ProductoViewSet
router = routers.DefaultRouter()

router.register('api/usuarios', UsuarioViewSet, 'usuarios')
router.register('api/productos', ProductoViewSet, 'productos')

urlpatterns = router.urls