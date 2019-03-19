# coding=utf-8

from rest_framework import serializers
from rest_framework.serializers import ALL_FIELDS

from works_single_view.apps.worksingle.models import WorksSingle, Single, Source, SourceSingle, Contributors


class WorksSingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorksSingle
        fields = ALL_FIELDS


class SingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Single
        fields = ALL_FIELDS


class SourceSingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = SourceSingle
        fields = ALL_FIELDS


class ContributorsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributors
        fields = ALL_FIELDS


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributors
        fields = ALL_FIELDS


class WorksSingleSerializer(serializers.ModelSerializer):
    class Meta:
        model = WorksSingle
        fields = ALL_FIELDS
