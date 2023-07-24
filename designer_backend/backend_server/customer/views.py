from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET'])
def test_view(request):
    CRM_HOST_IP = env('CRM_HOST_IP')  # SECEREY_KEY 값 불러오기
    CRM_HOST_PORT = env('CRM_HOST_PORT')  # DEBUG 값 불러오기

    return Response({"test": "테스트입니다.","SECRET_KEY":CRM_HOST_IP, "CRM_HOST_PORT":CRM_HOST_PORT})
