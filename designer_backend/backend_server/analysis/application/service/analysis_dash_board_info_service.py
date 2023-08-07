from ..port._in.analysis_dash_board_info_in_port import AnalysisDashBoardInfoInPort
from ..port.out.analysis_dash_board_info_out_port import AnalysisDashBoardInfoOutPort
import config.utils.common_utils as common_utils
from django.conf import settings


class AnalysisDashBoardInfoService:
    """
    # CLASS : AnalysisDashBoardInfoService
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/31 5:01 PM
    # DESCRIPTION
        - DashBoardInfo Service

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/31          jung-gyuho          최초 생성
    """

    def __init__(self, portInImpl: AnalysisDashBoardInfoInPort, portOutImpl: AnalysisDashBoardInfoOutPort):
        self.analysisIn = portInImpl
        self.analysisOut = portOutImpl

    def analysis_dash_board_info_crm(self, *args, **kwargs):
        print(f"{self.__class__.__name__} analysis_dash_board_info_crm *args ==> {args[0]}")

        data = self.analysisIn.analysis_in_port(self, args[0])

        for arg in args:
            print(f"{self.__class__.__name__} analysis_dash_board_info_crm *args ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} analysis_dash_board_info_crm **kwargs ==> {kwarg}")

        API_HOST = getattr(settings, "CRM_HOST_IP", None)
        API_PORT = getattr(settings, "CRM_HOST_PORT", None)
        API_ADR = API_HOST + ":" + API_PORT
        print(f"Api host ==> {API_HOST}")
        result = self.analysisOut.analysis_out_port(self, API_ADR, "/analysis/getDashBoardInfo/", "POST", data,
                                                    accessToken=kwargs['accessToken'],
                                                    refreshToken=kwargs['refreshToken'])

        jtOResult = common_utils.convert_json_to_obj(result['data'])
        print(f"{self.__class__.__name__} : analysis_dash_board_info_crm get result ==> {result}")
        print(f"{self.__class__.__name__} : analysis_dash_board_info_crm get jResult ==> {jtOResult}")

        return jtOResult
