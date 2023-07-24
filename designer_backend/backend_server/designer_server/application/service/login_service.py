from ..port._in.login_in_port import LoginInPort
from ..port.out.login_out_port import LoginOutPort
import config.utils.common_utils as CommontUtils
from django.conf import settings


class LoginService:

    def __init__(self, portInImpl: LoginInPort, portOutImpl: LoginOutPort):
        self.loginIn = portInImpl
        self.loginOut = portOutImpl

    def login_hrm(self, *args, **kwargs):
        print(f"{self.__class__.__name__} login_hrm *args ==> {args[0]}")

        request = self.loginIn.login_in_port(self, args[0])

        API_HOST = getattr(settings, "CRM_HOST_IP", None)
        API_PORT = getattr(settings, "CRM_HOST_PORT", None)
        API_ADR = API_HOST + ":" + API_PORT
        print(f"Api adr ==> {API_ADR}")

        result = self.loginOut.login_out_port(self, API_ADR, "/login/login/", "POST", request)

        jtOResult = CommontUtils.convert_json_to_obj(result)
        print(f"{self.__class__.__name__} : login_hrm get result ==> {result}")
        print(f"{self.__class__.__name__} : login_hrm get jResult ==> {jtOResult}")

        return jtOResult

    def login_crm(self, *args, **kwargs):
        print(f"{self.__class__.__name__} login_crm *args ==> {args[0]}")

        request = self.loginIn.login_in_port(self, args[0])

        API_HOST = getattr(settings, "CRM_HOST_IP", None)
        API_PORT = getattr(settings, "CRM_HOST_PORT", None)
        API_ADR = API_HOST + ":" + API_PORT
        print(f"Api host ==> {API_HOST}")

        result = self.loginOut.login_out_port(self, API_ADR, "/login/login/", "POST", request)

        print(f"{self.__class__.__name__} : login_crm get result ==> {result}")

        jtOResult = CommontUtils.convert_json_to_obj(result['data'])

        if result.get('accessToken'):
            jtOResult['accessToken'] = result['accessToken']

        if result.get('refreshToken'):
            jtOResult['refreshToken'] = result['refreshToken']

        print(f"{self.__class__.__name__} : login_crm get jtOResult ==> {jtOResult}")

        return jtOResult
