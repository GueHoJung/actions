from ..port._in.employ_in_port import EmployInPort
from ..port.out.employ_out_port import EmployOutPort
import config.utils.common_utils as common_utils
from django.conf import settings


class EmployService:
    """
    # CLASS : EmployService
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/28 6:07 PM
    # DESCRIPTION
        - 분석 관련 Service

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/28          jung-gyuho          최초 생성
    """

    def __init__(self, portInImpl: EmployInPort, portOutImpl: EmployOutPort):
        self.employIn = portInImpl
        self.employOut = portOutImpl

    def employ_apnt_list_hrm(self, *args, **kwargs):
        print(f"{self.__class__.__name__} employ_apnt_list_hrm *args ==> {args[0]}")

        data = self.employIn.employ_in_port(self, args[0])

        for arg in args:
            print(f"{self.__class__.__name__} employ_apnt_list_hrm *args ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} employ_apnt_list_hrm **kwargs ==> {kwarg}")

        API_HOST = getattr(settings, "HRM_HOST_IP", None)
        API_PORT = getattr(settings, "HRM_HOST_PORT", None)
        API_ADR = API_HOST + ":" + API_PORT
        print(f"Api host ==> {API_HOST}")
        result = self.employOut.employ_out_port(self, API_ADR, "/emply/getUserApntList/", "POST", data,
                                                accessToken=kwargs['accessToken'],
                                                refreshToken=kwargs['refreshToken'])

        jtOResult = common_utils.convert_json_to_obj(result['data'])
        print(f"{self.__class__.__name__} : employ_apnt_list_hrm get result ==> {result}")
        print(f"{self.__class__.__name__} : employ_apnt_list_hrm get jResult ==> {jtOResult}")

        return jtOResult
