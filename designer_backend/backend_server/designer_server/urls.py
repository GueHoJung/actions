from django.urls import include, path
from rest_framework import routers
from . import views  # views.py import
from .serializers import ItemSerializer


app_name='designer_server_api'

router = routers.DefaultRouter()  # DefaultRouter를 설정
router.register("DesignerTest", views.ItemViewSet)  # router에 viewset 등록

# 진입점 설정
urlpatterns = [

    path("default/", include(router.urls)),
    path("test/", views.DesignerTestAPI.as_view()),
    path("designer_test/", views.designer_test),

]
