from django.urls import include, path
from rest_framework import routers
from . import views  # views.py import


app_name='web'

router = routers.DefaultRouter()  # DefaultRouter를 설정
router.register("ImageUpload", views.ItemViewSet)  # router에 viewset 등록

# 진입점 설정
urlpatterns = [
    path('',views.index)

]