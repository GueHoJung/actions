from django.urls import include, path

from . import views
from .adapter._in.analysis_api_controller import AnalysisApiController

app_name = 'analysis'

# 진입점 설정
urlpatterns = [
    # DefaultRouter() 에 등록 된 viewset 은 아래와 같이 path를 설정하지 않아도 자동으로 생성됨
    # path("test/", views.test_view),
    path("getCustDetailAnlys/", AnalysisApiController.as_view())
]
