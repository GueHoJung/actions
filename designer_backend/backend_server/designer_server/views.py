from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
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
    serializer = ItemSerializer(queryset, many=True)
    return Response(serializer.data)

# APIView django rest framework 방식
class DesignerTestAPI(APIView):
    def get(self, request):
        queryset = DesignerTest.objects.all()
        print(queryset)
        serializer = ItemSerializer(queryset)
        return Response(serializer.data)
