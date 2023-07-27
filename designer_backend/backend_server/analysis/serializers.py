from rest_framework import serializers


class PostRequestSerializer(serializers.Serializer):
    """
    # CLASS : Serializers
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/27 5:55 PM
    # DESCRIPTION
        - Analysis Serializer

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/27          jung-gyuho          최초 생성
    """
    body = serializers.CharField(help_text="CRM ANALYSIS INFO PARAM JSON BODY", required=True)

    class Meta:
        ref_name = 'Analysis_PostRequestSerializer'


class PostResponseSerializer(serializers.Serializer):
    status = serializers.CharField()

    class Meta:
        ref_name = 'Analysis_PostResponseSerializer'
