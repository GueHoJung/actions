from django.shortcuts import render
from rest_framework import viewsets

from .models import ImageUpload
from .serializers import ItemSerializer

# Create your views here.
class ItemViewSet(viewsets.ModelViewSet):
    queryset = ImageUpload.objects.all()
    serializer_class = ItemSerializer
def index(request):
    image = ImageUpload.objects.all()
    return render(request, 'web/index.html', {'image': image})