# coding=utf-8
from rest_framework import routers

from .views import WorksSingleViewSet, SingleViewSet, SourceSingleViewSet, ContributorsViewSet, SourceViewSet

router = routers.SimpleRouter()
router.register(r'worksingle', WorksSingleViewSet, base_name='works_single')
router.register(r'single', SingleViewSet, base_name='single')
router.register(r'source_single', SourceSingleViewSet, base_name='source_single')
router.register(r'contributors', ContributorsViewSet, base_name='contributors')
router.register(r'source', SourceViewSet, base_name='source')

# Definir rutas estáticas
urlpatterns = []

# Rutas dinámicas
urlpatterns += router.urls
