# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from django.conf import settings
#
#
# # 아래 test_view() 함수 주석을 풀면, LoginService의 crm login 함수가 실행되는 현상 발생, docker-compose up 또는 컨테이너 restart 시에도 발생
# # Create your views here.
# @api_view(['GET'])
# def test_view(request):
#     API_HOST = getattr(settings, "CRM_HOST_IP", None)
#     API_PORT = getattr(settings, "CRM_HOST_PORT", None)
#
#     return Response({"test": "테스트입니다.", "API_HOST": API_HOST, "API_PORT": API_PORT})
