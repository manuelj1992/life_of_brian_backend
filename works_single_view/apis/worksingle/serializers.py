# coding=utf-8

from rest_framework import serializers
from rest_framework.serializers import ALL_FIELDS

from works_single_view.apps.worksingle.models import WorksSingle


class WorksSingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorksSingle
        fields = ALL_FIELDS
