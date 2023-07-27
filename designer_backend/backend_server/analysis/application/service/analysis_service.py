from ..port._in.analysis_in_port import AnalysisInPort
from ..port.out.analysis_out_port import AnalysisOutPort
import config.utils.common_utils as common_utils
from django.conf import settings


class AnalysisService:
    """
    # CLASS : AnalysisService
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/27 7:00 PM
    # DESCRIPTION
        - 분석 관련 Service

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/27          jung-gyuho          최초 생성
    """

    def __init__(self, portInImpl: AnalysisInPort, portOutImpl: AnalysisOutPort):
        self.analysisIn = portInImpl
        self.analysisOut = portOutImpl

    def analysis_cust_detail_crm(self, *args, **kwargs):
        print(f"{self.__class__.__name__} analysis_cust_detail_crm *args ==> {args[0]}")

        data = self.analysisIn.analysis_in_port(self, args[0])

        for arg in args:
            print(f"{self.__class__.__name__} analysis_cust_detail_crm *args ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} analysis_cust_detail_crm **kwargs ==> {kwarg}")

        API_HOST = getattr(settings, "CRM_HOST_IP", None)
        API_PORT = getattr(settings, "CRM_HOST_PORT", None)
        API_ADR = API_HOST + ":" + API_PORT
        print(f"Api host ==> {API_HOST}")
        result = self.analysisOut.analysis_out_port(self, API_ADR, "/analysis/getCustDetailAnlys/", "POST", data,
                                                    accessToken=kwargs['accessToken'],
                                                    refreshToken=kwargs['refreshToken'])

        jtOResult = common_utils.convert_json_to_obj(result['data'])
        print(f"{self.__class__.__name__} : analysis_cust_detail_crm get result ==> {result}")
        print(f"{self.__class__.__name__} : analysis_cust_detail_crm get jResult ==> {jtOResult}")

        return jtOResult
