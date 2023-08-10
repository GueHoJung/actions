from ..port._in.analysis_user_growth_rate_rank_in_port import AnalysisUserGrowthRateRankInPort
from ..port.out.analysis_user_growth_rate_rank_out_port import AnalysisUserGrowthRateRankOutPort
import config.utils.common_utils as common_utils
from django.conf import settings
import logging

logger = logging.getLogger("django.server")


class AnalysisUserGrowthRateRankService:
    """
    # CLASS : AnalysisUserGrowthRateRankService
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/08 7:16 PM
    # DESCRIPTION
        - UserGrowthRateRank Service

    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/08          jung-gyuho          최초 생성
    """

    def __init__(self, portInImpl: AnalysisUserGrowthRateRankInPort, portOutImpl: AnalysisUserGrowthRateRankOutPort):
        self.analysisIn = portInImpl
        self.analysisOut = portOutImpl

    def analysis_user_growth_rate_rank_crm(self, *args, **kwargs):
        print(f"{self.__class__.__name__} analysis_user_growth_rate_rank_crm *args ==> {args[0]}")

        data = self.analysisIn.analysis_in_port(self, args[0])

        for arg in args:
            print(f"{self.__class__.__name__} analysis_user_growth_rate_rank_crm *args ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} analysis_user_growth_rate_rank_crm **kwargs ==> {kwarg}")

        API_HOST = getattr(settings, "CRM_HOST_IP", None)
        API_PORT = getattr(settings, "CRM_HOST_PORT", None)
        API_ADR = API_HOST + ":" + API_PORT
        print(f"Api host ==> {API_HOST}")
        result = self.analysisOut.analysis_out_port(self, API_ADR, "/analysis/getUserGrowthRateRank/", "POST", data,
                                                    accessToken=kwargs['accessToken'],
                                                    refreshToken=kwargs['refreshToken'])

        jtOResult = common_utils.convert_json_to_obj(result['data'])
        # print(f"{self.__class__.__name__} : analysis_trm_type_user_sales_crm get result ==> {result}")
        # print(f"{self.__class__.__name__} : analysis_trm_type_user_sales_crm get jResult ==> {jtOResult}")
        logger.info(f"{self.__class__.__name__} : analysis_trm_type_user_sales_crm get jResult ==> {jtOResult}")

        return jtOResult
