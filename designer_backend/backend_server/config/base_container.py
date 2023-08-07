from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration

from designer_server.application.service.login_service import LoginService
from designer_server.application.port._in.login_in_port import LoginInHrmAPI
from designer_server.application.port._in.login_in_port import LoginInCrmAPI
from designer_server.application.port.out.login_out_port import LoginOutHrmAPI
from designer_server.application.port.out.login_out_port import LoginOutCrmAPI
from designer_server.adapter.out.login_hrm_api_adapter import LoginHrmApiAdapter
from designer_server.adapter.out.login_crm_api_adapter import LoginCrmApiAdapter

from reservation.application.service.reservation_service import ReservationService
from reservation.application.port.out.reservation_out_port import ReservationOutCrmAPI
from reservation.application.port._in.reservation_in_port import ReservationInCrmImpl
from reservation.adapter.out.reservation_api_adapter import ReservationApiAdapter

from customer.adapter.out.customer_api_adapter import CustomerApiAdapter
from customer.application.port.out.customer_out_port import CustomerOutCrmImpl
from customer.application.port._in.customer_in_port import CustomerInCrmImpl
from customer.application.service.customer_service import CustomerService

from analysis.adapter.out.analysis_api_adapter import AnalysisApiAdapter
from analysis.application.port.out.analysis_out_port import AnalysisOutCrmImpl
from analysis.application.port._in.analysis_in_port import AnalysisInCrmImpl
from analysis.application.service.analysis_service import AnalysisService

from employ.adapter.out.employ_api_adapter import EmployApiAdapter
from employ.application.port.out.employ_out_port import EmployOutHrmImpl
from employ.application.port._in.employ_in_port import EmployInHrmImpl
from employ.application.service.employ_service import EmployService

from order.adapter.out.order_prepaid_info_api_adapter import OrderPrepaidInfoApiAdapter
from order.application.port.out.order_prepaid_info_out_port import OrderPrepaidInfoOutCrmImpl
from order.application.port._in.order_prepaid_info_in_port import OrderPrepaidInfoInCrmImpl
from order.application.service.order_prepaid_info_service import OrderPrepaidInfoService

from order.adapter.out.order_ticket_list_api_adapter import OrderTicketListApiAdapter
from order.application.port.out.order_ticket_list_out_port import OrderTicketListOutCrmImpl
from order.application.port._in.order_ticket_list_in_port import OrderTicketListInCrmImpl
from order.application.service.order_ticket_list_service import OrderTicketListService

from order.adapter.out.order_prepaid_history_list_api_adapter import OrderPrepaidHistoryListApiAdapter
from order.application.port.out.order_prepaid_history_list_out_port import OrderPrepaidHistoryListOutCrmImpl
from order.application.port._in.order_prepaid_history_list_in_port import OrderPrepaidHistoryListInCrmImpl
from order.application.service.order_prepaid_history_list_service import OrderPrepaidHistoryListService

from order.adapter.out.order_ticket_history_list_api_adapter import OrderTicketHistoryListApiAdapter
from order.application.port.out.order_ticket_history_list_out_port import OrderTicketHistoryListOutCrmImpl
from order.application.port._in.order_ticket_history_list_in_port import OrderTicketHistoryListInCrmImpl
from order.application.service.order_ticket_history_list_service import OrderTicketHistoryListService

from customer.adapter.out.customer_cust_memo_list_api_adapter import CustomerCustMemoListApiAdapter
from customer.application.port.out.customer_cust_memo_list_out_port import CustomerCustMemoListOutCrmImpl
from customer.application.port._in.customer_cust_memo_list_in_port import CustomerCustMemoListInCrmImpl
from customer.application.service.customer_cust_memo_list_service import CustomerCustMemoListService

from customer.adapter.out.customer_cust_taste_list_api_adapter import CustomerCustTasteListApiAdapter
from customer.application.port.out.customer_cust_taste_list_out_port import CustomerCustTasteListOutCrmImpl
from customer.application.port._in.customer_cust_taste_list_in_port import CustomerCustTasteListInCrmImpl
from customer.application.service.customer_cust_taste_list_service import CustomerCustTasteListService

from customer.adapter.out.customer_modify_cust_info_api_adapter import CustomerModifyCustInfoApiAdapter
from customer.application.port.out.customer_modify_cust_info_out_port import CustomerModifyCustInfoOutCrmImpl
from customer.application.port._in.customer_modify_cust_info_in_port import CustomerModifyCustInfoInCrmImpl
from customer.application.service.customer_modify_cust_info_service import CustomerModifyCustInfoService

from order.adapter.out.order_visit_history_list_api_adapter import OrderVisitHistoryListApiAdapter
from order.application.port.out.order_visit_history_list_out_port import OrderVisitHistoryListOutCrmImpl
from order.application.port._in.order_visit_history_list_in_port import OrderVisitHistoryListInCrmImpl
from order.application.service.order_visit_history_list_service import OrderVisitHistoryListService

from order.adapter.out.order_visit_history_detail_api_adapter import OrderVisitHistoryDetailApiAdapter
from order.application.port.out.order_visit_history_detail_out_port import OrderVisitHistoryDetailOutCrmImpl
from order.application.port._in.order_visit_history_detail_in_port import OrderVisitHistoryDetailInCrmImpl
from order.application.service.order_visit_history_detail_service import OrderVisitHistoryDetailService

from analysis.adapter.out.analysis_product_user_sales_api_adapter import AnalysisProductUserSalesApiAdapter
from analysis.application.port.out.analysis_product_user_sales_out_port import AnalysisProductUserSalesOutCrmImpl
from analysis.application.port._in.analysis_product_user_sales_in_port import AnalysisProductUserSalesInCrmImpl
from analysis.application.service.analysis_product_user_sales_service import AnalysisProductUserSalesService

from analysis.adapter.out.analysis_prepaid_user_sales_api_adapter import AnalysisPrepaidUserSalesApiAdapter
from analysis.application.port.out.analysis_prepaid_user_sales_out_port import AnalysisPrepaidUserSalesOutCrmImpl
from analysis.application.port._in.analysis_prepaid_user_sales_in_port import AnalysisPrepaidUserSalesInCrmImpl
from analysis.application.service.analysis_prepaid_user_sales_service import AnalysisPrepaidUserSalesService

from analysis.adapter.out.analysis_dash_board_info_api_adapter import AnalysisDashBoardInfoApiAdapter
from analysis.application.port.out.analysis_dash_board_info_out_port import AnalysisDashBoardInfoOutCrmImpl
from analysis.application.port._in.analysis_dash_board_info_in_port import AnalysisDashBoardInfoInCrmImpl
from analysis.application.service.analysis_dash_board_info_service import AnalysisDashBoardInfoService

from stats.adapter.out.stats_yearly_sales_user_performance_api_adapter import StatsYearlySalesUserPerformanceApiAdapter
from stats.application.port.out.stats_yearly_sales_user_performance_out_port import \
    StatsYearlySalesUserPerformanceOutCrmImpl
from stats.application.port._in.stats_yearly_sales_user_performance_in_port import \
    StatsYearlySalesUserPerformanceInCrmImpl
from stats.application.service.stats_yearly_sales_user_performance_service import StatsYearlySalesUserPerformanceService

from stats.adapter.out.stats_monthly_sales_user_performance_api_adapter import \
    StatsMonthlySalesUserPerformanceApiAdapter
from stats.application.port.out.stats_monthly_sales_user_performance_out_port import \
    StatsMonthlySalesUserPerformanceOutCrmImpl
from stats.application.port._in.stats_monthly_sales_user_performance_in_port import \
    StatsMonthlySalesUserPerformanceInCrmImpl
from stats.application.service.stats_monthly_sales_user_performance_service import \
    StatsMonthlySalesUserPerformanceService

from stats.adapter.out.stats_daily_sales_user_performance_api_adapter import StatsDailySalesUserPerformanceApiAdapter
from stats.application.port.out.stats_daily_sales_user_performance_out_port import \
    StatsDailySalesUserPerformanceOutCrmImpl
from stats.application.port._in.stats_daily_sales_user_performance_in_port import \
    StatsDailySalesUserPerformanceInCrmImpl
from stats.application.service.stats_daily_sales_user_performance_service import StatsDailySalesUserPerformanceService

from stats.adapter.out.stats_yearly_sales_user_sales_api_adapter import StatsYearlySalesUserSalesApiAdapter
from stats.application.port.out.stats_yearly_sales_user_sales_out_port import StatsYearlySalesUserSalesOutCrmImpl
from stats.application.port._in.stats_yearly_sales_user_sales_in_port import StatsYearlySalesUserSalesInCrmImpl
from stats.application.service.stats_yearly_sales_user_sales_service import StatsYearlySalesUserSalesService

from stats.adapter.out.stats_monthly_sales_user_sales_api_adapter import StatsMonthlySalesUserSalesApiAdapter
from stats.application.port.out.stats_monthly_sales_user_sales_out_port import StatsMonthlySalesUserSalesOutCrmImpl
from stats.application.port._in.stats_monthly_sales_user_sales_in_port import StatsMonthlySalesUserSalesInCrmImpl
from stats.application.service.stats_monthly_sales_user_sales_service import StatsMonthlySalesUserSalesService

from stats.adapter.out.stats_daily_sales_user_sales_api_adapter import StatsDailySalesUserSalesApiAdapter
from stats.application.port.out.stats_daily_sales_user_sales_out_port import StatsDailySalesUserSalesOutCrmImpl
from stats.application.port._in.stats_daily_sales_user_sales_in_port import StatsDailySalesUserSalesInCrmImpl
from stats.application.service.stats_daily_sales_user_sales_service import StatsDailySalesUserSalesService

from stats.adapter.out.stats_yearly_sales_user_order_type_sales_api_adapter import \
    StatsYearlySalesUserOrderTypeSalesApiAdapter
from stats.application.port.out.stats_yearly_sales_user_order_type_sales_out_port import \
    StatsYearlySalesUserOrderTypeSalesOutCrmImpl
from stats.application.port._in.stats_yearly_sales_user_order_type_sales_in_port import \
    StatsYearlySalesUserOrderTypeSalesInCrmImpl
from stats.application.service.stats_yearly_sales_user_order_type_sales_service import \
    StatsYearlySalesUserOrderTypeSalesService

from stats.adapter.out.stats_daily_sales_user_order_type_sales_api_adapter import StatsDailySalesUserOrderTypeSalesApiAdapter
from stats.application.port.out.stats_daily_sales_user_order_type_sales_out_port import StatsDailySalesUserOrderTypeSalesOutCrmImpl
from stats.application.port._in.stats_daily_sales_user_order_type_sales_in_port import StatsDailySalesUserOrderTypeSalesInCrmImpl
from stats.application.service.stats_daily_sales_user_order_type_sales_service import StatsDailySalesUserOrderTypeSalesService

from stats.adapter.out.stats_daily_product_user_performance_api_adapter import \
    StatsDailyProductUserPerformanceApiAdapter
from stats.application.port.out.stats_daily_product_user_performance_out_port import \
    StatsDailyProductUserPerformanceOutCrmImpl
from stats.application.port._in.stats_daily_product_user_performance_in_port import \
    StatsDailyProductUserPerformanceInCrmImpl
from stats.application.service.stats_daily_product_user_performance_service import \
    StatsDailyProductUserPerformanceService

from stats.adapter.out.stats_monthly_product_user_performance_api_adapter import StatsMonthlyProductUserPerformanceApiAdapter
from stats.application.port.out.stats_monthly_product_user_performance_out_port import StatsMonthlyProductUserPerformanceOutCrmImpl
from stats.application.port._in.stats_monthly_product_user_performance_in_port import StatsMonthlyProductUserPerformanceInCrmImpl
from stats.application.service.stats_monthly_product_user_performance_service import StatsMonthlyProductUserPerformanceService

from analysis.adapter.out.analysis_product_sub_user_sales_api_adapter import AnalysisProductSubUserSalesApiAdapter
from analysis.application.port.out.analysis_product_sub_user_sales_out_port import AnalysisProductSubUserSalesOutCrmImpl
from analysis.application.port._in.analysis_product_sub_user_sales_in_port import AnalysisProductSubUserSalesInCrmImpl
from analysis.application.service.analysis_product_sub_user_sales_service import AnalysisProductSubUserSalesService

from analysis.adapter.out.analysis_ticket_user_sales_api_adapter import AnalysisTicketUserSalesApiAdapter
from analysis.application.port.out.analysis_ticket_user_sales_out_port import AnalysisTicketUserSalesOutCrmImpl
from analysis.application.port._in.analysis_ticket_user_sales_in_port import AnalysisTicketUserSalesInCrmImpl
from analysis.application.service.analysis_ticket_user_sales_service import AnalysisTicketUserSalesService

from analysis.adapter.out.analysis_trm_type_user_sales_api_adapter import AnalysisTrmTypeUserSalesApiAdapter
from analysis.application.port.out.analysis_trm_type_user_sales_out_port import AnalysisTrmTypeUserSalesOutCrmImpl
from analysis.application.port._in.analysis_trm_type_user_sales_in_port import AnalysisTrmTypeUserSalesInCrmImpl
from analysis.application.service.analysis_trm_type_user_sales_service import AnalysisTrmTypeUserSalesService

from analysis.adapter.out.analysis_user_product_sales_rank_api_adapter import AnalysisUserProductSalesRankApiAdapter
from analysis.application.port.out.analysis_user_product_sales_rank_out_port import AnalysisUserProductSalesRankOutCrmImpl
from analysis.application.port._in.analysis_user_product_sales_rank_in_port import AnalysisUserProductSalesRankInCrmImpl
from analysis.application.service.analysis_user_product_sales_rank_service import AnalysisUserProductSalesRankService

from analysis.adapter.out.analysis_monthly_cust_type_anlys_api_adapter import AnalysisMonthlyCustTypeAnlysApiAdapter
from analysis.application.port.out.analysis_monthly_cust_type_anlys_out_port import AnalysisMonthlyCustTypeAnlysOutCrmImpl
from analysis.application.port._in.analysis_monthly_cust_type_anlys_in_port import AnalysisMonthlyCustTypeAnlysInCrmImpl
from analysis.application.service.analysis_monthly_cust_type_anlys_service import AnalysisMonthlyCustTypeAnlysService

from analysis.adapter.out.analysis_weekly_cust_type_anlys_api_adapter import AnalysisWeeklyCustTypeAnlysApiAdapter
from analysis.application.port.out.analysis_weekly_cust_type_anlys_out_port import AnalysisWeeklyCustTypeAnlysOutCrmImpl
from analysis.application.port._in.analysis_weekly_cust_type_anlys_in_port import AnalysisWeeklyCustTypeAnlysInCrmImpl
from analysis.application.service.analysis_weekly_cust_type_anlys_service import AnalysisWeeklyCustTypeAnlysService

from analysis.adapter.out.analysis_daily_cust_type_anlys_api_adapter import AnalysisDailyCustTypeAnlysApiAdapter
from analysis.application.port.out.analysis_daily_cust_type_anlys_out_port import AnalysisDailyCustTypeAnlysOutCrmImpl
from analysis.application.port._in.analysis_daily_cust_type_anlys_in_port import AnalysisDailyCustTypeAnlysInCrmImpl
from analysis.application.service.analysis_daily_cust_type_anlys_service import AnalysisDailyCustTypeAnlysService

from analysis.adapter.out.analysis_user_sales_rank_api_adapter import AnalysisUserSalesRankApiAdapter
from analysis.application.port.out.analysis_user_sales_rank_out_port import AnalysisUserSalesRankOutCrmImpl
from analysis.application.port._in.analysis_user_sales_rank_in_port import AnalysisUserSalesRankInCrmImpl
from analysis.application.service.analysis_user_sales_rank_service import AnalysisUserSalesRankService

from analysis.adapter.out.analysis_monthly_synthesis_anlys_api_adapter import AnalysisMonthlySynthesisAnlysApiAdapter
from analysis.application.port.out.analysis_monthly_synthesis_anlys_out_port import AnalysisMonthlySynthesisAnlysOutCrmImpl
from analysis.application.port._in.analysis_monthly_synthesis_anlys_in_port import AnalysisMonthlySynthesisAnlysInCrmImpl
from analysis.application.service.analysis_monthly_synthesis_anlys_service import AnalysisMonthlySynthesisAnlysService

from analysis.adapter.out.analysis_weekly_synthesis_anlys_api_adapter import AnalysisWeeklySynthesisAnlysApiAdapter
from analysis.application.port.out.analysis_weekly_synthesis_anlys_out_port import AnalysisWeeklySynthesisAnlysOutCrmImpl
from analysis.application.port._in.analysis_weekly_synthesis_anlys_in_port import AnalysisWeeklySynthesisAnlysInCrmImpl
from analysis.application.service.analysis_weekly_synthesis_anlys_service import AnalysisWeeklySynthesisAnlysService

from analysis.adapter.out.analysis_daily_synthesis_anlys_api_adapter import AnalysisDailySynthesisAnlysApiAdapter
from analysis.application.port.out.analysis_daily_synthesis_anlys_out_port import AnalysisDailySynthesisAnlysOutCrmImpl
from analysis.application.port._in.analysis_daily_synthesis_anlys_in_port import AnalysisDailySynthesisAnlysInCrmImpl
from analysis.application.service.analysis_daily_synthesis_anlys_service import AnalysisDailySynthesisAnlysService

from analysis.adapter.out.analysis_monthly_cust_membership_anlys_api_adapter import AnalysisMonthlyCustMembershipAnlysApiAdapter
from analysis.application.port.out.analysis_monthly_cust_membership_anlys_out_port import AnalysisMonthlyCustMembershipAnlysOutCrmImpl
from analysis.application.port._in.analysis_monthly_cust_membership_anlys_in_port import AnalysisMonthlyCustMembershipAnlysInCrmImpl
from analysis.application.service.analysis_monthly_cust_membership_anlys_service import AnalysisMonthlyCustMembershipAnlysService

from analysis.adapter.out.analysis_weekly_cust_membership_anlys_api_adapter import \
    AnalysisWeeklyCustMembershipAnlysApiAdapter
from analysis.application.port.out.analysis_weekly_cust_membership_anlys_out_port import \
    AnalysisWeeklyCustMembershipAnlysOutCrmImpl
from analysis.application.port._in.analysis_weekly_cust_membership_anlys_in_port import \
    AnalysisWeeklyCustMembershipAnlysInCrmImpl
from analysis.application.service.analysis_weekly_cust_membership_anlys_service import \
    AnalysisWeeklyCustMembershipAnlysService

from analysis.adapter.out.analysis_daily_cust_membership_anlys_api_adapter import AnalysisDailyCustMembershipAnlysApiAdapter
from analysis.application.port.out.analysis_daily_cust_membership_anlys_out_port import AnalysisDailyCustMembershipAnlysOutCrmImpl
from analysis.application.port._in.analysis_daily_cust_membership_anlys_in_port import AnalysisDailyCustMembershipAnlysInCrmImpl
from analysis.application.service.analysis_daily_cust_membership_anlys_service import AnalysisDailyCustMembershipAnlysService

from analysis.adapter.out.analysis_user_prepaid_sales_rank_api_adapter import AnalysisUserPrepaidSalesRankApiAdapter
from analysis.application.port.out.analysis_user_prepaid_sales_rank_out_port import \
    AnalysisUserPrepaidSalesRankOutCrmImpl
from analysis.application.port._in.analysis_user_prepaid_sales_rank_in_port import AnalysisUserPrepaidSalesRankInCrmImpl
from analysis.application.service.analysis_user_prepaid_sales_rank_service import AnalysisUserPrepaidSalesRankService

from analysis.adapter.out.analysis_monthly_cust_prepaid_anlys_api_adapter import \
    AnalysisMonthlyCustPrepaidAnlysApiAdapter
from analysis.application.port.out.analysis_monthly_cust_prepaid_anlys_out_port import \
    AnalysisMonthlyCustPrepaidAnlysOutCrmImpl
from analysis.application.port._in.analysis_monthly_cust_prepaid_anlys_in_port import \
    AnalysisMonthlyCustPrepaidAnlysInCrmImpl
from analysis.application.service.analysis_monthly_cust_prepaid_anlys_service import \
    AnalysisMonthlyCustPrepaidAnlysService

from analysis.adapter.out.analysis_weekly_cust_prepaid_anlys_api_adapter import AnalysisWeeklyCustPrepaidAnlysApiAdapter
from analysis.application.port.out.analysis_weekly_cust_prepaid_anlys_out_port import AnalysisWeeklyCustPrepaidAnlysOutCrmImpl
from analysis.application.port._in.analysis_weekly_cust_prepaid_anlys_in_port import AnalysisWeeklyCustPrepaidAnlysInCrmImpl
from analysis.application.service.analysis_weekly_cust_prepaid_anlys_service import AnalysisWeeklyCustPrepaidAnlysService

from analysis.adapter.out.analysis_daily_cust_prepaid_anlys_api_adapter import AnalysisDailyCustPrepaidAnlysApiAdapter
from analysis.application.port.out.analysis_daily_cust_prepaid_anlys_out_port import \
    AnalysisDailyCustPrepaidAnlysOutCrmImpl
from analysis.application.port._in.analysis_daily_cust_prepaid_anlys_in_port import \
    AnalysisDailyCustPrepaidAnlysInCrmImpl
from analysis.application.service.analysis_daily_cust_prepaid_anlys_service import AnalysisDailyCustPrepaidAnlysService

class BaseContainer(DeclarativeContainer):
    """
    # Base container.
    ---
    This container stores objects shared by all other containers and objects
    common for all application parts.

    의존성 주입 클래스, 개별 클래스를 직접 호출 하지 않고 인터페이스에 주입해서 사용한다.
    """

    config = Configuration()

    # HRM Login API 의존성 주입
    loginHrmApiAdapterProvider = providers.Singleton(LoginHrmApiAdapter)
    loginOutHrmPortProvider = providers.Singleton(LoginOutHrmAPI, loginHrmApiAdapter=loginHrmApiAdapterProvider)
    loginHrmServiceProvider = providers.Singleton(LoginService, portInImpl=LoginInHrmAPI,
                                                  portOutImpl=loginOutHrmPortProvider)

    # CRM Login API 의존성 주입
    loginCrmApiAdapterProvider = providers.Singleton(LoginCrmApiAdapter)
    loginOutCrmPortProvider = providers.Singleton(LoginOutCrmAPI, loginCrmApiAdapter=loginCrmApiAdapterProvider)
    loginCrmServiceProvider = providers.Singleton(LoginService, portInImpl=LoginInCrmAPI,
                                                  portOutImpl=loginOutCrmPortProvider)
    # CRM Reservation API 의존성 주입
    reservationCrmApiAdapterProvider = providers.Singleton(ReservationApiAdapter)
    reservationOutCrmPortProvider = providers.Singleton(ReservationOutCrmAPI,
                                                        reservationCrmApiAdapter=reservationCrmApiAdapterProvider)
    reservationCrmServiceProvider = providers.Singleton(ReservationService, portInImpl=ReservationInCrmImpl,
                                                        portOutImpl=reservationOutCrmPortProvider)
    # CRM Customer API 의존성 주입
    customerCrmApiAdapterProvider = providers.Singleton(CustomerApiAdapter)
    customerOutCrmPortProvider = providers.Singleton(CustomerOutCrmImpl,
                                                     customerApiAdapter=customerCrmApiAdapterProvider)
    customerCrmServiceProvider = providers.Singleton(CustomerService, portInImpl=CustomerInCrmImpl,
                                                     portOutImpl=customerOutCrmPortProvider)
    # CRM Analysis API 의존성 주입
    analysisCrmApiAdapterProvider = providers.Singleton(AnalysisApiAdapter)
    analysisOutCrmPortProvider = providers.Singleton(AnalysisOutCrmImpl,
                                                     analysisApiAdapter=analysisCrmApiAdapterProvider)
    analysisCrmServiceProvider = providers.Singleton(AnalysisService, portInImpl=AnalysisInCrmImpl,
                                                     portOutImpl=analysisOutCrmPortProvider)

    # HRM Employ API 의존성 주입
    employHrmApiAdapterProvider = providers.Singleton(EmployApiAdapter)
    employOutHrmPortProvider = providers.Singleton(EmployOutHrmImpl,
                                                   employApiAdapter=employHrmApiAdapterProvider)
    employHrmServiceProvider = providers.Singleton(EmployService, portInImpl=EmployInHrmImpl,
                                                   portOutImpl=employOutHrmPortProvider)

    # CRM Order PrepaidInfo API 의존성 주입
    orderPrepaidInfoCrmApiAdapterProvider = providers.Singleton(OrderPrepaidInfoApiAdapter)
    orderPrepaidInfoOutCrmPortProvider = providers.Singleton(OrderPrepaidInfoOutCrmImpl,
                                                             orderPrepaidInfoApiAdapter=orderPrepaidInfoCrmApiAdapterProvider)
    orderPrepaidInfoCrmServiceProvider = providers.Singleton(OrderPrepaidInfoService,
                                                             portInImpl=OrderPrepaidInfoInCrmImpl,
                                                             portOutImpl=orderPrepaidInfoOutCrmPortProvider)

    # CRM OrderTicketList API 의존성 주입
    orderTicketListCrmApiAdapterProvider = providers.Singleton(OrderTicketListApiAdapter)
    orderTicketListOutCrmPortProvider = providers.Singleton(OrderTicketListOutCrmImpl,
                                                            orderTicketListApiAdapter=orderTicketListCrmApiAdapterProvider)
    orderTicketListCrmServiceProvider = providers.Singleton(OrderTicketListService, portInImpl=OrderTicketListInCrmImpl,
                                                            portOutImpl=orderTicketListOutCrmPortProvider)

    # CRM OrderPrepaidHistoryList API 의존성 주입
    orderPrepaidHistoryListCrmApiAdapterProvider = providers.Singleton(OrderPrepaidHistoryListApiAdapter)
    orderPrepaidHistoryListOutCrmPortProvider = providers.Singleton(OrderPrepaidHistoryListOutCrmImpl,
                                                                    orderPrepaidHistoryListApiAdapter=orderPrepaidHistoryListCrmApiAdapterProvider)
    orderPrepaidHistoryListCrmServiceProvider = providers.Singleton(OrderPrepaidHistoryListService,
                                                                    portInImpl=OrderPrepaidHistoryListInCrmImpl,
                                                                    portOutImpl=orderPrepaidHistoryListOutCrmPortProvider)

    # CRM OrderTicketHistoryList API 의존성 주입
    orderTicketHistoryListCrmApiAdapterProvider = providers.Singleton(OrderTicketHistoryListApiAdapter)
    orderTicketHistoryListOutCrmPortProvider = providers.Singleton(OrderTicketHistoryListOutCrmImpl,
                                                                   orderTicketHistoryListApiAdapter=orderTicketHistoryListCrmApiAdapterProvider)
    orderTicketHistoryListCrmServiceProvider = providers.Singleton(OrderTicketHistoryListService,
                                                                   portInImpl=OrderTicketHistoryListInCrmImpl,
                                                                   portOutImpl=orderTicketHistoryListOutCrmPortProvider)

    # CRM CustomerCustMemoList API 의존성 주입
    customerCustMemoListCrmApiAdapterProvider = providers.Singleton(CustomerCustMemoListApiAdapter)
    customerCustMemoListOutCrmPortProvider = providers.Singleton(CustomerCustMemoListOutCrmImpl,
                                                                 customerCustMemoListApiAdapter=customerCustMemoListCrmApiAdapterProvider)
    customerCustMemoListCrmServiceProvider = providers.Singleton(CustomerCustMemoListService,
                                                                 portInImpl=CustomerCustMemoListInCrmImpl,
                                                                 portOutImpl=customerCustMemoListOutCrmPortProvider)

    # CRM CustomerCustTasteList API 의존성 주입
    customerCustTasteListCrmApiAdapterProvider = providers.Singleton(CustomerCustTasteListApiAdapter)
    customerCustTasteListOutCrmPortProvider = providers.Singleton(CustomerCustTasteListOutCrmImpl,
                                                                  customerCustTasteListApiAdapter=customerCustTasteListCrmApiAdapterProvider)
    customerCustTasteListCrmServiceProvider = providers.Singleton(CustomerCustTasteListService,
                                                                  portInImpl=CustomerCustTasteListInCrmImpl,
                                                                  portOutImpl=customerCustTasteListOutCrmPortProvider)

    # CRM CustomerModifyCustInfo API 의존성 주입
    customerModifyCustInfoCrmApiAdapterProvider = providers.Singleton(CustomerModifyCustInfoApiAdapter)
    customerModifyCustInfoOutCrmPortProvider = providers.Singleton(CustomerModifyCustInfoOutCrmImpl,
                                                                   customerModifyCustInfoApiAdapter=customerModifyCustInfoCrmApiAdapterProvider)
    customerModifyCustInfoCrmServiceProvider = providers.Singleton(CustomerModifyCustInfoService,
                                                                   portInImpl=CustomerModifyCustInfoInCrmImpl,
                                                                   portOutImpl=customerModifyCustInfoOutCrmPortProvider)

    # CRM OrderVisitHistoryList API 의존성 주입
    orderVisitHistoryListCrmApiAdapterProvider = providers.Singleton(OrderVisitHistoryListApiAdapter)
    orderVisitHistoryListOutCrmPortProvider = providers.Singleton(OrderVisitHistoryListOutCrmImpl,
                                                                  orderVisitHistoryListApiAdapter=orderVisitHistoryListCrmApiAdapterProvider)
    orderVisitHistoryListCrmServiceProvider = providers.Singleton(OrderVisitHistoryListService,
                                                                  portInImpl=OrderVisitHistoryListInCrmImpl,
                                                                  portOutImpl=orderVisitHistoryListOutCrmPortProvider)

    # CRM OrderVisitHistoryDetail API 의존성 주입
    orderVisitHistoryDetailCrmApiAdapterProvider = providers.Singleton(OrderVisitHistoryDetailApiAdapter)
    orderVisitHistoryDetailOutCrmPortProvider = providers.Singleton(OrderVisitHistoryDetailOutCrmImpl,
                                                                    orderVisitHistoryDetailApiAdapter=orderVisitHistoryDetailCrmApiAdapterProvider)
    orderVisitHistoryDetailCrmServiceProvider = providers.Singleton(OrderVisitHistoryDetailService,
                                                                    portInImpl=OrderVisitHistoryDetailInCrmImpl,
                                                                    portOutImpl=orderVisitHistoryDetailOutCrmPortProvider)

    # CRM AnalysisProductUserSales API 의존성 주입
    analysisProductUserSalesCrmApiAdapterProvider = providers.Singleton(AnalysisProductUserSalesApiAdapter)
    analysisProductUserSalesOutCrmPortProvider = providers.Singleton(AnalysisProductUserSalesOutCrmImpl,
                                                                     analysisProductUserSalesApiAdapter=analysisProductUserSalesCrmApiAdapterProvider)
    analysisProductUserSalesCrmServiceProvider = providers.Singleton(AnalysisProductUserSalesService,
                                                                     portInImpl=AnalysisProductUserSalesInCrmImpl,
                                                                     portOutImpl=analysisProductUserSalesOutCrmPortProvider)

    # CRM AnalysisPrepaidUserSales API 의존성 주입
    analysisPrepaidUserSalesCrmApiAdapterProvider = providers.Singleton(AnalysisPrepaidUserSalesApiAdapter)
    analysisPrepaidUserSalesOutCrmPortProvider = providers.Singleton(AnalysisPrepaidUserSalesOutCrmImpl,
                                                                     analysisPrepaidUserSalesApiAdapter=analysisPrepaidUserSalesCrmApiAdapterProvider)
    analysisPrepaidUserSalesCrmServiceProvider = providers.Singleton(AnalysisPrepaidUserSalesService,
                                                                     portInImpl=AnalysisPrepaidUserSalesInCrmImpl,
                                                                     portOutImpl=analysisPrepaidUserSalesOutCrmPortProvider)

    # CRM AnalysisDashBoardInfo API 의존성 주입
    analysisDashBoardInfoCrmApiAdapterProvider = providers.Singleton(AnalysisDashBoardInfoApiAdapter)
    analysisDashBoardInfoOutCrmPortProvider = providers.Singleton(AnalysisDashBoardInfoOutCrmImpl,
                                                                  analysisDashBoardInfoApiAdapter=analysisDashBoardInfoCrmApiAdapterProvider)
    analysisDashBoardInfoCrmServiceProvider = providers.Singleton(AnalysisDashBoardInfoService,
                                                                  portInImpl=AnalysisDashBoardInfoInCrmImpl,
                                                                  portOutImpl=analysisDashBoardInfoOutCrmPortProvider)

    # CRM StatsYearlySalesUserPerformance API 의존성 주입
    statsYearlySalesUserPerformanceCrmApiAdapterProvider = providers.Singleton(
        StatsYearlySalesUserPerformanceApiAdapter)
    statsYearlySalesUserPerformanceOutCrmPortProvider = providers.Singleton(StatsYearlySalesUserPerformanceOutCrmImpl,
                                                                            statsYearlySalesUserPerformanceApiAdapter=statsYearlySalesUserPerformanceCrmApiAdapterProvider)
    statsYearlySalesUserPerformanceCrmServiceProvider = providers.Singleton(StatsYearlySalesUserPerformanceService,
                                                                            portInImpl=StatsYearlySalesUserPerformanceInCrmImpl,
                                                                            portOutImpl=statsYearlySalesUserPerformanceOutCrmPortProvider)

    # CRM StatsMonthlySalesUserPerformance API 의존성 주입
    statsMonthlySalesUserPerformanceCrmApiAdapterProvider = providers.Singleton(
        StatsMonthlySalesUserPerformanceApiAdapter)
    statsMonthlySalesUserPerformanceOutCrmPortProvider = providers.Singleton(StatsMonthlySalesUserPerformanceOutCrmImpl,
                                                                             statsMonthlySalesUserPerformanceApiAdapter=statsMonthlySalesUserPerformanceCrmApiAdapterProvider)
    statsMonthlySalesUserPerformanceCrmServiceProvider = providers.Singleton(StatsMonthlySalesUserPerformanceService,
                                                                             portInImpl=StatsMonthlySalesUserPerformanceInCrmImpl,
                                                                             portOutImpl=statsMonthlySalesUserPerformanceOutCrmPortProvider)

    # CRM StatsDailySalesUserPerformance API 의존성 주입
    statsDailySalesUserPerformanceCrmApiAdapterProvider = providers.Singleton(StatsDailySalesUserPerformanceApiAdapter)
    statsDailySalesUserPerformanceOutCrmPortProvider = providers.Singleton(StatsDailySalesUserPerformanceOutCrmImpl,
                                                                           statsDailySalesUserPerformanceApiAdapter=statsDailySalesUserPerformanceCrmApiAdapterProvider)
    statsDailySalesUserPerformanceCrmServiceProvider = providers.Singleton(StatsDailySalesUserPerformanceService,
                                                                           portInImpl=StatsDailySalesUserPerformanceInCrmImpl,
                                                                           portOutImpl=statsDailySalesUserPerformanceOutCrmPortProvider)

    # CRM StatsYearlySalesUserSales API 의존성 주입
    statsYearlySalesUserSalesCrmApiAdapterProvider = providers.Singleton(StatsYearlySalesUserSalesApiAdapter)
    statsYearlySalesUserSalesOutCrmPortProvider = providers.Singleton(StatsYearlySalesUserSalesOutCrmImpl,
                                                                      statsYearlySalesUserSalesApiAdapter=statsYearlySalesUserSalesCrmApiAdapterProvider)
    statsYearlySalesUserSalesCrmServiceProvider = providers.Singleton(StatsYearlySalesUserSalesService,
                                                                      portInImpl=StatsYearlySalesUserSalesInCrmImpl,
                                                                      portOutImpl=statsYearlySalesUserSalesOutCrmPortProvider)

    # CRM StatsMonthlySalesUserSales API 의존성 주입
    statsMonthlySalesUserSalesCrmApiAdapterProvider = providers.Singleton(StatsMonthlySalesUserSalesApiAdapter)
    statsMonthlySalesUserSalesOutCrmPortProvider = providers.Singleton(StatsMonthlySalesUserSalesOutCrmImpl,
                                                                       statsMonthlySalesUserSalesApiAdapter=statsMonthlySalesUserSalesCrmApiAdapterProvider)
    statsMonthlySalesUserSalesCrmServiceProvider = providers.Singleton(StatsMonthlySalesUserSalesService,
                                                                       portInImpl=StatsMonthlySalesUserSalesInCrmImpl,
                                                                       portOutImpl=statsMonthlySalesUserSalesOutCrmPortProvider)

    # CRM StatsDailySalesUserSales API 의존성 주입
    statsDailySalesUserSalesCrmApiAdapterProvider = providers.Singleton(StatsDailySalesUserSalesApiAdapter)
    statsDailySalesUserSalesOutCrmPortProvider = providers.Singleton(StatsDailySalesUserSalesOutCrmImpl,
                                                                     statsDailySalesUserSalesApiAdapter=statsDailySalesUserSalesCrmApiAdapterProvider)
    statsDailySalesUserSalesCrmServiceProvider = providers.Singleton(StatsDailySalesUserSalesService,
                                                                     portInImpl=StatsDailySalesUserSalesInCrmImpl,
                                                                     portOutImpl=statsDailySalesUserSalesOutCrmPortProvider)

    # CRM StatsYearlySalesUserOrderTypeSales API 의존성 주입
    statsYearlySalesUserOrderTypeSalesCrmApiAdapterProvider = providers.Singleton(
        StatsYearlySalesUserOrderTypeSalesApiAdapter)
    statsYearlySalesUserOrderTypeSalesOutCrmPortProvider = providers.Singleton(
        StatsYearlySalesUserOrderTypeSalesOutCrmImpl,
        statsYearlySalesUserOrderTypeSalesApiAdapter=statsYearlySalesUserOrderTypeSalesCrmApiAdapterProvider)
    statsYearlySalesUserOrderTypeSalesCrmServiceProvider = providers.Singleton(
        StatsYearlySalesUserOrderTypeSalesService, portInImpl=StatsYearlySalesUserOrderTypeSalesInCrmImpl,
        portOutImpl=statsYearlySalesUserOrderTypeSalesOutCrmPortProvider)

    # CRM StatsDailySalesUserOrderTypeSales API 의존성 주입
    statsDailySalesUserOrderTypeSalesCrmApiAdapterProvider = providers.Singleton(
        StatsDailySalesUserOrderTypeSalesApiAdapter)
    statsDailySalesUserOrderTypeSalesOutCrmPortProvider = providers.Singleton(
        StatsDailySalesUserOrderTypeSalesOutCrmImpl,
        statsDailySalesUserOrderTypeSalesApiAdapter=statsDailySalesUserOrderTypeSalesCrmApiAdapterProvider)
    statsDailySalesUserOrderTypeSalesCrmServiceProvider = providers.Singleton(StatsDailySalesUserOrderTypeSalesService,
                                                                              portInImpl=StatsDailySalesUserOrderTypeSalesInCrmImpl,
                                                                              portOutImpl=statsDailySalesUserOrderTypeSalesOutCrmPortProvider)

    # CRM StatsDailyProductUserPerformance API 의존성 주입
    statsDailyProductUserPerformanceCrmApiAdapterProvider = providers.Singleton(
        StatsDailyProductUserPerformanceApiAdapter)
    statsDailyProductUserPerformanceOutCrmPortProvider = providers.Singleton(StatsDailyProductUserPerformanceOutCrmImpl,
                                                                             statsDailyProductUserPerformanceApiAdapter=statsDailyProductUserPerformanceCrmApiAdapterProvider)
    statsDailyProductUserPerformanceCrmServiceProvider = providers.Singleton(StatsDailyProductUserPerformanceService,
                                                                             portInImpl=StatsDailyProductUserPerformanceInCrmImpl,
                                                                             portOutImpl=statsDailyProductUserPerformanceOutCrmPortProvider)

    # CRM StatsMonthlyProductUserPerformance API 의존성 주입
    statsMonthlyProductUserPerformanceCrmApiAdapterProvider = providers.Singleton(StatsMonthlyProductUserPerformanceApiAdapter)
    statsMonthlyProductUserPerformanceOutCrmPortProvider = providers.Singleton(StatsMonthlyProductUserPerformanceOutCrmImpl,
                                                                               statsMonthlyProductUserPerformanceApiAdapter=statsMonthlyProductUserPerformanceCrmApiAdapterProvider)
    statsMonthlyProductUserPerformanceCrmServiceProvider = providers.Singleton(StatsMonthlyProductUserPerformanceService, portInImpl=StatsMonthlyProductUserPerformanceInCrmImpl,
                                                                               portOutImpl=statsMonthlyProductUserPerformanceOutCrmPortProvider)

    # CRM AnalysisProductSubUserSales API 의존성 주입
    analysisProductSubUserSalesCrmApiAdapterProvider = providers.Singleton(AnalysisProductSubUserSalesApiAdapter)
    analysisProductSubUserSalesOutCrmPortProvider = providers.Singleton(AnalysisProductSubUserSalesOutCrmImpl,
                                                                        analysisProductSubUserSalesApiAdapter=analysisProductSubUserSalesCrmApiAdapterProvider)
    analysisProductSubUserSalesCrmServiceProvider = providers.Singleton(AnalysisProductSubUserSalesService,
                                                                        portInImpl=AnalysisProductSubUserSalesInCrmImpl,
                                                                        portOutImpl=analysisProductSubUserSalesOutCrmPortProvider)

    # CRM AnalysisTicketUserSales API 의존성 주입
    analysisTicketUserSalesCrmApiAdapterProvider = providers.Singleton(AnalysisTicketUserSalesApiAdapter)
    analysisTicketUserSalesOutCrmPortProvider = providers.Singleton(AnalysisTicketUserSalesOutCrmImpl,
                                                                    analysisTicketUserSalesApiAdapter=analysisTicketUserSalesCrmApiAdapterProvider)
    analysisTicketUserSalesCrmServiceProvider = providers.Singleton(AnalysisTicketUserSalesService, portInImpl=AnalysisTicketUserSalesInCrmImpl,
                                                                    portOutImpl=analysisTicketUserSalesOutCrmPortProvider)

    # CRM AnalysisTrmTypeUserSales API 의존성 주입
    analysisTrmTypeUserSalesCrmApiAdapterProvider = providers.Singleton(AnalysisTrmTypeUserSalesApiAdapter)
    analysisTrmTypeUserSalesOutCrmPortProvider = providers.Singleton(AnalysisTrmTypeUserSalesOutCrmImpl,
                                                                     analysisTrmTypeUserSalesApiAdapter=analysisTrmTypeUserSalesCrmApiAdapterProvider)
    analysisTrmTypeUserSalesCrmServiceProvider = providers.Singleton(AnalysisTrmTypeUserSalesService,
                                                                     portInImpl=AnalysisTrmTypeUserSalesInCrmImpl,
                                                                     portOutImpl=analysisTrmTypeUserSalesOutCrmPortProvider)

    # CRM AnalysisUserProductSalesRank API 의존성 주입
    analysisUserProductSalesRankCrmApiAdapterProvider = providers.Singleton(AnalysisUserProductSalesRankApiAdapter)
    analysisUserProductSalesRankOutCrmPortProvider = providers.Singleton(AnalysisUserProductSalesRankOutCrmImpl,
                                                                         analysisUserProductSalesRankApiAdapter=analysisUserProductSalesRankCrmApiAdapterProvider)
    analysisUserProductSalesRankCrmServiceProvider = providers.Singleton(AnalysisUserProductSalesRankService,
                                                                         portInImpl=AnalysisUserProductSalesRankInCrmImpl,
                                                                         portOutImpl=analysisUserProductSalesRankOutCrmPortProvider)

    # CRM AnalysisMonthlyCustTypeAnlys API 의존성 주입
    analysisMonthlyCustTypeAnlysCrmApiAdapterProvider = providers.Singleton(AnalysisMonthlyCustTypeAnlysApiAdapter)
    analysisMonthlyCustTypeAnlysOutCrmPortProvider = providers.Singleton(AnalysisMonthlyCustTypeAnlysOutCrmImpl,
                                                                         analysisMonthlyCustTypeAnlysApiAdapter=analysisMonthlyCustTypeAnlysCrmApiAdapterProvider)
    analysisMonthlyCustTypeAnlysCrmServiceProvider = providers.Singleton(AnalysisMonthlyCustTypeAnlysService,
                                                                         portInImpl=AnalysisMonthlyCustTypeAnlysInCrmImpl,
                                                                         portOutImpl=analysisMonthlyCustTypeAnlysOutCrmPortProvider)

    # CRM AnalysisWeeklyCustTypeAnlys API 의존성 주입
    analysisWeeklyCustTypeAnlysCrmApiAdapterProvider = providers.Singleton(AnalysisWeeklyCustTypeAnlysApiAdapter)
    analysisWeeklyCustTypeAnlysOutCrmPortProvider = providers.Singleton(AnalysisWeeklyCustTypeAnlysOutCrmImpl,
                                                                        analysisWeeklyCustTypeAnlysApiAdapter=analysisWeeklyCustTypeAnlysCrmApiAdapterProvider)
    analysisWeeklyCustTypeAnlysCrmServiceProvider = providers.Singleton(AnalysisWeeklyCustTypeAnlysService, portInImpl=AnalysisWeeklyCustTypeAnlysInCrmImpl,
                                                                        portOutImpl=analysisWeeklyCustTypeAnlysOutCrmPortProvider)

    # CRM AnalysisDailyCustTypeAnlys API 의존성 주입
    analysisDailyCustTypeAnlysCrmApiAdapterProvider = providers.Singleton(AnalysisDailyCustTypeAnlysApiAdapter)
    analysisDailyCustTypeAnlysOutCrmPortProvider = providers.Singleton(AnalysisDailyCustTypeAnlysOutCrmImpl,
                                                                       analysisDailyCustTypeAnlysApiAdapter=analysisDailyCustTypeAnlysCrmApiAdapterProvider)
    analysisDailyCustTypeAnlysCrmServiceProvider = providers.Singleton(AnalysisDailyCustTypeAnlysService,
                                                                       portInImpl=AnalysisDailyCustTypeAnlysInCrmImpl,
                                                                       portOutImpl=analysisDailyCustTypeAnlysOutCrmPortProvider)

    # CRM AnalysisUserSalesRank API 의존성 주입
    analysisUserSalesRankCrmApiAdapterProvider = providers.Singleton(AnalysisUserSalesRankApiAdapter)
    analysisUserSalesRankOutCrmPortProvider = providers.Singleton(AnalysisUserSalesRankOutCrmImpl,
                                                                  analysisUserSalesRankApiAdapter=analysisUserSalesRankCrmApiAdapterProvider)
    analysisUserSalesRankCrmServiceProvider = providers.Singleton(AnalysisUserSalesRankService, portInImpl=AnalysisUserSalesRankInCrmImpl,
                                                                  portOutImpl=analysisUserSalesRankOutCrmPortProvider)

    # CRM AnalysisMonthlySynthesisAnlys API 의존성 주입
    analysisMonthlySynthesisAnlysCrmApiAdapterProvider = providers.Singleton(AnalysisMonthlySynthesisAnlysApiAdapter)
    analysisMonthlySynthesisAnlysOutCrmPortProvider = providers.Singleton(AnalysisMonthlySynthesisAnlysOutCrmImpl,
                                                                          analysisMonthlySynthesisAnlysApiAdapter=analysisMonthlySynthesisAnlysCrmApiAdapterProvider)
    analysisMonthlySynthesisAnlysCrmServiceProvider = providers.Singleton(AnalysisMonthlySynthesisAnlysService,
                                                                          portInImpl=AnalysisMonthlySynthesisAnlysInCrmImpl,
                                                                          portOutImpl=analysisMonthlySynthesisAnlysOutCrmPortProvider)

    # CRM AnalysisWeeklySynthesisAnlys API 의존성 주입
    analysisWeeklySynthesisAnlysCrmApiAdapterProvider = providers.Singleton(AnalysisWeeklySynthesisAnlysApiAdapter)
    analysisWeeklySynthesisAnlysOutCrmPortProvider = providers.Singleton(AnalysisWeeklySynthesisAnlysOutCrmImpl,
                                                                         analysisWeeklySynthesisAnlysApiAdapter=analysisWeeklySynthesisAnlysCrmApiAdapterProvider)
    analysisWeeklySynthesisAnlysCrmServiceProvider = providers.Singleton(AnalysisWeeklySynthesisAnlysService, portInImpl=AnalysisWeeklySynthesisAnlysInCrmImpl,
                                                                         portOutImpl=analysisWeeklySynthesisAnlysOutCrmPortProvider)

    # CRM AnalysisDailySynthesisAnlys API 의존성 주입
    analysisDailySynthesisAnlysCrmApiAdapterProvider = providers.Singleton(AnalysisDailySynthesisAnlysApiAdapter)
    analysisDailySynthesisAnlysOutCrmPortProvider = providers.Singleton(AnalysisDailySynthesisAnlysOutCrmImpl,
                                                                        analysisDailySynthesisAnlysApiAdapter=analysisDailySynthesisAnlysCrmApiAdapterProvider)
    analysisDailySynthesisAnlysCrmServiceProvider = providers.Singleton(AnalysisDailySynthesisAnlysService,
                                                                        portInImpl=AnalysisDailySynthesisAnlysInCrmImpl,
                                                                        portOutImpl=analysisDailySynthesisAnlysOutCrmPortProvider)

    # CRM AnalysisMonthlyCustMembershipAnlys API 의존성 주입
    analysisMonthlyCustMembershipAnlysCrmApiAdapterProvider = providers.Singleton(
        AnalysisMonthlyCustMembershipAnlysApiAdapter)
    analysisMonthlyCustMembershipAnlysOutCrmPortProvider = providers.Singleton(
        AnalysisMonthlyCustMembershipAnlysOutCrmImpl,
        analysisMonthlyCustMembershipAnlysApiAdapter=analysisMonthlyCustMembershipAnlysCrmApiAdapterProvider)
    analysisMonthlyCustMembershipAnlysCrmServiceProvider = providers.Singleton(
        AnalysisMonthlyCustMembershipAnlysService, portInImpl=AnalysisMonthlyCustMembershipAnlysInCrmImpl,
        portOutImpl=analysisMonthlyCustMembershipAnlysOutCrmPortProvider)

    # CRM AnalysisWeeklyCustMembershipAnlys API 의존성 주입
    analysisWeeklyCustMembershipAnlysCrmApiAdapterProvider = providers.Singleton(
        AnalysisWeeklyCustMembershipAnlysApiAdapter)
    analysisWeeklyCustMembershipAnlysOutCrmPortProvider = providers.Singleton(
        AnalysisWeeklyCustMembershipAnlysOutCrmImpl,
        analysisWeeklyCustMembershipAnlysApiAdapter=analysisWeeklyCustMembershipAnlysCrmApiAdapterProvider)
    analysisWeeklyCustMembershipAnlysCrmServiceProvider = providers.Singleton(AnalysisWeeklyCustMembershipAnlysService,
                                                                              portInImpl=AnalysisWeeklyCustMembershipAnlysInCrmImpl,
                                                                              portOutImpl=analysisWeeklyCustMembershipAnlysOutCrmPortProvider)

    # CRM AnalysisDailyCustMembershipAnlys API 의존성 주입
    analysisDailyCustMembershipAnlysCrmApiAdapterProvider = providers.Singleton(AnalysisDailyCustMembershipAnlysApiAdapter)
    analysisDailyCustMembershipAnlysOutCrmPortProvider = providers.Singleton(AnalysisDailyCustMembershipAnlysOutCrmImpl,
                                                                             analysisDailyCustMembershipAnlysApiAdapter=analysisDailyCustMembershipAnlysCrmApiAdapterProvider)
    analysisDailyCustMembershipAnlysCrmServiceProvider = providers.Singleton(AnalysisDailyCustMembershipAnlysService, portInImpl=AnalysisDailyCustMembershipAnlysInCrmImpl,
                                                                             portOutImpl=analysisDailyCustMembershipAnlysOutCrmPortProvider)

    # CRM AnalysisUserPrepaidSalesRank API 의존성 주입
    analysisUserPrepaidSalesRankCrmApiAdapterProvider = providers.Singleton(AnalysisUserPrepaidSalesRankApiAdapter)
    analysisUserPrepaidSalesRankOutCrmPortProvider = providers.Singleton(AnalysisUserPrepaidSalesRankOutCrmImpl,
                                                                         analysisUserPrepaidSalesRankApiAdapter=analysisUserPrepaidSalesRankCrmApiAdapterProvider)
    analysisUserPrepaidSalesRankCrmServiceProvider = providers.Singleton(AnalysisUserPrepaidSalesRankService,
                                                                         portInImpl=AnalysisUserPrepaidSalesRankInCrmImpl,
                                                                         portOutImpl=analysisUserPrepaidSalesRankOutCrmPortProvider)

    # CRM AnalysisMonthlyCustPrepaidAnlys API 의존성 주입
    analysisMonthlyCustPrepaidAnlysCrmApiAdapterProvider = providers.Singleton(
        AnalysisMonthlyCustPrepaidAnlysApiAdapter)
    analysisMonthlyCustPrepaidAnlysOutCrmPortProvider = providers.Singleton(AnalysisMonthlyCustPrepaidAnlysOutCrmImpl,
                                                                            analysisMonthlyCustPrepaidAnlysApiAdapter=analysisMonthlyCustPrepaidAnlysCrmApiAdapterProvider)
    analysisMonthlyCustPrepaidAnlysCrmServiceProvider = providers.Singleton(AnalysisMonthlyCustPrepaidAnlysService,
                                                                            portInImpl=AnalysisMonthlyCustPrepaidAnlysInCrmImpl,
                                                                            portOutImpl=analysisMonthlyCustPrepaidAnlysOutCrmPortProvider)

    # CRM AnalysisWeeklyCustPrepaidAnlys API 의존성 주입
    analysisWeeklyCustPrepaidAnlysCrmApiAdapterProvider = providers.Singleton(AnalysisWeeklyCustPrepaidAnlysApiAdapter)
    analysisWeeklyCustPrepaidAnlysOutCrmPortProvider = providers.Singleton(AnalysisWeeklyCustPrepaidAnlysOutCrmImpl,
                                                                           analysisWeeklyCustPrepaidAnlysApiAdapter=analysisWeeklyCustPrepaidAnlysCrmApiAdapterProvider)
    analysisWeeklyCustPrepaidAnlysCrmServiceProvider = providers.Singleton(AnalysisWeeklyCustPrepaidAnlysService,
                                                                           portInImpl=AnalysisWeeklyCustPrepaidAnlysInCrmImpl,
                                                                           portOutImpl=analysisWeeklyCustPrepaidAnlysOutCrmPortProvider)

    # CRM AnalysisDailyCustPrepaidAnlys API 의존성 주입
    analysisDailyCustPrepaidAnlysCrmApiAdapterProvider = providers.Singleton(AnalysisDailyCustPrepaidAnlysApiAdapter)
    analysisDailyCustPrepaidAnlysOutCrmPortProvider = providers.Singleton(AnalysisDailyCustPrepaidAnlysOutCrmImpl,
                                                                          analysisDailyCustPrepaidAnlysApiAdapter=analysisDailyCustPrepaidAnlysCrmApiAdapterProvider)
    analysisDailyCustPrepaidAnlysCrmServiceProvider = providers.Singleton(AnalysisDailyCustPrepaidAnlysService,
                                                                          portInImpl=AnalysisDailyCustPrepaidAnlysInCrmImpl,
                                                                          portOutImpl=analysisDailyCustPrepaidAnlysOutCrmPortProvider)
