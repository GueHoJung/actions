import json
from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView

from .serializers import ItemSerializer
from .models import DesignerTest


# Create your views here.
# https://hangjastar.tistory.com/203
class ItemViewSet(viewsets.ModelViewSet):
    """
    # DESIGNER SERVER SELF DB
    ---
    ## 내용 : 데이터 베이스 테스트 입니다.
    ### /admin/ 에서 데이터 베이스를 확인할 수 있습니다.
    """
    queryset = DesignerTest.objects.all()
    serializer_class = ItemSerializer

task_id_query = openapi.Parameter('task_id', in_=openapi.IN_QUERY, description='task_id _in path', required=True,
                                      type=openapi.TYPE_NUMBER)
# api_view decorator django rest framework 방식
@api_view(["GET"])
# DRF Swagger Decorator
@swagger_auto_schema(tags=['LOGIN API by HRM SYSTEM'], operation_summary="HRM LOGIN API",
                         operation_description="DESIGNER SYSTEM에서 HRM SYSTEM으로 로그인 요청 API",
                         manual_parameters=[task_id_query], responses={200: 'Success'})
def designer_test(request):
    queryset = DesignerTest.objects.all()
    print("queryset : " + str(queryset))
    serializer = ItemSerializer(queryset, many=True)
    # print("serializer.data : "+str(serializer.data))
    # queryset_json = json.loads(serializers.serialize('json', queryset, ensure_ascii=False))
    # print("queryset_json : "+str(queryset_json))
    return Response(serializer.data)
    # return Response({"data": serializer.data}, status=status.HTTP_200_OK)
    # return JsonResponse({"data": queryset_json}, status=status.HTTP_200_OK)


# APIView django rest framework 방식
class DesignerTestAPI(APIView):
    def get(self, request):
        queryset = DesignerTest.objects.all()
        print(queryset)
        serializer = ItemSerializer(queryset, many=True)
        return Response(serializer.data)
