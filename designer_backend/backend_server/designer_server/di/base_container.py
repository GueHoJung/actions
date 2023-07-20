# from dependency_injector import providers
# from dependency_injector.containers import DeclarativeContainer
# from dependency_injector.providers import Configuration, Singleton
#
# from ..application.port._in.login_hrm_in_port import LoginHRMInAPI
# from ..application.service.login_hrm_service import LoginHRMService
# class BaseContainer(DeclarativeContainer):
#     """Base container."""
#
#     config = Configuration()
#
#     loginHRMInPortProvider = providers.Singleton(LoginHRMInAPI)
#
#     loginHRMServiceProvider = providers.Singleton(LoginHRMService, portImpl="serviceImpl")
#
#
#
# if __name__ == "__main__":
#     container = BaseContainer()
#
#     loginHRMServiceProvider = container.loginHRMServiceProvider()
