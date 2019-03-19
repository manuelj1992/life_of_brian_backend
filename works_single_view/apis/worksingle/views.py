# coding=utf-8
from rest_framework import viewsets
from works_single_view.apps.worksingle.models import WorksSingle, Single, Source, SourceSingle, Contributors
from .serializers import WorksSingleSerializer, SingleSerializer, SourceSerializer, SourceSingleSerializer, ContributorsSerializer


class WorksSingleViewSet(viewsets.ModelViewSet):
    queryset = WorksSingle.objects.all()
    serializer_class = WorksSingleSerializer


class SingleViewSet(viewsets.ModelViewSet):
    queryset = Single.objects.all()
    serializer_class = SingleSerializer


class SourceSingleViewSet(viewsets.ModelViewSet):
    queryset = SourceSingle.objects.all()
    serializer_class = SourceSingleSerializer


class SourceViewSet(viewsets.ModelViewSet):
    queryset = Source.objects.all()
    serializer_class = SourceSerializer


class ContributorsViewSet(viewsets.ModelViewSet):
    queryset = Contributors.objects.all()
    serializer_class = ContributorsSerializer
