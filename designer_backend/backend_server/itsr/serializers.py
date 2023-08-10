from rest_framework import serializers


class PostRequestSerializer(serializers.Serializer):
    """
    # CLASS : Serializers
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/09 2:32 PM
    # DESCRIPTION
        - Itsr Serializer

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/09          jung-gyuho          최초 생성
    """
    body = serializers.CharField(help_text="CRM Itsr INFO PARAM JSON BODY", required=True)

    class Meta:
        ref_name = 'Itsr_PostRequestSerializer'


class PostResponseSerializer(serializers.Serializer):
    status = serializers.CharField()

    class Meta:
        ref_name = 'Itsr_PostResponseSerializer'
