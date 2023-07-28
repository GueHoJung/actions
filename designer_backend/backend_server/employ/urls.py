from django.urls import path

from . import views
from .adapter._in.employ_api_controller import EmployApiController

app_name = 'employ'

# 진입점 설정
urlpatterns = [
    # DefaultRouter() 에 등록 된 viewset 은 아래와 같이 path를 설정하지 않아도 자동으로 생성됨
    # path("test/", views.test_view),
    path("getUserApntList/", EmployApiController.as_view())
]
