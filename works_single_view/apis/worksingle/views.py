# coding=utf-8
from rest_framework import viewsets
from works_single_view.apps.worksingle.models import WorksSingle
from .serializers import WorksSingleSerializer


class WorksSingleViewSet(viewsets.ModelViewSet):
    queryset = WorksSingle.objects.all()
    serializer_class = WorksSingleSerializer
