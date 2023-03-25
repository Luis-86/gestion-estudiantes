from rest_framework import routers
from .viewset import *

router = routers.SimpleRouter()
router.register('api/v1.0/bus', BusViewset)
router.register('api/v1.0/ruta', RutaViewset)
urlpatterns = router.urls
