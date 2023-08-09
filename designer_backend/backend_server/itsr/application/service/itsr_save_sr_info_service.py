from ..port._in.itsr_save_sr_info_in_port import ItsrSaveSrInfoInPort
from ..port.out.itsr_save_sr_info_out_port import ItsrSaveSrInfoOutPort
import config.utils.common_utils as common_utils
from django.conf import settings
import logging

logger = logging.getLogger("django.server")


class ItsrSaveSrInfoService:
    """
    # CLASS : ItsrSaveSrInfoService
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/09 2:43 PM
    # DESCRIPTION
        - SaveSrInfo Service

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/09          jung-gyuho          최초 생성
    """

    def __init__(self, portInImpl: ItsrSaveSrInfoInPort, portOutImpl: ItsrSaveSrInfoOutPort):
        self.itsrIn = portInImpl
        self.itsrOut = portOutImpl

    def itsr_save_sr_info_crm(self, *args, **kwargs):
        print(f"{self.__class__.__name__} itsr_save_sr_info_crm *args ==> {args[0]}")

        data = self.itsrIn.itsr_in_port(self, args[0])

        for arg in args:
            print(f"{self.__class__.__name__} itsr_save_sr_info_crm *args ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} itsr_save_sr_info_crm **kwargs ==> {kwarg}")

        API_HOST = getattr(settings, "CRM_HOST_IP", None)
        API_PORT = getattr(settings, "CRM_HOST_PORT", None)
        API_ADR = API_HOST + ":" + API_PORT
        print(f"Api host ==> {API_HOST}")
        result = self.itsrOut.itsr_out_port(self, API_ADR, "/itsr/saveSrInfo/", "POST", data,
                                            accessToken=kwargs['accessToken'],
                                            refreshToken=kwargs['refreshToken'])

        jtOResult = common_utils.convert_json_to_obj(result['data'])
        # print(f"{self.__class__.__name__} : analysis_trm_type_user_sales_crm get result ==> {result}")
        # print(f"{self.__class__.__name__} : analysis_trm_type_user_sales_crm get jResult ==> {jtOResult}")
        logger.info(f"{self.__class__.__name__} : analysis_trm_type_user_sales_crm get jResult ==> {jtOResult}")

        return jtOResult
