from rest_framework import serializers
# from .models import AdCampaigns
from . import models


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.DesignerTest
        fields = "__all__"
        # fields = ('name', 'description', 'cost')
        # fields = ('id','weight','image_url', 'landing_url', 'reward')

        # 옵션
        ordering_fields = 'id'


class GetRequestSerializer(serializers.Serializer):
    param1 = serializers.CharField(help_text="HRM LOGIN PARAM JSON BODY", required=True)


class GetResponseSerializer(serializers.Serializer):
    param1 = serializers.CharField(help_text="HRM LOGIN PARAM JSON BODY", required=True)


class PostRequestSerializer(serializers.Serializer):
    body = serializers.CharField(help_text="HRM LOGIN PARAM JSON BODY", required=True)


class PostResponseSerializer(serializers.Serializer):
    status = serializers.CharField()
