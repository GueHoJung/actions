from rest_framework import serializers


class PostRequestSerializer(serializers.Serializer):
    """
    # CLASS : PostRequestSerializer
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/21 9:20 PM
    # DESCRIPTION
        - 고객 관련 REQUEST API Serializer
    """
    body = serializers.CharField(help_text="CRM CUSTOMER INFO PARAM JSON BODY", required=True)

    class Meta:
        ref_name = 'Customer_PostRequestSerializer'


class PostResponseSerializer(serializers.Serializer):
    status = serializers.CharField()

    class Meta:
        ref_name = 'Customer_PostResponseSerializer'
