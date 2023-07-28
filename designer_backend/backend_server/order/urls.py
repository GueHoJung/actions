from django.urls import path

from . import views
from .adapter._in.order_prepaid_info_api_controller import OrderPrepaidInfoApiController
from .adapter._in.order_ticket_list_api_controller import OrderTicketListApiController
from .adapter._in.order_prepaid_history_list_api_controller import OrderPrepaidHistoryListApiController
from .adapter._in.order_ticket_history_list_api_controller import OrderTicketHistoryListApiController

app_name = 'order'

# 진입점 설정
urlpatterns = [
    # DefaultRouter() 에 등록 된 viewset 은 아래와 같이 path를 설정하지 않아도 자동으로 생성됨
    # path("test/", views.test_view),
    path("getPrpGridListAndSummary/", OrderPrepaidInfoApiController.as_view()),
    path("getTicketList/", OrderTicketListApiController.as_view()),
    path("getPrpHisGridList/", OrderPrepaidHistoryListApiController.as_view()),
    path("getTicketHistoryList/", OrderTicketHistoryListApiController.as_view())
]
