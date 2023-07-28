from django.urls import include, path

from .adapter._in.customer_api_contorller import CustomerApiController
from .adapter._in.customer_cust_memo_list_api_controller import CustomerCustMemoListApiController
from .adapter._in.customer_cust_taste_list_api_controller import CustomerCustTasteListApiController
from .adapter._in.customer_modify_cust_info_api_controller import CustomerModifyCustInfoApiController
from . import views

app_name = 'customer'

# 진입점 설정
urlpatterns = [
    # DefaultRouter() 에 등록 된 viewset 은 아래와 같이 path를 설정하지 않아도 자동으로 생성됨
    # path("test/", views.test_view),
    path("info/", CustomerApiController.as_view()),
    path("getCustMemoList/", CustomerCustMemoListApiController.as_view()),
    path("getCustTasteList/", CustomerCustTasteListApiController.as_view()),
    path("modifyCustInfo/", CustomerModifyCustInfoApiController.as_view()),
]
