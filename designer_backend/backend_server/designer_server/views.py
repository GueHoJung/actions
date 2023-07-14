import json
from django.shortcuts import render
from django.core import serializers
from django.http import JsonResponse

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
    queryset = DesignerTest.objects.all()
    serializer_class = ItemSerializer

# api_view decorator django rest framework 방식
@api_view(["GET"])
def designer_test(request):
    queryset = DesignerTest.objects.all()
    print("queryset : "+str(queryset))
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
