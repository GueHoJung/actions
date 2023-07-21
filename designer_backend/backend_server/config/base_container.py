from dependency_injector import providers
from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Configuration, Singleton

from designer_server.application.service.login_service import LoginService
from designer_server.application.port._in.login_in_port import LoginInHRMAPI
from designer_server.application.port.out.login_out_port import LoginOutHRMAPI
from designer_server.adapter.out.login_api_adapter import LoginApiAdapter


class BaseContainer(DeclarativeContainer):
    """
    # Base container.
    ---
    This container stores objects shared by all other containers and objects
    common for all application parts.

    의존성 주입 클래스, 개별 클래스를 직접 호출 하지 않고 인터페이스에 주입해서 사용한다.
    """

    config = Configuration()

    # Login API 의존성 주입
    loginHRMApiAdapterProvider = providers.Singleton(LoginApiAdapter)
    # HRM Login API 의존성 주입
    loginOutHRMPortProvider = providers.Singleton(LoginOutHRMAPI, loginHrmApiAdapter=loginHRMApiAdapterProvider)
    loginHRMServiceProvider = providers.Singleton(LoginService, portInImpl= LoginInHRMAPI, portOutImpl= loginOutHRMPortProvider)

    # CRM Login API 의존성 주입





if __name__ == "__main__":
    container = BaseContainer()

    loginHRMServiceProvider = container.loginHRMServiceProvider()
