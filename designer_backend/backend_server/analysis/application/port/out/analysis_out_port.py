from abc import ABC, abstractmethod

from ....adapter.out.analysis_api_adapter import AnalysisApiAdapter


class AnalysisOutPort(ABC):
    """
    # CLASS : AnalysisOutPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/07/27 7:04 PM
    # DESCRIPTION
        - 분석 관련 Out Port
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/07/27          jung-gyuho          최초 생성
    """

    @abstractmethod
    def analysis_out_port(self, request):
        pass


class AnalysisOutCrmImpl(AnalysisOutPort):

    def __init__(self, analysisApiAdapter: AnalysisApiAdapter):
        self.analysisApiAdapter = analysisApiAdapter

    def analysis_out_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} analysis_out_port args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : analysis_out_port get arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : analysis_out_port get kwarg ==> {kwarg}")

        result = self.analysisApiAdapter.analysis_cust_detail_crm_api(api_host=args[1], path=args[2],
                                                                      method=args[3],
                                                                      data=args[4], accessToken=kwargs['accessToken'],
                                                                      refreshToken=kwargs['refreshToken'])

        return result
