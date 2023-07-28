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

