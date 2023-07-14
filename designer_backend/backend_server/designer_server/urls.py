from django.urls import include, path
from rest_framework import routers
from . import views  # views.py import


app_name='designer_server_api'

router = routers.DefaultRouter()  # DefaultRouter를 설정
router.register("DesignerTest", views.ItemViewSet)  # router에 viewset 등록

# 진입점 설정
urlpatterns = [
    # DefaultRouter() 에 등록 된 viewset 은 아래와 같이 path를 설정하지 않아도 자동으로 생성됨
    path("default/", include(router.urls)),
    # APIView 방식 테스트
    path("test/", views.DesignerTestAPI.as_view()),
    # api_view decorator 방식 테스트
    path("designer_test/", views.designer_test),

]
