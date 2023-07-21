from abc import ABC, abstractmethod

from designer_server.adapter.out.login_api_adapter import LoginApiAdapter


class LoginOutPort(ABC):
    @abstractmethod
    def login_out_port(self, request):
        pass


class LoginOutHRMAPI(LoginOutPort):

    def __init__(self, loginHrmApiAdapter: LoginApiAdapter):
        self.loginHrmApiAdapter = loginHrmApiAdapter

    def login_out_port(self, *args, **kwargs):
        print(f"LoginHRMOutAPI login_out_port args ==> {args[1]}")

        result = self.loginHrmApiAdapter.login_hrm_api(path="/login/login/", method="POST", data=args[1])

        return result
