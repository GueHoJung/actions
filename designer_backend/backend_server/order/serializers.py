from rest_framework import serializers


class PostRequestSerializer(serializers.Serializer):
    """
    # CLASS : Serializers
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/28 6:48 PM
    # DESCRIPTION
        - Order Serializer

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/28          jung-gyuho          최초 생성
    """
    body = serializers.CharField(help_text="CRM Order INFO PARAM JSON BODY", required=True)

    class Meta:
        ref_name = 'Order_PostRequestSerializer'


class PostResponseSerializer(serializers.Serializer):
    status = serializers.CharField()

    class Meta:
        ref_name = 'Order_PostResponseSerializer'
