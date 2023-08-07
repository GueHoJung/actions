from django.urls import path

from . import views
from .adapter._in.stats_yearly_sales_user_performance_api_controller import StatsYearlySalesUserPerformanceApiController
from .adapter._in.stats_monthly_sales_user_performance_api_controller import StatsMonthlySalesUserPerformanceApiController
from .adapter._in.stats_daily_sales_user_performance_api_controller import StatsDailySalesUserPerformanceApiController
from .adapter._in.stats_yearly_sales_user_sales_api_controller import StatsYearlySalesUserSalesApiController
from .adapter._in.stats_monthly_sales_user_sales_api_controller import StatsMonthlySalesUserSalesApiController
from .adapter._in.stats_daily_sales_user_sales_api_controller import StatsDailySalesUserSalesApiController
from .adapter._in.stats_yearly_sales_user_order_type_sales_api_controller import StatsYearlySalesUserOrderTypeSalesApiController
from .adapter._in.stats_daily_sales_user_order_type_sales_api_controller import StatsDailySalesUserOrderTypeSalesApiController
from .adapter._in.stats_daily_product_user_performance_api_controller import StatsDailyProductUserPerformanceApiController
from .adapter._in.stats_monthly_product_user_performance_api_controller import StatsMonthlyProductUserPerformanceApiController

app_name = 'stats'

# 진입점 설정
urlpatterns = [
    # DefaultRouter() 에 등록 된 viewset 은 아래와 같이 path를 설정하지 않아도 자동으로 생성됨
    # path("test/", views.test_view),
    path("getYearlySalesUserPerformance/", StatsYearlySalesUserPerformanceApiController.as_view()),
    path("getMonthlySalesUserPerformance/", StatsMonthlySalesUserPerformanceApiController.as_view()),
    path("getDailySalesUserPerformance/", StatsDailySalesUserPerformanceApiController.as_view()),
    path("getYearlySalesUserSales/", StatsYearlySalesUserSalesApiController.as_view()),
    path("getMonthlySalesUserSales/", StatsMonthlySalesUserSalesApiController.as_view()),
    path("getDailySalesUserSales/", StatsDailySalesUserSalesApiController.as_view()),
    path("getYearlySalesUserOrdTypeSales/", StatsYearlySalesUserOrderTypeSalesApiController.as_view()),
    path("getSalesUserOrdTypeSales/", StatsDailySalesUserOrderTypeSalesApiController.as_view()),
    path("getDailyProductUserPerformance/", StatsDailyProductUserPerformanceApiController.as_view()),
    path("getMonthlyProductUserPerformance/", StatsMonthlyProductUserPerformanceApiController.as_view()),
]
