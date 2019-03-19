# coding=utf-8
from rest_framework import routers

from .views import WorksSingleViewSet

router = routers.SimpleRouter()
router.register(r'worksingle', WorksSingleViewSet, base_name='works_single')

# Definir rutas estáticas
urlpatterns = []

# Rutas dinámicas
urlpatterns += router.urls
