from abc import ABC, abstractmethod

from ....adapter.out.login_hrm_api_adapter import LoginHrmApiAdapter
from ....adapter.out.login_crm_api_adapter import LoginCrmApiAdapter


class LoginOutPort(ABC):
    @abstractmethod
    def login_out_port(self, request):
        pass


class LoginOutHrmAPI(LoginOutPort):

    def __init__(self, loginHrmApiAdapter: LoginHrmApiAdapter):
        self.loginHrmApiAdapter = loginHrmApiAdapter

    def login_out_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} login_out_port args ==> {args[1]}")

        result = self.loginHrmApiAdapter.login_hrm_api(path="/login/login/", method="POST", data=args[1])

        return result


class LoginOutCrmAPI(LoginOutPort):

    def __init__(self, loginCrmApiAdapter: LoginCrmApiAdapter):
        self.loginCrmApiAdapter = loginCrmApiAdapter

    def login_out_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} login_out_port args ==> {args[1]}")

        for args in args:
            print(f"{self.__class__.__name__} login_out_port get args ==> {args}")

        result = self.loginCrmApiAdapter.login_crm_api(api_host=args[1], path=args[2], method=args[3], data=args[4])

        return result
