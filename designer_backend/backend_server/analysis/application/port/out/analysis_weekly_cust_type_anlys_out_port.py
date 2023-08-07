from abc import ABC, abstractmethod

from ....adapter.out.analysis_weekly_cust_type_anlys_api_adapter import AnalysisWeeklyCustTypeAnlysApiAdapter


class AnalysisWeeklyCustTypeAnlysOutPort(ABC):
    """
    # CLASS : AnalysisWeeklyCustTypeAnlysOutPort
    # AUTHOR : jung-gyuho
    # TIME : 2023/08/07 6:21 PM
    # DESCRIPTION
        - WeeklyCustTypeAnlys Out Port
    =============================================
    DATE            AUTHOR          NOTE
    ---------------------------------------------
    2023/08/07          jung-gyuho          최초 생성
    """

    @abstractmethod
    def analysis_out_port(self, request):
        pass


class AnalysisWeeklyCustTypeAnlysOutCrmImpl(AnalysisWeeklyCustTypeAnlysOutPort):

    def __init__(self, analysisWeeklyCustTypeAnlysApiAdapter: AnalysisWeeklyCustTypeAnlysApiAdapter):
        self.analysisWeeklyCustTypeAnlysApiAdapter = analysisWeeklyCustTypeAnlysApiAdapter

    def analysis_out_port(self, *args, **kwargs):
        print(f"{self.__class__.__name__} analysis_out_port args ==> {args[1]}")

        for arg in args:
            print(f"{self.__class__.__name__} : analysis_out_port get arg ==> {arg}")

        for kwarg in kwargs:
            print(f"{self.__class__.__name__} : analysis_out_port get kwarg ==> {kwarg}")

        result = self.analysisWeeklyCustTypeAnlysApiAdapter.analysis_weekly_cust_type_anlys_crm_api(api_host=args[1],
                                                                                                    path=args[2],
                                                                                                    method=args[3],
                                                                                                    data=args[4],
                                                                                                    accessToken=kwargs[
                                                                                                        'accessToken'],
                                                                                                    refreshToken=kwargs[
                                                                                                        'refreshToken'])

        return result
