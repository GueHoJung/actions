from ..port._in.login_in_port import LoginInPort
from ..port.out.login_out_port import LoginOutPort
import config.utils.common_utils as CommontUtils


class LoginService:

    def __init__(self, portInImpl: LoginInPort, portOutImpl: LoginOutPort):
        self.loginIn = portInImpl
        self.loginOut = portOutImpl

    def login_hrm(self, *args, **kwargs):
        print(f"LoginHRMService login_hrm *args ==> {args[0]}")

        request = self.loginIn.login_in_port(self, args[0])
        result = self.loginOut.login_out_port(self, request)

        jtOResult = CommontUtils.convert_json_to_obj(result)
        print(f"LoginHrmService : login_hrm get result ==> {result}")
        print(f"LoginHrmService : login_hrm get jResult ==> {jtOResult}")

        return jtOResult

    def login_crm(self, *args, **kwargs):
        print(f"LoginCrmService login_crm *args ==> {args[0]}")

        request = self.loginIn.login_in_port(self, args[0])
        result = self.loginOut.login_out_port(self, request)

        jtOResult = CommontUtils.convert_json_to_obj(result)
        print(f"LoginCrmService : login_crm get result ==> {result}")
        print(f"LoginCrmService : login_crm get jtOResult ==> {jtOResult}")

        return jtOResult
