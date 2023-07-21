from ..port._in.login_in_port import LoginInPort
from ..port.out.login_out_port import LoginOutPort
from ...util.utils import convert_json_to_obj


class LoginService:

    def __init__(self, portInImpl: LoginInPort, portOutImpl: LoginOutPort):
        self.loginInHRM = portInImpl
        self.loginOutHRM = portOutImpl

    def login_hrm(self, *args, **kwargs):
        print(f"LoginHRMService login_hrm *args ==> {args[0]}")

        request = self.loginInHRM.login_in_port(self, args[0])
        result = self.loginOutHRM.login_out_port(self, request)

        jResult = convert_json_to_obj(result)
        print(f"LoginHRMService : login_hrm get result ==> {result}")
        print(f"LoginHRMService : login_hrm get jResult ==> {jResult}")

        return result
