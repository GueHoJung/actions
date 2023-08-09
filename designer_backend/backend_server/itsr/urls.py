from django.urls import path

from . import views
# from .adapter._in.itsr_api_controller import ItsrApiController
from .adapter._in.itsr_save_sr_info_api_controller import ItsrSaveSrInfoApiController
from .adapter._in.itsr_sr_grid_list_api_controller import ItsrSrGridListApiController

app_name = 'itsr'

# 진입점 설정
urlpatterns = [
    # DefaultRouter() 에 등록 된 viewset 은 아래와 같이 path를 설정하지 않아도 자동으로 생성됨
    # path("test/", views.test_view),
    path("saveSrInfo/", ItsrSaveSrInfoApiController.as_view()),
    path("getSrGridList/", ItsrSrGridListApiController.as_view()),
]
