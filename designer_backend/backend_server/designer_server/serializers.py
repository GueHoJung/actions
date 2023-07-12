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
