from rest_framework import serializers


class PostRequestSerializer(serializers.Serializer):
    """
    # CLASS : Serializers
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/31 5:11 PM
    # DESCRIPTION
        - Stats Serializer

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/31          jung-gyuho          최초 생성
    """
    body = serializers.CharField(help_text="CRM Stats INFO PARAM JSON BODY", required=True)

    class Meta:
        ref_name = 'Stats_PostRequestSerializer'


class PostResponseSerializer(serializers.Serializer):
    status = serializers.CharField()

    class Meta:
        ref_name = 'Stats_PostResponseSerializer'
