from ..port._in.employ_user_apnt_list_in_port import EmployUserApntListInPort
from ..port.out.employ_user_apnt_list_out_port import EmployUserApntListOutPort
import config.utils.common_utils as common_utils
from django.conf import settings
import logging

logger = logging.getLogger("django.server")


class EmployUserApntListService:
    """
    # CLASS : EmployUserApntListService
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/09 3:39 PM
    # DESCRIPTION
        - UserApntList Service

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/09          jung-gyuho          최초 생성
    """

    def __init__(self, portInImpl: EmployUserApntListInPort, portOutImpl: EmployUserApntListOutPort):
        self.employIn = portInImpl
        self.employOut = portOutImpl

    def employ_user_apnt_list_hrm(self, *args, **kwargs):
        print(f"{self.__class__.__name__} employ_user_apnt_list_hrm *args ==> {args[0]}")

        data = self.employIn.employ_in_port(self, args[0])

        for arg in args:
            print(f"{self.__class__.__name__} employ_user_apnt_list_hrm *args ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} employ_user_apnt_list_hrm **kwargs ==> {kwarg}")

        API_HOST = getattr(settings, "HRM_HOST_IP", None)
        API_PORT = getattr(settings, "HRM_HOST_PORT", None)
        API_ADR = API_HOST + ":" + API_PORT
        print(f"Api host ==> {API_HOST}")
        result = self.employOut.employ_out_port(self, API_ADR, "/emply/getUserApntList/", "POST", data,
                                                accessToken=kwargs['accessToken'],
                                                refreshToken=kwargs['refreshToken'])

        jtOResult = common_utils.convert_json_to_obj(result['data'])
        # print(f"{self.__class__.__name__} : analysis_trm_type_user_sales_hrm get result ==> {result}")
        # print(f"{self.__class__.__name__} : analysis_trm_type_user_sales_hrm get jResult ==> {jtOResult}")
        logger.info(f"{self.__class__.__name__} : analysis_trm_type_user_sales_hrm get jResult ==> {jtOResult}")

        return jtOResult
