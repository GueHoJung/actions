from django.urls import include, path

from . import views
from .adapter._in.analysis_api_controller import AnalysisApiController
from .adapter._in.analysis_product_user_sales_api_controller import AnalysisProductUserSalesApiController
from .adapter._in.analysis_prepaid_user_sales_api_controller import AnalysisPrepaidUserSalesApiController
from .adapter._in.analysis_dash_board_info_api_controller import AnalysisDashBoardInfoApiController
from .adapter._in.analysis_product_sub_user_sales_api_controller import AnalysisProductSubUserSalesApiController
from .adapter._in.analysis_ticket_user_sales_api_controller import AnalysisTicketUserSalesApiController
from .adapter._in.analysis_trm_type_user_sales_api_controller import AnalysisTrmTypeUserSalesApiController
from .adapter._in.analysis_user_product_sales_rank_api_controller import AnalysisUserProductSalesRankApiController
from .adapter._in.analysis_monthly_cust_type_anlys_api_controller import AnalysisMonthlyCustTypeAnlysApiController
from .adapter._in.analysis_weekly_cust_type_anlys_api_controller import AnalysisWeeklyCustTypeAnlysApiController
from .adapter._in.analysis_daily_cust_type_anlys_api_controller import AnalysisDailyCustTypeAnlysApiController
from .adapter._in.analysis_user_sales_rank_api_controller import AnalysisUserSalesRankApiController
from .adapter._in.analysis_monthly_synthesis_anlys_api_controller import AnalysisMonthlySynthesisAnlysApiController
from .adapter._in.analysis_weekly_synthesis_anlys_api_controller import AnalysisWeeklySynthesisAnlysApiController
from .adapter._in.analysis_daily_synthesis_anlys_api_controller import AnalysisDailySynthesisAnlysApiController
from .adapter._in.analysis_monthly_cust_membership_anlys_api_controller import AnalysisMonthlyCustMembershipAnlysApiController
from .adapter._in.analysis_weekly_cust_membership_anlys_api_controller import AnalysisWeeklyCustMembershipAnlysApiController
from .adapter._in.analysis_daily_cust_membership_anlys_api_controller import AnalysisDailyCustMembershipAnlysApiController
from .adapter._in.analysis_user_prepaid_sales_rank_api_controller import AnalysisUserPrepaidSalesRankApiController
from .adapter._in.analysis_monthly_cust_prepaid_anlys_api_controller import AnalysisMonthlyCustPrepaidAnlysApiController
from .adapter._in.analysis_weekly_cust_prepaid_anlys_api_controller import AnalysisWeeklyCustPrepaidAnlysApiController
from .adapter._in.analysis_daily_cust_prepaid_anlys_api_controller import AnalysisDailyCustPrepaidAnlysApiController

app_name = 'analysis'

# 진입점 설정
urlpatterns = [
    # DefaultRouter() 에 등록 된 viewset 은 아래와 같이 path를 설정하지 않아도 자동으로 생성됨
    # path("test/", views.test_view),
    path("getCustDetailAnlys/", AnalysisApiController.as_view()),
    path("getProductUserSales/", AnalysisProductUserSalesApiController.as_view()),
    path("getPrepaidUserSales/", AnalysisPrepaidUserSalesApiController.as_view()),
    path("getDashBoardInfo/", AnalysisDashBoardInfoApiController.as_view()),
    path("getProductSubUserSales/", AnalysisProductSubUserSalesApiController.as_view()),
    path("getTicketUserSales/", AnalysisTicketUserSalesApiController.as_view()),
    path("getTrmTypeUserSales/", AnalysisTrmTypeUserSalesApiController.as_view()),
    path("getUserProductSalesRank/", AnalysisUserProductSalesRankApiController.as_view()),
    path("getMonthlyCustTypeAnlys/", AnalysisMonthlyCustTypeAnlysApiController.as_view()),
    path("getWeeklyCustTypeAnlys/", AnalysisWeeklyCustTypeAnlysApiController.as_view()),
    path("getDailyCustTypeAnlys/", AnalysisDailyCustTypeAnlysApiController.as_view()),
    path("getUserSalesRank/", AnalysisUserSalesRankApiController.as_view()),
    path("getMonthlySynthesisAnlys/", AnalysisMonthlySynthesisAnlysApiController.as_view()),
    path("getWeeklySynthesisAnlys/", AnalysisWeeklySynthesisAnlysApiController.as_view()),
    path("getDailySynthesisAnlys/", AnalysisDailySynthesisAnlysApiController.as_view()),
    path("getMonthlyCustMembershipAnlys/", AnalysisMonthlyCustMembershipAnlysApiController.as_view()),
    path("getWeeklyCustMembershipAnlys/", AnalysisWeeklyCustMembershipAnlysApiController.as_view()),
    path("getDailyCustMembershipAnlys/", AnalysisDailyCustMembershipAnlysApiController.as_view()),
    path("getUserPrepaidSalesRank/", AnalysisUserPrepaidSalesRankApiController.as_view()),
    path("getMonthlyCustPrepaidAnlys/", AnalysisMonthlyCustPrepaidAnlysApiController.as_view()),
    path("getWeeklyCustPrepaidAnlys/", AnalysisWeeklyCustPrepaidAnlysApiController.as_view()),
    path("getDailyCustPrepaidAnlys/", AnalysisDailyCustPrepaidAnlysApiController.as_view()),
]
