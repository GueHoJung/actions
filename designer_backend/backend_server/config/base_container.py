from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, Singleton

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

from customer.application.service.customer_service import CustomerService
from customer.application.port.out.customer_out_port import CustomerOutCrmImpl
from customer.application.port._in.customer_in_port import CustomerInCrmImpl
from customer.adapter.out.customer_api_adapter import CustomerApiAdapter

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
                                                     customerCrmApiAdapter=customerCrmApiAdapterProvider)
    customerCrmServiceProvider = providers.Singleton(CustomerService, portInImpl=CustomerInCrmImpl,
                                                     portOutImpl=customerOutCrmPortProvider)
