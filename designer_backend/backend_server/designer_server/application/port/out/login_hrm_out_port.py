from abc import ABC, abstractmethod

from designer_backend.backend_server.designer_server.adapter.out.login_hrm_api_adapter import LoginHrmApiAdapter


class LoginOutPort(ABC):
    @abstractmethod
    def login_hrm_out(self, request):
        pass

class LoginHRMOutAPI(LoginOutPort):
    def login_hrm_out(self, request):
        print(f"LoginHRMAPI login_hrm_in request ==> {request}")

        result = LoginHrmApiAdapter().login_hrm_api(path="/login/login/", method="POST", data=request.data)

        return result
