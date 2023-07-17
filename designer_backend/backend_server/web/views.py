from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import ImageUpload
from .serializers import ItemSerializer

# Create your views here.
class ItemViewSet(viewsets.ModelViewSet):
    queryset = ImageUpload.objects.all()
    serializer_class = ItemSerializer
def index(request):
    image = ImageUpload.objects.all()
    return render(request, 'web/index.html', {'image': image})

@api_view(["GET"])
def image_test(request):
    queryset = ImageUpload.objects.all()
    serializer = ItemSerializer(queryset, many=True)
    return Response(serializer.data)