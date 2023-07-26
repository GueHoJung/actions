from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

# 아래 test_view() 함수 주석을 풀면, LoginService의 crm login 함수가 실행되는 현상 발생, docker-compose up 또는 컨테이너 restart 시에도 발생
# Create your views here.
# @api_view(['GET'])
# def test_view(request):
#     CRM_HOST_IP = env('CRM_HOST_IP')  # SECEREY_KEY 값 불러오기
#     CRM_HOST_PORT = env('CRM_HOST_PORT')  # DEBUG 값 불러오기
#
#     return Response({"test": "테스트입니다.","SECRET_KEY":CRM_HOST_IP, "CRM_HOST_PORT":CRM_HOST_PORT})
