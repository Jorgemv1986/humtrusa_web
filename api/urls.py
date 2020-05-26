from rest_framework import routers

from api.viewsets import ClientesViewSet

router = routers.SimpleRouter()
router.register('clientes', ClientesViewSet)

urlpatterns = router.urls
